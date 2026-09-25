"""Project configuration, model selectors, and `.env`/process/YAML resolution.

Nothing here imports a model SDK, opens a connection, or requires a credential.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Literal
from urllib.parse import urlsplit

import yaml
from dotenv import dotenv_values
from pydantic import BaseModel, ConfigDict, Field, model_validator

from regkg.models import InputMode


class ConfigError(ValueError):
    """Invalid or inconsistent configuration."""


class StrictModel(BaseModel):
    """Unknown fields are rejected instead of silently ignored."""

    model_config = ConfigDict(extra="forbid", frozen=True)


# ---------------------------------------------------------------------------
# configs/project.yaml


class ConditionConfig(StrictModel):
    # Control is an experimental condition, not a diagnosis; its disease stays null.
    disease: str | None


class DatasetConfig(StrictModel):
    name: str
    species: str
    ncbi_taxon_id: int
    tissue: str
    model_system: str
    conditions: dict[str, ConditionConfig]


class ChromLinkerSourceConfig(StrictModel):
    path: Path
    delimiter: str
    tf_column: str
    target_column: str
    score_label: str


class ExpressionSourceConfig(StrictModel):
    path: Path
    delimiter: str
    gene_column: str
    value_unit: str


class SignatureSourceConfig(StrictModel):
    path: Path
    delimiter: str


class NicheDefinitionConfig(StrictModel):
    focal_cell_type: str
    neighborhood_path: Path
    delimiter: str
    niche_column: str
    k_neighbors: int = Field(gt=0)
    clustering_resolution: float = Field(gt=0)
    conditions_pooled: list[str]
    method: str


class CellTypeConfig(StrictModel):
    display_name: str
    ontology_id: str | None = None


class ScopeConfig(StrictModel):
    cell_type: str
    tf_seeds: list[str]


class TolerancesConfig(StrictModel):
    signature_effect_abs: float = Field(ge=0)
    signature_effect_rel: float = Field(ge=0)
    neighborhood_row_sum: float = Field(ge=0)


class ProjectConfig(StrictModel):
    schema_version: int
    input_mode: InputMode
    data_root: Path
    ingest_chunk_rows: int = Field(gt=0)
    dataset: DatasetConfig
    chromlinker: ChromLinkerSourceConfig
    expression: ExpressionSourceConfig
    niche_expression_signatures: SignatureSourceConfig
    niche_definitions: list[NicheDefinitionConfig]
    cell_types: dict[str, CellTypeConfig]
    at1_scope: ScopeConfig
    tolerances: TolerancesConfig

    @model_validator(mode="after")
    def _consistent(self) -> ProjectConfig:
        focal = [d.focal_cell_type for d in self.niche_definitions]
        if len(set(focal)) != len(focal):
            raise ValueError("each focal cell type may have only one niche definition run")
        for definition in self.niche_definitions:
            if definition.focal_cell_type not in self.cell_types:
                raise ValueError(f"niche definition cell type lacks a display entry: {definition.focal_cell_type}")
            unknown = set(definition.conditions_pooled) - set(self.dataset.conditions)
            if unknown:
                raise ValueError(f"unknown pooled conditions for {definition.focal_cell_type}: {sorted(unknown)}")
        if self.at1_scope.cell_type not in self.cell_types:
            raise ValueError(f"scope cell type is not configured: {self.at1_scope.cell_type}")
        return self


@dataclass(frozen=True)
class LoadedProjectConfig:
    config: ProjectConfig
    config_path: Path
    repo_root: Path

    def resolve(self, relative: Path) -> Path:
        return relative if relative.is_absolute() else self.repo_root / relative

    @property
    def data_root(self) -> Path:
        return self.resolve(self.config.data_root)


def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "pyproject.toml").is_file():
            return candidate
    raise ConfigError(f"no repository root (pyproject.toml) above {start}")


def read_yaml(path: Path) -> dict[str, Any]:
    try:
        content = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ConfigError(f"configuration file not found: {path}") from error
    if content is None:
        return {}
    if not isinstance(content, dict):
        raise ConfigError(f"configuration root must be a mapping: {path}")
    return content


def load_project_config(path: Path, repo_root: Path | None = None) -> LoadedProjectConfig:
    """Load project.yaml; relative source paths resolve against the repository root, not the CWD."""
    path = path.resolve()
    root = (repo_root or find_repo_root(path.parent)).resolve()
    try:
        config = ProjectConfig.model_validate(read_yaml(path))
    except ValueError as error:
        raise ConfigError(f"invalid project configuration {path}: {error}") from error
    return LoadedProjectConfig(config=config, config_path=path, repo_root=root)


# ---------------------------------------------------------------------------
# Model selectors: "{provider}:{model_name}", split at the first colon only.


class ModelRole(StrEnum):
    CHAT = "chat"
    EMBEDDING = "embedding"


PROVIDER_ROLES: dict[str, ModelRole] = {
    "litellm": ModelRole.CHAT,
    "openrouter": ModelRole.CHAT,
    "groq": ModelRole.CHAT,
    "ollama": ModelRole.EMBEDDING,
    "sentence_transformers": ModelRole.EMBEDDING,
}
PROVIDER_ALIASES = {"sentence-transformers": "sentence_transformers"}


class ModelSelectorError(ConfigError):
    """A supplied selector is malformed, unknown, or used in the wrong role."""


@dataclass(frozen=True)
class ModelSpec:
    provider: str
    model_name: str

    @property
    def selector(self) -> str:
        return f"{self.provider}:{self.model_name}"


def is_placeholder(value: str) -> bool:
    return "<" in value and ">" in value


def parse_model_selector(value: str, role: ModelRole) -> ModelSpec:
    """Parse one selector. Placeholders are rejected; callers treat them as unconfigured."""
    if not isinstance(value, str) or not value:
        raise ModelSelectorError("model selector is empty")
    provider_raw, separator, model_name = value.partition(":")
    if not separator or not provider_raw or not model_name:
        raise ModelSelectorError(f"model selector must be 'provider:model_name', got {value!r}")
    if provider_raw != provider_raw.strip() or any(ch.isspace() for ch in provider_raw):
        raise ModelSelectorError(f"provider token contains whitespace: {provider_raw!r}")
    if model_name != model_name.strip():
        raise ModelSelectorError(f"model name has leading/trailing whitespace: {model_name!r}")
    if is_placeholder(value):
        raise ModelSelectorError(f"model selector is an unfilled placeholder: {value!r}")
    provider = PROVIDER_ALIASES.get(provider_raw.lower(), provider_raw.lower())
    provider_role = PROVIDER_ROLES.get(provider)
    if provider_role is None:
        raise ModelSelectorError(f"unknown model provider {provider_raw!r}; allowed: {sorted(PROVIDER_ROLES)}")
    if provider_role is not role:
        raise ModelSelectorError(f"provider {provider!r} is a {provider_role} provider, not usable for {role}")
    return ModelSpec(provider=provider, model_name=model_name)


# ---------------------------------------------------------------------------
# Environment: root .env, with actual process environment taking precedence.

SECRET_ENV_NAMES = frozenset(
    {"OPENROUTER_API_KEY", "LITELLM_API_KEY", "GROQ_API_KEY", "HF_TOKEN", "NEO4J_PASSWORD", "NCBI_API_KEY"}
)
# Personal but not secret; recorded only as present/absent, never copied into artifacts.
PRIVATE_ENV_NAMES = frozenset({"NCBI_EMAIL"})
SUPPORTED_ENV_NAMES = SECRET_ENV_NAMES | {
    "LLM_MODEL",
    "OPENROUTER_REASONING",
    "OPENROUTER_PROVIDER_SORT",
    "OPENROUTER_PROVIDER_ORDER",
    "OPENROUTER_MAX_PRICE_INPUT",
    "OPENROUTER_MAX_PRICE_OUTPUT",
    "OPENROUTER_APP_URL",
    "OPENROUTER_APP_TITLE",
    "EMBEDDINGS_ENABLED",
    "EMBEDDING_MODEL",
    "OLLAMA_BASE_URL",
    "LITELLM_BASE_URL",
    "LITELLM_API_BASE",
    "NEO4J_URI",
    "NEO4J_USERNAME",
    "NEO4J_DATABASE",
    "NCBI_EMAIL",
    "NCBI_TOOL",
}
PROVIDER_REQUIRED_ENV: dict[str, tuple[str, ...]] = {
    "litellm": ("LITELLM_BASE_URL", "LITELLM_API_KEY"),
    "openrouter": ("OPENROUTER_API_KEY",),
    "groq": ("GROQ_API_KEY",),
    "ollama": (),
    "sentence_transformers": (),
}
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"


def load_environment(env_file: Path | None, process_env: Mapping[str, str] | None = None) -> dict[str, str]:
    """Merge a dotenv file under the process environment.

    The file is parsed, never executed, with interpolation disabled. A variable present in the
    process environment wins even when it is explicitly empty.
    """
    file_values: dict[str, str] = {}
    if env_file is not None and env_file.is_file():
        file_values = {
            key: value for key, value in dotenv_values(env_file, interpolate=False).items() if value is not None
        }

    def with_alias(values):
        values = dict(values)
        if "LITELLM_BASE_URL" not in values and "LITELLM_API_BASE" in values:
            values["LITELLM_BASE_URL"] = values["LITELLM_API_BASE"]
        return values

    merged = with_alias(file_values)
    merged.update(with_alias(os.environ if process_env is None else process_env))
    return merged


def parse_strict_bool(name: str, value: str) -> bool:
    if value == "true":
        return True
    if value == "false":
        return False
    raise ConfigError(f"{name} must be exactly 'true' or 'false', got {value!r}")


def validate_service_url(name: str, value: str) -> str:
    """Nonsecret HTTP(S) endpoint; credentials must travel through dedicated SDK fields."""
    parts = urlsplit(value)
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise ConfigError(f"{name} must be an http(s) URL with a host")
    if parts.username or parts.password or parts.query or parts.fragment:
        raise ConfigError(f"{name} must not embed credentials, query parameters, or fragments")
    return value


class SelectionStatus(StrEnum):
    CONFIGURED = "configured"
    UNCONFIGURED = "unconfigured"
    DISABLED = "disabled"


@dataclass(frozen=True)
class RoleSelection:
    """Resolved model for one role. `source` records where the selector came from."""

    role_name: str
    status: SelectionStatus
    spec: ModelSpec | None
    source: str | None
    reason: str | None = None

    def to_record(self) -> dict[str, Any]:
        return {
            "role": self.role_name,
            "status": self.status.value,
            "selector": self.spec.selector if self.spec else None,
            "provider": self.spec.provider if self.spec else None,
            "model_name": self.spec.model_name if self.spec else None,
            "source": self.source,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class ModelSettings:
    """Nonsecret model configuration. Credential values are never stored, only their presence."""

    extractor: RoleSelection
    verifier: RoleSelection
    screener: RoleSelection
    embeddings: RoleSelection
    ollama_base_url: str | None
    credential_presence: dict[str, bool]

    @property
    def missing_credentials(self) -> list[str]:
        return sorted(name for name, present in self.credential_presence.items() if not present)

    def to_record(self) -> dict[str, Any]:
        return {
            "extractor": self.extractor.to_record(),
            "verifier": self.verifier.to_record(),
            "screener": self.screener.to_record(),
            "embeddings": self.embeddings.to_record(),
            "ollama_base_url": self.ollama_base_url,
            "credential_presence": dict(sorted(self.credential_presence.items())),
        }


def _nested(mapping: Mapping[str, Any], section: str, key: str, source: str) -> Any:
    block = mapping.get(section)
    if block is None:
        return None
    if not isinstance(block, Mapping):
        raise ConfigError(f"{source}: '{section}' must be a mapping")
    return block.get(key)


def _yaml_selector(value: Any, source: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ConfigError(f"{source} must be a string selector")
    return value


def _select(role_name: str, role: ModelRole, candidates: list[tuple[str | None, str]]) -> RoleSelection:
    """First nonblank candidate wins; a placeholder means the role remains unconfigured."""
    for value, source in candidates:
        if value is None or value == "":
            continue
        if is_placeholder(value):
            return RoleSelection(role_name, SelectionStatus.UNCONFIGURED, None, source, "placeholder selector")
        return RoleSelection(role_name, SelectionStatus.CONFIGURED, parse_model_selector(value, role), source)
    return RoleSelection(role_name, SelectionStatus.UNCONFIGURED, None, None, "no selector supplied")


def resolve_model_settings(
    env: Mapping[str, str],
    extraction_yaml: Mapping[str, Any] | None = None,
    literature_yaml: Mapping[str, Any] | None = None,
) -> ModelSettings:
    """Apply the plan §6.4.2 precedence.

    Only the model-selection keys of extraction.yaml/literature.yaml are read here; the full
    schemas of those files belong to the packages that own them.
    """
    extraction_yaml = extraction_yaml or {}
    literature_yaml = literature_yaml or {}

    extractor = _select(
        "extractor",
        ModelRole.CHAT,
        [
            (env.get("LLM_MODEL"), "env:LLM_MODEL"),
            (
                _yaml_selector(
                    _nested(extraction_yaml, "extractor", "model", "extraction.yaml"), "extraction.yaml extractor.model"
                ),
                "extraction.yaml:extractor.model",
            ),
        ],
    )
    verifier_yaml = _yaml_selector(
        _nested(extraction_yaml, "verifier", "model", "extraction.yaml"), "extraction.yaml verifier.model"
    )
    if verifier_yaml:
        verifier = _select("verifier", ModelRole.CHAT, [(verifier_yaml, "extraction.yaml:verifier.model")])
    else:
        verifier = RoleSelection(
            "verifier", extractor.status, extractor.spec, f"inherited:{extractor.source}", extractor.reason
        )

    # Paper screening (user-authorized): its own selector when given, otherwise the chat selection.
    screening_yaml = _yaml_selector(
        _nested(literature_yaml, "screening", "model", "literature.yaml"), "literature.yaml screening.model"
    )
    screening_selector = env.get("SCREENING_MODEL") or screening_yaml
    if screening_selector:
        screener = _select(
            "screener",
            ModelRole.CHAT,
            [(env.get("SCREENING_MODEL"), "env:SCREENING_MODEL"), (screening_yaml, "literature.yaml:screening.model")],
        )
    else:
        screener = RoleSelection(
            "screener", extractor.status, extractor.spec, f"inherited:{extractor.source}", extractor.reason
        )

    enabled_yaml = _nested(literature_yaml, "embeddings", "enabled", "literature.yaml")
    if "EMBEDDINGS_ENABLED" in env:
        enabled = parse_strict_bool("EMBEDDINGS_ENABLED", env["EMBEDDINGS_ENABLED"])
    elif enabled_yaml is None:
        enabled = False
    elif isinstance(enabled_yaml, bool):
        enabled = enabled_yaml
    else:
        raise ConfigError("literature.yaml embeddings.enabled must be a boolean")

    embedding_candidates = [
        (env.get("EMBEDDING_MODEL"), "env:EMBEDDING_MODEL"),
        (
            _yaml_selector(
                _nested(literature_yaml, "embeddings", "model", "literature.yaml"), "literature.yaml embeddings.model"
            ),
            "literature.yaml:embeddings.model",
        ),
    ]
    if enabled:
        embeddings = _select("embeddings", ModelRole.EMBEDDING, embedding_candidates)
        if embeddings.status is not SelectionStatus.CONFIGURED:
            raise ConfigError(
                f"embeddings are enabled but no real embedding selector is configured ({embeddings.reason})"
            )
    else:
        # A disabled role's selector is still validated so a typo cannot hide until it is enabled.
        chosen = _select("embeddings", ModelRole.EMBEDDING, embedding_candidates)
        embeddings = RoleSelection(
            "embeddings", SelectionStatus.DISABLED, chosen.spec, chosen.source, "embeddings disabled"
        )

    ollama_base_url = None
    if embeddings.status is SelectionStatus.CONFIGURED and embeddings.spec.provider == "ollama":
        override = env.get("OLLAMA_BASE_URL", "")
        ollama_base_url = validate_service_url("OLLAMA_BASE_URL", override) if override else DEFAULT_OLLAMA_BASE_URL

    required: set[str] = set()
    for selection in (extractor, verifier, screener, embeddings):
        if selection.status is SelectionStatus.CONFIGURED:
            required.update(PROVIDER_REQUIRED_ENV[selection.spec.provider])
    if "LITELLM_BASE_URL" in required and env.get("LITELLM_BASE_URL"):
        validate_service_url("LITELLM_BASE_URL", env["LITELLM_BASE_URL"])
    presence = {name: bool(env.get(name)) for name in required}

    return ModelSettings(extractor, verifier, screener, embeddings, ollama_base_url, presence)


def load_model_settings(repo_root: Path, process_env: Mapping[str, str] | None = None) -> ModelSettings:
    """Resolve model settings from root .env, the process environment, and optional stage YAML."""
    env = load_environment(repo_root / ".env", process_env)
    extraction = repo_root / "configs" / "extraction.yaml"
    literature = repo_root / "configs" / "literature.yaml"
    return resolve_model_settings(
        env,
        read_yaml(extraction) if extraction.is_file() else None,
        read_yaml(literature) if literature.is_file() else None,
    )


# ---------------------------------------------------------------------------
# configs/ranking.yaml (candidate generation) and configs/literature.yaml (retrieval queue).
# Later packages extend these files; each loader validates its own section strictly.


class HgncResourceConfig(StrictModel):
    archive_date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")


class CollectriResourceConfig(StrictModel):
    zenodo_record: str = Field(pattern=r"^\d+$")
    filename: str
    complex_regulators: list[str]


class ResourcesConfig(StrictModel):
    hgnc: HgncResourceConfig
    collectri: CollectriResourceConfig
    seed_publication_lists: dict[str, Path]
    # Observed expectation for the supplied lists; a different count must be investigated.
    expected_unique_pmids: int = Field(ge=0)


SIGN_BASES = {"pmid_evidence", "tf_regulon_majority", "default_activation"}


class ConcordanceConfig(StrictModel):
    # Engineering/coverage setting, not a biological threshold.
    min_targets: int = Field(ge=1)
    primary_sign_bases: list[str]
    sensitivity_sign_bases: list[str]

    @model_validator(mode="after")
    def _known_bases(self) -> ConcordanceConfig:
        for bases in (self.primary_sign_bases, self.sensitivity_sign_bases):
            if not bases or set(bases) - SIGN_BASES:
                raise ValueError(f"sign bases must be a nonempty subset of {sorted(SIGN_BASES)}")
        return self


class CandidateGenerationConfig(StrictModel):
    rule_version: str
    cell_types: list[str]
    resources: ResourcesConfig
    concordance: ConcordanceConfig
    extra_tfs_per_comparison: int = Field(ge=0)
    targets_per_candidate: int = Field(ge=0)


class RetrievalQueueConfig(StrictModel):
    query_version: str
    max_live_queries: int = Field(ge=0)
    max_aliases_per_gene: int = Field(ge=0)
    assay_terms: list[str]
    null_terms: list[str]
    context_terms: list[str]


# ---------------------------------------------------------------------------
# configs/manuscript_scope.yaml: the four manuscript regulatory cases (P2.11).


class LineageScopeConfig(StrictModel):
    cell_type: str  # exact source cell-type label
    tf_seeds: list[str] = Field(min_length=1)  # exact source symbols; order is not a ranking
    # Conditions with a primary Niche2-versus-Niche1 regulatory comparison in the manuscript.
    primary_conditions: list[str] = Field(min_length=1)
    # Lineage-specific retrieval context phrases; they select literature, they assert nothing.
    context_terms: list[str] = Field(min_length=1)
    # Draft interpretation to assess later; never used for scoring, filtering, or direction.
    draft_interpretation: str

    @model_validator(mode="after")
    def _unique(self) -> LineageScopeConfig:
        for name, values in (("tf_seeds", self.tf_seeds), ("primary_conditions", self.primary_conditions)):
            if len(set(values)) != len(values):
                raise ValueError(f"{self.cell_type}: duplicate {name}")
        return self


class ExpectedScopeCounts(StrictModel):
    primary_comparisons: int = Field(ge=1)
    lineage_tf_memberships: int = Field(ge=1)
    unique_named_tfs: int = Field(ge=1)


class QueryScheduleConfig(StrictModel):
    rule_version: str
    batch_size: int = Field(ge=1)  # queries per resumable batch; the P3 per-batch budget still applies


class ManuscriptScopeConfig(StrictModel):
    schema_version: int
    scope_version: str
    source: str
    lineages: list[LineageScopeConfig] = Field(min_length=1)
    expected: ExpectedScopeCounts
    schedule: QueryScheduleConfig

    @model_validator(mode="after")
    def _consistent(self) -> ManuscriptScopeConfig:
        cell_types = [lineage.cell_type for lineage in self.lineages]
        if len(set(cell_types)) != len(cell_types):
            raise ValueError("each lineage may appear only once")
        counts = {
            "primary_comparisons": sum(len(lineage.primary_conditions) for lineage in self.lineages),
            "lineage_tf_memberships": sum(len(lineage.tf_seeds) for lineage in self.lineages),
            "unique_named_tfs": len({seed for lineage in self.lineages for seed in lineage.tf_seeds}),
        }
        mismatched = {k: v for k, v in counts.items() if v != getattr(self.expected, k)}
        if mismatched:
            raise ValueError(f"scope does not reconcile with its expected counts: {mismatched}")
        return self


def load_manuscript_scope(path: Path, project: ProjectConfig) -> ManuscriptScopeConfig:
    try:
        scope = ManuscriptScopeConfig.model_validate(read_yaml(path))
    except ValueError as error:
        raise ConfigError(f"invalid manuscript scope {path}: {error}") from error
    for lineage in scope.lineages:
        if lineage.cell_type not in project.cell_types:
            raise ConfigError(f"{path.name}: unknown cell type {lineage.cell_type!r}")
        unknown = set(lineage.primary_conditions) - set(project.dataset.conditions)
        if unknown:
            raise ConfigError(f"{path.name}: {lineage.cell_type} has unknown conditions {sorted(unknown)}")
    return scope


RANKING_SECTIONS = {"schema_version", "candidate_generation"}
LITERATURE_SECTIONS = {
    "schema_version",
    "retrieval_queue",
    "embeddings",
    "search",
    "fetch",
    "retrieval",
    "bundles",
    "corpus",
}


def _section(path: Path, allowed: set[str], name: str) -> dict[str, Any]:
    content = read_yaml(path)
    unknown = sorted(set(content) - allowed)
    if unknown:
        raise ConfigError(f"{path.name}: unknown top-level fields {unknown}")
    if name not in content:
        raise ConfigError(f"{path.name}: missing '{name}' section")
    return content[name]


def load_candidate_config(path: Path) -> CandidateGenerationConfig:
    try:
        return CandidateGenerationConfig.model_validate(_section(path, RANKING_SECTIONS, "candidate_generation"))
    except ValueError as error:
        raise ConfigError(f"invalid candidate configuration {path}: {error}") from error


def load_queue_config(path: Path) -> RetrievalQueueConfig:
    try:
        return RetrievalQueueConfig.model_validate(_section(path, LITERATURE_SECTIONS, "retrieval_queue"))
    except ValueError as error:
        raise ConfigError(f"invalid retrieval-queue configuration {path}: {error}") from error


# ---------------------------------------------------------------------------
# configs/literature.yaml, P3 sections.


class SearchConfig(StrictModel):
    max_queries: int = Field(ge=0, le=20)
    max_results_per_query: int = Field(ge=1, le=10)
    max_papers: int = Field(ge=0, le=10)
    sources: list[str]
    timeout_seconds: float = Field(gt=0)
    max_retries: int = Field(ge=0, le=5)
    contact_tool: str
    include_advisor_seed_metadata: bool
    context_terms: list[str]
    assay_terms: list[str]

    @model_validator(mode="after")
    def _known_sources(self) -> SearchConfig:
        unknown = set(self.sources) - {"pubmed", "europepmc"}
        if unknown or not self.sources:
            raise ValueError(f"search sources must be a nonempty subset of pubmed/europepmc, got {self.sources}")
        return self


class FetchConfig(StrictModel):
    full_text_source: str
    pubtator_annotations: bool
    pdf_enabled: bool


class RetrievalConfig(StrictModel):
    hits_per_query: int = Field(ge=1)
    rrf_k: int = Field(ge=1)
    bm25_k1: float = Field(gt=0)
    bm25_b: float = Field(ge=0, le=1)


class BundleConfig(StrictModel):
    max_bundles: int = Field(ge=0, le=20)
    max_passages: int = Field(ge=1, le=3)
    max_chars: int = Field(ge=1, le=6000)
    max_per_paper: int = Field(ge=1)
    max_per_candidate_tf: int = Field(ge=1)


class EmbeddingSection(StrictModel):
    enabled: bool = False
    model: str | None = None
    revision: str | None = None
    device: str | None = None
    # A WordPiece token spans at least one character, so chunks of <= 1000 characters plus the
    # two special tokens cannot exceed the model's 1024-token context: truncation cannot occur.
    max_chunk_chars: int = Field(default=1000, ge=100)
    batch_size: int = Field(default=32, ge=1)


class PdfLimits(StrictModel):
    max_bytes: int = Field(gt=0)
    max_pages: int = Field(gt=0)
    timeout_seconds: float = Field(gt=0)
    # OCR stays off: born-digital PDFs carry a text layer; a scanned PDF is reported, not guessed.
    ocr: bool = False


class SpreadsheetLimits(StrictModel):
    max_sheets: int = Field(gt=0)
    max_rows_per_sheet: int = Field(gt=0)
    max_columns: int = Field(gt=0)


class ReadyBatchLimits(StrictModel):
    # Per live extraction batch, not a cap on the corpus.
    max_papers: int = Field(ge=1, le=10)
    max_bundles: int = Field(ge=1, le=20)
    max_scheduled_calls: int = Field(ge=1, le=40)


class BudgetAssumptions(StrictModel):
    """Planning assumptions for token estimates; P4 replaces them with a no-inference dry run."""

    chars_per_token: float = Field(gt=0)
    extractor_overhead_tokens: int = Field(ge=0)
    verifier_overhead_tokens: int = Field(ge=0)
    extractor_output_tokens_typical: int = Field(ge=0)
    extractor_output_tokens_cap: int = Field(ge=0)
    verifier_output_tokens_typical: int = Field(ge=0)
    verifier_output_tokens_cap: int = Field(ge=0)
    reasoning_tokens_typical: int = Field(ge=0)
    reasoning_tokens_cap: int = Field(ge=0)
    max_attempts_per_call: int = Field(ge=1)
    schema_preflight_calls: int = Field(ge=0)
    planning_reserve: float = Field(ge=0)
    # Illustrative USD per million tokens (input, output); not verified quotes.
    illustrative_rates: dict[str, tuple[float, float]]
    # Evidence-assembly (P4 context investigation) bounds and per-scenario call/token assumptions:
    # input_tokens_cap_per_call, preflight_calls_per_batch, and low/typical/conservative entries with
    # calls, first_call_input_tokens, history_growth_per_call_tokens, output_tokens_per_call.
    assembly: dict


class SupplementException(StrictModel):
    """A named, bounded allowance for one oversized supplement; the global limit stays in force."""

    pmid: str
    filename: str
    max_bytes: int = Field(gt=0, le=67_108_864)  # 64 MiB compressed
    max_expanded_bytes: int = Field(gt=0, le=536_870_912)  # 512 MiB expanded
    reason: str


class CorpusConfig(StrictModel):
    version: str
    audit_batch_size: int = Field(ge=1, le=10)
    discovery_batch_size: int = Field(ge=1, le=20)
    acquisition_batch_size: int = Field(ge=1, le=10)
    supplement_max_bytes: int = Field(gt=0)
    supplement_extensions: list[str]
    supplement_size_exceptions: list[SupplementException] = []
    # OA article PDFs fetched only as non-canonical alternates to validate the PDF branch.
    pdf_validation_articles: int = Field(ge=0)
    pdf: PdfLimits
    spreadsheet: SpreadsheetLimits
    corpus_hits_per_query: int = Field(ge=1)
    ready_batch: ReadyBatchLimits
    budget: BudgetAssumptions


class ScreeningAllowance(StrictModel):
    """Hard per-run bounds for LLM screening. A missing bound is not a licence to spend."""

    max_calls: int | None = Field(default=None, ge=1)
    max_input_tokens: int | None = Field(default=None, ge=1)
    max_output_tokens: int | None = Field(default=None, ge=1)
    max_usd: float | None = Field(default=None, ge=0)


class ScreeningConfig(StrictModel):
    model: str | None = None
    litellm_reasoning_effort: Literal["low", "high", "max"] | None = None
    rule: str
    window_input_tokens: int = Field(ge=500)
    prompt_overhead_tokens: int = Field(ge=0)
    max_output_tokens: int = Field(ge=100)
    window_overlap_sections: int = Field(ge=0, le=3)
    supplement_preview_chars: int = Field(ge=0, le=2000)
    max_supplements_listed: int = Field(ge=1)
    max_table_rows_per_section: int = Field(ge=1, le=50)
    chars_per_token: int = Field(ge=1, le=10)
    max_attempts_per_call: int = Field(ge=1, le=5)
    concurrency: int = Field(ge=1, le=8)
    allowance: ScreeningAllowance = ScreeningAllowance()


class LiteratureConfig(StrictModel):
    schema_version: int
    retrieval_queue: RetrievalQueueConfig
    search: SearchConfig
    fetch: FetchConfig
    retrieval: RetrievalConfig
    bundles: BundleConfig
    embeddings: EmbeddingSection = EmbeddingSection()
    screening: ScreeningConfig | None = None
    corpus: CorpusConfig | None = None


def load_literature_config(path: Path) -> LiteratureConfig:
    try:
        return LiteratureConfig.model_validate(read_yaml(path))
    except ValueError as error:
        raise ConfigError(f"invalid literature configuration {path}: {error}") from error
