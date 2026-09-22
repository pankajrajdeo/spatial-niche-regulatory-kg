"""Semantic identity rules for project-data records, shared by ingestion and verification.

An ID changes whenever a scientific assignment it names changes: a revised niche definition,
biological context, or niche membership yields new IDs instead of mutating payload under an old
one. Execution timestamps, machine paths, and whole artifact keys are never part of an identity.
"""

from __future__ import annotations

import pandas as pd

from regkg.provenance import stable_id


def nullable(value: object) -> str | None:
    """Missing niche membership from a pandas/Arrow column becomes None, never NaN, in an identity."""
    return None if value is None or pd.isna(value) else str(value)


def definition_run_id(
    dataset_id: str,
    focal_cell_type: str,
    k_neighbors: int,
    clustering_resolution: float,
    conditions_pooled: list[str],
    method: str,
    neighborhood_source_id: str,
) -> str:
    """Local, content-qualified niche-definition identifier.

    The supplied neighborhood table (via its content-hashed source ID) is what defines the niches
    here. This is not a recovered Yale clustering-run accession; none was supplied.
    """
    return stable_id(
        "nicherun",
        {
            "dataset_id": dataset_id,
            "focal_cell_type": focal_cell_type,
            "k_neighbors": k_neighbors,
            "clustering_resolution": clustering_resolution,
            "conditions_pooled": sorted(conditions_pooled),
            "method": method,
            "neighborhood_source_id": neighborhood_source_id,
        },
    )


def niche_state_id(dataset_id: str, run_id: str, focal_cell_type_id: str, niche_label: str) -> str:
    # Condition is deliberately absent: niches were clustered from pooled Control and IPF cells.
    return stable_id(
        "niche",
        {
            "dataset_id": dataset_id,
            "definition_run_id": run_id,
            "focal_cell_type_id": focal_cell_type_id,
            "niche_label": niche_label,
        },
    )


def context_id(
    dataset_id: str,
    species: str,
    tissue: str,
    cell_type_id: str,
    condition: str,
    disease: str | None,
    model_system: str,
) -> str:
    """Every stated biological-context fact, including the (nullable) disease annotation."""
    return stable_id(
        "context",
        {
            "dataset_id": dataset_id,
            "species": species,
            "tissue": tissue,
            "cell_type_id": cell_type_id,
            "condition": condition,
            "disease": disease,
            "model_system": model_system,
        },
    )


def comparison_id(
    dataset_id: str,
    cell_type_id: str,
    condition: str,
    context: str,
    case_niche_state_id: str,
    reference_niche_state_id: str,
) -> str:
    return stable_id(
        "comparison",
        {
            "dataset_id": dataset_id,
            "cell_type_id": cell_type_id,
            "condition": condition,
            "context_id": context,
            "case_niche_state_id": case_niche_state_id,
            "reference_niche_state_id": reference_niche_state_id,
        },
    )


def signature_row_id(source_id: str, comparison: str, gene_id: str) -> str:
    return stable_id("signature", {"source_id": source_id, "comparison_id": comparison, "gene_id": gene_id})


def chromlinker_observation_id(
    source_id: str, tf_gene_id: str, target_gene_id: str, context_label: str, context: str, niche: str | None
) -> str:
    return stable_id(
        "chromlinker",
        {
            "source_id": source_id,
            "tf_gene_id": tf_gene_id,
            "target_gene_id": target_gene_id,
            "context_label": context_label,
            "context_id": context,
            "niche_state_id": niche,
        },
    )


def expression_observation_id(source_id: str, gene_id: str, context_label: str, context: str, niche: str | None) -> str:
    return stable_id(
        "expression",
        {
            "source_id": source_id,
            "gene_id": gene_id,
            "context_label": context_label,
            "context_id": context,
            "niche_state_id": niche,
        },
    )
