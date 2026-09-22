"""Cached, checksum-verified snapshots of external reference resources.

A snapshot is downloaded once into `data/external/...` with its provenance. Later runs reuse the
cached bytes after re-hashing them, so replay makes no network request.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

from regkg.provenance import read_json, sha256_file, utc_now, write_json

USER_AGENT = "regkg/0.1 (spatial-niche-regulatory-kg; bounded reference snapshot)"
TIMEOUT_SECONDS = 60.0
MAX_RETRIES = 2


class ResourceError(RuntimeError):
    """A reference resource could not be obtained or failed its integrity check."""


@dataclass(frozen=True)
class Snapshot:
    path: Path
    provenance: dict[str, Any]
    network_requests: int


class Fetcher:
    """Bounded HTTP GETs with retry/backoff; counts requests so replay can prove zero network use."""

    def __init__(self) -> None:
        self.requests = 0

    def get(self, url: str) -> httpx.Response:
        last_error: Exception | None = None
        for attempt in range(MAX_RETRIES + 1):
            self.requests += 1
            try:
                response = httpx.get(
                    url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT_SECONDS, follow_redirects=True
                )
            except httpx.HTTPError as error:
                last_error = error
            else:
                if response.status_code == 200:
                    return response
                if response.status_code not in {429, 500, 502, 503, 504}:
                    raise ResourceError(f"GET {url} returned HTTP {response.status_code}")
                last_error = ResourceError(f"GET {url} returned HTTP {response.status_code}")
                retry_after = response.headers.get("Retry-After", "")
                if attempt < MAX_RETRIES and retry_after.isdigit():
                    time.sleep(min(int(retry_after), 30))
                    continue
            if attempt < MAX_RETRIES:
                time.sleep(2**attempt)
        raise ResourceError(f"GET {url} failed after {MAX_RETRIES + 1} attempts: {last_error}")

    def get_json(self, url: str) -> Any:
        return self.get(url).json()


def _write_bytes_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_bytes(content)
    os.replace(temporary, path)


def cached_snapshot(directory: Path, filename: str) -> Snapshot | None:
    """Return a cached snapshot only if its bytes still match the recorded SHA-256."""
    path, provenance_path = directory / filename, directory / "provenance.json"
    if not (path.is_file() and provenance_path.is_file()):
        return None
    provenance = read_json(provenance_path)
    if sha256_file(path) != provenance["sha256"]:
        raise ResourceError(f"cached snapshot {path} no longer matches its recorded SHA-256; refusing to use it")
    return Snapshot(path, provenance, 0)


def store_snapshot(
    directory: Path,
    filename: str,
    content: bytes,
    url: str,
    fetcher: Fetcher,
    *,
    expected_md5_hex: str | None,
    metadata: dict[str, Any],
    response_headers: dict[str, str],
) -> Snapshot:
    md5_hex = hashlib.md5(content).hexdigest()
    if expected_md5_hex is not None and md5_hex != expected_md5_hex:
        raise ResourceError(f"{url}: MD5 {md5_hex} does not match publisher checksum {expected_md5_hex}")
    path = directory / filename
    _write_bytes_atomic(path, content)
    provenance = {
        "url": url,
        "retrieved_at": utc_now(),
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "md5": md5_hex,
        "publisher_md5_verified": expected_md5_hex is not None,
        "response_headers": response_headers,
        **metadata,
    }
    write_json(directory / "provenance.json", provenance)
    return Snapshot(path, provenance, fetcher.requests)


def md5_from_base64(value: str) -> str:
    return base64.b64decode(value).hex()


def selected_headers(response: httpx.Response) -> dict[str, str]:
    keep = ("etag", "last-modified", "content-length", "content-type", "x-goog-generation")
    return {key: response.headers[key] for key in keep if key in response.headers}


def dump_json(path: Path, value: Any) -> None:
    _write_bytes_atomic(path, (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8"))
