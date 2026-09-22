"""Neighbor-composition tables that define each condition-pooled niche state."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from regkg.config import NicheDefinitionConfig
from regkg.project_data.contexts import NICHE_LABEL
from regkg.project_data.io import SourceDataError, read_header, read_table, require_symbols
from regkg.provenance import stable_id

_FILENAME = re.compile(r"^(?P<cell_type>.+)_knn_(?P<k>\d+)_res(?P<resolution>\d+(?:\.\d+)?)_")


@dataclass(frozen=True)
class NeighborhoodTable:
    definition: NicheDefinitionConfig
    wide: pd.DataFrame
    neighbor_categories: list[str]
    niche_labels: list[str]


def check_filename(path: Path, definition: NicheDefinitionConfig) -> None:
    """Configuration is authoritative; the filename must not contradict it."""
    match = _FILENAME.match(path.name)
    if not match:
        return
    stated = (match["cell_type"], int(match["k"]), float(match["resolution"]))
    configured = (definition.focal_cell_type, definition.k_neighbors, definition.clustering_resolution)
    if stated != configured:
        raise SourceDataError(f"{path.name}: filename states {stated}, configuration states {configured}")


def read_neighborhood(path: Path, definition: NicheDefinitionConfig, row_sum_tolerance: float) -> NeighborhoodTable:
    check_filename(path, definition)
    header = read_header(path, definition.delimiter)
    if header[0] != definition.niche_column:
        raise SourceDataError(f"{path.name}: first column is {header[0]!r}, expected {definition.niche_column!r}")
    categories = header[1:]
    wide = read_table(
        path, definition.delimiter, {definition.niche_column: str, **dict.fromkeys(categories, "float64")}
    )
    niches = wide[definition.niche_column]
    require_symbols(niches, definition.niche_column, path.name)
    if niches.duplicated().any():
        raise SourceDataError(f"{path.name}: duplicate niche rows {niches[niches.duplicated()].tolist()}")
    bad_labels = [label for label in niches if not NICHE_LABEL.match(label)]
    if bad_labels:
        raise SourceDataError(f"{path.name}: niche labels must look like 'niche_<n>': {bad_labels}")
    counts = wide[categories].to_numpy(dtype=np.float64)
    if not np.isfinite(counts).all() or (counts < 0).any():
        raise SourceDataError(f"{path.name}: mean neighbor counts must be finite and nonnegative")
    # Each focal cell has exactly k neighbors, so reported mean counts must sum to k.
    sums = counts.sum(axis=1)
    off = np.abs(sums - definition.k_neighbors) > row_sum_tolerance
    if off.any():
        raise SourceDataError(
            f"{path.name}: rows {niches[off].tolist()} sum to {sums[off].tolist()}, expected {definition.k_neighbors}"
        )
    return NeighborhoodTable(definition, wide, categories, niches.tolist())


def neighborhood_long(
    table: NeighborhoodTable,
    source_id: str,
    niche_state_ids: dict[tuple[str, str], str],
    definition_run_id: str,
    cell_type_ids: dict[str, str],
) -> pd.DataFrame:
    """Long rows for reported categories only; an absent category is unreported, never a zero."""
    definition = table.definition
    rows = []
    for _, source_row in table.wide.iterrows():
        niche_label = source_row[definition.niche_column]
        niche_state_id = niche_state_ids[(definition.focal_cell_type, niche_label)]
        profile_id = stable_id("nprofile", {"niche_state_id": niche_state_id, "source_id": source_id})
        for category in table.neighbor_categories:
            count = float(source_row[category])
            rows.append(
                {
                    "entry_id": stable_id("nentry", {"profile_id": profile_id, "neighbor_cell_type": category}),
                    "profile_id": profile_id,
                    "niche_state_id": niche_state_id,
                    "definition_run_id": definition_run_id,
                    "source_id": source_id,
                    "focal_cell_type": definition.focal_cell_type,
                    "niche_label": niche_label,
                    "neighbor_cell_type_raw": category,
                    "neighbor_cell_type_id": cell_type_ids[category],
                    "mean_neighbor_count": count,
                    "neighbor_fraction": count / definition.k_neighbors,
                    "k_neighbors": definition.k_neighbors,
                    "clustering_resolution": definition.clustering_resolution,
                }
            )
    return pd.DataFrame(rows)
