"""Shared bounded HTTP access to literature services, with a success-only response cache.

Replaces the reference wrapper's unavailable `lungchat` TLS/trace/session layer with explicit
per-request records. Certificates are verified (httpx default). Nothing runs at import time.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx

from regkg.provenance import canonical_json, utc_now

USER_AGENT = "regkg/0.1 (spatial-niche-regulatory-kg; bounded literature retrieval)"
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


@dataclass(frozen=True)
class Service:
    name: str
    label: str
    base_url: str
    min_interval_seconds: float  # spacing between requests to respect the published rate limit


# Rates: NCBI E-utilities 3 requests/s without a key, 10 with one (NLM KA-05317). PubTator3 is
# a separate NCBI service limited to 3 requests/s and receives no E-utilities key. Europe PMC
# publishes no numeric limit for its public REST API; a conservative 5 requests/s is used.
SERVICES = {
    "pubmed": Service("pubmed", "PubMed", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils", 0.34),
    "europepmc": Service("europepmc", "Europe PMC", "https://www.ebi.ac.uk/europepmc/webservices/rest", 0.2),
    "pubtator": Service("pubtator", "PubTator", "https://www.ncbi.nlm.nih.gov/research/pubtator3-api", 0.34),
    # NCBI's PMC Open Access dataset on AWS Open Data (public, no credentials): per-article-version
    # metadata with license/retraction flags and MD5s, JATS, the publisher PDF, and supplements.
    "pmc_oa": Service("pmc_oa", "PMC Open Access dataset", "https://pmc-oa-opendata.s3.amazonaws.com", 0.1),
}


class SourceError(RuntimeError):
    """A request did not yield a usable response. `kind` classifies why; never 'no literature'."""

    def __init__(self, service: str, kind: str, detail: str) -> None:
        super().__init__(f"{service}: {kind}: {detail}")
        self.service, self.kind, self.detail = service, kind, detail


class NotFound(SourceError):
    """The service answered definitively that the identifier or asset does not exist."""


@dataclass(frozen=True)
class NcbiSettings:
    tool: str
    email: str | None = None
    api_key: str | None = None

    @classmethod
    def from_env(cls, env: dict[str, str], default_tool: str) -> NcbiSettings:
        return cls(env.get("NCBI_TOOL") or default_tool, env.get("NCBI_EMAIL") or None, env.get("NCBI_API_KEY") or None)

    def params(self) -> dict[str, str]:
        params = {"tool": self.tool}
        if self.email:
            params["email"] = self.email
        if self.api_key:
            params["api_key"] = self.api_key
        return params

    def presence(self) -> dict[str, bool]:
        return {"NCBI_TOOL": bool(self.tool), "NCBI_EMAIL": bool(self.email), "NCBI_API_KEY": bool(self.api_key)}


@dataclass
class Response:
    service: str
    url: str  # recorded without credentials
    body: bytes
    content_type: str | None
    cached: bool
    cache_key: str

    def json(self) -> Any:
        return json.loads(self.body)


@dataclass
class RequestRecord:
    service: str
    cache_key: str
    url: str
    params: dict[str, str]
    outcome: str  # cached | fetched | not_found | failed
    attempts: int
    http_status: int | None
    error_kind: str | None
    bytes: int | None
    sha256: str | None
    at: str


@dataclass
class SourceClient:
    cache_dir: Path
    ncbi: NcbiSettings
    timeout_seconds: float = 30.0
    max_retries: int = 2
    transport: httpx.BaseTransport | None = None
    records: list[RequestRecord] = field(default_factory=list)
    _last: dict[str, float] = field(default_factory=dict)
    _client: httpx.Client | None = None

    @property
    def network_requests(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for record in self.records:
            if record.outcome != "cached":
                counts[record.service] = counts.get(record.service, 0) + record.attempts
        return counts

    def _http(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(
                headers={"User-Agent": USER_AGENT},
                timeout=self.timeout_seconds,
                follow_redirects=True,
                transport=self.transport,
            )
        return self._client

    def close(self) -> None:
        if self._client is not None:
            self._client.close()

    def get(
        self,
        service: str,
        path: str,
        params: dict[str, str],
        validate: Callable[[httpx.Response], None] | None = None,
        not_found_status: frozenset[int] = frozenset({404}),
    ) -> Response:
        """GET with caching; the E-utilities key/contact is attached only for the PubMed service."""
        spec = SERVICES[service]
        url = f"{spec.base_url}/{path.lstrip('/')}"
        public = {k: str(v) for k, v in sorted(params.items())}
        cache_key = hashlib.sha256(
            canonical_json({"service": service, "url": url, "params": public}).encode()
        ).hexdigest()
        cached = self._read_cache(cache_key)
        if cached is not None:
            self.records.append(
                RequestRecord(
                    service,
                    cache_key,
                    url,
                    public,
                    "cached",
                    0,
                    200,
                    None,
                    len(cached[0]),
                    hashlib.sha256(cached[0]).hexdigest(),
                    utc_now(),
                )
            )
            return Response(service, url, cached[0], cached[1], True, cache_key)
        send = dict(public)
        if service == "pubmed":
            send.update(self.ncbi.params())
        attempts, status, kind, detail = 0, None, "request_failed", ""
        for attempt in range(self.max_retries + 1):
            attempts += 1
            wait = spec.min_interval_seconds - (time.monotonic() - self._last.get(service, 0.0))
            if wait > 0:
                time.sleep(wait)
            self._last[service] = time.monotonic()
            try:
                response = self._http().get(url, params=send)
            except httpx.TimeoutException as error:
                kind, detail, status = "timeout", type(error).__name__, None
            except httpx.HTTPError as error:
                kind, detail, status = "request_failed", type(error).__name__, None
            else:
                status = response.status_code
                if status in not_found_status:
                    self._record(service, cache_key, url, public, "not_found", attempts, status, "not_found", response)
                    raise NotFound(service, "not_found", f"HTTP {status}")
                if status == 200:
                    try:
                        if validate:
                            validate(response)
                    except ValueError as error:
                        kind, detail = "malformed_response", str(error)
                    else:
                        self._write_cache(cache_key, response.content, response.headers.get("content-type"))
                        self._record(service, cache_key, url, public, "fetched", attempts, status, None, response)
                        return Response(
                            service, url, response.content, response.headers.get("content-type"), False, cache_key
                        )
                elif status in RETRYABLE_STATUS:
                    kind, detail = ("rate_limited" if status == 429 else "server_error"), f"HTTP {status}"
                    retry_after = response.headers.get("Retry-After", "")
                    if attempt < self.max_retries and retry_after.isdigit():
                        time.sleep(min(int(retry_after), 30))
                        continue
                else:
                    kind, detail = "http_error", f"HTTP {status}"
                    break
            if attempt < self.max_retries:
                time.sleep(2**attempt)
        self.records.append(
            RequestRecord(service, cache_key, url, public, "failed", attempts, status, kind, None, None, utc_now())
        )
        raise SourceError(service, kind, detail)

    def _record(self, service, cache_key, url, params, outcome, attempts, status, kind, response) -> None:
        self.records.append(
            RequestRecord(
                service,
                cache_key,
                url,
                params,
                outcome,
                attempts,
                status,
                kind,
                len(response.content),
                hashlib.sha256(response.content).hexdigest(),
                utc_now(),
            )
        )

    def _paths(self, cache_key: str) -> tuple[Path, Path]:
        base = self.cache_dir / cache_key[:2] / cache_key
        return base.with_suffix(".body"), base.with_suffix(".json")

    def _read_cache(self, cache_key: str) -> tuple[bytes, str | None] | None:
        body, meta = self._paths(cache_key)
        if not (body.is_file() and meta.is_file()):
            return None
        info = json.loads(meta.read_text())
        content = body.read_bytes()
        if hashlib.sha256(content).hexdigest() != info["sha256"]:
            raise SourceError("cache", "cache_corrupted", str(body))
        return content, info.get("content_type")

    def _write_cache(self, cache_key: str, content: bytes, content_type: str | None) -> None:
        body, meta = self._paths(cache_key)
        body.parent.mkdir(parents=True, exist_ok=True)
        for path, data in (
            (body, content),
            (
                meta,
                json.dumps(
                    {
                        "sha256": hashlib.sha256(content).hexdigest(),
                        "content_type": content_type,
                        "stored_at": utc_now(),
                    }
                ).encode(),
            ),
        ):
            temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}")
            temporary.write_bytes(data)
            os.replace(temporary, path)
