"""P3 corpus readiness: the whole advisor corpus plus the manuscript discovery queue.

Work runs in resumable batches (at most ten publications per acquisition batch, twenty queries
per discovery batch) persisted under `data/work/<corpus_id>/`. A completed batch is never redone;
an interrupted run resumes at the first missing batch. Reports are published as immutable
`litcorpus-*` artifacts. Nothing here calls a chat model.
"""

from __future__ import annotations

import csv
import json
import os
import re
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import pandas as pd

import regkg
from regkg.analysis import schemas as candidate_schemas
from regkg.analysis.verify import artifact_integrity as candidate_integrity
from regkg.config import (
    CorpusConfig,
    LiteratureConfig,
    LoadedProjectConfig,
    ManuscriptScopeConfig,
    load_literature_config,
)
from regkg.literature.acquire import PaperAcquisition, acquire_batch
from regkg.literature.advisors import AdvisorReconciliation, reconcile_advisors
from regkg.literature.http import SourceClient
from regkg.literature.screening import PRIMARY, UNCERTAIN, lineage_signals, provisional_roles
from regkg.provenance import (
    canonical_json,
    code_fingerprint,
    describe_outputs,
    discard_directory,
    git_revision,
    new_execution_id,
    publish_directory,
    read_json,
    sha256_file,
    sha256_text,
    stable_id,
    staging_directory,
    utc_now,
    write_json,
)
from regkg.workflows.literature import CODE_PATHS, _client

CORPUS_SCHEMA = "p3-corpus-1"
# Bump when the stored meaning of a batch record changes; completed batches are otherwise reused.
WORK_VERSION = "p3-corpus-work-1"
BASELINE_CANDIDATES = "candidates-ad74f8d35867b7f3"

# Acquisition states (coverage ledger)
NOT_CHECKED = "NOT_CHECKED"
FULL_TEXT_ACQUIRED = "FULL_TEXT_ACQUIRED"
ABSTRACT_ONLY = "ABSTRACT_ONLY"
MANUAL_DOWNLOAD_NEEDED = "MANUAL_DOWNLOAD_NEEDED"
FETCH_FAILED = "FETCH_FAILED"
IDENTITY_REVIEW_REQUIRED = "IDENTITY_REVIEW_REQUIRED"
UNAVAILABLE_CONFIRMED = "UNAVAILABLE_CONFIRMED"


class CorpusError(RuntimeError):
    """Corpus preparation failed; completed batches remain and nothing partial was published."""


@dataclass
class CorpusContext:
    loaded: LoadedProjectConfig
    literature: LiteratureConfig
    corpus: CorpusConfig
    manuscript_key: str
    manuscript_dir: Path
    scope: ManuscriptScopeConfig
    queue: pd.DataFrame
    candidates: pd.DataFrame
    advisors: pd.DataFrame
    reconciliation: AdvisorReconciliation
    corpus_id: str
    work_dir: Path

    @property
    def papers_root(self) -> Path:
        return self.loaded.data_root / "papers"


def corpus_context(loaded: LoadedProjectConfig, manuscript_key: str, literature: Path) -> CorpusContext:
    config = load_literature_config(literature)
    if config.corpus is None:
        raise CorpusError(f"{literature} has no corpus section")
    processed = loaded.data_root / "processed"
    manuscript_dir, baseline_dir = processed / manuscript_key, processed / BASELINE_CANDIDATES
    for directory, schema in (
        (manuscript_dir, candidate_schemas.MANUSCRIPT_SCHEMA_VERSION),
        (baseline_dir, candidate_schemas.CANDIDATE_SCHEMA_VERSION),
    ):
        failed = (
            [c for c in candidate_integrity(directory, schema) if not c.passed] if directory.is_dir() else ["missing"]
        )
        if failed:
            raise CorpusError(f"{directory.name} is missing or failed integrity: {failed}")
    # The accepted AT1 baseline is the advisor-seed authority; the manuscript artifact must agree.
    advisors = pd.read_parquet(baseline_dir / "seed_publications.parquet")
    if sha256_file(baseline_dir / "seed_publications.parquet") != sha256_file(
        manuscript_dir / "seed_publications.parquet"
    ):
        raise CorpusError("advisor seed tables of the baseline and manuscript candidate artifacts differ")
    lists = read_json(baseline_dir / "resources.json")["seed_publication_lists"]
    reconciliation = reconcile_advisors(advisors, lists, loaded.repo_root)
    manifest = read_json(manuscript_dir / "manifest.json")
    scope = ManuscriptScopeConfig.model_validate(manifest["config"]["scope"])
    identity = {
        "manuscript_key": manuscript_key,
        "advisor_seeds_sha256": sha256_file(baseline_dir / "seed_publications.parquet"),
        "corpus_version": config.corpus.version,
    }
    corpus_id = f"corpus-{sha256_text(canonical_json(identity))[:16]}"
    return CorpusContext(
        loaded,
        config,
        config.corpus,
        manuscript_key,
        manuscript_dir,
        scope,
        pd.read_parquet(manuscript_dir / "retrieval_queue.parquet").sort_values("priority"),
        pd.read_parquet(manuscript_dir / "candidates.parquet"),
        advisors,
        reconciliation,
        corpus_id,
        loaded.data_root / "work" / corpus_id,
    )


def lineage_terms(ctx: CorpusContext) -> list[dict]:
    """Per lineage: named regulators and candidate TFs with their queue names, plus context terms."""
    names: dict[str, list[str]] = {}
    for row in ctx.queue.itertuples(index=False):
        names.setdefault(row.tf_hgnc_id, list(json.loads(row.terms_json)["tf"]))
    result = []
    for lineage in ctx.scope.lineages:
        own = ctx.candidates[ctx.candidates["cell_type"] == lineage.cell_type]
        named = sorted(set(own.loc[own["is_seed"], "tf_hgnc_id"]))
        result.append(
            {
                "cell_type": lineage.cell_type,
                "named_tfs": {h: names[h] for h in named},
                "candidate_tfs": {h: names[h] for h in sorted(set(own["tf_hgnc_id"]))},
                "context_terms": lineage.context_terms,
            }
        )
    return result


# ---------------------------------------------------------------------------
# Resumable batches


def _atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}")
    temporary.write_text(json.dumps(value, sort_keys=True, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(temporary, path)


def run_batches(directory: Path, items: list, size: int, identity: dict, process, limit: int | None = None) -> dict:
    """Process `items` in fixed batches; completed batches (same items and identity) are reused.

    Returns {"records": [...completed batch records...], "pending_batches": n, "executed": n}.
    """
    chunks = [items[i : i + size] for i in range(0, len(items), size)]
    records, executed = [], 0
    for index, chunk in enumerate(chunks, start=1):
        path = directory / f"batch-{index:03d}.json"
        batch_identity = sha256_text(canonical_json({"items": chunk, "work": WORK_VERSION, **identity}))
        if path.is_file():
            stored = read_json(path)
            if stored.get("identity") == batch_identity:
                records.append(stored)
                continue
        if limit is not None and executed >= limit:
            continue  # left pending; later completed batches are still loaded
        started = utc_now()
        results, requests = process(chunk)
        record = {
            "batch_index": index,
            "identity": batch_identity,
            "items": chunk,
            "results": results,
            "network_requests": requests,
            "started_at": started,
            "completed_at": utc_now(),
        }
        _atomic_json(path, record)  # persisted before the next batch starts
        records.append(record)
        executed += 1
    return {"records": records, "pending_batches": len(chunks) - len(records), "executed": executed}


# ---------------------------------------------------------------------------
# Advisor audit


def audit_advisors(ctx: CorpusContext, client: SourceClient | None = None, max_batches: int | None = None) -> dict:
    """Acquisition audit of every advisor PMID, at most ten per batch, in PMID order."""
    client = client or _client(ctx.loaded, ctx.literature)
    items = [
        [row.publication_id, str(row.pmid)]
        for row in ctx.advisors.sort_values("pmid", key=lambda s: s.astype(int)).itertuples()
    ]
    expected_doi = dict(zip(ctx.advisors["pmid"].astype(str), ctx.advisors["doi"], strict=True))

    def process(chunk):
        before = dict(client.network_requests)
        papers = acquire_batch(
            client,
            [(pid, pmid) for pid, pmid in chunk],
            ctx.papers_root,
            ctx.loaded.repo_root,
            ctx.corpus.supplement_max_bytes,
            ctx.corpus.supplement_extensions,
            fetch_supplements=True,
            pdf_alternates=set(),
            expected_dois=expected_doi,
        )
        after = client.network_requests
        return [p.to_json() for p in papers], {k: after.get(k, 0) - before.get(k, 0) for k in after}

    identity = {
        "route": "advisor_audit",
        "supplement_max_bytes": ctx.corpus.supplement_max_bytes,
        "supplement_extensions": ctx.corpus.supplement_extensions,
    }
    try:
        return run_batches(
            ctx.work_dir / "advisor_audit", items, ctx.corpus.audit_batch_size, identity, process, max_batches
        )
    finally:
        client.close()


def fetch_pdf_alternates(ctx: CorpusContext, audits: list[dict], client: SourceClient | None = None) -> dict:
    """OA article PDFs (non-canonical alternates) for a few advisor papers, to validate the PDF branch."""
    chosen = [
        a
        for a in sorted(audits, key=lambda a: int(a["pmid"]))
        if a["full_text_route"] and a["oa_dataset_status"] == "present" and (a["oa_metadata"] or {}).get("pdf_url")
    ][: ctx.corpus.pdf_validation_articles]
    client = client or _client(ctx.loaded, ctx.literature)
    from regkg.literature.acquire import _oa_file

    def process(chunk):
        results = []
        for pmid in chunk:
            audit = next(a for a in chosen if a["pmid"] == pmid)
            paper = PaperAcquisition(audit["publication_id"], pmid)
            _oa_file(
                client,
                paper,
                audit["oa_metadata"]["pdf_url"],
                "article.pdf",
                "pdf_alternate",
                ctx.papers_root,
                ctx.loaded.repo_root,
            )
            results.append({"pmid": pmid, "assets": paper.assets, "errors": paper.errors})
        return results, client.network_requests

    try:
        return run_batches(
            ctx.work_dir / "pdf_alternates", [a["pmid"] for a in chosen], 10, {"route": "pdf_alternates"}, process
        )
    finally:
        client.close()


# ---------------------------------------------------------------------------
# Coverage ledger and manual-download report


def acquisition_state(audit: dict | None, disposition: dict | None = None) -> tuple[str, str]:
    """(state, reason) from an audit record and an optional recorded user disposition."""
    if audit is None:
        return NOT_CHECKED, "batch not yet run"
    if audit["identity_issues"]:
        return IDENTITY_REVIEW_REQUIRED, "; ".join(audit["identity_issues"])
    if audit["full_text_route"] or any(a["role"] == "manual_article" for a in audit["assets"]):
        return FULL_TEXT_ACQUIRED, audit["full_text_route"] or "manual intake"
    if disposition and disposition.get("disposition") == "unavailable":
        return UNAVAILABLE_CONFIRMED, disposition.get("note") or "user disposition"
    if disposition and disposition.get("disposition") == "abstract_only":
        return ABSTRACT_ONLY, disposition.get("note") or "user disposition: abstract-only scope"
    if audit["pubmed_status"].startswith("failed") or audit["full_text_status"].startswith("failed"):
        return FETCH_FAILED, audit["full_text_status"] if audit["full_text_status"].startswith("failed") else audit[
            "pubmed_status"
        ]
    if audit["pubmed_status"] == "not_found":
        return IDENTITY_REVIEW_REQUIRED, "PubMed returned no record for this PMID"
    return MANUAL_DOWNLOAD_NEEDED, {
        "not_open_access": "not in the open-access subset",
        "no_pmcid": "no PMC copy; publisher access only",
        "open_access_unknown": "open-access status not reported",
        "not_served": "full text not served by the open-access API",
    }.get(audit["full_text_status"], audit["full_text_status"])


def access_status(audit: dict | None) -> str:
    if audit is None:
        return "not_checked"
    if audit["is_open_access"]:
        return "open_access"
    free = any((link.get("availability") or "").lower() == "free" for link in audit["links"])
    if free:
        return "free_to_read_not_open_access"
    if audit["in_pmc"]:
        return "in_pmc_not_open_access"
    return "publisher_or_unknown"


def download_need(roles: list[dict], signals: dict[str, dict]) -> tuple[str, str, str]:
    """(need_type, priority, reason). Manuscript-relevant primary evidence first; no lineage is favoured."""
    names = {r["role"] for r in roles}
    lineages = sorted(c for c, s in signals.items() if s["named_tfs"] or s["candidate_tfs"])
    if PRIMARY in names:
        if lineages:
            return (
                "required_for_extraction",
                "high",
                f"provisional primary evidence; candidate TFs for {', '.join(lineages)}",
            )
        return "required_for_extraction", "medium", "provisional primary evidence; no manuscript TF in title/abstract"
    if UNCERTAIN in names:
        return "resolve_screening_uncertainty", "medium", "role uncertain from title/abstract"
    return "optional_background", "low", "provisional background/resource/other-context role"


def _url(links: list[dict], kind: str) -> str | None:
    return next((link["url"] for link in links if link["kind"] == kind), None)


INBOX = "data/papers/manual_inbox"
DOWNLOAD_STATES = ("NEEDED", "RECEIVED", "IDENTITY_REVIEW_REQUIRED", "INGESTED")
ROUTES_CHECKED = {
    "pubmed_efetch": "PubMed record",
    "europepmc_core": "Europe PMC metadata and returned full-text links",
    "pmc_oa_dataset": "PMC Open Access dataset (AWS Open Data)",
    "europepmc_fulltextxml": "Europe PMC open-access JATS",
    "pubtator_biocjson": "PubTator BioC open-access text",
}


def _json(value) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)


def advisor_ledger(
    ctx: CorpusContext,
    audits: dict[str, dict],
    batches: dict[str, int],
    dispositions: dict[str, dict] | None = None,
    documents: dict[str, dict] | None = None,
    screening: dict[str, dict] | None = None,
    readiness: dict[str, dict] | None = None,
) -> pd.DataFrame:
    """One row per advisor PMID. Acquisition, parsing, screening, readiness, and extraction stay separate."""
    terms = lineage_terms(ctx)
    rows = []
    for advisor in ctx.advisors.sort_values("pmid", key=lambda s: s.astype(int)).itertuples(index=False):
        pmid = str(advisor.pmid)
        audit = audits.get(pmid)
        disposition = (dispositions or {}).get(pmid)
        state, state_reason = acquisition_state(audit, disposition)
        document = (documents or {}).get(pmid) or {}
        title = (audit or {}).get("title") or advisor.title
        abstract = (audit or {}).get("abstract") or ""
        roles = provisional_roles(title, abstract, (audit or {}).get("publication_types") or [], document.get("text"))
        signals = lineage_signals(f"{title} {abstract} {document.get('text') or ''}", terms)
        need, priority, priority_reason = download_need(roles, signals)
        screen = (screening or {}).get(pmid) or {"disposition": "NOT_SCREENED", "reason": "not yet parsed/screened"}
        ready = (readiness or {}).get(pmid) or _audit_readiness(state, state_reason, bool(document))
        links = (audit or {}).get("links") or []
        rows.append(
            {
                "publication_id": advisor.publication_id,
                "pmid": pmid,
                "pmcid": (audit or {}).get("pmcid"),
                "doi": (audit or {}).get("doi") or advisor.doi,
                "title": title,
                "year": (audit or {}).get("year") or advisor.year,
                "journal": (audit or {}).get("journal") or advisor.journal,
                "first_author": advisor.first_author,
                "advisor_lists": _json(list(advisor.resources)),
                "memberships": _json([dict(m) for m in advisor.memberships]),
                "metadata_conflict_fields": _json(list(advisor.metadata_conflict_fields)),
                "retracted": bool((audit or {}).get("retracted")),
                "corrections": _json((audit or {}).get("corrections") or []),
                "acquisition_batch": batches.get(pmid),
                "acquisition_priority": priority,
                "priority_reason": priority_reason,
                "download_need": need,
                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "pmc_url": _url(links, "pmc"),
                "doi_url": _url(links, "doi"),
                "returned_links": _json([link for link in links if link["kind"] == "returned_full_text"]),
                "access_status": access_status(audit),
                "license": (audit or {}).get("license"),
                "checked_sources": _json((audit or {}).get("checked_sources") or []),
                "checked_at": (audit or {}).get("checked_at"),
                "acquisition_state": state,
                "acquisition_reason": state_reason,
                "full_text_route": (audit or {}).get("full_text_route"),
                "oa_dataset_version": (audit or {}).get("oa_dataset_version"),
                "asset_ids": _json([a["sha256"] for a in (audit or {}).get("assets") or []]),
                "supplements_listed": len((audit or {}).get("supplements") or []),
                "supplements_acquired": sum(s["state"] == "acquired" for s in (audit or {}).get("supplements") or []),
                "parsing_state": document.get("parsing_state", "NOT_PARSED"),
                "parser": document.get("parser"),
                "canonical_document": document.get("document_id"),
                "coverage_components": _json(document.get("components") or {}),
                "missing_components": _json(document.get("missing") or _missing_before_parse(state)),
                "roles": _json(roles),
                "roles_review_status": "provisional_rule_based_pending_lead_review",
                "lineage_signals": _json(signals),
                "screening_disposition": screen["disposition"],
                "screening_reason": screen["reason"],
                "readiness_state": ready["state"],
                "readiness_reasons": _json(ready["reasons"]),
                "ready_bundle_ids": _json(ready.get("bundle_ids") or []),
                "extraction_status": "NOT_RUN",
                "extraction_run_ids": _json([]),
                "user_disposition": _json(disposition) if disposition else None,
            }
        )
    return pd.DataFrame(rows)


def _missing_before_parse(state: str) -> list[str]:
    return [] if state == FULL_TEXT_ACQUIRED else ["article_full_text"]


def _audit_readiness(state: str, reason: str, parsed: bool) -> dict:
    if state in {FULL_TEXT_ACQUIRED, ABSTRACT_ONLY}:
        return {"state": "NEEDS_SCREENING_REVIEW", "reasons": ["acquired; parsing/screening pending"]}
    if state in {IDENTITY_REVIEW_REQUIRED}:
        return {"state": "NEEDS_SCREENING_REVIEW", "reasons": [f"identity review: {reason}"]}
    return {"state": "NEEDS_ASSET", "reasons": [f"{state}: {reason}"]}


def asset_table(audits: dict[str, dict], intake: list[dict] | None = None) -> pd.DataFrame:
    rows = []
    for pmid, audit in sorted(audits.items(), key=lambda kv: int(kv[0])):
        for asset in audit["assets"]:
            rows.append(
                {
                    "pmid": pmid,
                    "publication_id": audit["publication_id"],
                    "parent": None,
                    "version": audit.get("oa_dataset_version"),
                    **asset,
                }
            )
        for item in audit.get("supplements") or []:
            if item.get("asset"):
                rows.append(
                    {
                        "pmid": pmid,
                        "publication_id": audit["publication_id"],
                        "parent": "article",
                        "version": audit.get("oa_dataset_version"),
                        **item["asset"],
                    }
                )
    for item in intake or []:
        rows.append(
            {"parent": "article" if item["role"] == "manual_supplement" else None, "version": "manual_intake", **item}
        )
    frame = pd.DataFrame(rows)
    if len(frame):
        frame["format"] = frame["name"].str.rsplit(".", n=1).str[-1].str.lower()
    return frame


def supplement_inventory(audits: dict[str, dict]) -> pd.DataFrame:
    rows = [
        {
            "pmid": pmid,
            "publication_id": a["publication_id"],
            **{k: v for k, v in s.items() if k != "asset"},
            "asset_sha256": (s.get("asset") or {}).get("sha256"),
        }
        for pmid, a in sorted(audits.items(), key=lambda kv: int(kv[0]))
        for s in a.get("supplements") or []
    ]
    return pd.DataFrame(
        rows,
        columns=[
            "pmid",
            "publication_id",
            "filename",
            "label",
            "jats_item_id",
            "size",
            "md5",
            "url",
            "state",
            "asset_sha256",
        ],
    )


def manual_downloads(ledger: pd.DataFrame, audits: dict[str, dict], intake_state: dict[str, dict]) -> pd.DataFrame:
    """One actionable row per needed asset, grouped by publication (NEEDED/RECEIVED/... states)."""
    rows = []
    for row in ledger.itertuples(index=False):
        audit = audits.get(row.pmid) or {}
        checked = [ROUTES_CHECKED[s] for s in json.loads(row.checked_sources) if s in ROUTES_CHECKED]
        base = {
            "publication_id": row.publication_id,
            "pmid": row.pmid,
            "doi": row.doi,
            "title": row.title,
            "year": row.year,
            "advisor_lists": row.advisor_lists,
            "priority": row.acquisition_priority,
            "priority_reason": row.priority_reason,
            "evidence_roles": ", ".join(sorted({r["role"] for r in json.loads(row.roles)})),
            "pubmed_url": row.pubmed_url,
            "pmc_url": row.pmc_url,
            "doi_url": row.doi_url,
            "routes_checked": "; ".join(checked),
            "last_checked": row.checked_at,
        }
        items = []
        if row.acquisition_state in {MANUAL_DOWNLOAD_NEEDED, IDENTITY_REVIEW_REQUIRED}:
            links = [link for link in json.loads(row.returned_links) if link.get("url")]
            items.append(
                {
                    "item": "article PDF",
                    "need_type": row.download_need,
                    "expected_filename": "article.pdf",
                    "discovered_links": _json(
                        [{k: link[k] for k in ("url", "availability", "document_style", "site")} for link in links]
                    ),
                    "why_user_action": row.acquisition_reason
                    if row.acquisition_state == MANUAL_DOWNLOAD_NEEDED
                    else f"identity review: {row.acquisition_reason}",
                }
            )
        for supplement in audit.get("supplements") or []:
            if supplement["state"] == "not_in_oa_dataset":
                items.append(
                    {
                        "item": f"supplement {supplement.get('label') or supplement['filename']}",
                        "need_type": "supplementary_context",
                        "expected_filename": f"supplement-{supplement['filename']}",
                        "discovered_links": _json([]),
                        "why_user_action": "listed by the article but absent from the open-access dataset",
                    }
                )
        for item in items:
            request_id = stable_id("download", {"pmid": row.pmid, "item": item["expected_filename"]})
            state = intake_state.get(request_id, {})
            rows.append(
                {
                    "request_id": request_id,
                    **base,
                    **item,
                    "inbox_destination": f"{INBOX}/{row.pmid}/{item['expected_filename']}",
                    "state": state.get("state", "NEEDED"),
                    "user_note": state.get("note"),
                    "local_asset_sha256": state.get("sha256"),
                }
            )
    columns = [
        "request_id",
        "publication_id",
        "pmid",
        "doi",
        "title",
        "year",
        "advisor_lists",
        "priority",
        "priority_reason",
        "evidence_roles",
        "item",
        "need_type",
        "expected_filename",
        "inbox_destination",
        "pubmed_url",
        "pmc_url",
        "doi_url",
        "discovered_links",
        "why_user_action",
        "routes_checked",
        "last_checked",
        "state",
        "user_note",
        "local_asset_sha256",
    ]
    order = {"high": 0, "medium": 1, "low": 2}
    frame = pd.DataFrame(rows, columns=columns)
    return frame.sort_values(
        ["priority", "pmid", "item"], key=lambda s: s.map(order) if s.name == "priority" else s, kind="mergesort"
    ).reset_index(drop=True)


def acquisition_failures(audits: dict[str, dict], parse_failures: list[dict] | None = None) -> pd.DataFrame:
    """System failures (timeouts, malformed responses, parse errors); never labelled paywalled.

    A failure later recovered through another route stays listed, with the route that recovered it.
    """
    rows = []
    for pmid, a in sorted(audits.items(), key=lambda kv: int(kv[0])):
        for error in a["errors"]:
            supplement = error.startswith("supplement ")
            recovered = None if supplement else a.get("full_text_route")
            rows.append(
                {
                    "pmid": pmid,
                    "publication_id": a["publication_id"],
                    "stage": "acquisition",
                    "detail": error,
                    "recovered_by": recovered,
                    "manual_fallback": None
                    if recovered
                    else "a user-supplied copy can substitute (fallback, not the diagnosed cause)",
                }
            )
    rows += parse_failures or []
    return pd.DataFrame(rows, columns=["pmid", "publication_id", "stage", "detail", "recovered_by", "manual_fallback"])


def _md_text(value) -> str:
    text = "" if value is None or (isinstance(value, float) and pd.isna(value)) else str(value)
    for ch in "\\|[]*_<>`#":
        text = text.replace(ch, "\\" + ch)
    return " ".join(text.split())


def _md_link(label: str, url) -> str:
    if not isinstance(url, str) or not url.startswith(("https://", "http://")):
        return ""
    return f"[{label}](<{url.replace('>', '%3E').replace(' ', '%20')}>)"


def downloads_markdown(key: str, downloads: pd.DataFrame, failures: pd.DataFrame, history: list[dict]) -> str:
    lines = [
        f"# Manual downloads — {key}",
        "",
        "Place files at the listed inbox path (a filename is a mapping hint, not identity proof), add a row to",
        f"`{INBOX}/intake.csv` (`pmid,filename,role,source_url,acquired_on,disposition,note`), then run",
        "`regkg literature intake`. DOI links are landing pages, not promises of a downloadable PDF.",
        "No login, proxy, or session URLs belong in the intake file.",
        "",
    ]
    sections = [
        ("Immediate downloads (manuscript extraction or screening)", downloads["priority"].isin(["high", "medium"])),
        ("Lower-priority background/reference material", downloads["priority"] == "low"),
    ]
    for heading, mask in sections:
        part = downloads[mask]
        lines += [f"## {heading} ({len(part)})", ""]
        for pmid, group in part.groupby("pmid", sort=False):
            first = group.iloc[0]
            links = " · ".join(
                filter(
                    None,
                    [
                        _md_link("PubMed", first.pubmed_url),
                        _md_link("PMC", first.pmc_url),
                        _md_link("DOI", first.doi_url),
                    ],
                )
            )
            lines.append(f"### PMID {pmid} ({_md_text(first.year)}) — {_md_text(first.title)}")
            lines.append(
                f"- Priority **{first.priority}**: {_md_text(first.priority_reason)}; provisional roles "
                f"{_md_text(first.evidence_roles)}; lists {_md_text(', '.join(json.loads(first.advisor_lists)))}"
            )
            lines.append(f"- Links: {links}")
            for item in group.itertuples(index=False):
                extra = " · ".join(
                    filter(
                        None,
                        [
                            _md_link(
                                f"{link.get('site')} {link.get('document_style')} ({link.get('availability')})",
                                link.get("url"),
                            )
                            for link in json.loads(item.discovered_links)
                        ],
                    )
                )
                lines.append(
                    f"- [{item.state}] {_md_text(item.item)} → `{item.inbox_destination}` — "
                    f"{_md_text(item.why_user_action)}; checked: {_md_text(item.routes_checked)}"
                    + (f"; returned links: {extra}" if extra else "")
                )
            lines.append("")
    lines += [f"## Acquisition failures ({len(failures)}) — system errors, not access restrictions", ""]
    for row in failures.itertuples(index=False):
        outcome = f"recovered by {row.recovered_by}" if isinstance(row.recovered_by, str) else row.manual_fallback
        lines.append(f"- PMID {row.pmid} [{row.stage}]: {_md_text(row.detail)} ({_md_text(outcome)})")
    if history:
        lines += ["", f"## Changes since the previous report ({len(history)})", ""]
        lines += [
            f"- {_md_text(h['request_id'])} PMID {h['pmid']}: {h['previous_state']} → {h['current_state']}"
            for h in history
        ]
    return "\n".join(lines) + "\n"


def report_history(ctx: CorpusContext, downloads: pd.DataFrame) -> tuple[str | None, list[dict]]:
    pointer = ctx.work_dir / "latest_report.json"
    if not pointer.is_file():
        return None, []
    previous_key = read_json(pointer)["key"]
    path = ctx.loaded.data_root / "processed" / previous_key / "manual_downloads.csv"
    if not path.is_file():
        return previous_key, []
    previous = pd.read_csv(path, dtype=str, keep_default_na=False)
    current = dict(zip(downloads["request_id"], downloads["state"], strict=True))
    history = []
    for row in previous.itertuples(index=False):
        now = current.get(row.request_id, "RESOLVED_NOT_NEEDED")
        if now != row.state:
            history.append(
                {
                    "request_id": row.request_id,
                    "pmid": row.pmid,
                    "previous_state": row.state,
                    "current_state": now,
                    "previous_report": previous_key,
                }
            )
    return previous_key, history


def publish_report(
    ctx: CorpusContext,
    kind: str,
    identity: dict,
    tables: dict[str, pd.DataFrame],
    documents: dict[str, Any],
    counts: dict,
) -> tuple[str, Path, str]:
    """Publish an immutable `litcorpus-*` artifact (or reuse an identical one) plus a reports/ copy."""
    identity = {
        **identity,
        "schema": CORPUS_SCHEMA,
        "kind": kind,
        "corpus_id": ctx.corpus_id,
        "code": code_fingerprint(Path(regkg.__file__).parent, CODE_PATHS),
    }
    key = f"litcorpus-{sha256_text(canonical_json(identity))[:16]}"
    final = ctx.loaded.data_root / "processed" / key
    status = "REUSED"
    if not final.exists():
        execution_id = new_execution_id("literature-corpus")
        staging = staging_directory(final, execution_id)
        try:
            rows = {}
            for name, frame in tables.items():
                if name.endswith(".parquet"):
                    frame.to_parquet(staging / name, index=False)
                else:
                    frame.to_csv(staging / name, index=False, quoting=csv.QUOTE_MINIMAL)
                rows[name] = len(frame)
            for name, value in documents.items():
                path = staging / name
                path.parent.mkdir(parents=True, exist_ok=True)
                if isinstance(value, str):
                    path.write_text(value, encoding="utf-8")
                else:
                    write_json(path, value)
            write_json(
                staging / "manifest.json",
                {
                    "stage": "literature_corpus",
                    "schema_version": CORPUS_SCHEMA,
                    "key": key,
                    "kind": kind,
                    "status": "SUCCEEDED",
                    "execution_id": execution_id,
                    "created_at": utc_now(),
                    "corpus_id": ctx.corpus_id,
                    "inputs": {"manuscript_key": ctx.manuscript_key, "advisor_seed_authority": BASELINE_CANDIDATES},
                    "identity": identity,
                    "counts": counts,
                    "code": {
                        "fingerprint": identity["code"],
                        "paths": CODE_PATHS,
                        "git": git_revision(ctx.loaded.repo_root),
                    },
                    "outputs": describe_outputs(staging, rows),
                },
            )
            publish_directory(staging, final)
            status = "SUCCEEDED"
        except BaseException:
            discard_directory(staging)
            raise
    # Convenience copies for reading; the checksummed originals stay in the artifact.
    reports = ctx.loaded.repo_root / "reports" / "literature" / key
    reports.mkdir(parents=True, exist_ok=True)
    for name in (
        "manual_downloads.md",
        "manual_downloads.csv",
        "advisor_coverage.csv",
        "extraction_readiness.md",
        "inference_budget.md",
        "coverage_report.md",
        "discovery_downloads.csv",
    ):
        if (final / name).is_file():
            (reports / name).write_bytes((final / name).read_bytes())
    _atomic_json(ctx.work_dir / "latest_report.json", {"key": key, "kind": kind, "at": utc_now()})
    return key, final, status


def _audits(result: dict) -> tuple[dict[str, dict], dict[str, int]]:
    audits, batches = {}, {}
    for record in result["records"]:
        for paper in record["results"]:
            audits[paper["pmid"]] = paper
            batches[paper["pmid"]] = record["batch_index"]
    return audits, batches


def intake_status(ctx: CorpusContext) -> tuple[dict[str, dict], dict[str, dict], list[dict]]:
    """(dispositions by PMID, download-request states, accepted intake assets) from the last intake run."""
    path = ctx.work_dir / "intake" / "state.json"
    if not path.is_file():
        return {}, {}, []
    state = read_json(path)
    return state.get("dispositions", {}), state.get("requests", {}), state.get("assets", [])


def run_corpus_audit(
    loaded: LoadedProjectConfig,
    manuscript_key: str,
    literature: Path,
    max_batches: int | None = None,
    client: SourceClient | None = None,
) -> dict:
    ctx = corpus_context(loaded, manuscript_key, literature)
    result = audit_advisors(ctx, client, max_batches)
    audits, batches = _audits(result)
    dispositions, request_states, intake_assets = intake_status(ctx)
    for asset in intake_assets:
        audits.get(asset["pmid"], {}).setdefault("assets", []).append(asset)
    ledger = advisor_ledger(ctx, audits, batches, dispositions)
    downloads = manual_downloads(ledger, audits, request_states)
    failures = acquisition_failures(audits)
    previous, history = report_history(ctx, downloads)
    requests: dict[str, int] = {}
    for record in result["records"][-result["executed"] :] if result["executed"] else []:
        for service, count in record["network_requests"].items():
            requests[service] = requests.get(service, 0) + count
    counts = {
        "advisor_pmids": ctx.reconciliation.unique_pmids,
        "advisor_memberships": ctx.reconciliation.memberships,
        "advisor_per_list": ctx.reconciliation.per_list,
        "advisor_in_several_lists": ctx.reconciliation.in_several_lists,
        "audit_batches_completed": len(result["records"]),
        "audit_batches_pending": result["pending_batches"],
        "audit_batches_executed_now": result["executed"],
        "acquisition_state": ledger["acquisition_state"].value_counts().to_dict(),
        "access_status": ledger["access_status"].value_counts().to_dict(),
        "full_text_route": ledger["full_text_route"].fillna("none").value_counts().to_dict(),
        "retracted": int(ledger["retracted"].sum()),
        "supplements_listed": int(ledger["supplements_listed"].sum()),
        "supplements_acquired": int(ledger["supplements_acquired"].sum()),
        "download_rows": len(downloads),
        "download_rows_by_priority": downloads["priority"].value_counts().to_dict(),
        "papers_awaiting_user_files": int(downloads.loc[downloads["state"] == "NEEDED", "pmid"].nunique()),
        "acquisition_failures": len(failures),
        "network_requests_this_execution": requests,
        "previous_report": previous,
    }
    identity = {
        "batches": [r["identity"] for r in result["records"]],
        "intake": sha256_text(canonical_json([dispositions, request_states, intake_assets])),
    }
    tables = {
        "advisor_coverage.parquet": ledger,
        "advisor_coverage.csv": ledger,
        "coverage_assets.parquet": asset_table(audits),
        "supplement_inventory.csv": supplement_inventory(audits),
        "manual_downloads.csv": downloads,
        "acquisition_failures.csv": failures,
    }
    documents = {
        "manual_downloads.md": downloads_markdown(ctx.corpus_id, downloads, failures, history),
        "reconciliation.json": ctx.reconciliation.__dict__,
        "coverage.json": counts,
        "history.json": history,
    }
    key, final, status = publish_report(ctx, "audit", identity, tables, documents, counts)
    return {"status": status, "key": key, "artifact": final, "corpus_id": ctx.corpus_id, "counts": counts}


# ---------------------------------------------------------------------------
# Discovery: the fixed manuscript queue, in schedule order, at most twenty queries per batch


PUNCTUATED_TERM = re.compile(r"[^\w\s-]")


def punctuation_probe(queue: pd.DataFrame, client: SourceClient) -> dict:
    """Check how each source handles punctuated queue phrases before bulk execution.

    Each punctuated phrase is compared with its word-only form. Equal counts mean the source reduces
    the punctuation to word tokens, so no adapter normalization is needed; any difference stops
    discovery until a versioned normalization is decided.
    """
    from regkg.literature.search import _pubmed_esearch_check

    phrases = sorted(
        {
            t
            for row in queue.itertuples(index=False)
            for t in json.loads(row.terms_json)["qualifiers"]
            if PUNCTUATED_TERM.search(t)
        }
    )
    results = []
    for phrase in phrases:
        words = " ".join(re.sub(r"[^\w]+", " ", phrase).split())
        entry = {"phrase": phrase, "word_form": words}
        for label, text in (("phrase", phrase), ("word_form", words)):
            pubmed = client.get(
                "pubmed",
                "esearch.fcgi",
                {"db": "pubmed", "term": f'"{text}"[tiab]', "retmax": "0", "retmode": "json"},
                validate=_pubmed_esearch_check,
            ).json()
            result = pubmed["esearchresult"]
            epmc = client.get(
                "europepmc",
                "search",
                {"query": f'"{text}"', "format": "json", "pageSize": "1", "resultType": "lite", "cursorMark": "*"},
                validate=_require_keys,
            ).json()
            entry[label] = {
                "pubmed_count": int(result["count"]),
                "pubmed_translation": result.get("querytranslation"),
                "pubmed_warnings": result.get("warninglist"),
                "europepmc_hits": int(epmc["hitCount"]),
            }
        entry["equivalent"] = all(
            entry["phrase"][k] == entry["word_form"][k] for k in ("pubmed_count", "europepmc_hits")
        )
        results.append(entry)
    return {
        "rule": "punctuation-probe-1",
        "phrases": results,
        "normalization": "none_required" if all(r["equivalent"] for r in results) else "required",
        "checked_at": utc_now(),
    }


def _require_keys(response) -> None:
    body = response.json()
    if "hitCount" not in body:
        raise ValueError("response lacks hitCount")


def run_discovery(ctx: CorpusContext, client: SourceClient | None = None, max_batches: int | None = None) -> dict:
    from regkg.literature.search import QuerySpec, search_papers

    client = client or _client(ctx.loaded, ctx.literature)
    try:
        probe = punctuation_probe(ctx.queue, client)
        _atomic_json(ctx.work_dir / "discovery" / "punctuation_probe.json", probe)
        if probe["normalization"] != "none_required":
            raise CorpusError(
                "punctuated query phrases differ from their word forms; decide a versioned "
                f"normalization before discovery: {ctx.work_dir / 'discovery' / 'punctuation_probe.json'}"
            )
        queue = ctx.queue.sort_values("schedule_position")
        items = queue["query_id"].tolist()
        by_id = queue.set_index("query_id")

        def process(chunk):
            before = dict(client.network_requests)
            results = []
            for query_id in chunk:
                row = by_id.loc[query_id]
                result = search_papers(
                    QuerySpec.from_queue_row(query_id, row["terms_json"]),
                    client,
                    ctx.literature.search.sources,
                    ctx.literature.search.max_results_per_query,
                )
                results.append(result.to_json())
            after = client.network_requests
            return results, {k: after.get(k, 0) - before.get(k, 0) for k in after}

        identity = {
            "route": "manuscript_discovery",
            "sources": ctx.literature.search.sources,
            "max_results": ctx.literature.search.max_results_per_query,
        }
        result = run_batches(
            ctx.work_dir / "discovery", items, ctx.corpus.discovery_batch_size, identity, process, max_batches
        )
        result["probe"] = probe
        return result
    finally:
        client.close()


def discovery_counts(result: dict) -> dict:
    statuses: dict[str, int] = {}
    requests: dict[str, int] = {}
    for record in result["records"]:
        for item in record["results"]:
            statuses[item["status"]] = statuses.get(item["status"], 0) + 1
    for record in result["records"][-result["executed"] :] if result["executed"] else []:
        for service, count in record["network_requests"].items():
            requests[service] = requests.get(service, 0) + count
    return {
        "batches_completed": len(result["records"]),
        "batches_pending": result["pending_batches"],
        "batches_executed_now": result["executed"],
        "queries_executed": sum(len(r["items"]) for r in result["records"]),
        "query_status": statuses,
        "punctuation_normalization": result["probe"]["normalization"],
        "network_requests_this_execution": requests,
    }


def run_corpus_discovery(
    loaded: LoadedProjectConfig,
    manuscript_key: str,
    literature: Path,
    max_batches: int | None = None,
    client: SourceClient | None = None,
) -> dict:
    ctx = corpus_context(loaded, manuscript_key, literature)
    result = run_discovery(ctx, client, max_batches)
    return {
        "status": "SUCCEEDED" if not result["pending_batches"] else "PARTIAL",
        "key": "(workspace batches)",
        "artifact": ctx.work_dir / "discovery",
        "corpus_id": ctx.corpus_id,
        "counts": discovery_counts(result),
    }


def discovery_publications(ctx: CorpusContext, result: dict, audits: dict[str, dict]) -> tuple[pd.DataFrame, list]:
    """Unify discovery hits (and advisor PMIDs) into publications with lineage associations.

    A lineage association is eligible for acquisition when a query of that lineage retrieved the
    paper and its title/abstract names that query's TF exactly. Discovery never displaces advisor
    papers: an advisor PMID keeps its advisor route whether or not a query also found it.
    """
    from regkg.literature.publications import any_term, resolve_publications
    from regkg.literature.search import SourceRecord

    queue = ctx.queue.set_index("query_id")
    labelled = []
    for record in result["records"]:
        for item in record["results"]:
            labelled += [(item["query_id"], SourceRecord(**r)) for r in item["records"]]
    publications = resolve_publications(labelled)
    advisor_pmids = set(ctx.advisors["pmid"].astype(str))
    rows = []
    for publication in publications:
        title, abstract = publication.best("title") or "", publication.best("abstract") or ""
        text = f"{title} {abstract}"
        associations: dict[str, dict] = {}
        for query_id in sorted({label for label, _ in publication.records}):
            row = queue.loc[query_id]
            names = json.loads(row["terms_json"])["tf"]
            entry = associations.setdefault(row["cell_type"], {"queries": [], "tfs_named": set(), "context_terms": []})
            entry["queries"].append(query_id)
            if any_term(text, names):
                entry["tfs_named"].add(row["tf_hgnc_id"])
        lineage_context = {x.cell_type: x.context_terms for x in ctx.scope.lineages}
        for cell_type, entry in associations.items():
            entry["tfs_named"] = sorted(entry["tfs_named"])
            entry["context_terms"] = sorted(t for t in lineage_context[cell_type] if any_term(text, [t], False))
            entry["eligible"] = bool(entry["tfs_named"]) and not publication.retracted
        pmid = publication.identifiers.get("pmid")
        rows.append(
            {
                "publication_id": publication.publication_id,
                "pmid": pmid,
                "pmcid": publication.identifiers.get("pmcid"),
                "doi": publication.identifiers.get("doi"),
                "title": title,
                "year": publication.best("year"),
                "retracted": publication.retracted,
                "is_preprint": publication.is_preprint,
                "advisor": pmid in advisor_pmids,
                "lineage_associations": associations,
                "eligible_lineages": sorted(c for c, e in associations.items() if e["eligible"]),
                "query_hits": len({label for label, _ in publication.records}),
            }
        )
    return pd.DataFrame(rows), publications


def discovery_acquisition_order(ctx: CorpusContext, discovered: pd.DataFrame) -> list[tuple[str, str]]:
    """Eligible non-advisor papers with a PMID, interleaved across lineages with a rotating start.

    Tier 1 (acquired): an eligible association whose lineage context phrase also appears in the
    title/abstract. Within a lineage: more named TFs, more query hits, then PMID. A paper eligible
    for several lineages is queued once, at its earliest position.
    """
    per_lineage: dict[str, list] = {}
    for row in discovered.itertuples(index=False):
        if row.advisor or not isinstance(row.pmid, str):
            continue
        for cell_type in row.eligible_lineages:
            entry = row.lineage_associations[cell_type]
            if not entry["context_terms"]:
                continue  # tier 2: TF named without lineage context in title/abstract; deferred, listed
            key = (-int(bool(entry["context_terms"])), -len(entry["tfs_named"]), -row.query_hits, int(row.pmid))
            per_lineage.setdefault(cell_type, []).append((key, row.publication_id, row.pmid))
    lineages = sorted(per_lineage)
    pending = {c: [(p, m) for _, p, m in sorted(per_lineage[c])] for c in lineages}
    order, seen, round_index = [], set(), 0
    while any(pending.values()):
        start = round_index % len(lineages)
        for cell_type in lineages[start:] + lineages[:start]:
            while pending[cell_type]:
                pid, pmid = pending[cell_type].pop(0)
                if pid not in seen:
                    seen.add(pid)
                    order.append((pid, pmid))
                    break
        round_index += 1
    return order


def discovery_state(ctx: CorpusContext) -> tuple[dict, pd.DataFrame, list[tuple[str, str]]]:
    queue = ctx.queue.sort_values("schedule_position")["query_id"].tolist()
    identity = {
        "route": "manuscript_discovery",
        "sources": ctx.literature.search.sources,
        "max_results": ctx.literature.search.max_results_per_query,
    }
    result = run_batches(ctx.work_dir / "discovery", queue, ctx.corpus.discovery_batch_size, identity, None, limit=0)
    # A bounded retry of a partial/failed search is stored separately; completed batch records stay as written.
    retries_path = ctx.work_dir / "discovery" / "retries.json"
    retries = read_json(retries_path) if retries_path.is_file() else {}
    for record in result["records"]:
        record["results"] = [
            retries[r["query_id"]]["result"]
            if r["query_id"] in retries and retries[r["query_id"]]["result"]["status"] in {"success", "empty"}
            else r
            for r in record["results"]
        ]
    result["retries"] = retries
    probe_path = ctx.work_dir / "discovery" / "punctuation_probe.json"
    result["probe"] = read_json(probe_path) if probe_path.is_file() else {"normalization": "not_checked"}
    discovered, _ = discovery_publications(ctx, result, {})
    return result, discovered, discovery_acquisition_order(ctx, discovered)


def acquire_discovery(
    ctx: CorpusContext, order: list[tuple[str, str]], client: SourceClient | None = None, max_batches: int | None = None
) -> dict:
    """OA full text for tier-1 discovery papers; supplements are inventoried, not downloaded."""
    client = client or _client(ctx.loaded, ctx.literature)

    def process(chunk):
        before = dict(client.network_requests)
        papers = acquire_batch(
            client,
            [(pid, pmid) for pid, pmid in chunk],
            ctx.papers_root,
            ctx.loaded.repo_root,
            ctx.corpus.supplement_max_bytes,
            ctx.corpus.supplement_extensions,
            fetch_supplements=False,
            pdf_alternates=set(),
        )
        after = client.network_requests
        return [p.to_json() for p in papers], {k: after.get(k, 0) - before.get(k, 0) for k in after}

    try:
        return run_batches(
            ctx.work_dir / "discovery_acquisition",
            [list(x) for x in order],
            ctx.corpus.acquisition_batch_size,
            {"route": "discovery_acquisition"},
            process,
            max_batches,
        )
    finally:
        client.close()


def retry_incomplete_searches(ctx: CorpusContext, client: SourceClient | None = None) -> dict:
    """Retry each partial/failed discovery query once through the existing bounded client (cached successes reused)."""
    from regkg.literature.search import QuerySpec, search_papers

    result = run_batches(
        ctx.work_dir / "discovery",
        ctx.queue.sort_values("schedule_position")["query_id"].tolist(),
        ctx.corpus.discovery_batch_size,
        {
            "route": "manuscript_discovery",
            "sources": ctx.literature.search.sources,
            "max_results": ctx.literature.search.max_results_per_query,
        },
        None,
        limit=0,
    )
    path = ctx.work_dir / "discovery" / "retries.json"
    retries = read_json(path) if path.is_file() else {}
    pending = [
        r
        for b in result["records"]
        for r in b["results"]
        if r["status"] in {"partial", "failed"} and r["query_id"] not in retries
    ]
    if not pending:
        return retries
    client = client or _client(ctx.loaded, ctx.literature)
    by_id = ctx.queue.set_index("query_id")
    try:
        for original in pending:
            retried = search_papers(
                QuerySpec.from_queue_row(original["query_id"], by_id.loc[original["query_id"], "terms_json"]),
                client,
                ctx.literature.search.sources,
                ctx.literature.search.max_results_per_query,
            )
            retries[original["query_id"]] = {
                "at": utc_now(),
                "original_status": original["status"],
                "original_outcomes": original["outcomes"],
                "result": retried.to_json(),
                "network_requests": dict(client.network_requests),
            }
    finally:
        client.close()
    _atomic_json(path, retries)
    return retries


def acquire_needed_supplements(ctx: CorpusContext, needs: list[dict], client: SourceClient | None = None) -> dict:
    """Download only supplements required by candidate evidence (open-access dataset copies, MD5-checked).

    `needs` items: pmid, publication_id, filename, url, md5, size. The existing size bound applies;
    larger files stay deferred with their link. Resumable in batches of ten files.
    """
    from regkg.literature.acquire import _md5_check
    from regkg.literature.fetch import store_asset
    from regkg.literature.http import SourceError

    client = client or _client(ctx.loaded, ctx.literature)
    # Named per-file allowances only; the global supplement limit still applies to everything else.
    exceptions = {(x.pmid, x.filename): x for x in ctx.corpus.supplement_size_exceptions}

    def process(chunk):
        before = dict(client.network_requests)
        results = []
        for need in chunk:
            entry = {**need, "state": "", "asset": None, "error": None}
            exception = exceptions.get((str(need["pmid"]), need["filename"]))
            allowance = exception.max_bytes if exception else ctx.corpus.supplement_max_bytes
            entry["size_allowance_bytes"] = allowance
            entry["size_exception"] = exception.reason if exception else None
            if not need.get("url"):
                entry["state"] = "missing_asset"
            elif (need.get("size") or 0) > allowance:
                entry["state"] = "deferred_size_limit"
            else:
                key = need["url"].removeprefix("https://pmc-oa-opendata.s3.amazonaws.com/")
                try:
                    response = client.get("pmc_oa", key, {}, validate=_md5_check(need.get("md5")))
                    asset = store_asset(
                        ctx.papers_root,
                        need["publication_id"],
                        f"supplement-{need['filename']}",
                        "supplement",
                        response.body,
                        response.cache_key,
                        need["url"],
                        ctx.loaded.repo_root,
                    )
                    entry.update(state="acquired", asset=asdict(asset))
                except SourceError as error:
                    entry.update(state=f"fetch_failed:{error.kind}", error=str(error))
            results.append(entry)
        after = client.network_requests
        return results, {k: after.get(k, 0) - before.get(k, 0) for k in after}

    items = sorted(needs, key=lambda n: (int(n["pmid"]), n["filename"]))
    identity = {
        "route": "needed_supplements",
        "size_exceptions": sorted(f"{x.pmid}/{x.filename}:{x.max_bytes}" for x in exceptions.values()),
    }
    try:
        return run_batches(ctx.work_dir / "needed_supplements", items, 10, identity, process)
    finally:
        client.close()


# ---------------------------------------------------------------------------
# Supplemental synonym queries: a separate, versioned queue; the accepted P2 queue is never changed

SYNONYM_QUERY_RULE = "p3-synonym-queries-1"
SUPPLEMENTAL_ACQUISITION_CAP = 20  # tier-1 papers acquired from this follow-up; the rest stay listed


def synonym_queue(gaps: dict) -> list[dict]:
    """The proposed ontology-gap queries as queue rows with stable IDs and exact terms."""
    rows = []
    for query in gaps["queries"]:
        terms = {"tf": query["tf_terms"], "target": [], "qualifiers": query["context_phrases"]}
        rows.append(
            {
                "query_id": f"syn-{query['cell_type']}-{query['tf_hgnc_id']}",
                "rule": SYNONYM_QUERY_RULE,
                "cell_type": query["cell_type"],
                "tf_hgnc_id": query["tf_hgnc_id"],
                "terms_json": canonical_json(terms),
                "phrase_ontology_ids": query["phrase_ontology_ids"],
            }
        )
    return rows


def _synonym_identity(
    ctx: CorpusContext, queue: list[dict], route: str = "supplemental_synonym_discovery", rule: str = SYNONYM_QUERY_RULE
) -> dict:
    return {
        "route": route,
        "rule": rule,
        "queue_sha256": sha256_text(canonical_json(queue)),
        "sources": ctx.literature.search.sources,
        "max_results": ctx.literature.search.max_results_per_query,
    }


def synonym_search(
    ctx: CorpusContext,
    queue: list[dict],
    client: SourceClient | None = None,
    execute: bool = False,
    directory_name: str = "supplemental_discovery",
    rule: str = SYNONYM_QUERY_RULE,
    route: str = "supplemental_synonym_discovery",
) -> dict:
    """Run (execute=True) or reload a bounded queue in batches of the discovery batch size."""
    from regkg.literature.search import QuerySpec, search_papers

    by_id = {q["query_id"]: q for q in queue}
    directory = ctx.work_dir / directory_name
    identity = _synonym_identity(ctx, queue, route, rule)
    _atomic_json(directory / "queue.json", {"rule": rule, "queries": queue})
    if not execute:
        return run_batches(directory, list(by_id), ctx.corpus.discovery_batch_size, identity, None, limit=0)
    client = client or _client(ctx.loaded, ctx.literature)

    def process(chunk):
        before = dict(client.network_requests)
        results = [
            search_papers(
                QuerySpec.from_queue_row(query_id, by_id[query_id]["terms_json"]),
                client,
                ctx.literature.search.sources,
                ctx.literature.search.max_results_per_query,
            ).to_json()
            for query_id in chunk
        ]
        after = client.network_requests
        return results, {k: after.get(k, 0) - before.get(k, 0) for k in after}

    try:
        return run_batches(directory, list(by_id), ctx.corpus.discovery_batch_size, identity, process)
    finally:
        client.close()


def synonym_publications(
    ctx: CorpusContext,
    queue: list[dict],
    result: dict,
    p2_discovered: pd.DataFrame,
    cap: int = SUPPLEMENTAL_ACQUISITION_CAP,
) -> tuple[pd.DataFrame, list[tuple[str, str]]]:
    """Supplemental hits with their overlap against P2 discovery and the advisor list, and the bounded
    tier-1 acquisition order for new papers.

    Tier 1 uses the P2 rule with the query's synonym phrases as extra context terms: the title/abstract
    names the query's TF exactly and a lineage context phrase. Overlapping papers keep their P2 route.
    """
    from regkg.literature.publications import any_term, resolve_publications
    from regkg.literature.search import SourceRecord

    by_id = {q["query_id"]: q for q in queue}
    labelled = [
        (item["query_id"], SourceRecord(**x))
        for rec in result["records"]
        for item in rec["results"]
        for x in item["records"]
    ]
    p2_ids = set(p2_discovered["publication_id"])
    p2_pmids = {p for p in p2_discovered["pmid"] if isinstance(p, str)}
    advisor_pmids = set(ctx.advisors["pmid"].astype(str))
    lineage_context = {x.cell_type: x.context_terms for x in ctx.scope.lineages}
    rows, candidates = [], []
    for publication in resolve_publications(labelled):
        title, abstract = publication.best("title") or "", publication.best("abstract") or ""
        text = f"{title} {abstract}"
        pmid = publication.identifiers.get("pmid")
        associations: dict[str, dict] = {}
        for query_id in sorted({label for label, _ in publication.records}):
            query = by_id[query_id]
            terms = json.loads(query["terms_json"])
            entry = associations.setdefault(
                query["cell_type"], {"queries": [], "tfs_named": set(), "context_terms": set()}
            )
            entry["queries"].append(query_id)
            if any_term(text, terms["tf"]):
                entry["tfs_named"].add(query["tf_hgnc_id"])
            context = list(terms["qualifiers"]) + list(lineage_context[query["cell_type"]])
            entry["context_terms"] |= {t for t in context if any_term(text, [t], False)}
        for entry in associations.values():
            entry["tfs_named"], entry["context_terms"] = sorted(entry["tfs_named"]), sorted(entry["context_terms"])
            entry["eligible"] = bool(entry["tfs_named"]) and not publication.retracted
        if pmid in advisor_pmids:
            overlap = "advisor"
        elif publication.publication_id in p2_ids or pmid in p2_pmids:
            overlap = "p2_discovery"
        else:
            overlap = "new"
        tier1 = sorted(c for c, e in associations.items() if e["eligible"] and e["context_terms"])
        if overlap != "new":
            tier = f"already_in_{overlap}"
        elif tier1 and pmid:
            tier = "tier1_candidate"
            key = (-max(len(associations[c]["tfs_named"]) for c in tier1), -len(publication.records), int(pmid))
            candidates.append((key, publication.publication_id, pmid))
        elif any(e["eligible"] for e in associations.values()):
            tier = "tier2_deferred_no_lineage_context_in_title_abstract" if pmid else "deferred_no_pmid"
        else:
            tier = "metadata_only_no_exact_tf_in_title_abstract"
        rows.append(
            {
                "publication_id": publication.publication_id,
                "pmid": pmid,
                "pmcid": publication.identifiers.get("pmcid"),
                "doi": publication.identifiers.get("doi"),
                "title": title,
                "year": publication.best("year"),
                "retracted": publication.retracted,
                "is_preprint": publication.is_preprint,
                "advisor": overlap == "advisor",
                "overlap": overlap,
                "tier": tier,
                "lineage_associations": associations,
                "eligible_lineages": tier1,
                "query_hits": len({label for label, _ in publication.records}),
            }
        )
    frame = pd.DataFrame(rows)
    order = [(pid, pmid) for _, pid, pmid in sorted(candidates)][:cap]
    chosen = {pid for pid, _ in order}
    if len(frame):
        frame.loc[(frame["tier"] == "tier1_candidate") & frame["publication_id"].isin(chosen), "tier"] = (
            "tier1_acquired"
        )
        frame.loc[frame["tier"] == "tier1_candidate", "tier"] = "tier1_deferred_supplemental_cap"
    return frame, order


def synonym_acquisition(
    ctx: CorpusContext,
    order: list[tuple[str, str]],
    client: SourceClient | None = None,
    execute: bool = False,
    directory_name: str = "supplemental_acquisition",
    rule: str = SYNONYM_QUERY_RULE,
) -> dict:
    """OA full text for a bounded tier-1 order (supplements inventoried, not downloaded)."""
    directory = ctx.work_dir / directory_name
    identity = {"route": directory_name, "rule": rule}
    items = [list(x) for x in order]
    if not execute:
        return run_batches(directory, items, ctx.corpus.acquisition_batch_size, identity, None, limit=0)
    client = client or _client(ctx.loaded, ctx.literature)

    def process(chunk):
        before = dict(client.network_requests)
        papers = acquire_batch(
            client,
            [(pid, pmid) for pid, pmid in chunk],
            ctx.papers_root,
            ctx.loaded.repo_root,
            ctx.corpus.supplement_max_bytes,
            ctx.corpus.supplement_extensions,
            fetch_supplements=False,
            pdf_alternates=set(),
        )
        after = client.network_requests
        return [p.to_json() for p in papers], {k: after.get(k, 0) - before.get(k, 0) for k in after}

    try:
        return run_batches(directory, items, ctx.corpus.acquisition_batch_size, identity, process)
    finally:
        client.close()


def synonym_report(
    queue: list[dict],
    result: dict,
    frame: pd.DataFrame,
    acquisition: dict,
    rule: str = SYNONYM_QUERY_RULE,
    cap: int = SUPPLEMENTAL_ACQUISITION_CAP,
) -> dict:
    """Exact terms, source translations, per-query results, overlap, and incremental yield."""
    results = {item["query_id"]: item for rec in result["records"] for item in rec["results"]}
    queries = []
    for query in queue:
        item = results.get(query["query_id"])
        found = (
            frame[
                frame["lineage_associations"].map(
                    lambda a, q=query["query_id"]: any(q in e["queries"] for e in a.values())
                )
            ]
            if len(frame)
            else frame
        )
        queries.append(
            {
                **query,
                "search_status": item["status"] if item else "NOT_SEARCHED",
                "translations": item["translations"] if item else None,
                "outcomes": item["outcomes"] if item else None,
                "publications": int(len(found)),
                "overlap": found["overlap"].value_counts().to_dict() if len(found) else {},
                "new_tier1": int(found["tier"].isin(["tier1_acquired", "tier1_deferred_supplemental_cap"]).sum())
                if len(found)
                else 0,
            }
        )
    acquired = [p for b in acquisition["records"] for p in b["results"]]
    return {
        "rule": rule,
        "status": "executed" if len(results) == len(queue) else ("partial" if results else "not_executed"),
        "p2_queue_modified": False,
        "queries": queries,
        "publications": int(len(frame)),
        "overlap": frame["overlap"].value_counts().to_dict() if len(frame) else {},
        "tiers": frame["tier"].value_counts().to_dict() if len(frame) else {},
        "acquisition": {
            "cap": cap,
            "attempted": len(acquired),
            # full text fetched, by the acquisition's own status (asset roles are route-specific)
            "with_full_text": sum(1 for p in acquired if p.get("full_text_status") == "fetched"),
            "without_full_text": sorted(
                {f"{p['pmid']}:{p.get('full_text_status')}" for p in acquired if p.get("full_text_status") != "fetched"}
            ),
            "pending_batches": acquisition["pending_batches"],
        },
        "caveat": "Lexical non-coverage of a phrase is not a retrieval gap; overlap with P2 discovery measures it.",
    }


def run_synonym_discovery(
    loaded: LoadedProjectConfig, manuscript_key: str, literature: Path, max_batches: int | None = None
) -> dict:
    """Execute the supplemental synonym queue, then acquire the bounded tier-1 set (live network)."""
    from regkg.literature.ontology import build_context, query_synonym_gaps
    from regkg.workflows.corpus_prepare import _names

    ctx = corpus_context(loaded, manuscript_key, literature)
    ontology = build_context(loaded.repo_root / "configs" / "ontology_scope.yaml", loaded.data_root / "external")
    queue = synonym_queue(query_synonym_gaps(ontology, lineage_terms(ctx), _names(ctx.queue)))
    result = synonym_search(ctx, queue, execute=True)
    if result["pending_batches"]:
        raise CorpusError("supplemental synonym searches incomplete; rerun to resume")
    _, p2_discovered, _ = discovery_state(ctx)
    frame, order = synonym_publications(ctx, queue, result, p2_discovered)
    acquisition = synonym_acquisition(ctx, order, execute=True)
    report = synonym_report(queue, result, frame, acquisition)
    _atomic_json(ctx.work_dir / "supplemental_discovery" / "report.json", report)
    return {
        "status": "SUCCEEDED" if not acquisition["pending_batches"] else "PARTIAL",
        "key": "(workspace batches)",
        "artifact": ctx.work_dir / "supplemental_discovery",
        "corpus_id": ctx.corpus_id,
        "counts": {k: report[k] for k in ("publications", "overlap", "tiers", "acquisition")},
    }


# ---------------------------------------------------------------------------
# Gap-directed queue: the lineages whose exact populations have no corpus evidence


GAP_QUERY_RULE = "p3-gap-queries-1"


def gap_queue(path: Path) -> tuple[list[dict], dict]:
    """The curated gap queue as queue rows (the accepted P2 queue is never touched)."""
    import yaml

    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if document["rule"] != GAP_QUERY_RULE:
        raise CorpusError(f"{path}: expected rule {GAP_QUERY_RULE}, found {document['rule']}")
    if len(document["queries"]) > 10:
        raise CorpusError(f"{path}: {len(document['queries'])} queries exceeds the authorized bound of 10")
    rows = [
        {
            "query_id": query["query_id"],
            "rule": GAP_QUERY_RULE,
            "cell_type": query["cell_type"],
            "tf_hgnc_id": query["tf_hgnc_id"],
            "terms_json": canonical_json(
                {
                    "tf": query["terms"]["tf"],
                    "target": query["terms"].get("target") or [],
                    "qualifiers": query["terms"]["qualifiers"],
                }
            ),
        }
        for query in document["queries"]
    ]
    return rows, document


def acquired_pmids(ctx: CorpusContext, directory_name: str) -> set[str]:
    """PMIDs already acquired through a completed batch directory (read directly, order-independent)."""
    directory = ctx.work_dir / directory_name
    return {
        paper["pmid"]
        for path in sorted(directory.glob("batch-*.json"))
        for paper in read_json(path)["results"]
        if paper.get("pmid")
    }


def gap_state(ctx: CorpusContext, p2_discovered: pd.DataFrame, queue_path: Path, execute: bool = False) -> dict:
    """The bounded gap queue, its results, overlap and (at most `acquisition_cap`) new acquisitions."""
    queue, document = gap_queue(queue_path)
    result = synonym_search(
        ctx, queue, execute=execute, directory_name="gap_discovery", rule=GAP_QUERY_RULE, route="gap_discovery"
    )
    cap = int(document.get("acquisition_cap", SUPPLEMENTAL_ACQUISITION_CAP))
    frame, order = synonym_publications(ctx, queue, result, p2_discovered, cap)
    # A paper already acquired by the earlier supplemental queue is neither re-acquired nor counted as new.
    prior = acquired_pmids(ctx, "supplemental_acquisition")
    order = [(pid, pmid) for pid, pmid in order if pmid not in prior]
    acquisition = synonym_acquisition(
        ctx, order, execute=execute, directory_name="gap_acquisition", rule=GAP_QUERY_RULE
    )
    report = synonym_report(queue, result, frame, acquisition, GAP_QUERY_RULE, cap)
    report["queue_path"] = queue_path.name
    report["queue_sha256"] = sha256_file(queue_path)
    report["already_acquired_by_supplemental_queue"] = sorted(prior & set(frame["pmid"].dropna())) if len(frame) else []
    report["interpretation"] = (
        "No hit means no retrievable literature support in these sources for that exact population and "
        "regulator, not biological absence. Every manuscript case stays in the final reporting."
    )
    report["source_bound"] = (
        f"at most {ctx.literature.search.max_results_per_query} records per source per query; "
        "hit_count in each outcome shows what was available"
    )
    return {
        "queue": queue,
        "result": result,
        "frame": frame,
        "order": order,
        "acquisition": acquisition,
        "report": report,
    }


def run_gap_discovery(
    loaded: LoadedProjectConfig, manuscript_key: str, literature: Path, queue_path: Path | None = None
) -> dict:
    """Execute the bounded gap queue, then acquire at most the authorized number of new tier-1 papers."""
    ctx = corpus_context(loaded, manuscript_key, literature)
    queue_path = queue_path or loaded.repo_root / "configs" / "p3_gap_queries.yaml"
    _, p2_discovered, _ = discovery_state(ctx)
    state = gap_state(ctx, p2_discovered, queue_path, execute=True)
    if state["result"]["pending_batches"]:
        raise CorpusError("gap-directed searches incomplete; rerun to resume")
    _atomic_json(ctx.work_dir / "gap_discovery" / "report.json", state["report"])
    return {
        "status": "SUCCEEDED" if not state["acquisition"]["pending_batches"] else "PARTIAL",
        "key": "(workspace batches)",
        "artifact": ctx.work_dir / "gap_discovery",
        "corpus_id": ctx.corpus_id,
        "counts": {k: state["report"][k] for k in ("publications", "overlap", "tiers", "acquisition")},
    }


# ---------------------------------------------------------------------------
# Bounded primary full-text retry for papers whose fetched JATS has no body


FULL_TEXT_RETRY_RULE = "p3-full-text-retry-1"


def _has_body(content: bytes) -> bool:
    """A JATS record with an empty or missing <body> is not usable full text."""
    body = content.split(b"<body", 1)
    return len(body) > 1 and len(body[1].split(b"</body>", 1)[0]) > 2000


def retry_full_text(
    ctx: CorpusContext, targets: list[dict], client: SourceClient | None = None, execute: bool = False
) -> dict:
    """Re-fetch full text for named PMIDs through the PMC OA dataset copy, which the first pass skips
    whenever Europe PMC answered at all. One attempt per paper per run; resumable and bounded."""
    from regkg.literature.acquire import _md5_check, _md5_of, oa_dataset
    from regkg.literature.fetch import store_asset
    from regkg.literature.http import SourceError

    directory = ctx.work_dir / "full_text_retry"
    items = sorted(targets, key=lambda t: int(t["pmid"]))
    identity = {"route": "full_text_retry", "rule": FULL_TEXT_RETRY_RULE}
    if not execute:
        return run_batches(directory, items, 10, identity, None, limit=0)
    client = client or _client(ctx.loaded, ctx.literature)

    def process(chunk):
        before = dict(client.network_requests)
        results = []
        for target in chunk:
            entry = {**target, "attempts": [], "state": "", "asset": None}
            try:
                version, metadata, _ = oa_dataset(client, target["pmcid"])
                url = (metadata or {}).get("xml_url")
                entry["oa_dataset_version"] = version
                if not url:
                    entry["state"] = "no_oa_dataset_xml"
                else:
                    key = url.removeprefix("s3://pmc-oa-opendata/").split("?")[0]
                    response = client.get("pmc_oa", key, {}, validate=_md5_check(_md5_of(url)))
                    usable = _has_body(response.body)
                    entry["attempts"].append(
                        {"source": "pmc_oa_dataset_jats", "bytes": len(response.body), "usable_body": usable}
                    )
                    if usable:
                        asset = store_asset(
                            ctx.papers_root,
                            target["publication_id"],
                            "fulltext_pmc_oa.xml",
                            "jats_full_text",
                            response.body,
                            response.cache_key,
                            f"https://pmc-oa-opendata.s3.amazonaws.com/{key}",
                            ctx.loaded.repo_root,
                        )
                        entry.update(state="full_text_recovered", asset=asdict(asset))
                    else:
                        entry["state"] = "no_usable_body_in_any_authorized_route"
            except SourceError as error:
                entry["state"] = f"fetch_failed:{error.kind}"
                entry["attempts"].append({"source": "pmc_oa_dataset_jats", "error": str(error)})
            results.append(entry)
        after = client.network_requests
        return results, {k: after.get(k, 0) - before.get(k, 0) for k in after}

    try:
        return run_batches(directory, items, 10, identity, process)
    finally:
        client.close()


def run_full_text_retry(loaded: LoadedProjectConfig, manuscript_key: str, literature: Path, pmids: list[str]) -> dict:
    ctx = corpus_context(loaded, manuscript_key, literature)
    # The paper may have entered through any acquisition route, so read the stored acquisitions themselves.
    targets, seen = [], set()
    for name in ("discovery_acquisition", "supplemental_acquisition", "gap_acquisition", "advisor_audit"):
        for path in sorted((ctx.work_dir / name).glob("batch-*.json")):
            for paper in read_json(path)["results"]:
                pmid = str(paper.get("pmid") or "")
                if pmid in pmids and pmid not in seen and isinstance(paper.get("pmcid"), str):
                    seen.add(pmid)
                    targets.append(
                        {
                            "pmid": pmid,
                            "publication_id": paper["publication_id"],
                            "pmcid": paper["pmcid"],
                            "title": paper.get("title", ""),
                            "previous_route": paper.get("full_text_route"),
                        }
                    )
    missing = sorted(set(pmids) - {t["pmid"] for t in targets})
    result = retry_full_text(ctx, targets, execute=True)
    entries = [e for b in result["records"] for e in b["results"]]
    return {
        "status": "SUCCEEDED",
        "key": "(workspace batches)",
        "artifact": ctx.work_dir / "full_text_retry",
        "corpus_id": ctx.corpus_id,
        "counts": {
            "targets": len(targets),
            "without_pmcid": missing,
            "outcomes": {e["pmid"]: e["state"] for e in entries},
            "attempts": {e["pmid"]: e["attempts"] for e in entries},
        },
    }
