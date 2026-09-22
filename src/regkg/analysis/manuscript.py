"""Manuscript-scope candidates (P2.11-P2.13): every regulatory case through the same P2 pipeline.

Each lineage uses the shared resolver, CollecTRI prior, signed concordance, candidate union,
target selection, and queue code with its own seeds, signatures, and project contexts. A TF named
in several lineages keeps one gene identity but gets a separate candidate per comparison and
separate queries per lineage, so no lineage's seeds or evidence reach another.

Only the manuscript's primary comparisons generate candidates. Other supplied signature
comparisons of the same lineages (Control for KRT5-/KRT17+ cells and activated fibrotic
fibroblasts, whose Control niche ChromLinker contexts are not supplied) are listed as
observation-only; they are neither dropped nor given invented regulatory contexts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import pyarrow.parquet as pq

import regkg
from regkg.analysis import schemas
from regkg.analysis.candidates import REASON_SEED, project_evidence, resolve_seeds, select_candidates, select_targets
from regkg.analysis.concordance import COMPARISON_VIEW, PRIMARY_POLICY, ComparisonVector, comparison_vectors
from regkg.analysis.gene_mapping import RESOLVED, read_hgnc
from regkg.analysis.queue import STATUS_NOT_SEARCHED, build_queue, query_names, schedule_queries
from regkg.analysis.stage import (
    CODE_PATHS,
    SOFTWARE,
    CandidateOutcome,
    CandidateStageError,
    SharedResources,
    both_policies,
    coverage_report,
    execute_stage,
    resource_record,
    shared_resources,
    shared_tables,
)
from regkg.analysis.verify import (
    _detail,
    _read,
    _same_rows,
    artifact_integrity,
    connectivity_semantics,
    schema_checks,
    shared_checks,
    target_selection,
)
from regkg.config import (
    CandidateGenerationConfig,
    LoadedProjectConfig,
    ManuscriptScopeConfig,
    RetrievalQueueConfig,
    load_candidate_config,
    load_manuscript_scope,
    load_queue_config,
)
from regkg.models import CheckResult, StageStatus
from regkg.project_data.io import write_parquet
from regkg.project_data.verify import Checks, published_integrity
from regkg.provenance import (
    canonical_json,
    code_fingerprint,
    describe_outputs,
    git_revision,
    read_json,
    sha256_file,
    sha256_text,
    software_versions,
    stable_id,
    utc_now,
    write_json,
)

STAGE = "manuscript-candidates"
KEY_PREFIX = "mcandidates"
ROLE_PRIMARY = "primary_regulatory"
ROLE_SIGNATURE_ONLY = "signature_only_not_primary"


@dataclass(frozen=True)
class ManuscriptInputs:
    loaded: LoadedProjectConfig
    scope: ManuscriptScopeConfig
    scope_path: Path
    candidate_config: CandidateGenerationConfig
    queue_config: RetrievalQueueConfig
    resources: SharedResources


def lineage_comparisons(
    signatures: pd.DataFrame, contexts: pd.DataFrame, mappings: pd.DataFrame, scope: ManuscriptScopeConfig
) -> tuple[list[tuple[str, ComparisonVector]], pd.DataFrame]:
    """Primary vectors per lineage, and every supplied signature comparison of the scoped lineages."""
    chromlinker = contexts[contexts["in_chromlinker"] & contexts["niche_state_id"].notna()]
    label_of = chromlinker.set_index(["niche_state_id", "condition_raw"])["context_label_raw"]
    primary, rows = [], []
    for lineage in scope.lineages:
        vectors = comparison_vectors(signatures, mappings, lineage.cell_type)
        missing = set(lineage.primary_conditions) - {v.condition for v in vectors}
        if missing:
            # A primary comparison without supplied signatures cannot be constructed; never invent one.
            raise CandidateStageError(f"{lineage.cell_type}: no signature comparison for {sorted(missing)}")
        for vector in vectors:
            case = label_of.get((vector.case_niche_state_id, vector.condition))
            reference = label_of.get((vector.reference_niche_state_id, vector.condition))
            status = (
                "both_supplied"
                if case and reference
                else "case_missing"
                if reference
                else "reference_missing"
                if case
                else "none_supplied"
            )
            is_primary = vector.condition in lineage.primary_conditions
            if is_primary:
                primary.append((lineage.cell_type, vector))
            group = signatures[signatures["comparison_id"] == vector.comparison_id]
            rows.append(
                {
                    "comparison_id": vector.comparison_id,
                    "cell_type": lineage.cell_type,
                    "condition": vector.condition,
                    "case_niche_state_id": vector.case_niche_state_id,
                    "reference_niche_state_id": vector.reference_niche_state_id,
                    "comparison_view": COMPARISON_VIEW,
                    "effect_definition": group["effect_definition"].iloc[0],
                    **vector.coverage,
                    "comparison_role": ROLE_PRIMARY if is_primary else ROLE_SIGNATURE_ONLY,
                    "chromlinker_case_context_label": case,
                    "chromlinker_reference_context_label": reference,
                    "regulatory_context_status": status,
                }
            )
    return primary, pd.DataFrame(rows, columns=schemas.M_COMPARISONS.names)


def lineage_candidates(
    comparisons: pd.DataFrame,
    primary_concordance: pd.DataFrame,
    mappings: pd.DataFrame,
    scope: ManuscriptScopeConfig,
    config: CandidateGenerationConfig,
) -> pd.DataFrame:
    """The P2 candidate union run once per lineage, over its primary comparisons and its own seeds."""
    frames = []
    for lineage in scope.lineages:
        own = comparisons[
            (comparisons["cell_type"] == lineage.cell_type) & (comparisons["comparison_role"] == ROLE_PRIMARY)
        ]
        concordance = primary_concordance[primary_concordance["comparison_id"].isin(own["comparison_id"])]
        seeds = resolve_seeds(lineage.tf_seeds, mappings)
        selected = select_candidates(own, concordance, seeds, config.extra_tfs_per_comparison, config.rule_version)
        frames.append(selected.assign(cell_type=lineage.cell_type, scope_version=scope.scope_version))
    return pd.concat(frames, ignore_index=True)


def lineage_queues(
    candidates: pd.DataFrame,
    targets: pd.DataFrame,
    names: dict[str, list[str]],
    queue_config: RetrievalQueueConfig,
    scope: ManuscriptScopeConfig,
) -> pd.DataFrame:
    """Per-lineage queues with lineage context terms, merged by the fair cross-lineage schedule."""
    queues = {}
    for lineage in scope.lineages:
        own = candidates[candidates["cell_type"] == lineage.cell_type]
        own_targets = targets[targets["candidate_id"].isin(own["candidate_id"])]
        config = queue_config.model_copy(update={"context_terms": lineage.context_terms})
        identity = {"cell_type": lineage.cell_type, "scope_version": scope.scope_version}
        queue = build_queue(own, own_targets, names, config, scope=identity)
        queues[lineage.cell_type] = queue.assign(
            cell_type=lineage.cell_type, scope_version=scope.scope_version, lineage_priority=queue["priority"]
        )
    schedule = schedule_queries(queues, scope.schedule.batch_size)
    frame = pd.concat(queues.values(), ignore_index=True).merge(
        schedule, on=["cell_type", "query_id"], how="inner", validate="one_to_one"
    )
    frame["priority"] = frame["schedule_position"]
    # The first fair batch replaces the per-lineage baseline slice.
    frame["in_initial_live_slice"] = frame["batch_index"] == 1
    return frame.sort_values("priority").reset_index(drop=True)[schemas.M_QUEUE.names]


def lineage_memberships(
    candidates: pd.DataFrame,
    targets: pd.DataFrame,
    queue: pd.DataFrame,
    mappings: pd.DataFrame,
    scope: ManuscriptScopeConfig,
) -> pd.DataFrame:
    """One row per named lineage-TF membership: the manuscript's reconciliation unit."""
    rows = []
    for lineage in scope.lineages:
        seeds = resolve_seeds(lineage.tf_seeds, mappings)
        for seed in seeds.itertuples(index=False):
            own = candidates[
                (candidates["cell_type"] == lineage.cell_type)
                & (candidates["tf_hgnc_id"] == seed.hgnc_id)
                & candidates["reasons"].map(lambda r: REASON_SEED in r)
            ].sort_values("comparison_id")
            lineage_queries = queue[(queue["cell_type"] == lineage.cell_type) & (queue["tf_hgnc_id"] == seed.hgnc_id)]
            rows.append(
                {
                    "membership_id": stable_id(
                        "membership",
                        {"cell_type": lineage.cell_type, "tf_hgnc_id": seed.hgnc_id, "scope": scope.scope_version},
                    ),
                    "cell_type": lineage.cell_type,
                    "tf_symbol_raw": seed.source_symbol,
                    "tf_hgnc_id": seed.hgnc_id,
                    "tf_approved_symbol": seed.approved_symbol,
                    "tf_gene_id": seed.gene_id,
                    "primary_comparison_ids": list(own["comparison_id"]),
                    "conditions": list(own["condition"]),
                    "candidate_ids": list(own["candidate_id"]),
                    "in_prior": bool(own["in_prior"].any()),
                    "concordance_eligible_comparisons": list(own.loc[own["concordance_eligible"], "comparison_id"]),
                    "tf_in_chromlinker": bool(own["tf_in_chromlinker"].any()),
                    "target_count": int(targets["candidate_id"].isin(own["candidate_id"]).sum()),
                    "query_count": len(lineage_queries),
                    "missing_component_reasons": sorted(
                        {reason for reasons in own["missing_component_reasons"] for reason in reasons}
                    ),
                    "scope_version": scope.scope_version,
                }
            )
    return pd.DataFrame(rows, columns=schemas.LINEAGE_TF_MEMBERSHIPS.names)


# ---------------------------------------------------------------------------
# Stage


def prepare_manuscript_inputs(
    loaded: LoadedProjectConfig, ingest_key: str, scope_path: Path, ranking: Path, literature: Path, fetcher
) -> ManuscriptInputs:
    scope = load_manuscript_scope(scope_path, loaded.config)
    candidate_config, queue_config = load_candidate_config(ranking), load_queue_config(literature)
    resources = shared_resources(loaded, ingest_key, candidate_config, fetcher)
    return ManuscriptInputs(loaded, scope, scope_path, candidate_config, queue_config, resources)


def manuscript_key(inputs: ManuscriptInputs, code_hash: str, decoupler_version: str | None) -> str:
    identity = {
        "stage": STAGE,
        "schema_version": schemas.MANUSCRIPT_SCHEMA_VERSION,
        "ingest_key": inputs.resources.ingest_dir.name,
        "scope": inputs.scope.model_dump(mode="json"),
        "hgnc_sha256": inputs.resources.hgnc.provenance["sha256"],
        "collectri_sha256": inputs.resources.collectri.provenance["sha256"],
        "seed_lists": inputs.resources.seed_hashes,
        "candidate_config": inputs.candidate_config.model_dump(mode="json"),
        "queue_config": inputs.queue_config.model_dump(mode="json"),
        "code": code_hash,
        "decoupler": decoupler_version,
    }
    return f"{KEY_PREFIX}-{sha256_text(canonical_json(identity))[:16]}"


def run_manuscript_candidates(
    loaded: LoadedProjectConfig, ingest_key: str, scope_path: Path, ranking: Path, literature: Path
) -> CandidateOutcome:
    def plan(fetcher, execution_id: str, started: str):
        inputs = prepare_manuscript_inputs(loaded, ingest_key, scope_path, ranking, literature, fetcher)
        versions = software_versions(SOFTWARE)
        code_hash = code_fingerprint(Path(regkg.__file__).parent, CODE_PATHS)
        key = manuscript_key(inputs, code_hash, versions["decoupler"])

        def build(staging: Path) -> dict[str, int]:
            return build_manuscript(inputs, key, code_hash, versions, staging, execution_id, started, fetcher)

        return key, build

    context = {"ingest_key": ingest_key, "scope": str(scope_path)}
    return execute_stage(loaded, STAGE, context, plan, schemas.MANUSCRIPT_SCHEMA_VERSION)


def build_manuscript(
    inputs: ManuscriptInputs,
    key: str,
    code_hash: str,
    versions: dict[str, str | None],
    out: Path,
    execution_id: str,
    started: str,
    fetcher,
) -> dict[str, int]:
    scope, config, queue_config = inputs.scope, inputs.candidate_config, inputs.queue_config
    ingest = inputs.resources.ingest_dir
    shared = shared_tables(inputs.resources, config)
    mappings = shared.mappings
    signatures = pd.read_parquet(ingest / "niche_expression_signatures.parquet")
    contexts = pd.read_parquet(ingest / "contexts.parquet")

    primary_vectors, comparisons = lineage_comparisons(signatures, contexts, mappings, scope)
    vectors = [vector for _, vector in primary_vectors]
    lineage_of = dict(zip(comparisons["comparison_id"], comparisons["cell_type"], strict=True))
    gene_of_symbol = mappings[mappings["mapping_status"].isin(RESOLVED)].set_index("approved_symbol")["gene_id"]
    vector_rows = pd.concat(
        [
            pd.DataFrame(
                {
                    "comparison_id": v.comparison_id,
                    "approved_symbol": v.values.index,
                    "gene_id": v.values.index.map(gene_of_symbol),
                    "effect_niche2_minus_niche1": v.values.to_numpy(),
                }
            )
            for v in vectors
        ],
        ignore_index=True,
    )
    concordance = both_policies(vectors, shared, config, versions["decoupler"])
    concordance["cell_type"] = concordance["comparison_id"].map(lineage_of)
    primary = concordance[concordance["sign_policy"] == PRIMARY_POLICY]

    selected = lineage_candidates(comparisons, primary, mappings, scope, config)
    resolved = mappings[mappings["mapping_status"].isin(RESOLVED)]
    tf_genes = sorted(resolved.loc[resolved["hgnc_id"].isin(selected["tf_hgnc_id"]), "gene_id"])
    chromlinker = pq.read_table(
        ingest / "chromlinker_observations.parquet", filters=[("tf_gene_id", "in", tf_genes)]
    ).to_pandas()
    expression = pq.read_table(
        ingest / "expression_observations.parquet", filters=[("gene_id", "in", tf_genes)]
    ).to_pandas()
    evidence, candidate_observations = project_evidence(
        selected, mappings, contexts, chromlinker, expression, signatures
    )
    candidates = selected.merge(evidence, on="candidate_id", how="left", validate="one_to_one")
    targets = select_targets(
        selected, evidence, shared.priors, mappings, chromlinker, signatures, config.targets_per_candidate
    )
    targets["cell_type"] = targets["comparison_id"].map(lineage_of)

    names = query_names(
        set(selected["tf_hgnc_id"]) | set(targets["target_hgnc_id"]), shared.hgnc, queue_config.max_aliases_per_gene
    )
    queue = lineage_queues(selected, targets, names, queue_config, scope)
    memberships = lineage_memberships(candidates, targets, queue, mappings, scope)

    rows = {}
    for name, frame in (
        ("gene_mappings.parquet", mappings),
        ("seed_publications.parquet", shared.publications),
        ("prior_interactions.parquet", shared.priors),
        ("comparisons.parquet", comparisons),
        ("comparison_vectors.parquet", vector_rows),
        ("concordance.parquet", concordance),
        ("candidates.parquet", candidates),
        ("candidate_chromlinker_observations.parquet", candidate_observations),
        ("candidate_targets.parquet", targets),
        ("retrieval_queue.parquet", queue),
        ("lineage_tf_memberships.parquet", memberships),
    ):
        schema = schemas.MANUSCRIPT_TABLE_SCHEMAS[name]
        rows[name] = write_parquet(frame[schema.names], schema, out / name)

    resources = resource_record(inputs.resources, inputs.loaded, fetcher)
    write_json(out / "resources.json", resources)
    primary_rows = comparisons[comparisons["comparison_role"] == ROLE_PRIMARY]
    write_json(
        out / "coverage_report.json",
        coverage_report(
            mappings,
            shared.genes,
            shared.parsed,
            shared.priors,
            shared.sensitivity,
            primary_rows,
            concordance,
            candidates,
            targets,
            queue,
            shared.publications,
            shared.publication_conflicts,
            queue_config,
        ),
    )
    write_json(
        out / "manuscript_manifest.json",
        manuscript_manifest(scope, comparisons, candidates, targets, queue, memberships, concordance),
    )

    checks = manuscript_checks(
        out, ingest, inputs.loaded.repo_root, scope, config, queue_config, inputs.resources.hgnc.path
    )
    failed = [c for c in checks if not c.passed]
    if failed:
        raise CandidateStageError(
            "pre-publication checks failed: " + "; ".join(f"{c.name}: {c.detail}" for c in failed)
        )
    manifest = {
        "stage": STAGE,
        "schema_version": schemas.MANUSCRIPT_SCHEMA_VERSION,
        "candidate_key": key,
        "status": StageStatus.SUCCEEDED.value,
        "execution_id": execution_id,
        "started_at": started,
        "ended_at": utc_now(),
        "input_mode": inputs.loaded.config.input_mode.value,
        "inputs": {
            "ingest_key": ingest.name,
            "scope_path": inputs.scope_path.resolve().relative_to(inputs.loaded.repo_root).as_posix()
            if inputs.scope_path.resolve().is_relative_to(inputs.loaded.repo_root)
            else inputs.scope_path.as_posix(),
            "scope_sha256": sha256_file(inputs.scope_path),
            "resources": resources,
        },
        "config": {
            "scope": scope.model_dump(mode="json"),
            "candidate_generation": config.model_dump(mode="json"),
            "retrieval_queue": queue_config.model_dump(mode="json"),
        },
        "code": {"fingerprint": code_hash, "paths": CODE_PATHS, "git": git_revision(inputs.loaded.repo_root)},
        "software": versions,
        "checks": [c.model_dump() for c in checks],
        "outputs": describe_outputs(out, rows),
        "error": None,
    }
    write_json(out / "manifest.json", manifest)
    return rows


def _label(value) -> str | None:
    return None if pd.isna(value) else str(value)


def manuscript_manifest(
    scope: ManuscriptScopeConfig,
    comparisons: pd.DataFrame,
    candidates: pd.DataFrame,
    targets: pd.DataFrame,
    queue: pd.DataFrame,
    memberships: pd.DataFrame,
    concordance: pd.DataFrame,
) -> dict[str, Any]:
    """Reconciled manuscript candidate/coverage manifest (JSON view of the tables)."""
    primary_eligible = concordance[concordance["sign_policy"] == PRIMARY_POLICY]
    lineages = []
    for lineage in scope.lineages:
        own = comparisons[comparisons["cell_type"] == lineage.cell_type]
        entries = []
        for comparison in own.itertuples(index=False):
            rows = candidates[candidates["comparison_id"] == comparison.comparison_id]
            entry = {
                "comparison_id": comparison.comparison_id,
                "condition": comparison.condition,
                "comparison_role": comparison.comparison_role,
                "regulatory_context_status": comparison.regulatory_context_status,
                # A context that is not supplied is null, never NaN or an empty label.
                "chromlinker_case_context_label": _label(comparison.chromlinker_case_context_label),
                "chromlinker_reference_context_label": _label(comparison.chromlinker_reference_context_label),
                "signature_genes": int(comparison.signature_genes),
            }
            if comparison.comparison_role == ROLE_PRIMARY:
                entry.update(
                    candidates=len(rows),
                    seed_candidates=int(rows["is_seed"].sum()),
                    concordance_extras=int((~rows["is_seed"]).sum()),
                    eligible_regulators_primary_policy=int(
                        primary_eligible.loc[
                            primary_eligible["comparison_id"] == comparison.comparison_id, "eligible"
                        ].sum()
                    ),
                    candidates_with_targets=int(
                        targets.loc[targets["comparison_id"] == comparison.comparison_id, "candidate_id"].nunique()
                    ),
                )
            else:
                entry["status"] = (
                    "observation_only: supplied signature preserved in the ingest artifact; no candidates, "
                    "no regulatory comparison, no disease-interaction claim"
                )
            entries.append(entry)
        own_queue = queue[queue["cell_type"] == lineage.cell_type]
        lineages.append(
            {
                "cell_type": lineage.cell_type,
                "tf_seeds": lineage.tf_seeds,
                "primary_conditions": lineage.primary_conditions,
                "draft_interpretation_to_assess": lineage.draft_interpretation,
                "comparisons": entries,
                "candidate_tfs": int(
                    candidates.loc[candidates["cell_type"] == lineage.cell_type, "tf_hgnc_id"].nunique()
                ),
                "queries": len(own_queue),
                "queries_in_first_batch": int((own_queue["batch_index"] == 1).sum()),
            }
        )
    shared = memberships.groupby("tf_hgnc_id").agg(
        symbol=("tf_approved_symbol", "first"), lineages=("cell_type", lambda s: sorted(s))
    )
    batches = queue.groupby("batch_index")
    primary = comparisons[comparisons["comparison_role"] == ROLE_PRIMARY]
    return {
        "scope_version": scope.scope_version,
        "source": scope.source,
        "status": "pending_lead_review",
        "expected": scope.expected.model_dump(),
        "observed": {
            "primary_comparisons": len(primary),
            "lineage_tf_memberships": len(memberships),
            "unique_named_tfs": int(memberships["tf_hgnc_id"].nunique()),
            "candidates": len(candidates),
            "unique_candidate_tfs": int(candidates["tf_hgnc_id"].nunique()),
            "targets": len(targets),
            "queries": len(queue),
        },
        "lineages": lineages,
        "named_tfs_in_several_lineages": {
            h: {"symbol": r.symbol, "lineages": r.lineages} for h, r in shared.iterrows() if len(r.lineages) > 1
        },
        "schedule": {
            "rule_version": scope.schedule.rule_version,
            "batch_size": scope.schedule.batch_size,
            "batches": [
                {
                    "batch_index": int(b),
                    "queries": len(g),
                    "by_lineage": g["cell_type"].value_counts().sort_index().to_dict(),
                }
                for b, g in batches
            ],
            "search_status": queue["search_status"].value_counts().to_dict(),
        },
        "notes": [
            "Draft interpretations are claims to assess later; they do not enter scores, filters, or directions.",
            "Signature effects are descriptive Niche2-minus-Niche1 pooled mean-log-expression differences, "
            "not log2FC or sample-aware DE.",
            "ChromLinker score semantics are unconfirmed: no connectivity rank or interpreted delta is computed.",
            "AT1 and alveolar macrophage Control and IPF contrasts are separate within-condition comparisons; "
            "comparing them is not a disease-by-niche interaction test.",
            "Control signatures of KRT5neg_KRT17pos and Activated_Fibrotic_FBs are observation-only: no Control "
            "niche ChromLinker contexts are supplied, and none are invented.",
            "Queries shared in text across lineages remain separate lineage-scoped rows; identical requests reuse "
            "the source cache when executed.",
        ],
    }


# ---------------------------------------------------------------------------
# Verification


def manuscript_checks(
    artifact_dir: Path,
    ingest_dir: Path,
    repo_root: Path,
    scope: ManuscriptScopeConfig,
    config: CandidateGenerationConfig,
    queue_config: RetrievalQueueConfig,
    hgnc_path: Path,
) -> list[CheckResult]:
    checks = Checks()
    schema_checks(checks, artifact_dir, schemas.MANUSCRIPT_TABLE_SCHEMAS)
    shared_checks(checks, artifact_dir, ingest_dir, repo_root, config, hgnc_path)
    mappings = _read(artifact_dir, "gene_mappings.parquet")
    comparisons = _read(artifact_dir, "comparisons.parquet")
    concordance = _read(artifact_dir, "concordance.parquet")
    candidates = _read(artifact_dir, "candidates.parquet")
    targets = _read(artifact_dir, "candidate_targets.parquet")
    queue = _read(artifact_dir, "retrieval_queue.parquet")
    memberships = _read(artifact_dir, "lineage_tf_memberships.parquet")
    signatures = _read(ingest_dir, "niche_expression_signatures.parquet")
    contexts = _read(ingest_dir, "contexts.parquet")
    primary_ids = set(comparisons.loc[comparisons["comparison_role"] == ROLE_PRIMARY, "comparison_id"])

    def scope_comparisons() -> tuple[bool, str]:
        _, expected = lineage_comparisons(signatures, contexts, mappings, scope)
        same = _same_rows(expected, comparisons, schemas.M_COMPARISONS)
        primary = comparisons[comparisons["comparison_role"] == ROLE_PRIMARY]
        pairs = set(zip(primary["cell_type"], primary["condition"], strict=True))
        wanted = {(lineage.cell_type, c) for lineage in scope.lineages for c in lineage.primary_conditions}
        count_ok = len(primary) == scope.expected.primary_comparisons and pairs == wanted
        others = comparisons[comparisons["comparison_role"] != ROLE_PRIMARY]
        missing = [
            f"{r.cell_type}/{r.condition}:{r.regulatory_context_status}"
            for r in comparisons.itertuples(index=False)
            if r.regulatory_context_status != "both_supplied"
        ]
        return same and count_ok, _detail(
            f"{len(primary)} primary comparisons (expected {scope.expected.primary_comparisons}) exactly "
            f"{sorted(pairs)}; {len(others)} observation-only signature comparisons; contexts not both "
            f"supplied: {missing}",
            {"recomputed_from_ingest": same, "primary_pairs_and_count": count_ok},
        )

    checks.run("scope:primary_comparisons_and_missing_contexts", scope_comparisons)

    def scope_memberships() -> tuple[bool, str]:
        expected = lineage_memberships(candidates, targets, queue, mappings, scope)
        same = _same_rows(expected, memberships, schemas.LINEAGE_TF_MEMBERSHIPS)
        counts_ok = (
            len(memberships) == scope.expected.lineage_tf_memberships
            and memberships["tf_hgnc_id"].nunique() == scope.expected.unique_named_tfs
            and memberships["membership_id"].is_unique
        )
        per_lineage = {lineage.cell_type: set(lineage.primary_conditions) for lineage in scope.lineages}
        covered = all(set(r.conditions) == per_lineage[r.cell_type] for r in memberships.itertuples(index=False))
        # One gene identity per named TF, whichever lineages name it.
        identity_ok = (memberships.groupby("tf_symbol_raw")["tf_hgnc_id"].nunique() == 1).all() and (
            memberships.groupby("tf_symbol_raw")["tf_gene_id"].nunique() == 1
        ).all()
        several = memberships.groupby("tf_approved_symbol")["cell_type"].agg(sorted)
        several = {s: c for s, c in several.items() if len(c) > 1}
        return same and counts_ok and covered and bool(identity_ok), _detail(
            f"{len(memberships)} lineage-TF memberships (expected {scope.expected.lineage_tf_memberships}), "
            f"{memberships['tf_hgnc_id'].nunique()} unique TFs (expected {scope.expected.unique_named_tfs}); each "
            f"a seed candidate in every primary comparison of its lineage; shared identities {several}",
            {
                "recomputed": same,
                "counts": counts_ok,
                "every_primary_comparison": covered,
                "one_identity": bool(identity_ok),
            },
        )

    checks.run("scope:lineage_tf_memberships", scope_memberships)

    def isolation_and_selection() -> tuple[bool, str]:
        primary = concordance[concordance["sign_policy"] == PRIMARY_POLICY]
        expected = lineage_candidates(comparisons, primary, mappings, scope, config)
        same = _same_rows(expected, candidates, schemas.M_CANDIDATES)
        seed_ids = {
            lineage.cell_type: set(resolve_seeds(lineage.tf_seeds, mappings)["hgnc_id"]) for lineage in scope.lineages
        }
        lineage_of = dict(zip(comparisons["comparison_id"], comparisons["cell_type"], strict=True))
        leaked = [
            r.candidate_id
            for r in candidates.itertuples(index=False)
            if (REASON_SEED in r.reasons) != (r.tf_hgnc_id in seed_ids[r.cell_type])
            or lineage_of.get(r.comparison_id) != r.cell_type
            or r.comparison_id not in primary_ids
        ]
        extras_ok = (
            candidates.groupby("comparison_id")["is_seed"]
            .apply(lambda s: (~s).sum())
            .le(config.extra_tfs_per_comparison)
            .all()
        )
        concordance_ok = (concordance["comparison_id"].map(lineage_of) == concordance["cell_type"]).all() and set(
            concordance["comparison_id"]
        ) == primary_ids
        return same and not leaked and bool(extras_ok) and bool(concordance_ok), _detail(
            f"{len(candidates)} candidates in {candidates['comparison_id'].nunique()} primary comparisons; seed "
            f"reasons only for the lineage's own seeds; <= {config.extra_tfs_per_comparison} concordance extras "
            "per comparison; recomputed per lineage identical",
            {
                "recomputed": same,
                f"leaked_or_misplaced:{leaked[:3]}": not leaked,
                "extras_bounded": bool(extras_ok),
                "concordance_primary_only": bool(concordance_ok),
            },
        )

    checks.run("candidates:lineage_isolation_and_selection", isolation_and_selection)
    checks.run("candidates:no_connectivity_rank", lambda: connectivity_semantics(candidates))

    def targets_check() -> tuple[bool, str]:
        ok, detail = target_selection(targets, mappings, _read(artifact_dir, "comparison_vectors.parquet"), config)
        owner = candidates.set_index("candidate_id")
        consistent = targets.empty or (
            (targets["candidate_id"].map(owner["cell_type"]) == targets["cell_type"]).all()
            and (targets["candidate_id"].map(owner["comparison_id"]) == targets["comparison_id"]).all()
        )
        return ok and bool(consistent), _detail(
            detail + "; each target in its candidate's lineage and comparison", {"lineage_consistent": consistent}
        )

    checks.run("targets:bounded_selection", targets_check)

    def queue_reproducible() -> tuple[bool, str]:
        names = query_names(
            set(candidates["tf_hgnc_id"]) | set(targets["target_hgnc_id"]),
            read_hgnc(hgnc_path),
            queue_config.max_aliases_per_gene,
        )
        same = _same_rows(lineage_queues(candidates, targets, names, queue_config, scope), queue, schemas.M_QUEUE)
        lineage_of = dict(zip(candidates["candidate_id"], candidates["cell_type"], strict=True))
        mixed = [
            r.query_id
            for r in queue.itertuples(index=False)
            if {lineage_of[c] for c in r.candidate_ids} != {r.cell_type}
        ]
        queued = set(zip(queue["cell_type"], queue["tf_hgnc_id"], strict=True))
        unqueued = sorted(set(zip(candidates["cell_type"], candidates["tf_hgnc_id"], strict=True)) - queued)
        status_ok = set(queue["search_status"]) == {STATUS_NOT_SEARCHED} and queue["date_restriction"].isna().all()
        return same and not mixed and not unqueued and bool(status_ok), _detail(
            f"{len(queue)} lineage-scoped queries, all NOT_SEARCHED; every query's candidates from its own "
            "lineage; every lineage-TF candidate queued; rebuild identical",
            {
                "rebuild_identical": same,
                f"mixed_lineages:{mixed[:3]}": not mixed,
                f"unqueued:{unqueued[:3]}": not unqueued,
                "status": bool(status_ok),
            },
        )

    checks.run("queue:lineage_queues_reproducible", queue_reproducible)

    def fair_schedule() -> tuple[bool, str]:
        size = scope.schedule.batch_size
        positions_ok = (
            queue["priority"].tolist() == list(range(1, len(queue) + 1))
            and (queue["priority"] == queue["schedule_position"]).all()
        )
        batch_ok = (queue["batch_index"] == (queue["schedule_position"] - 1) // size + 1).all()
        order_ok = all(
            g.sort_values("schedule_position")["lineage_priority"].is_monotonic_increasing
            for _, g in queue.groupby("cell_type")
        )
        # No starvation: any lineage with queries at or after a batch has a query in that batch
        # (whenever the batch has room for every lineage).
        starved = []
        for batch, group in queue.groupby("batch_index"):
            start = group["schedule_position"].min()
            waiting = set(queue.loc[queue["schedule_position"] >= start, "cell_type"])
            if size >= len(waiting) and not waiting <= set(group["cell_type"]):
                starved.append(int(batch))
        first = queue[queue["batch_index"] == 1]["cell_type"].value_counts().sort_index().to_dict()
        return bool(positions_ok and batch_ok and order_ok) and not starved, _detail(
            f"{queue['batch_index'].nunique()} batches of <= {size}; first batch by lineage {first}; lineage order "
            "preserved; no lineage starved",
            {
                "positions": bool(positions_ok),
                "batches": bool(batch_ok),
                "lineage_order": order_ok,
                f"starved_batches:{starved[:3]}": not starved,
            },
        )

    checks.run("queue:fair_cross_lineage_schedule", fair_schedule)
    return checks.results


def verify_manuscript_artifact(artifact_dir: Path, repo_root: Path) -> list[CheckResult]:
    results = artifact_integrity(artifact_dir, schemas.MANUSCRIPT_SCHEMA_VERSION)
    if not all(r.passed for r in results):
        return results
    manifest = read_json(artifact_dir / "manifest.json")
    ingest_dir = artifact_dir.parent / manifest["inputs"]["ingest_key"]
    results += [
        CheckResult(name=f"upstream:{r.name}", passed=r.passed, detail=r.detail)
        for r in published_integrity(ingest_dir)
    ]
    resources = manifest["inputs"]["resources"]
    checks = Checks()
    for name in ("hgnc", "collectri"):
        path = repo_root / resources[name]["path"]
        current = sha256_file(path) if path.is_file() else None
        checks.add(f"resource_unchanged:{name}", current == resources[name]["sha256"], f"{resources[name]['path']}")
    for path, digest in resources["seed_publication_lists"].items():
        current = sha256_file(repo_root / path) if (repo_root / path).is_file() else None
        checks.add(
            f"resource_unchanged:{path}", current == digest, "sha256 matches" if current == digest else "CHANGED"
        )
    results += checks.results
    if not all(r.passed for r in results):
        return results
    scope = ManuscriptScopeConfig.model_validate(manifest["config"]["scope"])
    config = CandidateGenerationConfig.model_validate(manifest["config"]["candidate_generation"])
    queue_config = RetrievalQueueConfig.model_validate(manifest["config"]["retrieval_queue"])
    return results + manuscript_checks(
        artifact_dir, ingest_dir, repo_root, scope, config, queue_config, repo_root / resources["hgnc"]["path"]
    )
