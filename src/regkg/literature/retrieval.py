"""Passage retrieval per executed query and bounded evidence bundles.

Scores combine exact candidate-name hits, BM25 over section-aware passages, and (when configured)
selected-model embeddings via reciprocal-rank fusion. Co-occurrence of a TF, a target, and an
assay word is a retrieval reason only; bundles are evidence candidates, never accepted findings.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass

import numpy as np
from rank_bm25 import BM25Okapi

from regkg.config import BundleConfig, RetrievalConfig
from regkg.literature.parse import CAPTION_PRESENT, FIGURE_REFERENCE, Document, Passage
from regkg.literature.publications import term_pattern
from regkg.provenance import stable_id

TOKEN = re.compile(r"[a-z0-9]+(?:[-.][a-z0-9]+)*")
BACK_REFERENCE = re.compile(
    r"^(?:This|These|Those|Such|In contrast|However|Conversely|Similarly|Likewise|Moreover|Furthermore|"
    r"Consistent with|Together|Accordingly|Thus|Therefore)\b"
)
NEGATION = re.compile(
    r"\b(?:not|no|without|failed to|unaffected|absence|neither|nor|did not|does not|cannot)\b|n't", re.IGNORECASE
)
COMPARISON = re.compile(r"\b(?:compared (?:with|to)|versus|vs\.?|relative to|control|than)\b", re.IGNORECASE)
BUNDLE_STATUS = "evidence_candidate_not_accepted"
BUNDLE_RULE = "p3-bundles-3"


def tokenize(text: str) -> list[str]:
    return TOKEN.findall(text.lower())


@dataclass
class QueryTerms:
    query_id: str
    priority: int
    tf_hgnc_id: str
    tf_terms: list[str]
    target_hgnc_id: str | None
    target_terms: list[str]
    qualifiers: list[str]
    candidate_ids: list[str]

    @property
    def text(self) -> str:
        return " ".join(self.tf_terms + self.target_terms + self.qualifiers)


@dataclass
class Hit:
    query_id: str
    passage_id: str
    publication_id: str
    rank: int
    exact_tf: bool
    exact_target: bool
    bm25_score: float
    bm25_rank: int | None
    dense_score: float | None
    dense_rank: int | None
    fused_score: float
    reasons: list[str]


def rank_passages(
    query: QueryTerms,
    passages: list[Passage],
    owners: list[str],
    bm25: BM25Okapi,
    dense: np.ndarray | None,
    config: RetrievalConfig,
) -> list[Hit]:
    """Order: exact TF mention, exact target mention, fused BM25/dense rank, passage order (stable)."""
    if not passages:
        return []
    scores = bm25.get_scores(tokenize(query.text))
    bm25_order = [i for i in np.argsort(-scores, kind="stable") if scores[i] > 0]
    bm25_rank = {int(i): r for r, i in enumerate(bm25_order, start=1)}
    dense_rank = {}
    if dense is not None:
        dense_rank = {int(i): r for r, i in enumerate(np.argsort(-dense, kind="stable"), start=1)}
    rows = []
    for index, passage in enumerate(passages):
        exact_tf = any(term_pattern(t).search(passage.text) for t in query.tf_terms)
        exact_target = bool(query.target_terms) and any(
            term_pattern(t).search(passage.text) for t in query.target_terms
        )
        fused = sum(1.0 / (config.rrf_k + rank) for rank in (bm25_rank.get(index), dense_rank.get(index)) if rank)
        reasons = [
            name
            for name, flag in (
                ("exact_tf", exact_tf),
                ("exact_target", exact_target),
                ("bm25", index in bm25_rank),
                ("dense", dense is not None),
            )
            if flag
        ]
        rows.append((index, exact_tf, exact_target, fused, reasons))
    rows.sort(key=lambda r: (-int(r[1]), -int(r[2]), -r[3], r[0]))
    hits = []
    for rank, (index, exact_tf, exact_target, fused, reasons) in enumerate(rows[: config.hits_per_query], start=1):
        hits.append(
            Hit(
                query.query_id,
                passages[index].passage_id,
                owners[index],
                rank,
                exact_tf,
                exact_target,
                float(scores[index]),
                bm25_rank.get(index),
                None if dense is None else float(dense[index]),
                dense_rank.get(index),
                fused,
                reasons,
            )
        )
    return hits


@dataclass
class Bundle:
    bundle_id: str
    publication_id: str
    query_id: str
    # Retrieval context from the P2 queue, not entities extracted from the passages.
    retrieval_candidate_ids: list[str]
    retrieval_tf_hgnc_id: str
    retrieval_target_hgnc_id: str | None
    anchor_passage_id: str
    passages: list[dict]
    total_chars: int
    context_reasons: list[str]
    incomplete_reasons: list[str]
    flags: list[str]
    retrieval: dict
    status: str = BUNDLE_STATUS
    rule_version: str = BUNDLE_RULE

    @property
    def extraction_ready(self) -> bool:
        return not self.incomplete_reasons

    def to_json(self) -> dict:
        return {**asdict(self), "context_complete": self.extraction_ready, "extraction_ready": self.extraction_ready}


def _context(anchor: Passage, document: Document) -> tuple[list[tuple[Passage, str, bool]], list[str]]:
    """(passage, reason, required) in priority order, plus context that is missing in the source."""
    by_order = {p.order: p for p in document.passages}
    needed: list[tuple[Passage, str, bool]] = []
    missing: list[str] = []
    if anchor.kind in {"table_row", "table_footnote"}:
        same_table = [p for p in document.passages if p.table_id and p.table_id == anchor.table_id]
        if anchor.table_id is None:
            missing.append("table_identity_unavailable")
        # Caption policy: a table-row finding needs the table caption; a missing caption (or a label
        # alone) is recorded as incomplete. A label-only passage is still included for inspection.
        if anchor.table_caption_status != CAPTION_PRESENT:
            missing.append(f"table_caption_missing:{anchor.table_caption_status or 'unknown'}")
        needed += [
            (p, "table_caption", anchor.table_caption_status == CAPTION_PRESENT)
            for p in same_table
            if p.kind == "table_caption"
        ]
        needed += [(p, "table_footnote", True) for p in same_table if p.kind == "table_footnote" and p is not anchor]
        if anchor.table_structure != "header_grid_expanded":
            # No faithful column semantics: the row is kept for inspection but is not extraction-ready.
            missing.append(f"table_header_unavailable:{anchor.table_structure or 'unknown'}")
        # Header source rows are included for inspection when room remains; column semantics are
        # already bound to each cell in `cells` for supported layouts.
        needed += [(p, "table_header_source_row", False) for p in same_table if p.kind == "table_header"]
    if anchor.kind in {"paragraph", "abstract"} and BACK_REFERENCE.match(anchor.text):
        previous = by_order.get(anchor.order - 1)
        if previous is not None and previous.section_path == anchor.section_path:
            needed.append((previous, "preceding_passage_for_back_reference", True))
        else:
            missing.append("back_reference_target_unavailable")
    captions = {}
    for passage in document.passages:
        if passage.kind == "figure_caption" and passage.item_label:
            number = re.search(r"(\d+)", passage.item_label)
            if number:
                captions.setdefault(number.group(1), passage)
    for label in sorted({m.group(1) for m in FIGURE_REFERENCE.finditer(anchor.text)}, key=int):
        if label in captions:
            needed.append((captions[label], "referenced_figure_caption", True))
        elif anchor.kind != "figure_caption":
            missing.append(f"referenced_figure_caption_not_found:{label}")
    return needed, missing


def assemble_bundles(
    queries: list[QueryTerms],
    hits: dict[str, list[Hit]],
    documents: dict[str, Document],
    passages: dict[str, Passage],
    config: BundleConfig,
    mentions: dict[str, list[dict]] | None = None,
) -> tuple[list[Bundle], list[dict]]:
    """Round-robin over queries in priority order; each round takes the next unused exact-TF anchor."""
    bundles: list[Bundle] = []
    rejected: list[dict] = []
    per_paper: dict[str, int] = {}
    per_tf: dict[str, int] = {}
    used: set[str] = set()
    cursors = {q.query_id: 0 for q in queries}
    ordered = sorted(queries, key=lambda q: q.priority)
    progress = True
    while len(bundles) < config.max_bundles and progress:
        progress = False
        for query in ordered:
            if len(bundles) >= config.max_bundles:
                break
            candidates = hits.get(query.query_id, [])
            while cursors[query.query_id] < len(candidates):
                hit = candidates[cursors[query.query_id]]
                cursors[query.query_id] += 1
                if not hit.exact_tf or hit.passage_id in used:
                    continue
                if (
                    per_paper.get(hit.publication_id, 0) >= config.max_per_paper
                    or per_tf.get(query.tf_hgnc_id, 0) >= config.max_per_candidate_tf
                ):
                    continue
                bundle = _bundle(
                    query, hit, documents[hit.publication_id], passages[hit.passage_id], config, mentions or {}
                )
                if bundle is None:
                    rejected.append(
                        {"query_id": query.query_id, "passage_id": hit.passage_id, "reason": "anchor_exceeds_max_chars"}
                    )
                    continue
                bundles.append(bundle)
                used.add(hit.passage_id)
                per_paper[hit.publication_id] = per_paper.get(hit.publication_id, 0) + 1
                per_tf[query.tf_hgnc_id] = per_tf.get(query.tf_hgnc_id, 0) + 1
                progress = True
                break
    return bundles, rejected


def _bundle(
    query: QueryTerms,
    hit: Hit,
    document: Document,
    anchor: Passage,
    config: BundleConfig,
    mentions: dict[str, list[dict]],
) -> Bundle | None:
    if len(anchor.text) > config.max_chars:
        return None
    chosen = [anchor]
    needed, missing = _context(anchor, document)
    reasons, incomplete = [], list(missing)
    for passage, reason, required in needed:
        if passage in chosen:
            continue
        total = sum(len(p.text) for p in chosen) + len(passage.text)
        if len(chosen) >= config.max_passages or total > config.max_chars:
            # Required context that does not fit is reported, never silently cut.
            if required:
                incomplete.append(f"context_not_included:{reason}:{passage.passage_id}")
            continue
        chosen.append(passage)
        reasons.append(reason)
    chosen.sort(key=lambda p: p.order)
    text = " ".join(p.text for p in chosen)
    flags = [
        name for name, pattern in (("negation_cue", NEGATION), ("comparison_cue", COMPARISON)) if pattern.search(text)
    ]
    return Bundle(
        bundle_id=stable_id(
            "bundle",
            {"query_id": query.query_id, "passages": [p.passage_id for p in chosen], "rule": BUNDLE_RULE},
        ),
        publication_id=document.publication_id,
        query_id=query.query_id,
        retrieval_candidate_ids=query.candidate_ids,
        retrieval_tf_hgnc_id=query.tf_hgnc_id,
        retrieval_target_hgnc_id=query.target_hgnc_id,
        anchor_passage_id=anchor.passage_id,
        passages=[
            {
                "passage_id": p.passage_id,
                "kind": p.kind,
                "section_path": p.section_path,
                "section_type": p.section_type,
                "start": p.start,
                "end": p.end,
                "locator": p.locator,
                "asset_sha256": p.asset_sha256,
                "text": p.text,
                "is_anchor": p is anchor,
                "table_id": p.table_id,
                "table_caption_status": p.table_caption_status,
                "table_structure": p.table_structure,
                "table_header": p.table_header,
                "cells": p.cells,
                "mentions": mentions.get(p.passage_id, []),
            }
            for p in chosen
        ],
        total_chars=sum(len(p.text) for p in chosen),
        context_reasons=reasons,
        incomplete_reasons=incomplete,
        flags=flags,
        retrieval={
            "rank": hit.rank,
            "reasons": hit.reasons,
            "bm25_score": hit.bm25_score,
            "dense_score": hit.dense_score,
            "fused_score": hit.fused_score,
        },
    )
