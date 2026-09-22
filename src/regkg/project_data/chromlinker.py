"""ChromLinker TF→gene connection scores, preserved exactly as supplied.

The score transform, the meaning of zero, and TF-level aggregation are unconfirmed. Every value,
including zeros, becomes one observation; nothing is exponentiated, filtered, ranked, or turned
into a regulatory edge.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from regkg.config import ChromLinkerSourceConfig
from regkg.models import CHROMLINKER_OBSERVATIONS, ScoreSemanticsStatus
from regkg.project_data.identities import chromlinker_observation_id, nullable
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
class ChromLinkerLayout:
    context_labels: list[str]
    tfs: set[str]
    targets: set[str]
    n_rows: int


def read_chromlinker_layout(path: Path, source: ChromLinkerSourceConfig) -> ChromLinkerLayout:
    header = read_header(path, source.delimiter)
    if header[:2] != [source.tf_column, source.target_column]:
        raise SourceDataError(f"{path.name}: first columns are {header[:2]}, expected TF/target columns")
    keys = pd.read_csv(
        path, sep=source.delimiter, usecols=[source.tf_column, source.target_column], dtype=str, **READ_OPTIONS
    )
    for column in (source.tf_column, source.target_column):
        require_symbols(keys[column], column, path.name)
    duplicated = keys.duplicated(keep=False)
    if duplicated.any():
        examples = keys[duplicated].head(5).to_dict("records")
        raise SourceDataError(f"{path.name}: {int(duplicated.sum())} rows share a TF/target pair, e.g. {examples}")
    return ChromLinkerLayout(
        context_labels=header[2:],
        tfs=set(keys[source.tf_column]),
        targets=set(keys[source.target_column]),
        n_rows=len(keys),
    )


def write_chromlinker_observations(
    path: Path,
    source: ChromLinkerSourceConfig,
    layout: ChromLinkerLayout,
    source_id: str,
    label_lookup: pd.DataFrame,
    gene_ids: dict[str, str],
    output: Path,
    chunk_rows: int,
) -> NumericStats:
    stats = NumericStats()
    dtypes = {source.tf_column: str, source.target_column: str, **dict.fromkeys(layout.context_labels, "float64")}
    lookup = label_lookup.loc[layout.context_labels]
    with ParquetStream(output, CHROMLINKER_OBSERVATIONS) as stream:
        for chunk in iter_chunks(path, source.delimiter, dtypes, chunk_rows):
            stats.update(chunk[layout.context_labels])
            long = melt_row_major(chunk, [source.tf_column, source.target_column], layout.context_labels)
            tf_ids = long[source.tf_column].map(gene_ids)
            target_ids = long[source.target_column].map(gene_ids)
            context = lookup.loc[long["context_label_raw"]].reset_index(drop=True)
            observation_ids = [
                chromlinker_observation_id(source_id, tf, target, label, context_id, nullable(niche))
                for tf, target, label, context_id, niche in zip(
                    tf_ids,
                    target_ids,
                    long["context_label_raw"],
                    context["context_id"],
                    context["niche_state_id"],
                    strict=True,
                )
            ]
            stream.write(
                pd.DataFrame(
                    {
                        "observation_id": observation_ids,
                        "source_id": source_id,
                        "source_row_index": long["source_row_index"],
                        "tf_symbol_raw": long[source.tf_column],
                        "tf_gene_id": tf_ids,
                        "target_symbol_raw": long[source.target_column],
                        "target_gene_id": target_ids,
                        "context_label_raw": long["context_label_raw"],
                        "context_id": context["context_id"],
                        "niche_state_id": context["niche_state_id"],
                        "condition": context["condition"],
                        "cell_type_id": context["cell_type_id"],
                        "raw_score": long["value"],
                        "score_label": source.score_label,
                        "score_semantics_status": ScoreSemanticsStatus.UNCONFIRMED.value,
                    }
                )
            )
    if stats.nonfinite:
        raise SourceDataError(f"{path.name}: {stats.nonfinite} non-finite scores")
    return stats
