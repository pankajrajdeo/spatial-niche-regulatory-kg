"""A proposed P4 pilot (at most 10 papers / 20 bundles) drawn from a published corpus artifact.

The proposal is for lead review. It is written under reports/ and never changes the immutable corpus
artifact. Selection is deterministic (rule PILOT_RULE); it is a screening choice, not evidence that a
bundle holds a valid regulatory finding in the manuscript cell population.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

import pandas as pd

from regkg.config import LoadedProjectConfig
from regkg.literature.ontology import build_context
from regkg.literature.screening import source_context
from regkg.provenance import canonical_json, sha256_file, sha256_text, utc_now
from regkg.workflows import corpus as c
from regkg.workflows import corpus_ready as r

PILOT_RULE = "p3-pilot-proposal-2"  # 2: per-association TF identity; cell class named in the anchor
MAX_PAPERS, MAX_BUNDLES, MAX_PER_LINEAGE, MAX_PER_PAPER = 10, 20, 5, 3

# Context strength for one (bundle, lineage) association, strongest first. Passage labels are the
# passage's own stated context; paper labels only rank. Background/resource and irrelevant are excluded.
CONTEXT_TIERS = (
    ("passage_direct", lambda a: a["passage_relevance"] == "direct_context_candidate"),
    ("paper_direct_passage_unresolved", lambda a: a["relevance"] == "direct_context_candidate"),
    ("passage_transferable", lambda a: a["passage_relevance"] == "potentially_transferable_mechanism"),
    ("paper_transferable_passage_unresolved", lambda a: a["relevance"] == "potentially_transferable_mechanism"),
    ("unresolved", lambda a: a["relevance"] == "unresolved"),
)
EXCLUDED_LABELS = {"irrelevant_to_assigned_question", "biological_background_resource"}


def _tier(association: dict) -> int | None:
    if {association["relevance"], association["passage_relevance"]} & EXCLUDED_LABELS:
        return None
    return next((i for i, (_, test) in enumerate(CONTEXT_TIERS) if test(association)), None)


def eligibility(payload: dict) -> list[str]:
    """Bundle-level reasons a ready bundle is outside the pilot pool (empty = may contribute)."""
    reasons = []
    if payload["readiness_state"] != "READY_FULL_TEXT":
        reasons.append("not_source_ready")
    if "source_result_candidate" not in payload["attributions"]:
        reasons.append("no_source_result_candidate_attribution")
    if not payload["tf_identity"]["resolved_tfs"]:
        reasons.append("no_tf_consistent_with_source_identifier")
    return reasons


def association_reason(payload: dict, association: dict, cell_mention: str | None) -> str | None:
    """Why one (bundle, lineage, TF) association cannot enter the pool, or None."""
    if not payload["tf_identity"]["per_tf"][association["tf_hgnc_id"]]["scorable_as_resolved_human"]:
        return "association_tf_not_consistent_with_source_identifier"  # judged per TF, never per bundle
    if _tier(association) is None:
        return "context_label_background_or_irrelevant"
    if cell_mention is None:
        return "anchor_does_not_name_lineage_cell_class"
    return None


def candidates(
    payloads: list[dict], named: dict[str, set[str]], cell_mentions: dict[str, dict[str, str | None]]
) -> tuple[dict[str, list[dict]], dict[str, dict[str, int]]]:
    """Per lineage, eligible (bundle, lineage) options with their best context tier, and per lineage the
    count of associations excluded by each reason.

    `cell_mentions[payload_id][lineage]` is "strict", "broad" or None: whether the anchor passage itself
    names the manuscript cell (strict) or its cell class (broad), e.g. fibroblast for fibrotic fibroblasts.
    """
    options: dict[str, list[dict]] = {lineage: [] for lineage in named}
    excluded: dict[str, dict[str, int]] = {lineage: {} for lineage in named}
    for payload in payloads:
        bundle_reasons = eligibility(payload)
        for lineage in named:
            own = [a for a in payload["associations"] if a["cell_type"] == lineage]
            mention = cell_mentions.get(payload["payload_id"], {}).get(lineage)
            usable = []
            for a in own:
                reason = bundle_reasons[0] if bundle_reasons else association_reason(payload, a, mention)
                if reason:
                    excluded[lineage][reason] = excluded[lineage].get(reason, 0) + 1
                else:
                    usable.append((_tier(a), a["tf_hgnc_id"]))
            if not usable:
                continue
            best = min(t for t, _ in usable)
            tfs = sorted({tf for t, tf in usable if t == best})
            options[lineage].append(
                {
                    "payload_id": payload["payload_id"],
                    "pmid": payload["pmid"],
                    "lineage": lineage,
                    "tier": best,
                    "context_tier": CONTEXT_TIERS[best][0],
                    "cell_mention": mention,
                    "tf_hgnc_ids": tfs,
                    "named_regulator": bool(set(tfs) & named[lineage]),
                    "priority": payload["priority"],
                }
            )
    return options, excluded


def select(options: dict[str, list[dict]]) -> list[dict]:
    """Round-robin over lineages; each pick prefers a TF new to that lineage, stronger context, a named
    regulator, then retrieval priority. Paper, bundle, per-lineage, and per-paper caps are hard."""
    chosen, papers, per_paper, seen_tfs = [], set(), {}, {lineage: set() for lineage in options}
    taken = set()
    while len(chosen) < MAX_BUNDLES:
        progressed = False
        for lineage in sorted(options):
            if len(chosen) >= MAX_BUNDLES or sum(x["lineage"] == lineage for x in chosen) >= MAX_PER_LINEAGE:
                continue
            pool = [
                o
                for o in options[lineage]
                if o["payload_id"] not in taken
                and per_paper.get(o["pmid"], 0) < MAX_PER_PAPER
                and (o["pmid"] in papers or len(papers) < MAX_PAPERS)
            ]
            if not pool:
                continue
            pick = min(
                pool,
                key=lambda o, s=seen_tfs[lineage]: (
                    not (set(o["tf_hgnc_ids"]) - s),
                    o["tier"],
                    o["cell_mention"] != "strict",
                    not o["named_regulator"],
                    -o["priority"],
                    o["payload_id"],
                ),
            )
            chosen.append(pick)
            taken.add(pick["payload_id"])
            papers.add(pick["pmid"])
            per_paper[pick["pmid"]] = per_paper.get(pick["pmid"], 0) + 1
            seen_tfs[lineage] |= set(pick["tf_hgnc_ids"])
            progressed = True
        if not progressed:
            break
    return chosen


def coverage(options: dict[str, list[dict]], chosen: list[dict], named: dict[str, set[str]]) -> dict:
    report = {}
    for lineage, pool in sorted(options.items()):
        picks = [x for x in chosen if x["lineage"] == lineage]
        by_tier = {name: sum(o["tier"] == i for o in pool) for i, (name, _) in enumerate(CONTEXT_TIERS)}
        gaps = []
        if not pool:
            gaps.append("no_eligible_bundle")
        else:
            if not by_tier["passage_direct"]:
                gaps.append("no_passage_direct_context_bundle_in_pool")
            if not any(o["cell_mention"] == "strict" for o in pool):
                gaps.append("anchor_names_only_the_broad_cell_class_not_the_manuscript_population")
        covered = {tf for x in picks for tf in x["tf_hgnc_ids"]}
        pool_tfs = {tf for o in pool for tf in o["tf_hgnc_ids"]}
        report[lineage] = {
            "eligible_bundles": len(pool),
            "eligible_by_context_tier": by_tier,
            "eligible_tfs": sorted(pool_tfs),
            "selected_bundles": len(picks),
            "selected_tfs": sorted(covered),
            "named_regulators_without_eligible_bundle": sorted(named[lineage] - pool_tfs),
            "gaps": gaps,
        }
    return report


def run_pilot_proposal(loaded: LoadedProjectConfig, manuscript_key: str, literature: Path, corpus_key: str) -> dict:
    ctx = c.corpus_context(loaded, manuscript_key, literature)
    artifact = loaded.data_root / "processed" / corpus_key
    ready_path = artifact / "source_bundles_ready.jsonl"
    payloads = [json.loads(line) for line in ready_path.read_text(encoding="utf-8").splitlines() if line]
    named = {x["cell_type"]: set(x["named_tfs"]) for x in c.lineage_terms(ctx)}
    ontology = build_context(loaded.repo_root / "configs" / "ontology_scope.yaml", loaded.data_root / "external")
    cell_mentions = {p["payload_id"]: anchor_cell_mentions(p, named, ontology) for p in payloads}
    options, excluded = candidates(payloads, named, cell_mentions)
    chosen = select(options)
    by_id = {p["payload_id"]: p for p in payloads}
    titles = _titles(artifact)
    manifest = r.batch_manifest(
        {"batch_index": 0, "payload_ids": [x["payload_id"] for x in chosen]},
        by_id,
        {"manuscript_key": manuscript_key, "corpus_key": corpus_key},
    )
    body = {k: v for k, v in manifest.items() if k != "manifest_sha256"}
    body["status"] = "proposed_pilot_pending_lead_review"
    manifest = {**body, "manifest_sha256": sha256_text(canonical_json(body))}
    pool_reasons: dict[str, int] = {}
    for payload in payloads:
        for reason in eligibility(payload) or ["eligible"]:
            pool_reasons[reason] = pool_reasons.get(reason, 0) + 1
    proposal = {
        "rule": PILOT_RULE,
        "status": "proposed_pending_lead_review",
        "created_at": utc_now(),
        "corpus_key": corpus_key,
        "inputs_sha256": {
            "source_bundles_ready.jsonl": sha256_file(ready_path),
            "manifest.json": sha256_file(artifact / "manifest.json"),
        },
        "limits": {
            "papers": MAX_PAPERS,
            "bundles": MAX_BUNDLES,
            "per_lineage": MAX_PER_LINEAGE,
            "per_paper": MAX_PER_PAPER,
        },
        "ready_bundles": len(payloads),
        "pool_screen": pool_reasons,
        "selected": [
            {
                **x,
                "title": titles.get(x["pmid"], ""),
                "tf_identity": by_id[x["payload_id"]]["tf_identity"],
                "anchor_excerpt": _excerpt(by_id[x["payload_id"]]),
            }
            for x in chosen
        ],
        "papers": len({x["pmid"] for x in chosen}),
        "coverage": coverage(options, chosen, named),
        "excluded_associations_by_lineage": excluded,
        # direct-context ready associations the pool rule excluded: for lead review of species/ortholog
        # handling and attribution, not silently dropped
        "direct_context_not_in_pool": direct_context_not_in_pool(payloads, cell_mentions),
        "caveats": [
            "Source-identifier consistency does not establish experimental species, cell context, or a valid "
            "regulatory finding; P4 extraction/verification decides those.",
            "Context tiers are deterministic screening labels. Ontology/manuscript labels such as aberrant "
            "basaloid or activated/CTHRC1+ fibroblasts are hints, not the exact manuscript population.",
            "Bundles outside the pilot remain in the corpus frontier; the pilot is not a sample for recall.",
        ],
    }
    proposal["proposal_sha256"] = sha256_text(canonical_json({k: v for k, v in proposal.items() if k != "created_at"}))
    out = loaded.repo_root / "reports" / "literature" / corpus_key
    out.mkdir(parents=True, exist_ok=True)
    (out / "proposed_pilot.json").write_text(json.dumps(proposal, indent=1, sort_keys=True), encoding="utf-8")
    (out / "proposed_pilot_manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
    (out / "proposed_pilot.md").write_text(_markdown(proposal), encoding="utf-8")
    return {
        "status": "SUCCEEDED",
        "key": proposal["proposal_sha256"][:16],
        "artifact": out,
        "corpus_id": ctx.corpus_id,
        "counts": {
            "bundles": len(chosen),
            "papers": proposal["papers"],
            "pool_screen": pool_reasons,
            "selected_by_lineage": {k: v["selected_bundles"] for k, v in proposal["coverage"].items()},
        },
    }


def anchor_cell_mentions(payload: dict, named: dict, ontology) -> dict[str, str | None]:
    anchor = next(p for p in payload["parts"] if p["passage_id"] == payload["anchor_passage_id"])
    profile = source_context(anchor["text"], ontology)["cell_types"]
    return {
        lineage: "strict" if profile[lineage]["strict"] else ("broad" if profile[lineage]["broad"] else None)
        for lineage in named
    }


def direct_context_not_in_pool(payloads: list[dict], cell_mentions: dict) -> list[dict]:
    rows = []
    for payload in payloads:
        for a in payload["associations"]:
            if "direct_context_candidate" not in (a["relevance"], a["passage_relevance"]):
                continue
            mention = cell_mentions[payload["payload_id"]].get(a["cell_type"])
            reasons = eligibility(payload) or [association_reason(payload, a, mention)]
            if reasons != [None]:
                rows.append(
                    {
                        "payload_id": payload["payload_id"],
                        "pmid": payload["pmid"],
                        "lineage": a["cell_type"],
                        "tf_hgnc_id": a["tf_hgnc_id"],
                        "tf_identity": payload["tf_identity"]["per_tf"][a["tf_hgnc_id"]]["status"],
                        "attributions": payload["attributions"],
                        "reasons": reasons,
                    }
                )
    return sorted(rows, key=lambda x: (x["lineage"], x["pmid"], x["payload_id"], x["tf_hgnc_id"]))


def _titles(artifact: Path) -> dict[str, str]:
    titles = {}
    for name in ("discovery_coverage.parquet", "advisor_coverage.parquet"):  # advisor titles win
        frame = pd.read_parquet(artifact / name, columns=["pmid", "title"])
        titles.update({str(k): v for k, v in zip(frame["pmid"], frame["title"], strict=True) if isinstance(v, str)})
    return titles


def _excerpt(payload: dict, limit: int = 240) -> str:
    anchor = next(p for p in payload["parts"] if p["passage_id"] == payload["anchor_passage_id"])
    text = " ".join(anchor["text"].split())
    return text[:limit] + ("…" if len(text) > limit else "")


def _markdown(proposal: dict) -> str:
    esc = lambda v: html.escape(str(v)).replace("|", "\\|")  # noqa: E731
    lines = [
        f"# Proposed P4 pilot — PROPOSAL ONLY ({esc(proposal['status'])})",
        "",
        f"Corpus `{esc(proposal['corpus_key'])}`, rule `{PILOT_RULE}`, proposal `{proposal['proposal_sha256'][:16]}`.",
        f"{len(proposal['selected'])} bundles from {proposal['papers']} papers "
        f"(limits {proposal['limits']['bundles']} bundles / {proposal['limits']['papers']} papers).",
        "",
        f"Pool screen of {proposal['ready_bundles']} ready bundles: {esc(proposal['pool_screen'])}",
        "",
        "| Lineage | Context tier | Cell named in anchor | TFs | PMID | Title | Bundle | Anchor excerpt |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for x in proposal["selected"]:
        lines.append(
            f"| {esc(x['lineage'])} | {esc(x['context_tier'])} | {esc(x['cell_mention'])} | "
            f"{esc(', '.join(x['tf_hgnc_ids']))} | "
            f"{esc(x['pmid'])} | {esc(x['title'][:90])} | `{esc(x['payload_id'])}` | {esc(x['anchor_excerpt'])} |"
        )
    lines += ["", "## Coverage and gaps", ""]
    for lineage, cov in proposal["coverage"].items():
        lines.append(f"- **{esc(lineage)}**: {esc(cov)}")
    lines += ["", "## Direct-context ready associations outside the pool", ""]
    lines += [
        f"- {esc(x['lineage'])} PMID {esc(x['pmid'])} {esc(x['tf_hgnc_id'])} ({esc(x['tf_identity'])}): "
        f"{esc(', '.join(x['reasons']))}"
        for x in proposal["direct_context_not_in_pool"]
    ] or ["- none"]
    lines += ["", "## Excluded associations by lineage", ""]
    lines += [f"- {esc(k)}: {esc(v)}" for k, v in proposal["excluded_associations_by_lineage"].items()]
    lines += ["", "## Caveats", ""] + [f"- {esc(x)}" for x in proposal["caveats"]]
    return "\n".join(lines) + "\n"
