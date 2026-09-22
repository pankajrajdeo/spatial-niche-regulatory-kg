"""Secure XML parsing and text helpers shared by literature search and document parsing."""

from __future__ import annotations

import unicodedata

from lxml import etree


class UnsafeXMLError(ValueError):
    """The document declares a DTD or entities; literature XML is parsed without them."""


def secure_parser() -> etree.XMLParser:
    # No entity expansion, no DTD loading, no network access, no huge-tree allowance.
    return etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        load_dtd=False,
        dtd_validation=False,
        huge_tree=False,
        remove_comments=True,
    )


def parse_xml(content: bytes) -> etree._Element:
    root = etree.fromstring(content, parser=secure_parser())
    doctype = root.getroottree().docinfo
    if doctype.internalDTD is not None and list(doctype.internalDTD.iterentities()):
        raise UnsafeXMLError("XML declares internal entities; refusing to expand them")
    return root


def normalize_text(text: str) -> str:
    """Unicode NFC, then all whitespace runs -> one space (part of rule ws-collapse-nfc-block-space-2)."""
    return " ".join(unicodedata.normalize("NFC", text).split())


# Block-level JATS/PubMed elements: a boundary between them is a word boundary, so they are
# separated by a space (itertext() would glue "...fibrosis.</title><p>a, b" into "fibrosis.a, b").
BLOCK_TAGS = frozenset(
    {
        "title",
        "p",
        "label",
        "caption",
        "list-item",
        "list",
        "sec",
        "def-item",
        "term",
        "def",
        "td",
        "th",
        "tr",
        "disp-quote",
        "statement",
        "AbstractText",
        # A JATS <break/> separates words ("Gene<break/>TF Rank"); gluing them changed header meaning.
        "break",
    }
)
# Floats nested inside a paragraph are separate passages; their text is not repeated in the paragraph.
FLOAT_TAGS = frozenset({"fig", "table-wrap", "supplementary-material", "fig-group", "table-wrap-group"})


def element_text(element: etree._Element | None, skip: frozenset[str] = frozenset()) -> str:
    """Element text with block boundaries spaced and `skip` subtrees omitted (ws-collapse-nfc-block-space-3)."""
    if element is None:
        return ""
    parts: list[str] = []

    def walk(node: etree._Element) -> None:
        parts.append(node.text or "")
        for child in node:
            if isinstance(child.tag, str) and child.tag not in skip:
                block = child.tag in BLOCK_TAGS
                parts.append(" " if block else "")
                walk(child)
                parts.append(" " if block else "")
            parts.append(child.tail or "")

    walk(element)
    return normalize_text("".join(parts))
