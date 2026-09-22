"""Deterministic literature retrieval queue. Nothing here searches; every row is NOT_SEARCHED.

Query text is a service-neutral boolean string (quoted phrases, AND/OR); P3 adapts it to the
chosen API. No publication-date restriction is applied.
"""

from __future__ import annotations

import json

import pandas as pd

from regkg.analysis.gene_mapping import safe_aliases
from regkg.config import RetrievalQueueConfig
from regkg.provenance import stable_id

TYPE_ASSAY = "tf_target_regulatory_assay"
TYPE_CONTEXT = "tf_lung_context"
TYPE_NULL = "tf_target_null_or_negative"
STATUS_NOT_SEARCHED = "NOT_SEARCHED"


def _quoted(term: str) -> str:
    return '"' + term.replace('"', "") + '"'


def _group(terms: list[str]) -> str:
    return "(" + " OR ".join(_quoted(t) for t in terms) + ")"


def build_queue(
    candidates: pd.DataFrame,
    targets: pd.DataFrame,
    names: dict[str, list[str]],
    config: RetrievalQueueConfig,
    scope: dict | None = None,
) -> pd.DataFrame:
    """One row per distinct query; candidates sharing a query are listed on it.

    `scope` (e.g. a manuscript lineage) joins the query identity, so the same text requested for
    two lineages stays two queries with separate nomination contexts; the AT1 baseline passes none.

    `names` maps an HGNC ID to [approved symbol, *safe aliases]. Priority interleaves TFs: each
    TF's first query precedes any TF's second one, seeds before other candidates, then HGNC ID.
    Manuscript seed order is deliberately not used.
    """
    queries: dict[str, dict] = {}

    def add(query_type: str, tf: str, target: str | None, rank: int, effect: float | None, candidate) -> None:
        tf_terms, target_terms = names[tf], names[target] if target else []
        parts = [_group(tf_terms)]
        if target:
            parts.append(_group(target_terms))
        extra = {TYPE_ASSAY: config.assay_terms, TYPE_NULL: config.null_terms, TYPE_CONTEXT: config.context_terms}[
            query_type
        ]
        parts.append(_group(extra))
        text = " AND ".join(parts)
        identity = {"version": config.query_version, "type": query_type, "tf": tf, "target": target, "text": text}
        query_id = stable_id("query", identity if scope is None else {**identity, "scope": scope})
        entry = queries.setdefault(
            query_id,
            {
                "query_id": query_id,
                "query_type": query_type,
                "query_text": text,
                "terms_json": json.dumps(
                    {"tf": tf_terms, "target": target_terms, "qualifiers": extra}, ensure_ascii=False
                ),
                "tf_hgnc_id": tf,
                "tf_symbol": tf_terms[0],
                "target_hgnc_id": target,
                "target_symbol": target_terms[0] if target else None,
                "candidate_ids": set(),
                "comparison_ids": set(),
                "conditions": set(),
                "reasons": set(),
                "source_routes": set(),
                "best_target_rank": rank,
                "max_abs_effect": abs(effect) if effect is not None else None,
                "is_seed_tf": False,
            },
        )
        entry["candidate_ids"].add(candidate.candidate_id)
        entry["comparison_ids"].add(candidate.comparison_id)
        entry["conditions"].add(candidate.condition)
        entry["reasons"].update(candidate.reasons)
        entry["is_seed_tf"] |= bool(candidate.is_seed)
        entry["best_target_rank"] = min(entry["best_target_rank"], rank)
        if effect is not None:
            entry["max_abs_effect"] = max(entry["max_abs_effect"], abs(effect))
        return entry

    by_candidate = targets.groupby("candidate_id") if len(targets) else {}
    for candidate in candidates.itertuples(index=False):
        add(TYPE_CONTEXT, candidate.tf_hgnc_id, None, 0, None, candidate)
        chosen = (
            by_candidate.get_group(candidate.candidate_id)
            if len(targets) and candidate.candidate_id in by_candidate.groups
            else None
        )
        if chosen is None:
            continue  # TF-only retrieval: no eligible target, none invented
        for target in chosen.itertuples(index=False):
            entry = add(
                TYPE_ASSAY,
                candidate.tf_hgnc_id,
                target.target_hgnc_id,
                target.target_rank,
                target.effect_niche2_minus_niche1,
                candidate,
            )
            entry["source_routes"].update(target.source_routes)
            if target.target_rank == 1:
                entry = add(
                    TYPE_NULL,
                    candidate.tf_hgnc_id,
                    target.target_hgnc_id,
                    1,
                    target.effect_niche2_minus_niche1,
                    candidate,
                )
                entry["source_routes"].update(target.source_routes)

    frame = pd.DataFrame(queries.values())
    if frame.empty:
        return frame
    for column in ["candidate_ids", "comparison_ids", "conditions", "reasons", "source_routes"]:
        frame[column] = frame[column].map(sorted)

    # Per-TF sequence: assay queries by target rank then |effect| then target; the context query
    # second (first when the TF has no target); the null-phrasing query last.
    type_order = {TYPE_ASSAY: 0, TYPE_CONTEXT: 1, TYPE_NULL: 2}
    frame["_type"] = frame["query_type"].map(type_order)
    frame["_effect"] = -frame["max_abs_effect"].fillna(0.0)
    frame = frame.sort_values(
        ["tf_hgnc_id", "_type", "best_target_rank", "_effect", "target_hgnc_id"], kind="mergesort", na_position="first"
    )
    positions = []
    for _, group in frame.groupby("tf_hgnc_id", sort=False):
        order = list(group.index)
        assays = [i for i in order if group.loc[i, "query_type"] == TYPE_ASSAY]
        contexts = [i for i in order if group.loc[i, "query_type"] == TYPE_CONTEXT]
        nulls = [i for i in order if group.loc[i, "query_type"] == TYPE_NULL]
        sequence = assays[:1] + contexts + assays[1:] + nulls if assays else contexts + nulls
        positions.extend((index, position) for position, index in enumerate(sequence))
    frame.loc[[i for i, _ in positions], "tf_query_position"] = [p for _, p in positions]
    frame["_group"] = (~frame["is_seed_tf"]).astype(int)
    frame = frame.sort_values(["tf_query_position", "_group", "tf_hgnc_id"], kind="mergesort").reset_index(drop=True)
    frame["priority"] = range(1, len(frame) + 1)
    frame["in_initial_live_slice"] = frame["priority"] <= config.max_live_queries
    frame["search_status"] = STATUS_NOT_SEARCHED
    frame["date_restriction"] = None
    frame["query_version"] = config.query_version
    frame["tf_query_position"] = frame["tf_query_position"].astype(int)
    return frame.drop(columns=["_type", "_effect", "_group"])


def query_names(hgnc_ids: set[str], hgnc: pd.DataFrame, limit: int) -> dict[str, list[str]]:
    symbol = dict(zip(hgnc["hgnc_id"], hgnc["symbol"], strict=True))
    return {h: [symbol[h], *safe_aliases(h, hgnc, limit)] for h in sorted(hgnc_ids) if h}


def schedule_queries(queues: dict[str, pd.DataFrame], batch_size: int) -> pd.DataFrame:
    """Interleave per-lineage queues into one deterministic order and fixed batches.

    Each round takes the next query of every lineage that still has one, keeping each lineage's
    own priority order. The first lineage rotates by round (lineages sorted by label), so none has
    standing priority, and a lineage with a long queue cannot starve the others.
    """
    lineages = sorted(queues)
    pending = {name: list(queues[name].sort_values("lineage_priority")["query_id"]) for name in lineages}
    order: list[tuple[str, str]] = []
    round_index = 0
    while any(pending.values()):
        start = round_index % len(lineages)
        for name in lineages[start:] + lineages[:start]:
            if pending[name]:
                order.append((name, pending[name].pop(0)))
        round_index += 1
    frame = pd.DataFrame(order, columns=["cell_type", "query_id"])
    frame["schedule_position"] = range(1, len(frame) + 1)
    frame["batch_index"] = (frame["schedule_position"] - 1) // batch_size + 1
    return frame


def next_pending(schedule: pd.DataFrame, searched_query_ids: set[str], limit: int) -> pd.DataFrame:
    """Resume point: the first `limit` scheduled queries not yet searched, in schedule order."""
    remaining = schedule[~schedule["query_id"].isin(searched_query_ids)]
    return remaining.sort_values("schedule_position").head(limit)
