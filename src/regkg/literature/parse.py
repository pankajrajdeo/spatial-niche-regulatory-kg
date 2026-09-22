"""Canonical documents with exact passage offsets and original XML locators.

Canonical text is the passages joined by a blank line, each passage normalized by rule
`ws-collapse-nfc-block-space-2` (block boundaries spaced, nested floats kept out of paragraphs,
Unicode NFC, whitespace runs -> one space). Every passage records its
[start, end) offsets in that text and the XPath of its source element. Table rows are rendered
as their cells joined by " | "; the header row is kept as its own passage. Figure pixels are not
interpreted; captions are text.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field

from lxml import etree

from regkg.literature.xml import FLOAT_TAGS, element_text, normalize_text, parse_xml
from regkg.provenance import stable_id

TEXT_RULE = "ws-collapse-nfc-block-space-3"  # 3: <break/> is a word boundary
# Rule 3: every table has an internal identity (asset + table locator) independent of the optional
# XML id, and a recorded caption status; rule 2 grouped table context only by XML id.
TABLE_RULE = "span-expanded-grid-3"
CAPTION_PRESENT = "present"
CAPTION_LABEL_ONLY = "label_only"  # a label such as "Table 1" is not a caption
CAPTION_ABSENT = "absent"
# BioC kinds rule 2: a generic `footnote` (e.g. a supplementary URL list) is a footnote, not a table
# footnote; only BioC `table_footnote` passages, or footnotes inside a TABLE section, belong to tables.
BIOC_RULE = "bioc-kinds-2"
SEPARATOR = "\n\n"
XLINK = "{http://www.w3.org/1999/xlink}href"
SKIP_ANCESTORS = {"fig", "table-wrap", "ref-list", "supplementary-material", "caption", "table", "fn-group"}
SECTION_KEYWORDS = [
    ("methods", ("method", "material", "experimental procedure", "star★methods", "star methods")),
    ("results", ("result",)),
    ("discussion", ("discussion", "conclusion")),
    ("introduction", ("introduction", "background")),
]


class ParseError(ValueError):
    """A fetched asset could not be turned into a canonical document."""


@dataclass
class Passage:
    passage_id: str
    order: int
    # title | abstract | paragraph | figure_caption | table_caption | table_header | table_row |
    # table_footnote | footnote (generic, not table-bound) | supplementary
    kind: str
    section_path: str
    section_type: str
    text: str
    start: int
    end: int
    locator: str  # XPath in the source asset, or a named field for search records
    item_id: str | None = None  # figure/table/supplement id as given in the source (may be absent)
    table_id: str | None = None  # internal table identity; never shared by two source tables
    table_caption_status: str | None = None  # present | label_only | absent (table passages only)
    item_label: str | None = None
    table_header: str | None = None  # column header paths joined by " | " (supported layouts only)
    table_structure: str | None = None  # header_grid_expanded | no_header | unsupported_layout:* | flattened_bioc_*
    cells: list[dict] | None = None  # structured cells: text, column range, header (supported layouts only)
    asset_sha256: str | None = None  # raw source identity, kept separately from the content-qualified ID
    page: int | None = None  # PDF page (1-based) where the passage starts
    bbox: list[float] | None = None  # PDF bounding box (left, top, right, bottom) on that page


@dataclass
class Document:
    publication_id: str
    text_version: str  # europepmc_jats | pubmed_abstract | europepmc_search_record
    source_asset_sha256: str
    passages: list[Passage] = field(default_factory=list)
    supplementary: list[dict] = field(default_factory=list)
    # Parser-specific rule versions; they join passage identity (e.g. BioC kinds, PDF conversion).
    extra_rules: dict = field(default_factory=dict)

    @property
    def canonical_text(self) -> str:
        return SEPARATOR.join(p.text for p in self.passages)

    @property
    def canonical_sha256(self) -> str:
        return hashlib.sha256(self.canonical_text.encode("utf-8")).hexdigest()

    def to_json(self) -> dict:
        return {
            "publication_id": self.publication_id,
            "text_version": self.text_version,
            "text_rule": TEXT_RULE,
            "table_rule": TABLE_RULE,
            "source_asset_sha256": self.source_asset_sha256,
            "canonical_sha256": self.canonical_sha256,
            "canonical_text": self.canonical_text,
            "passages": [asdict(p) for p in self.passages],
            "supplementary": self.supplementary,
            **({"extra_rules": self.extra_rules} if self.extra_rules else {}),
        }


class _Builder:
    def __init__(self, document: Document) -> None:
        self.document = document
        self.offset = 0

    def add(self, kind: str, text: str, locator: str, section_path: str, section_type: str, **extra) -> None:
        text = normalize_text(text)
        if not text:
            return
        if self.document.passages:
            self.offset += len(SEPARATOR)
        start, end = self.offset, self.offset + len(text)
        self.offset = end
        order = len(self.document.passages)
        # Content-qualified identity: a revised normalization/table rule or changed text over the same
        # raw asset and XPath yields a new passage ID instead of silently reusing the old one.
        passage_id = stable_id(
            "passage",
            {
                "asset_sha256": self.document.source_asset_sha256,
                "locator": locator,
                "kind": kind,
                "text_rule": TEXT_RULE,
                "table_rule": TABLE_RULE,
                "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                **self.document.extra_rules,
            },
        )
        extra.setdefault("asset_sha256", self.document.source_asset_sha256)
        self.document.passages.append(
            Passage(passage_id, order, kind, section_path, section_type, text, start, end, locator, **extra)
        )


def section_type(titles: list[str], sec_types: list[str]) -> str:
    for value in [*sec_types, *titles]:
        lowered = value.lower()
        for name, keywords in SECTION_KEYWORDS:
            if any(keyword in lowered for keyword in keywords):
                return name
    return "other"


def _sections(element: etree._Element) -> tuple[list[str], list[str]]:
    titles, types = [], []
    for ancestor in reversed(list(element.iterancestors("sec", "abstract", "app", "boxed-text"))):
        title = element_text(ancestor.find("title"))
        if ancestor.tag == "abstract":
            title = title or "Abstract"
        if title:
            titles.append(title)
        if ancestor.get("sec-type"):
            types.append(ancestor.get("sec-type"))
    return titles, types


def _row_cells(row: etree._Element) -> list[str]:
    return [element_text(cell) for cell in row if cell.tag in {"td", "th"}]


def parse_jats(publication_id: str, content: bytes) -> Document:
    root = parse_xml(content)
    if root.tag != "article":
        raise ParseError(f"expected JATS <article>, got <{root.tag}>")
    tree = root.getroottree()
    document = Document(publication_id, "europepmc_jats", hashlib.sha256(content).hexdigest())
    build = _Builder(document)
    title = root.find("front/article-meta/title-group/article-title")
    if title is not None:
        build.add("title", element_text(title), tree.getpath(title), "Title", "title")
    for abstract in root.iterfind("front/article-meta/abstract"):
        for paragraph in abstract.iter("p"):
            titles, _ = _sections(paragraph)
            build.add(
                "abstract",
                element_text(paragraph, skip=FLOAT_TAGS),
                tree.getpath(paragraph),
                " > ".join(titles) or "Abstract",
                "abstract",
            )
    for container in (root.find("body"), root.find("back")):
        if container is None:
            continue
        for element in container.iter("p", "fig", "table-wrap", "supplementary-material"):
            ancestors = {a.tag for a in element.iterancestors()}
            if element.tag == "p" and ancestors & SKIP_ANCESTORS:
                continue
            if element.tag in {"fig", "table-wrap"} and ancestors & {"fig", "table-wrap"}:
                continue
            titles, types = _sections(element)
            path = " > ".join(titles) or ("Back matter" if container.tag == "back" else "Body")
            kind_of_section = section_type(titles, types)
            locator = tree.getpath(element)
            if element.tag == "p":
                build.add("paragraph", element_text(element, skip=FLOAT_TAGS), locator, path, kind_of_section)
            elif element.tag == "fig":
                label = element_text(element.find("label"))
                caption = element_text(element.find("caption"))
                build.add(
                    "figure_caption",
                    f"{label} {caption}".strip(),
                    locator,
                    path,
                    kind_of_section,
                    item_id=element.get("id"),
                    item_label=label or None,
                )
            elif element.tag == "table-wrap":
                _add_table(build, element, tree, path, kind_of_section)
            else:
                label = element_text(element.find("label"))
                caption = element_text(element.find("caption"))
                href = element.get(XLINK) or next((m.get(XLINK) for m in element.iter("media")), None)
                document.supplementary.append(
                    {"item_id": element.get("id"), "label": label or None, "href": href, "locator": locator}
                )
                build.add(
                    "supplementary",
                    f"{label} {caption}".strip(),
                    locator,
                    path,
                    kind_of_section,
                    item_id=element.get("id"),
                    item_label=label or None,
                )
    if not document.passages:
        raise ParseError("JATS article produced no text passages")
    return document


class UnsupportedTable(ValueError):
    """A table layout whose cell/header association cannot be reconstructed faithfully."""


def _span(cell: etree._Element, attribute: str) -> int:
    value = (cell.get(attribute) or "1").strip()
    if not value.isdigit() or not 1 <= int(value) <= 100:
        raise UnsupportedTable(f"invalid_{attribute}")
    return int(value)


def expand_grid(rows: list[etree._Element]) -> list[list[tuple[int, int, bool]]]:
    """Place cells into a rectangular grid honoring rowspan/colspan.

    Each slot holds (source row index, cell index within that row, carried), where `carried` marks a
    slot filled by a rowspan from an earlier row. Ragged or overlapping layouts are refused, never padded.
    """
    grid: list[list[tuple[int, int, bool]]] = []
    pending: dict[int, tuple[int, int, int]] = {}  # column -> (rows remaining, origin row, origin cell)
    for r, row in enumerate(rows):
        slots: dict[int, tuple[int, int, bool]] = {}
        carry: dict[int, tuple[int, int, int]] = {}
        for column, (remaining, origin_row, origin_cell) in pending.items():
            slots[column] = (origin_row, origin_cell, True)
            if remaining > 1:
                carry[column] = (remaining - 1, origin_row, origin_cell)
        column = 0
        for index, cell in enumerate(c for c in row if c.tag in {"td", "th"}):
            if cell.find(".//table") is not None:
                raise UnsupportedTable("nested_table")
            rowspan, colspan = _span(cell, "rowspan"), _span(cell, "colspan")
            while column in slots:
                column += 1
            for offset in range(colspan):
                if column + offset in slots:
                    raise UnsupportedTable("overlapping_spans")
                slots[column + offset] = (r, index, False)
                if rowspan > 1:
                    carry[column + offset] = (rowspan - 1, r, index)
            column += colspan
        width = max(slots) + 1 if slots else 0
        if sorted(slots) != list(range(width)):
            raise UnsupportedTable("gap_in_row_after_span_expansion")
        grid.append([slots[c] for c in range(width)])
        pending = carry
    if pending:
        raise UnsupportedTable("rowspan_extends_past_table")
    if len({len(line) for line in grid}) > 1:
        raise UnsupportedTable("ragged_rows_after_span_expansion")
    return grid


def column_headers(header_rows: list[etree._Element]) -> list[str]:
    """Per-column header path, top to bottom, e.g. "Treatment / IPF"; spans repeat a label once."""
    grid = expand_grid(header_rows)
    texts = [[element_text(c) for c in row if c.tag in {"td", "th"}] for row in header_rows]
    headers = []
    for column in range(len(grid[0]) if grid else 0):
        labels: list[str] = []
        for row, cell, _ in (line[column] for line in grid):
            label = texts[row][cell]
            if label and (not labels or labels[-1] != label):
                labels.append(label)
        headers.append(" / ".join(labels))
    return headers


def table_structure(table_wrap: etree._Element) -> tuple[str, list[str] | None, list | None]:
    """(structure status, column headers, body grid) for a JATS table-wrap."""
    header_rows = [row for head in table_wrap.iter("thead") for row in head.iter("tr")]
    body_rows = [row for row in table_wrap.iter("tr") if row not in header_rows]
    try:
        body_grid = expand_grid(body_rows) if body_rows else []
        if not header_rows:
            return "no_header", None, body_grid
        headers = column_headers(header_rows)
        if body_grid and len(body_grid[0]) != len(headers):
            raise UnsupportedTable("header_and_body_widths_differ")
        return "header_grid_expanded", headers, body_grid
    except UnsupportedTable as error:
        return f"unsupported_layout:{error}", None, None


def row_cells(body_rows: list[etree._Element], body_grid: list, r: int, headers: list[str] | None) -> list[dict]:
    texts = [[element_text(c) for c in row if c.tag in {"td", "th"}] for row in body_rows]
    cells: list[dict] = []
    previous = None
    for column, (origin_row, origin_cell, carried) in enumerate(body_grid[r]):
        if (origin_row, origin_cell) == previous:
            cells[-1]["col_span"] += 1
            continue
        previous = (origin_row, origin_cell)
        cells.append(
            {
                "text": texts[origin_row][origin_cell],
                "col_start": column,
                "col_span": 1,
                "carried_from_rowspan": carried,
                "header": None,
            }
        )
    for cell in cells:
        if headers:
            covered = headers[cell["col_start"] : cell["col_start"] + cell["col_span"]]
            cell["header"] = " + ".join(dict.fromkeys(h for h in covered if h)) or None
    return cells


def table_id(asset_sha256: str, locator: str) -> str:
    return stable_id("table", {"asset_sha256": asset_sha256, "locator": locator})


def caption_status(label: str, caption: str) -> str:
    return CAPTION_PRESENT if caption else CAPTION_LABEL_ONLY if label else CAPTION_ABSENT


def _add_table(build: _Builder, table_wrap: etree._Element, tree, path: str, kind_of_section: str) -> None:
    label = element_text(table_wrap.find("label"))
    caption = element_text(table_wrap.find("caption"))
    item = {
        "item_id": table_wrap.get("id"),
        "item_label": label or None,
        "table_id": table_id(build.document.source_asset_sha256, tree.getpath(table_wrap)),
        "table_caption_status": caption_status(label, caption),
    }
    build.add("table_caption", f"{label} {caption}".strip(), tree.getpath(table_wrap), path, kind_of_section, **item)
    header_rows = [row for head in table_wrap.iter("thead") for row in head.iter("tr")]
    body_rows = [row for row in table_wrap.iter("tr") if row not in header_rows]
    structure, headers, body_grid = table_structure(table_wrap)
    joined = " | ".join(headers) if headers else None
    for row in header_rows:
        build.add(
            "table_header",
            " | ".join(_row_cells(row)),
            tree.getpath(row),
            path,
            kind_of_section,
            table_header=joined,
            table_structure=structure,
            **item,
        )
    for r, row in enumerate(body_rows):
        # The row text stays the source cells in order; spans and headers live in `cells`.
        cells = row_cells(body_rows, body_grid, r, headers) if body_grid is not None else None
        build.add(
            "table_row",
            " | ".join(_row_cells(row)),
            tree.getpath(row),
            path,
            kind_of_section,
            table_header=joined,
            table_structure=structure,
            cells=cells,
            **item,
        )
    for footnote in table_wrap.iterfind("table-wrap-foot"):
        build.add(
            "table_footnote",
            element_text(footnote),
            tree.getpath(footnote),
            path,
            kind_of_section,
            table_structure=structure,
            **item,
        )


def parse_pubmed_abstract(publication_id: str, content: bytes, pmid: str | None = None) -> Document:
    """The record of `pmid` (or the first record) in a PubMed efetch response."""
    root = parse_xml(content)
    tree = root.getroottree()
    article = next(
        (
            a
            for a in root.iter("PubmedArticle")
            if pmid is None or (a.findtext("MedlineCitation/PMID") or "").strip() == pmid
        ),
        None,
    )
    if article is None:
        raise ParseError(f"PubMed XML contains no PubmedArticle{' for PMID ' + pmid if pmid else ''}")
    document = Document(publication_id, "pubmed_abstract", hashlib.sha256(content).hexdigest())
    build = _Builder(document)
    title = article.find("MedlineCitation/Article/ArticleTitle")
    if title is not None:
        build.add("title", element_text(title), tree.getpath(title), "Title", "title")
    for node in article.iterfind("MedlineCitation/Article/Abstract/AbstractText"):
        label = node.get("Label")
        build.add(
            "abstract",
            element_text(node),
            tree.getpath(node),
            f"Abstract > {label}" if label else "Abstract",
            "abstract",
        )
    if not document.passages:
        raise ParseError("PubMed record has neither title nor abstract text")
    return document


def parse_search_record(publication_id: str, content: bytes) -> Document:
    record = json.loads(content)
    document = Document(publication_id, "europepmc_search_record", hashlib.sha256(content).hexdigest())
    build = _Builder(document)
    build.add("title", record.get("title") or "", "search_record/title", "Title", "title")
    build.add("abstract", record.get("abstract") or "", "search_record/abstract", "Abstract", "abstract")
    if not document.passages:
        raise ParseError("search record has neither title nor abstract text")
    return document


FIGURE_REFERENCE = re.compile(r"\b(?:Fig(?:ure)?s?\.?|Figure)\s*(\d+)", re.IGNORECASE)


BIOC_SECTIONS = {
    "INTRO": "introduction",
    "METHODS": "methods",
    "RESULTS": "results",
    "DISCUSS": "discussion",
    "CONCL": "discussion",
    "ABSTRACT": "abstract",
    "TITLE": "title",
    "FIG": "other",
    "TABLE": "other",
    "SUPPL": "other",
    "CASE": "other",
    "APPENDIX": "other",
}
BIOC_SKIPPED_SECTIONS = {"REF", "AUTH_CONT", "COMP_INT", "ACK_FUND", "ABBR", "REVIEW_INFO", "KEYWORD"}


def _bioc_kind(section: str, kind: str) -> str | None:
    if kind.startswith("title") or kind.startswith("abstract_title") or kind == "fig_title_caption":
        return None  # heading-only passages; the heading is kept in section_path
    if section == "TITLE" or kind == "front":
        return "title"
    if section == "ABSTRACT":
        return "abstract"
    if kind == "fig_caption":
        return "figure_caption"
    if kind in {"table_caption", "table_title_caption"}:
        return "table_caption"
    if kind == "table":
        return "table_row"  # PubTator flattens a table's cells into one passage; no header row is exposed
    if kind == "table_footnote" or (kind == "footnote" and section == "TABLE"):
        return "table_footnote"
    if kind == "footnote":
        return "footnote"
    return "paragraph"


def parse_bioc(publication_id: str, content: bytes) -> Document:
    """PubTator3 BioC JSON full text (PMC open-access subset) as a canonical document."""
    bioc = json.loads(content)
    document = Document(
        publication_id, "pubtator_bioc", hashlib.sha256(content).hexdigest(), extra_rules={"bioc_rule": BIOC_RULE}
    )
    build = _Builder(document)
    heading: dict[str, str] = {}
    for index, passage in enumerate(bioc.get("passages", [])):
        infons = passage.get("infons") or {}
        section, kind = infons.get("section_type") or "", infons.get("type") or ""
        if section in BIOC_SKIPPED_SECTIONS:
            continue
        if kind.startswith("title") or kind.startswith("abstract_title"):
            heading[section] = normalize_text(passage.get("text") or "")
        mapped = _bioc_kind(section, kind)
        if mapped is None:
            continue
        path = " > ".join(filter(None, [section.title() or "Body", heading.get(section)]))
        build.add(
            mapped,
            passage.get("text") or "",
            f"bioc/passages[{index}]@offset={passage.get('offset')}",
            path,
            BIOC_SECTIONS.get(section, "other"),
            item_id=infons.get("id"),
            # PubTator flattens tables; column semantics are not recoverable from BioC. Passages of one
            # table share a BioC id; an id-less table passage stays its own table.
            **(
                {
                    "table_structure": "flattened_bioc_no_cell_structure",
                    "table_id": table_id(
                        document.source_asset_sha256,
                        f"bioc/table@id={infons['id']}" if infons.get("id") else f"bioc/passages[{index}]",
                    ),
                }
                if mapped.startswith("table_")
                else {}
            ),
        )
    captioned = {p.table_id for p in document.passages if p.kind == "table_caption"}
    for passage in document.passages:
        if passage.table_id:
            passage.table_caption_status = CAPTION_PRESENT if passage.table_id in captioned else CAPTION_ABSENT
    if not any(p.kind not in {"title", "abstract"} for p in document.passages):
        raise ParseError("BioC document has no body text beyond title/abstract")
    return document
