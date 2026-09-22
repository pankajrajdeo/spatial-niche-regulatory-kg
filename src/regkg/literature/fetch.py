"""Eligible source assets for selected publications: PubMed records, open-access JATS, PubTator.

This takes over the reference wrapper's `get_paper_details` responsibility. A definitive
"not found" is distinguished from a failed request; neither says anything about the biology.
Only open-access full text is requested; no PDFs are downloaded and no access control is bypassed.
"""

from __future__ import annotations

import hashlib
import json
import os
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

from regkg.literature.http import NotFound, SourceClient, SourceError
from regkg.literature.publications import normalize_doi, normalize_pmcid, normalize_pmid
from regkg.literature.search import SourceRecord, parse_pubmed_xml
from regkg.literature.xml import parse_xml
from regkg.provenance import utc_now

# Identifier prefixes accepted by the reference `get_paper_details`, retained here.
IDENTIFIER_KINDS = {"pmid": "pmid", "ppr": "pprid", "pprid": "pprid", "doi": "doi", "pmcid": "pmcid", "epmc": "epmc"}


def parse_work_id(work_id: str) -> tuple[str, str]:
    """Validate an identifier such as `pmid:123`, `PMC456`, or `doi:10.x/y` (reference behavior)."""
    identifier = (work_id or "").strip()
    prefix, _, value = identifier.partition(":")
    if not value:
        if identifier.isdigit():
            prefix, value = "pmid", identifier
        elif identifier.upper().startswith("PMC"):
            prefix, value = "pmcid", identifier
        else:
            prefix, value = "", identifier
    kind = IDENTIFIER_KINDS.get(prefix.lower())
    normalized = {"pmid": normalize_pmid, "pmcid": normalize_pmcid, "doi": normalize_doi}.get(
        kind, lambda v: v or None
    )(value)
    if not kind or not normalized:
        raise ValueError(f"{work_id!r} is not a recognized publication identifier")
    return kind, normalized


def fetch_pubmed_record(client: SourceClient, pmid: str) -> tuple[SourceRecord, bytes, str]:
    """One PubMed record; raises NotFound when efetch answers without that PMID."""
    response = client.get(
        "pubmed", "efetch.fcgi", {"db": "pubmed", "id": pmid, "retmode": "xml"}, validate=lambda r: parse_xml(r.content)
    )
    records = [r for r in parse_pubmed_xml(response.body, response.cache_key) if r.pmid == pmid]
    if not records:
        raise NotFound("pubmed", "not_found", f"efetch returned no record for PMID {pmid}")
    return records[0], response.body, response.cache_key


def fetch_full_text(client: SourceClient, pmcid: str) -> tuple[bytes, str]:
    """Europe PMC JATS for the open-access subset; 404 means it is not served for this article."""

    def check(response) -> None:
        root = parse_xml(response.content)
        if root.tag != "article":
            raise ValueError(f"expected a JATS <article>, got <{root.tag}>")

    response = client.get("europepmc", f"{pmcid}/fullTextXML", {}, validate=check)
    return response.body, response.cache_key


def europepmc_open_access(client: SourceClient, pmcid: str) -> bool | None:
    """Europe PMC's open-access flag for a PMCID. Its fullTextXML endpoint answers HTTP 500 (not 404)
    for articles outside the open-access subset, so access is checked before any full-text request."""
    from regkg.literature.search import _require_json_keys

    response = client.get(
        "europepmc",
        "search",
        {"query": f"PMCID:{pmcid}", "format": "json", "resultType": "core", "pageSize": "1", "cursorMark": "*"},
        validate=_require_json_keys("hitCount", "resultList"),
    )
    results = response.json()["resultList"].get("result", [])
    flag = results[0].get("isOpenAccess") if results else None
    return {"Y": True, "N": False}.get(flag)


def fetch_pubtator(client: SourceClient, pmids: list[str]) -> tuple[dict[str, dict], str]:
    """PubTator3 BioC JSON (full text where PubTator has it) for up to 100 PMIDs in one request."""

    def check(response) -> None:
        body = response.json()
        if not isinstance(body, dict) or not isinstance(body.get("PubTator3"), list):
            raise ValueError("PubTator response lacks the PubTator3 document list")

    response = client.get(
        "pubtator",
        "publications/export/biocjson",
        {"pmids": ",".join(sorted(pmids, key=int)), "full": "true"},
        validate=check,
    )
    documents = {str(doc.get("pmid") or doc.get("id")): doc for doc in response.json()["PubTator3"]}
    return documents, response.cache_key


@dataclass
class Asset:
    name: str
    role: str  # pubmed_record | jats_full_text | pubtator_annotations | search_record
    path: str
    sha256: str
    bytes: int
    source_cache_key: str
    retrieved_at: str
    url: str


@dataclass
class FetchResult:
    publication_id: str
    identifiers: dict[str, str]
    pubmed_status: str  # fetched | not_found | failed:<kind> | no_pmid
    full_text_status: str  # fetched | not_open_access | not_served | failed:<kind> | no_pmcid
    pubtator_status: str  # fetched | not_indexed | failed:<kind> | no_pmid | disabled
    access_status: str  # open_access_full_text | abstract_only | unavailable
    license: str | None
    open_access: bool | None = None
    assets: list[Asset] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        return asdict(self)


def store_asset(
    papers_root: Path,
    publication_id: str,
    name: str,
    role: str,
    content: bytes,
    cache_key: str,
    url: str,
    repo_root: Path,
) -> Asset:
    digest = hashlib.sha256(content).hexdigest()
    directory = papers_root / publication_id.replace(":", "_") / digest
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        temporary = path.with_name(f".{name}.{uuid.uuid4().hex}")
        temporary.write_bytes(content)
        os.replace(temporary, path)
    try:
        shown = path.resolve().relative_to(repo_root).as_posix()
    except ValueError:
        shown = path.as_posix()
    return Asset(name, role, shown, digest, len(content), cache_key, utc_now(), url)


def pubtator_full_text_license(document: dict | None) -> str | None:
    """The license infon of a PubTator document that carries body text beyond title/abstract."""
    if not document:
        return None
    passages = document.get("passages", [])
    body = any((p.get("infons") or {}).get("section_type") not in {None, "TITLE", "ABSTRACT"} for p in passages)
    license_text = next(
        ((p.get("infons") or {}).get("license") for p in passages if (p.get("infons") or {}).get("license")), None
    )
    return license_text[:300] if body and license_text else None


def jats_license(content: bytes) -> str | None:
    root = parse_xml(content)
    for node in root.iter("license"):
        href = node.get("{http://www.w3.org/1999/xlink}href")
        text = " ".join("".join(node.itertext()).split())
        return href or text[:300] or None
    return None


def fetch_publication(
    client: SourceClient,
    publication,
    pubtator_docs: dict[str, dict] | None,
    pubtator_cache_key: str | None,
    pubtator_status_all: str,
    papers_root: Path,
    repo_root: Path,
) -> FetchResult:
    ids = dict(publication.identifiers)
    result = FetchResult(
        publication.publication_id, ids, "no_pmid", "no_pmcid", pubtator_status_all, "unavailable", None
    )
    pmid = ids.get("pmid")
    if pmid:
        try:
            record, body, key = fetch_pubmed_record(client, pmid)
            result.pubmed_status = "fetched"
            result.assets.append(
                store_asset(
                    papers_root,
                    publication.publication_id,
                    "pubmed.xml",
                    "pubmed_record",
                    body,
                    key,
                    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                    repo_root,
                )
            )
            if record.pmcid and "pmcid" not in ids:
                # Linking a PMCID the PubMed record itself states is verified identity.
                ids["pmcid"] = normalize_pmcid(record.pmcid)
        except NotFound:
            result.pubmed_status = "not_found"
        except SourceError as error:
            result.pubmed_status = f"failed:{error.kind}"
            result.errors.append(str(error))
    open_access = next((r.is_open_access for _, r in publication.records if r.is_open_access is not None), None)
    pmcid = ids.get("pmcid")
    if pmcid and open_access is None:
        try:
            open_access = europepmc_open_access(client, pmcid)
        except SourceError as error:
            result.errors.append(f"open-access lookup: {error}")
    result.open_access = open_access
    if pmcid and open_access is False:
        result.full_text_status = "not_open_access"
    elif pmcid:
        try:
            body, key = fetch_full_text(client, pmcid)
            result.full_text_status = "fetched"
            result.license = jats_license(body)
            result.assets.append(
                store_asset(
                    papers_root,
                    publication.publication_id,
                    "fulltext.xml",
                    "jats_full_text",
                    body,
                    key,
                    f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML",
                    repo_root,
                )
            )
        except NotFound:
            result.full_text_status = "not_served"
        except SourceError as error:
            result.full_text_status = f"failed:{error.kind}"
            result.errors.append(str(error))
    if pmid and pubtator_docs is not None:
        document = pubtator_docs.get(pmid)
        if document is None:
            result.pubtator_status = "not_indexed"
        else:
            content = json.dumps(document, sort_keys=True, ensure_ascii=False).encode("utf-8")
            result.pubtator_status = "fetched"
            result.assets.append(
                store_asset(
                    papers_root,
                    publication.publication_id,
                    "pubtator.json",
                    "pubtator_annotations",
                    content,
                    pubtator_cache_key,
                    "https://www.ncbi.nlm.nih.gov/research/pubtator3-api/publications/export/biocjson",
                    repo_root,
                )
            )
    if not pmid and publication.records:
        # Europe PMC-only records (e.g. preprints): the search record is the only text asset.
        record = next(r for _, r in publication.records if r.source == "europepmc")
        content = json.dumps(asdict(record), sort_keys=True, ensure_ascii=False).encode("utf-8")
        result.assets.append(
            store_asset(
                papers_root,
                publication.publication_id,
                "search_record.json",
                "search_record",
                content,
                record.cache_key,
                "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                repo_root,
            )
        )
    bioc_full_text = pubtator_full_text_license(pubtator_docs.get(pmid) if pmid and pubtator_docs else None)
    if result.full_text_status == "fetched":
        result.access_status = "open_access_full_text"
    elif bioc_full_text:
        # PubTator distributes the PMC open-access text with its license; used when JATS is unavailable.
        result.access_status = "open_access_full_text"
        result.license = result.license or bioc_full_text
    elif result.pubmed_status == "fetched" or any(a.role == "search_record" for a in result.assets):
        result.access_status = "abstract_only"
    result.identifiers = ids
    return result
