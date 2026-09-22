"""Deterministic identities and all-or-nothing artifact publication."""

from __future__ import annotations

import math
import subprocess
import sys

import pytest

from regkg.provenance import (
    canonical_json,
    code_fingerprint,
    discard_directory,
    publish_directory,
    sha256_file,
    stable_id,
    staging_directory,
)


def test_stable_id_ignores_key_order_and_separates_namespaces():
    first = stable_id("gene", {"ncbi_taxon_id": 9606, "source_symbol": "TEAD1"})
    assert first == stable_id("gene", {"source_symbol": "TEAD1", "ncbi_taxon_id": 9606})
    assert first != stable_id("celltype", {"ncbi_taxon_id": 9606, "source_symbol": "TEAD1"})
    assert first != stable_id("gene", {"ncbi_taxon_id": 10090, "source_symbol": "TEAD1"})  # species-qualified
    assert first.startswith("gene:") and len(first.split(":")[1]) == 20


def test_stable_id_is_identical_across_processes():
    code = "from regkg.provenance import stable_id; print(stable_id('gene', {'source_symbol': 'KLF5', 'x': [1, 2]}))"
    runs = {
        subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True).stdout
        for _ in range(2)
    }
    assert runs == {stable_id("gene", {"source_symbol": "KLF5", "x": [1, 2]}) + "\n"}


def test_canonical_json_rejects_non_finite_numbers_and_bad_namespaces():
    with pytest.raises(ValueError):
        canonical_json({"value": math.nan})
    with pytest.raises(ValueError):
        stable_id("bad:namespace", {})


def test_publication_is_atomic_and_never_replaces_existing(tmp_path):
    final = tmp_path / "processed" / "ingest-x"
    staging = staging_directory(final, "exec-1")
    (staging / "table.parquet").write_bytes(b"first")
    assert not final.exists()  # nothing visible until the rename
    publish_directory(staging, final)
    assert (final / "table.parquet").read_bytes() == b"first"

    again = staging_directory(final, "exec-2")
    (again / "table.parquet").write_bytes(b"second")
    with pytest.raises(FileExistsError):
        publish_directory(again, final)
    discard_directory(again)
    assert (final / "table.parquet").read_bytes() == b"first"
    assert not again.exists()


def test_code_fingerprint_changes_with_content(tmp_path):
    package = tmp_path / "pkg"
    (package / "sub").mkdir(parents=True)
    (package / "a.py").write_text("x = 1\n")
    (package / "sub" / "b.py").write_text("y = 2\n")
    before = code_fingerprint(package, ["a.py", "sub"])
    assert before == code_fingerprint(package, ["sub", "a.py"])
    (package / "sub" / "b.py").write_text("y = 3\n")
    assert code_fingerprint(package, ["a.py", "sub"]) != before
    assert len(sha256_file(package / "a.py")) == 64
