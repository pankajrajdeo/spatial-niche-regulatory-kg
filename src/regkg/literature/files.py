"""Asset routing and readers for article PDFs and supplements behind the canonical Document contract.

Routing checks the bytes, not the filename: an HTML page named `.pdf` is not a PDF. Supported
routes: PDF and DOCX through local Docling (no OCR, no remote services), XLSX through openpyxl,
CSV/TSV through the csv module, plain text, and bounded ZIP inspection whose supported members
are routed again. Everything else is inventoried with an explicit disposition.

Parsing is not interpretation. Spreadsheet and PDF table regions keep their coordinates and raw
cell tokens, but their scientific meaning (entities, contrast, units, statistics) is unknown to the
parser, so their rows are marked for interpretation review and never become ready bundles here.
No formula is evaluated, no macro or link is followed, and file content is never executed.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import io
import stat
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path, PurePosixPath

from regkg.literature.parse import Document, _Builder, section_type
from regkg.literature.xml import normalize_text
from regkg.provenance import canonical_json, stable_id

SHEET_RULE = "sheet-rows-1"
DELIMITED_RULE = "delimited-rows-2"  # 2: complete row scan, selective materialization
TEXT_FILE_RULE = "text-paragraphs-1"
PDF_RULE = "docling-map-1"
# Archive bounds: members, total expanded bytes, and compression ratio (zip-bomb guard).
ZIP_MAX_MEMBERS = 500
ZIP_MAX_BYTES = 500_000_000
ZIP_MAX_RATIO = 200

# Parse states (coverage ledger vocabulary)
PARSED = "PARSED"
PARTIAL = "PARTIAL"
PARSE_FAILED = "PARSE_FAILED"
NOT_PARSED = "NOT_PARSED"


@dataclass
class ParseReport:
    asset_sha256: str
    name: str
    declared_extension: str
    detected_type: str
    route: str  # jats | bioc | docling_pdf | docling_docx | xlsx | delimited | text | zip | unsupported:<why>
    state: str  # PARSED | PARTIAL | PARSE_FAILED | NOT_PARSED
    reasons: list[str] = field(default_factory=list)
    parser: str | None = None
    parser_config: dict = field(default_factory=dict)
    components: dict = field(default_factory=dict)  # e.g. pages, paragraphs, tables, sheets, rows inspected
    interpretation: str | None = None  # e.g. table_meaning_requires_review
    document_id: str | None = None
    members: list[dict] = field(default_factory=list)  # archive members

    def to_json(self) -> dict:
        return asdict(self)


def detect_type(content: bytes, name: str) -> tuple[str, list[str]]:
    """(detected type, mismatch notes) from magic bytes and structure; the extension is only a claim."""
    extension = PurePosixPath(name).suffix.lower().lstrip(".")
    head = content[:1024]
    notes = []
    if not content:
        return "empty", ["empty_file"]
    if head.startswith(b"%PDF-"):
        detected = "pdf"
    elif head.startswith(b"PK\x03\x04") or head.startswith(b"PK\x05\x06"):
        try:
            names = set(zipfile.ZipFile(io.BytesIO(content)).namelist())
        except zipfile.BadZipFile:
            return "corrupt_zip", ["zip_signature_but_unreadable"]
        detected = (
            "xlsx"
            if "xl/workbook.xml" in names
            else "docx"
            if "word/document.xml" in names
            else ("pptx" if "ppt/presentation.xml" in names else "odf" if "mimetype" in names else "zip")
        )
    elif head.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        detected = "ole2_legacy_office"  # .xls/.doc binary formats
    elif head.startswith((b"\x89PNG", b"\xff\xd8\xff", b"GIF8", b"II*\x00", b"MM\x00*")):
        detected = "image"
    elif head[4:8] == b"ftyp":
        detected = "video"
    elif head.lstrip().lower().startswith((b"<!doctype html", b"<html")):
        detected = "html"
    elif b"\x00" not in head:
        try:
            content[:65536].decode("utf-8")
            detected = {"csv": "csv", "tsv": "tsv", "tab": "tsv"}.get(extension, "text")
        except UnicodeDecodeError:
            detected = "text_non_utf8"
    else:
        detected = "binary_unknown"
    expected = {
        "pdf": "pdf",
        "xlsx": "xlsx",
        "xlsm": "xlsx",
        "docx": "docx",
        "zip": "zip",
        "xls": "ole2_legacy_office",
        "doc": "ole2_legacy_office",
        "csv": "csv",
        "tsv": "tsv",
        "txt": "text",
    }.get(extension)
    if expected and expected != detected:
        notes.append(f"extension_{extension}_but_content_{detected}")
    return detected, notes


def looks_tab_delimited(content: bytes, sample_lines: int = 200) -> bool:
    """A text file whose lines mostly carry the same number (>= 1) of tabs is a table, not prose."""
    lines = [line for line in content[:1_000_000].decode("utf-8", errors="replace").splitlines()[:sample_lines] if line]
    if len(lines) < 3:
        return False
    counts = [line.count("\t") for line in lines]
    common = max(set(counts), key=counts.count)
    return common >= 1 and counts.count(common) / len(counts) >= 0.8


def _document(publication_id: str, text_version: str, content: bytes, rules: dict) -> Document:
    return Document(publication_id, text_version, hashlib.sha256(content).hexdigest(), extra_rules=rules)


def document_id(asset_sha256: str, route: str, rules: dict) -> str:
    return stable_id("document", {"asset_sha256": asset_sha256, "route": route, **rules})


# ---------------------------------------------------------------------------
# Spreadsheets and delimited text


def _token(value) -> tuple[str | None, str | None]:
    """(canonical string, value type) of a stored cell value; dates are flagged, never re-guessed."""
    if value is None:
        return None, None
    if isinstance(value, bool):
        return ("TRUE" if value else "FALSE"), "bool"
    if isinstance(value, int):
        return str(value), "int"
    if isinstance(value, float):
        return repr(value), "float"
    if isinstance(value, dt.datetime | dt.date | dt.time):
        # A date may be a gene symbol an earlier spreadsheet converted (e.g. SEPT2); keep it flagged.
        return value.isoformat(), "date"
    return str(value), "text"


def parse_xlsx(
    publication_id: str,
    content: bytes,
    name: str,
    max_sheets: int,
    max_rows: int,
    max_columns: int,
    full_inspection_max_bytes: int = 3_000_000,
) -> tuple[Document | None, ParseReport]:
    import openpyxl

    sha = hashlib.sha256(content).hexdigest()
    rules = {
        "sheet_rule": SHEET_RULE,
        "openpyxl": openpyxl.__version__,
        "max_sheets": max_sheets,
        "max_rows": max_rows,
        "max_columns": max_columns,
    }
    report = ParseReport(
        sha,
        name,
        PurePosixPath(name).suffix.lower().lstrip("."),
        "xlsx",
        "xlsx",
        NOT_PARSED,
        parser=f"openpyxl {openpyxl.__version__}",
        parser_config={
            "max_sheets": max_sheets,
            "max_rows_per_sheet": max_rows,
            "max_columns": max_columns,
            "formulas": "text_and_cached_value_kept_separately",
            "evaluation": "none",
            "macros": "not_loaded",
        },
        interpretation="table_meaning_requires_review",
    )
    try:
        formulas = openpyxl.load_workbook(io.BytesIO(content), read_only=True, data_only=False, keep_links=False)
        cached = openpyxl.load_workbook(io.BytesIO(content), read_only=True, data_only=True, keep_links=False)
    except Exception as error:  # noqa: BLE001 - any reader failure is a reported parse failure
        report.state, report.reasons = PARSE_FAILED, [f"{type(error).__name__}: {error}"[:300]]
        return None, report
    # Structure that the streaming reader cannot see (hidden rows/columns, merged cells) is read only
    # for small workbooks; otherwise it is recorded as not inspected.
    structure = {}
    if len(content) <= full_inspection_max_bytes:
        try:
            full = openpyxl.load_workbook(io.BytesIO(content), read_only=False, data_only=False, keep_links=False)
            for ws in full.worksheets:
                structure[ws.title] = {
                    "merged_ranges": [str(r) for r in ws.merged_cells.ranges][:50],
                    "hidden_rows": [i for i, d in ws.row_dimensions.items() if d.hidden][:200],
                    "hidden_columns": [k for k, d in ws.column_dimensions.items() if d.hidden][:200],
                }
        except Exception as error:  # noqa: BLE001
            report.reasons.append(f"structure_inspection_failed: {type(error).__name__}")
    else:
        report.reasons.append("hidden_rows_columns_and_merged_cells_not_inspected_large_workbook")
    document = _document(publication_id, "supplement_xlsx", content, rules)
    build = _Builder(document)
    sheets = []
    partial = False
    for index, ws in enumerate(formulas.worksheets):
        state = getattr(ws, "sheet_state", "visible")
        entry = {
            "sheet": ws.title,
            "state": state,
            "rows_inspected": 0,
            "rows_total": 0,
            "columns_seen": 0,
            "formula_cells": 0,
            "date_typed_cells": 0,
            "header_row": None,
            **structure.get(ws.title, {}),
        }
        sheets.append(entry)
        if index >= max_sheets:
            entry["status"] = "not_inspected_sheet_limit"
            partial = True
            continue
        values = cached[ws.title].iter_rows()
        header: list[str | None] | None = None
        for row_number, (row, cached_row) in enumerate(zip(ws.iter_rows(), values, strict=False), start=1):
            entry["rows_total"] += 1
            if entry["rows_inspected"] >= max_rows:
                continue  # counted, not parsed
            cells = []
            for column, (cell, cached_cell) in enumerate(zip(row, cached_row, strict=False)):
                if column >= max_columns:
                    entry["columns_truncated"] = True
                    break
                formula = cell.value if isinstance(cell.value, str) and cell.value.startswith("=") else None
                token, kind = _token(cached_cell.value if formula else cell.value)
                if token is None and formula is None:
                    continue
                entry["formula_cells"] += formula is not None
                entry["date_typed_cells"] += kind == "date"
                cells.append(
                    {
                        "column": column + 1,
                        "row": row_number,
                        "value": token,
                        "value_type": kind,
                        "formula": formula,
                        "cached_value_missing": bool(formula) and token is None,
                        "number_format": getattr(cell, "number_format", None),
                    }
                )
            if not cells:
                continue
            entry["rows_inspected"] += 1
            entry["columns_seen"] = max(entry["columns_seen"], max(c["column"] for c in cells))
            if header is None:
                # Assumption (recorded): the first nonempty row is the header. Region meaning is unknown.
                header = [None] * entry["columns_seen"]
                for c in cells:
                    header[c["column"] - 1] = c["value"]
                entry["header_row"] = row_number
                kind = "supplement_table_header"
            else:
                for c in cells:
                    c["header"] = header[c["column"] - 1] if c["column"] <= len(header) else None
                kind = "supplement_table_row"
            text = " | ".join(c["value"] or f"={c['formula']}" for c in cells)
            build.add(
                kind,
                text,
                f"xlsx:sheet={ws.title};row={row_number}",
                f"Supplement {name} > {ws.title}",
                "supplement",
                cells=cells,
                table_id=stable_id("table", {"asset": sha, "sheet": ws.title}),
                table_structure="sheet_first_row_header_unverified",
                item_id=ws.title,
            )
        entry["status"] = "partial_row_limit" if entry["rows_total"] > entry["rows_inspected"] else "inspected"
        if entry["rows_total"] > max_rows or entry.get("columns_truncated"):
            partial = True
    report.components = {"sheets": sheets, "passages": len(document.passages)}
    report.state = PARTIAL if partial or report.reasons else PARSED
    if partial:
        report.reasons.append("row/column/sheet limits reached; remaining cells counted, not parsed")
    report.document_id = document_id(sha, "xlsx", rules)
    return (document if document.passages else None), report


@dataclass(frozen=True)
class RowSelector:
    """Which rows of a large table are materialized beyond the leading sample.

    A row is kept when a cell is exactly one of `symbols` (a candidate gene/TF name or alias) or
    contains one of `phrases` (a manuscript population name). Every row is still scanned and counted,
    so a selective materialization is never reported as a complete one.
    """

    rule: str
    symbols: frozenset[str]
    phrases: frozenset[str]

    def fingerprint(self) -> dict:
        """Identity of the effective selection: a digest of its exact contents, not just their counts."""
        body = canonical_json({"rule": self.rule, "symbols": sorted(self.symbols), "phrases": sorted(self.phrases)})
        return {
            "rule": self.rule,
            "digest": hashlib.sha256(body.encode()).hexdigest(),
            "symbols": len(self.symbols),
            "phrases": len(self.phrases),
        }

    def matches(self, row: list[str]) -> bool:
        for value in row:
            token = value.strip()
            if not token:
                continue
            if token.upper() in self.symbols:
                return True
            lowered = token.lower()
            if any(phrase in lowered for phrase in self.phrases):
                return True
        return False


def parse_delimited(
    publication_id: str,
    content: bytes,
    name: str,
    delimiter: str,
    max_rows: int,
    max_columns: int,
    selector: RowSelector | None = None,
    max_selected_rows: int = 2000,
) -> tuple[Document | None, ParseReport]:
    sha = hashlib.sha256(content).hexdigest()
    # Passage content depends on the limits and on the selection, so both belong to document identity.
    rules = {
        "delimited_rule": DELIMITED_RULE,
        "delimiter": delimiter,
        "max_rows": max_rows,
        "max_columns": max_columns,
        "max_selected_rows": max_selected_rows,
        "selector": selector.fingerprint() if selector else None,
    }
    report = ParseReport(
        sha,
        name,
        PurePosixPath(name).suffix.lower().lstrip("."),
        "delimited",
        "delimited",
        NOT_PARSED,
        parser="python csv",
        parser_config={
            "delimiter": delimiter,
            "encoding": "utf-8-sig",
            "typed_conversion": "none (raw tokens kept)",
            "scan": "all rows",
            "materialization": f"header + first {max_rows} rows (selector cap {max_selected_rows})"
            + (" + rows matching the manuscript selector" if selector else ""),
            "selector": selector.fingerprint() if selector else None,
        },
        interpretation="table_meaning_requires_review",
    )
    try:
        text = content.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        report.state, report.reasons = PARSE_FAILED, [f"not UTF-8: {error}"]
        return None, report
    document = _document(publication_id, "supplement_delimited", content, rules)
    build = _Builder(document)
    widths: dict[int, int] = {}
    header, rows_total, inspected, matched, materialized_matches = None, 0, 0, 0, 0
    try:
        for row_number, row in enumerate(csv.reader(io.StringIO(text), delimiter=delimiter), start=1):
            rows_total += 1
            if not any(cell.strip() for cell in row):
                continue
            widths[len(row)] = widths.get(len(row), 0) + 1
            selected = header is not None and selector is not None and selector.matches(row)
            matched += int(selected)
            if selected and materialized_matches >= max_selected_rows:
                selected = False  # the overflow stays counted, never silently dropped
            materialized_matches += int(selected and inspected >= max_rows)
            # Every row is read and counted; only sample and selected rows become passages, so memory
            # stays bounded by the materialized set rather than by the table size.
            if inspected >= max_rows and not selected:
                continue
            inspected += 1
            # Tokens stay exactly as written: "NA", "<0.01", "1e-5", leading zeros are not converted.
            cells = [
                {"column": i + 1, "row": row_number, "value": v, "value_type": "text"}
                for i, v in enumerate(row[:max_columns])
                if v != ""
            ]
            if header is None:
                header = row
                kind = "supplement_table_header"
            else:
                for c in cells:
                    c["header"] = header[c["column"] - 1] if c["column"] <= len(header) else None
                kind = "supplement_table_row"
            build.add(
                kind,
                " | ".join(c["value"] for c in cells),
                f"delimited:row={row_number}",
                f"Supplement {name}",
                "supplement",
                cells=cells,
                table_id=stable_id("table", {"asset": sha}),
                table_structure="delimited_first_row_header_unverified",
            )
    except csv.Error as error:
        report.state, report.reasons = PARSE_FAILED, [f"csv: {error}"]
        return None, report
    report.components = {
        "rows_total": rows_total,
        "rows_inspected": inspected,
        "rows_matching_selector": matched,
        "selector_rows_materialized_beyond_sample": materialized_matches,
        "scan_complete": True,
        "row_widths": widths,
    }
    if len(widths) > 1:
        report.reasons.append(f"non_rectangular_rows: widths {sorted(widths)}")
    if matched > materialized_matches + min(matched, max_rows):
        report.reasons.append(f"selector_match_limit_reached: {matched} matches, {materialized_matches} materialized")
    if rows_total > inspected:
        report.reasons.append(
            f"selective_materialization: {inspected} of {rows_total} rows materialized "
            f"(header + first {max_rows} + {matched} selector matches); all rows scanned and counted"
        )
    report.state = PARTIAL if report.reasons else PARSED
    report.document_id = document_id(sha, "delimited", rules)
    return (document if document.passages else None), report


def parse_text_file(publication_id: str, content: bytes, name: str) -> tuple[Document | None, ParseReport]:
    sha = hashlib.sha256(content).hexdigest()
    rules = {"text_file_rule": TEXT_FILE_RULE}
    report = ParseReport(
        sha, name, PurePosixPath(name).suffix.lower().lstrip("."), "text", "text", NOT_PARSED, parser="utf-8 paragraphs"
    )
    try:
        text = content.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        report.state, report.reasons = PARSE_FAILED, [f"not UTF-8: {error}"]
        return None, report
    document = _document(publication_id, "supplement_text", content, rules)
    build = _Builder(document)
    offset = 0
    for block in text.split("\n\n"):
        build.add("supplement_text", block, f"text:char={offset}", f"Supplement {name}", "supplement")
        offset += len(block) + 2
    report.state, report.components = PARSED, {"paragraphs": len(document.passages)}
    report.document_id = document_id(sha, "text", rules)
    return (document if document.passages else None), report


# ---------------------------------------------------------------------------
# Archives


def inspect_zip(
    content: bytes, name: str, max_bytes: int = ZIP_MAX_BYTES
) -> tuple[list[tuple[str, bytes]], ParseReport]:
    """Bounded, non-executing ZIP inspection: returns safe members to route, plus the inventory."""
    sha = hashlib.sha256(content).hexdigest()
    report = ParseReport(
        sha,
        name,
        "zip",
        "zip",
        "zip",
        NOT_PARSED,
        parser="zipfile (bounded)",
        parser_config={"max_members": ZIP_MAX_MEMBERS, "max_bytes": max_bytes, "max_ratio": ZIP_MAX_RATIO},
    )
    try:
        archive = zipfile.ZipFile(io.BytesIO(content))
        infos = archive.infolist()
    except zipfile.BadZipFile as error:
        report.state, report.reasons = PARSE_FAILED, [f"bad zip: {error}"]
        return [], report
    members, total = [], 0
    for info in infos:
        member = {"name": info.filename, "size": info.file_size, "compressed": info.compress_size}
        path = PurePosixPath(info.filename)
        mode = info.external_attr >> 16
        if info.is_dir() or path.name.startswith(("._", ".DS_Store")) or "__MACOSX" in path.parts:
            member["disposition"] = "skipped_directory_or_os_metadata"
        elif path.is_absolute() or ".." in path.parts:
            member["disposition"] = "rejected_path_traversal"
        elif stat.S_ISLNK(mode):
            member["disposition"] = "rejected_symlink"
        elif info.flag_bits & 0x1:
            member["disposition"] = "unsupported_encrypted"
        elif (
            len(members) >= ZIP_MAX_MEMBERS
            or total + info.file_size > max_bytes
            or (info.compress_size and info.file_size / info.compress_size > ZIP_MAX_RATIO)
        ):
            member["disposition"] = "deferred_archive_limit"
        else:
            data = archive.read(info)
            total += len(data)
            member.update(disposition="extracted_for_routing", sha256=hashlib.sha256(data).hexdigest())
            members.append((path.name, data))
        report.members.append(member)
    deferred = [m for m in report.members if m["disposition"].startswith(("rejected", "unsupported", "deferred"))]
    report.state = PARTIAL if deferred else PARSED
    report.reasons = [f"{len(deferred)} members not extracted"] if deferred else []
    report.components = {"members": len(infos), "extracted": len(members)}
    return members, report


# ---------------------------------------------------------------------------
# Docling (PDF, DOCX)


def docling_assets() -> dict:
    """Installed Docling versions and cached model revisions (local Hugging Face cache refs)."""
    import importlib.metadata as metadata

    versions = {p: metadata.version(p) for p in ("docling", "docling-core", "docling-ibm-models")}
    cache = Path.home() / ".cache" / "huggingface" / "hub"
    models = {}
    for repo in ("docling-project--docling-layout-heron", "docling-project--docling-models"):
        ref = cache / f"models--{repo}" / "refs" / "main"
        models[repo.replace("--", "/")] = ref.read_text().strip() if ref.is_file() else None
    return {**versions, "models": models}


_CONVERTERS: dict = {}


def _converter(timeout: float):
    if timeout not in _CONVERTERS:
        from docling.datamodel.accelerator_options import AcceleratorOptions
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.document_converter import DocumentConverter, PdfFormatOption, WordFormatOption

        options = PdfPipelineOptions()
        options.do_ocr = False  # a page without a text layer is reported, not guessed
        options.do_table_structure = True
        options.enable_remote_services = False
        options.allow_external_plugins = False
        options.generate_page_images = False
        options.generate_picture_images = False
        options.document_timeout = timeout
        options.accelerator_options = AcceleratorOptions(device="auto")
        _CONVERTERS[timeout] = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=options),
                InputFormat.DOCX: WordFormatOption(),
            }
        )
    return _CONVERTERS[timeout]


def pdf_page_count(content: bytes) -> int | None:
    try:
        import pypdfium2

        return len(pypdfium2.PdfDocument(content))
    except Exception:  # noqa: BLE001 - encrypted/corrupt PDFs are reported by the conversion itself
        return None


def parse_docling(
    publication_id: str,
    content: bytes,
    name: str,
    kind: str,
    text_version: str,
    max_bytes: int,
    max_pages: int,
    timeout: float,
) -> tuple[Document | None, ParseReport, dict]:
    """PDF/DOCX -> Document with page/bbox/item provenance. Returns (document, report, raw export)."""
    from docling.datamodel.base_models import ConversionStatus, DocumentStream
    from docling_core.types.doc import PictureItem, SectionHeaderItem, TableItem, TextItem

    sha = hashlib.sha256(content).hexdigest()
    assets = docling_assets()
    rules = {"pdf_rule": PDF_RULE, "docling": assets["docling"], "docling_core": assets["docling-core"]}
    route = f"docling_{kind}"
    report = ParseReport(
        sha,
        name,
        PurePosixPath(name).suffix.lower().lstrip("."),
        kind,
        route,
        NOT_PARSED,
        parser=f"docling {assets['docling']}",
        parser_config={
            "ocr": False,
            "table_structure": True,
            "remote_services": False,
            "max_pages": max_pages,
            "max_bytes": max_bytes,
            "timeout_seconds": timeout,
            "models": assets["models"],
        },
    )
    if len(content) > max_bytes:
        report.state, report.reasons = PARSE_FAILED, [f"size {len(content)} exceeds {max_bytes}; not converted"]
        return None, report, {}
    pages = pdf_page_count(content) if kind == "pdf" else None
    stream = DocumentStream(name=f"{sha[:12]}.{kind}", stream=io.BytesIO(content))
    try:
        result = _converter(timeout).convert(stream, raises_on_error=False, max_num_pages=max_pages)
    except Exception as error:  # noqa: BLE001
        report.state, report.reasons = PARSE_FAILED, [f"{type(error).__name__}: {error}"[:300]]
        return None, report, {}
    if result.status not in {ConversionStatus.SUCCESS, ConversionStatus.PARTIAL_SUCCESS}:
        report.state = PARSE_FAILED
        report.reasons = [f"docling status {result.status.value}"] + [str(e.error_message)[:200] for e in result.errors]
        if pages is not None and pages > max_pages:
            report.reasons.append(f"{pages} pages exceed the {max_pages}-page limit; request a page-limited copy")
        return None, report, {}
    doc = result.document
    document = _document(publication_id, text_version, content, rules)
    build = _Builder(document)
    headings: list[str] = []
    captions_of_tables = {c.cref for t in doc.tables for c in t.captions}
    footnotes_of_tables = {c.cref for t in doc.tables for c in t.footnotes}
    captions_of_pictures = {c.cref for p in doc.pictures for c in p.captions}
    removed = {"page_header": 0, "page_footer": 0}
    text_pages: set[int] = set()
    tables = figures = 0

    def provenance(item) -> dict:
        prov = item.prov[0] if getattr(item, "prov", None) else None
        if prov is None:
            return {}
        box = prov.bbox
        text_pages.add(prov.page_no)
        return {"page": prov.page_no, "bbox": [round(box.l, 2), round(box.t, 2), round(box.r, 2), round(box.b, 2)]}

    for item, _level in doc.iterate_items():
        label = str(getattr(item, "label", ""))
        path = " > ".join(headings[-3:]) or "Body"
        kind_of_section = section_type(headings[-3:], [])
        if label in removed:
            removed[label] += 1  # repeated running headers/footers are not article content
            continue
        if isinstance(item, SectionHeaderItem):
            level = max(1, int(getattr(item, "level", 1) or 1))
            del headings[level - 1 :]  # a heading replaces its level and everything below it
            headings.append(normalize_text(item.text))
            continue
        if isinstance(item, TableItem):
            tables += 1
            _docling_table(build, item, doc, sha, path, kind_of_section, provenance(item))
            continue
        if isinstance(item, PictureItem):
            figures += 1
            continue  # the caption is its own item; pixels are never interpreted
        if not isinstance(item, TextItem):
            continue
        text = normalize_text(item.text)
        if not text:
            continue
        if item.self_ref in captions_of_tables:
            continue  # emitted with its table
        if item.self_ref in footnotes_of_tables:
            continue
        kind_name = (
            "figure_caption"
            if item.self_ref in captions_of_pictures or label == "caption"
            else "title"
            if label == "title"
            else "footnote"
            if label == "footnote"
            else "formula"
            if label == "formula"
            else "paragraph"
        )
        build.add(kind_name, text, f"docling:{item.self_ref}", path, kind_of_section, **provenance(item))
    total_pages = len(doc.pages)
    blank = sorted(set(doc.pages) - text_pages)
    # Running headers/footers sit in Docling's furniture layer and are not iterated as content.
    furniture = sum(
        1 for text in doc.texts if str(getattr(text, "content_layer", "body")) not in {"body", "ContentLayer.BODY"}
    )
    report.components = {
        "furniture_items_excluded": furniture,
        "pages_in_file": pages,
        "pages_converted": total_pages,
        "passages": len(document.passages),
        "tables": tables,
        "figures": figures,
        "running_headers_footers_removed": removed,
        "pages_without_text_items": blank[:50],
    }
    confidence = getattr(result, "confidence", None)
    if confidence is not None:
        report.components["quality_grade_mean"] = str(getattr(confidence, "mean_grade", None))
        report.components["quality_grade_low"] = str(getattr(confidence, "low_grade", None))
    if pages is not None and pages > total_pages:
        report.reasons.append(f"only {total_pages} of {pages} pages converted (page limit)")
    if blank:
        report.reasons.append(f"{len(blank)} pages without text items (image-only or scanned; OCR disabled)")
    if result.status == ConversionStatus.PARTIAL_SUCCESS:
        report.reasons.append("docling reported partial success (e.g. timeout)")
    if tables:
        report.interpretation = "pdf_table_structure_unverified"
    report.state = PARTIAL if report.reasons else PARSED
    if not document.passages:
        report.state = PARSE_FAILED
        report.reasons.append("no text passages extracted")
        return None, report, {}
    report.document_id = document_id(sha, route, rules)
    return document, report, doc.export_to_dict()


def _docling_table(build: _Builder, item, doc, sha: str, path: str, kind_of_section: str, prov: dict) -> None:
    table_id = stable_id("table", {"asset": sha, "item": item.self_ref})
    caption = normalize_text(item.caption_text(doc) or "")
    status = "present" if caption else "absent"
    common = {"table_id": table_id, "table_caption_status": status, "item_id": item.self_ref, **prov}
    if caption:
        build.add("table_caption", caption, f"docling:{item.self_ref}#caption", path, kind_of_section, **common)
    grid = item.data.grid
    header_rows = [r for r, row in enumerate(grid) if row and all(c.column_header for c in row if c.text)]
    headers: list[str] = []
    if header_rows:
        width = item.data.num_cols
        headers = [
            " / ".join(
                dict.fromkeys(normalize_text(grid[r][c].text) for r in header_rows if normalize_text(grid[r][c].text))
            )
            for c in range(width)
        ]
    # Docling's grid is a model output; its merged-cell and row alignment are not verified here.
    structure = "docling_grid_unverified" if header_rows else "no_header"
    for r, row in enumerate(grid):
        seen, cells = set(), []
        for c, cell in enumerate(row):
            key = (cell.start_row_offset_idx, cell.start_col_offset_idx)
            if key in seen or not normalize_text(cell.text):
                continue
            seen.add(key)
            cells.append(
                {
                    "text": normalize_text(cell.text),
                    "col_start": cell.start_col_offset_idx,
                    "col_span": cell.col_span,
                    "row_span": cell.row_span,
                    "column_header": cell.column_header,
                    "header": headers[c] if headers and r not in header_rows else None,
                }
            )
        if not cells:
            continue
        kind = "table_header" if r in header_rows else "table_row"
        build.add(
            kind,
            " | ".join(c["text"] for c in cells),
            f"docling:{item.self_ref}#row={r}",
            path,
            kind_of_section,
            table_header=" | ".join(headers) if headers else None,
            table_structure=structure,
            cells=cells,
            **common,
        )
    for note in item.footnotes:
        text = normalize_text(note.resolve(doc).text)
        if text:
            build.add(
                "table_footnote",
                text,
                f"docling:{note.cref}",
                path,
                kind_of_section,
                table_structure=structure,
                **common,
            )
