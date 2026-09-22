"""Publication identity across PubMed and Europe PMC, and deterministic live-corpus selection.

Identifiers are merged only when one source record states them together (e.g. a PubMed record
listing its PMCID and DOI). Similar titles are never evidence of identity, so a preprint and its
journal version remain separate unless a record links them explicitly.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field

from regkg.literature.search import SourceRecord
from regkg.provenance import stable_id

DOI_PREFIXES = ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/", "doi:")
RETRACTION_TYPES = {"retractionin", "retraction in", "retractedandrepublishedin"}


def normalize_doi(value: str | None) -> str | None:
    if not value:
        return None
    doi = value.strip()
    lowered = doi.lower()
    for prefix in DOI_PREFIXES:
        if lowered.startswith(prefix):
            doi = doi[len(prefix) :]
            break
    doi = doi.strip().lower()  # DOIs are case-insensitive by specification
    return doi if doi.startswith("10.") else None


def normalize_pmcid(value: str | None) -> str | None:
    if not value:
        return None
    digits = value.strip().upper().removeprefix("PMC")
    return f"PMC{digits}" if digits.isdigit() else None


def normalize_pmid(value: str | None) -> str | None:
    value = (value or "").strip()
    return value if value.isdigit() and not value.startswith("0") else None


def record_identifiers(record: SourceRecord) -> dict[str, str]:
    found = {
        "pmid": normalize_pmid(record.pmid),
        "pmcid": normalize_pmcid(record.pmcid),
        "doi": normalize_doi(record.doi),
        "epmc": record.epmc_id,
    }
    return {kind: value for kind, value in found.items() if value}


def publication_id(ids: dict[str, str]) -> str:
    # Same identity rule as P2 seed publications: a PMID alone when present.
    for kind in ("pmid", "pmcid", "doi", "epmc"):
        if kind in ids:
            return stable_id("publication", {kind: ids[kind]})
    raise ValueError("record has no usable identifier")


@dataclass
class Publication:
    publication_id: str
    identifiers: dict[str, str]
    records: list[tuple[str, SourceRecord]] = field(default_factory=list)  # (membership label, record)
    identity_conflict: list[str] = field(default_factory=list)

    def best(self, attribute: str):
        """PubMed metadata first, then Europe PMC; never mixes fields within one value."""
        ordered = sorted(self.records, key=lambda item: 0 if item[1].source == "pubmed" else 1)
        for _, record in ordered:
            value = getattr(record, attribute)
            if value not in (None, "", []):
                return value
        return None

    @property
    def retracted(self) -> bool:
        return any(c.get("type", "").lower() in RETRACTION_TYPES for _, r in self.records for c in r.corrections)

    @property
    def is_preprint(self) -> bool:
        return any(r.is_preprint for _, r in self.records)


def resolve_publications(records: list[tuple[str, SourceRecord]]) -> list[Publication]:
    """Union identifiers co-stated by a record. Components claiming two PMIDs (or PMCIDs) are not merged."""
    parent: dict[str, str] = {}

    def find(node: str) -> str:
        while parent.setdefault(node, node) != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    keyed = []
    for label, record in records:
        ids = record_identifiers(record)
        if not ids:
            continue
        nodes = [f"{k}:{v}" for k, v in sorted(ids.items())]
        for node in nodes[1:]:
            parent[find(node)] = find(nodes[0])
        keyed.append((label, record, ids, nodes[0]))

    components: dict[str, list] = defaultdict(list)
    for item in keyed:
        components[find(item[3])].append(item)
    publications: dict[str, Publication] = {}
    for items in components.values():
        pmids = {i[2]["pmid"] for i in items if "pmid" in i[2]}
        pmcids = {i[2]["pmcid"] for i in items if "pmcid" in i[2]}
        conflict = []
        if len(pmids) > 1:
            conflict.append(f"multiple PMIDs {sorted(pmids)}")
        if len(pmcids) > 1:
            conflict.append(f"multiple PMCIDs {sorted(pmcids)}")
        groups = [[item] for item in items] if conflict else [items]
        for group in groups:
            merged: dict[str, str] = {}
            for _, _, ids, _ in group:
                for kind, value in ids.items():
                    merged.setdefault(kind, value)
            pid = publication_id(merged)
            publication = publications.setdefault(pid, Publication(pid, merged, identity_conflict=conflict))
            for kind, value in merged.items():
                publication.identifiers.setdefault(kind, value)
            publication.records.extend((label, record) for label, record, _, _ in group)
    return sorted(publications.values(), key=lambda p: p.publication_id)


# ---------------------------------------------------------------------------
# Corpus selection


def term_pattern(term: str) -> re.Pattern:
    # Gene symbols are matched case-sensitively as whole tokens (hyphens/digits count as token parts).
    return re.compile(rf"(?<![A-Za-z0-9-]){re.escape(term)}(?![A-Za-z0-9-])")


def any_term(text: str, terms: list[str], case_sensitive: bool = True) -> bool:
    if case_sensitive:
        return any(term_pattern(term).search(text) for term in terms)
    lowered = text.lower()
    return any(term_pattern(term.lower()).search(lowered) for term in terms)


@dataclass
class SelectionFeatures:
    publication_id: str
    tf_hgnc_ids: list[str]
    tf_in_title_ids: list[str]
    target_hgnc_ids: list[str]
    query_hits: int
    context_in_title: bool
    context_hit: bool
    assay_hit: bool
    advisor_seed: bool
    is_preprint: bool
    retracted: bool
    has_abstract: bool
    eligible: bool
    exclusion_reason: str | None

    def sort_key(self, pmid: str | None) -> tuple:
        # Selection rule p3-selection-3: title-level lung context and a candidate TF named in the
        # title outrank abstract-only mentions; context outranks a target mention, so an off-tissue
        # paper naming TF and target cannot displace a lung paper about the TF.
        return (
            -int(self.context_in_title),
            -int(bool(self.tf_in_title_ids)),
            -int(self.context_hit),
            -int(bool(self.target_hgnc_ids)),
            -int(self.assay_hit),
            -len(self.tf_hgnc_ids),
            -self.query_hits,
            -int(self.advisor_seed),
            int(self.is_preprint),
            int(pmid) if pmid else 10**12,
            self.publication_id,
        )


def selection_features(
    publication: Publication,
    tf_names: dict[str, list[str]],
    target_names: dict[str, list[str]],
    context_terms: list[str],
    assay_terms: list[str],
    advisor_pmids: set[str],
) -> SelectionFeatures:
    title = publication.best("title") or ""
    text = f"{title} {publication.best('abstract') or ''}"
    tfs = sorted(h for h, names in tf_names.items() if any_term(text, names))
    tfs_in_title = sorted(h for h, names in tf_names.items() if any_term(title, names))
    targets = sorted(h for h, names in target_names.items() if any_term(text, names))
    queries = {label for label, _ in publication.records if not label.startswith("advisor_seed")}
    reason = None
    if publication.retracted:
        reason = "retracted"
    elif not tfs:
        reason = "no_exact_candidate_tf_mention_in_title_or_abstract"
    return SelectionFeatures(
        publication_id=publication.publication_id,
        tf_hgnc_ids=tfs,
        tf_in_title_ids=tfs_in_title,
        target_hgnc_ids=targets,
        query_hits=len(queries),
        context_in_title=any_term(title, context_terms, case_sensitive=False),
        context_hit=any_term(text, context_terms, case_sensitive=False),
        assay_hit=any_term(text, assay_terms, case_sensitive=False),
        advisor_seed=publication.identifiers.get("pmid") in advisor_pmids,
        is_preprint=publication.is_preprint,
        retracted=publication.retracted,
        has_abstract=bool(publication.best("abstract")),
        eligible=reason is None,
        exclusion_reason=reason,
    )


def select_corpus(
    features: list[SelectionFeatures], pmids: dict[str, str | None], seed_tfs: list[str], max_papers: int
) -> list[tuple[str, str]]:
    """(publication_id, reason) in selection order.

    First, for each manuscript seed TF in HGNC-ID order, the best eligible paper mentioning it,
    preferring papers naming that TF in the title (coverage); then remaining slots by the same
    deterministic ordering (PMID breaks ties).
    """
    eligible = sorted((f for f in features if f.eligible), key=lambda f: f.sort_key(pmids.get(f.publication_id)))
    chosen: list[tuple[str, str]] = []
    taken: set[str] = set()
    for tf in sorted(seed_tfs):
        if len(chosen) >= max_papers:
            break
        options = [f for f in eligible if tf in f.tf_hgnc_ids and f.publication_id not in taken]
        options.sort(key=lambda f: (tf not in f.tf_in_title_ids, f.sort_key(pmids.get(f.publication_id))))
        match = options[0] if options else None
        if match:
            chosen.append((match.publication_id, f"seed_tf_coverage:{tf}"))
            taken.add(match.publication_id)
    for feature in eligible:
        if len(chosen) >= max_papers:
            break
        if feature.publication_id not in taken:
            chosen.append((feature.publication_id, "ranked_relevance"))
            taken.add(feature.publication_id)
    return chosen
