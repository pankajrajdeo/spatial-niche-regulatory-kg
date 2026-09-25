"""Reconcile completed screening with frozen source bundles; never call a model.

The result is a preparation checkpoint. Missing assets and unresolved interpretation
remain blockers; creating this report cannot authorize or certify full extraction.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path

import pandas as pd
import yaml

from regkg.config import load_literature_config
from regkg.literature.screening import attribution
from regkg.literature.screening_llm import build_sections, has_main_text
from regkg.provenance import canonical_json, sha256_file, sha256_text
from regkg.workflows import corpus_ready as ready
from regkg.workflows.corpus_parse import _load_document

RULE = "p3-screening-reconciliation-2"
# Lead review of source abstracts/citations, not publication-type filtering alone.
BACKGROUND = {
    "37511489": "Review of BHLHE41 in cancer; retain secondary context, not independent experiments.",
    "33872194": "Commentary explicitly attributes EGR2 experiments to Daniel et al.",
    "29786110": "Review of WNT signaling; secondary synthesis, not a new experiment.",
    "31529710": "Commentary on macrophage identity; retain primary-study attribution.",
    "41227363": "HOPX review synthesizes prior work across organs.",
    "40508199": "Review of matricellular mechanisms in IPF.",
    "42613076": "Review of ageing and persistent transitional states.",
    "41939908": "Review of macrophage heterogeneity in fibrosis and cancer.",
    "40066231": "Review of YAP in inflammatory diseases and cancer.",
    "41597218": "Abstract explicitly states review and proposes a synthesis model.",
    "42396453": "Abstract explicitly synthesizes human studies and models across diseases.",
}
# PMID 40464702 is indexed as Review, but its abstract reports its own ATAC/RNA/ChIP,
# CUT&RUN and reporter experiments. Keep it eligible, preserving the metadata conflict.


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.open() if line.strip()]


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows))


def selected_questions(record: dict) -> list[str]:
    return sorted(q for q, v in record["questions"].items() if v["decision"] == "include_for_extraction")


def main_text(document) -> bool:
    sections, _, _ = build_sections([vars(p) for p in document.passages])
    return has_main_text(sections)


def verified_versions(work: Path, audits: dict) -> dict[str, dict]:
    """Resolve published-DOI links and recorded source-backed study-version reviews."""
    by_doi = {a["doi"].lower(): a for a in audits.values() if a.get("doi")}
    aliases = {}
    for path in sorted((work / "p3-final-acquisition").glob("*-biorxiv.json")):
        value = json.loads(path.read_text())
        for record in value.get("response", {}).get("collection", []):
            target = by_doi.get(str(record.get("published", "")).lower())
            if target:
                aliases[value["publication_id"]] = {
                    "canonical_publication_id": target["publication_id"],
                    "pmid": target["pmid"],
                    "published_doi": target["doi"],
                    "preprint_doi": value["doi"],
                    "source": value["source"],
                    "source_sha256": sha256_file(path),
                }
    reviewed = work / "p3-final-acquisition/reviewed-study-aliases.json"
    if reviewed.exists():
        for value in json.loads(reviewed.read_text()):
            target = audits[value["canonical_publication_id"]]
            if target["doi"].lower() != value["published_doi"].lower():
                raise ValueError("Reviewed study alias disagrees with canonical DOI")
            aliases[value["publication_id"]] = value
    return aliases


def candidate_passages(document, cited: set[str], expand: bool) -> list:
    """Newly acquired full texts get every Results passage/caption, without a TF/top-k gate.

    Methods remain available as context. Other passages remain in a separate frontier;
    this is candidate preparation, not an assertion of exhaustive finding extraction.
    """
    return [
        p
        for p in document.passages
        if p.passage_id in cited
        or (
            expand
            and (
                p.kind == "abstract"
                or p.kind == "figure_caption"
                or (p.section_type == "results" and p.kind in {"paragraph", "table_row", "table_caption"})
            )
        )
    ]


def verify_parts(bundle: dict, document) -> None:
    passages = {p.passage_id: p for p in document.passages}
    for part in bundle["parts"]:
        p = passages[part["passage_id"]]
        if p.text != part["text"] or p.asset_sha256 != part["asset_sha256"] or p.locator != part["locator"]:
            raise ValueError(f"Source mismatch: {p.passage_id}")
        if document.canonical_text[p.start : p.end] != p.text:
            raise ValueError(f"Offset mismatch: {p.passage_id}")


def source_bundle(document, report: dict, anchor, record: dict, citations: list[dict], retracted=False) -> dict:
    b = ready.build_bundle(anchor, document, report["document_id"], {}, set())
    b.update(
        publication_id=record["publication_id"],
        pmid=record["pmid"],
        document_role="article",
        text_version=document.text_version,
        source_asset_sha256=document.source_asset_sha256,
        canonical_sha256=document.canonical_sha256,
        document_parse=report,
        tf_hgnc_ids=[],
        tf_identity=None,
        priority=1.0,
        item_ids=[],
        associations=[],
        lineages=selected_questions(record),
        relevance={},
        passage_relevance={},
        attributions=[attribution(anchor.kind, anchor.section_type, anchor.text)],
        selection_provenance={
            "rule": RULE,
            "citation_ids": sorted({c["passage_id"] for c in citations}),
            "entity_resolution": "P4_required; screening names are not gene mappings",
        },
    )
    b["relevance"] = {q: ["screening_selected_candidate"] for q in b["lineages"]}
    b["readiness_state"], b["readiness_reasons"] = ready.readiness(
        b, set(b["attributions"]), False, retracted, report, []
    )
    # Front-matter-only JATS is not full text, even though its parser reports PARSED.
    if not main_text(document):
        b["readiness_state"] = "NEEDS_ASSET"
        b["readiness_reasons"].append("main_text_missing_no_abstract_only_disposition")
    # A reference without a checked local dependency is not eligible for assembly yet.
    if b["supplement_references"]:
        b["readiness_state"] = "NEEDS_ASSET"
        b["readiness_reasons"].append("selected_reference_requires_supplement_inventory_reconciliation")
    verify_parts(b, document)
    return b


def audits_from_work(work: Path) -> dict[str, dict]:
    result = {}
    for directory in (
        "discovery_acquisition",
        "supplemental_acquisition",
        "gap_acquisition",
        "advisor_audit",
        "p3-final-acquisition",
    ):
        for path in sorted((work / directory).glob("batch-*.json")):
            value = json.loads(path.read_text())
            rows = value if isinstance(value, list) else value["results"]
            result.update({r["publication_id"]: r for r in rows if "publication_id" in r})
    return result


def supplement_dependencies(work, inventory, audits, documents, reports, bundles, config):
    from regkg.workflows.corpus_prepare import _dependencies, _merge_needed

    by_pmid = {a["pmid"]: a for a in audits.values()}
    for directory in (
        work / "needed_supplements",
        work / "p3-final-supplements/needed_supplements",
        work / "p3-final-supplements/additional/needed_supplements",
        work / "p3-final-supplements/size-repair/needed_supplements",
    ):
        for path in sorted(directory.glob("batch-*.json")):
            _merge_needed(by_pmid, {"records": [json.loads(path.read_text())]})
    parsed = {"articles": {}, "supplements": []}
    for pid, document in documents.items():
        if pid in audits:
            parsed["articles"][audits[pid]["pmid"]] = (document, reports[pid], [])
    for row in inventory[inventory.component != "article"].to_dict("records"):
        parsed["supplements"].append({"pmid": str(row["pmid"]), "supplement": row["supplement"], "report": row})
    for path in sorted((work / "p3-final-supplements").glob("*-parsed.json")):
        value = json.loads(path.read_text())
        for report in value["reports"]:
            parsed["supplements"].append({"pmid": value["pmid"], "supplement": value["supplement"], "report": report})
    scoped = [b for b in bundles if b.get("selection_provenance") and b["pmid"] in by_pmid]
    dependencies, needs = _dependencies(scoped, by_pmid, parsed, config.supplement_extensions)
    by_payload = {}
    for dep in dependencies:
        by_payload.setdefault(dep["payload_id"], []).append(dep)
    for b in scoped:
        deps = by_payload.get(b["payload_id"], [])
        if not deps or not main_text(documents[b["publication_id"]]):
            continue
        b["readiness_state"], b["readiness_reasons"] = ready.readiness(
            b,
            set(b["attributions"]),
            False,
            audits[b["publication_id"]].get("retracted", False),
            b["document_parse"],
            [d["state"] for d in deps],
        )
        if any(d["state"] == "to_acquire" for d in deps):
            b["readiness_state"] = "NEEDS_ASSET"
            b["readiness_reasons"].append("required_supplement_pending_acquisition")
    return dependencies, needs


def reconcile(root: Path, corpus_key: str, screening_label: str) -> Path:
    artifact = root / "data/processed" / corpus_key
    work = root / "data/work/corpus-c700d6e584b7bccf"
    records_path = root / "reports/literature" / corpus_key / f"screening_records_{screening_label}.jsonl"
    records = read_jsonl(records_path)
    if len({r["publication_id"] for r in records}) != len(records):
        raise ValueError("Duplicate screening publication IDs")
    if any(r["state"] != "screened" or r["windows_unread"] for r in records):
        raise ValueError("Screening execution has unresolved failures")
    selected = [r for r in records if selected_questions(r)]
    inventory = pd.read_parquet(artifact / "parse_inventory.parquet")
    inventory["pmid"] = inventory["pmid"].astype(str)
    audit = audits_from_work(work)
    aliases = verified_versions(work, audit)
    discovered = pd.read_parquet(artifact / "discovery_coverage.parquet").drop_duplicates("publication_id")
    metadata = {r["publication_id"]: r for r in discovered.to_dict("records")}
    source_reports = {}
    for r in selected:
        rows = inventory[(inventory["pmid"] == r["pmid"]) & (inventory.component == "article")]
        canonical = rows[rows.version_role == "canonical"]
        if len(canonical):
            item = canonical.iloc[0].to_dict()
            item["reasons"] = json.loads(item["reasons"]) if isinstance(item["reasons"], str) else []
            source_reports[r["publication_id"]] = item
        extra = work / "p3-final-acquisition" / f"parsed-{r['pmid']}.json"
        if extra.exists():
            source_reports[r["publication_id"]] = json.loads(extra.read_text())["report"]
    for path in sorted((work / "p3-final-acquisition").glob("*-source.json")):
        value = json.loads(path.read_text())
        if value.get("report"):
            source_reports[value["publication_id"]] = value["report"]
    source_docs = {}
    for pid, report in source_reports.items():
        if report and report.get("cache_key"):
            path = work / "parsed" / report["cache_key"] / "document.json"
            if path.exists():
                source_docs[pid] = _load_document(json.loads(path.read_text()))
    selection_ids = {
        r["publication_id"] for r in selected if r["pmid"] not in BACKGROUND and r["publication_id"] not in aliases
    }
    payloads = {
        b["payload_id"]: b for b in read_jsonl(artifact / "bundles_all.jsonl") if b["publication_id"] in selection_ids
    }
    newly_built, citation_checks, frontier, papers, downloads = [], [], [], [], []
    for record in selected:
        pid, pmid = record["publication_id"], record["pmid"]
        doc, report = source_docs.get(pid), source_reports.get(pid)
        a = audit.get(pid, {})
        is_full = bool(doc and main_text(doc))
        background = pmid in BACKGROUND or pid in aliases
        citations = [
            c for q in record["questions"].values() if q["decision"] == "include_for_extraction" for c in q["citations"]
        ]
        cited = {c["passage_id"] for c in citations}
        if doc and not background:
            current = {p.passage_id: p for p in doc.passages}
            for citation in citations:
                exact = current.get(citation["passage_id"])
                matches = [p.passage_id for p in doc.passages if citation["exact_span"] in p.text]
                state = (
                    "EXACT_SOURCE"
                    if exact and citation["exact_span"] in exact.text
                    else ("EXACT_QUOTE_NEW_VERSION_UNIQUE" if len(matches) == 1 else "SCREENED_VERSION_ONLY")
                )
                citation_checks.append(
                    {
                        "publication_id": pid,
                        "original_passage_id": citation["passage_id"],
                        "state": state,
                        "matching_passage_ids": matches,
                        "exact_span": citation["exact_span"],
                    }
                )
                if state != "SCREENED_VERSION_ONLY":
                    cited.update(matches)
            # Also restore selected passages missed by the former exact-TF filter.
            has_ready = any(
                b["publication_id"] == pid and b["readiness_state"].startswith("READY") for b in payloads.values()
            )
            anchors = candidate_passages(doc, cited, record["pool"] == "discovered_metadata_only" or not has_ready)
            existing_anchors = {b["anchor_passage_id"] for b in payloads.values() if b["publication_id"] == pid}
            for anchor in anchors:
                if anchor.passage_id in existing_anchors:
                    continue
                b = source_bundle(doc, report, anchor, record, citations, a.get("retracted", False))
                payloads[b["payload_id"]] = b
                newly_built.append(b["payload_id"])
            for p in doc.passages:
                frontier.append(
                    {
                        "publication_id": pid,
                        "passage_id": p.passage_id,
                        "kind": p.kind,
                        "section_type": p.section_type,
                        "disposition": "candidate_or_context"
                        if p.passage_id in cited or p in anchors or p.passage_id in existing_anchors
                        else "retained_source_not_selected_as_anchor",
                        "reason": "references/titles/methods/other prose retained; no claim of biological irrelevance",
                    }
                )
        # Preserve earlier readiness; do not let a PARSED front-matter record bypass source checks.
        for b in payloads.values():
            if b["publication_id"] == pid and not is_full and b["readiness_state"].startswith("READY"):
                b["readiness_state"] = "NEEDS_ASSET"
                b["readiness_reasons"] = [*b["readiness_reasons"], "main_text_missing_no_abstract_only_disposition"]
        own = [b for b in payloads.values() if b["publication_id"] == pid]
        ready_ids = [b["payload_id"] for b in own if b["readiness_state"].startswith("READY")]
        info = metadata.get(pid, {})
        doi = a.get("doi") or info.get("doi")
        pmcid = a.get("pmcid") or info.get("pmcid")
        state = (
            "NO_ELIGIBLE_BUNDLE_REVIEWED"
            if background
            else ("NEEDS_ASSET" if not is_full else "READY_FULL_TEXT" if ready_ids else "NEEDS_CONTEXT")
        )
        papers.append(
            {
                "publication_id": pid,
                "pmid": pmid,
                "doi": doi,
                "pmcid": pmcid,
                "title": record["title"],
                "screening_pool": record["pool"],
                "selected_for_extraction": not background,
                "questions": selected_questions(record),
                "source_full_text_available": is_full,
                "readiness_state": state,
                "role_review": (
                    "Verified preprint of selected journal article; preserve version, do not count twice."
                    if pid in aliases
                    else BACKGROUND.get(pmid, "Candidate findings; P4 must verify type, attribution and context.")
                ),
                "version_alias": aliases.get(pid),
                "ready_bundle_count": len(ready_ids),
                "bundle_count": len(own),
                "ready_bundle_ids": ready_ids,
                "extraction_status": "NOT_RUN",
                "publication_types": a.get("publication_types", []),
                "source_document_id": report.get("document_id") if report else None,
            }
        )
        if not is_full and not background:
            link = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            task_id = pmid or pid.replace(":", "-")
            downloads.append(
                {
                    "publication_id": pid,
                    "pmid": pmid,
                    "doi": doi,
                    "title": record["title"],
                    "priority": "named_manuscript_gap"
                    if pmid in {"41386231", "42555354", "42327275"}
                    else "selected_evidence",
                    "item": "article full text",
                    "landing_url": link,
                    "expected_path": f"data/papers/manual_inbox/{task_id}/article.pdf",
                    "status": "NEEDED",
                    "why": "Selected evidence; no usable canonical main text locally.",
                    "automatic_route_status": a.get("full_text_status", "DOI_ONLY_IDENTITY_AND_ACCESS_REVIEW"),
                    "checked_sources": a.get("checked_sources", []),
                    "checked_at": a.get("checked_at"),
                    "questions": selected_questions(record),
                }
            )
    bundles = sorted(payloads.values(), key=lambda b: b["payload_id"])
    cfg = load_literature_config(root / "configs/literature.yaml").corpus
    dependencies, needs = supplement_dependencies(work, inventory, audit, source_docs, source_reports, bundles, cfg)
    for paper in papers:
        own = [b for b in bundles if b["publication_id"] == paper["publication_id"]]
        paper["ready_bundle_ids"] = [b["payload_id"] for b in own if b["readiness_state"].startswith("READY")]
        paper["ready_bundle_count"] = len(paper["ready_bundle_ids"])
    original_queue = [
        q for q in read_jsonl(artifact / "context_investigations.jsonl") if q["publication_id"] in selection_ids
    ]
    extra_queue = ready.investigations([b for b in bundles if b["payload_id"] in set(newly_built)], dependencies)
    queue = {q["investigation_id"]: q for q in original_queue + extra_queue}
    questions = sorted({q for r in selected for q in selected_questions(r)})
    batches = ready.ready_batches(bundles, questions, cfg.ready_batch)
    budget = ready.budget(bundles, batches, list(queue.values()), cfg.budget, questions)
    budget["provider"] = "litellm:prescient.glm-5.3-flash"
    budget["proxy_usd"] = None
    ready_bundles = [b for b in bundles if b["readiness_state"].startswith("READY")]
    evidence_tokens = sum(math.ceil(b["serialized_chars"] / cfg.budget.chars_per_token) for b in ready_bundles)
    n = len(ready_bundles)
    budget["typical_ready_calls_separately"] = {
        "extractor_calls": n,
        "verifier_calls_up_to": n,
        "extractor_input_estimate": evidence_tokens + n * cfg.budget.extractor_overhead_tokens,
        "verifier_input_estimate": evidence_tokens
        + n * (cfg.budget.verifier_overhead_tokens + cfg.budget.extractor_output_tokens_typical),
        "note": "Verifier includes source again plus extraction output; final prompts and tokenizer remain P4 checks.",
    }
    budget["notes"].append(
        "Old OpenRouter rate scenarios are illustrative only, not the selected proxy price. "
        "P4 must calibrate GLM reasoning/output caps."
    )
    source_inputs = {
        "corpus_manifest": sha256_file(artifact / "manifest.json"),
        "screening_records": sha256_file(records_path),
        "rule": RULE,
        "source_documents": {pid: d.canonical_sha256 for pid, d in source_docs.items()},
        "background_dispositions": BACKGROUND,
        "corpus_configuration": cfg.model_dump(),
        "verified_version_aliases": aliases,
        "implementation_sha256": sha256_file(Path(__file__)),
        "supplement_preparation": {
            str(p.relative_to(work)): sha256_file(p) for p in sorted((work / "p3-final-supplements").rglob("*.json"))
        },
    }
    key = "p3selection-" + sha256_text(canonical_json(source_inputs))[:16]
    out = root / "data/processed" / key
    if out.exists():
        manifest = json.loads((out / "manifest.json").read_text())
        if any(sha256_file(out / name) != checksum for name, checksum in manifest["outputs"].items()):
            raise ValueError("Existing selection failed manifest verification")
        print(json.dumps({"status": "REUSED_VERIFIED", "selection_key": key}))
        return out
    out.mkdir()
    by_id = {b["payload_id"]: b for b in bundles}
    # Check every scheduled part against its canonical document, including reused bundles.
    by_document = {source_reports[pid]["document_id"]: doc for pid, doc in source_docs.items()}
    for b in bundles:
        if not b["readiness_state"].startswith("READY"):
            continue
        for part in b["parts"]:
            doc_id = part["document_id"]
            if doc_id not in by_document:
                rows = inventory[inventory.document_id == doc_id]
                if not len(rows):
                    raise ValueError(f"Missing scheduled source document: {doc_id}")
                path = work / "parsed" / rows.iloc[0]["cache_key"] / "document.json"
                by_document[doc_id] = _load_document(json.loads(path.read_text()))
            verify_parts({"parts": [part]}, by_document[doc_id])
        if len(b["parts"]) > 3 or len(ready.serialize_evidence(b["parts"])) > 6000:
            raise ValueError("Scheduled evidence exceeds source bundle bounds")
    for batch in batches:
        write_json(
            out / "ready_batches" / f"batch-{batch['batch_index']:03}.json",
            ready.batch_manifest(batch, by_id, source_inputs),
        )
    write_jsonl(out / "bundles_all.jsonl", bundles)
    write_jsonl(out / "source_bundles_ready.jsonl", [b for b in bundles if b["readiness_state"].startswith("READY")])
    write_jsonl(out / "context_investigations.jsonl", list(queue.values()))
    write_jsonl(out / "citation_reconciliation.jsonl", citation_checks)
    write_jsonl(out / "supplement_dependencies.jsonl", dependencies)
    write_json(out / "supplement_acquisition_remaining.json", needs)
    write_jsonl(out / "source_frontier.jsonl", frontier)
    write_json(out / "paper_selection.json", papers)
    pd.DataFrame(papers).to_csv(out / "paper_selection.csv", index=False)
    pd.DataFrame(downloads).to_csv(out / "manual_downloads.csv", index=False)
    write_json(out / "inference_budget.json", budget)
    advisor = pd.read_parquet(artifact / "advisor_coverage.parquet")
    by_pmid = {r["pmid"]: r for r in records if r["pmid"]}
    if any(str(p) not in by_pmid for p in advisor.pmid):
        raise ValueError("Missing advisor screening record")
    advisor["llm_screening_state"] = advisor.pmid.astype(str).map(lambda p: by_pmid[p]["state"])
    advisor["llm_selected"] = advisor.pmid.astype(str).map(lambda p: bool(selected_questions(by_pmid[p])))
    advisor["final_selected"] = advisor.pmid.astype(str).map(
        lambda p: bool(selected_questions(by_pmid[p])) and p not in BACKGROUND
    )
    advisor.to_csv(out / "advisor_coverage.csv", index=False)
    # Keep nonselected uncertainty and old obligations visible; nonselection is not irrelevant full text.
    write_jsonl(
        out / "nonselected_dispositions.jsonl",
        [
            dict(
                publication_id=r["publication_id"],
                pmid=r["pmid"],
                source_record_line=index + 1,
                questions={q: v["decision"] for q, v in r["questions"].items()},
                lead_disposition=(
                    "No positive inclusion in performed screening; preserve background/uncertainty; "
                    "no whole-paper irrelevance claim."
                ),
            )
            for index, r in enumerate(records)
            if not selected_questions(r)
        ],
    )
    scope = yaml.safe_load((root / "configs/manuscript_scope.yaml").read_text())
    coverage = []
    for lineage in scope["lineages"]:
        question = lineage["cell_type"]
        own = [r for r in selected if r["publication_id"] in selection_ids and question in selected_questions(r)]
        for tf in lineage["tf_seeds"]:
            named = {
                r["publication_id"]
                for r in own
                if any(
                    tf.upper() == str(g).upper()
                    for c in r["questions"][question]["citations"]
                    for g in c.get("genes_or_tfs_reported", [])
                )
            }
            coverage.append(
                {
                    "lineage": question,
                    "regulator": tf,
                    "primary_conditions": lineage["primary_conditions"],
                    "selected_papers": len(own),
                    "papers_reporting_exact_regulator_name": len(named),
                    "ready_papers_reporting_name": sum(
                        p["publication_id"] in named and p["ready_bundle_count"] > 0 for p in papers
                    ),
                    "note": "Screening-name coverage only; no TF family resolution or experimental support inferred.",
                }
            )
    pd.DataFrame(coverage).to_csv(out / "lineage_regulator_coverage.csv", index=False)
    summary = {
        "status": "PREPARATION_CHECKPOINT_NOT_FULL_CORPUS_ACCEPTANCE",
        "selection_key": key,
        "screened_records": len(records),
        "screening_inclusions": len(selected),
        "background_only_reviewed": sum(r["pmid"] in BACKGROUND for r in selected),
        "verified_preprint_aliases": len(aliases),
        "extraction_selected_records": len(selection_ids),
        "selected_full_text_papers": sum(
            p["selected_for_extraction"] and p["source_full_text_available"] for p in papers
        ),
        "papers_with_ready_bundles": sum(p["ready_bundle_count"] > 0 for p in papers),
        "ready_bundles": sum(b["readiness_state"].startswith("READY") for b in bundles),
        "all_candidate_bundles": len(bundles),
        "new_bundles": len(newly_built),
        "bundle_states": dict(Counter(b["readiness_state"] for b in bundles)),
        "ready_batches": len(batches),
        "context_investigations": len(queue),
        "manual_article_requests": len(downloads),
        "advisor_papers_accounted": len(advisor),
        "extraction_calls_completed": 0,
        "open_obligations": [
            "Selected missing full texts need intake or explicit disposition.",
            "Source-specific table meaning and supplement dependency review remain separate blockers.",
            "Unresolved DOI-only versions need verified linkage; "
            "do not count possible preprint/journal pairs as independent studies.",
            "P4 final prompts/token estimates and implementation validation not performed.",
        ],
        "source_inputs": source_inputs,
    }
    write_json(out / "extraction_readiness.json", summary)
    write_json(
        out / "manifest.json",
        {
            "rule": RULE,
            "inputs": source_inputs,
            "outputs": {str(p.relative_to(out)): sha256_file(p) for p in sorted(out.rglob("*")) if p.is_file()},
        },
    )
    report = root / "reports/literature" / key
    report.mkdir(parents=True, exist_ok=True)
    lines = [
        "# P3 extraction selection and source requests",
        "",
        f"Selected {len(selection_ids)} publication records for extraction; "
        f"{summary['background_only_reviewed']} background/commentary and {len(aliases)} verified version aliases.",
        f"{summary['papers_with_ready_bundles']} papers have {summary['ready_bundles']} ready bundles; "
        f"{len(downloads)} selected records lack full text.",
        "",
        "This is not complete P3 acceptance: listed source/interpretation blockers remain open.",
        "",
        "## Article requests",
        "",
        "| PMID / DOI | Paper | Source | Save as |",
        "|---|---|---|---|",
    ]
    for d in sorted(downloads, key=lambda x: (x["priority"] != "named_manuscript_gap", x["pmid"])):
        title = d["title"].replace("|", "\\|")
        lines.append(
            f"| {d['pmid'] or d['doi']} | {title} | [Landing page]({d['landing_url']}) | `{d['expected_path']}` |"
        )
    (report / "manual_downloads.md").write_text("\n".join(lines) + "\n")
    pd.DataFrame(downloads).to_csv(report / "manual_downloads.csv", index=False)
    write_json(report / "extraction_readiness.json", summary)
    print(json.dumps({k: v for k, v in summary.items() if k != "source_inputs"}, indent=2))
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--screening-label", default="litellm_repaired")
    args = parser.parse_args()
    reconcile(Path.cwd(), args.corpus, args.screening_label)


if __name__ == "__main__":
    main()
