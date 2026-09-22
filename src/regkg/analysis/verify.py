"""Checks of a candidate artifact, run before publication and by `regkg verify candidates`.

Deterministic outputs (candidate union, targets, queue) are recomputed from the stored inputs
with the same functions and must match exactly.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from regkg.analysis import schemas
from regkg.analysis.candidates import (
    REASON_CONCORDANCE,
    REASON_SEED,
    REGULATOR_SCOPE,
    resolve_seeds,
    select_candidates,
)
from regkg.analysis.concordance import PRIMARY_POLICY, SENSITIVITY_POLICY
from regkg.analysis.gene_mapping import MAPPING_RULE_VERSION, RESOLVED, read_hgnc, symbol_index
from regkg.analysis.queue import STATUS_NOT_SEARCHED, build_queue, query_names
from regkg.config import CandidateGenerationConfig, RetrievalQueueConfig
from regkg.models import CheckResult, StageStatus
from regkg.project_data.verify import Checks
from regkg.provenance import read_json, sha256_file


def _read(directory: Path, name: str) -> pd.DataFrame:
    return pq.read_table(directory / name).to_pandas()


def _same_rows(expected: pd.DataFrame, stored: pd.DataFrame, schema: pa.Schema) -> bool:
    """Compare through the declared Arrow schema, so Parquet round-trip dtypes cannot mask or fake a match."""
    columns = [name for name in schema.names if name in expected.columns]
    subset = pa.schema([schema.field(name) for name in columns])

    def table(frame: pd.DataFrame) -> pa.Table:
        return pa.Table.from_pandas(frame[columns].reset_index(drop=True), schema=subset, preserve_index=False)

    return table(expected).equals(table(stored))


def _detail(summary: str, failures: dict[str, bool]) -> str:
    failed = [name for name, passed in failures.items() if not passed]
    return summary if not failed else f"{summary} -- FAILED: {', '.join(failed)}"


def artifact_integrity(artifact_dir: Path, schema_version: str = schemas.CANDIDATE_SCHEMA_VERSION) -> list[CheckResult]:
    checks = Checks()
    manifest_path = artifact_dir / "manifest.json"
    if not manifest_path.is_file():
        checks.add("manifest:present", False, "missing manifest.json")
        return checks.results
    manifest = read_json(manifest_path)
    checks.add(
        "manifest:status",
        manifest.get("status") == StageStatus.SUCCEEDED.value
        and manifest.get("schema_version") == schema_version
        and manifest.get("candidate_key") == artifact_dir.name,
        f"status {manifest.get('status')}, schema {manifest.get('schema_version')}, "
        f"key {manifest.get('candidate_key')}",
    )
    listed = {o["path"]: o["sha256"] for o in manifest.get("outputs", [])}
    present = {p.relative_to(artifact_dir).as_posix() for p in artifact_dir.rglob("*") if p.is_file()} - {
        "manifest.json"
    }
    changed = sorted(
        p for p, digest in listed.items() if not (artifact_dir / p).is_file() or sha256_file(artifact_dir / p) != digest
    )
    checks.add(
        "manifest:output_checksums",
        not changed and present == set(listed),
        f"{len(listed)} outputs; changed/missing {changed}; unlisted {sorted(present - set(listed))}",
    )
    return checks.results


def table_checks(
    artifact_dir: Path,
    ingest_dir: Path,
    repo_root: Path,
    config: CandidateGenerationConfig,
    queue_config: RetrievalQueueConfig,
    tf_seeds: list[str],
    hgnc_path: Path,
) -> list[CheckResult]:
    checks = Checks()
    schema_checks(checks, artifact_dir, schemas.TABLE_SCHEMAS)
    shared_checks(checks, artifact_dir, ingest_dir, repo_root, config, hgnc_path)
    mappings = _read(artifact_dir, "gene_mappings.parquet")
    concordance = _read(artifact_dir, "concordance.parquet")
    candidates = _read(artifact_dir, "candidates.parquet")
    targets = _read(artifact_dir, "candidate_targets.parquet")
    queue = _read(artifact_dir, "retrieval_queue.parquet")

    def candidate_selection() -> tuple[bool, str]:
        mapped = mappings
        seeds = resolve_seeds(tf_seeds, mapped)
        primary = concordance[concordance["sign_policy"] == PRIMARY_POLICY]
        comparisons = _read(artifact_dir, "comparisons.parquet")
        expected = select_candidates(comparisons, primary, seeds, config.extra_tfs_per_comparison, config.rule_version)
        same = _same_rows(expected, candidates, schemas.CANDIDATES)
        per = candidates.groupby("comparison_id")
        seeds_ok = all(
            set(seeds["hgnc_id"])
            <= set(
                candidates.loc[
                    (candidates["comparison_id"] == c) & candidates["reasons"].map(lambda r: REASON_SEED in r),
                    "tf_hgnc_id",
                ]
            )
            for c in comparisons["comparison_id"]
        ) and set(candidates["regulator_scope"]) <= {REGULATOR_SCOPE}
        extras = candidates[~candidates["is_seed"]]
        extras_ok = (
            extras["reasons"].map(lambda r: list(r) == [REASON_CONCORDANCE]).all()
            and per.apply(lambda g: (~g["is_seed"]).sum() <= config.extra_tfs_per_comparison).all()
        )
        return (
            same and seeds_ok and bool(extras_ok),
            _detail(
                f"{len(candidates)} candidates across {per.ngroups} comparisons; all {len(seeds)} seeds in each; "
                f"<= {config.extra_tfs_per_comparison} extras each; recomputed selection identical",
                {"recomputed_selection": same, "seeds_present": seeds_ok, "extras_bounded": bool(extras_ok)},
            ),
        )

    checks.run("candidates:seeds_topk_ties", candidate_selection)

    checks.run("candidates:no_connectivity_rank", lambda: connectivity_semantics(candidates))

    checks.run(
        "targets:bounded_selection",
        lambda: target_selection(targets, mappings, _read(artifact_dir, "comparison_vectors.parquet"), config),
    )

    def queue_rules() -> tuple[bool, str]:
        hgnc = read_hgnc(hgnc_path)
        names = query_names(
            set(candidates["tf_hgnc_id"]) | set(targets.get("target_hgnc_id", [])),
            hgnc,
            queue_config.max_aliases_per_gene,
        )
        same = _same_rows(build_queue(candidates, targets, names, queue_config), queue, schemas.RETRIEVAL_QUEUE)
        ok = (
            queue["query_id"].is_unique
            and queue["priority"].tolist() == list(range(1, len(queue) + 1))
            and set(queue["search_status"]) == {STATUS_NOT_SEARCHED}
            and queue["date_restriction"].isna().all()
            and int(queue["in_initial_live_slice"].sum()) == min(len(queue), queue_config.max_live_queries)
        )
        every_tf = set(candidates["tf_hgnc_id"]) <= set(queue["tf_hgnc_id"])
        return (
            bool(same and ok and every_tf),
            _detail(
                f"{len(queue)} queries, all NOT_SEARCHED, priorities 1..{len(queue)}; initial slice "
                f"{int(queue['in_initial_live_slice'].sum())}; every candidate TF queued; rebuild identical",
                {"rebuild_identical": same, "status_priority_slice": bool(ok), "every_tf_queued": every_tf},
            ),
        )

    checks.run("queue:reproducible", queue_rules)
    return checks.results


def schema_checks(checks: Checks, artifact_dir: Path, table_schemas: dict[str, pa.Schema]) -> None:
    for name, schema in table_schemas.items():
        checks.run(
            f"schema:{name}",
            lambda name=name, schema=schema: (
                pq.read_schema(artifact_dir / name).remove_metadata().equals(schema),
                "matches the declared Arrow schema",
            ),
        )


def shared_checks(
    checks: Checks,
    artifact_dir: Path,
    ingest_dir: Path,
    repo_root: Path,
    config: CandidateGenerationConfig,
    hgnc_path: Path,
) -> None:
    """Mapping, resource, prior, advisor-metadata, and concordance checks common to every scope."""
    genes = _read(ingest_dir, "genes.parquet")
    mappings = _read(artifact_dir, "gene_mappings.parquet")
    priors = _read(artifact_dir, "prior_interactions.parquet")
    concordance = _read(artifact_dir, "concordance.parquet")
    publications = _read(artifact_dir, "seed_publications.parquet")
    resources = read_json(artifact_dir / "resources.json")

    def gene_mapping() -> tuple[bool, str]:
        same_ids = mappings["gene_id"].tolist() == genes["gene_id"].tolist()
        same_symbols = mappings["source_symbol"].tolist() == genes["source_symbol"].tolist()
        resolved = mappings[mappings["mapping_status"].isin(RESOLVED)]
        one_to_one = not resolved["hgnc_id"].duplicated().any() and resolved["hgnc_id"].notna().all()
        unresolved_null = mappings.loc[~mappings["mapping_status"].isin(RESOLVED), "hgnc_id"].isna().all()
        versioned = set(mappings["mapping_version"]) == {config.resources.hgnc.archive_date}
        return (
            same_ids and same_symbols and one_to_one and bool(unresolved_null) and versioned,
            f"{len(mappings)} P1 gene IDs preserved in order; {len(resolved)} resolved one-to-one to HGNC; "
            "ambiguous/conflicting/unresolved carry no HGNC ID",
        )

    checks.run("genes:mapping_preserves_p1_ids", gene_mapping)

    # Independent of the resolver: every indirect resolution must have exactly one owner across the
    # snapshot's previous-symbol and alias fields together; every ambiguous one must have several.
    def indirect_mappings_unambiguous() -> tuple[bool, str]:
        _, previous, alias = symbol_index(read_hgnc(hgnc_path))

        def owners(symbol: str) -> set[str]:
            return previous.get(symbol, set()) | alias.get(symbol, set())

        entities = pd.concat(
            [
                mappings[["source_symbol", "mapping_status", "hgnc_id"]].rename(columns={"source_symbol": "symbol"}),
                priors[["target_symbol_raw", "target_mapping_status", "target_hgnc_id"]].set_axis(
                    ["symbol", "mapping_status", "hgnc_id"], axis=1
                ),
                priors.loc[
                    priors["regulator_type"] == "gene",
                    ["regulator_symbol_raw", "regulator_mapping_status", "regulator_hgnc_id"],
                ].set_axis(["symbol", "mapping_status", "hgnc_id"], axis=1),
            ]
        ).drop_duplicates()
        indirect = entities[entities["mapping_status"].isin({"resolved_previous_symbol", "resolved_alias_symbol"})]
        bad_indirect = [s for s, h in zip(indirect["symbol"], indirect["hgnc_id"], strict=True) if owners(s) != {h}]
        ambiguous = entities[entities["mapping_status"] == "ambiguous"]
        bad_ambiguous = [
            s
            for s, h in zip(ambiguous["symbol"], ambiguous["hgnc_id"], strict=True)
            if len(owners(s)) < 2 or pd.notna(h)
        ]
        rule_ok = set(mappings["mapping_rule_version"]) == {MAPPING_RULE_VERSION}
        return (
            not bad_indirect and not bad_ambiguous and rule_ok,
            _detail(
                f"{len(indirect)} indirect resolutions each have one owner across previous+alias fields; "
                f"{len(ambiguous)} ambiguous symbols have several owners and no selected ID",
                {
                    f"indirect_not_unique:{bad_indirect[:5]}": not bad_indirect,
                    f"ambiguous_inconsistent:{bad_ambiguous[:5]}": not bad_ambiguous,
                    "rule_version": rule_ok,
                },
            ),
        )

    checks.run("genes:indirect_mappings_unambiguous", indirect_mappings_unambiguous)

    def resource_provenance() -> tuple[bool, str]:
        ok, details = True, []
        for name in ("hgnc", "collectri"):
            item = resources[name]
            ok &= sha256_file(repo_root / item["path"]) == item["sha256"]
            ok &= bool(item["publisher_md5_verified"]) and bool(item.get("license")) and bool(item.get("version"))
            details.append(
                f"{name} {item.get('version')} sha256 {item['sha256'][:12]}… license {item.get('license')!r}"
            )
        prior_ok = set(priors["snapshot_sha256"]) == {resources["collectri"]["sha256"]}
        return ok and prior_ok, "; ".join(details) + "; every prior record carries the snapshot hash"

    checks.run("resources:provenance", resource_provenance)

    def prior_preservation() -> tuple[bool, str]:
        raw = pd.read_csv(repo_root / resources["collectri"]["path"], dtype=str, keep_default_na=False)
        raw_rows = len(raw)
        complexes = priors[priors["regulator_type"] == "complex"]
        complex_ok = (
            set(complexes["regulator_symbol_raw"]) <= set(config.resources.collectri.complex_regulators)
            and complexes["regulator_hgnc_id"].isna().all()
        )
        unknown_ok = ((priors["sign"] == "unknown") == (priors["sign_basis"] == "default_activation")).all()
        unique = priors["prior_interaction_id"].is_unique
        return (
            len(priors) == raw_rows and complex_ok and bool(unknown_ok) and unique,
            f"{len(priors)} records = {raw_rows} source rows; {len(complexes)} complex records not split; "
            "sign unknown exactly where CollecTRI assumed default activation",
        )

    checks.run("prior:records_complexes_signs", prior_preservation)

    def seed_publication_metadata() -> tuple[bool, str]:
        memberships = int(publications["memberships"].map(len).sum())
        expected = config.resources.expected_unique_pmids
        ok = (
            publications["pmid"].is_unique
            and len(publications) == expected
            and set(publications["evidence_status"]) == {"seed_metadata_not_evidence"}
        )
        return ok, f"{len(publications)} unique PMIDs (expected {expected}), {memberships} memberships; metadata only"

    checks.run("seeds:publications", seed_publication_metadata)

    def concordance_rules() -> tuple[bool, str]:
        eligible_ok = (concordance["eligible"] == (concordance["observed_targets"] >= concordance["min_targets"])).all()
        score_ok = (concordance["ulm_score"].notna() == concordance["eligible"]).all()
        direction = concordance["ulm_score"].map(
            lambda s: None if pd.isna(s) else "positive" if s > 0 else "negative" if s < 0 else "zero"
        )
        direction_ok = (direction.fillna("none") == concordance["concordance_direction"].fillna("none")).all()
        tmin_ok = set(concordance["min_targets"]) <= {config.concordance.min_targets}
        policies_ok = set(concordance["sign_policy"]) <= {PRIMARY_POLICY, SENSITIVITY_POLICY}
        return (
            bool(eligible_ok and score_ok and direction_ok and tmin_ok and policies_ok),
            f"scores exist exactly where observed targets >= {config.concordance.min_targets}; "
            "direction = sign of score",
        )

    checks.run("concordance:coverage_rule", concordance_rules)


def connectivity_semantics(candidates: pd.DataFrame) -> tuple[bool, str]:
    ok = (
        candidates["connectivity_rank"].isna().all()
        and candidates["interpreted_connectivity_delta"].isna().all()
        and set(candidates["score_semantics_status"]) == {"unconfirmed"}
    )
    return bool(ok), "connectivity rank and interpreted delta null for every candidate; semantics unconfirmed"


def target_selection(
    targets: pd.DataFrame, mappings: pd.DataFrame, vectors: pd.DataFrame, config: CandidateGenerationConfig
) -> tuple[bool, str]:
    if targets.empty:
        return True, "no eligible targets"
    per = targets.groupby("candidate_id")
    bounded = per.size().le(config.targets_per_candidate).all()
    resolved = set(mappings.loc[mappings["mapping_status"].isin(RESOLVED), "gene_id"])
    ordered = True
    for _, group in per:
        effects = group.sort_values("target_rank")
        key = list(zip(-effects["effect_niche2_minus_niche1"].abs(), effects["target_gene_id"], strict=True))
        ordered &= key == sorted(key)
    routed = targets["source_routes"].map(len).gt(0).all()
    in_vectors = (
        targets.merge(
            vectors, left_on=["comparison_id", "target_gene_id"], right_on=["comparison_id", "gene_id"], how="left"
        )["approved_symbol"]
        .notna()
        .all()
    )
    return (
        bool(bounded and ordered and routed and in_vectors and targets["target_gene_id"].isin(resolved).all()),
        f"{len(targets)} targets for {per.ngroups} candidates; <= {config.targets_per_candidate} each; "
        "resolved, route-linked, ordered by |effect| then gene ID",
    )


def verify_candidate_artifact(artifact_dir: Path, repo_root: Path) -> list[CheckResult]:
    from regkg.config import CandidateGenerationConfig as Candidate
    from regkg.config import RetrievalQueueConfig as Queue
    from regkg.project_data.verify import published_integrity

    results = artifact_integrity(artifact_dir)
    if not all(r.passed for r in results):
        return results
    manifest = read_json(artifact_dir / "manifest.json")
    ingest_dir = artifact_dir.parent / manifest["inputs"]["ingest_key"]
    upstream = published_integrity(ingest_dir)
    results += [CheckResult(name=f"upstream:{r.name}", passed=r.passed, detail=r.detail) for r in upstream]
    resources = manifest["inputs"]["resources"]
    checks = Checks()
    for name in ("hgnc", "collectri"):
        path = repo_root / resources[name]["path"]
        current = sha256_file(path) if path.is_file() else None
        checks.add(
            f"resource_unchanged:{name}",
            current == resources[name]["sha256"],
            f"{resources[name]['path']} sha256 "
            f"{'matches' if current == resources[name]['sha256'] else 'CHANGED or missing'}",
        )
    for path, digest in resources["seed_publication_lists"].items():
        current = sha256_file(repo_root / path) if (repo_root / path).is_file() else None
        checks.add(
            f"resource_unchanged:{path}", current == digest, "sha256 matches" if current == digest else "CHANGED"
        )
    results += checks.results
    if not all(r.passed for r in results):
        return results
    config = Candidate.model_validate(manifest["config"]["candidate_generation"])
    queue_config = Queue.model_validate(manifest["config"]["retrieval_queue"])
    return results + table_checks(
        artifact_dir,
        ingest_dir,
        repo_root,
        config,
        queue_config,
        manifest["config"]["tf_seeds"],
        repo_root / resources["hgnc"]["path"],
    )
