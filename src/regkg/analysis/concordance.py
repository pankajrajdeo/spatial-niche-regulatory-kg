"""AT1 Niche2-vs-Niche1 comparison vectors and signed-regulon ULM concordance.

The ULM score is decoupler's univariate linear-model t-value relating a regulator's signed prior
weights to the descriptive Niche2-minus-Niche1 pooled mean-log-expression contrast. It measures
agreement between a curated prior and a descriptive pattern. It is not TF activity, causal
regulation, or sample-aware differential expression; no p-value from it is used or stored.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from regkg.analysis.gene_mapping import RESOLVED

METHOD = "decoupler.mt.ulm"
# Project analysis choice, not the standard CollecTRI benchmark: CollecTRI records whose sign came
# from literature references or regulon-majority inference. Regulon-inferred signs are not
# edge-specific experimental evidence; "default activation" (+1 assumed) records are excluded.
PRIMARY_POLICY = "literature_or_regulon_sign"
# Standard CollecTRI usage with every assigned weight, including default activation.
SENSITIVITY_POLICY = "sensitivity_collectri_assigned_weights"
COLUMNS = [
    "comparison_id",
    "condition",
    "case_niche_state_id",
    "reference_niche_state_id",
    "comparison_view",
    "sign_policy",
    "regulator_key",
    "regulator_type",
    "regulator_hgnc_id",
    "prior_universe_targets",
    "observed_targets",
    "vector_genes",
    "min_targets",
    "eligible",
    "ulm_score",
    "concordance_direction",
    "method",
    "method_version",
]
COMPARISON_VIEW = "niche2_minus_niche1"  # Niche2 is the case/target niche; Niche1 is the reference.


@dataclass(frozen=True)
class ComparisonVector:
    comparison_id: str
    condition: str
    case_niche_state_id: str
    reference_niche_state_id: str
    values: pd.Series  # indexed by HGNC approved symbol
    coverage: dict[str, int]


def comparison_vectors(signatures: pd.DataFrame, mappings: pd.DataFrame, cell_type: str) -> list[ComparisonVector]:
    """One complete signed vector per condition; Control and IPF are never merged."""
    mapped = mappings.set_index("gene_id")
    vectors = []
    for comparison_id, group in signatures[signatures["cell_type_raw"] == cell_type].groupby(
        "comparison_id", sort=True
    ):
        status = group["gene_id"].map(mapped["mapping_status"])
        finite = np.isfinite(group["effect_niche2_minus_niche1"].to_numpy())
        usable = group[status.isin(RESOLVED).to_numpy() & finite]
        symbols = usable["gene_id"].map(mapped["approved_symbol"])
        if symbols.duplicated().any():
            raise ValueError(f"{comparison_id}: resolved mappings are not one-to-one; conflicts must be rejected first")
        values = pd.Series(
            usable["effect_niche2_minus_niche1"].to_numpy(), index=symbols.to_numpy(), name=comparison_id
        )
        conditions = group["condition"].unique()
        vectors.append(
            ComparisonVector(
                comparison_id=comparison_id,
                condition=str(conditions[0]),
                case_niche_state_id=str(group["case_niche_state_id"].iloc[0]),
                reference_niche_state_id=str(group["reference_niche_state_id"].iloc[0]),
                values=values.sort_index(),
                coverage={
                    "signature_genes": len(group),
                    "resolved_finite_genes": len(usable),
                    "excluded_unresolved": int((status == "unresolved").sum()),
                    "excluded_ambiguous": int((status == "ambiguous").sum()),
                    "excluded_conflicting_duplicate_mapping": int((status == "conflict_shared_hgnc_id").sum()),
                    "excluded_nonfinite": int((~finite).sum()),
                },
            )
        )
    return vectors


def run_ulm(vector: ComparisonVector, net: pd.DataFrame, tmin: int) -> pd.Series:
    import decoupler as dc

    data = vector.values.to_frame().T
    # empty=False: decoupler otherwise drops features equal to 0, i.e. genes whose descriptive
    # effect is exactly zero. A zero difference is a supplied value and stays in the vector.
    scores, _method_pvalues = dc.mt.ulm(data=data, net=net, tmin=tmin, empty=False)
    return scores.iloc[0]


def concordance_table(
    vectors: list[ComparisonVector],
    net: pd.DataFrame,
    regulator_info: pd.DataFrame,
    tmin: int,
    policy: str,
    decoupler_version: str,
) -> pd.DataFrame:
    """Coverage for every regulator in the network; a score only where coverage meets tmin."""
    universe = net.groupby("source")["target"].nunique()
    rows = []
    for vector in vectors:
        observed = net[net["target"].isin(vector.values.index)].groupby("source")["target"].nunique()
        eligible = observed[observed >= tmin].index
        # Coverage decides eligibility first; decoupler is called only when some regulator qualifies,
        # so a comparison with none keeps its coverage rows with null scores.
        scores = run_ulm(vector, net, tmin) if len(eligible) else pd.Series(dtype=float)
        if set(scores.index) != set(eligible):
            raise RuntimeError("decoupler's tmin filtering disagrees with the recorded target coverage")
        for regulator in sorted(universe.index):
            score = float(scores[regulator]) if regulator in scores.index else None
            info = regulator_info.loc[regulator]
            rows.append(
                {
                    "comparison_id": vector.comparison_id,
                    "condition": vector.condition,
                    "case_niche_state_id": vector.case_niche_state_id,
                    "reference_niche_state_id": vector.reference_niche_state_id,
                    "comparison_view": COMPARISON_VIEW,
                    "sign_policy": policy,
                    "regulator_key": regulator,
                    "regulator_type": info["regulator_type"],
                    "regulator_hgnc_id": info["regulator_hgnc_id"],
                    "prior_universe_targets": int(universe[regulator]),
                    "observed_targets": int(observed.get(regulator, 0)),
                    "vector_genes": len(vector.values),
                    "min_targets": tmin,
                    "eligible": regulator in scores.index,
                    "ulm_score": score,
                    "concordance_direction": (
                        None if score is None else "positive" if score > 0 else "negative" if score < 0 else "zero"
                    ),
                    "method": METHOD,
                    "method_version": decoupler_version,
                }
            )
    # Explicit dtypes keep an empty table usable: an untyped empty mask would select columns, not rows.
    frame = pd.DataFrame(rows, columns=COLUMNS)
    return frame.astype(
        {
            "eligible": bool,
            "ulm_score": float,
            "prior_universe_targets": int,
            "observed_targets": int,
            "vector_genes": int,
            "min_targets": int,
        }
    )
