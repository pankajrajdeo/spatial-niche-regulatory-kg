"""Hashes, deterministic IDs, manifests, and atomic artifact publication."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import uuid
from collections.abc import Iterable, Mapping
from datetime import UTC, datetime
from importlib import metadata
from pathlib import Path
from typing import Any

ID_HEX_LENGTH = 20  # 80 bits; uniqueness is still checked on every output table.
_HASH_CHUNK_BYTES = 1 << 20


def canonical_json(value: Any) -> str:
    """Serialize identity content with sorted keys and a fixed representation."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def stable_id(namespace: str, identity: Mapping[str, Any]) -> str:
    """Deterministic application ID, independent of process, machine path, and key order."""
    if not namespace or ":" in namespace:
        raise ValueError(f"invalid ID namespace: {namespace!r}")
    payload = canonical_json({"namespace": namespace, "identity": dict(identity)})
    return f"{namespace}:{hashlib.sha256(payload.encode('utf-8')).hexdigest()[:ID_HEX_LENGTH]}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(_HASH_CHUNK_BYTES):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def code_fingerprint(package_root: Path, relative_paths: Iterable[str]) -> str:
    """Hash of result-affecting source files; used because uncommitted code has no Git revision."""
    digest = hashlib.sha256()
    for relative in sorted(relative_paths):
        path = package_root / relative
        files = sorted(path.rglob("*.py")) if path.is_dir() else [path]
        for file in files:
            digest.update(file.relative_to(package_root).as_posix().encode("utf-8"))
            digest.update(b"\0")
            digest.update(file.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()


def git_revision(repo_root: Path) -> dict[str, Any]:
    """Current commit and whether the working tree has uncommitted changes; null if unavailable."""
    try:
        head = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"], capture_output=True, text=True, check=True
        ).stdout.strip()
        status = subprocess.run(
            ["git", "-C", str(repo_root), "status", "--porcelain"], capture_output=True, text=True, check=True
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return {"commit": None, "dirty": None}
    return {"commit": head, "dirty": bool(status.strip())}


def software_versions(distributions: Iterable[str]) -> dict[str, str | None]:
    versions: dict[str, str | None] = {"python": sys.version.split()[0]}
    for name in distributions:
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            versions[name] = None
    return versions


def utc_now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def new_execution_id(stage: str) -> str:
    return f"{stage}-{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}-{uuid.uuid4().hex[:8]}"


def write_json(path: Path, value: Any) -> None:
    """Write JSON through a same-directory temporary file so readers never see a partial file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def staging_directory(final_dir: Path, execution_id: str) -> Path:
    staging = final_dir.parent / ".staging" / f"{final_dir.name}.{execution_id}"
    staging.mkdir(parents=True, exist_ok=False)
    return staging


def publish_directory(staging: Path, final_dir: Path) -> None:
    """Atomically move a complete staging directory to its final artifact path.

    Never replaces an existing artifact: a failed or repeated attempt cannot clobber prior success.
    """
    if final_dir.exists():
        raise FileExistsError(f"artifact already exists and will not be replaced: {final_dir}")
    final_dir.parent.mkdir(parents=True, exist_ok=True)
    os.rename(staging, final_dir)


def discard_directory(staging: Path) -> None:
    if staging.exists():
        shutil.rmtree(staging)


def describe_outputs(artifact_dir: Path, row_counts: Mapping[str, int]) -> list[dict[str, Any]]:
    """Checksums for every file in an artifact directory except the manifest itself."""
    outputs = []
    for path in sorted(p for p in artifact_dir.rglob("*") if p.is_file() and p.name != "manifest.json"):
        relative = path.relative_to(artifact_dir).as_posix()
        outputs.append(
            {
                "path": relative,
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
                "rows": row_counts.get(relative),
            }
        )
    return outputs
