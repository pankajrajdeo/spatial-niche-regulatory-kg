"""Pseudobulk CPTT expression, preserved as supplied.

CPTT is supporting absolute expression; it is not assumed to share the normalization of the pooled
signature means, and no renormalization or differential expression is computed.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from regkg.config import ExpressionSourceConfig
from regkg.models import EXPRESSION_OBSERVATIONS
from regkg.project_data.identities import expression_observation_id, nullable
from regkg.project_data.io import (
    READ_OPTIONS,
    NumericStats,
    ParquetStream,
    SourceDataError,
    iter_chunks,
    melt_row_major,
    read_header,
    require_symbols,
)


@dataclass(frozen=True)
class ExpressionLayout:
    context_labels: list[str]
    genes: set[str]
    n_rows: int


def read_expression_layout(path: Path, source: ExpressionSourceConfig) -> ExpressionLayout:
    header = read_header(path, source.delimiter)
    if header[0] != source.gene_column:
        raise SourceDataError(f"{path.name}: first column is {header[0]!r}, expected {source.gene_column!r}")
    genes = pd.read_csv(path, sep=source.delimiter, usecols=[source.gene_column], dtype=str, **READ_OPTIONS)[
        source.gene_column
    ]
    require_symbols(genes, source.gene_column, path.name)
    if genes.duplicated().any():
        examples = genes[genes.duplicated(keep=False)].head(5).tolist()
        raise SourceDataError(f"{path.name}: {int(genes.duplicated().sum())} duplicated gene rows, e.g. {examples}")
    return ExpressionLayout(context_labels=header[1:], genes=set(genes), n_rows=len(genes))


def write_expression_observations(
    path: Path,
    source: ExpressionSourceConfig,
    layout: ExpressionLayout,
    source_id: str,
    label_lookup: pd.DataFrame,
    gene_ids: dict[str, str],
    output: Path,
    chunk_rows: int,
) -> NumericStats:
    stats = NumericStats()
    dtypes = {source.gene_column: str, **dict.fromkeys(layout.context_labels, "float64")}
    lookup = label_lookup.loc[layout.context_labels]
    with ParquetStream(output, EXPRESSION_OBSERVATIONS) as stream:
        for chunk in iter_chunks(path, source.delimiter, dtypes, chunk_rows):
            stats.update(chunk[layout.context_labels])
            long = melt_row_major(chunk, [source.gene_column], layout.context_labels)
            gene_id = long[source.gene_column].map(gene_ids)
            context = lookup.loc[long["context_label_raw"]].reset_index(drop=True)
            observation_ids = [
                expression_observation_id(source_id, gene, label, context_id, nullable(niche))
                for gene, label, context_id, niche in zip(
                    gene_id, long["context_label_raw"], context["context_id"], context["niche_state_id"], strict=True
                )
            ]
            stream.write(
                pd.DataFrame(
                    {
                        "observation_id": observation_ids,
                        "source_id": source_id,
                        "source_row_index": long["source_row_index"],
                        "gene_symbol_raw": long[source.gene_column],
                        "gene_id": gene_id,
                        "context_label_raw": long["context_label_raw"],
                        "context_id": context["context_id"],
                        "niche_state_id": context["niche_state_id"],
                        "condition": context["condition"],
                        "cell_type_id": context["cell_type_id"],
                        "value": long["value"],
                        "value_unit": source.value_unit,
                    }
                )
            )
    if stats.nonfinite:
        raise SourceDataError(f"{path.name}: {stats.nonfinite} non-finite expression values")
    if stats.negatives:
        raise SourceDataError(f"{path.name}: {stats.negatives} negative CPTT values")
    return stats
