"""Full-text availability audit and acquisition for a batch of publications (at most ten).

Routes, in order of preference: Europe PMC open-access JATS, the PMC Open Access dataset
(NCBI's AWS Open Data copy: metadata with license/retraction flags and MD5s, JATS, the publisher
PDF, and supplements), and PubTator's BioC rendering of open-access text. Only open-access
content is downloaded; everything else gets verified landing links for a manual download.
Returned links are recorded as given; no PDF URL is constructed or guessed, and no login or
proxy route is used. Failures are classified per paper and never read as "unavailable".
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path, PurePosixPath

from regkg.literature.fetch import (
    Asset,
    fetch_full_text,
    fetch_pubtator,
    jats_license,
    pubtator_full_text_license,
    store_asset,
)
from regkg.literature.http import NotFound, SourceClient, SourceError
from regkg.literature.parse import ParseError, parse_jats
from regkg.literature.publications import normalize_doi, normalize_pmcid
from regkg.literature.search import SourceRecord, _epmc_record, _require_json_keys, parse_pubmed_xml
from regkg.literature.xml import parse_xml
from regkg.provenance import utc_now

S3_NS = "{http://s3.amazonaws.com/doc/2006-03-01/}"
FIGURE_EXTENSIONS = {".jpg", ".jpeg", ".gif", ".png", ".tif", ".tiff"}
RETRACTED_TYPES = {"retracted publication", "retraction of publication"}


@dataclass
class Link:
    kind: str  # pubmed | pmc | doi | returned_full_text
    url: str
    availability: str | None  # as returned by the source (e.g. "Open access", "Free", "Subscription required")
    document_style: str | None  # html | pdf | doi, as returned
    site: str | None
    discovery_source: str  # identifier_resolver | europepmc_fullTextUrlList | pmc_oa_dataset
    discovered_at: str


@dataclass
class SupplementItem:
    filename: str
    label: str | None  # from the article's JATS inventory when present
    jats_item_id: str | None
    size: int | None
    md5: str | None
    url: str | None
    # acquired | size_limit_deferred | unsupported_extension_inventoried | fetch_failed:<kind> |
    # not_in_oa_dataset | md5_mismatch | not_requested
    state: str
    asset: dict | None = None


@dataclass
class PaperAcquisition:
    publication_id: str
    pmid: str
    pmcid: str | None = None
    doi: str | None = None
    title: str | None = None
    abstract: str | None = None
    year: int | None = None
    journal: str | None = None
    publication_types: list[str] = field(default_factory=list)
    mesh_terms: list[str] = field(default_factory=list)
    corrections: list[dict] = field(default_factory=list)
    retracted: bool = False
    pubmed_status: str = "not_checked"  # fetched | not_found | failed:<kind>
    europepmc_status: str = "not_checked"  # found | not_indexed | failed:<kind>
    is_open_access: bool | None = None
    in_pmc: bool | None = None
    has_pdf: bool | None = None
    has_supplements: bool | None = None
    license: str | None = None
    oa_dataset_version: str | None = None
    oa_dataset_status: str = "not_checked"  # present | absent | failed:<kind> | no_pmcid
    oa_metadata: dict | None = None
    full_text_route: str | None = None  # europepmc_jats | pmc_oa_dataset_jats | pubtator_bioc
    full_text_status: str = "not_checked"
    pubtator_status: str = "not_checked"
    bioc_full_text: bool = False  # PubTator carries licensed open-access body text for this PMID
    identity_issues: list[str] = field(default_factory=list)
    links: list[dict] = field(default_factory=list)
    assets: list[dict] = field(default_factory=list)
    supplements: list[dict] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    checked_sources: list[str] = field(default_factory=list)
    checked_at: str = ""

    def to_json(self) -> dict:
        return asdict(self)


def _asset(asset: Asset) -> dict:
    return asdict(asset)


def pubmed_batch(client: SourceClient, pmids: list[str]) -> dict[str, tuple[SourceRecord, bytes, str]]:
    response = client.get(
        "pubmed",
        "efetch.fcgi",
        {"db": "pubmed", "id": ",".join(sorted(pmids, key=int)), "retmode": "xml"},
        validate=lambda r: parse_xml(r.content),
    )
    records = {r.pmid: r for r in parse_pubmed_xml(response.body, response.cache_key)}
    # Each paper keeps the exact batch response as its record asset (with its own PMID inside).
    return {pmid: (records[pmid], response.body, response.cache_key) for pmid in pmids if pmid in records}


def europepmc_batch(client: SourceClient, pmids: list[str]) -> dict[str, dict]:
    query = "EXT_ID:(" + " OR ".join(sorted(pmids, key=int)) + ") AND SRC:MED"
    response = client.get(
        "europepmc",
        "search",
        {"query": query, "format": "json", "resultType": "core", "pageSize": str(len(pmids)), "cursorMark": "*"},
        validate=_require_json_keys("hitCount", "resultList"),
    )
    return {str(item.get("pmid")): item for item in response.json()["resultList"].get("result", [])}


def _s3_list(client: SourceClient, prefix: str, delimiter: str | None = None) -> tuple[list[str], list[dict]]:
    params = {"list-type": "2", "prefix": prefix, "max-keys": "1000"}
    if delimiter:
        params["delimiter"] = delimiter

    def check(response) -> None:
        if parse_xml(response.content).tag != f"{S3_NS}ListBucketResult":
            raise ValueError("not an S3 ListBucketResult")

    root = parse_xml(client.get("pmc_oa", "", params, validate=check).body)
    if root.findtext(f"{S3_NS}IsTruncated") == "true":
        raise SourceError("pmc_oa", "malformed_response", f"listing of {prefix} exceeds one page")
    prefixes = [node.findtext(f"{S3_NS}Prefix") for node in root.iter(f"{S3_NS}CommonPrefixes")]
    files = [
        {"key": node.findtext(f"{S3_NS}Key"), "size": int(node.findtext(f"{S3_NS}Size") or 0)}
        for node in root.iter(f"{S3_NS}Contents")
    ]
    return prefixes, files


def _md5_check(expected: str | None):
    def check(response) -> None:
        if expected and hashlib.md5(response.content).hexdigest() != expected:
            raise ValueError("MD5 differs from the dataset metadata")

    return check


def _md5_of(url: str | None) -> str | None:
    match = re.search(r"[?&]md5=([0-9a-f]{32})", url or "")
    return match.group(1) if match else None


def _metadata_check(response) -> None:
    body = json.loads(response.content)
    if not isinstance(body, dict) or not body.get("pmcid"):
        raise ValueError("OA dataset metadata lacks a pmcid")


def oa_dataset(client: SourceClient, pmcid: str) -> tuple[str | None, dict | None, list[dict]]:
    """Latest article version in the PMC OA dataset: (version prefix, metadata, files)."""
    prefixes, _ = _s3_list(client, f"{pmcid}.", "/")
    versions = sorted(
        (p for p in prefixes if re.fullmatch(rf"{pmcid}\.\d+/", p or "")), key=lambda p: int(p[len(pmcid) + 1 : -1])
    )
    if not versions:
        return None, None, []
    version = versions[-1].rstrip("/")
    _, files = _s3_list(client, f"{version}/")
    metadata = client.get("pmc_oa", f"{version}/{version}.json", {}, validate=_metadata_check).json()
    return version, metadata, files


def _links(paper: PaperAcquisition, epmc: dict | None, now: str) -> list[dict]:
    links = [
        Link(
            "pubmed", f"https://pubmed.ncbi.nlm.nih.gov/{paper.pmid}/", None, None, "PubMed", "identifier_resolver", now
        )
    ]
    if paper.pmcid:
        url = f"https://pmc.ncbi.nlm.nih.gov/articles/{paper.pmcid}/"
        links.append(Link("pmc", url, None, None, "PMC", "identifier_resolver", now))
    if paper.doi:
        # A DOI resolves to a landing page; it is not a promise of a downloadable PDF.
        links.append(Link("doi", f"https://doi.org/{paper.doi}", None, None, "DOI", "identifier_resolver", now))
    for item in ((epmc or {}).get("fullTextUrlList") or {}).get("fullTextUrl", []):
        links.append(
            Link(
                "returned_full_text",
                item.get("url"),
                item.get("availability"),
                item.get("documentStyle"),
                item.get("site"),
                "europepmc_fullTextUrlList",
                now,
            )
        )
    return [asdict(link) for link in links]


def acquire_batch(
    client: SourceClient,
    batch: list[tuple[str, str]],
    papers_root: Path,
    repo_root: Path,
    supplement_max_bytes: int,
    supplement_extensions: list[str],
    fetch_supplements: bool,
    pdf_alternates: set[str],
    expected_dois: dict[str, str | None] | None = None,
) -> list[PaperAcquisition]:
    """Audit and acquire one batch of (publication_id, PMID) pairs; per-paper failures stay recorded."""
    now = utc_now()
    pmids = [pmid for _, pmid in batch]
    papers = {pmid: PaperAcquisition(pid, pmid, checked_at=now) for pid, pmid in batch}
    try:
        pubmed = pubmed_batch(client, pmids)
        for pmid, paper in papers.items():
            paper.checked_sources.append("pubmed_efetch")
            if pmid not in pubmed:
                paper.pubmed_status = "not_found"
                continue
            record, body, key = pubmed[pmid]
            paper.pubmed_status = "fetched"
            paper.pmcid = normalize_pmcid(record.pmcid)
            paper.doi = normalize_doi(record.doi)
            paper.title, paper.abstract, paper.year, paper.journal = (
                record.title,
                record.abstract,
                record.year,
                record.journal,
            )
            paper.publication_types, paper.mesh_terms, paper.corrections = (
                record.publication_types,
                record.mesh_terms,
                record.corrections,
            )
            paper.assets.append(
                _asset(
                    store_asset(
                        papers_root,
                        paper.publication_id,
                        "pubmed_batch.xml",
                        "pubmed_record",
                        body,
                        key,
                        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                        repo_root,
                    )
                )
            )
    except SourceError as error:
        for paper in papers.values():
            paper.pubmed_status = f"failed:{error.kind}"
            paper.errors.append(f"pubmed: {error}")
    try:
        epmc = europepmc_batch(client, pmids)
    except SourceError as error:
        epmc = None
        for paper in papers.values():
            paper.europepmc_status = f"failed:{error.kind}"
            paper.errors.append(f"europepmc search: {error}")
    try:
        pubtator, pubtator_key = fetch_pubtator(client, pmids)
    except SourceError as error:
        pubtator, pubtator_key = None, None
        for paper in papers.values():
            paper.pubtator_status = f"failed:{error.kind}"
            paper.errors.append(f"pubtator: {error}")

    for pmid, paper in papers.items():
        item = (epmc or {}).get(pmid)
        if epmc is not None:
            paper.checked_sources.append("europepmc_core")
            paper.europepmc_status = "found" if item else "not_indexed"
        if item:
            record = _epmc_record(item, 1, "")
            flag = {"Y": True, "N": False}
            paper.is_open_access, paper.in_pmc = record.is_open_access, record.in_pmc
            paper.has_pdf, paper.has_supplements = flag.get(item.get("hasPDF")), flag.get(item.get("hasSuppl"))
            paper.license = record.license
            paper.pmcid = paper.pmcid or normalize_pmcid(record.pmcid)
            paper.doi = paper.doi or normalize_doi(record.doi)
            if any(t.lower() in RETRACTED_TYPES for t in record.publication_types):
                paper.retracted = True
        paper.retracted |= any(c.get("type") == "RetractionIn" for c in paper.corrections)
        expected = normalize_doi((expected_dois or {}).get(pmid))
        if expected and paper.doi and expected != paper.doi:
            paper.identity_issues.append(f"advisor DOI {expected} differs from PubMed DOI {paper.doi}")
        paper.links = _links(paper, item, now)
        _full_text(
            client,
            paper,
            papers_root,
            repo_root,
            supplement_max_bytes,
            supplement_extensions,
            fetch_supplements,
            pmid in pdf_alternates,
        )
        if pubtator is not None:
            paper.checked_sources.append("pubtator_biocjson")
            document = pubtator.get(pmid)
            if document is None:
                paper.pubtator_status = "not_indexed"
            else:
                paper.pubtator_status = "fetched"
                bioc_license = pubtator_full_text_license(document)
                if bioc_license:
                    paper.bioc_full_text = True
                    if not paper.full_text_route:
                        # PubTator distributes PMC open-access text with its license; used without JATS.
                        paper.full_text_route = "pubtator_bioc"
                        paper.license = paper.license or bioc_license
                content = json.dumps(document, sort_keys=True, ensure_ascii=False).encode("utf-8")
                paper.assets.append(
                    _asset(
                        store_asset(
                            papers_root,
                            paper.publication_id,
                            "pubtator.json",
                            "pubtator_annotations",
                            content,
                            pubtator_key,
                            "https://www.ncbi.nlm.nih.gov/research/pubtator3-api/publications/export/biocjson",
                            repo_root,
                        )
                    )
                )
    return list(papers.values())


def _full_text(
    client: SourceClient,
    paper: PaperAcquisition,
    papers_root: Path,
    repo_root: Path,
    supplement_max_bytes: int,
    supplement_extensions: list[str],
    fetch_supplements: bool,
    pdf_alternate: bool,
) -> None:
    if not paper.pmcid:
        paper.oa_dataset_status, paper.full_text_status = "no_pmcid", "no_pmcid"
        return
    files: list[dict] = []
    try:
        paper.checked_sources.append("pmc_oa_dataset")
        version, metadata, files = oa_dataset(client, paper.pmcid)
        paper.oa_dataset_status = "present" if version else "absent"
        paper.oa_dataset_version, paper.oa_metadata = version, metadata
        if metadata:
            if str(metadata.get("pmid") or "") not in {"", paper.pmid}:
                paper.identity_issues.append(f"OA dataset PMID {metadata.get('pmid')} differs from {paper.pmid}")
            meta_doi = normalize_doi(metadata.get("doi"))
            if meta_doi and paper.doi and meta_doi != paper.doi:
                paper.identity_issues.append(f"OA dataset DOI {meta_doi} differs from {paper.doi}")
            paper.retracted |= bool(metadata.get("is_retracted"))
            paper.license = paper.license or metadata.get("license_code")
            if metadata.get("is_pmc_openaccess"):
                paper.is_open_access = True
    except SourceError as error:
        paper.oa_dataset_status = f"failed:{error.kind}"
        paper.errors.append(f"pmc oa dataset: {error}")
        metadata = None
    jats: bytes | None = None
    if paper.is_open_access:
        try:
            paper.checked_sources.append("europepmc_fulltextxml")
            jats, key = fetch_full_text(client, paper.pmcid)
            paper.full_text_route, paper.full_text_status = "europepmc_jats", "fetched"
            paper.assets.append(
                _asset(
                    store_asset(
                        papers_root,
                        paper.publication_id,
                        "fulltext.xml",
                        "jats_full_text",
                        jats,
                        key,
                        f"https://www.ebi.ac.uk/europepmc/webservices/rest/{paper.pmcid}/fullTextXML",
                        repo_root,
                    )
                )
            )
        except SourceError as error:
            paper.full_text_status = f"failed:{error.kind}" if not isinstance(error, NotFound) else "not_served"
            paper.errors.append(f"europepmc fullTextXML: {error}")
        if jats is None and metadata and metadata.get("xml_url"):
            jats = _oa_file(
                client, paper, metadata["xml_url"], "fulltext_pmc_oa.xml", "jats_full_text", papers_root, repo_root
            )
            if jats is not None:
                paper.full_text_route, paper.full_text_status = "pmc_oa_dataset_jats", "fetched"
                paper.license = paper.license or jats_license(jats)
        if paper.full_text_route and paper.license is None and jats is not None:
            paper.license = jats_license(jats)
    elif paper.is_open_access is False:
        paper.full_text_status = "not_open_access"
    else:
        paper.full_text_status = "open_access_unknown"
    if metadata and pdf_alternate and metadata.get("pdf_url"):
        _oa_file(client, paper, metadata["pdf_url"], "article.pdf", "pdf_alternate", papers_root, repo_root)
    if paper.is_open_access:
        paper.supplements = [
            asdict(s)
            for s in _supplements(
                client,
                paper,
                jats,
                files,
                metadata,
                papers_root,
                repo_root,
                supplement_max_bytes,
                supplement_extensions,
                fetch_supplements,
            )
        ]


def _oa_file(client, paper, s3_url: str, name: str, role: str, papers_root, repo_root) -> bytes | None:
    key = s3_url.removeprefix("s3://pmc-oa-opendata/").split("?")[0]
    try:
        response = client.get("pmc_oa", key, {}, validate=_md5_check(_md5_of(s3_url)))
    except SourceError as error:
        paper.errors.append(f"pmc oa {PurePosixPath(key).name}: {error}")
        return None
    url = f"https://pmc-oa-opendata.s3.amazonaws.com/{key}"
    paper.assets.append(
        _asset(
            store_asset(
                papers_root, paper.publication_id, name, role, response.body, response.cache_key, url, repo_root
            )
        )
    )
    return response.body


def _supplements(
    client, paper, jats, files, metadata, papers_root, repo_root, max_bytes, extensions, fetch
) -> list[SupplementItem]:
    """Every supplementary item the article or dataset lists, with an explicit acquisition state."""
    inventory: dict[str, tuple[str | None, str | None]] = {}
    if jats is not None:
        try:
            for item in parse_jats(paper.publication_id, jats).supplementary:
                if item.get("href"):
                    inventory[PurePosixPath(item["href"]).name] = (item.get("label"), item.get("item_id"))
        except (ParseError, ValueError) as error:
            paper.errors.append(f"supplement inventory: {error}")
    md5 = {PurePosixPath(u.split("?")[0]).name: _md5_of(u) for u in (metadata or {}).get("media_urls", [])}
    main = {
        PurePosixPath(str((metadata or {}).get(k) or "").split("?")[0]).name for k in ("pdf_url", "xml_url", "text_url")
    }
    listed = {PurePosixPath(f["key"]).name: f for f in files}
    names = set(inventory) | {
        n
        for n in listed
        if n not in main and not n.endswith(".json") and PurePosixPath(n).suffix.lower() not in FIGURE_EXTENSIONS
    }
    items = []
    for name in sorted(names):
        label, item_id = inventory.get(name, (None, None))
        entry = listed.get(name)
        url = f"https://pmc-oa-opendata.s3.amazonaws.com/{entry['key']}" if entry else None
        item = SupplementItem(name, label, item_id, entry["size"] if entry else None, md5.get(name), url, "")
        extension = PurePosixPath(name).suffix.lower().lstrip(".")
        if entry is None:
            item.state = "not_in_oa_dataset"
        elif extension not in extensions:
            item.state = "unsupported_extension_inventoried"
        elif entry["size"] > max_bytes:
            item.state = "size_limit_deferred"
        elif not fetch:
            item.state = "not_requested"
        else:
            try:
                response = client.get("pmc_oa", entry["key"], {}, validate=_md5_check(item.md5))
                asset = store_asset(
                    papers_root,
                    paper.publication_id,
                    f"supplement-{name}",
                    "supplement",
                    response.body,
                    response.cache_key,
                    url,
                    repo_root,
                )
                item.state, item.asset = "acquired", _asset(asset)
            except SourceError as error:
                item.state = "md5_mismatch" if error.kind == "malformed_response" else f"fetch_failed:{error.kind}"
                paper.errors.append(f"supplement {name}: {error}")
        items.append(item)
    return items
