"""Arrow schemas of every P2 table (P1 schemas stay in regkg.models, unchanged)."""

from __future__ import annotations

import pyarrow as pa

CANDIDATE_SCHEMA_VERSION = "p2-candidates-2"

S, F, INT, B = pa.string(), pa.float64(), pa.int64(), pa.bool_()
STRINGS = pa.list_(pa.string())

GENE_MAPPINGS = pa.schema(
    [
        ("gene_id", S),
        ("source_symbol", S),
        ("species", S),
        ("mapping_status", S),
        ("match_route", S),
        ("hgnc_id", S),
        ("approved_symbol", S),
        ("ncbi_gene_id", S),
        ("ensembl_gene_id", S),
        ("locus_group", S),
        ("candidate_hgnc_ids", STRINGS),
        ("conflicting_gene_ids", STRINGS),
        ("mapping_source", S),
        ("mapping_version", S),
        ("mapping_rule_version", S),
    ]
)

MEMBERSHIP = pa.struct(
    [
        ("resource", S),
        ("source_path", S),
        ("source_sha256", S),
        ("source_row_index", INT),
        ("tier", S),
        ("annotations_json", S),
    ]
)
SEED_PUBLICATIONS = pa.schema(
    [
        ("publication_id", S),
        ("pmid", S),
        ("doi", S),
        ("title", S),
        ("year", INT),
        ("journal", S),
        ("first_author", S),
        ("resources", STRINGS),
        ("memberships", pa.list_(MEMBERSHIP)),
        ("metadata_conflict_fields", STRINGS),
        ("evidence_status", S),
    ]
)

PRIOR_INTERACTIONS = pa.schema(
    [
        ("prior_interaction_id", S),
        ("resource", S),
        ("resource_version", S),
        ("resource_doi", S),
        ("snapshot_sha256", S),
        ("license", S),
        ("retrieved_at", S),
        ("source_row_index", INT),
        ("regulator_symbol_raw", S),
        ("regulator_type", S),
        ("regulator_mapping_status", S),
        ("regulator_match_route", S),
        ("regulator_candidate_hgnc_ids", STRINGS),
        ("regulator_hgnc_id", S),
        ("regulator_approved_symbol", S),
        ("target_symbol_raw", S),
        ("target_mapping_status", S),
        ("target_match_route", S),
        ("target_candidate_hgnc_ids", STRINGS),
        ("target_hgnc_id", S),
        ("target_approved_symbol", S),
        ("source_weight", F),
        ("sign", S),
        ("sign_basis", S),
        ("pmids", STRINGS),
        ("other_references", STRINGS),
        ("component_resources", STRINGS),
        ("pair_record_count", INT),
        ("pair_signs_disagree", B),
        ("regulator_key", S),
        ("ulm_exclusion_reason", S),
    ]
)

COMPARISONS = pa.schema(
    [
        ("comparison_id", S),
        ("cell_type", S),
        ("condition", S),
        ("case_niche_state_id", S),
        ("reference_niche_state_id", S),
        ("comparison_view", S),
        ("effect_definition", S),
        ("signature_genes", INT),
        ("resolved_finite_genes", INT),
        ("excluded_unresolved", INT),
        ("excluded_ambiguous", INT),
        ("excluded_conflicting_duplicate_mapping", INT),
        ("excluded_nonfinite", INT),
    ]
)

COMPARISON_VECTORS = pa.schema(
    [("comparison_id", S), ("approved_symbol", S), ("gene_id", S), ("effect_niche2_minus_niche1", F)]
)

CONCORDANCE = pa.schema(
    [
        ("comparison_id", S),
        ("condition", S),
        ("case_niche_state_id", S),
        ("reference_niche_state_id", S),
        ("comparison_view", S),
        ("sign_policy", S),
        ("regulator_key", S),
        ("regulator_type", S),
        ("regulator_hgnc_id", S),
        ("prior_universe_targets", INT),
        ("observed_targets", INT),
        ("vector_genes", INT),
        ("min_targets", INT),
        ("eligible", B),
        ("ulm_score", F),
        ("concordance_direction", S),
        ("method", S),
        ("method_version", S),
    ]
)

CANDIDATES = pa.schema(
    [
        ("candidate_id", S),
        ("comparison_id", S),
        ("condition", S),
        ("case_niche_state_id", S),
        ("reference_niche_state_id", S),
        ("target_niche_state_id", S),
        ("tf_hgnc_id", S),
        ("regulator_scope", S),
        ("reasons", STRINGS),
        ("is_seed", B),
        ("in_prior", B),
        ("prior_universe_targets", INT),
        ("observed_prior_targets", INT),
        ("concordance_eligible", B),
        ("ulm_score", F),
        ("concordance_direction", S),
        ("concordance_selection_rank", INT),
        ("rule_version", S),
        ("tf_gene_id", S),
        ("tf_symbol", S),
        ("score_semantics_status", S),
        ("connectivity_rank", INT),
        ("interpreted_connectivity_delta", F),
        ("tf_in_chromlinker", B),
        ("chromlinker_target_count", INT),
        ("chromlinker_case_context_label", S),
        ("chromlinker_case_observations", INT),
        ("chromlinker_case_nonzero", INT),
        ("chromlinker_case_min", F),
        ("chromlinker_case_median", F),
        ("chromlinker_case_max", F),
        ("tf_cptt_case", F),
        ("chromlinker_reference_context_label", S),
        ("chromlinker_reference_observations", INT),
        ("chromlinker_reference_nonzero", INT),
        ("chromlinker_reference_min", F),
        ("chromlinker_reference_median", F),
        ("chromlinker_reference_max", F),
        ("tf_cptt_reference", F),
        ("tf_signature_mean_expr_niche1", F),
        ("tf_signature_mean_expr_niche2", F),
        ("tf_signature_effect_niche2_minus_niche1", F),
        ("tf_signature_pct_expr_niche1", F),
        ("tf_signature_pct_expr_niche2", F),
        ("missing_component_reasons", STRINGS),
    ]
)

CANDIDATE_CHROMLINKER = pa.schema(
    [
        ("candidate_id", S),
        ("niche_role", S),
        ("observation_id", S),
        ("target_gene_id", S),
        ("context_label_raw", S),
        ("raw_score", F),
        ("score_semantics_status", S),
    ]
)

CANDIDATE_TARGETS = pa.schema(
    [
        ("candidate_id", S),
        ("comparison_id", S),
        ("tf_hgnc_id", S),
        ("target_rank", INT),
        ("target_gene_id", S),
        ("target_hgnc_id", S),
        ("target_symbol", S),
        ("effect_niche2_minus_niche1", F),
        ("source_routes", STRINGS),
        ("prior_interaction_ids", STRINGS),
        ("prior_signs", STRINGS),
        ("eligible_pool_size", INT),
        ("selection_basis", S),
    ]
)

RETRIEVAL_QUEUE = pa.schema(
    [
        ("query_id", S),
        ("query_type", S),
        ("query_text", S),
        ("terms_json", S),
        ("tf_hgnc_id", S),
        ("tf_symbol", S),
        ("target_hgnc_id", S),
        ("target_symbol", S),
        ("candidate_ids", STRINGS),
        ("comparison_ids", STRINGS),
        ("conditions", STRINGS),
        ("reasons", STRINGS),
        ("source_routes", STRINGS),
        ("best_target_rank", INT),
        ("max_abs_effect", F),
        ("is_seed_tf", B),
        ("tf_query_position", INT),
        ("priority", INT),
        ("in_initial_live_slice", B),
        ("search_status", S),
        ("date_restriction", S),
        ("query_version", S),
    ]
)

TABLE_SCHEMAS: dict[str, pa.Schema] = {
    "gene_mappings.parquet": GENE_MAPPINGS,
    "seed_publications.parquet": SEED_PUBLICATIONS,
    "prior_interactions.parquet": PRIOR_INTERACTIONS,
    "comparisons.parquet": COMPARISONS,
    "comparison_vectors.parquet": COMPARISON_VECTORS,
    "concordance.parquet": CONCORDANCE,
    "candidates.parquet": CANDIDATES,
    "candidate_chromlinker_observations.parquet": CANDIDATE_CHROMLINKER,
    "candidate_targets.parquet": CANDIDATE_TARGETS,
    "retrieval_queue.parquet": RETRIEVAL_QUEUE,
}


# ---------------------------------------------------------------------------
# Manuscript-scope extension (P2.11-P2.13). The baseline schemas above stay unchanged so the
# accepted AT1 artifact remains verifiable; these add explicit lineage/comparison identity.

MANUSCRIPT_SCHEMA_VERSION = "p2-manuscript-1"


def _extend(schema: pa.Schema, fields: list[tuple[str, pa.DataType]]) -> pa.Schema:
    return pa.schema(list(schema) + [pa.field(name, kind) for name, kind in fields])


M_COMPARISONS = _extend(
    COMPARISONS,
    [
        ("comparison_role", S),  # primary_regulatory | signature_only_not_primary
        ("chromlinker_case_context_label", S),
        ("chromlinker_reference_context_label", S),
        ("regulatory_context_status", S),  # both_supplied | case_missing | reference_missing | none_supplied
    ],
)
M_CONCORDANCE = _extend(CONCORDANCE, [("cell_type", S)])
M_CANDIDATES = _extend(CANDIDATES, [("cell_type", S), ("scope_version", S)])
M_TARGETS = _extend(CANDIDATE_TARGETS, [("cell_type", S)])
M_QUEUE = _extend(
    RETRIEVAL_QUEUE,
    [
        ("cell_type", S),
        ("scope_version", S),
        ("lineage_priority", INT),  # order within the lineage's own queue
        ("schedule_position", INT),  # equals `priority`: the fair cross-lineage order
        ("batch_index", INT),
    ],
)
LINEAGE_TF_MEMBERSHIPS = pa.schema(
    [
        ("membership_id", S),
        ("cell_type", S),
        ("tf_symbol_raw", S),
        ("tf_hgnc_id", S),
        ("tf_approved_symbol", S),
        ("tf_gene_id", S),
        ("primary_comparison_ids", STRINGS),
        ("conditions", STRINGS),
        ("candidate_ids", STRINGS),
        ("in_prior", B),
        ("concordance_eligible_comparisons", STRINGS),
        ("tf_in_chromlinker", B),
        ("target_count", INT),
        ("query_count", INT),
        ("missing_component_reasons", STRINGS),
        ("scope_version", S),
    ]
)

MANUSCRIPT_TABLE_SCHEMAS: dict[str, pa.Schema] = {
    "gene_mappings.parquet": GENE_MAPPINGS,
    "seed_publications.parquet": SEED_PUBLICATIONS,
    "prior_interactions.parquet": PRIOR_INTERACTIONS,
    "comparisons.parquet": M_COMPARISONS,
    "comparison_vectors.parquet": COMPARISON_VECTORS,
    "concordance.parquet": M_CONCORDANCE,
    "candidates.parquet": M_CANDIDATES,
    "candidate_chromlinker_observations.parquet": CANDIDATE_CHROMLINKER,
    "candidate_targets.parquet": M_TARGETS,
    "retrieval_queue.parquet": M_QUEUE,
    "lineage_tf_memberships.parquet": LINEAGE_TF_MEMBERSHIPS,
}
