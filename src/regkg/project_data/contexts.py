"""Context-label parsing and the dataset's cell-type, niche-state, and context identities."""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass

import pandas as pd

from regkg.config import ProjectConfig
from regkg.models import DiseaseStatus
from regkg.project_data.identities import context_id as make_context_id
from regkg.project_data.identities import definition_run_id, niche_state_id
from regkg.project_data.io import SourceDataError
from regkg.provenance import stable_id

_NICHE_SUFFIX = re.compile(r"^(?P<cell_type>.+)_(?P<niche>niche_\d+)$")
NICHE_LABEL = re.compile(r"^niche_\d+$")


@dataclass(frozen=True)
class ContextLabel:
    raw: str
    condition_raw: str
    cell_type_raw: str
    niche_label: str | None


def parse_context_label(label: str) -> ContextLabel:
    """Split at the first period; only a trailing `_niche_<integer>` is niche membership.

    Underscores inside cell-type names (e.g. `Activated_Fibrotic_FBs`) are never split.
    """
    condition, separator, rest = label.partition(".")
    if not separator or not condition or not rest:
        raise SourceDataError(f"context label is not '<condition>.<cell type>': {label!r}")
    match = _NICHE_SUFFIX.match(rest)
    if match:
        return ContextLabel(label, condition, match["cell_type"], match["niche"])
    return ContextLabel(label, condition, rest, None)


@dataclass(frozen=True)
class IdentityRegistry:
    dataset_id: str
    cell_type_ids: dict[str, str]
    definition_run_ids: dict[str, str]
    niche_state_ids: dict[tuple[str, str], str]
    context_ids: dict[tuple[str, str], str]
    labels: dict[str, ContextLabel]
    cell_types: pd.DataFrame
    niche_states: pd.DataFrame
    biological_contexts: pd.DataFrame
    contexts: pd.DataFrame
    unobserved_configured_cell_types: list[str]

    def label_lookup(self) -> pd.DataFrame:
        """Per context label: biological context, niche state (nullable), condition, cell type."""
        return self.contexts.set_index("context_label_raw")[
            ["context_id", "niche_state_id", "condition_raw", "cell_type_id"]
        ].rename(columns={"condition_raw": "condition"})


def dataset_id_for(config: ProjectConfig) -> str:
    return stable_id("dataset", {"name": config.dataset.name})


def build_registry(
    config: ProjectConfig,
    niche_labels_by_focal_type: Mapping[str, list[str]],
    neighborhood_source_ids: Mapping[str, str],
    neighbor_categories: Iterable[str],
    expression_labels: list[str],
    chromlinker_labels: list[str],
    signature_groups: Iterable[tuple[str, str]],
) -> IdentityRegistry:
    dataset = config.dataset
    dataset_id = dataset_id_for(config)
    all_labels = list(dict.fromkeys([*expression_labels, *chromlinker_labels]))
    labels = {label: parse_context_label(label) for label in all_labels}
    signature_groups = sorted(set(signature_groups))

    observed_conditions = {parsed.condition_raw for parsed in labels.values()} | {
        condition for _, condition in signature_groups
    }
    unknown_conditions = sorted(observed_conditions - set(dataset.conditions))
    if unknown_conditions:
        raise SourceDataError(f"conditions not declared in project config: {unknown_conditions}")

    observed_cell_types = (
        {parsed.cell_type_raw for parsed in labels.values()}
        | set(neighbor_categories)
        | {cell_type for cell_type, _ in signature_groups}
        | set(niche_labels_by_focal_type)
    )
    undisplayed = sorted(observed_cell_types - set(config.cell_types))
    if undisplayed:
        raise SourceDataError(f"cell types missing from the curated display map: {undisplayed}")

    focal_types = {definition.focal_cell_type: definition for definition in config.niche_definitions}
    cell_type_ids = {
        label: stable_id("celltype", {"dataset_id": dataset_id, "label": label})
        for label in sorted(observed_cell_types)
    }
    cell_types = pd.DataFrame(
        {
            "cell_type_id": [cell_type_ids[label] for label in cell_type_ids],
            "dataset_id": dataset_id,
            "label": list(cell_type_ids),
            "raw_label": list(cell_type_ids),
            "display_label": [config.cell_types[label].display_name for label in cell_type_ids],
            "ontology_id": [config.cell_types[label].ontology_id for label in cell_type_ids],
            "is_niche_focal_type": [label in focal_types for label in cell_type_ids],
        }
    )

    # Niche identity: dataset + definition run + focal cell type + niche label. Condition is
    # deliberately absent because the clustering pooled Control and IPF cells.
    definition_run_ids: dict[str, str] = {}
    niche_state_ids: dict[tuple[str, str], str] = {}
    niche_rows = []
    for focal, definition in sorted(focal_types.items()):
        if focal not in niche_labels_by_focal_type:
            raise SourceDataError(f"no neighborhood niches were read for configured focal type {focal}")
        run_id = definition_run_id(
            dataset_id,
            focal,
            definition.k_neighbors,
            definition.clustering_resolution,
            definition.conditions_pooled,
            definition.method,
            neighborhood_source_ids[focal],
        )
        definition_run_ids[focal] = run_id
        for niche_label in niche_labels_by_focal_type[focal]:
            niche_id = niche_state_id(dataset_id, run_id, cell_type_ids[focal], niche_label)
            niche_state_ids[(focal, niche_label)] = niche_id
            niche_rows.append(
                {
                    "niche_state_id": niche_id,
                    "dataset_id": dataset_id,
                    "definition_run_id": run_id,
                    "focal_cell_type_id": cell_type_ids[focal],
                    "focal_cell_type": focal,
                    "niche_label": niche_label,
                    "condition_pooled": len(definition.conditions_pooled) > 1,
                    "conditions_used_for_clustering": sorted(definition.conditions_pooled),
                    "k_neighbors": definition.k_neighbors,
                    "clustering_resolution": definition.clustering_resolution,
                    "definition_method": definition.method,
                    "neighborhood_source_id": neighborhood_source_ids[focal],
                }
            )

    for parsed in labels.values():
        if parsed.niche_label is not None and (parsed.cell_type_raw, parsed.niche_label) not in niche_state_ids:
            raise SourceDataError(
                f"context {parsed.raw!r} names a niche absent from the configured neighborhood definitions"
            )

    context_keys = sorted(
        {(parsed.cell_type_raw, parsed.condition_raw) for parsed in labels.values()} | set(signature_groups)
    )
    context_ids = {}
    context_rows = []
    for cell_type, condition in context_keys:
        disease = dataset.conditions[condition].disease
        context_id = make_context_id(
            dataset_id,
            dataset.species,
            dataset.tissue,
            cell_type_ids[cell_type],
            condition,
            disease,
            dataset.model_system,
        )
        context_ids[(cell_type, condition)] = context_id
        context_rows.append(
            {
                "context_id": context_id,
                "dataset_id": dataset_id,
                "species": dataset.species,
                "tissue": dataset.tissue,
                "cell_type_id": cell_type_ids[cell_type],
                "cell_type": cell_type,
                "condition": condition,
                "disease": disease,
                "disease_status": (DiseaseStatus.STATED if disease else DiseaseStatus.NOT_SPECIFIED).value,
                "model_system": dataset.model_system,
            }
        )

    expression_set, chromlinker_set = set(expression_labels), set(chromlinker_labels)
    contexts = pd.DataFrame(
        [
            {
                "context_label_raw": parsed.raw,
                "condition_raw": parsed.condition_raw,
                "cell_type_raw": parsed.cell_type_raw,
                "niche_label": parsed.niche_label,
                "context_id": context_ids[(parsed.cell_type_raw, parsed.condition_raw)],
                "cell_type_id": cell_type_ids[parsed.cell_type_raw],
                "niche_state_id": (
                    niche_state_ids[(parsed.cell_type_raw, parsed.niche_label)] if parsed.niche_label else None
                ),
                "in_expression": parsed.raw in expression_set,
                "in_chromlinker": parsed.raw in chromlinker_set,
            }
            for parsed in labels.values()
        ]
    )

    return IdentityRegistry(
        dataset_id=dataset_id,
        cell_type_ids=cell_type_ids,
        definition_run_ids=definition_run_ids,
        niche_state_ids=niche_state_ids,
        context_ids=context_ids,
        labels=labels,
        cell_types=cell_types,
        niche_states=pd.DataFrame(niche_rows),
        biological_contexts=pd.DataFrame(context_rows),
        contexts=contexts,
        unobserved_configured_cell_types=sorted(set(config.cell_types) - observed_cell_types),
    )
