"""Parse every acquired corpus asset into canonical Documents, with a per-asset cache.

Canonical article version per publication, in order: open-access JATS (Europe PMC, then the PMC
OA dataset copy), PubTator BioC open-access text, an identity-confirmed manual PDF, then the
PubMed abstract. Other versions (e.g. validation PDFs) are parsed as alternates and never feed
bundles, so one study is not counted twice. Supplements are routed by content type; archive
members are extracted within bounds and routed again.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from pathlib import Path, PurePosixPath

from regkg.literature import files
from regkg.literature.fetch import store_asset
from regkg.literature.parse import (
    BIOC_RULE,
    TABLE_RULE,
    TEXT_RULE,
    Document,
    ParseError,
    Passage,
    parse_bioc,
    parse_jats,
    parse_pubmed_abstract,
)
from regkg.provenance import canonical_json, read_json, sha256_text

PARSE_WORK = "p3-parse-work-2"  # 2: effective limits and row selection belong to the cache key
MAX_SELECTED_ROWS = 2000
ARTICLE_ROUTES = ("jats", "bioc", "docling_pdf", "pubmed_abstract")


def _rules(route: str, options: dict | None = None) -> dict:
    """Everything that changes a parsed document for this route, including the effective limits and the
    row selection. A cache entry is only reused when all of it is identical."""
    base = {"work": PARSE_WORK, "text_rule": TEXT_RULE, "table_rule": TABLE_RULE}
    if route == "bioc":
        base["bioc_rule"] = BIOC_RULE
    if route.startswith("docling"):
        assets = files.docling_assets()
        base.update(pdf_rule=files.PDF_RULE, docling=assets["docling"], models=assets["models"])
    if route == "xlsx":
        base["sheet_rule"] = files.SHEET_RULE
    if route == "delimited":
        base["delimited_rule"] = files.DELIMITED_RULE
    if options:
        base["options"] = options
    return base


def delimited_options(sheet_limits, selector: files.RowSelector | None, max_selected_rows: int) -> dict:
    return {
        "max_rows": sheet_limits.max_rows_per_sheet,
        "max_columns": sheet_limits.max_columns,
        "max_selected_rows": max_selected_rows,
        "selector": selector.fingerprint() if selector else None,
    }


def sheet_options(sheet_limits) -> dict:
    return {
        "max_sheets": sheet_limits.max_sheets,
        "max_rows": sheet_limits.max_rows_per_sheet,
        "max_columns": sheet_limits.max_columns,
    }


def pdf_options(limits) -> dict:
    return {
        "max_bytes": limits.max_bytes,
        "max_pages": limits.max_pages,
        "timeout_seconds": limits.timeout_seconds,
        "ocr": limits.ocr,
    }


def _load_document(payload: dict) -> Document:
    document = Document(
        payload["publication_id"],
        payload["text_version"],
        payload["source_asset_sha256"],
        [Passage(**p) for p in payload["passages"]],
        payload["supplementary"],
        payload.get("extra_rules") or {},
    )
    if document.canonical_text != payload["canonical_text"]:
        raise ValueError(f"{payload['publication_id']}: passages do not reproduce the stored canonical text")
    return document


def parse_cached(
    work_dir: Path, route: str, publication_id: str, content: bytes, name: str, parse, options: dict | None = None
) -> tuple[Document | None, dict]:
    """Run `parse()` once per (asset bytes, route, rules, effective options); later runs read the cache."""
    sha = hashlib.sha256(content).hexdigest()
    key = sha256_text(
        canonical_json({"sha": sha, "route": route, "publication": publication_id, **_rules(route, options)})
    )[:24]
    directory = work_dir / "parsed" / key
    if (directory / "report.json").is_file():
        report = read_json(directory / "report.json")
        document = (
            _load_document(read_json(directory / "document.json")) if (directory / "document.json").is_file() else None
        )
        return document, report
    document, report = parse()
    directory.mkdir(parents=True, exist_ok=True)
    if document is not None:
        (directory / "document.json").write_text(json.dumps(document.to_json(), ensure_ascii=False), encoding="utf-8")
    report = {**report, "cache_key": key, "publication_id": publication_id, "name": name}
    (directory / "report.json").write_text(json.dumps(report, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return document, report


def _xml_report(sha: str, name: str, route: str, state: str, reasons: list[str], document: Document | None) -> dict:
    kinds: dict[str, int] = {}
    for p in document.passages if document else []:
        kinds[p.kind] = kinds.get(p.kind, 0) + 1
    return files.ParseReport(
        sha,
        name,
        PurePosixPath(name).suffix.lstrip("."),
        route,
        route,
        state,
        reasons,
        parser="regkg safe lxml/json",
        components={"passages": kinds},
        document_id=files.document_id(sha, route, document.extra_rules if document else {}),
    ).to_json()


def parse_article(
    work_dir: Path, repo_root: Path, audit: dict, manual: list[dict], limits
) -> tuple[Document | None, dict, list[dict]]:
    """(canonical article document, its report, reports of every attempted/alternate article version)."""
    pid, pmid = audit["publication_id"], audit["pmid"]
    assets = {a["role"]: a for a in audit["assets"]}
    attempts = []
    candidates = []
    for asset in audit["assets"]:
        if asset["role"] == "jats_full_text":
            candidates.append(("jats", asset))
    if audit.get("bioc_full_text") and "pubtator_annotations" in assets:
        candidates.append(("bioc", assets["pubtator_annotations"]))
    for asset in manual:
        if asset["role"] == "manual_article" and asset.get("identity") == "confirmed":
            candidates.append(("docling_pdf", asset))
    if "pubmed_record" in assets:
        candidates.append(("pubmed_abstract", assets["pubmed_record"]))
    parsed: list[tuple[str, dict, Document | None, dict]] = []
    for route, asset in candidates:
        content = (repo_root / asset["path"]).read_bytes()
        sha = hashlib.sha256(content).hexdigest()

        def parse(route=route, content=content, sha=sha, asset=asset):
            try:
                if route == "jats":
                    document = parse_jats(pid, content)
                elif route == "bioc":
                    document = parse_bioc(pid, content)
                elif route == "pubmed_abstract":
                    document = parse_pubmed_abstract(pid, content, pmid)
                else:
                    document, report, _ = files.parse_docling(
                        pid,
                        content,
                        asset["name"],
                        "pdf",
                        "manual_pdf",
                        limits.max_bytes,
                        limits.max_pages,
                        limits.timeout_seconds,
                    )
                    return document, report.to_json()
            except (ParseError, ValueError) as error:
                return None, _xml_report(
                    sha, asset["name"], route, files.PARSE_FAILED, [f"{type(error).__name__}: {error}"], None
                )
            return document, _xml_report(sha, asset["name"], route, files.PARSED, [], document)

        document, report = parse_cached(
            work_dir, route, pid, content, asset["name"], parse, pdf_options(limits) if route == "docling_pdf" else None
        )
        report = {**report, "version_role": "candidate", "asset_role": asset["role"]}
        attempts.append(report)
        parsed.append((route, asset, document, report))
    usable = [x for x in parsed if x[2] is not None and x[3]["state"] in {files.PARSED, files.PARTIAL}]
    # Among JATS copies prefer the one with the most body content: a record carrying only front matter
    # (title and abstract) is not complete full text, whichever source served it first.
    jats = [x for x in usable if x[0] == "jats"]
    best = max(jats, key=lambda x: _body_passages(x[2])) if jats else None
    if best is not None and _body_passages(best[2]):
        chosen, chosen_report = best[2], best[3]
    elif usable:
        chosen, chosen_report = usable[0][2], usable[0][3]
    else:
        chosen, chosen_report = None, None
    if chosen_report is not None:
        chosen_report["version_role"] = "canonical"
    return chosen, chosen_report, attempts


def _body_passages(document: Document | None) -> int:
    return sum(1 for p in document.passages if p.locator.startswith("/article/body")) if document else 0


def parse_supplement(
    work_dir: Path,
    repo_root: Path,
    papers_root: Path,
    publication_id: str,
    asset: dict,
    limits,
    sheet_limits,
    depth: int = 0,
    selector: files.RowSelector | None = None,
    archive_max_bytes: int = files.ZIP_MAX_BYTES,
) -> list[tuple[Document | None, dict]]:
    """Route one supplement by content; archives yield their members' results as well."""
    content = (repo_root / asset["path"]).read_bytes()
    name = asset["name"].removeprefix("supplement-")
    detected, notes = files.detect_type(content, name)
    sha = hashlib.sha256(content).hexdigest()

    def unsupported(reason: str) -> tuple[None, dict]:
        report = files.ParseReport(
            sha,
            name,
            PurePosixPath(name).suffix.lstrip("."),
            detected,
            f"unsupported:{reason}",
            files.NOT_PARSED,
            notes + [reason],
        )
        return None, report.to_json()

    if detected in {"pdf", "docx"}:
        route = f"docling_{detected}"

        def parse():
            document, report, _ = files.parse_docling(
                publication_id,
                content,
                name,
                detected,
                f"supplement_{route}",
                limits.max_bytes,
                limits.max_pages,
                limits.timeout_seconds,
            )
            return document, {**report.to_json(), "reasons": notes + report.reasons}
    elif detected == "xlsx":
        route = "xlsx"

        def parse():
            document, report = files.parse_xlsx(
                publication_id,
                content,
                name,
                sheet_limits.max_sheets,
                sheet_limits.max_rows_per_sheet,
                sheet_limits.max_columns,
            )
            return document, report.to_json()
    elif detected in {"csv", "tsv"}:
        route = "delimited"

        def parse():
            document, report = files.parse_delimited(
                publication_id,
                content,
                name,
                "," if detected == "csv" else "\t",
                sheet_limits.max_rows_per_sheet,
                sheet_limits.max_columns,
                selector,
                MAX_SELECTED_ROWS,
            )
            return document, report.to_json()
    elif detected == "text" and files.looks_tab_delimited(content):
        # Tab-separated tables saved as .txt: rows keep coordinates and are marked for interpretation review.
        route = "delimited"
        notes = notes + ["text_file_detected_as_tab_delimited_table"]

        def parse():
            document, report = files.parse_delimited(
                publication_id,
                content,
                name,
                "\t",
                sheet_limits.max_rows_per_sheet,
                sheet_limits.max_columns,
                selector,
                MAX_SELECTED_ROWS,
            )
            return document, {**report.to_json(), "reasons": notes + report.reasons}
    elif detected == "text":
        route = "text"

        def parse():
            document, report = files.parse_text_file(publication_id, content, name)
            return document, report.to_json()
    elif detected == "zip" and depth == 0:
        members, report = files.inspect_zip(content, name, archive_max_bytes)
        results: list[tuple[Document | None, dict]] = [(None, {**report.to_json(), "parent_asset": asset["sha256"]})]
        for member_name, data in members:
            stored = store_asset(
                papers_root,
                publication_id,
                f"supplement-{member_name}",
                "archive_member",
                data,
                f"archive:{sha}",
                f"archive:{name}/{member_name}",
                repo_root,
            )
            for document, member_report in parse_supplement(
                work_dir,
                repo_root,
                papers_root,
                publication_id,
                {**asdict(stored)},
                limits,
                sheet_limits,
                depth + 1,
                selector,
                archive_max_bytes,
            ):
                results.append((document, {**member_report, "parent_asset": sha, "archive_member": member_name}))
        return results
    elif detected == "ole2_legacy_office":
        return [unsupported("legacy_binary_office_format_no_reader_installed")]
    else:
        return [unsupported(f"no_reader_for_{detected}")]
    options = None
    if route == "delimited":
        options = delimited_options(sheet_limits, selector, MAX_SELECTED_ROWS)
    elif route == "xlsx":
        options = sheet_options(sheet_limits)
    elif route.startswith("docling"):
        options = pdf_options(limits)
    return [parse_cached(work_dir, route, publication_id, content, name, parse, options)]


def parse_all(
    work_dir: Path,
    repo_root: Path,
    papers_root: Path,
    audits: dict[str, dict],
    manual: dict[str, list],
    alternates: list[dict],
    limits,
    sheet_limits,
    log=print,
    selector: files.RowSelector | None = None,
    archive_allowances: dict[tuple[str, str], int] | None = None,
) -> dict:
    """Parse canonical articles for every audited publication, advisor supplements, and alternates."""
    articles, supplements, alternate_results = {}, [], []
    for index, (pmid, audit) in enumerate(sorted(audits.items(), key=lambda kv: int(kv[0])), start=1):
        articles[pmid] = parse_article(work_dir, repo_root, audit, manual.get(pmid, []), limits)
        if index % 50 == 0:
            log(f"articles parsed: {index}/{len(audits)}")
    for pmid, audit in sorted(audits.items(), key=lambda kv: int(kv[0])):
        for item in audit.get("supplements") or []:
            if item.get("asset"):
                for document, report in parse_supplement(
                    work_dir,
                    repo_root,
                    papers_root,
                    audit["publication_id"],
                    item["asset"],
                    limits,
                    sheet_limits,
                    0,
                    selector,
                    (archive_allowances or {}).get((pmid, item["filename"]), files.ZIP_MAX_BYTES),
                ):
                    supplements.append(
                        {"pmid": pmid, "document": document, "report": report, "supplement": item["filename"]}
                    )
        for asset in manual.get(pmid, []):
            if asset["role"] == "manual_supplement" and asset.get("identity") == "confirmed":
                for document, report in parse_supplement(
                    work_dir, repo_root, papers_root, audit["publication_id"], asset, limits, sheet_limits, 0, selector
                ):
                    supplements.append(
                        {"pmid": pmid, "document": document, "report": report, "supplement": asset["name"]}
                    )
        log(f"supplements parsed for PMID {pmid}: {len(supplements)} results so far")
    for item in alternates:
        pmid, asset = item["pmid"], item["asset"]
        content = (repo_root / asset["path"]).read_bytes()
        publication_id = audits[pmid]["publication_id"]

        def parse(content=content, asset=asset, publication_id=publication_id):
            document, report, _ = files.parse_docling(
                publication_id,
                content,
                asset["name"],
                "pdf",
                "pdf_alternate",
                limits.max_bytes,
                limits.max_pages,
                limits.timeout_seconds,
            )
            return document, report.to_json()

        document, report = parse_cached(
            work_dir, "docling_pdf", publication_id, content, asset["name"], parse, pdf_options(limits)
        )
        alternate_results.append(
            {"pmid": pmid, "document": document, "report": {**report, "version_role": "alternate"}}
        )
    return {"articles": articles, "supplements": supplements, "alternates": alternate_results}
