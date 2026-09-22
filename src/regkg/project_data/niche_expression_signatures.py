"""Yale pooled niche-expression signatures.

These are descriptive Niche2-minus-Niche1 differences of pooled mean log-normalized expression.
They are not log2 fold changes or sample-aware differential expression, so no p-value, FDR, or
significance field is produced.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

from regkg.config import ProjectConfig
from regkg.models import DonorStatus
from regkg.project_data.identities import comparison_id as make_comparison_id
from regkg.project_data.identities import signature_row_id
from regkg.project_data.io import SourceDataError, read_header, read_table, require_symbols

# Explicit source → normalized column map; the header must match these keys exactly.
COLUMN_MAP = {
    "dataset": "dataset_raw",
    "cell_type": "cell_type_raw",
    "condition": "condition",
    "comparison": "comparison_raw",
    "gene": "gene_symbol_raw",
    "mean_log_normalized_expression_niche_1": "mean_expr_niche1",
    "mean_log_normalized_expression_niche_2": "mean_expr_niche2",
    "niche_2_minus_niche_1_mean_log_normalized_expression": "effect_niche2_minus_niche1",
    "pct_expressing_niche_1": "pct_expr_niche1",
    "pct_expressing_niche_2": "pct_expr_niche2",
    "n_cells_niche_1": "n_cells_niche1",
    "n_cells_niche_2": "n_cells_niche2",
    "effect_definition": "effect_definition",
}
TEXT_COLUMNS = ["dataset", "cell_type", "condition", "comparison", "gene", "effect_definition"]
FLOAT_COLUMNS = [
    "mean_log_normalized_expression_niche_1",
    "mean_log_normalized_expression_niche_2",
    "niche_2_minus_niche_1_mean_log_normalized_expression",
    "pct_expressing_niche_1",
    "pct_expressing_niche_2",
]
COUNT_COLUMNS = ["n_cells_niche_1", "n_cells_niche_2"]
KEY_COLUMNS = ["dataset_raw", "cell_type_raw", "condition", "comparison_raw", "gene_symbol_raw"]
GROUP_COLUMNS = ["dataset_raw", "cell_type_raw", "condition", "comparison_raw"]
# The value columns are fixed to niche_2 (case) and niche_1 (reference); any other comparison
# string would contradict their meaning.
SUPPORTED_COMPARISON = re.compile(r"^(?P<case>niche_2)_vs_(?P<reference>niche_1)$")
EXPRESSION_UNIT = "mean log-normalized expression"
FRACTION_UNIT = "fraction of cells expressing, [0, 1]"


def effect_mismatch(
    mean1: np.ndarray, mean2: np.ndarray, effect: np.ndarray, abs_tol: float, rel_tol: float
) -> np.ndarray:
    """Vectorized math.isclose(effect, mean2 - mean1)."""
    expected = mean2 - mean1
    tolerance = np.maximum(rel_tol * np.maximum(np.abs(effect), np.abs(expected)), abs_tol)
    return np.abs(effect - expected) > tolerance


def read_signatures(path: Path, delimiter: str) -> pd.DataFrame:
    header = read_header(path, delimiter)
    if set(header) != set(COLUMN_MAP):
        raise SourceDataError(
            f"{path.name}: unexpected columns; missing {sorted(set(COLUMN_MAP) - set(header))}, "
            f"extra {sorted(set(header) - set(COLUMN_MAP))}"
        )
    # Counts are read as float first so a fractional count is detected rather than truncated.
    dtypes = {**dict.fromkeys(TEXT_COLUMNS, str), **dict.fromkeys(FLOAT_COLUMNS + COUNT_COLUMNS, "float64")}
    frame = read_table(path, delimiter, dtypes).rename(columns=COLUMN_MAP)
    for column in ["dataset_raw", "cell_type_raw", "condition", "comparison_raw", "gene_symbol_raw"]:
        require_symbols(frame[column], column, path.name)
    return frame


def validate_signatures(frame: pd.DataFrame, config: ProjectConfig, source: str) -> None:
    tolerances = config.tolerances
    numeric = frame[[COLUMN_MAP[c] for c in FLOAT_COLUMNS + COUNT_COLUMNS]].to_numpy(dtype=np.float64)
    if not np.isfinite(numeric).all():
        raise SourceDataError(f"{source}: non-finite numeric values")
    datasets = sorted(set(frame["dataset_raw"]) - {config.dataset.name})
    if datasets:
        raise SourceDataError(f"{source}: dataset values {datasets} differ from configured {config.dataset.name!r}")
    comparisons = sorted(c for c in set(frame["comparison_raw"]) if not SUPPORTED_COMPARISON.match(c))
    if comparisons:
        raise SourceDataError(f"{source}: unsupported comparisons {comparisons}; columns define niche_2 minus niche_1")
    if frame["effect_definition"].str.strip().eq("").any():
        raise SourceDataError(f"{source}: blank effect_definition")

    mismatch = effect_mismatch(
        frame["mean_expr_niche1"].to_numpy(),
        frame["mean_expr_niche2"].to_numpy(),
        frame["effect_niche2_minus_niche1"].to_numpy(),
        tolerances.signature_effect_abs,
        tolerances.signature_effect_rel,
    )
    if mismatch.any():
        raise SourceDataError(
            f"{source}: {int(mismatch.sum())} rows where effect != mean_niche_2 - mean_niche_1, "
            f"first data rows {frame.index[mismatch][:5].tolist()}"
        )
    for column in ["pct_expr_niche1", "pct_expr_niche2"]:
        values = frame[column]
        if ((values < 0) | (values > 1)).any():
            raise SourceDataError(f"{source}: {column} must be a fraction in [0, 1]")
    for column in ["n_cells_niche1", "n_cells_niche2"]:
        values = frame[column]
        if ((values < 0) | (values != np.floor(values))).any():
            raise SourceDataError(f"{source}: {column} must hold nonnegative integers")
    duplicates = frame.duplicated(KEY_COLUMNS, keep=False)
    if duplicates.any():
        examples = frame.loc[duplicates, KEY_COLUMNS].head(5).to_dict("records")
        raise SourceDataError(f"{source}: {int(duplicates.sum())} rows share a signature key, e.g. {examples}")
    # Cell counts describe the niche groups, so they must be constant within each group.
    varying = frame.groupby(GROUP_COLUMNS)[["n_cells_niche1", "n_cells_niche2"]].nunique().gt(1).any(axis=1)
    if varying.any():
        raise SourceDataError(f"{source}: cell counts vary within groups {varying[varying].index.tolist()}")


def signature_table(
    frame: pd.DataFrame,
    source_id: str,
    dataset_id: str,
    cell_type_ids: dict[str, str],
    context_ids: dict[tuple[str, str], str],
    niche_state_ids: dict[tuple[str, str], str],
    gene_ids: dict[str, str],
) -> pd.DataFrame:
    comparisons = {}
    for cell_type, condition, comparison in (
        frame[["cell_type_raw", "condition", "comparison_raw"]].drop_duplicates().itertuples(index=False)
    ):
        match = SUPPORTED_COMPARISON.match(comparison)
        for niche in (match["case"], match["reference"]):
            if (cell_type, niche) not in niche_state_ids:
                raise SourceDataError(f"signature group {cell_type}/{condition} references undefined niche {niche}")
        case_id = niche_state_ids[(cell_type, match["case"])]
        reference_id = niche_state_ids[(cell_type, match["reference"])]
        comparison_id = make_comparison_id(
            dataset_id,
            cell_type_ids[cell_type],
            condition,
            context_ids[(cell_type, condition)],
            case_id,
            reference_id,
        )
        comparisons[(cell_type, condition, comparison)] = (comparison_id, case_id, reference_id)

    keys = list(zip(frame["cell_type_raw"], frame["condition"], frame["comparison_raw"], strict=True))
    comparison_ids = [comparisons[key][0] for key in keys]
    genes = [gene_ids[symbol] for symbol in frame["gene_symbol_raw"]]
    return pd.DataFrame(
        {
            "signature_row_id": [signature_row_id(source_id, c, g) for c, g in zip(comparison_ids, genes, strict=True)],
            "comparison_id": comparison_ids,
            "source_id": source_id,
            "source_row_index": frame.index.to_numpy(dtype=np.int64),
            "dataset_raw": frame["dataset_raw"].to_numpy(),
            "cell_type_raw": frame["cell_type_raw"].to_numpy(),
            "cell_type_id": frame["cell_type_raw"].map(cell_type_ids).to_numpy(),
            "condition": frame["condition"].to_numpy(),
            "context_id": [context_ids[(cell_type, condition)] for cell_type, condition, _ in keys],
            "comparison_raw": frame["comparison_raw"].to_numpy(),
            "case_niche_state_id": [comparisons[key][1] for key in keys],
            "reference_niche_state_id": [comparisons[key][2] for key in keys],
            "gene_symbol_raw": frame["gene_symbol_raw"].to_numpy(),
            "gene_id": genes,
            "mean_expr_niche1": frame["mean_expr_niche1"].to_numpy(),
            "mean_expr_niche2": frame["mean_expr_niche2"].to_numpy(),
            "effect_niche2_minus_niche1": frame["effect_niche2_minus_niche1"].to_numpy(),
            "pct_expr_niche1": frame["pct_expr_niche1"].to_numpy(),
            "pct_expr_niche2": frame["pct_expr_niche2"].to_numpy(),
            "n_cells_niche1": frame["n_cells_niche1"].to_numpy(dtype=np.int64),
            "n_cells_niche2": frame["n_cells_niche2"].to_numpy(dtype=np.int64),
            "effect_definition": frame["effect_definition"].to_numpy(),
            "expression_unit": EXPRESSION_UNIT,
            "fraction_unit": FRACTION_UNIT,
        }
    )


def sampling_coverage(signatures: pd.DataFrame) -> pd.DataFrame:
    """Cell counts per compared niche group. Donor coverage is not supplied and stays null."""
    groups = signatures.drop_duplicates("comparison_id")
    rows = []
    for group in groups.itertuples(index=False):
        match = SUPPORTED_COMPARISON.match(group.comparison_raw)
        for role, niche, state_id, n_cells in (
            ("reference", match["reference"], group.reference_niche_state_id, group.n_cells_niche1),
            ("case", match["case"], group.case_niche_state_id, group.n_cells_niche2),
        ):
            rows.append(
                {
                    "comparison_id": group.comparison_id,
                    "dataset_raw": group.dataset_raw,
                    "cell_type": group.cell_type_raw,
                    "condition": group.condition,
                    "niche_label": niche,
                    "niche_state_id": state_id,
                    "role_in_comparison": role,
                    "n_cells": int(n_cells),
                    "n_donors": None,
                    "donor_status": DonorStatus.NOT_SUPPLIED.value,
                }
            )
    return pd.DataFrame(rows)
