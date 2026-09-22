"""Bounded biomedical literature search for the AT1 candidate retrieval queue.

Adapted from reference/literature_search_tool.py (sha256 eb3f7f74...). Retained: source labels,
bounded result validation, upstream-failure classification, coverage warnings, and publication
identifier parsing (now in fetch.py). Removed: agent/tool framing, the MedCPT reranker, and the
unavailable `lungchat` engine, trace, TLS, and payload modules. The PubMed and Europe PMC source
adapters below are implemented here against their public APIs; the original engine was not
available and is not reused. Papers are returned as structured records; ranking of passages
happens later (exact identifiers, BM25, selected embeddings).

No date, publication-type, or species filter is applied: those controls were not implemented and
tested per source, and the plan forbids imposing a default window or MeSH-only species restriction.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field

import httpx

from regkg.literature.http import SERVICES, SourceClient, SourceError
from regkg.literature.xml import element_text, parse_xml

MIN_RESULTS = 1
MAX_RESULTS = 10

_SOURCE_LABELS = {"pubmed": "PubMed", "europepmc": "Europe PMC", "pubtator": "PubTator"}
_UPSTREAM_FAILURES = {"timeout", "request_failed", "server_error", "rate_limited", "http_error", "malformed_response"}

# Retrieval statuses; an empty or failed search is never evidence that literature does not exist.
STATUS_SUCCESS = "success"
STATUS_PARTIAL = "partial"  # at least one source failed, others answered
STATUS_EMPTY = "empty"  # every source answered with zero results
STATUS_FAILED = "failed"  # no source answered


@dataclass
class QuerySpec:
    query_id: str
    tf_terms: list[str]
    target_terms: list[str]
    qualifiers: list[str]

    @classmethod
    def from_queue_row(cls, query_id: str, terms_json: str) -> QuerySpec:
        terms = json.loads(terms_json)
        return cls(query_id, list(terms["tf"]), list(terms.get("target") or []), list(terms["qualifiers"]))

    def groups(self) -> list[list[str]]:
        return [group for group in (self.tf_terms, self.target_terms, self.qualifiers) if group]


@dataclass
class SourceRecord:
    source: str
    rank: int
    cache_key: str
    pmid: str | None = None
    pmcid: str | None = None
    doi: str | None = None
    epmc_id: str | None = None
    title: str = ""
    abstract: str = ""
    journal: str | None = None
    year: int | None = None
    publication_types: list[str] = field(default_factory=list)
    mesh_terms: list[str] = field(default_factory=list)
    is_preprint: bool = False
    is_open_access: bool | None = None
    in_pmc: bool | None = None
    license: str | None = None
    corrections: list[dict] = field(default_factory=list)


@dataclass
class SourceOutcome:
    source: str
    status: str  # answered | failed
    hit_count: int | None
    returned: int
    error_kind: str | None = None
    error_detail: str | None = None


@dataclass
class SearchResult:
    query_id: str
    status: str
    outcomes: list[SourceOutcome]
    records: list[SourceRecord]
    warnings: list[str]
    translations: dict[str, str]

    def to_json(self) -> dict:
        return asdict(self)


def coverage_warning(source: str) -> str:
    label = _SOURCE_LABELS.get(source) or "A literature source"
    return f"{label} was unavailable; coverage may be reduced."


def validate_limit(max_results: int) -> int:
    if not MIN_RESULTS <= max_results <= MAX_RESULTS:
        raise ValueError(f"max_results must be between {MIN_RESULTS} and {MAX_RESULTS}; got {max_results}")
    return max_results


def _quote(term: str) -> str:
    return '"' + term.replace('"', "") + '"'


def translate_query(spec: QuerySpec, source: str) -> str:
    """P2's service-neutral groups: PubMed restricts phrases to title/abstract; Europe PMC uses its
    default fields (which include open-access full text)."""
    if source == "pubmed":
        return " AND ".join("(" + " OR ".join(f"{_quote(t)}[tiab]" for t in group) + ")" for group in spec.groups())
    return " AND ".join("(" + " OR ".join(_quote(t) for t in group) + ")" for group in spec.groups())


def _year(text: str | None) -> int | None:
    digits = "".join(ch for ch in (text or "")[:4] if ch.isdigit())
    return int(digits) if len(digits) == 4 else None


def parse_pubmed_xml(content: bytes, cache_key: str) -> list[SourceRecord]:
    """PubmedArticle records from an efetch XML response."""
    records = []
    for article in parse_xml(content).iter("PubmedArticle"):
        citation = article.find("MedlineCitation")
        ids = {
            node.get("IdType"): (node.text or "").strip()
            for node in article.iterfind("PubmedData/ArticleIdList/ArticleId")
        }
        parts = []
        for node in citation.iterfind("Article/Abstract/AbstractText"):
            label = node.get("Label")
            parts.append((f"{label}: " if label else "") + element_text(node))
        date = citation.find("Article/Journal/JournalIssue/PubDate")
        year = None
        if date is not None:
            year = _year(date.findtext("Year")) or _year(date.findtext("MedlineDate"))
        types = [element_text(n) for n in citation.iterfind("Article/PublicationTypeList/PublicationType")]
        corrections = [
            {
                "type": node.get("RefType"),
                "ref_source": element_text(node.find("RefSource")),
                "pmid": (node.findtext("PMID") or "").strip() or None,
            }
            for node in citation.iterfind("CommentsCorrectionsList/CommentsCorrections")
            if node.get("RefType")
            in {
                "RetractionIn",
                "RetractionOf",
                "ErratumIn",
                "ErratumFor",
                "ExpressionOfConcernIn",
                "UpdateIn",
                "CorrectedandRepublishedIn",
                "RetractedandRepublishedIn",
            }
        ]
        records.append(
            SourceRecord(
                source="pubmed",
                rank=0,
                cache_key=cache_key,
                pmid=(citation.findtext("PMID") or "").strip() or None,
                pmcid=ids.get("pmc") or None,
                doi=ids.get("doi") or None,
                title=element_text(citation.find("Article/ArticleTitle")),
                abstract=" ".join(parts),
                journal=element_text(citation.find("Article/Journal/Title")) or None,
                year=year,
                publication_types=types,
                mesh_terms=[element_text(n) for n in citation.iterfind("MeshHeadingList/MeshHeading/DescriptorName")],
                is_preprint="Preprint" in types,
                corrections=corrections,
            )
        )
    return records


def _require_json_keys(*keys: str):
    def check(response: httpx.Response) -> None:
        body = response.json()
        missing = [key for key in keys if key not in body]
        if missing:
            # Europe PMC intermittently answers HTTP 200 with only {"version": ...}; that is a failed
            # request, not an empty result.
            raise ValueError(f"response lacks {missing}")

    return check


def _pubmed_esearch_check(response: httpx.Response) -> None:
    body = response.json()
    result = body.get("esearchresult")
    if result is None or "idlist" not in result or "count" not in result or "ERROR" in result:
        raise ValueError("esearch response lacks esearchresult/idlist/count")


def search_pubmed(client: SourceClient, spec: QuerySpec, max_results: int) -> tuple[SourceOutcome, list[SourceRecord]]:
    term = translate_query(spec, "pubmed")
    response = client.get(
        "pubmed",
        "esearch.fcgi",
        {"db": "pubmed", "term": term, "retmax": str(max_results), "sort": "relevance", "retmode": "json"},
        validate=_pubmed_esearch_check,
    )
    result = response.json()["esearchresult"]
    pmids = [str(pmid) for pmid in result["idlist"]][:max_results]
    records: list[SourceRecord] = []
    if pmids:
        details = client.get(
            "pubmed",
            "efetch.fcgi",
            {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"},
            validate=lambda r: parse_xml(r.content),
        )
        by_pmid = {record.pmid: record for record in parse_pubmed_xml(details.body, details.cache_key)}
        for rank, pmid in enumerate(pmids, start=1):
            record = by_pmid.get(pmid) or SourceRecord("pubmed", rank, details.cache_key, pmid=pmid)
            record.rank = rank
            records.append(record)
    return SourceOutcome("pubmed", "answered", int(result["count"]), len(records)), records


def _epmc_record(item: dict, rank: int, cache_key: str) -> SourceRecord:
    types = list((item.get("pubTypeList") or {}).get("pubType") or [])
    corrections = [
        {
            "type": c.get("type"),
            "ref_source": c.get("source"),
            "pmid": c.get("id") if c.get("source") == "MED" else None,
        }
        for c in (item.get("commentCorrectionList") or {}).get("commentCorrection") or []
    ]
    flag = {"Y": True, "N": False}
    return SourceRecord(
        source="europepmc",
        rank=rank,
        cache_key=cache_key,
        pmid=item.get("pmid") or None,
        pmcid=item.get("pmcid") or None,
        doi=item.get("doi") or None,
        epmc_id=f"{item.get('source')}:{item.get('id')}",
        title=" ".join((item.get("title") or "").split()),
        abstract=" ".join((item.get("abstractText") or "").split()),
        journal=((item.get("journalInfo") or {}).get("journal") or {}).get("title"),
        year=_year(item.get("pubYear")),
        publication_types=types,
        is_preprint=item.get("source") == "PPR" or "Preprint" in types or "preprint" in types,
        is_open_access=flag.get(item.get("isOpenAccess")),
        in_pmc=flag.get(item.get("inPMC")),
        license=item.get("license"),
        corrections=corrections,
    )


def search_europepmc(
    client: SourceClient, spec: QuerySpec, max_results: int
) -> tuple[SourceOutcome, list[SourceRecord]]:
    query = translate_query(spec, "europepmc")
    response = client.get(
        "europepmc",
        "search",
        {"query": query, "format": "json", "resultType": "core", "pageSize": str(max_results), "cursorMark": "*"},
        validate=_require_json_keys("hitCount", "resultList"),
    )
    body = response.json()
    items = body["resultList"].get("result", [])[:max_results]
    records = [_epmc_record(item, rank, response.cache_key) for rank, item in enumerate(items, start=1)]
    return SourceOutcome("europepmc", "answered", int(body["hitCount"]), len(records)), records


ADAPTERS = {"pubmed": search_pubmed, "europepmc": search_europepmc}


def search_papers(spec: QuerySpec, client: SourceClient, sources: list[str], max_results: int) -> SearchResult:
    """Run one queued query against each source; partial and failed coverage stay explicit."""
    validate_limit(max_results)
    unknown = [s for s in sources if s not in ADAPTERS or s not in SERVICES]
    if unknown:
        raise ValueError(f"unsupported literature sources {unknown}")
    outcomes, records, warnings = [], [], []
    for source in sources:
        try:
            outcome, found = ADAPTERS[source](client, spec, max_results)
        except SourceError as error:
            outcome, found = SourceOutcome(source, "failed", None, 0, error.kind, error.detail), []
            if error.kind in _UPSTREAM_FAILURES or error.kind == "not_found":
                warnings.append(coverage_warning(source))
        outcomes.append(outcome)
        records.extend(found)
    answered = [o for o in outcomes if o.status == "answered"]
    if not answered:
        status = STATUS_FAILED
    elif len(answered) < len(outcomes):
        status = STATUS_PARTIAL
    elif not records:
        status = STATUS_EMPTY
    else:
        status = STATUS_SUCCESS
    # Unlike the reference's non-success branch, warnings are kept for every status.
    return SearchResult(
        spec.query_id,
        status,
        outcomes,
        records,
        sorted(set(warnings)),
        {source: translate_query(spec, source) for source in sources},
    )
