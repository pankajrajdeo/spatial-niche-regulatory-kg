"""Source reading and schema-checked Parquet writing shared by the project-data parsers."""

from __future__ import annotations

import csv
from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


class SourceDataError(ValueError):
    """A supplied input violates its expected structure or scientific invariants."""


# Symbols such as "NA" or "NULL" are valid gene names; never let pandas turn them into missing values.
# pandas' default float converter can differ from the correctly rounded decimal value by one ULP
# (observed in 619,604 signature cells); round_trip preserves the supplied decimal exactly.
READ_OPTIONS = {"keep_default_na": False, "na_values": [], "na_filter": False, "float_precision": "round_trip"}


def read_header(path: Path, delimiter: str) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        try:
            header = next(csv.reader(handle, delimiter=delimiter))
        except StopIteration as error:
            raise SourceDataError(f"{path.name}: file is empty") from error
    duplicates = sorted(name for name, count in Counter(header).items() if count > 1)
    if duplicates:
        raise SourceDataError(f"{path.name}: duplicate column names {duplicates}")
    if any(not name.strip() for name in header):
        raise SourceDataError(f"{path.name}: empty column name in header")
    if len(header) < 2:
        raise SourceDataError(f"{path.name}: expected a delimited table with {delimiter!r}, got {len(header)} column")
    return header


def _numeric_parse_error(path: Path, error: Exception) -> SourceDataError:
    # With NA detection disabled, blank or "NaN" text in a measurement column cannot parse.
    return SourceDataError(f"{path.name}: non-numeric, blank, or NaN text in a numeric column ({error})")


def read_table(path: Path, delimiter: str, dtypes: dict[str, object]) -> pd.DataFrame:
    try:
        return pd.read_csv(path, sep=delimiter, dtype=dtypes, **READ_OPTIONS)
    except (ValueError, TypeError) as error:
        raise _numeric_parse_error(path, error) from error


def iter_chunks(path: Path, delimiter: str, dtypes: dict[str, object], chunk_rows: int) -> Iterator[pd.DataFrame]:
    """Stream a delimited file in bounded row chunks with a stable 0-based source row index."""
    offset = 0
    reader = pd.read_csv(path, sep=delimiter, dtype=dtypes, chunksize=chunk_rows, **READ_OPTIONS)
    while True:
        try:
            chunk = next(reader)
        except StopIteration:
            return
        except (ValueError, TypeError) as error:
            raise _numeric_parse_error(path, error) from error
        chunk.index = pd.RangeIndex(offset, offset + len(chunk))
        offset += len(chunk)
        yield chunk


def require_symbols(values: pd.Series, column: str, source: str) -> None:
    blank = values.str.strip().eq("") | values.ne(values.str.strip())
    if blank.any():
        rows = values.index[blank][:5].tolist()
        raise SourceDataError(f"{source}: blank or whitespace-padded {column} at data rows {rows}")


@dataclass
class NumericStats:
    """Running arithmetic summaries of a numeric block; used for audit and zero preservation."""

    values: int = 0
    nonfinite: int = 0
    zeros: int = 0
    negatives: int = 0
    minimum: float | None = None
    maximum: float | None = None
    nonzero_by_column: Counter = field(default_factory=Counter)
    values_by_column: Counter = field(default_factory=Counter)

    def update(self, block: pd.DataFrame) -> None:
        matrix = block.to_numpy(dtype=np.float64)
        finite = np.isfinite(matrix)
        self.values += matrix.size
        self.nonfinite += int((~finite).sum())
        self.zeros += int((matrix == 0).sum())
        self.negatives += int((matrix < 0).sum())
        if finite.any():
            low, high = float(matrix[finite].min()), float(matrix[finite].max())
            self.minimum = low if self.minimum is None else min(self.minimum, low)
            self.maximum = high if self.maximum is None else max(self.maximum, high)
        for column, count in zip(block.columns, (matrix != 0).sum(axis=0), strict=True):
            self.nonzero_by_column[column] += int(count)
            self.values_by_column[column] += matrix.shape[0]


def to_arrow(frame: pd.DataFrame, schema: pa.Schema) -> pa.Table:
    """Convert with an exact column set; extra or missing columns are errors, not silent drops."""
    if list(frame.columns) != schema.names:
        raise ValueError(f"table columns {list(frame.columns)} do not match schema {schema.names}")
    table = pa.Table.from_pandas(frame, schema=schema, preserve_index=False)
    return table.replace_schema_metadata(None)


def write_parquet(frame: pd.DataFrame, schema: pa.Schema, path: Path) -> int:
    pq.write_table(to_arrow(frame, schema), path, compression="zstd")
    return len(frame)


class ParquetStream:
    """Append bounded chunks to one Parquet file under a fixed schema."""

    def __init__(self, path: Path, schema: pa.Schema) -> None:
        self.schema = schema
        self.rows = 0
        self._writer = pq.ParquetWriter(path, schema, compression="zstd")

    def write(self, frame: pd.DataFrame) -> None:
        self._writer.write_table(to_arrow(frame, self.schema))
        self.rows += len(frame)

    def close(self) -> None:
        self._writer.close()

    def __enter__(self) -> ParquetStream:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


def melt_row_major(chunk: pd.DataFrame, id_columns: list[str], value_columns: list[str]) -> pd.DataFrame:
    """Wide to long in source order: each source row, then its context columns left to right."""
    values = chunk[value_columns].to_numpy(dtype=np.float64)
    n_rows, n_columns = values.shape
    long = {"source_row_index": np.repeat(chunk.index.to_numpy(dtype=np.int64), n_columns)}
    for column in id_columns:
        long[column] = np.repeat(chunk[column].to_numpy(dtype=object), n_columns)
    long["context_label_raw"] = np.tile(np.array(value_columns, dtype=object), n_rows)
    long["value"] = values.ravel(order="C")
    return pd.DataFrame(long)
