"""Advisor corpus reconciliation: the accepted P2 seed table against the supplied source lists.

Counts are recomputed from the source files. Any PMID or list membership present on one side
only, or a source checksum that differs from the one P2 recorded, fails reconciliation.
"""

from __future__ import annotations

import csv
import io
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from regkg.literature.publications import normalize_pmid
from regkg.provenance import sha256_file


class AdvisorReconciliationError(ValueError):
    """The P2 advisor table and the supplied source lists disagree."""


@dataclass(frozen=True)
class AdvisorReconciliation:
    unique_pmids: int
    memberships: int
    per_list: dict[str, int]
    in_several_lists: int
    source_sha256: dict[str, str]


def reconcile_advisors(seeds: pd.DataFrame, lists: dict[str, str], repo_root: Path) -> AdvisorReconciliation:
    """`lists` maps each source path (repository-relative) to the SHA-256 P2 recorded for it."""
    source_members: set[tuple[str, str, int]] = set()
    for path, recorded in sorted(lists.items()):
        actual = sha256_file(repo_root / path)
        if actual != recorded:
            raise AdvisorReconciliationError(f"{path}: SHA-256 {actual[:12]} differs from P2's {recorded[:12]}")
        text = (repo_root / path).read_text(encoding="utf-8-sig")
        for index, row in enumerate(csv.DictReader(io.StringIO(text))):
            pmid = normalize_pmid(row.get("pmid"))
            if pmid is None:
                raise AdvisorReconciliationError(f"{path} row {index}: no valid PMID ({row.get('pmid')!r})")
            source_members.add((pmid, path, index))
    table_members = {
        (str(row.pmid), m["source_path"], int(m["source_row_index"]))
        for row in seeds.itertuples(index=False)
        for m in row.memberships
    }
    source_pmids, table_pmids = {m[0] for m in source_members}, set(seeds["pmid"].astype(str))
    problems = {
        "pmids_missing_from_p2": sorted(source_pmids - table_pmids),
        "pmids_not_in_sources": sorted(table_pmids - source_pmids),
        "memberships_missing_from_p2": sorted(source_members - table_members)[:10],
        "memberships_not_in_sources": sorted(table_members - source_members)[:10],
    }
    if any(problems.values()) or not seeds["pmid"].is_unique:
        raise AdvisorReconciliationError(f"advisor reconciliation failed: {problems}")
    per_list = pd.Series([m[1] for m in source_members]).value_counts().sort_index().to_dict()
    lists_per_pmid = pd.Series([m[0] for m in source_members]).value_counts()
    return AdvisorReconciliation(
        unique_pmids=len(source_pmids),
        memberships=len(source_members),
        per_list={k: int(v) for k, v in per_list.items()},
        in_several_lists=int((lists_per_pmid > 1).sum()),
        source_sha256=dict(sorted(lists.items())),
    )
