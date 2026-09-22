"""Per-paper screening, fail-closed bundles, supplement dependencies, investigations, and the budget.

Every acquired paper is screened passage by passage for the manuscript candidate TFs (rule
p3-screen-1); retrieval scores (BM25 and cached embeddings) only order the work and never decide
eligibility. Each candidate item keeps its source locator, matched TF, manuscript lineage
associations, the paper's source-reported context, and a provisional relevance/attribution label.

Bundles serialize their evidence with one function (rule p3-serialize-1): at most three source
parts and 6,000 characters including text, cells, headers, locators, and the mention records that
travel with them. Evidence is never truncated; what does not fit is a recorded blocker. A bundle is
source-ready only when its context is complete, its attribution is the paper's own result, and its
document is fully parsed full text (or abstract-only under a recorded disposition). Resolvable
context gaps become entries of a separate context-investigation queue for P4; nothing here resolves
them or calls a chat model.
"""

from __future__ import annotations

import hashlib
import json
import math
import re

import numpy as np
import pandas as pd

from regkg.config import BudgetAssumptions
from regkg.literature import embeddings as emb
from regkg.literature.parse import Document, Passage
from regkg.literature.retrieval import BACK_REFERENCE, COMPARISON, NEGATION, BM25Okapi, QueryTerms, _context, tokenize
from regkg.literature.screening import IRRELEVANT, TRANSFERABLE, attribution
from regkg.provenance import canonical_json, sha256_text, stable_id

SCREEN_RULE = "p3-screen-2"  # 2: passage-level context decides disposition; case variants as hints
SERIAL_RULE = "p3-serialize-2"  # 2: mention records carry their resolution
PAYLOAD_RULE = "p3-corpus-payload-2"
TF_IDENTITY_RULE = "p3-tf-identity-2"  # 2: per TF over the merged association set
DEPENDENCY_RULE = "p3-dependency-2"  # 2: partial capture kept; bounded same-publication navigation
MAX_NAVIGATION_ASSETS = 25
MAX_PARTS = 3
MAX_EVIDENCE_CHARS = 6000
SUPPLEMENT_REFERENCE = re.compile(
    r"\b(Supplementa(?:ry|l) (?:Tables?|Fig(?:ure)?s?\.?|Data|Information|Methods|Materials?|Notes?|Movies?|Videos?)"
    r"\s*S?\d*[A-Za-z]?|(?:Table|Fig(?:ure)?\.?|Data|Movie|Video) S\d+[A-Za-z]?|Additional files? \d+|"
    r"Extended Data (?:Fig(?:ure)?\.?|Table) \d+)",
    re.IGNORECASE,
)
TABLE_REGION_KINDS = {"supplement_table_header", "supplement_table_row"}
READY_ATTRIBUTIONS = {"source_result_candidate", "abstract_summary"}
MENTION_FIELDS = (
    "text",
    "start",
    "end",
    "hgnc_id",
    "candidate_hgnc_id",
    "species_taxon",
    "identity_status",
    "resolution",
)


def query_terms(queue: pd.DataFrame) -> list[QueryTerms]:
    terms = []
    for row in queue.sort_values("priority").itertuples(index=False):
        data = json.loads(row.terms_json)
        terms.append(
            QueryTerms(
                row.query_id,
                int(row.priority),
                row.tf_hgnc_id,
                list(data["tf"]),
                row.target_hgnc_id if isinstance(row.target_hgnc_id, str) else None,
                list(data.get("target") or []),
                list(data["qualifiers"]),
                list(row.candidate_ids),
            )
        )
    return terms


# ---------------------------------------------------------------------------
# Serialization shared by the size limit and the budget


def part_record(passage: Passage, document_id: str, mentions: list[dict], genes: set[str]) -> dict:
    """One source part as it would enter a prompt. Mention records are those for manuscript genes;
    the count of other mentions is kept so the omission is explicit."""
    kept = [
        {k: m.get(k) for k in MENTION_FIELDS}
        for m in mentions
        if (m.get("hgnc_id") in genes or m.get("candidate_hgnc_id") in genes)
    ]
    return {
        "document_id": document_id,
        "passage_id": passage.passage_id,
        "kind": passage.kind,
        "section_path": passage.section_path,
        "locator": passage.locator,
        "page": passage.page,
        "text": passage.text,
        "table_header": passage.table_header,
        "cells": passage.cells,
        "mentions": kept,
        "other_mentions_not_serialized": len(mentions) - len(kept),
        "asset_sha256": passage.asset_sha256,
    }


def serialize_evidence(parts: list[dict]) -> str:
    """The single measurement of evidence content: one JSON line per source part."""
    return "\n".join(json.dumps(p, ensure_ascii=False, sort_keys=True, default=str) for p in parts)


# ---------------------------------------------------------------------------
# Screening


def gene_matcher(names: dict[str, list[str]]):
    """Whole-token matcher over validated TF names (approved symbol + safe aliases), case-sensitive.

    A rodent-style capitalisation of the approved symbol ("Egr2" for EGR2) is matched as a retrieval
    hint with species/entity identity unresolved; no human ID is inferred from it and no other case
    variants are accepted.
    """
    by_term: dict[str, tuple[str, str]] = {}
    for hgnc, terms in names.items():
        for index, term in enumerate(terms):
            by_term.setdefault(term, (hgnc, "exact_symbol" if index == 0 else "validated_alias"))
        symbol = terms[0]
        variant = symbol[0] + symbol[1:].lower()
        if len(symbol) >= 3 and variant != symbol:
            by_term.setdefault(variant, (hgnc, "case_variant_species_unresolved"))
    pattern = re.compile(
        "|".join(rf"(?<![A-Za-z0-9-]){re.escape(t)}(?![A-Za-z0-9-])" for t in sorted(by_term, key=len, reverse=True))
    )

    def match(text: str) -> dict[str, dict]:
        found: dict[str, dict] = {}
        for m in pattern.finditer(text):
            hgnc, kind = by_term[m.group(0)]
            entry = found.setdefault(hgnc, {"terms": set(), "kinds": set()})
            entry["terms"].add(m.group(0))
            entry["kinds"].add(kind)
        return {h: {"terms": sorted(v["terms"]), "kinds": sorted(v["kinds"])} for h, v in found.items()}

    return match


def _excluded_section(passage: Passage) -> str | None:
    if re.search(r"\b(references?|bibliograph\w*|literature cited)\b", passage.section_path.lower()):
        return "reference_list_section"
    return None


def screen(
    documents: dict[str, Document],
    meta: dict[str, dict],
    lineages: list[dict],
    relevance: dict,
    match,
    ontology=None,
) -> list[dict]:
    """One screening item per (source part or table region, matched TF), with all lineage associations.

    `relevance[(pmid, cell_type)]` is the paper's provisional (label, reason); it prioritises only. The
    passage's own context decides disposition: a passage is set aside as irrelevant only when both the
    paper label and the passage itself indicate another context. Everything else stays a candidate.
    """
    from regkg.literature.screening import context_relevance, regulatory_content, source_context

    tf_lineages: dict[str, list[str]] = {}
    for lineage in lineages:
        for hgnc in lineage["candidate_tfs"]:
            tf_lineages.setdefault(hgnc, []).append(lineage["cell_type"])
    items: list[dict] = []
    for doc_id, document in documents.items():
        info = meta[doc_id]
        regions: dict[tuple[str, str], dict] = {}
        for passage in document.passages:
            hits = match(passage.text)
            passage_profile = (
                source_context(passage.text, ontology) if hits and passage.kind not in TABLE_REGION_KINDS else None
            )
            for hgnc, hit in hits.items():
                terms = hit["terms"]
                cells = tf_lineages.get(hgnc, [])
                if not cells:
                    continue
                labels = {c: relevance.get((info["pmid"], c), ("unresolved", "no paper-level context")) for c in cells}
                base = {
                    "publication_id": info["publication_id"],
                    "pmid": info["pmid"],
                    "document_id": doc_id,
                    "document_role": info["role"],
                    "text_version": document.text_version,
                    "source_asset_sha256": document.source_asset_sha256,
                    "tf_hgnc_id": hgnc,
                    "matched_terms": terms,
                    "match_kinds": hit["kinds"],
                    "lineages": {c: {"relevance": v[0], "reason": v[1]} for c, v in labels.items()},
                    "rule_version": SCREEN_RULE,
                }
                if passage.kind in TABLE_REGION_KINDS:
                    region = regions.setdefault(
                        (passage.table_id or passage.item_id or "", hgnc),
                        {
                            **base,
                            "item_id": stable_id(
                                "screen", {"doc": doc_id, "table": passage.table_id, "tf": hgnc, "rule": SCREEN_RULE}
                            ),
                            "unit": "table_region",
                            "passage_id": None,
                            "kind": "supplement_table_region",
                            "table_id": passage.table_id,
                            "locator": None,
                            "page": None,
                            "row_locators": [],
                            "rows_matched": 0,
                            "section_type": "supplement",
                            "attribution": "table_meaning_requires_review",
                            "outcome": "requires_interpretation_review",
                            "outcome_reason": "table region: entities, contrast, units, statistics unverified",
                        },
                    )
                    region["rows_matched"] += 1
                    if len(region["row_locators"]) < 5:
                        region["row_locators"].append(passage.locator)
                    region["locator"] = region["row_locators"][0]
                    continue
                item = {
                    **base,
                    "item_id": stable_id("screen", {"passage": passage.passage_id, "tf": hgnc, "rule": SCREEN_RULE}),
                    "unit": "passage",
                    "passage_id": passage.passage_id,
                    "kind": passage.kind,
                    "table_id": passage.table_id,
                    "locator": passage.locator,
                    "page": passage.page,
                    "row_locators": [],
                    "rows_matched": None,
                    "section_type": passage.section_type,
                    "attribution": attribution(passage.kind, passage.section_type, passage.text),
                }
                regulatory = regulatory_content(passage.text)
                for cell_type, entry in item["lineages"].items():
                    label, reason = context_relevance(passage_profile, cell_type, regulatory, [])
                    entry.update(passage_relevance=label, passage_reason=reason)
                excluded = _excluded_section(passage)
                if excluded:
                    item.update(outcome="excluded_non_evidence_section", outcome_reason=excluded)
                elif passage.kind == "title":
                    item.update(outcome="title_mention_paper_level", outcome_reason="a title is not a finding")
                elif not passage_profile["lung_tissue"] and all(
                    v["relevance"] == IRRELEVANT and v["passage_relevance"] in {IRRELEVANT, TRANSFERABLE}
                    for v in item["lineages"].values()
                ):
                    # Paper label and the passage agree on another context; preserved, not bundled.
                    item.update(
                        outcome="screened_irrelevant_context",
                        outcome_reason="paper and passage both indicate a non-lung context; preserved",
                    )
                elif item["attribution"] == "methods_context":
                    item.update(
                        outcome="supporting_methods_retained",
                        outcome_reason="methods passage: supporting context, not a standalone finding",
                    )
                else:
                    item.update(outcome="bundle_candidate", outcome_reason="prose candidate for a source bundle")
                items.append(item)
        items.extend(regions.values())
    return sorted(items, key=lambda i: i["item_id"])


def prioritize(
    documents: dict[str, Document],
    queries: list[QueryTerms],
    items: list[dict],
    backend,
    store_root,
    embedding_config,
    rrf_k: int,
    bm25_k1: float,
    bm25_b: float,
    log=print,
) -> tuple[dict, dict]:
    """Best fused BM25/embedding score per candidate passage over its TF's lineage queries (ordering only)."""
    passages = [p for d in documents.values() for p in d.passages]
    index = {p.passage_id: i for i, p in enumerate(passages)}
    bm25 = BM25Okapi([tokenize(p.text) for p in passages] or [[""]], k1=bm25_k1, b=bm25_b)
    record: dict = {"dense_status": emb.DENSE_DISABLED if backend is None else emb.DENSE_OK, "passages": len(passages)}
    dense: dict[str, np.ndarray] = {}
    if backend is not None and passages:
        store = emb.VectorStore(store_root, backend)
        chunks = {p.passage_id: emb.chunk_text(p.text, embedding_config.max_chunk_chars) for p in passages}
        digests = {hashlib.sha256(c.encode()).hexdigest() for cs in chunks.values() for c in cs}
        missing = len(digests - set(store.vectors))
        log(f"embedding cache: {len(digests)} unique chunks, {missing} misses to encode")
        dimension = (backend.identity.get("metadata") or {}).get("embedding_length")
        vectors = store.encode([c for cs in chunks.values() for c in cs], embedding_config.batch_size, dimension)
        ordered = [hashlib.sha256(c.encode()).hexdigest() for p in passages for c in chunks[p.passage_id]]
        matrix = np.stack([vectors[d] for d in ordered])
        starts = np.cumsum([0] + [len(chunks[p.passage_id]) for p in passages[:-1]])
        for query in queries:
            dense[query.query_id] = np.maximum.reduceat(matrix @ store.embed_query(query.text, dimension), starts)
        record.update(
            selector=backend.selector,
            cache_id=backend.cache_id,
            unique_chunks=len(digests),
            cache_misses_before_encoding=missing,
            embedding_requests=store.requests,
            largest_input_size=max(store.sizes, default=0),
            largest_query_size=max(store.query_sizes, default=0),
            encoding_contract=backend.contract.to_record() if backend.contract else None,
        )
    by_tf: dict[str, set[int]] = {}
    for item in items:
        if item["passage_id"]:
            by_tf.setdefault(item["tf_hgnc_id"], set()).add(index[item["passage_id"]])
    best: dict[tuple[str, str], tuple[float, str]] = {}
    for query in queries:
        rows = sorted(by_tf.get(query.tf_hgnc_id, ()))
        if not rows:
            continue
        ranks = [np.argsort(np.argsort(-bm25.get_scores(tokenize(query.text)), kind="stable"), kind="stable")]
        if query.query_id in dense:
            ranks.append(np.argsort(np.argsort(-dense[query.query_id], kind="stable"), kind="stable"))
        for row in rows:
            fused = sum(1.0 / (rrf_k + 1 + int(r[row])) for r in ranks)
            key = (passages[row].passage_id, query.tf_hgnc_id)
            if key not in best or fused > best[key][0]:
                best[key] = (fused, query.query_id)
    return best, record


# ---------------------------------------------------------------------------
# Bundles


def build_bundle(
    anchor: Passage, document: Document, document_id: str, mentions: dict[str, list[dict]], genes: set[str]
) -> dict:
    """Anchor plus required/linked context within the serialized limit; nothing is truncated."""
    needed, missing = _context(anchor, document)
    reasons, incomplete = [], list(missing)
    following = next((p for p in document.passages if p.order == anchor.order + 1), None)
    if following is not None and following.section_path == anchor.section_path and BACK_REFERENCE.match(following.text):
        # The next passage continues this one ("In contrast, ..."), often carrying a null or
        # contrasting result without repeating the TF name.
        needed.append((following, "following_passage_continues_anchor", True))

    def records(selected):
        return [part_record(p, document_id, mentions.get(p.passage_id, []), genes) for p in selected]

    parts = [anchor]
    if len(serialize_evidence(records(parts))) > MAX_EVIDENCE_CHARS:
        incomplete.append("serialized_size_exceeds_limit:anchor")
    else:
        for passage, reason, required in needed:
            if passage in parts:
                continue
            trial = sorted([*parts, passage], key=lambda p: p.order)
            if len(trial) > MAX_PARTS or len(serialize_evidence(records(trial))) > MAX_EVIDENCE_CHARS:
                if required:
                    incomplete.append(f"context_not_included:{reason}:{passage.passage_id}")
                continue
            parts = trial
            reasons.append(reason)
    serialized = records(parts)
    text = " ".join(p.text for p in parts)
    return {
        "payload_id": stable_id(
            "payload",
            {"anchor": anchor.passage_id, "parts": [p.passage_id for p in parts], "rules": [PAYLOAD_RULE, SERIAL_RULE]},
        ),
        "document_id": document_id,
        "anchor_passage_id": anchor.passage_id,
        "parts": serialized,
        "part_count": len(parts),
        "serialized_chars": len(serialize_evidence(serialized)),
        "context_reasons": reasons,
        "incomplete_reasons": incomplete,
        "supplement_references": sorted({m.group(0) for m in SUPPLEMENT_REFERENCE.finditer(text)}),
        "flags": [n for n, pat in (("negation_cue", NEGATION), ("comparison_cue", COMPARISON)) if pat.search(text)],
        "rule_version": PAYLOAD_RULE,
        "serialization_rule": SERIAL_RULE,
    }


# Most severe first: a bundle-level status names the worst per-TF status.
IDENTITY_SEVERITY = (
    "ambiguous_source_identifier",
    "name_conflicts_with_source_identifier",
    "case_variant_species_unresolved",
    "name_only_species_unknown",
    "consistent_with_source_identifier",
)


def _one_tf_identity(mentions: list[dict], kinds: set[str]) -> str:
    if any(m.get("resolution") == "ambiguous" for m in mentions):
        return "ambiguous_source_identifier"
    statuses = {m.get("identity_status") for m in mentions}
    if "conflicting_source_identifier" in statuses:
        return "name_conflicts_with_source_identifier"
    if "consistent_with_source_identifier" in statuses:
        return "consistent_with_source_identifier"
    if kinds == {"case_variant_species_unresolved"}:
        return "case_variant_species_unresolved"
    return "name_only_species_unknown"


def tf_identity(payload: dict, kinds_by_tf: dict[str, set[str]]) -> dict:
    """Per candidate TF, the identity the anchor's own mentions support; never upgraded to a human ID.

    Each TF is judged only on its own mentions, so a resolved TF never upgrades another TF in the
    bundle. The bundle is scorable as resolved human associations only if every TF is consistent
    with a source identifier; an ambiguous source identifier for any TF blocks readiness.
    """
    anchor = next(p for p in payload["parts"] if p["passage_id"] == payload["anchor_passage_id"])
    per_tf = {}
    for tf in sorted(kinds_by_tf):
        own = [m for m in anchor["mentions"] if tf in (m.get("candidate_hgnc_id"), m.get("hgnc_id"))]
        status = _one_tf_identity(own, kinds_by_tf[tf])
        per_tf[tf] = {
            "status": status,
            "scorable_as_resolved_human": status == "consistent_with_source_identifier",
            "match_kinds": sorted(kinds_by_tf[tf]),
            # the source's own annotations, verbatim (species kept; never inferred)
            "source_identifiers": [
                {"hgnc_id": h, "resolution": res, "species_taxon": taxon}
                for h, res, taxon in sorted(
                    {
                        (m.get("hgnc_id"), m.get("resolution"), m.get("species_taxon"))
                        for m in own
                        if m.get("identity_status") == "source_identifier"
                    },
                    key=str,
                )
            ],
        }
    statuses = {v["status"] for v in per_tf.values()}
    status = next(x for x in IDENTITY_SEVERITY if x in statuses) if statuses else "name_only_species_unknown"
    return {
        "rule": TF_IDENTITY_RULE,
        "status": status,
        "scorable_as_resolved_human": bool(per_tf) and all(v["scorable_as_resolved_human"] for v in per_tf.values()),
        "resolved_tfs": sorted(t for t, v in per_tf.items() if v["scorable_as_resolved_human"]),
        "unresolved_tfs": sorted(t for t, v in per_tf.items() if not v["scorable_as_resolved_human"]),
        "per_tf": per_tf,
        "match_kinds": sorted({k for v in kinds_by_tf.values() for k in v}),
    }


# ---------------------------------------------------------------------------
# Supplement dependencies


KIND_WORDS = (
    ("extended_figure", r"extended data fig"),
    ("extended_table", r"extended data table"),
    ("table", r"table"),
    ("figure", r"fig"),
    ("movie", r"movie|video"),
    ("data", r"data"),
    ("file", r"additional file"),
)
COVERAGE = re.compile(
    r"(extended data fig\w*\.?|extended data tables?|(?:supplementa\w* )?(?:fig\w*\.?|tables?|data|movies?|videos?))"
    r"\s*S?(\d+)(?:\s*(?:[-–—]|to|through|and)\s*S?(\d+))?",
    re.IGNORECASE,
)


def _kind(text: str) -> str:
    lowered = text.lower()
    return next((kind for kind, pattern in KIND_WORDS if re.search(pattern, lowered)), "information")


def _reference_key(text: str) -> tuple[str, str | None]:
    number = re.search(r"(\d+)\s*[a-z]?\s*$", text.lower())
    return _kind(text), number.group(1) if number else None


def covered_items(text: str) -> set[tuple[str, str]]:
    """(kind, number) pairs a caption or filename states explicitly, including ranges like "Figures S1-S8"."""
    items = set()
    for m in COVERAGE.finditer(text or ""):
        first, last = int(m.group(2)), int(m.group(3) or m.group(2))
        if 0 < last - first < 50:
            items |= {(_kind(m.group(1)), str(n)) for n in range(first, last + 1)}
        else:
            items.add((_kind(m.group(1)), str(first)))
    return items


def resolve_dependency(
    reference: str, supplements: list[dict], captions: dict[str, str] | None = None
) -> tuple[str, list[dict]]:
    """(resolution, matched inventory items) for one supplementary reference of a paper.

    In order of evidence: the item's JATS label, its JATS caption stating the item, then a filename that
    encodes kind and number. A single or generic container is only a candidate; two files of one
    paper are never assumed linked, and nothing is matched by proximity.
    """
    key = _reference_key(reference)
    if key[1] is None:
        return "unresolved_reference", []
    for resolution, text_of in (
        ("resolved_by_label", lambda s: s.get("label") or ""),
        ("resolved_by_caption", lambda s: (captions or {}).get(s["filename"], "")),
        ("resolved_by_filename", lambda s: re.sub(r"[_.-]", " ", s["filename"])),
    ):
        matched = [s for s in supplements if key in covered_items(text_of(s))]
        if matched:
            return resolution, matched
    generic = [
        s
        for s in supplements
        if re.search(
            r"supplement\w* (information|material|data)|appendix|ESM1\b|supp_info",
            f"{s.get('label') or ''} {(captions or {}).get(s['filename'], '')} {s.get('filename')}",
            re.IGNORECASE,
        )
    ]
    if len(supplements) == 1:
        return "single_supplement_container_unverified", supplements
    if generic:
        return "container_candidate_unverified", generic
    return "unresolved_reference", []


# ---------------------------------------------------------------------------
# Readiness and the investigation queue


def readiness(
    payload: dict,
    attributions: set[str],
    abstract_disposition: bool,
    retracted: bool,
    parse: dict,
    dependency_states: list[str],
) -> tuple[str, list[str]]:
    reasons = list(payload["incomplete_reasons"])
    if payload["supplement_references"]:
        reasons.append("cross_asset_context_required:" + "; ".join(payload["supplement_references"][:5]))
    if payload["text_version"] == "pubmed_abstract" and not abstract_disposition:
        reasons.append("abstract_only_requires_recorded_disposition")
    if parse["state"] != "PARSED":
        reasons.append(f"document_parse_{parse['state'].lower()}:" + "; ".join(parse.get("reasons") or [])[:200])
    if retracted:
        reasons.append("retracted_publication_excluded_from_primary_support")
    if not attributions & READY_ATTRIBUTIONS:
        reasons.append("experimental_attribution_unresolved:" + ",".join(sorted(attributions)))
    if (payload.get("tf_identity") or {}).get("status") == "ambiguous_source_identifier":
        reasons.append("tf_identity_ambiguous_source_identifier")
    # Unresolved references with local supplements stay NEEDS_CONTEXT (an investigation); a needed
    # asset that is missing, unsupported, failed, or over the size bound blocks as NEEDS_ASSET.
    if any(
        s in {"missing_asset", "unsupported_format", "parse_failed", "deferred_size_limit"} for s in dependency_states
    ):
        reasons.append("required_supplement_unavailable_or_unresolved")
    if not reasons:
        return ("READY_ABSTRACT_ONLY" if payload["text_version"] == "pubmed_abstract" else "READY_FULL_TEXT"), []
    for prefix, state in (
        ("document_parse", "NEEDS_PARSE_REPAIR"),
        ("abstract_only", "NEEDS_ASSET"),
        ("required_supplement", "NEEDS_ASSET"),
        ("retracted", "NEEDS_SCREENING_REVIEW"),
        ("experimental_attribution", "NEEDS_SCREENING_REVIEW"),
        ("tf_identity_ambiguous", "NEEDS_SCREENING_REVIEW"),
    ):
        if any(r.startswith(prefix) for r in reasons):
            return state, reasons
    return "NEEDS_CONTEXT", reasons


INVESTIGABLE = (
    "cross_asset_context_required",
    "referenced_figure_caption_not_found",
    "context_not_included",
    "back_reference_target_unavailable",
    "serialized_size_exceeds_limit",
    "table_caption_missing",
    "table_header_unavailable",
)


def investigations(
    payloads: list[dict], dependencies: list[dict], local_sources: dict[str, list[str]] | None = None
) -> list[dict]:
    """Context questions whose sources are local, for P4's bounded assembly (queued, never run here).

    Only NEEDS_CONTEXT payloads qualify; missing assets, parse repairs, and attribution review stay
    with P3/lead review. An unresolved or container-only reference may navigate the publication's own
    local parsed sources (at most MAX_NAVIGATION_ASSETS); sharing a publication does not establish that
    a source describes the same experiment. Deduplicated investigations keep every anchor and bundle.
    """
    by_payload: dict[str, list[dict]] = {}
    for dep in dependencies:
        by_payload.setdefault(dep["payload_id"], []).append(dep)
    queue: dict[str, dict] = {}
    for payload in payloads:
        if payload["readiness_state"] != "NEEDS_CONTEXT":
            continue
        for reason in payload["readiness_reasons"]:
            gap = reason.split(":")[0]
            if gap not in INVESTIGABLE:
                continue
            deps = by_payload.get(payload["payload_id"], []) if gap == "cross_asset_context_required" else []
            matched = {a for d in deps for a in d["local_asset_sha256"]}
            navigate = gap == "cross_asset_context_required" and any(
                d.get("state", "") == "unresolved_reference" or d.get("state", "").endswith("link_unverified")
                for d in deps
            )
            candidates = (
                set((local_sources or {}).get(payload["pmid"], [])[:MAX_NAVIGATION_ASSETS]) if navigate else set()
            )
            assets = sorted(matched | candidates | {payload["source_asset_sha256"]})
            detail = reason.split(":", 1)[1] if ":" in reason else ""
            key = stable_id(
                "investigation",
                {"publication": payload["publication_id"], "gap": gap, "detail": detail, "assets": assets},
            )
            entry = queue.setdefault(
                key,
                {
                    "investigation_id": key,
                    "publication_id": payload["publication_id"],
                    "pmid": payload["pmid"],
                    "gap_type": gap,
                    "detail": detail,
                    "permitted_asset_sha256": assets,
                    "navigation_scope": (
                        "same_publication_local_sources (experiment link unverified)"
                        if candidates
                        else "matched_sources_only"
                    ),
                    "anchor_part_ids": [],
                    "bundle_ids": [],
                    "manuscript_lineages": [],
                    "question": f"Locate the source context needed for '{gap}' ({detail[:200]}) within the permitted "
                    "assets of this publication, or report that it is not present.",
                    "status": "QUEUED_NOT_RUN",
                    "rule_version": DEPENDENCY_RULE,
                },
            )
            entry["anchor_part_ids"] = sorted(set(entry["anchor_part_ids"]) | {payload["anchor_passage_id"]})
            entry["bundle_ids"] = sorted(set(entry["bundle_ids"]) | {payload["payload_id"]})
            entry["manuscript_lineages"] = sorted(set(entry["manuscript_lineages"]) | set(payload["lineages"]))
    return sorted(queue.values(), key=lambda q: q["investigation_id"])


def ready_batches(payloads: list[dict], lineages: list[str], limits) -> list[dict]:
    """Deterministic ready batches: lineage rotation, then retrieval priority; every ready payload is queued."""
    ready = [p for p in payloads if p["readiness_state"].startswith("READY")]
    queues = {
        c: sorted((p for p in ready if c in p["lineages"]), key=lambda p: (-p["priority"], p["payload_id"]))
        for c in lineages
    }
    order, seen, round_index = [], set(), 0
    while any(queues.values()):
        start = round_index % len(lineages)
        for cell_type in lineages[start:] + lineages[:start]:
            while queues[cell_type]:
                payload = queues[cell_type].pop(0)
                if payload["payload_id"] not in seen:
                    seen.add(payload["payload_id"])
                    order.append(payload)
                    break
        round_index += 1
    per_bundle_calls = 2
    capacity = min(limits.max_bundles, limits.max_scheduled_calls // per_bundle_calls)
    batches, pending = [], order
    while pending:
        batch, papers, rest = [], set(), []
        for payload in pending:
            fits_paper = payload["publication_id"] in papers or len(papers) < limits.max_papers
            if len(batch) < capacity and fits_paper:
                batch.append(payload)
                papers.add(payload["publication_id"])
            else:
                rest.append(payload)
        batches.append(batch)
        pending = rest
    return [
        {
            "batch_index": i,
            "payload_ids": [p["payload_id"] for p in b],
            "papers": sorted({p["publication_id"] for p in b}),
            "scheduled_calls": per_bundle_calls * len(b),
        }
        for i, b in enumerate(batches, start=1)
    ]


def batch_manifest(batch: dict, payloads: dict[str, dict], inputs: dict) -> dict:
    items = []
    for payload_id in batch["payload_ids"]:
        p = payloads[payload_id]
        items.append(
            {
                "payload_id": payload_id,
                "evidence_sha256": sha256_text(serialize_evidence(p["parts"])),
                "serialized_chars": p["serialized_chars"],
                "publication_id": p["publication_id"],
                "pmid": p["pmid"],
                "document_id": p["document_id"],
                "source_asset_sha256": p["source_asset_sha256"],
                "parts": [
                    {
                        "passage_id": x["passage_id"],
                        "locator": x["locator"],
                        "asset_sha256": x["asset_sha256"],
                        "text_sha256": hashlib.sha256(x["text"].encode()).hexdigest(),
                    }
                    for x in p["parts"]
                ],
                "context_complete": not p["readiness_reasons"],
                "readiness_state": p["readiness_state"],
                "lineages": p["lineages"],
                "relevance": p["relevance"],
                "passage_relevance": p.get("passage_relevance"),
                "tf_hgnc_ids": p["tf_hgnc_ids"],
                "tf_identity": p.get("tf_identity"),
            }
        )
    body = {
        **batch,
        "items": items,
        "inputs": inputs,
        "status": "prepared_not_frozen_pending_corpus_checkpoint_and_model_selection",
    }
    return {**body, "manifest_sha256": sha256_text(canonical_json(body))}


# ---------------------------------------------------------------------------
# Budget (estimates; no tokenizer or prompt exists yet)


def budget(
    payloads: list[dict], batches: list[dict], queue: list[dict], assumptions: BudgetAssumptions, lineages: list[str]
) -> dict:
    """Scenario estimates (no model calls). Modeled scenarios are labelled; the only genuine configured
    ceiling is the assembly contract's (4 calls x 8,000 input / 1,000 output tokens per investigation).
    Extraction/verification have no configured ceiling yet, so their "conservative" rows are scenarios.
    """
    a = assumptions
    tokens = lambda chars: math.ceil(chars / a.chars_per_token)  # noqa: E731
    ready = [p for p in payloads if p["readiness_state"].startswith("READY")]
    by_id = {p["payload_id"]: p for p in payloads}

    def extraction(evidence_chars: list[int], scenario: str) -> dict:
        conservative = scenario == "conservative"
        attempts = a.max_attempts_per_call if conservative else 1
        out_x = a.extractor_output_tokens_cap if conservative else a.extractor_output_tokens_typical
        out_v = a.verifier_output_tokens_cap if conservative else a.verifier_output_tokens_typical
        reason = a.reasoning_tokens_cap if conservative else a.reasoning_tokens_typical
        n, content = len(evidence_chars), sum(tokens(c) for c in evidence_chars)
        return {
            "input": attempts * (n * (a.extractor_overhead_tokens + a.verifier_overhead_tokens + out_x) + 2 * content),
            "output": attempts * n * (out_x + out_v + 2 * reason),
            "calls": attempts * 2 * n,
        }

    def assembly(n: int, scenario: str) -> dict:
        cap_in, cap_out = a.assembly["input_tokens_cap_per_call"], 1000
        if scenario == "ceiling":
            return {"input": n * 4 * cap_in, "output": n * 4 * cap_out, "calls": n * 4}
        s = a.assembly["conservative" if scenario == "conservative" else scenario]
        per = sum(
            min(cap_in, s["first_call_input_tokens"] + i * s["history_growth_per_call_tokens"])
            for i in range(s["calls"])
        )
        return {
            "input": n * per,
            "output": n * s["calls"] * min(cap_out, s["output_tokens_per_call"]),
            "calls": n * s["calls"],
        }

    def preflight(n_batches: int, scenario: str) -> dict:
        attempts = a.max_attempts_per_call if scenario in {"conservative", "ceiling"} else 1
        calls = n_batches * (a.schema_preflight_calls + a.assembly["preflight_calls_per_batch"]) * attempts
        return {"input": calls * a.extractor_overhead_tokens, "output": calls * 200, "calls": calls}

    def total(*parts: dict) -> dict:
        return {k: sum(p[k] for p in parts) for k in ("input", "output", "calls")}

    # Downstream of assembly: each linked blocked bundle yields at most one repaired bundle (deduplicated
    # across investigations) of at most 6,000 serialized characters. More children would be dependent on
    # P4's outcome and must be re-budgeted then.
    repaired = sorted({b for q in queue for b in q.get("bundle_ids", [])})
    repaired_chars = [min(by_id[b]["serialized_chars"], MAX_EVIDENCE_CHARS) for b in repaired if b in by_id]
    ready_chars = [p["serialized_chars"] for p in ready]
    # Hypothetical: every payload ready, oversized evidence split into <= 6,000-character children.
    split_chars = [c for p in payloads for c in _split(p["serialized_chars"])]
    investigation_batches = math.ceil(len(queue) / 20)
    scenarios = {}
    for scenario in ("low", "typical", "conservative", "ceiling"):
        ex_scenario = "conservative" if scenario in {"conservative", "ceiling"} else "typical"
        scenarios[scenario] = {
            "current_ready_only": total(extraction(ready_chars, ex_scenario), preflight(len(batches), scenario)),
            "assembly_only_no_result": total(
                assembly(len(queue), scenario), preflight(investigation_batches, scenario)
            ),
            "assembly_plus_downstream": total(
                assembly(len(queue), scenario),
                preflight(investigation_batches, scenario),
                extraction(repaired_chars, ex_scenario),
            ),
            "hypothetical_all_payloads_split": total(
                extraction(split_chars, ex_scenario), preflight(math.ceil(len(split_chars) / 20), scenario)
            ),
        }

    def costs(sums: dict) -> dict:
        return {
            name: round((sums["input"] * rin + sums["output"] * rout) / 1_000_000, 2)
            for name, (rin, rout) in a.illustrative_rates.items()
        }

    sizes = sorted(tokens(p["serialized_chars"]) for p in payloads)
    return {
        "status": "ESTIMATE_ONLY: no tokenizer, prompt, or schema is final; prices are illustrative, not verified",
        "assumptions": a.model_dump(),
        "counts": {
            "payloads": len(payloads),
            "ready": len(ready),
            "ready_batches": len(batches),
            "context_investigations": len(queue),
            "repaired_bundles_bound": len(repaired_chars),
            "hypothetical_split_children": len(split_chars),
            "evidence_tokens_per_payload": {
                "min": sizes[0] if sizes else 0,
                "median": sizes[len(sizes) // 2] if sizes else 0,
                "max": sizes[-1] if sizes else 0,
            },
        },
        "scenarios": {s: {name: {**v, "usd": costs(v)} for name, v in rows.items()} for s, rows in scenarios.items()},
        "ready_by_lineage_overlapping": {c: sum(c in p["lineages"] for p in ready) for c in lineages},
        "notes": [
            "Rows: current_ready_only = extraction/verification of source-ready bundles + preflight; "
            "assembly_only_no_result = investigations that find nothing (no downstream calls); "
            "assembly_plus_downstream = assembly + extraction/verification of each linked repaired bundle once; "
            "hypothetical_all_payloads_split = every payload, oversized evidence split into <= 6,000-char children.",
            "'ceiling' applies the assembly contract's configured maximum (4 x 8,000 input, 4 x 1,000 output incl. "
            "reasoning); extraction/verification and preflight have no configured ceiling, so they use the "
            "conservative scenario there.",
            "Downstream bound: at most one repaired bundle per linked blocked bundle; more is P4-dependent.",
            "Evidence tokens = serialize_evidence() characters / chars_per_token; overhead is counted per call.",
            "The planning reserve is a margin, not an enforced ceiling; no caching discount is assumed.",
        ],
    }


def _split(chars: int) -> list[int]:
    if chars <= MAX_EVIDENCE_CHARS:
        return [chars]
    full, rest = divmod(chars, MAX_EVIDENCE_CHARS)
    return [MAX_EVIDENCE_CHARS] * full + ([rest] if rest else [])
