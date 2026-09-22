"""Advisor-selected paper lists: publication metadata only, never accepted scientific findings."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from regkg.project_data.io import READ_OPTIONS, SourceDataError, read_header
from regkg.provenance import sha256_file, stable_id

SHARED_FIELDS = ["year", "journal", "first_author", "title", "doi"]
EVIDENCE_STATUS = "seed_metadata_not_evidence"


@dataclass(frozen=True)
class SeedList:
    resource: str
    path: Path
    relative: str


def read_seed_list(seed: SeedList) -> pd.DataFrame:
    header = read_header(seed.path, ",")
    required = {"tier", "pmid", *SHARED_FIELDS}
    if not required <= set(header):
        raise SourceDataError(f"{seed.relative}: missing columns {sorted(required - set(header))}")
    frame = pd.read_csv(seed.path, dtype=str, **READ_OPTIONS)
    bad = frame.loc[~frame["pmid"].str.fullmatch(r"[1-9]\d*"), "pmid"].tolist()
    if bad:
        raise SourceDataError(f"{seed.relative}: non-numeric PMIDs {bad[:5]}")
    duplicated = frame.loc[frame["pmid"].duplicated(keep=False), "pmid"].unique().tolist()
    if duplicated:
        raise SourceDataError(f"{seed.relative}: PMIDs listed more than once {duplicated[:5]}")
    return frame


def seed_publications(seeds: list[SeedList]) -> tuple[pd.DataFrame, list[dict]]:
    """One row per PMID; every list membership and its full annotation row is retained.

    Disagreeing shared metadata across lists is reported, not resolved by picking one value.
    """
    memberships: dict[str, list[dict]] = {}
    for seed in seeds:
        frame = read_seed_list(seed)
        for index, row in frame.iterrows():
            memberships.setdefault(row["pmid"], []).append(
                {
                    "resource": seed.resource,
                    "source_path": seed.relative,
                    "source_sha256": sha256_file(seed.path),
                    "source_row_index": int(index),
                    "tier": row["tier"],
                    "annotations_json": json.dumps(row.to_dict(), sort_keys=True, ensure_ascii=False),
                }
            )
    rows, conflicts = [], []
    for pmid in sorted(memberships, key=int):
        entries = memberships[pmid]
        values = {field: [json.loads(e["annotations_json"])[field] for e in entries] for field in SHARED_FIELDS}
        for field, observed in values.items():
            if len(set(observed)) > 1:
                conflicts.append({"pmid": pmid, "field": field, "values": observed})
        consistent = {field: (observed[0] if len(set(observed)) == 1 else None) for field, observed in values.items()}
        rows.append(
            {
                "publication_id": stable_id("publication", {"pmid": pmid}),
                "pmid": pmid,
                "doi": consistent["doi"] or None,
                "title": consistent["title"],
                "year": int(consistent["year"]) if consistent["year"] else None,
                "journal": consistent["journal"],
                "first_author": consistent["first_author"],
                "resources": sorted({e["resource"] for e in entries}),
                "memberships": entries,
                "metadata_conflict_fields": sorted(f for f, o in values.items() if len(set(o)) > 1),
                "evidence_status": EVIDENCE_STATUS,
            }
        )
    return pd.DataFrame(rows), conflicts
