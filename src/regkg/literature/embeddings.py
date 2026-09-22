"""Selected-model passage embeddings behind one query/document interface (plan §6.4.1).

Ollama uses `langchain_ollama.OllamaEmbeddings`; Sentence Transformers uses
`langchain_huggingface.HuggingFaceEmbeddings`. SDKs are imported only when their backend is built.
Neither adapter exposes a no-truncation flag (Ollama silently cuts input at the model context;
Sentence Transformers cuts at max_seq_length). An `EncodingContract` is therefore derived from the
selected model before any request and every input, including queries, is checked against it:

- Ollama with a WordPiece (`bert`) tokenizer: each token spans >= 1 character, so an input of at
  most (context - special tokens) characters cannot be truncated. Other tokenizers are refused.
- Sentence Transformers: inputs are counted with the model's own tokenizer against max_seq_length.

An input over the bound raises an error; nothing is silently truncated. Passages are chunked at
sentence boundaries to `max_chunk_chars` and a passage scores by its best chunk.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Protocol

import numpy as np
import pandas as pd

from regkg.config import EmbeddingSection, ModelSettings, SelectionStatus
from regkg.provenance import canonical_json

DENSE_NOT_CONFIGURED = "not_configured"
DENSE_DISABLED = "disabled"
DENSE_OK = "ok"
DENSE_FAILED = "configured_backend_failed"
SENTENCE_END = re.compile(r"(?<=[.!?;])\s+")


class EmbeddingSetupError(RuntimeError):
    """The selected embedding backend cannot be constructed (missing extra, bad endpoint, bad model)."""


class EmbeddingInputError(ValueError):
    """An input exceeds the validated encoding contract; it is rejected rather than truncated."""


@dataclass
class EncodingContract:
    backend: str
    method: str  # wordpiece_char_bound | tokenizer_token_count
    context_tokens: int
    special_tokens: int
    max_input_chars: int | None  # wordpiece_char_bound only
    max_input_tokens: int | None  # tokenizer_token_count only
    prefix_policy: str
    validated: list[str]
    token_counter: Any = None  # callable(text) -> tokens including special tokens

    def check(self, text: str) -> int:
        """Size of `text` under this contract (chars or tokens); raises when it could be truncated."""
        if self.method == "wordpiece_char_bound":
            if len(text) > self.max_input_chars:
                raise EmbeddingInputError(f"input of {len(text)} chars exceeds the {self.max_input_chars}-char bound")
            return len(text)
        tokens = int(self.token_counter(text))
        if tokens > self.max_input_tokens:
            raise EmbeddingInputError(f"input of {tokens} tokens exceeds max_seq_length {self.max_input_tokens}")
        return tokens

    def to_record(self) -> dict[str, Any]:
        record = asdict(self)
        record.pop("token_counter")
        return record


def ollama_contract(metadata: dict[str, Any], section: EmbeddingSection) -> EncodingContract:
    """Character bound valid only for a WordPiece tokenizer with known context and special tokens."""
    context, tokenizer, special = (
        metadata.get("context_length"),
        metadata.get("tokenizer_model"),
        metadata.get("special_tokens"),
    )
    if tokenizer != "bert" or not isinstance(context, int) or special is None:
        raise EmbeddingSetupError(
            f"cannot verify a no-truncation bound for tokenizer {tokenizer!r} (context {context}); unsupported model"
        )
    bound = context - special
    if section.max_chunk_chars > bound:
        raise EmbeddingSetupError(
            f"embeddings.max_chunk_chars={section.max_chunk_chars} exceeds the verified bound {bound} "
            f"(context {context} tokens - {special} special tokens, >=1 char per WordPiece token)"
        )
    return EncodingContract(
        "ollama",
        "wordpiece_char_bound",
        context,
        special,
        section.max_chunk_chars,
        None,
        "raw text for queries and documents; the Ollama template is {{ .Prompt }} and no prefix is documented",
        [
            "tokenizer.ggml.model == bert (WordPiece)",
            f"context_length == {context}",
            f"special tokens (CLS/SEP) == {special}",
            f"max_chunk_chars {section.max_chunk_chars} <= {bound}",
        ],
    )


def sentence_transformer_contract(client: Any, section: EmbeddingSection) -> EncodingContract:
    model = getattr(client, "_client", None)
    limit, tokenizer = getattr(model, "max_seq_length", None), getattr(model, "tokenizer", None)
    if not isinstance(limit, int) or tokenizer is None:
        raise EmbeddingSetupError("Sentence Transformers model exposes no max_seq_length/tokenizer; unsupported")

    def count(text: str) -> int:
        return len(tokenizer(text, add_special_tokens=True)["input_ids"])

    special = count("") if callable(tokenizer) else 0
    return EncodingContract(
        "sentence_transformers",
        "tokenizer_token_count",
        limit,
        special,
        None,
        limit,
        "raw text; configure prompts explicitly if the selected model requires them",
        [f"max_seq_length == {limit}", "inputs counted with the model tokenizer incl. special tokens"],
        count,
    )


class Embeddings(Protocol):
    def embed_query(self, text: str) -> list[float]: ...

    def embed_documents(self, texts: list[str]) -> list[list[float]]: ...


@dataclass
class EmbeddingBackend:
    selector: str
    provider: str
    model_name: str
    client: Embeddings
    identity: dict[str, Any]  # nonsecret model identity used in cache keys and manifests
    contract: EncodingContract | None = None

    @property
    def vector_identity(self) -> dict[str, Any]:
        """Only what determines a vector for a given input text (not metadata, contract, or endpoint)."""
        keys = ("selector", "digest", "revision", "encoding", "normalize")
        return {key: self.identity[key] for key in keys if key in self.identity}

    @property
    def cache_id(self) -> str:
        return hashlib.sha256(canonical_json(self.vector_identity).encode()).hexdigest()[:16]


def ollama_model_metadata(base_url: str, model_name: str) -> dict[str, Any]:
    """Actual model metadata from the local Ollama server (digest, dimensions, context, pooling)."""
    import httpx

    try:
        tags = httpx.get(f"{base_url}/api/tags", timeout=20).json()
        show = httpx.post(f"{base_url}/api/show", json={"model": model_name}, timeout=20).json()
        version = httpx.get(f"{base_url}/api/version", timeout=20).json().get("version")
    except (httpx.HTTPError, ValueError) as error:
        raise EmbeddingSetupError(f"Ollama at {base_url} is unreachable or invalid: {type(error).__name__}") from error
    entry = next((m for m in tags.get("models", []) if m.get("name") == model_name), None)
    if entry is None:
        raise EmbeddingSetupError(f"model {model_name!r} is not installed on Ollama at {base_url}; not downloading it")
    info = show.get("model_info") or {}
    architecture = info.get("general.architecture", "")
    special = sum(info.get(f"tokenizer.ggml.{name}_token_id") is not None for name in ("cls", "seperator"))
    return {
        "digest": entry.get("digest"),
        "size_bytes": entry.get("size"),
        "ollama_version": version,
        "format": (entry.get("details") or {}).get("format"),
        "quantization": (entry.get("details") or {}).get("quantization_level"),
        "architecture": architecture,
        "parameter_count": info.get("general.parameter_count"),
        "embedding_length": info.get(f"{architecture}.embedding_length"),
        "context_length": info.get(f"{architecture}.context_length"),
        # llama.cpp pooling enum: 0 none, 1 mean, 2 cls, 3 last, 4 rank.
        "pooling_type": info.get(f"{architecture}.pooling_type"),
        "tokenizer_model": info.get("tokenizer.ggml.model"),
        "special_tokens": special if special else None,
        "template": show.get("template"),
        "capabilities": show.get("capabilities"),
        "license_first_line": (show.get("license") or "").strip().splitlines()[0:1],
    }


def build_embeddings(settings: ModelSettings, section: EmbeddingSection) -> EmbeddingBackend | None:
    """The configured backend, or None when embeddings are disabled or no model is configured."""
    selection = settings.embeddings
    if selection.status is not SelectionStatus.CONFIGURED:
        return None
    spec = selection.spec
    if spec.provider == "ollama":
        try:
            from langchain_ollama import OllamaEmbeddings
        except ImportError as error:
            raise EmbeddingSetupError("Ollama embeddings need the 'embeddings-ollama' extra") from error
        metadata = ollama_model_metadata(settings.ollama_base_url, spec.model_name)
        contract = ollama_contract(metadata, section)  # validated before any encoding request
        client = OllamaEmbeddings(model=spec.model_name, base_url=settings.ollama_base_url)
        identity = {
            "selector": spec.selector,
            "digest": metadata["digest"],
            "max_chunk_chars": section.max_chunk_chars,
            "encoding": "raw_text_no_prefix",
        }
        return EmbeddingBackend(
            spec.selector,
            "ollama",
            spec.model_name,
            client,
            {**identity, "endpoint": settings.ollama_base_url, "metadata": metadata, "contract": contract.to_record()},
            contract,
        )
    if spec.provider == "sentence_transformers":
        try:
            from langchain_huggingface import HuggingFaceEmbeddings
        except ImportError as error:
            raise EmbeddingSetupError(
                "Sentence Transformers embeddings need the 'embeddings-sentence-transformers' extra"
            ) from error
        model_kwargs = {
            key: value for key, value in (("device", section.device), ("revision", section.revision)) if value
        }
        client = HuggingFaceEmbeddings(
            model_name=spec.model_name, model_kwargs=model_kwargs, encode_kwargs={"normalize_embeddings": True}
        )
        contract = sentence_transformer_contract(client, section)
        identity = {
            "selector": spec.selector,
            "revision": section.revision,
            "max_chunk_chars": section.max_chunk_chars,
            "encoding": "raw_text_no_prefix",
            "normalize": True,
            "contract": contract.to_record(),
        }
        return EmbeddingBackend(spec.selector, "sentence_transformers", spec.model_name, client, identity, contract)
    raise EmbeddingSetupError(f"unsupported embedding provider {spec.provider!r}")


def chunk_text(text: str, max_chars: int) -> list[str]:
    """Sentence-boundary chunks of at most max_chars; an overlong sentence is split at whitespace."""
    pieces: list[str] = []
    for sentence in SENTENCE_END.split(text):
        while len(sentence) > max_chars:
            cut = sentence.rfind(" ", 0, max_chars)
            cut = cut if cut > 0 else max_chars
            pieces.append(sentence[:cut].strip())
            sentence = sentence[cut:].strip()
        if sentence:
            pieces.append(sentence)
    chunks: list[str] = []
    for piece in pieces:
        if chunks and len(chunks[-1]) + 1 + len(piece) <= max_chars:
            chunks[-1] = f"{chunks[-1]} {piece}"
        else:
            chunks.append(piece)
    return chunks or [text[:max_chars]]


def _validate(vectors: np.ndarray, expected_dim: int | None) -> None:
    if vectors.ndim != 2 or vectors.shape[1] == 0 or not np.isfinite(vectors).all():
        raise EmbeddingSetupError("embedding backend returned empty or non-finite vectors")
    if expected_dim is not None and vectors.shape[1] != expected_dim:
        raise EmbeddingSetupError(f"vector dimension {vectors.shape[1]} differs from model metadata {expected_dim}")


class VectorStore:
    """Chunk vectors cached by (backend identity, chunk SHA-256); replay issues no embedding request."""

    def __init__(self, root: Path, backend: EmbeddingBackend) -> None:
        self.directory = root / backend.cache_id
        self.backend = backend
        self.directory.mkdir(parents=True, exist_ok=True)
        (self.directory / "store.json").write_text(canonical_json(backend.vector_identity) + "\n", encoding="utf-8")
        self.vectors: dict[str, np.ndarray] = {}
        self.requests = 0
        self.sizes: list[int] = []
        self.query_sizes: list[int] = []
        for shard in sorted(self.directory.glob("vectors-*.parquet")):
            frame = pd.read_parquet(shard)
            for sha, vector in zip(frame["chunk_sha256"], frame["vector"], strict=True):
                self.vectors[sha] = np.asarray(vector, dtype=np.float32)

    def encode(self, texts: list[str], batch_size: int, expected_dim: int | None) -> dict[str, np.ndarray]:
        keyed = {hashlib.sha256(t.encode("utf-8")).hexdigest(): t for t in texts}
        for text in keyed.values():  # every input is checked before the first request
            self.sizes.append(self.backend.contract.check(text) if self.backend.contract else len(text))
        missing = [sha for sha in sorted(keyed) if sha not in self.vectors]
        new: dict[str, np.ndarray] = {}
        for start in range(0, len(missing), batch_size):
            batch = missing[start : start + batch_size]
            vectors = np.asarray(self.backend.client.embed_documents([keyed[s] for s in batch]), dtype=np.float32)
            self.requests += 1
            _validate(vectors, expected_dim)
            new.update(zip(batch, vectors, strict=True))
            if len(new) >= 4096:  # persist progress so an interrupted large encode resumes from the cache
                self._persist(new)
                new = {}
        if new:
            self._persist(new)
        return {sha: self.vectors[sha] for sha in keyed}

    def embed_query(self, text: str, expected_dim: int | None) -> np.ndarray:
        # The model documents no query prefix, so queries are raw text like documents; they are
        # encoded through the interface's embed_query and cached under a separate key space.
        sha = hashlib.sha256(f"query\0{text}".encode()).hexdigest()
        self.query_sizes.append(self.backend.contract.check(text) if self.backend.contract else len(text))
        if sha not in self.vectors:
            vector = np.asarray([self.backend.client.embed_query(text)], dtype=np.float32)
            self.requests += 1
            _validate(vector, expected_dim)
            self._persist({sha: vector[0]})
        return self.vectors[sha]

    def _persist(self, new: dict[str, np.ndarray]) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256("".join(sorted(new)).encode()).hexdigest()[:16]
        shard = self.directory / f"vectors-{digest}.parquet"
        frame = pd.DataFrame({"chunk_sha256": list(new), "vector": [v.tolist() for v in new.values()]})
        temporary = shard.with_name(f".{shard.name}.tmp")
        frame.to_parquet(temporary, index=False)
        temporary.replace(shard)
        self.vectors.update(new)
