"""AT1 candidate TFs per comparison, their descriptive project evidence, and bounded search targets.

Two routes feed candidates: fixed manuscript seeds (included regardless of score) and the largest
absolute signed-regulon concordance scores. Seed order is not a ranking, and a concordance sign
is not a direction of TF activity.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from regkg.analysis.gene_mapping import RESOLVED
from regkg.provenance import stable_id

REASON_SEED = "manuscript_seed"
REASON_CONCORDANCE = "top_abs_signed_regulon_concordance"
SEMANTICS_UNCONFIRMED = "unconfirmed"
# CollecTRI regulators include co-regulators and general transcription factors. A candidate entry
# or a high ULM score does not establish direct DNA binding.
REGULATOR_SCOPE = "individual-gene CollecTRI regulator; DNA binding not established"
CANDIDATE_COLUMNS = [
    "candidate_id",
    "comparison_id",
    "condition",
    "case_niche_state_id",
    "reference_niche_state_id",
    "target_niche_state_id",
    "tf_hgnc_id",
    "regulator_scope",
    "reasons",
    "is_seed",
    "in_prior",
    "prior_universe_targets",
    "observed_prior_targets",
    "concordance_eligible",
    "ulm_score",
    "concordance_direction",
    "concordance_selection_rank",
    "rule_version",
]
OBSERVATION_COLUMNS = [
    "candidate_id",
    "niche_role",
    "observation_id",
    "target_gene_id",
    "context_label_raw",
    "raw_score",
    "score_semantics_status",
]
TARGET_COLUMNS = [
    "candidate_id",
    "comparison_id",
    "tf_hgnc_id",
    "target_rank",
    "target_gene_id",
    "target_hgnc_id",
    "target_symbol",
    "effect_niche2_minus_niche1",
    "source_routes",
    "prior_interaction_ids",
    "prior_signs",
    "eligible_pool_size",
    "selection_basis",
]


def resolve_seeds(seeds: list[str], mappings: pd.DataFrame) -> pd.DataFrame:
    """Seeds are exact source symbols; each must resolve to one HGNC ID."""
    frame = mappings.set_index("source_symbol").reindex(seeds)
    unresolved = frame.index[~frame["mapping_status"].isin(RESOLVED)].tolist()
    if unresolved:
        raise ValueError(f"TF seeds without a unique HGNC mapping: {unresolved}")
    return frame.reset_index()[["source_symbol", "hgnc_id", "approved_symbol", "gene_id"]]


def select_candidates(
    comparisons: pd.DataFrame,
    concordance: pd.DataFrame,
    seeds: pd.DataFrame,
    extra_per_comparison: int,
    rule_version: str,
) -> pd.DataFrame:
    """Seeds plus up to `extra_per_comparison` eligible individual-gene regulators by |score|.

    Driven by the comparison objects, so seeds are candidates even when no regulator is eligible
    or the prior network is empty. Ties on |score| are broken by HGNC ID; complexes are never
    candidates. A TF selected by both routes gets one candidate row carrying both reasons.
    """
    rows = []
    seed_ids = set(seeds["hgnc_id"])
    for comparison in comparisons.sort_values("comparison_id").itertuples(index=False):
        group = concordance[concordance["comparison_id"] == comparison.comparison_id]
        genes = group[(group["regulator_type"] == "gene") & group["regulator_hgnc_id"].notna()]
        pool = genes.loc[genes["eligible"].astype(bool).to_numpy()].assign(abs_score=lambda f: f["ulm_score"].abs())
        ranked = pool.sort_values(["abs_score", "regulator_hgnc_id"], ascending=[False, True], kind="mergesort")
        ranked = ranked.assign(concordance_selection_rank=np.arange(1, len(ranked) + 1))
        extras = ranked[~ranked["regulator_hgnc_id"].isin(seed_ids)].head(extra_per_comparison)
        # A seed that would also have qualified by score keeps both reasons.
        by_score = set(extras["regulator_hgnc_id"]) | set(ranked.head(extra_per_comparison)["regulator_hgnc_id"])
        by_hgnc = genes.set_index("regulator_hgnc_id")
        rank_of = dict(zip(ranked["regulator_hgnc_id"], ranked["concordance_selection_rank"], strict=True))
        chosen = list(seeds["hgnc_id"]) + [h for h in extras["regulator_hgnc_id"] if h not in seed_ids]
        for hgnc_id in chosen:
            reasons = [REASON_SEED] if hgnc_id in seed_ids else []
            if hgnc_id in by_score:
                reasons.append(REASON_CONCORDANCE)
            record = by_hgnc.loc[hgnc_id] if hgnc_id in by_hgnc.index else None
            rows.append(
                {
                    "candidate_id": stable_id(
                        "candidate",
                        {
                            "comparison_id": comparison.comparison_id,
                            "tf_hgnc_id": hgnc_id,
                            "rule_version": rule_version,
                        },
                    ),
                    "comparison_id": comparison.comparison_id,
                    "condition": comparison.condition,
                    "case_niche_state_id": comparison.case_niche_state_id,
                    "reference_niche_state_id": comparison.reference_niche_state_id,
                    "target_niche_state_id": comparison.case_niche_state_id,
                    "tf_hgnc_id": hgnc_id,
                    "regulator_scope": REGULATOR_SCOPE,
                    "reasons": reasons,
                    "is_seed": hgnc_id in seed_ids,
                    "in_prior": record is not None,
                    "prior_universe_targets": None if record is None else int(record["prior_universe_targets"]),
                    "observed_prior_targets": None if record is None else int(record["observed_targets"]),
                    "concordance_eligible": False if record is None else bool(record["eligible"]),
                    "ulm_score": None if record is None or not record["eligible"] else float(record["ulm_score"]),
                    "concordance_direction": None if record is None else record["concordance_direction"],
                    "concordance_selection_rank": rank_of.get(hgnc_id),
                    "rule_version": rule_version,
                }
            )
    return pd.DataFrame(rows, columns=CANDIDATE_COLUMNS)


def project_evidence(
    candidates: pd.DataFrame,
    mappings: pd.DataFrame,
    contexts: pd.DataFrame,
    chromlinker: pd.DataFrame,
    expression: pd.DataFrame,
    signatures: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Descriptive ChromLinker/expression support per candidate plus the raw ChromLinker rows used.

    ChromLinker score semantics are unconfirmed, so no connectivity rank or interpreted delta is
    computed; zeros are counted as supplied values, not as absent connections.
    """
    gene_of_hgnc = mappings[mappings["mapping_status"].isin(RESOLVED)].set_index("hgnc_id")["gene_id"]
    symbol_of_hgnc = mappings[mappings["mapping_status"].isin(RESOLVED)].set_index("hgnc_id")["approved_symbol"]
    # Whether a context exists in ChromLinker comes from the P1 context table, not from the rows
    # of the selected TFs, so a TF without connectivity is not mistaken for a missing context.
    chromlinker_labels = set(contexts.loc[contexts["in_chromlinker"], "context_label_raw"])
    label_of = contexts.dropna(subset=["niche_state_id"]).set_index(["niche_state_id", "condition_raw"])[
        "context_label_raw"
    ]
    evidence, observation_rows = [], []
    for candidate in candidates.itertuples(index=False):
        gene_id = gene_of_hgnc.get(candidate.tf_hgnc_id)
        labels = {
            "case": label_of.get((candidate.case_niche_state_id, candidate.condition)),
            "reference": label_of.get((candidate.reference_niche_state_id, candidate.condition)),
        }
        record = {
            "candidate_id": candidate.candidate_id,
            "tf_gene_id": gene_id,
            "tf_symbol": symbol_of_hgnc.get(candidate.tf_hgnc_id),
            "score_semantics_status": SEMANTICS_UNCONFIRMED,
            "connectivity_rank": None,
            "interpreted_connectivity_delta": None,
        }
        tf_rows = chromlinker[chromlinker["tf_gene_id"] == gene_id] if gene_id is not None else chromlinker.iloc[:0]
        record["tf_in_chromlinker"] = len(tf_rows) > 0
        record["chromlinker_target_count"] = int(tf_rows["target_gene_id"].nunique())
        missing = [] if record["tf_in_chromlinker"] else ["tf_absent_from_chromlinker"]
        for role, label in labels.items():
            rows = tf_rows[tf_rows["context_label_raw"] == label] if label else tf_rows.iloc[:0]
            scores = rows["raw_score"].to_numpy()
            record[f"chromlinker_{role}_context_label"] = label if label and label in chromlinker_labels else None
            record[f"chromlinker_{role}_observations"] = len(rows)
            record[f"chromlinker_{role}_nonzero"] = int((scores != 0).sum())
            record[f"chromlinker_{role}_min"] = float(scores.min()) if len(scores) else None
            record[f"chromlinker_{role}_median"] = float(np.median(scores)) if len(scores) else None
            record[f"chromlinker_{role}_max"] = float(scores.max()) if len(scores) else None
            if record[f"chromlinker_{role}_context_label"] is None:
                missing.append(f"chromlinker_{role}_context_not_supplied")
            for row in rows.itertuples(index=False):
                observation_rows.append(
                    {
                        "candidate_id": candidate.candidate_id,
                        "niche_role": role,
                        "observation_id": row.observation_id,
                        "target_gene_id": row.target_gene_id,
                        "context_label_raw": row.context_label_raw,
                        "raw_score": row.raw_score,
                        "score_semantics_status": row.score_semantics_status,
                    }
                )
            expr = (
                expression[(expression["gene_id"] == gene_id) & (expression["context_label_raw"] == label)]
                if (gene_id is not None and label)
                else expression.iloc[:0]
            )
            record[f"tf_cptt_{role}"] = float(expr["value"].iloc[0]) if len(expr) else None
            if not len(expr):
                missing.append(f"tf_expression_{role}_not_supplied")
        sig = signatures[(signatures["comparison_id"] == candidate.comparison_id) & (signatures["gene_id"] == gene_id)]
        for column in [
            "mean_expr_niche1",
            "mean_expr_niche2",
            "effect_niche2_minus_niche1",
            "pct_expr_niche1",
            "pct_expr_niche2",
        ]:
            record[f"tf_signature_{column}"] = float(sig[column].iloc[0]) if len(sig) else None
        if not len(sig):
            missing.append("tf_signature_not_supplied")
        missing.append("connectivity_rank_unavailable_unconfirmed_semantics")
        if not candidate.in_prior:
            missing.append("tf_absent_from_prior")
        elif not candidate.concordance_eligible:
            missing.append("prior_target_coverage_below_minimum")
        record["missing_component_reasons"] = missing
        evidence.append(record)
    return pd.DataFrame(evidence), pd.DataFrame(observation_rows, columns=OBSERVATION_COLUMNS)


def select_targets(
    candidates: pd.DataFrame,
    evidence: pd.DataFrame,
    priors: pd.DataFrame,
    mappings: pd.DataFrame,
    chromlinker: pd.DataFrame,
    signatures: pd.DataFrame,
    per_candidate: int,
) -> pd.DataFrame:
    """Up to `per_candidate` resolved targets per candidate for literature retrieval coverage only.

    Eligible targets appear in the TF's CollecTRI records or its supplied ChromLinker rows and in
    the comparison's signature. They are ordered by |descriptive effect|, then gene ID. This is a
    retrieval choice, not a biological ranking.
    """
    resolved = mappings[mappings["mapping_status"].isin(RESOLVED)]
    gene_of_symbol = resolved.set_index("approved_symbol")["gene_id"]
    tf_gene = evidence.set_index("candidate_id")["tf_gene_id"]
    rows = []
    for candidate in candidates.itertuples(index=False):
        tf_priors = priors[(priors["regulator_hgnc_id"] == candidate.tf_hgnc_id) & priors["target_hgnc_id"].notna()]
        prior_genes = set(tf_priors["target_approved_symbol"].map(gene_of_symbol).dropna())
        gene_id = tf_gene.get(candidate.candidate_id)
        chromlinker_genes = (
            set(chromlinker.loc[chromlinker["tf_gene_id"] == gene_id, "target_gene_id"]) if gene_id else set()
        )
        chromlinker_genes &= set(resolved["gene_id"])
        sig = signatures[signatures["comparison_id"] == candidate.comparison_id].set_index("gene_id")
        pool = sorted((prior_genes | chromlinker_genes) & set(sig.index))
        if not pool:
            continue
        table = pd.DataFrame({"target_gene_id": pool})
        table["effect"] = sig.loc[pool, "effect_niche2_minus_niche1"].to_numpy()
        table["abs_effect"] = table["effect"].abs()
        table = table.sort_values(["abs_effect", "target_gene_id"], ascending=[False, True], kind="mergesort")
        for rank, target in enumerate(table.head(per_candidate).itertuples(index=False), start=1):
            routes = [
                r
                for r, genes in (("collectri_prior", prior_genes), ("chromlinker", chromlinker_genes))
                if target.target_gene_id in genes
            ]
            target_symbol = resolved.set_index("gene_id").loc[target.target_gene_id, "approved_symbol"]
            prior_rows = tf_priors[tf_priors["target_approved_symbol"] == target_symbol]
            rows.append(
                {
                    "candidate_id": candidate.candidate_id,
                    "comparison_id": candidate.comparison_id,
                    "tf_hgnc_id": candidate.tf_hgnc_id,
                    "target_rank": rank,
                    "target_gene_id": target.target_gene_id,
                    "target_hgnc_id": resolved.set_index("gene_id").loc[target.target_gene_id, "hgnc_id"],
                    "target_symbol": target_symbol,
                    "effect_niche2_minus_niche1": float(target.effect),
                    "source_routes": routes,
                    "prior_interaction_ids": sorted(prior_rows["prior_interaction_id"]),
                    "prior_signs": sorted(set(prior_rows["sign"])),
                    "eligible_pool_size": len(pool),
                    "selection_basis": "abs_descriptive_effect_then_gene_id; retrieval coverage only",
                }
            )
    return pd.DataFrame(rows, columns=TARGET_COLUMNS)
