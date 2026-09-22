"""Gene mentions in canonical passages: candidate-name retrieval hits and PubTator source identifiers.

Two different things are recorded and never conflated (rule `p3-mentions-3`):

- An exact candidate-name hit is retrieval association with a human P2 candidate. It carries
  `candidate_hgnc_id` as a hint only; the passage may describe a mouse gene, so the hit
  establishes neither species nor a resolved entity (`hgnc_id` is always null).
- A PubTator annotation carries a species-specific NCBI Gene ID. It resolves to an HGNC ID only
  when the HGNC snapshot maps that NCBI ID to exactly one human gene; other IDs (e.g. mouse
  orthologs) stay unresolved with the raw ID and are never mapped onto human genes.

Overlapping records are reconciled into an explicit identity status, so a name hit on a span that
PubTator identifies as a mouse gene is visibly conflicting rather than silently "human".
PubTator offsets refer to PubTator's text version: an annotation is first checked against its own
text at its own offsets, then attached to canonical text only where the exact mention is found.
"""

from __future__ import annotations

import bisect
from dataclasses import asdict, dataclass, field

from regkg.literature.parse import Document
from regkg.literature.publications import term_pattern
from regkg.literature.xml import normalize_text
from regkg.provenance import stable_id

MENTION_RULE = "p3-mentions-3"
ALIGN_EXACT = "aligned_exact"  # same passage text; mention found at the expected position
ALIGN_REMATCHED = "rematched_in_passage"  # passage found; mention text found at a different position
ALIGN_CONTEXT = "rematched_by_context"  # mention and its surrounding text found once in canonical text
ALIGN_UNIQUE = "rematched_unique_in_document"  # the mention string occurs exactly once in the document
ALIGN_UNALIGNED = "unaligned_text_version_differs"  # external offsets kept; no canonical span attached
ALIGN_EXTERNAL_MISMATCH = "external_offsets_inconsistent"  # annotation text differs from its own source slice

# Resolution of the biological entity a record refers to.
CANDIDATE_HINT = "candidate_name_match_species_unknown"
RESOLVED_HUMAN = "resolved_ncbi_gene_human"
UNRESOLVED = "unresolved_non_human_or_unmapped"
AMBIGUOUS = "ambiguous"
NOT_ATTACHED = "not_attached_external_offset_mismatch"

# Identity status after reconciling overlapping records on the same canonical span.
HINT_ONLY = "candidate_hint_only"  # no source identifier covers this name hit
CONSISTENT = "consistent_with_source_identifier"  # PubTator resolves the span to the same human gene
CONFLICTING = "conflicting_source_identifier"  # PubTator names another, non-human, or ambiguous entity
SOURCE_IDENTIFIER = "source_identifier"
NOT_ATTACHED_STATUS = "not_attached"
NOT_ASSESSED = "not_assessed_external_offset_mismatch"


@dataclass
class Mention:
    mention_id: str
    publication_id: str
    passage_id: str | None
    start: int | None  # canonical offsets; None when not attached
    end: int | None
    text: str
    source: str  # exact_candidate_name | pubtator
    entity_type: str
    candidate_hgnc_id: str | None  # retrieval hint (exact-name hits only)
    hgnc_id: str | None  # resolved human entity identity (source identifiers only)
    resolution: str
    species_taxon: str | None  # "9606" only when a source identifier maps to one human gene
    species_evidence: str
    external_identifier: str | None
    external_offset: int | None
    external_length: int | None
    alignment: str | None
    identity_status: str
    linked_mention_ids: list[str] = field(default_factory=list)
    rule_version: str = MENTION_RULE

    def to_json(self) -> dict:
        return asdict(self)


def candidate_name_mentions(document: Document, names: dict[str, list[str]]) -> list[Mention]:
    mentions = []
    for passage in document.passages:
        for hgnc_id, terms in sorted(names.items()):
            for term in terms:
                for match in term_pattern(term).finditer(passage.text):
                    start = passage.start + match.start()
                    mentions.append(
                        Mention(
                            stable_id(
                                "mention",
                                {"passage": passage.passage_id, "start": start, "term": term, "rule": MENTION_RULE},
                            ),
                            document.publication_id,
                            passage.passage_id,
                            start,
                            start + len(term),
                            term,
                            "exact_candidate_name",
                            "Gene",
                            candidate_hgnc_id=hgnc_id,
                            hgnc_id=None,
                            resolution=CANDIDATE_HINT,
                            species_taxon=None,
                            species_evidence="unknown_name_match_only",
                            external_identifier=None,
                            external_offset=None,
                            external_length=None,
                            alignment=ALIGN_EXACT,
                            identity_status=HINT_ONLY,
                        )
                    )
    return mentions


def _locate(document: Document, text: str) -> tuple[object | None, int | None]:
    for passage in document.passages:
        position = passage.text.find(text)
        if position >= 0:
            return passage, passage.start + position
    return None, None


def _align(
    canonical: str, external_text: str, relative: int, mention: str, passage, passage_start
) -> tuple[int | None, str]:
    """Canonical start for one external mention, verified as exact text, and how it was found."""
    if passage is not None:
        expected = passage_start + len(normalize_text(external_text[:relative]))
        expected += 1 if relative and external_text[:relative][-1:].isspace() else 0
        if canonical[expected : expected + len(mention)] == mention:
            return expected, ALIGN_EXACT
    left_source = normalize_text(external_text[:relative])
    right_source = normalize_text(external_text[relative + len(mention) :])
    for width in (40, 20, 10):
        left = left_source[-width:]
        right = right_source[:width]
        needle = (
            f"{left} {mention} {right}" if left and right else f"{left} {mention}" if left else f"{mention} {right}"
        )
        if canonical.count(needle) == 1:
            start = canonical.index(needle) + (len(left) + 1 if left else 0)
            if canonical[start : start + len(mention)] == mention:
                return start, ALIGN_CONTEXT
    if passage is not None and passage.text.count(mention) == 1:
        return passage.start + passage.text.index(mention), ALIGN_REMATCHED
    if canonical.count(mention) == 1:
        return canonical.index(mention), ALIGN_UNIQUE
    return None, ALIGN_UNALIGNED


def source_identity(
    identifier: str | None, human_gene_of_ncbi: dict[str, str]
) -> tuple[str, str | None, str | None, str]:
    """(resolution, hgnc_id, species_taxon, species_evidence) for one PubTator gene identifier."""
    ids = [part for part in (identifier or "").replace(",", ";").split(";") if part]
    if len(ids) > 1:
        return AMBIGUOUS, None, None, "multiple_ncbi_gene_ids"
    if ids and ids[0] in human_gene_of_ncbi:
        return RESOLVED_HUMAN, human_gene_of_ncbi[ids[0]], "9606", "ncbi_gene_id_maps_to_one_human_hgnc_gene"
    if ids:
        # Not a human gene in the snapshot (e.g. a mouse ortholog). Its species is not asserted
        # and it is never mapped onto a human gene.
        return UNRESOLVED, None, None, "ncbi_gene_id_not_in_human_hgnc_map"
    return UNRESOLVED, None, None, "no_identifier"


def pubtator_mentions(document: Document, pubtator: dict, human_gene_of_ncbi: dict[str, str]) -> list[Mention]:
    canonical = document.canonical_text
    starts = [p.start for p in document.passages]
    mentions = []
    for bioc in pubtator.get("passages", []):
        external_text = bioc.get("text") or ""
        base = int(bioc.get("offset") or 0)
        normalized = normalize_text(external_text)
        passage, passage_start = _locate(document, normalized) if normalized else (None, None)
        for annotation in bioc.get("annotations", []):
            infons = annotation.get("infons") or {}
            if infons.get("type") != "Gene":
                continue
            identifier = str(infons.get("identifier") or "") or None
            resolution, hgnc_id, taxon, evidence = source_identity(identifier, human_gene_of_ncbi)
            for location in annotation.get("locations", []):
                offset, length = int(location["offset"]), int(location["length"])
                relative = offset - base
                source_slice = external_text[relative : relative + length] if relative >= 0 else ""
                start = end = passage_id = None
                if not source_slice or source_slice != (annotation.get("text") or ""):
                    # The annotation disagrees with its own source location: attach nothing to it.
                    text, alignment = annotation.get("text") or "", ALIGN_EXTERNAL_MISMATCH
                    record = (NOT_ATTACHED, None, None, NOT_ATTACHED_STATUS, NOT_ASSESSED)
                else:
                    text = normalize_text(source_slice)
                    start, alignment = _align(canonical, external_text, relative, text, passage, passage_start)
                    record = (resolution, hgnc_id, taxon, SOURCE_IDENTIFIER, evidence)
                    if start is not None:
                        end = start + len(text)
                        owner = document.passages[bisect.bisect_right(starts, start) - 1]
                        passage_id = owner.passage_id if end <= owner.end else None
                        if passage_id is None:
                            start, end, alignment = None, None, ALIGN_UNALIGNED  # would straddle two passages
                mentions.append(
                    Mention(
                        stable_id(
                            "mention",
                            {
                                "publication": document.publication_id,
                                "pubtator": annotation.get("id"),
                                "offset": offset,
                                "rule": MENTION_RULE,
                            },
                        ),
                        document.publication_id,
                        passage_id,
                        start,
                        end,
                        text,
                        "pubtator",
                        "Gene",
                        candidate_hgnc_id=None,
                        hgnc_id=record[1],
                        resolution=record[0],
                        species_taxon=record[2],
                        species_evidence=record[4],
                        external_identifier=identifier,
                        external_offset=offset,
                        external_length=length,
                        alignment=alignment,
                        identity_status=record[3],
                    )
                )
    return mentions


def reconcile(mentions: list[Mention]) -> list[Mention]:
    """Link each candidate-name hit to PubTator records on overlapping canonical spans."""
    by_passage: dict[str, list[Mention]] = {}
    for mention in mentions:
        if mention.source == "pubtator" and mention.start is not None:
            by_passage.setdefault(mention.passage_id, []).append(mention)
    for mention in mentions:
        if mention.source != "exact_candidate_name":
            continue
        overlapping = [
            m for m in by_passage.get(mention.passage_id, []) if m.start < mention.end and mention.start < m.end
        ]
        mention.linked_mention_ids = sorted(m.mention_id for m in overlapping)
        if not overlapping:
            mention.identity_status = HINT_ONLY
        elif all(m.resolution == RESOLVED_HUMAN and m.hgnc_id == mention.candidate_hgnc_id for m in overlapping):
            mention.identity_status = CONSISTENT
        else:
            mention.identity_status = CONFLICTING
        for other in overlapping:
            other.linked_mention_ids = sorted(set(other.linked_mention_ids) | {mention.mention_id})
    return mentions
