"""`regkg literature corpus-prepare`: parse, screen, retrieve, and report readiness for the corpus.

Requires completed advisor-audit, discovery, and discovery-acquisition batches (it never launches
new searches). Three coverage numbers stay separate: papers accounted for, full texts processed,
and papers/bundles extracted (always zero here: P4 has not run). Ready batches are preparation
artifacts; the corpus is not frozen while user downloads or review dispositions remain open.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import pandas as pd

from regkg.config import LoadedProjectConfig, load_model_settings
from regkg.literature import embeddings as emb
from regkg.literature import files
from regkg.literature.intake import run_intake
from regkg.literature.ontology import build_context, query_synonym_gaps
from regkg.literature.passages import candidate_name_mentions, pubtator_mentions, reconcile
from regkg.literature.screening import context_relevance, provisional_roles, regulatory_content, source_context
from regkg.provenance import canonical_json, sha256_text, stable_id, utc_now
from regkg.workflows import corpus as c
from regkg.workflows import corpus_ready as r
from regkg.workflows.corpus_parse import parse_all
from regkg.workflows.literature import _human_gene_map

MENTION_KEEP = [
    "mention_id",
    "start",
    "end",
    "text",
    "source",
    "candidate_hgnc_id",
    "hgnc_id",
    "resolution",
    "species_taxon",
    "species_evidence",
    "external_identifier",
    "identity_status",
    "alignment",
]
PROSE_ROUTES = {"docling_pdf", "docling_docx", "text"}


def _complete(result: dict, what: str) -> None:
    if result["pending_batches"]:
        raise c.CorpusError(f"{what}: {result['pending_batches']} batches pending; run that step first")


def run_intake_step(loaded: LoadedProjectConfig, manuscript_key: str, literature: Path) -> dict:
    """Process `data/papers/manual_inbox/intake.csv` and record dispositions/assets for later reports."""
    ctx = c.corpus_context(loaded, manuscript_key, literature)
    audits = _all_audits(ctx)
    publications = {
        pmid: {"publication_id": a["publication_id"], "doi": a.get("doi"), "title": a.get("title")}
        for pmid, a in audits.items()
    }
    known = {x["sha256"] for a in audits.values() for x in a["assets"]}
    inbox = loaded.data_root / "papers" / "manual_inbox"
    result = run_intake(inbox, ctx.papers_root, loaded.repo_root, publications, known)
    dispositions, requests, assets = {}, {}, []
    for record in result["records"]:
        if record["state"] == "DISPOSITION_RECORDED":
            reason = record["reasons"][-1].removeprefix("user disposition: ")
            dispositions[record["pmid"]] = {"disposition": reason, "note": record["note"]}
        if record["asset"]:
            identity = "confirmed" if record["state"] in {"INGESTED", "DUPLICATE"} else "review_required"
            assets.append({**record["asset"], "identity": identity, "identity_evidence": record["identity_evidence"]})
        state = {
            "INGESTED": "INGESTED",
            "DUPLICATE": "INGESTED",
            "IDENTITY_REVIEW_REQUIRED": "IDENTITY_REVIEW_REQUIRED",
            "REJECTED": "RECEIVED",
        }.get(record["state"])
        if state:
            requests[record["request_id"]] = {
                "state": state,
                "sha256": record["sha256"],
                "note": "; ".join(record["reasons"]),
            }
    c._atomic_json(
        ctx.work_dir / "intake" / "state.json",
        {
            "dispositions": dispositions,
            "requests": requests,
            "assets": assets,
            "at": utc_now(),
            "records": result["records"],
            "unlisted": result["unlisted"],
        },
    )
    counts = {
        "manifest": result["manifest"],
        "records": Counter(x["state"] for x in result["records"]),
        "unlisted_files": len(result["unlisted"]),
        "dispositions": len(dispositions),
        "assets": len(assets),
    }
    return {
        "status": "SUCCEEDED",
        "key": "(intake state)",
        "artifact": ctx.work_dir / "intake",
        "corpus_id": ctx.corpus_id,
        "counts": {k: dict(v) if isinstance(v, Counter) else v for k, v in counts.items()},
    }


def _all_audits(ctx) -> dict[str, dict]:
    advisor = c.run_batches(
        ctx.work_dir / "advisor_audit",
        _advisor_items(ctx),
        ctx.corpus.audit_batch_size,
        _advisor_identity(ctx),
        None,
        limit=0,
    )
    _complete(advisor, "advisor audit")
    _, _, order = c.discovery_state(ctx)
    discovery = c.run_batches(
        ctx.work_dir / "discovery_acquisition",
        [list(x) for x in order],
        ctx.corpus.acquisition_batch_size,
        {"route": "discovery_acquisition"},
        None,
        limit=0,
    )
    _complete(discovery, "discovery acquisition")
    audits = {p["pmid"]: {**p, "route": "discovery"} for b in discovery["records"] for p in b["results"]}
    audits.update({p["pmid"]: {**p, "route": "advisor"} for b in advisor["records"] for p in b["results"]})
    return audits


def _advisor_items(ctx) -> list:
    ordered = ctx.advisors.sort_values("pmid", key=lambda s: s.astype(int))
    return [[row.publication_id, str(row.pmid)] for row in ordered.itertuples()]


def _advisor_identity(ctx) -> dict:
    return {
        "route": "advisor_audit",
        "supplement_max_bytes": ctx.corpus.supplement_max_bytes,
        "supplement_extensions": ctx.corpus.supplement_extensions,
    }


PREVIOUS_REPORT = "litcorpus-1ed92d41df5cb075"  # the corrected pass under review
EXCLUDED_SAMPLE_RULE = "p3-excluded-sample-1"
TABLE_ROUTES = {"xlsx", "delimited"}


def run_corpus_prepare(
    loaded: LoadedProjectConfig, manuscript_key: str, literature: Path, process_env=None, log=print
) -> dict:
    ctx = c.corpus_context(loaded, manuscript_key, literature)
    advisor = c.run_batches(
        ctx.work_dir / "advisor_audit",
        _advisor_items(ctx),
        ctx.corpus.audit_batch_size,
        _advisor_identity(ctx),
        None,
        limit=0,
    )
    _complete(advisor, "advisor audit")
    advisor_audits, advisor_batches = c._audits(advisor)
    log("retrying incomplete searches (bounded)")
    retries = c.retry_incomplete_searches(ctx)
    discovery_result, discovered, order = c.discovery_state(ctx)
    _complete(discovery_result, "discovery")
    acquisition = c.acquire_discovery(ctx, order)  # completed batches reused; only changed batches run
    _complete(acquisition, "discovery acquisition")
    audits = _all_audits(ctx)
    for entry in recovered_full_text(ctx):
        audit = audits.get(entry["pmid"])
        if audit is not None and all(a["sha256"] != entry["asset"]["sha256"] for a in audit["assets"]):
            audit["assets"].append(entry["asset"])
    alternates = c.fetch_pdf_alternates(ctx, list(advisor_audits.values()))
    alternate_assets = [
        {"pmid": x["pmid"], "asset": a} for b in alternates["records"] for x in b["results"] for a in x["assets"]
    ]
    dispositions, request_states, intake_assets = c.intake_status(ctx)
    manual: dict[str, list] = {}
    for asset in intake_assets:
        manual.setdefault(asset["pmid"], []).append(asset)
        if asset["identity"] == "confirmed" and asset["role"] == "manual_article" and asset["pmid"] in audits:
            audits[asset["pmid"]]["assets"].append(asset)
    terms = c.lineage_terms(ctx)
    ontology = build_context(loaded.repo_root / "configs" / "ontology_scope.yaml", loaded.data_root / "external")
    query_gaps = query_synonym_gaps(ontology, terms, _names(ctx.queue))
    synonym_queue = c.synonym_queue(query_gaps)
    synonym_result = c.synonym_search(ctx, synonym_queue)  # reload only; `synonym-discover` executes it
    synonym_frame, synonym_order = c.synonym_publications(ctx, synonym_queue, synonym_result, discovered)
    synonym_acquired = c.synonym_acquisition(ctx, synonym_order)
    for batch in synonym_acquired["records"]:
        for paper in batch["results"]:
            audits.setdefault(paper["pmid"], {**paper, "route": "supplemental_discovery"})
    synonym_followup = c.synonym_report(synonym_queue, synonym_result, synonym_frame, synonym_acquired)
    gap = c.gap_state(ctx, discovered, loaded.repo_root / "configs" / "p3_gap_queries.yaml")
    for batch in gap["acquisition"]["records"]:
        for paper in batch["results"]:
            audits.setdefault(paper["pmid"], {**paper, "route": "gap_discovery"})
    names = _names(ctx.queue)
    tf_names = {h: n for lineage in terms for h, n in lineage["candidate_tfs"].items()}
    genes = set(names)
    settings = load_model_settings(loaded.repo_root, process_env)
    backend = (
        emb.build_embeddings(settings, ctx.literature.embeddings)
        if settings.embeddings.status.value != "disabled"
        else None
    )
    queries = r.query_terms(ctx.queue)
    selector = _row_selector(tf_names, ontology)
    size_allowances = {(x.pmid, x.filename): x.max_bytes for x in ctx.corpus.supplement_size_exceptions}
    archive_allowances = {(x.pmid, x.filename): x.max_expanded_bytes for x in ctx.corpus.supplement_size_exceptions}
    # Round 1 finds the supplements that candidate evidence needs; round 2 registers, parses, and screens
    # the acquired ones like every other asset. Needs found only in round 2 stay recorded as pending.
    needed_result = {"records": [], "pending_batches": 0, "executed": 0}
    for round_index in (1, 2):
        log(f"round {round_index}: parsing (cached per asset)")
        parsed = parse_all(
            ctx.work_dir,
            loaded.repo_root,
            ctx.papers_root,
            audits,
            manual,
            alternate_assets,
            ctx.corpus.pdf,
            ctx.corpus.spreadsheet,
            log=lambda m: None,
            selector=selector,
            archive_allowances=archive_allowances,
        )
        documents, meta, parse_rows, parse_of = _documents(parsed, audits)
        relevance, profiles = _relevance(audits, parsed, terms, ontology)
        mentions_by_passage, mention_counts = _mentions(documents, meta, audits, names, ctx, loaded)
        items = r.screen(documents, meta, terms, relevance, r.gene_matcher(tf_names), ontology)
        priority, embedding_record = {}, {}
        if round_index == 2:
            pool = {d: doc for d, doc in documents.items() if meta[d]["route"] not in TABLE_ROUTES}
            priority, embedding_record = r.prioritize(
                pool,
                queries,
                [i for i in items if i["document_id"] in pool],
                backend,
                loaded.data_root / "external" / "embeddings",
                ctx.literature.embeddings,
                ctx.literature.retrieval.rrf_k,
                ctx.literature.retrieval.bm25_k1,
                ctx.literature.retrieval.bm25_b,
                log=log,
            )
        payloads = _bundles(items, documents, meta, mentions_by_passage, genes, priority, ctx.queue, parse_of)
        dependencies, needed = _dependencies(
            payloads, audits, parsed, ctx.corpus.supplement_extensions, size_allowances
        )
        if round_index == 2:
            break
        needed = needed + _exception_needs(audits, ctx.corpus.supplement_size_exceptions, needed)
        log(f"needed supplements: {len(needed)} files")
        needed_result = c.acquire_needed_supplements(ctx, needed)
        _merge_needed(audits, needed_result)
    pending_needed = needed  # needs first seen in round 2 (acquired on the next run)
    local_sources = _local_sources(parsed)
    retracted = {pmid for pmid, a in audits.items() if a.get("retracted")}
    abstract_ok = {pmid for pmid, d in dispositions.items() if d.get("disposition") == "abstract_only"}
    deps_of: dict[str, list[str]] = {}
    for dep in dependencies:
        deps_of.setdefault(dep["payload_id"], []).append(dep["state"])
    for payload in payloads:
        state, reasons = r.readiness(
            payload,
            set(payload["attributions"]),
            payload["pmid"] in abstract_ok,
            payload["pmid"] in retracted,
            payload["document_parse"],
            deps_of.get(payload["payload_id"], []),
        )
        payload["readiness_state"], payload["readiness_reasons"] = state, reasons
    queue = r.investigations(payloads, dependencies, local_sources)
    lineages = sorted(x.cell_type for x in ctx.scope.lineages)
    batches = r.ready_batches(payloads, lineages, ctx.corpus.ready_batch)
    by_id = {p["payload_id"]: p for p in payloads}
    for batch in batches:
        for payload_id in batch["payload_ids"]:
            by_id[payload_id]["ready_batch"] = batch["batch_index"]
    ledger_items = _item_status(items, by_id)
    inputs = {"manuscript_key": manuscript_key, "corpus_id": ctx.corpus_id}
    manifests = {
        f"ready_batches/batch-{b['batch_index']:03d}.json": r.batch_manifest(b, by_id, inputs) for b in batches
    }
    budget = r.budget(payloads, batches, queue, ctx.corpus.budget, lineages)

    log("paper-level coverage")
    papers = _paper_coverage(audits, parsed, ledger_items, payloads, dispositions, relevance, profiles)
    screening = {
        p: {"disposition": v["screening_disposition"], "reason": v["screening_reason"]} for p, v in papers.items()
    }
    paper_ready = {
        p: {"state": v["readiness_state"], "reasons": v["readiness_reasons"], "bundle_ids": v["ready_bundle_ids"]}
        for p, v in papers.items()
    }
    document_info = {p: v["document_info"] for p, v in papers.items()}
    ledger = c.advisor_ledger(
        ctx,
        advisor_audits,
        advisor_batches,
        dispositions,
        {p: document_info[p] for p in advisor_audits},
        screening,
        paper_ready,
    )
    discovery_ledger = _discovery_ledger(discovered, order, audits, papers)
    if len(synonym_frame):
        new = synonym_frame[synonym_frame["overlap"] == "new"]
        supplemental = _discovery_ledger(new, synonym_order, audits, papers, "supplemental_synonym")
        discovery_ledger = pd.concat([discovery_ledger, supplemental], ignore_index=True)
    if len(gap["frame"]):
        fresh = gap["frame"][gap["frame"]["overlap"] == "new"]
        fresh = fresh[~fresh["publication_id"].isin(set(discovery_ledger["publication_id"]))]
        if len(fresh):  # a paper found by both queues is listed once
            discovery_ledger = pd.concat(
                [discovery_ledger, _discovery_ledger(fresh, gap["order"], audits, papers, "gap_directed")],
                ignore_index=True,
            )
    downloads, navigation_tasks = _downloads(ctx, audits, papers, dependencies, discovery_ledger, request_states)
    assets = _asset_registry(audits, intake_assets, parse_rows)
    registry = _registry_check(needed_result, assets, parse_rows, ledger_items)
    parse_failures = [
        {
            "pmid": row["pmid"],
            "publication_id": audits[row["pmid"]]["publication_id"],
            "stage": f"parse:{row['component']}",
            "detail": f"{row.get('name')}: {row.get('reasons')}",
            "recovered_by": None,
            "manual_fallback": "source inspection or an alternative copy",
        }
        for row in parse_rows
        if row["state"] == "PARSE_FAILED"
    ]
    failures = c.acquisition_failures(audits, parse_failures)
    sample = _excluded_sample(ctx, discovered, discovery_result, terms, ontology)
    coverage = _lineage_coverage(ctx, payloads, ledger_items, discovery_ledger, queue)
    comparison = _before_after(loaded, payloads, ledger_items, papers, ledger, downloads, assets)
    readiness = _readiness_json(
        ctx,
        ledger,
        discovery_ledger,
        payloads,
        batches,
        downloads,
        parse_rows,
        coverage,
        embedding_record,
        mention_counts,
        discovery_result,
        ledger_items,
        queue,
        papers,
        dependencies,
        comparison,
        retries,
        sample,
    )
    readiness["summary"].update(
        needed_supplement_registry={k: v for k, v in registry.items() if k != "files"},
        needed_supplements_pending_next_round=len(pending_needed),
        source_navigation_tasks=len(navigation_tasks),
        download_rows_by_group=downloads["group"].value_counts().to_dict() if len(downloads) else {},
        missing_article_pdfs=int(downloads["group"].str.startswith("article").sum()) if len(downloads) else 0,
        identified_missing_files=int((downloads["group"] == "identified_missing_file").sum()) if len(downloads) else 0,
        unidentified_references=int((downloads["group"] == "unidentified_reference").sum()) if len(downloads) else 0,
        ready_by_label_level=direct_ready_counts(payloads),
        tf_identity_of_ready=dict(
            Counter(p["tf_identity"]["status"] for p in payloads if p["readiness_state"].startswith("READY"))
        ),
        ontology=ontology.record,
        synonym_followup={
            k: synonym_followup[k] for k in ("status", "publications", "overlap", "tiers", "acquisition")
        },
        gap_followup={k: gap["report"][k] for k in ("status", "publications", "overlap", "tiers", "acquisition")},
    )
    previous, history = c.report_history(ctx, downloads)
    counts = readiness["summary"]
    identity = {
        "inputs": sha256_text(
            canonical_json(
                {
                    "advisor": [b["identity"] for b in advisor["records"]],
                    "discovery": [b["identity"] for b in discovery_result["records"]],
                    "retries": sorted(retries),
                    "parsed": sorted(str(row.get("cache_key")) for row in parse_rows),
                    "payloads": [p["payload_id"] + p["readiness_state"] for p in payloads],
                    "needed_supplements": [b["identity"] for b in needed_result["records"]],
                    # asset bytes and parser outputs: a changed supplement or parse invalidates the report
                    "asset_sha256": sorted({str(row.get("asset_sha256")) for row in parse_rows}),
                    "synonym_followup": [
                        b["identity"] for b in synonym_result["records"] + synonym_acquired["records"]
                    ],
                    "gap_followup": [b["identity"] for b in gap["result"]["records"] + gap["acquisition"]["records"]],
                    "intake": [dispositions, request_states, intake_assets],
                    "embedding": embedding_record.get("cache_id"),
                    "rules": [
                        r.SCREEN_RULE,
                        r.SERIAL_RULE,
                        r.PAYLOAD_RULE,
                        r.TF_IDENTITY_RULE,
                        r.DEPENDENCY_RULE,
                        EXCLUDED_SAMPLE_RULE,
                    ],
                    "ontology": ontology.record,
                }
            )
        )
    }
    ready_payloads = [p for p in payloads if p["readiness_state"].startswith("READY")]
    tables = {
        "screening_ledger.parquet": pd.DataFrame([_flat(i) for i in ledger_items]),
        "screening_ledger.csv": pd.DataFrame([_flat(i) for i in ledger_items]),
        "advisor_coverage.parquet": ledger,
        "advisor_coverage.csv": ledger,
        "discovery_coverage.parquet": discovery_ledger,
        "paper_coverage.csv": pd.DataFrame(
            [_flat({k: v for k, v in x.items() if k != "document_info"} | {"pmid": p}) for p, x in papers.items()]
        ),
        "coverage_assets.parquet": assets,
        "supplement_inventory.csv": c.supplement_inventory(audits),
        "supplement_dependencies.csv": pd.DataFrame([_flat(d) for d in dependencies]),
        "parse_inventory.parquet": pd.DataFrame(parse_rows),
        "parse_inventory.csv": pd.DataFrame(parse_rows),
        "manual_downloads.csv": downloads,
        "source_navigation_tasks.csv": navigation_tasks,
        "acquisition_failures.csv": failures,
        "excluded_discovery_sample.csv": pd.DataFrame([_flat(s) for s in sample["records"]]),
        "remaining_work.parquet": _remaining_work(payloads, discovery_ledger, downloads, queue, ledger_items),
    }
    jsonl = lambda rows: "".join(json.dumps(x, sort_keys=True, ensure_ascii=False, default=str) + "\n" for x in rows)  # noqa: E731
    documents_out = {
        "source_bundles_ready.jsonl": jsonl(ready_payloads),
        "bundles_all.jsonl": jsonl(payloads),
        "context_investigations.jsonl": jsonl(queue),
        "manual_downloads.md": _downloads_md(ctx.corpus_id, downloads, navigation_tasks, failures, history),
        "needed_supplement_registry.json": registry,
        "extraction_readiness.json": readiness,
        "extraction_readiness.md": _readiness_md(readiness),
        "inference_budget.json": budget,
        "inference_budget.md": _budget_md(budget),
        "coverage_report.md": _coverage_md(readiness),
        "excluded_discovery_sample.json": sample,
        "reconciliation.json": ctx.reconciliation.__dict__,
        "punctuation_probe.json": discovery_result["probe"],
        "search_retries.json": retries,
        "history.json": history,
        "embeddings.json": embedding_record,
        "before_after.json": comparison,
        "ontology_scope.json": ontology.record,
        "ontology_query_gaps.json": query_gaps,
        "synonym_followup.json": synonym_followup,
        "gap_followup.json": gap["report"],
        **manifests,
    }
    key, final, status = c.publish_report(
        ctx, "prepared", identity, tables, documents_out, {**counts, "previous_report": previous}
    )
    return {"status": status, "key": key, "artifact": final, "corpus_id": ctx.corpus_id, "counts": counts}


# ---------------------------------------------------------------------------
# steps


def _documents(parsed, audits):
    documents, meta, parse_rows, parse_of = {}, {}, [], {}
    for pmid, (document, report, attempts) in parsed["articles"].items():
        for attempt in attempts:
            parse_rows.append({"pmid": pmid, "component": "article", **_flat(attempt)})
        if document is not None:
            doc_id = report["document_id"]
            documents[doc_id] = document
            meta[doc_id] = {
                "publication_id": audits[pmid]["publication_id"],
                "pmid": pmid,
                "role": "article",
                "route": report["route"],
            }
            parse_of[doc_id] = {"state": report["state"], "reasons": report.get("reasons") or []}
    for item in parsed["supplements"]:
        report = item["report"]
        parse_rows.append(
            {"pmid": item["pmid"], "component": "supplement", "supplement": item["supplement"], **_flat(report)}
        )
        if item["document"] is not None and (report["route"] in PROSE_ROUTES or report["route"] in TABLE_ROUTES):
            doc_id = report["document_id"]
            documents[doc_id] = item["document"]
            meta[doc_id] = {
                "publication_id": audits[item["pmid"]]["publication_id"],
                "pmid": item["pmid"],
                "role": "supplement",
                "route": report["route"],
                "supplement": item["supplement"],
            }
            parse_of[doc_id] = {"state": report["state"], "reasons": report.get("reasons") or []}
    for item in parsed["alternates"]:
        parse_rows.append({"pmid": item["pmid"], "component": "alternate_article_pdf", **_flat(item["report"])})
    return documents, meta, parse_rows, parse_of


def _relevance(audits, parsed, terms, ontology=None) -> tuple[dict, dict]:
    """Per (pmid, lineage) provisional relevance from the paper's own title/abstract (rule p3-context-1)."""
    relevance, profiles = {}, {}
    for pmid, audit in audits.items():
        text = f"{audit.get('title') or ''} {audit.get('abstract') or ''}"
        profile = source_context(text, ontology)
        roles = [
            x["role"]
            for x in provisional_roles(audit.get("title"), audit.get("abstract"), audit.get("publication_types") or [])
        ]
        assay = regulatory_content(text)
        profiles[pmid] = {
            **profile,
            "regulatory_content_in_title_abstract": assay,
            "roles": roles,
            "basis": "title_abstract" if audit.get("abstract") else "title_only",
        }
        for lineage in terms:
            relevance[(pmid, lineage["cell_type"])] = context_relevance(profile, lineage["cell_type"], assay, roles)
    return relevance, profiles


def _mentions(documents, meta, audits, names, ctx, loaded):
    human = _human_gene_map(ctx.manuscript_dir, loaded.repo_root)
    by_passage: dict[str, list[dict]] = {}
    counts: Counter = Counter()
    for doc_id, document in documents.items():
        if meta[doc_id]["route"] in TABLE_ROUTES:
            continue
        found = candidate_name_mentions(document, names)
        pubtator = next(
            (a for a in audits[meta[doc_id]["pmid"]]["assets"] if a["role"] == "pubtator_annotations"), None
        )
        if pubtator and meta[doc_id]["role"] == "article":
            found += pubtator_mentions(document, json.loads((loaded.repo_root / pubtator["path"]).read_bytes()), human)
        for mention in reconcile(found):
            counts[mention.identity_status] += 1
            if mention.passage_id:
                row = mention.to_json()
                by_passage.setdefault(mention.passage_id, []).append({k: row[k] for k in MENTION_KEEP})
    return by_passage, counts


def _bundles(items, documents, meta, mentions, genes, priority, queue, parse_of) -> list[dict]:
    """One bundle per candidate anchor passage; all its TF/lineage/query associations are kept."""
    queue_rows = queue[["query_id", "cell_type", "tf_hgnc_id", "comparison_ids"]]
    by_anchor: dict[str, list[dict]] = {}
    for item in items:
        if item["outcome"] == "bundle_candidate":
            by_anchor.setdefault(item["passage_id"], []).append(item)
    passages = {p.passage_id: (doc_id, p) for doc_id, d in documents.items() for p in d.passages}
    payloads: dict[str, dict] = {}
    for passage_id, anchored in sorted(by_anchor.items()):
        doc_id, anchor = passages[passage_id]
        document = documents[doc_id]
        bundle = r.build_bundle(anchor, document, doc_id, mentions, genes)
        tfs = sorted({i["tf_hgnc_id"] for i in anchored})
        associations = []
        for item in anchored:
            for cell_type, label in item["lineages"].items():
                rows = queue_rows[
                    (queue_rows["cell_type"] == cell_type) & (queue_rows["tf_hgnc_id"] == item["tf_hgnc_id"])
                ]
                associations.append(
                    {
                        "cell_type": cell_type,
                        "tf_hgnc_id": item["tf_hgnc_id"],
                        "query_ids": sorted(rows["query_id"]),
                        "comparison_ids": sorted({x for ids in rows["comparison_ids"] for x in ids}),
                        "relevance": label["relevance"],
                        "relevance_reason": label["reason"],
                        "passage_relevance": label.get("passage_relevance"),
                    }
                )
        entry = payloads.setdefault(
            bundle["payload_id"],
            {
                **bundle,
                "publication_id": meta[doc_id]["publication_id"],
                "pmid": meta[doc_id]["pmid"],
                "document_role": meta[doc_id]["role"],
                "text_version": document.text_version,
                "source_asset_sha256": document.source_asset_sha256,
                "canonical_sha256": document.canonical_sha256,
                "document_parse": parse_of[doc_id],
                "item_ids": [],
                "tf_hgnc_ids": [],
                "attributions": [],
                "associations": [],
                "priority": 0.0,
            },
        )
        entry["item_ids"] += [i["item_id"] for i in anchored]
        entry["tf_hgnc_ids"] = sorted(set(entry["tf_hgnc_ids"]) | set(tfs))
        entry["attributions"] = sorted(set(entry["attributions"]) | {i["attribution"] for i in anchored})
        entry["associations"] += associations
        entry["priority"] = max([entry["priority"]] + [priority.get((passage_id, t), (0.0, None))[0] for t in tfs])
        kinds = entry.setdefault("_match_kinds", {})
        for i in anchored:
            kinds.setdefault(i["tf_hgnc_id"], set()).update(i.get("match_kinds", []))
    for payload in payloads.values():
        # after merging: identity covers every TF associated with the bundle, not the last group
        payload["tf_identity"] = r.tf_identity(payload, payload.pop("_match_kinds"))
        payload["identity_flags"] = sorted(
            {v["status"] for v in payload["tf_identity"]["per_tf"].values() if not v["scorable_as_resolved_human"]}
        )
        payload["lineages"] = sorted({a["cell_type"] for a in payload["associations"]})
        payload["relevance"] = {
            c: sorted({a["relevance"] for a in payload["associations"] if a["cell_type"] == c})
            for c in payload["lineages"]
        }
        # Paper-level labels prioritise; the passage label is the passage's own stated context.
        payload["passage_relevance"] = {
            c: sorted({a["passage_relevance"] for a in payload["associations"] if a["cell_type"] == c})
            for c in payload["lineages"]
        }
        payload["query_associations"] = len(
            {(a["cell_type"], q) for a in payload["associations"] for q in a["query_ids"]}
        )
    return sorted(payloads.values(), key=lambda p: p["payload_id"])


def _dependencies(payloads, audits, parsed, extensions=(), allowances=None) -> tuple[list[dict], list[dict]]:
    """Supplement dependencies of candidate bundles and the needed files still to acquire."""
    captions = {
        pmid: _supplement_captions(document) for pmid, (document, _, _) in parsed["articles"].items() if document
    }
    parsed_supplements = {}
    for item in parsed["supplements"]:
        parsed_supplements.setdefault((item["pmid"], item["supplement"]), []).append(item["report"])
    dependencies, needed = [], {}
    for payload in payloads:
        supplements = audits[payload["pmid"]].get("supplements") or []
        for reference in payload["supplement_references"]:
            resolution, matched = r.resolve_dependency(reference, supplements, captions.get(payload["pmid"]))
            files = []
            for s in matched:
                reports = parsed_supplements.get((payload["pmid"], s["filename"]), [])
                state = _dependency_state(
                    s, reports, extensions, (allowances or {}).get((payload["pmid"], s["filename"]))
                )
                if state == "to_acquire":
                    needed[(payload["pmid"], s["filename"])] = {
                        "pmid": payload["pmid"],
                        "publication_id": payload["publication_id"],
                        "filename": s["filename"],
                        "url": s["url"],
                        "md5": s["md5"],
                        "size": s["size"],
                    }
                files.append(
                    {
                        "filename": s["filename"],
                        "label": s.get("label"),
                        "url": s.get("url"),
                        "inventory_state": s["state"],
                        "state": state,
                        "asset_sha256": (s.get("asset") or {}).get("sha256"),
                    }
                )
            state = (
                ("missing_asset" if not supplements else "unresolved_reference")
                if not files
                else (min((f["state"] for f in files), key=_STATE_ORDER.index))
            )
            if resolution.endswith("container_unverified") and state.startswith("available"):
                state = f"{state}_link_unverified"  # a container may not hold the cited item
            dependencies.append(
                {
                    "dependency_id": stable_id(
                        "dependency", {"payload": payload["payload_id"], "reference": reference}
                    ),
                    "payload_id": payload["payload_id"],
                    "publication_id": payload["publication_id"],
                    "pmid": payload["pmid"],
                    "reference": reference,
                    "resolution": resolution,
                    "files": files,
                    "state": state,
                    "local_asset_sha256": sorted(f["asset_sha256"] for f in files if f["asset_sha256"]),
                    "why_needed": "cited by candidate evidence; its content may define the result",
                    "rule_version": r.DEPENDENCY_RULE,
                }
            )
    return dependencies, sorted(needed.values(), key=lambda n: (int(n["pmid"]), n["filename"]))


_STATE_ORDER = [
    "available_parsed",
    "available_partial",
    "to_acquire",
    "deferred_size_limit",
    "unsupported_format",
    "parse_failed",
    "missing_asset",
    "unresolved_reference",
]


def _supplement_captions(document) -> dict[str, str]:
    """Filename -> the article's own label/caption text for each supplementary item (JATS)."""
    text_of = {p.item_id: p.text for p in document.passages if p.kind == "supplementary" and p.item_id}
    result = {}
    for item in document.supplementary:
        if item.get("href"):
            result[Path(item["href"]).name] = (
                f"{item.get('label') or ''} {text_of.get(item.get('item_id'), '')}".strip()
            )
    return result


def _dependency_state(supplement: dict, reports: list[dict], extensions=(), size_allowance: int | None = None) -> str:
    """State of one needed file. PARTIAL (row/page limits, some archive members unparsed) is not complete."""
    if supplement["state"] == "acquired":
        members = [x for x in reports if x.get("route") != "zip"] or reports
        states = [x["state"] for x in members]
        if not states:
            return "parse_failed"
        if all(s == "PARSED" for s in states):
            return "available_parsed"
        if any(s in {"PARSED", "PARTIAL"} for s in states):
            return "available_partial"
        return "unsupported_format" if set(states) == {"NOT_PARSED"} else "parse_failed"
    if supplement["state"] in {"not_requested", "fetch_failed:timeout", "fetch_failed:server_error"}:
        return "to_acquire"
    if supplement["state"] == "size_limit_deferred":
        # A named allowance re-opens exactly this file; everything else stays deferred.
        fits = size_allowance is not None and (supplement.get("size") or 0) <= size_allowance
        return "to_acquire" if fits else "deferred_size_limit"
    if supplement["state"] == "unsupported_extension_inventoried":
        # Inventoried before this format was routed (e.g. zip/xls): acquirable now, not unsupported.
        return (
            "to_acquire"
            if Path(supplement["filename"]).suffix.lower().lstrip(".") in extensions
            else "unsupported_format"
        )
    return "missing_asset"


def _merge_needed(audits: dict, needed_result: dict) -> None:
    """Record acquired needed supplements on their publication's inventory so they are registered and parsed."""
    for record in needed_result["records"]:
        for entry in record["results"]:
            audit = audits.get(entry["pmid"])
            if audit is None:
                continue
            item = next((s for s in audit.get("supplements") or [] if s["filename"] == entry["filename"]), None)
            if item is None:
                continue
            if entry["state"] == "acquired":
                item.update(state="acquired", asset=entry["asset"], acquisition_route="needed_for_candidate_evidence")
            elif entry["state"] in {"deferred_size_limit"}:
                item["state"] = "size_limit_deferred"
            elif entry["state"].startswith("fetch_failed"):
                item["state"] = entry["state"]


def _asset_registry(audits, intake_assets, parse_rows) -> pd.DataFrame:
    """Checksummed asset registry: acquired assets plus archive members linked to their parent archive."""
    frame = c.asset_table(audits, intake_assets)
    members = [
        {
            "pmid": r["pmid"],
            "publication_id": audits[r["pmid"]]["publication_id"],
            "parent": r["parent_asset"],
            "version": "archive_member",
            "name": r["archive_member"],
            "role": "archive_member",
            "sha256": r["asset_sha256"],
            "format": str(r["archive_member"]).rsplit(".", 1)[-1].lower(),
        }
        for r in parse_rows
        if isinstance(r.get("archive_member"), str)
    ]
    return pd.concat([frame, pd.DataFrame(members)], ignore_index=True) if members else frame


def member_shas(members: list[dict]) -> set[str]:
    return {r.get("asset_sha256") for r in members}


def _registry_check(needed_result, assets, parse_rows, ledger_items) -> dict:
    """Every acquired needed supplement (and its archive members) is registered, inventoried, and screened
    or explicitly excluded with a reason."""
    registered, inventoried = (
        set(assets["sha256"]) if len(assets) else set(),
        {r.get("asset_sha256") for r in parse_rows},
    )
    screened_docs = {i["source_asset_sha256"] for i in ledger_items}
    rows = []
    for record in needed_result["records"]:
        for entry in record["results"]:
            sha = (entry.get("asset") or {}).get("sha256")
            members = [r for r in parse_rows if sha and r.get("parent_asset") == sha]
            states = {r["state"] for r in parse_rows if sha and r.get("asset_sha256") == sha} | {
                r["state"] for r in members
            }
            screened = sha in screened_docs or any(r.get("asset_sha256") in screened_docs for r in members)
            rows.append(
                {
                    "pmid": entry["pmid"],
                    "filename": entry["filename"],
                    "state": entry["state"],
                    "sha256": sha,
                    "registered": sha in registered if sha else False,
                    "parse_inventoried": sha in inventoried if sha else False,
                    "archive_members": len(members),
                    "members_registered": sum(r.get("asset_sha256") in registered for r in members),
                    "parse_states": sorted(states),
                    "screening_items_from_asset": sum(
                        1 for i in ledger_items if sha and i["source_asset_sha256"] in {sha, *member_shas(members)}
                    ),
                    "has_screening_items": screened,
                    "exclusion_reason": None if sha else entry["state"],
                    # parsed text without a candidate-TF mention yields no ledger item; that is a screening result
                    "no_screening_items_reason": None
                    if screened or not sha
                    else (
                        "parsed_no_candidate_tf_mention"
                        if states & {"PARSED", "PARTIAL"}
                        else "not_parsed:" + ",".join(sorted(states) or ["no_parse_record"])
                    ),
                }
            )
    acquired = [x for x in rows if x["sha256"]]
    return {
        "needed_files": len(rows),
        "acquired": len(acquired),
        "registered": sum(x["registered"] for x in acquired),
        "parse_inventoried": sum(x["parse_inventoried"] for x in acquired),
        "with_screening_items": sum(x["has_screening_items"] for x in acquired),
        "without_screening_items_by_reason": dict(
            Counter(x["no_screening_items_reason"] for x in acquired if not x["has_screening_items"])
        ),
        "excluded_with_reason": [x for x in rows if not x["sha256"]],
        "files": rows,
    }


def _local_sources(parsed) -> dict[str, list[str]]:
    """Per PMID, the asset SHA-256s of locally parsed supplement documents (bounded navigation scope)."""
    sources: dict[str, set[str]] = {}
    for item in parsed["supplements"]:
        if item["document"] is not None and item["report"]["state"] in {"PARSED", "PARTIAL"}:
            sources.setdefault(item["pmid"], set()).add(item["report"]["asset_sha256"])
    return {pmid: sorted(v) for pmid, v in sources.items()}


def _item_status(items, payloads_by_id) -> list[dict]:
    """Screening ledger rows with their processing status (bundled/ready, context, review, unprocessed)."""
    anchor_of = {}
    for payload in payloads_by_id.values():
        for item_id in payload["item_ids"]:
            anchor_of[item_id] = payload
    rows = []
    for item in items:
        payload = anchor_of.get(item["item_id"])
        if payload is None:
            status = {
                "requires_interpretation_review": "requires_table_interpretation_review",
                "supporting_methods_retained": "retained_supporting_context",
                "screened_irrelevant_context": "screened_irrelevant_preserved",
                "title_mention_paper_level": "not_bundled_title",
                "excluded_non_evidence_section": "not_bundled_reference_section",
            }.get(item["outcome"], "unprocessed")
            rows.append({**item, "payload_id": None, "processing_status": status, "readiness_state": None})
            continue
        state = payload["readiness_state"]
        status = (
            "bundled_source_ready"
            if state.startswith("READY")
            else "bundled_requires_context"
            if state == "NEEDS_CONTEXT"
            else "bundled_requires_attribution_or_identity_review"
            if state == "NEEDS_SCREENING_REVIEW"
            else "bundled_requires_parse_repair"
            if state == "NEEDS_PARSE_REPAIR"
            else "bundled_requires_asset"
        )
        rows.append(
            {**item, "payload_id": payload["payload_id"], "processing_status": status, "readiness_state": state}
        )
    return rows


def _paper_coverage(audits, parsed, ledger_items, payloads, dispositions, relevance, profiles) -> dict:
    """Per acquired paper: screening disposition, readiness, and why a paper has no ready bundle."""
    by_pmid_items: dict[str, list[dict]] = {}
    for item in ledger_items:
        by_pmid_items.setdefault(item["pmid"], []).append(item)
    by_pmid_payloads: dict[str, list[dict]] = {}
    for payload in payloads:
        by_pmid_payloads.setdefault(payload["pmid"], []).append(payload)
    result = {}
    for pmid, audit in audits.items():
        document, report, _ = parsed["articles"][pmid]
        state, _ = c.acquisition_state(audit, dispositions.get(pmid))
        own_items, own = by_pmid_items.get(pmid, []), by_pmid_payloads.get(pmid, [])
        ready = sorted(p["payload_id"] for p in own if p["readiness_state"].startswith("READY"))
        labels = sorted({relevance[(pmid, c)][0] for (p, c) in relevance if p == pmid})
        if document is None:
            category = "parsing_context_or_identity_failure"
        elif ready:
            category = "has_source_ready_bundles"
        elif own:
            category = (
                "insufficient_available_text"
                if document.text_version == "pubmed_abstract"
                else "parsing_context_or_identity_failure"
                if any(p["readiness_state"] == "NEEDS_PARSE_REPAIR" for p in own)
                else "bundles_blocked_pending_context_or_review"
            )
        elif own_items and all(i["processing_status"] == "screened_irrelevant_preserved" for i in own_items):
            category = "provisionally_screened_background_or_irrelevant"
        elif document.text_version == "pubmed_abstract":
            category = "insufficient_available_text"
        elif not own_items or all(i["processing_status"].startswith("not_bundled") for i in own_items):
            category = "no_candidate_found_in_inspected_content"
        else:
            category = "candidates_retained_not_bundled (methods/table regions/irrelevant)"
        disposition = (
            "CANDIDATE_PASSAGES_FOUND"
            if own
            else "CONTEXT_ONLY"
            if set(labels) <= {"biological_background_resource", "irrelevant_to_assigned_question"}
            else "NO_CANDIDATE_PASSAGES"
        )
        if document is None:
            disposition = "NOT_SCREENED"
        paper_state = (
            "READY_FULL_TEXT"
            if ready and document.text_version != "pubmed_abstract"
            else "READY_ABSTRACT_ONLY"
            if ready
            else "NEEDS_ASSET"
            if state != c.FULL_TEXT_ACQUIRED
            else "NEEDS_PARSE_REPAIR"
            if document is None
            else Counter(p["readiness_state"] for p in own).most_common(1)[0][0]
            if own
            else "NEEDS_SCREENING_REVIEW"
        )
        supplement_reports = [s["report"] for s in parsed["supplements"] if s["pmid"] == pmid]
        result[pmid] = {
            "publication_id": audit["publication_id"],
            "route": audit.get("route"),
            "acquisition_state": state,
            "text_version": document.text_version if document else None,
            "no_bundle_category": category,
            "candidate_items": len(own_items),
            "bundles": len(own),
            "ready_bundles": len(ready),
            "screening_disposition": disposition,
            "screening_reason": f"{len(own_items)} screening items, {len(own)} bundles; rule {r.SCREEN_RULE}",
            "readiness_state": paper_state,
            "readiness_reasons": sorted({x for p in own for x in p["readiness_reasons"]})[:10] if not ready else [],
            "ready_bundle_ids": ready,
            "context_labels": labels,
            "source_context": profiles[pmid],
            "document_info": _document_info(document, report, supplement_reports, state),
        }
    return result


def _excluded_sample(ctx, discovered, discovery_result, terms, ontology=None) -> dict:
    """Up to 24 excluded discovery papers: 3 per (lineage x exclusion group), reproducible by hash order."""
    records_by_pid = {}
    for record in discovery_result["records"]:
        for item in record["results"]:
            for source in item["records"]:
                key = source.get("pmid") or source.get("doi") or source.get("epmc_id")
                records_by_pid.setdefault(key, source)
    queue = ctx.queue.set_index("query_id")
    lineage_tfs = {t["cell_type"]: t["candidate_tfs"] for t in terms}
    chosen, shortfall, seen = [], {}, set()
    groups = [("metadata_only_no_exact_tf_in_title_abstract", False), ("tier2_tf_without_lineage_context", True)]
    for lineage in sorted(lineage_tfs):
        for group, tf_present in groups:
            pool = []
            for row in discovered.itertuples(index=False):
                association = row.lineage_associations.get(lineage)
                if row.advisor or association is None:
                    continue
                excluded = (
                    (not association["tfs_named"])
                    if not tf_present
                    else (association["tfs_named"] and not association["context_terms"])
                )
                if excluded and row.publication_id not in seen:
                    order = hashlib.sha256(f"{EXCLUDED_SAMPLE_RULE}|{row.publication_id}".encode()).hexdigest()
                    pool.append((order, row))
            picked = [row for _, row in sorted(pool, key=lambda x: x[0])[:3]]
            if len(picked) < 3:
                shortfall[f"{lineage}|{group}"] = 3 - len(picked)
            for row in picked:
                seen.add(row.publication_id)
                source = records_by_pid.get(row.pmid if isinstance(row.pmid, str) else row.doi) or {}
                text = f"{row.title or ''} {source.get('abstract') or ''}"
                profile = source_context(text, ontology)
                association = row.lineage_associations[lineage]
                tfs = {
                    h: n
                    for h, n in lineage_tfs[lineage].items()
                    if h in {queue.loc[q, "tf_hgnc_id"] for q in association["queries"]}
                }
                named = sorted(
                    h
                    for h, names in tfs.items()
                    if any(
                        re.search(
                            rf"(?<![A-Za-z0-9-]){re.escape(n)}"
                            rf"(?![A-Za-z0-9-])",
                            text,
                        )
                        for n in names
                    )
                )
                label, reason = context_relevance(profile, lineage, regulatory_content(text), [])
                # Absence of the TF name in a title/abstract repeats the original exclusion; it is not an
                # independent judgement, so such records stay unresolved.
                if not source.get("abstract"):
                    decision = "unresolved_insufficient_text"
                elif named and label == "direct_context_candidate":
                    decision = "potentially_relevant_consider_targeted_acquisition"
                elif not named:
                    decision = "unresolved_tf_not_in_title_abstract_full_text_not_inspected"
                elif label == "irrelevant_to_assigned_question":
                    decision = "provisionally_outside_context_title_abstract"
                else:
                    decision = "unresolved"
                chosen.append(
                    {
                        "lineage": lineage,
                        "group": group,
                        "publication_id": row.publication_id,
                        "pmid": row.pmid if isinstance(row.pmid, str) else None,
                        "title": row.title,
                        "tfs_in_title_abstract": named,
                        "context_label": label,
                        "context_reason": reason,
                        "decision": decision,
                        "text_basis": "title_abstract" if source.get("abstract") else "title",
                    }
                )
    return {
        "rule": EXCLUDED_SAMPLE_RULE,
        "selection": "per lineage and exclusion group, the 3 lowest sha256(rule|publication_id), deduplicated",
        "limitation": "a small audit sample; it does not estimate recall or show that excluded papers are irrelevant",
        "shortfall": shortfall,
        "records": chosen,
        "decisions": dict(Counter(x["decision"] for x in chosen)),
    }


def direct_ready_counts(payloads: list[dict]) -> dict:
    """Ready bundles per lineage by label level (provisional screened-context counts, not findings)."""
    counts = {}
    for p in payloads:
        if not p["readiness_state"].startswith("READY"):
            continue
        for cell_type in p["lineages"]:
            entry = counts.setdefault(cell_type, {"ready": 0, "paper_label_direct": 0, "passage_label_direct": 0})
            entry["ready"] += 1
            entry["paper_label_direct"] += "direct_context_candidate" in p["relevance"].get(cell_type, [])
            entry["passage_label_direct"] += "direct_context_candidate" in (p.get("passage_relevance") or {}).get(
                cell_type, []
            )
    return dict(sorted(counts.items()))


def _before_after(loaded, payloads, ledger_items, papers, ledger, downloads=None, assets=None) -> dict:
    previous_dir = loaded.data_root / "processed" / PREVIOUS_REPORT
    before = (
        json.loads((previous_dir / "extraction_readiness.json").read_text())["summary"] if previous_dir.is_dir() else {}
    )
    previous_bundles = (
        [json.loads(line) for line in (previous_dir / "bundles_all.jsonl").read_text().splitlines()]
        if (previous_dir / "bundles_all.jsonl").is_file()
        else []
    )
    previous_downloads = (
        pd.read_csv(previous_dir / "manual_downloads.csv")
        if (previous_dir / "manual_downloads.csv").is_file()
        else None
    )
    previous_assets = (
        pd.read_parquet(previous_dir / "coverage_assets.parquet")
        if (previous_dir / "coverage_assets.parquet").is_file()
        else None
    )
    examples = {}
    for pmid in ("32566118", "32046263", "25120651"):
        own = [p for p in payloads if p["pmid"] == pmid]
        examples[pmid] = {
            "bundles": len(own),
            "ready": sum(p["readiness_state"].startswith("READY") for p in own),
            "labels": papers.get(pmid, {}).get("context_labels"),
        }
    bundles_before = before.get("bundles") or {}
    return {
        "previous_report": PREVIOUS_REPORT,
        "before": {
            "screening_items": (before.get("screening_items") or {}).get("total"),
            "unique_bundles": bundles_before.get("unique"),
            "ready_bundles": bundles_before.get("ready_unique"),
            "bundles_by_state": bundles_before.get("by_state"),
            "context_investigations": (before.get("context_investigations") or {}).get("queued"),
            "direct_ready_by_lineage": direct_ready_counts(previous_bundles) if previous_bundles else None,
            "download_rows_by_group": previous_downloads["group"].value_counts().to_dict()
            if previous_downloads is not None
            else None,
            "registered_assets": len(previous_assets) if previous_assets is not None else None,
        },
        "after": {
            "screening_items": len(ledger_items),
            "unique_bundles": len(payloads),
            "ready_bundles": sum(p["readiness_state"].startswith("READY") for p in payloads),
            "bundles_by_state": dict(Counter(p["readiness_state"] for p in payloads)),
            "direct_ready_by_lineage": direct_ready_counts(payloads),
            "download_rows_by_group": downloads["group"].value_counts().to_dict()
            if downloads is not None and len(downloads)
            else {},
            "registered_assets": len(assets) if assets is not None else None,
        },
        "note": "Context labels are provisional screened-context counts from deterministic rules; they are not "
        "experiment-local biological evidence and do not show that relevant literature is absent.",
        "review_examples": examples,
    }


def _previous_advisor_with_bundles(previous_dir: Path) -> int | None:
    path = previous_dir / "advisor_coverage.parquet"
    if not path.is_file():
        return None
    return int((pd.read_parquet(path)["screening_disposition"] == "CANDIDATE_PASSAGES_FOUND").sum())


# ---------------------------------------------------------------------------
# helpers and reports


def _flat(report: dict) -> dict:
    return {
        k: (json.dumps(v, sort_keys=True, default=str) if isinstance(v, dict | list) else v) for k, v in report.items()
    }


ROW_SELECTOR_RULE = "p3-table-row-selector-1"


def recovered_full_text(ctx) -> list[dict]:
    """Assets recovered by a completed `full-text-retry` run (read directly; order-independent)."""
    directory = ctx.work_dir / "full_text_retry"
    return [
        entry
        for path in sorted(directory.glob("batch-*.json"))
        for entry in c.read_json(path)["results"]
        if entry.get("asset")
    ]


def _exception_needs(audits: dict, exceptions, needed: list[dict]) -> list[dict]:
    """A supplement with a named size allowance is acquired on its own account, even when no bundle
    references it yet (the allowance is the lead's decision that the file is required)."""
    already = {(n["pmid"], n["filename"]) for n in needed}
    extra = []
    for exception in exceptions:
        audit = audits.get(exception.pmid)
        if audit is None or (exception.pmid, exception.filename) in already:
            continue
        for supplement in audit.get("supplements") or []:
            if supplement["filename"] != exception.filename or supplement.get("asset"):
                continue
            if (supplement.get("size") or 0) > exception.max_bytes:
                continue
            extra.append(
                {
                    "pmid": exception.pmid,
                    "publication_id": audit["publication_id"],
                    "filename": exception.filename,
                    "url": supplement.get("url"),
                    "md5": supplement.get("md5"),
                    "size": supplement.get("size"),
                    "requested_by": "named_size_allowance",
                }
            )
    return extra


def _row_selector(tf_names: dict[str, list[str]], ontology) -> files.RowSelector:
    """Rows of large supplementary tables worth materializing: a candidate TF name, or a manuscript
    population name (tables spell them with underscores as well as spaces)."""
    symbols = {name.upper() for names in tf_names.values() for name in names}
    phrases = set()
    for table in (ontology.strict, ontology.broad):
        for lineage_phrases in table.values():
            for phrase in lineage_phrases:
                phrases.add(phrase.lower())
                phrases.add(phrase.lower().replace(" ", "_"))
    return files.RowSelector(ROW_SELECTOR_RULE, frozenset(symbols), frozenset(phrases))


def _names(queue: pd.DataFrame) -> dict[str, list[str]]:
    names: dict[str, list[str]] = {}
    for row in queue.itertuples(index=False):
        terms = json.loads(row.terms_json)
        names.setdefault(row.tf_hgnc_id, list(terms["tf"]))
        if isinstance(row.target_hgnc_id, str):
            names.setdefault(row.target_hgnc_id, list(terms["target"]))
    return names


def _document_info(document, report, supplement_reports: list[dict], state: str) -> dict:
    if document is None:
        return {"parsing_state": "PARSE_FAILED" if report else "NOT_PARSED", "missing": ["article_text"]}
    kinds = Counter(p.kind for p in document.passages)
    supplements = Counter(s["state"] for s in supplement_reports)
    missing = []
    if document.text_version == "pubmed_abstract":
        missing.append("article_full_text")
    if supplements.get("NOT_PARSED") or supplements.get("PARSE_FAILED"):
        missing.append("some_supplements_unparsed_or_unsupported")
    if document.text_version == "pubtator_bioc":
        missing.append("table_column_structure (BioC flattens tables)")
    return {
        "parsing_state": report["state"],
        "parser": report.get("parser"),
        "document_id": report["document_id"],
        "components": {
            "text_version": document.text_version,
            "paragraphs": kinds.get("paragraph", 0),
            "abstract": kinds.get("abstract", 0),
            "figure_captions": kinds.get("figure_caption", 0),
            "table_rows": kinds.get("table_row", 0),
            "supplement_parse_states": dict(supplements),
        },
        "missing": missing,
        "text": document.canonical_text if document.text_version != "pubmed_abstract" else None,
    }


def _discovery_ledger(discovered: pd.DataFrame, order, audits, papers, route: str = "p2_queue") -> pd.DataFrame:
    """One row per discovered publication. Supplemental synonym rows (only papers new to P2 discovery
    and the advisor list) carry their tier from `synonym_publications`."""
    tier1 = {pid for pid, _ in order}
    rows = []
    for row in discovered.itertuples(index=False):
        pmid = row.pmid if isinstance(row.pmid, str) else None
        audit = audits.get(pmid) if pmid else None
        if route != "p2_queue":
            tier = row.tier
        elif row.advisor:
            tier = "advisor_route"
        elif row.publication_id in tier1:
            tier = "tier1_acquired"
        elif row.eligible_lineages:
            tier = "tier2_deferred_no_lineage_context_in_title_abstract" if pmid else "deferred_no_pmid"
        else:
            tier = "metadata_only_no_exact_tf_in_title_abstract"
        state, reason = c.acquisition_state(audit) if audit else (c.NOT_CHECKED, tier)
        paper = papers.get(pmid) or {}
        rows.append(
            {
                "publication_id": row.publication_id,
                "discovery_route": route,
                "pmid": pmid,
                "pmcid": row.pmcid,
                "doi": row.doi,
                "title": row.title,
                "year": row.year,
                "retracted": bool(row.retracted),
                "advisor": bool(row.advisor),
                "tier": tier,
                "query_associated_lineages": json.dumps(sorted(row.lineage_associations)),
                "eligible_lineages": json.dumps(list(row.eligible_lineages)),
                "lineage_associations": json.dumps(row.lineage_associations, sort_keys=True, default=list),
                "context_labels": json.dumps(paper.get("context_labels") or []),
                "query_hits": int(row.query_hits),
                "acquisition_state": state,
                "acquisition_reason": reason,
                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else None,
                "no_bundle_category": paper.get("no_bundle_category"),
                "bundles": paper.get("bundles"),
                "ready_bundles": paper.get("ready_bundles"),
                "readiness_state": paper.get("readiness_state", "NOT_ACQUIRED"),
                "extraction_status": "NOT_RUN",
            }
        )
    return pd.DataFrame(rows)


def _downloads(
    ctx, audits, papers, dependencies, discovery_ledger, request_states
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """User-facing requests and, separately, source-navigation tasks (never download placeholders).

    Groups: identified_missing_file (a named supplement no route could supply), size_or_parse_repair
    (a named file that is too large or failed/unsupported), unidentified_reference (the cited item is
    not identifiable and no local candidate exists; one row per reference), and article PDFs by
    priority. References that local sources may resolve are source-navigation tasks instead.
    """
    rows: dict[str, dict] = {}
    tasks = []
    for dep in dependencies:
        audit = audits[dep["pmid"]]
        state = dep["state"]
        if state.startswith("available") and not state.endswith("link_unverified"):
            continue
        if state == "unresolved_reference" or state.endswith("link_unverified"):
            local = [f for f in dep["files"] if f.get("asset_sha256")]
            if local or any(s.get("asset") for s in audit.get("supplements") or []):
                tasks.append(
                    {
                        "task_id": stable_id("navigate", {"dependency": dep["dependency_id"]}),
                        "pmid": dep["pmid"],
                        "publication_id": dep["publication_id"],
                        "reference": dep["reference"],
                        "resolution": dep["resolution"],
                        "payload_id": dep["payload_id"],
                        "candidate_local_assets": json.dumps(dep["local_asset_sha256"]),
                        "kind": "source_navigation_local_candidates",
                    }
                )
                continue
            key = stable_id("download", {"pmid": dep["pmid"], "reference": dep["reference"]})
            row = rows.setdefault(
                key,
                _download_row(
                    audit,
                    "unidentified_reference",
                    f"cited item '{dep['reference']}'",
                    None,
                    "the cited supplementary item is not identifiable from the article's inventory; obtain the "
                    "publisher's supplementary package or record a disposition",
                    None,
                    [],
                    request_states,
                    key,
                ),
            )
            row["affected_bundles"] = json.dumps(sorted(set(json.loads(row["affected_bundles"])) | {dep["payload_id"]}))
            continue
        for f in dep["files"]:
            group = "identified_missing_file" if state == "missing_asset" else "size_or_parse_repair"
            filename = f"supplement-{f['filename']}"
            key = stable_id("download", {"pmid": dep["pmid"], "item": filename})
            why = {
                "missing_asset": "named supplement not available through an open-access route",
                "deferred_size_limit": "open-access file exceeds the configured size bound (download from the link)",
                "unsupported_format": "file format has no reader; an alternative format or review is needed",
                "parse_failed": "file could not be parsed; an alternative copy or inspection is needed",
            }.get(state, state)
            row = rows.setdefault(
                key,
                _download_row(
                    audit, group, f"supplement {f['filename']}", filename, why, f.get("url"), [], request_states, key
                ),
            )
            row["cited_as"] = json.dumps(sorted(set(json.loads(row["cited_as"])) | {dep["reference"]}))
            row["affected_bundles"] = json.dumps(sorted(set(json.loads(row["affected_bundles"])) | {dep["payload_id"]}))
    for pmid, paper in papers.items():
        if paper["acquisition_state"] == c.FULL_TEXT_ACQUIRED:
            continue
        audit = audits[pmid]
        labels = set(paper["context_labels"])
        if paper["bundles"] and "direct_context_candidate" in labels:
            group, why = "article_required_for_candidate_evidence", "abstract names a manuscript TF in direct context"
        elif paper["bundles"] or (
            audit.get("route") == "advisor"
            and labels - {"irrelevant_to_assigned_question", "biological_background_resource"}
        ):
            group, why = (
                "article_potentially_useful_awaiting_relevance_review",
                "candidate TF evidence or unresolved relevance",
            )
        else:
            group, why = "article_lower_priority_background", "no candidate TF evidence in the available text"
        links = [x for x in audit.get("links") or [] if x["kind"] == "returned_full_text"]
        key = stable_id("download", {"pmid": pmid, "item": "article.pdf"})
        rows.setdefault(
            key,
            _download_row(
                audit,
                group,
                "article PDF",
                "article.pdf",
                f"{why}; {c.acquisition_state(audit)[1]}",
                links[0]["url"] if links else None,
                list(paper["ready_bundle_ids"]),
                request_states,
                key,
            ),
        )
    order = {g: i for i, g in enumerate(DOWNLOAD_GROUPS)}
    frame = pd.DataFrame(list(rows.values()))
    frame = frame.sort_values(
        ["group", "route", "pmid"], key=lambda s: s.map(order) if s.name == "group" else s, kind="mergesort"
    ).reset_index(drop=True)
    return frame, pd.DataFrame(tasks)


DOWNLOAD_GROUPS = [
    "identified_missing_file",
    "article_required_for_candidate_evidence",
    "size_or_parse_repair",
    "unidentified_reference",
    "article_potentially_useful_awaiting_relevance_review",
    "article_lower_priority_background",
]


def _download_row(audit, group, item, filename, why, link, bundles, request_states, request_id) -> dict:
    pmid = audit["pmid"]
    state = request_states.get(request_id, {})
    return {
        "request_id": request_id,
        "group": group,
        "route": audit.get("route"),
        "pmid": pmid,
        "doi": audit.get("doi"),
        "title": audit.get("title"),
        "year": audit.get("year"),
        "item": item,
        "expected_filename": filename,
        "inbox_destination": f"{c.INBOX}/{pmid}/{filename}" if filename else None,
        "why": why,
        "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "pmc_url": f"https://pmc.ncbi.nlm.nih.gov/articles/{audit['pmcid']}/" if audit.get("pmcid") else None,
        "doi_url": f"https://doi.org/{audit['doi']}" if audit.get("doi") else None,
        "verified_link": link,
        "access": "access_restricted_or_not_open_access"
        if audit.get("is_open_access") is False
        else "open_access"
        if audit.get("is_open_access")
        else "unknown",
        "transient_failures": "; ".join(e for e in audit.get("errors") or [] if "timeout" in e or "server_error" in e),
        "cited_as": json.dumps([]),
        "affected_bundles": json.dumps(sorted(bundles)),
        "state": state.get("state", "NEEDED" if filename else "NEEDS_IDENTIFICATION"),
        "local_asset_sha256": state.get("sha256"),
    }


def _downloads_md(corpus_id, downloads, tasks, failures, history) -> str:
    lines = [
        f"# Manual downloads and identification tasks — {corpus_id}",
        "",
        "Place each file at its inbox path, list it in `data/papers/manual_inbox/intake.csv`",
        "(`pmid,filename,role,source_url,acquired_on,disposition,note`), then run `regkg literature intake`.",
        "A filename is a mapping hint, not identity proof. DOI links are landing pages. No login/proxy URLs.",
        "Unidentified references are not downloads: each is a separate identification task.",
        "",
    ]
    titles = {
        "identified_missing_file": "Identified missing supplement files",
        "article_required_for_candidate_evidence": "Article PDFs required for candidate evidence",
        "size_or_parse_repair": "Size-limit or parse repairs (file known)",
        "unidentified_reference": "Unidentified cited items (identification tasks, not downloads)",
        "article_potentially_useful_awaiting_relevance_review": "Article PDFs potentially useful (relevance review)",
        "article_lower_priority_background": "Lower-priority background article PDFs",
    }
    for group, heading in titles.items():
        part = downloads[downloads["group"] == group] if len(downloads) else downloads
        lines += [f"## {heading} ({len(part)} items, {part['pmid'].nunique() if len(part) else 0} papers)", ""]
        for row in part.itertuples(index=False):
            links = " · ".join(
                filter(
                    None,
                    [
                        c._md_link("PubMed", row.pubmed_url),
                        c._md_link("PMC", row.pmc_url),
                        c._md_link("DOI", row.doi_url),
                        c._md_link("link", row.verified_link),
                    ],
                )
            )
            target = (
                f"→ `{row.inbox_destination}`" if isinstance(row.inbox_destination, str) else "(no file destination)"
            )
            lines.append(
                f"- [{row.state}] PMID {row.pmid} ({c._md_text(row.year)}, {row.route}) {c._md_text(row.title)} — "
                f"{c._md_text(row.item)} {target}; {c._md_text(row.why)}; access {row.access}"
                + (f"; transient failures: {c._md_text(row.transient_failures)}" if row.transient_failures else "")
                + f"; {links}"
            )
        lines.append("")
    lines += [f"## Source-navigation tasks for P4 ({len(tasks)}) — local sources may resolve these; no download", ""]
    lines += [f"## Acquisition and parse failures ({len(failures)}) — system errors, not access restrictions", ""]
    for row in failures.itertuples(index=False):
        outcome = f"recovered by {row.recovered_by}" if isinstance(row.recovered_by, str) else row.manual_fallback
        lines.append(f"- PMID {row.pmid} [{row.stage}]: {c._md_text(row.detail)} ({c._md_text(outcome)})")
    if history:
        lines += ["", f"## Changes since the previous report ({len(history)})", ""]
        lines += [f"- PMID {h['pmid']}: {h['previous_state']} → {h['current_state']}" for h in history]
    return "\n".join(lines) + "\n"


def _lineage_coverage(ctx, payloads, ledger_items, discovery_ledger, queue) -> dict:
    memberships = pd.read_parquet(ctx.manuscript_dir / "lineage_tf_memberships.parquet")
    comparisons = pd.read_parquet(ctx.manuscript_dir / "comparisons.parquet")
    lineages = {}
    for lineage in ctx.scope.lineages:
        cell = lineage.cell_type
        own = [p for p in payloads if cell in p["lineages"]]
        items = [i for i in ledger_items if cell in i["lineages"]]
        labels = Counter(p["relevance"][cell][0] if p["relevance"].get(cell) else "unresolved" for p in own)
        regulators = {}
        for m in memberships[memberships["cell_type"] == cell].itertuples(index=False):
            mine = [p for p in own if m.tf_hgnc_id in p["tf_hgnc_ids"]]
            regulators[m.tf_approved_symbol] = {
                "screening_items": sum(1 for i in items if i["tf_hgnc_id"] == m.tf_hgnc_id),
                "bundles": len(mine),
                "ready": sum(p["readiness_state"].startswith("READY") for p in mine),
                "ready_direct_context": sum(
                    p["readiness_state"].startswith("READY")
                    and "direct_context_candidate" in p["relevance"].get(cell, [])
                    for p in mine
                ),
                "papers_with_bundles": len({p["pmid"] for p in mine}),
            }
        per_comparison = {}
        for cmp in comparisons[
            (comparisons["cell_type"] == cell) & (comparisons["comparison_role"] == "primary_regulatory")
        ].itertuples(index=False):
            mine = [p for p in own if any(cmp.comparison_id in a["comparison_ids"] for a in p["associations"])]
            per_comparison[f"{cmp.condition} ({cmp.comparison_id})"] = {
                "bundles": len(mine),
                "ready": sum(p["readiness_state"].startswith("READY") for p in mine),
            }
        lineages[cell] = {
            "screening_items": len(items),
            "bundles": len(own),
            "ready_bundles": sum(p["readiness_state"].startswith("READY") for p in own),
            "bundle_relevance_labels": dict(labels),
            "context_investigations": sum(cell in q["manuscript_lineages"] for q in queue),
            "blocked": dict(Counter(p["readiness_state"] for p in own if not p["readiness_state"].startswith("READY"))),
            "named_regulators": regulators,
            "primary_comparisons": per_comparison,
        }
    return lineages


def _readiness_json(
    ctx,
    ledger,
    discovery_ledger,
    payloads,
    batches,
    downloads,
    parse_rows,
    coverage,
    embedding_record,
    mention_counts,
    discovery_result,
    ledger_items,
    queue,
    papers,
    dependencies,
    comparison,
    retries,
    sample,
) -> dict:
    parse = pd.DataFrame(parse_rows)
    ready = [p for p in payloads if p["readiness_state"].startswith("READY")]
    acquired = [p for p in papers.values()]
    summary = {
        "advisor_seed_pmids": ctx.reconciliation.unique_pmids,
        "advisor_memberships_reconciled": ctx.reconciliation.memberships,
        "unique_publications": {
            "advisor": len(ledger),
            "discovery_unique": int((~discovery_ledger["advisor"]).sum()),
            "acquired_total": len(acquired),
        },
        "availability": dict(
            Counter(
                "full_text" if p["acquisition_state"] == c.FULL_TEXT_ACQUIRED else "abstract_only" for p in acquired
            )
        ),
        "papers_or_bundles_extracted": 0,
        "screening_items": {
            "total": len(ledger_items),
            "unique_source_regions": len(
                {i["passage_id"] or f"{i['document_id']}|{i['table_id']}" for i in ledger_items}
            ),
            "by_processing_status": dict(Counter(i["processing_status"] for i in ledger_items)),
            "by_attribution": dict(Counter(i["attribution"] for i in ledger_items)),
        },
        "bundles": {
            "unique": len(payloads),
            "ready_unique": len(ready),
            "query_lineage_associations": sum(p["query_associations"] for p in payloads),
            "by_state": dict(Counter(p["readiness_state"] for p in payloads)),
            "blocker_reasons": dict(Counter(x.split(":")[0] for p in payloads for x in p["readiness_reasons"])),
            "serialized_chars_max": max((p["serialized_chars"] for p in payloads), default=0),
        },
        "context_investigations": {"queued": len(queue), "by_gap": dict(Counter(q["gap_type"] for q in queue))},
        "supplement_dependencies": {
            "total": len(dependencies),
            "by_state": dict(Counter(d["state"] for d in dependencies)),
        },
        "ready_batches": len(batches),
        "acquired_papers_without_ready_bundles": dict(
            Counter(p["no_bundle_category"] for p in acquired if not p["ready_bundles"])
        ),
        "papers_with_ready_bundles": sum(1 for p in acquired if p["ready_bundles"]),
        "advisor_readiness": ledger["readiness_state"].value_counts().to_dict(),
        "papers_awaiting_user_files": {
            g: int(downloads.loc[(downloads["group"] == g) & (downloads["state"] == "NEEDED"), "pmid"].nunique())
            for g in downloads["group"].unique()
        }
        if len(downloads)
        else {},
        # identification tasks (which file is "Figure S2"?) are not user downloads
        "papers_with_unidentified_references": int(
            downloads.loc[downloads["group"] == "unidentified_reference", "pmid"].nunique()
        )
        if len(downloads)
        else 0,
        "discovery_tiers": discovery_ledger["tier"].value_counts().to_dict(),
        "queries": {
            "total": len(ctx.queue),
            "executed": sum(len(b["items"]) for b in discovery_result["records"]),
            "retried": {q: v["result"]["status"] for q, v in retries.items()},
            "punctuation_normalization": discovery_result["probe"]["normalization"],
        },
        "parse_states_by_route": {
            f"{k[0]}|{k[1]}": int(v) for k, v in parse.groupby(["route", "state"]).size().items()
        },
        "mention_identity_status": dict(mention_counts),
        "retrieval": {
            k: embedding_record.get(k)
            for k in (
                "dense_status",
                "selector",
                "passages",
                "unique_chunks",
                "cache_misses_before_encoding",
                "embedding_requests",
            )
        },
        "excluded_sample_decisions": sample["decisions"],
        "before_after": {"before": comparison["before"], "after": comparison["after"]},
        "corpus_frozen": False,
        "freeze_blockers": [
            "user downloads/dispositions for listed assets",
            "lead review of provisional roles, context "
            "labels, attribution-unresolved items, and background dispositions",
            "P4 context investigations are queued, not run",
            "LLM provider/model/key selection by the user",
        ],
    }
    return {
        "generated_at": utc_now(),
        "corpus_id": ctx.corpus_id,
        "summary": summary,
        "lineages": coverage,
        "ready_batches": [
            {k: b[k] for k in ("batch_index", "papers", "scheduled_calls")} | {"bundles": len(b["payload_ids"])}
            for b in batches
        ],
    }


def _remaining_work(payloads, discovery_ledger, downloads, queue, ledger_items) -> pd.DataFrame:
    rows = [
        {
            "kind": "bundle",
            "id": p["payload_id"],
            "pmid": p["pmid"],
            "state": p["readiness_state"],
            "ready_batch": p.get("ready_batch"),
            "reasons": json.dumps(p["readiness_reasons"]),
            "lineages": json.dumps(p["lineages"]),
        }
        for p in payloads
    ]
    rows += [
        {
            "kind": "context_investigation",
            "id": q["investigation_id"],
            "pmid": q["pmid"],
            "state": q["status"],
            "ready_batch": None,
            "reasons": q["gap_type"],
            "lineages": json.dumps(q["manuscript_lineages"]),
        }
        for q in queue
    ]
    rows += [
        {
            "kind": "table_region_interpretation",
            "id": i["item_id"],
            "pmid": i["pmid"],
            "state": i["processing_status"],
            "ready_batch": None,
            "reasons": i["outcome_reason"],
            "lineages": json.dumps(sorted(i["lineages"])),
        }
        for i in ledger_items
        if i["processing_status"] == "requires_table_interpretation_review"
    ]
    rows += [
        {
            "kind": f"download:{d.group}",
            "id": d.request_id,
            "pmid": d.pmid,
            "state": d.state,
            "ready_batch": None,
            "reasons": d.why,
            "lineages": None,
        }
        for d in downloads.itertuples(index=False)
    ]
    deferred = discovery_ledger[discovery_ledger["tier"].str.startswith(("tier2", "deferred"))]
    rows += [
        {
            "kind": "deferred_discovery_paper",
            "id": d.publication_id,
            "pmid": d.pmid,
            "state": d.tier,
            "ready_batch": None,
            "reasons": "not acquired (outside the tier-1 frontier)",
            "lineages": d.eligible_lineages,
        }
        for d in deferred.itertuples(index=False)
    ]
    return pd.DataFrame(rows)


def _readiness_md(readiness: dict) -> str:
    s = readiness["summary"]
    ba = s["before_after"]
    lines = [
        "# Extraction readiness (preparation only; corpus NOT frozen)",
        "",
        f"Corpus `{readiness['corpus_id']}`, generated {readiness['generated_at']}.",
        "",
        "## Coverage",
        "",
        f"- Unique publications: {s['unique_publications']}; availability of acquired papers: {s['availability']}",
        f"- Screening items: {s['screening_items']['total']} ({s['screening_items']['unique_source_regions']} unique "
        f"source regions); by status {s['screening_items']['by_processing_status']}",
        f"- Attribution labels: {s['screening_items']['by_attribution']}",
        f"- Bundles: {s['bundles']['unique']} unique ({s['bundles']['query_lineage_associations']} query/lineage "
        f"associations); ready {s['bundles']['ready_unique']}; by state {s['bundles']['by_state']}",
        f"- Blocker reasons: {s['bundles']['blocker_reasons']}",
        f"- Context investigations queued for P4 (not run): {s['context_investigations']}",
        f"- Supplement dependencies: {s['supplement_dependencies']}",
        f"- Ready batches (<= 10 papers, <= 20 bundles, <= 40 scheduled calls): {s['ready_batches']}",
        f"- Papers with ready bundles: {s['papers_with_ready_bundles']}; acquired papers without ready bundles: "
        f"{s['acquired_papers_without_ready_bundles']}",
        f"- Papers awaiting user files: {s['papers_awaiting_user_files']}",
        f"- Papers/bundles extracted: {s['papers_or_bundles_extracted']} (P4 not run)",
        "",
        "## Before/after (previous: global top-10 per query)",
        "",
        f"- Before: {ba['before']}",
        f"- After: {ba['after']}",
        "",
        "## Per lineage",
        "",
    ]
    for cell, info in readiness["lineages"].items():
        lines.append(f"### {cell}")
        lines.append(
            f"- Screening items {info['screening_items']}; bundles {info['bundles']}, ready "
            f"{info['ready_bundles']}; relevance labels {info['bundle_relevance_labels']}; investigations "
            f"{info['context_investigations']}; blocked {info['blocked']}"
        )
        for name, reg in info["named_regulators"].items():
            lines.append(f"  - {name}: {reg}")
        for cmp, info2 in info["primary_comparisons"].items():
            lines.append(f"  - comparison {cmp}: {info2}")
        lines.append("")
    lines += ["## Why the corpus is not frozen", ""] + [f"- {b}" for b in s["freeze_blockers"]]
    return "\n".join(lines) + "\n"


def _budget_md(budget: dict) -> str:
    lines = [
        "# Inference budget — ESTIMATE ONLY (no chat calls made)",
        "",
        budget["status"],
        "",
        f"Counts: {budget['counts']}",
        "",
        "| Scenario | Row | Input tokens | Output tokens (incl. reasoning) | Calls | USD by illustrative rate |",
        "|---|---|---|---|---|---|",
    ]
    for scenario, rows in budget["scenarios"].items():
        for name, row in rows.items():
            usd = ", ".join(f"{k} ${v}" for k, v in row["usd"].items())
            lines.append(f"| {scenario} | {name} | {row['input']:,} | {row['output']:,} | {row['calls']:,} | {usd} |")
    lines += [
        "",
        "## Assumptions",
        "",
        "```json",
        json.dumps(budget["assumptions"], indent=1),
        "```",
        "",
        "## Notes",
        "",
    ]
    return "\n".join(lines + [f"- {n}" for n in budget["notes"]]) + "\n"


def _coverage_md(readiness: dict) -> str:
    s = readiness["summary"]
    return "\n".join(
        [
            "# Corpus coverage report",
            "",
            f"- Advisor PMIDs {s['advisor_seed_pmids']}, memberships {s['advisor_memberships_reconciled']} "
            "(reconciled from source files)",
            f"- Queries: {s['queries']}",
            f"- Discovery tiers: {s['discovery_tiers']}",
            f"- Parse states by route: {s['parse_states_by_route']}",
            f"- Mention identity status: {s['mention_identity_status']}",
            f"- Retrieval: {s['retrieval']}",
            f"- Excluded-sample decisions: {s['excluded_sample_decisions']}",
            "",
            "See extraction_readiness.md, inference_budget.md, and before_after.json.",
            "",
        ]
    )
