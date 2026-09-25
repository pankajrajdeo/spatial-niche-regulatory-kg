"""Read-only canonical source registry and integrity checks at the P3/P4 boundary."""

from dataclasses import asdict
from pathlib import Path

import pandas as pd

from regkg.provenance import canonical_json, read_json, sha256_file, sha256_text, stable_id
from regkg.workflows.corpus_parse import _load_document
from regkg.workflows.corpus_ready import serialize_evidence
from regkg.workflows.p3_selection import read_jsonl

MAX_EVIDENCE_PARTS = 8
MAX_EVIDENCE_CHARS = 16000


class SourceRegistry:
    def __init__(self, root: Path, selection: str, work: Path):
        self.root, self.work = root, work
        self.artifact = root / "data/processed" / selection
        manifest = read_json(self.artifact / "manifest.json")
        for name, digest in manifest["outputs"].items():
            if sha256_file(self.artifact / name) != digest:
                raise ValueError(f"Selection output changed: {name}")
        self.manifest_hash = sha256_file(self.artifact / "manifest.json")
        self.bundles = {b["payload_id"]: b for b in read_jsonl(self.artifact / "bundles_all.jsonl")}
        # Bundles carry their parse receipts; supplement documents also occur in parent inventory.
        self.reports = {b["document_id"]: b["document_parse"] for b in self.bundles.values()}
        for path in sorted((root / "data/processed").glob("litcorpus-68fea35a393fe816/parse_inventory.parquet")):
            for report in pd.read_parquet(path).to_dict("records"):
                if not isinstance(self.reports.get(report["document_id"], {}).get("cache_key"), str):
                    self.reports[report["document_id"]] = report
        self.documents, self.file_hashes = {}, {}

    def document(self, document_id: str):
        if document_id not in self.reports:
            raise ValueError("Unknown source document")
        report = self.reports[document_id]
        key = report.get("cache_key")
        if not isinstance(key, str) or not key.isalnum():
            raise ValueError("Invalid source cache identity")
        path = self.work / "parsed" / key / "document.json"
        digest = sha256_file(path)
        if document_id in self.file_hashes and self.file_hashes[document_id] != digest:
            raise ValueError("SOURCE_CHANGED")
        self.file_hashes[document_id] = digest
        if document_id not in self.documents:
            doc = _load_document(read_json(path))
            if doc.source_asset_sha256 != report["asset_sha256"]:
                raise ValueError("Source asset identity mismatch")
            self.documents[document_id] = doc
        doc = self.documents[document_id]
        asset_dir = self.root / "data/papers" / doc.publication_id.replace(":", "_") / doc.source_asset_sha256
        candidates = [p for p in asset_dir.glob("*") if p.is_file()]
        if not candidates or not any(sha256_file(p) == doc.source_asset_sha256 for p in candidates):
            raise ValueError("Original source asset missing or changed; P3 repair required")
        return self.documents[document_id]

    def part(self, document_id: str, passage_id: str) -> dict:
        doc = self.document(document_id)
        passage = next((p for p in doc.passages if p.passage_id == passage_id), None)
        if passage is None or doc.canonical_text[passage.start : passage.end] != passage.text:
            raise ValueError("Invalid source passage or offsets")
        body = asdict(passage)
        body.update(
            publication_id=doc.publication_id,
            document_id=document_id,
            document_sha256=doc.canonical_sha256,
            publication_version_id=doc.text_version,
            parser_rule_version=doc.extra_rules,
            quality_flags=self.reports[document_id].get("reasons", []),
        )
        body["part_id"] = stable_id(
            "part", {"document": document_id, "passage": passage_id, "content": sha256_text(canonical_json(body))}
        )
        body["part_sha256"] = sha256_text(canonical_json(body))
        return body

    def validate_bundle(self, bundle: dict, require_ready: bool = True) -> list[dict]:
        if require_ready and not bundle["readiness_state"].startswith("READY"):
            raise ValueError("Bundle is not source-ready")
        if len(bundle["parts"]) > MAX_EVIDENCE_PARTS or len(serialize_evidence(bundle["parts"])) > MAX_EVIDENCE_CHARS:
            raise ValueError("Evidence payload exceeds P4 context bounds")
        parts = []
        for raw in bundle["parts"]:
            part = self.part(raw["document_id"], raw["passage_id"])
            for field in ("text", "locator", "asset_sha256", "cells", "table_header", "page"):
                if raw.get(field) != part.get(field):
                    raise ValueError(f"Source part mismatch: {field}")
            if part["publication_id"] != bundle["publication_id"]:
                raise ValueError("Cross-publication source part")
            if raw["document_id"] == bundle["document_id"] and part["document_sha256"] != bundle["canonical_sha256"]:
                raise ValueError("Canonical source changed")
            parts.append(part)
        return parts

    def paper_parts(self, bundle: dict) -> list[dict]:
        # Same canonical document/version; cross-asset interpretation is never guessed.
        doc = self.document(bundle["document_id"])
        return [self.part(bundle["document_id"], p.passage_id) for p in doc.passages]


def model_parts(parts: list[dict]) -> list[dict]:
    records = [
        {
            k: p.get(k)
            for k in (
                "part_id",
                "document_id",
                "kind",
                "section_path",
                "text",
                "table_header",
                "cells",
                "table_id",
                "item_id",
                "item_label",
                "page",
                "bbox",
                "locator",
                "table_structure",
            )
        }
        for p in parts
    ]
    for record in records:
        record["cells"] = [
            {**cell, "cell_ref": f"{record['part_id']}:c{cell['col_start']}"} for cell in record.get("cells") or []
        ]
    return records


def pubtator_context(registry: SourceRegistry, parts: list[dict]) -> dict:
    """Reuse aligned cached PubTator types; external identity is a hint, not evidence."""
    from regkg.literature.passages import pubtator_mentions

    assets, hints, unaligned = {}, [], 0
    for document_id in sorted({p["document_id"] for p in parts}):
        doc = registry.document(document_id)
        paper_dir = registry.root / "data/papers" / doc.publication_id.replace(":", "_")
        selected = {p["passage_id"]: p for p in parts if p["document_id"] == document_id}
        for path in sorted(paper_dir.glob("*/pubtator.json")):
            digest = sha256_file(path)
            if path.parent.name != digest:
                raise ValueError("PubTator source asset checksum mismatch")
            assets[str(path.relative_to(registry.root))] = digest
            # Keep the original NCBI identifiers. Human mapping is independently validated
            # downstream; an external annotation must not establish experimental species.
            for mention in pubtator_mentions(
                doc, read_json(path), {}, {"Gene", "Chemical", "Disease", "Species", "CellLine", "Mutation"}
            ):
                if mention.passage_id is None:
                    unaligned += 1
                elif mention.passage_id in selected:
                    part = selected[mention.passage_id]
                    if doc.canonical_text[mention.start : mention.end] != mention.text:
                        raise ValueError("PubTator canonical span mismatch")
                    hints.append(
                        {
                            "part_id": part["part_id"],
                            "text": mention.text,
                            "entity_type": mention.entity_type,
                            "source": "PubTator3",
                            "source_asset_sha256": digest,
                            "external_identifier": mention.external_identifier,
                            "external_offset": mention.external_offset,
                            "start": mention.start,
                            "end": mention.end,
                            "alignment": mention.alignment,
                        }
                    )
    return {
        "status": "CACHED_ANNOTATIONS" if assets else "NO_CACHED_ANNOTATIONS",
        "assets": assets,
        "mentions": hints,
        "gene_mentions": [hint for hint in hints if hint["entity_type"] == "Gene"],
        "unaligned_document_mentions": unaligned,
        "role": "Identity hints only; not experimental context or verified regulatory relations",
    }


def bundle_parts(parts: list[dict]) -> list[dict]:
    """Original source fields used by the P3 scientific-payload size contract."""
    fields = (
        "document_id",
        "passage_id",
        "kind",
        "section_path",
        "locator",
        "page",
        "text",
        "table_header",
        "cells",
        "asset_sha256",
    )
    return [{key: part.get(key) for key in fields} for part in parts]
