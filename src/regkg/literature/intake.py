"""Manual download intake from `data/papers/manual_inbox/` (user-supplied article PDFs, supplements).

`intake.csv` maps files to publications: pmid, filename, role (article | supplement), source_url,
acquired_on, disposition (optional: unavailable | abstract_only), note. A filename is only a
mapping hint: identity is confirmed from the file's own text (PMID, DOI, or most title words in
its first pages). Unconfirmable files go to identity review. Paths may not leave the inbox,
symlinks are not followed, content is never executed, and originals are left unchanged.
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

from regkg.literature.fetch import store_asset
from regkg.literature.files import detect_type
from regkg.provenance import stable_id

INTAKE_COLUMNS = ["pmid", "filename", "role", "source_url", "acquired_on", "disposition", "note"]
DISPOSITIONS = {"", "unavailable", "abstract_only"}
SESSION_HINTS = re.compile(r"(token|session|sid|auth|ticket|ezproxy|login|signature|key)=", re.IGNORECASE)
MAX_BYTES = 200_000_000


@dataclass
class IntakeRecord:
    pmid: str
    filename: str
    role: str
    state: str  # INGESTED | IDENTITY_REVIEW_REQUIRED | REJECTED | DISPOSITION_RECORDED | DUPLICATE
    reasons: list[str] = field(default_factory=list)
    sha256: str | None = None
    detected_type: str | None = None
    identity_evidence: list[str] = field(default_factory=list)
    asset: dict | None = None
    source_url: str | None = None
    acquired_on: str | None = None
    note: str | None = None
    request_id: str | None = None


def safe_url(url: str) -> tuple[str | None, str | None]:
    """A nonsecret http(s) landing URL, or (None, reason) when it carries credentials or session state."""
    url = (url or "").strip()
    if not url:
        return None, None
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"}:
        return None, "source_url dropped: not http(s)"
    if parts.username or parts.password or SESSION_HINTS.search(parts.query):
        return None, "source_url dropped: credential or session parameters"
    return url, None


def pdf_identity_text(content: bytes, pages: int = 3) -> str:
    try:
        import pypdfium2

        document = pypdfium2.PdfDocument(content)
        return " ".join(document[i].get_textpage().get_text_range() for i in range(min(pages, len(document))))
    except Exception:  # noqa: BLE001 - encrypted/unreadable PDFs are unconfirmable, reviewed below
        return ""


def identity_evidence(text: str, pmid: str, doi: str | None, title: str | None) -> list[str]:
    lowered = " ".join(text.lower().split())
    evidence = []
    if re.search(rf"(?<!\d){re.escape(pmid)}(?!\d)", lowered):
        evidence.append("pmid_in_text")
    if doi and doi.lower() in lowered.replace(" ", ""):
        evidence.append("doi_in_text")
    words = [w for w in re.findall(r"[a-z0-9]{4,}", (title or "").lower())]
    if words:
        found = sum(w in lowered for w in words) / len(words)
        if found >= 0.8:
            evidence.append(f"title_words_{found:.0%}")
    return evidence


def run_intake(
    inbox: Path, papers_root: Path, repo_root: Path, publications: dict[str, dict], known_hashes: set[str]
) -> dict:
    """Process intake.csv. `publications` maps PMID -> {publication_id, doi, title}.

    `known_hashes` are bytes already acquired through automatic routes; the same bytes supplied
    manually are recorded as DUPLICATE. Re-running intake over the same inbox is idempotent.
    """
    manifest = inbox / "intake.csv"
    records: list[IntakeRecord] = []
    if not manifest.is_file():
        return {"records": [], "unlisted": sorted(_files(inbox)), "manifest": "absent"}
    rows = list(csv.DictReader(io.StringIO(manifest.read_text(encoding="utf-8-sig"))))
    listed = set()
    for row in rows:
        pmid, filename = (row.get("pmid") or "").strip(), (row.get("filename") or "").strip()
        role = (row.get("role") or "article").strip()
        disposition = (row.get("disposition") or "").strip()
        url, url_problem = safe_url(row.get("source_url") or "")
        record = IntakeRecord(
            pmid,
            filename,
            role,
            "REJECTED",
            source_url=url,
            acquired_on=(row.get("acquired_on") or "").strip() or None,
            note=row.get("note") or None,
        )
        if url_problem:
            record.reasons.append(url_problem)
        expected = "article.pdf" if role == "article" else f"supplement-{PurePosixPath(filename).name}"
        record.request_id = stable_id("download", {"pmid": pmid, "item": expected})
        records.append(record)
        if pmid not in publications:
            record.reasons.append("PMID is not in the advisor or discovery corpus")
            continue
        if disposition not in DISPOSITIONS or role not in {"article", "supplement"}:
            record.reasons.append(f"unknown role/disposition {role!r}/{disposition!r}")
            continue
        if disposition and not filename:
            record.state = "DISPOSITION_RECORDED"
            record.reasons.append(f"user disposition: {disposition}")
            continue
        path = inbox / pmid / filename
        listed.add(path)
        try:
            resolved = path.resolve(strict=True)
            resolved.relative_to(inbox.resolve())
        except (FileNotFoundError, ValueError):
            record.reasons.append("file missing or outside the inbox")
            continue
        if path.is_symlink() or not resolved.is_file():
            record.reasons.append("not a regular file (symlinks are not followed)")
            continue
        content = resolved.read_bytes()
        record.sha256 = hashlib.sha256(content).hexdigest()
        detected, notes = detect_type(content, filename)
        record.detected_type = detected
        record.reasons += notes
        if not content or len(content) > MAX_BYTES:
            record.reasons.append(f"size {len(content)} outside 1..{MAX_BYTES}")
            continue
        if role == "article" and detected != "pdf":
            record.reasons.append(f"article must be a PDF; content is {detected}")
            continue
        info = publications[pmid]
        text = pdf_identity_text(content) if detected == "pdf" else ""
        record.identity_evidence = identity_evidence(text, pmid, info.get("doi"), info.get("title"))
        duplicate = record.sha256 in known_hashes
        asset = store_asset(
            papers_root,
            info["publication_id"],
            f"manual-{PurePosixPath(filename).name}",
            f"manual_{role}",
            content,
            "manual_intake",
            url or "",
            repo_root,
        )
        record.asset = {
            **asdict(asset),
            "pmid": pmid,
            "publication_id": info["publication_id"],
            "acquired_on": record.acquired_on,
        }
        known_hashes.add(record.sha256)
        if not record.identity_evidence:
            # Unverified manual files (articles and supplements alike) need review before use.
            record.state = "IDENTITY_REVIEW_REQUIRED"
            record.reasons.append("no PMID, DOI, or title match in the file's own text")
        else:
            record.state = "DUPLICATE" if duplicate else "INGESTED"
    return {
        "records": [asdict(r) for r in records],
        "unlisted": sorted(str(p) for p in _files(inbox) - listed),
        "manifest": "present",
    }


def _files(inbox: Path) -> set[Path]:
    return {p for p in inbox.glob("*/*") if p.is_file()} if inbox.is_dir() else set()
