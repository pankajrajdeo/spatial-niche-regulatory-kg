"""Shared enums, small record contracts, and the Arrow schemas of every P1 table."""

from __future__ import annotations

from enum import StrEnum

import pyarrow as pa
from pydantic import BaseModel, ConfigDict

# 2: definition IDs qualified by neighborhood source; observation/comparison IDs qualified by
# resolved context and niche; context identity includes disease (P1 review R1/R2).
SCHEMA_VERSION = "p1-project-data-2"


class InputMode(StrEnum):
    REAL = "real"
    FIXTURE = "fixture"


class StageStatus(StrEnum):
    SUCCEEDED = "SUCCEEDED"
    REUSED = "REUSED"
    PARTIAL = "PARTIAL"
    FAILED = "FAILED"


class ScoreSemanticsStatus(StrEnum):
    # ChromLinker transform, zero meaning, and TF aggregation have not been supplied.
    UNCONFIRMED = "unconfirmed"


class MappingStatus(StrEnum):
    UNRESOLVED_EXTERNAL_ID = "unresolved_external_id"


class DiseaseStatus(StrEnum):
    STATED = "stated"
    NOT_SPECIFIED = "not_specified"


class DonorStatus(StrEnum):
    NOT_SUPPLIED = "not_supplied"


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SourceFile(Record):
    source_id: str
    role: str
    path: str
    sha256: str
    bytes: int
    format: str
    delimiter: str
    n_data_rows: int
    n_columns: int
    columns: list[str]
    key_columns: list[str]
    duplicate_key_count: int
    nonfinite_value_count: int
    numeric_min: float | None
    numeric_max: float | None
    zero_value_count: int | None


class CheckResult(Record):
    name: str
    passed: bool
    detail: str


# ---------------------------------------------------------------------------
# Arrow schemas. Tables are validated against these on write (column set, order, and type).

GENES = pa.schema(
    [
        ("gene_id", pa.string()),
        ("species", pa.string()),
        ("ncbi_taxon_id", pa.int64()),
        ("source_symbol", pa.string()),
        ("normalized_symbol", pa.string()),
        ("approved_symbol", pa.string()),
        ("hgnc_id", pa.string()),
        ("ensembl_gene_id", pa.string()),
        ("ncbi_gene_id", pa.string()),
        ("mapping_status", pa.string()),
        ("mapping_source", pa.string()),
        ("mapping_version", pa.string()),
        ("is_tf", pa.bool_()),
        ("is_tf_source", pa.string()),
        ("in_chromlinker_tf", pa.bool_()),
        ("in_chromlinker_target", pa.bool_()),
        ("in_expression", pa.bool_()),
        ("in_niche_signatures", pa.bool_()),
        ("suffix_variant_base_symbol", pa.string()),
    ]
)

CELL_TYPES = pa.schema(
    [
        ("cell_type_id", pa.string()),
        ("dataset_id", pa.string()),
        ("label", pa.string()),
        ("raw_label", pa.string()),
        ("display_label", pa.string()),
        ("ontology_id", pa.string()),
        ("is_niche_focal_type", pa.bool_()),
    ]
)

NICHE_STATES = pa.schema(
    [
        ("niche_state_id", pa.string()),
        ("dataset_id", pa.string()),
        ("definition_run_id", pa.string()),
        ("focal_cell_type_id", pa.string()),
        ("focal_cell_type", pa.string()),
        ("niche_label", pa.string()),
        ("condition_pooled", pa.bool_()),
        ("conditions_used_for_clustering", pa.list_(pa.string())),
        ("k_neighbors", pa.int64()),
        ("clustering_resolution", pa.float64()),
        ("definition_method", pa.string()),
        ("neighborhood_source_id", pa.string()),
    ]
)

BIOLOGICAL_CONTEXTS = pa.schema(
    [
        ("context_id", pa.string()),
        ("dataset_id", pa.string()),
        ("species", pa.string()),
        ("tissue", pa.string()),
        ("cell_type_id", pa.string()),
        ("cell_type", pa.string()),
        ("condition", pa.string()),
        ("disease", pa.string()),
        ("disease_status", pa.string()),
        ("model_system", pa.string()),
    ]
)

CONTEXTS = pa.schema(
    [
        ("context_label_raw", pa.string()),
        ("condition_raw", pa.string()),
        ("cell_type_raw", pa.string()),
        ("niche_label", pa.string()),
        ("context_id", pa.string()),
        ("cell_type_id", pa.string()),
        ("niche_state_id", pa.string()),
        ("in_expression", pa.bool_()),
        ("in_chromlinker", pa.bool_()),
    ]
)

CHROMLINKER_OBSERVATIONS = pa.schema(
    [
        ("observation_id", pa.string()),
        ("source_id", pa.string()),
        ("source_row_index", pa.int64()),
        ("tf_symbol_raw", pa.string()),
        ("tf_gene_id", pa.string()),
        ("target_symbol_raw", pa.string()),
        ("target_gene_id", pa.string()),
        ("context_label_raw", pa.string()),
        ("context_id", pa.string()),
        ("niche_state_id", pa.string()),
        ("condition", pa.string()),
        ("cell_type_id", pa.string()),
        ("raw_score", pa.float64()),
        ("score_label", pa.string()),
        ("score_semantics_status", pa.string()),
    ]
)

EXPRESSION_OBSERVATIONS = pa.schema(
    [
        ("observation_id", pa.string()),
        ("source_id", pa.string()),
        ("source_row_index", pa.int64()),
        ("gene_symbol_raw", pa.string()),
        ("gene_id", pa.string()),
        ("context_label_raw", pa.string()),
        ("context_id", pa.string()),
        ("niche_state_id", pa.string()),
        ("condition", pa.string()),
        ("cell_type_id", pa.string()),
        ("value", pa.float64()),
        ("value_unit", pa.string()),
    ]
)

NEIGHBORHOOD_PROFILES = pa.schema(
    [
        ("entry_id", pa.string()),
        ("profile_id", pa.string()),
        ("niche_state_id", pa.string()),
        ("definition_run_id", pa.string()),
        ("source_id", pa.string()),
        ("focal_cell_type", pa.string()),
        ("niche_label", pa.string()),
        ("neighbor_cell_type_raw", pa.string()),
        ("neighbor_cell_type_id", pa.string()),
        ("mean_neighbor_count", pa.float64()),
        ("neighbor_fraction", pa.float64()),
        ("k_neighbors", pa.int64()),
        ("clustering_resolution", pa.float64()),
    ]
)

NICHE_EXPRESSION_SIGNATURES = pa.schema(
    [
        ("signature_row_id", pa.string()),
        ("comparison_id", pa.string()),
        ("source_id", pa.string()),
        ("source_row_index", pa.int64()),
        ("dataset_raw", pa.string()),
        ("cell_type_raw", pa.string()),
        ("cell_type_id", pa.string()),
        ("condition", pa.string()),
        ("context_id", pa.string()),
        ("comparison_raw", pa.string()),
        ("case_niche_state_id", pa.string()),
        ("reference_niche_state_id", pa.string()),
        ("gene_symbol_raw", pa.string()),
        ("gene_id", pa.string()),
        ("mean_expr_niche1", pa.float64()),
        ("mean_expr_niche2", pa.float64()),
        ("effect_niche2_minus_niche1", pa.float64()),
        ("pct_expr_niche1", pa.float64()),
        ("pct_expr_niche2", pa.float64()),
        ("n_cells_niche1", pa.int64()),
        ("n_cells_niche2", pa.int64()),
        ("effect_definition", pa.string()),
        ("expression_unit", pa.string()),
        ("fraction_unit", pa.string()),
    ]
)

SAMPLING_COVERAGE = pa.schema(
    [
        ("comparison_id", pa.string()),
        ("dataset_raw", pa.string()),
        ("cell_type", pa.string()),
        ("condition", pa.string()),
        ("niche_label", pa.string()),
        ("niche_state_id", pa.string()),
        ("role_in_comparison", pa.string()),
        ("n_cells", pa.int64()),
        ("n_donors", pa.int64()),
        ("donor_status", pa.string()),
    ]
)

TABLE_SCHEMAS: dict[str, pa.Schema] = {
    "genes.parquet": GENES,
    "cell_types.parquet": CELL_TYPES,
    "niche_states.parquet": NICHE_STATES,
    "biological_contexts.parquet": BIOLOGICAL_CONTEXTS,
    "contexts.parquet": CONTEXTS,
    "chromlinker_observations.parquet": CHROMLINKER_OBSERVATIONS,
    "expression_observations.parquet": EXPRESSION_OBSERVATIONS,
    "neighborhood_profiles.parquet": NEIGHBORHOOD_PROFILES,
    "niche_expression_signatures.parquet": NICHE_EXPRESSION_SIGNATURES,
    "sampling_coverage.parquet": SAMPLING_COVERAGE,
}
