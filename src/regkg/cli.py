"""Command-line entry point: argument parsing and dispatch only."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import regkg
from regkg.config import ConfigError, find_repo_root, load_model_settings, load_project_config


def _package_repo_root() -> Path:
    """Repository of this (editable) checkout; the working directory is never consulted."""
    return find_repo_root(Path(regkg.__file__).resolve().parent)


def _default_config() -> Path:
    return _package_repo_root() / "configs" / "project.yaml"


def _print_checks(results) -> int:
    failed = [result for result in results if not result.passed]
    for result in results:
        print(f"{'PASS' if result.passed else 'FAIL'}  {result.name}: {result.detail}")
    print(f"status: {'FAILED' if failed else 'PASSED'} ({len(results) - len(failed)}/{len(results)} checks passed)")
    return 1 if failed else 0


def cmd_ingest(args: argparse.Namespace) -> int:
    from regkg.project_data.ingest import run_ingest

    loaded = load_project_config(args.config)
    outcome = run_ingest(loaded)
    try:
        location = outcome.artifact_dir.relative_to(loaded.repo_root).as_posix()
    except ValueError:
        location = outcome.artifact_dir.as_posix()
    print(f"status: {outcome.status.value}")
    print(f"ingest_key: {outcome.ingest_key}")
    print(f"artifact: {location}")
    print(f"execution_id: {outcome.execution_id}")
    print(f"input_mode: {loaded.config.input_mode.value}")
    for name, count in sorted(outcome.row_counts.items()):
        print(f"rows {name}: {count}")
    return 0


def cmd_verify_project_data(args: argparse.Namespace) -> int:
    from regkg.project_data.verify import verify_artifact

    loaded = load_project_config(args.config)
    artifact_dir = loaded.data_root / "processed" / args.run
    if not artifact_dir.is_dir():
        print(f"error: no ingest artifact {args.run!r} under {loaded.data_root / 'processed'}", file=sys.stderr)
        return 1
    print(f"ingest_key: {args.run}")
    return _print_checks(verify_artifact(artifact_dir, loaded.repo_root))


def cmd_candidates(args: argparse.Namespace) -> int:
    from regkg.analysis.stage import run_candidates

    loaded = load_project_config(args.config)
    root = loaded.repo_root
    outcome = run_candidates(
        loaded,
        args.run,
        args.cell_type,
        args.ranking or root / "configs" / "ranking.yaml",
        args.literature or root / "configs" / "literature.yaml",
    )
    print(f"status: {outcome.status.value}")
    print(f"candidate_key: {outcome.candidate_key}")
    print(f"artifact: {outcome.artifact_dir.relative_to(root).as_posix()}")
    print(f"execution_id: {outcome.execution_id}")
    print(f"network_requests: {outcome.network_requests}")
    for name, count in sorted(outcome.row_counts.items()):
        print(f"rows {name}: {count}")
    return 0


def cmd_manuscript_candidates(args: argparse.Namespace) -> int:
    from regkg.analysis.manuscript import run_manuscript_candidates

    loaded = load_project_config(args.config)
    root = loaded.repo_root
    outcome = run_manuscript_candidates(
        loaded,
        args.run,
        args.scope or root / "configs" / "manuscript_scope.yaml",
        args.ranking or root / "configs" / "ranking.yaml",
        args.literature or root / "configs" / "literature.yaml",
    )
    print(f"status: {outcome.status.value}")
    print(f"candidate_key: {outcome.candidate_key}")
    print(f"artifact: {outcome.artifact_dir.relative_to(root).as_posix()}")
    print(f"execution_id: {outcome.execution_id}")
    print(f"network_requests: {outcome.network_requests}")
    for name, count in sorted(outcome.row_counts.items()):
        print(f"rows {name}: {count}")
    return 0


def cmd_verify_manuscript_candidates(args: argparse.Namespace) -> int:
    from regkg.analysis.manuscript import KEY_PREFIX, verify_manuscript_artifact

    loaded = load_project_config(args.config)
    artifact_dir = loaded.data_root / "processed" / args.run
    if not args.run.startswith(f"{KEY_PREFIX}-") or not artifact_dir.is_dir():
        print(f"error: no manuscript candidate artifact {args.run!r}", file=sys.stderr)
        return 1
    print(f"candidate_key: {args.run}")
    return _print_checks(verify_manuscript_artifact(artifact_dir, loaded.repo_root))


def cmd_verify_candidates(args: argparse.Namespace) -> int:
    from regkg.analysis.verify import verify_candidate_artifact

    loaded = load_project_config(args.config)
    artifact_dir = loaded.data_root / "processed" / args.run
    if not args.run.startswith("candidates-") or not artifact_dir.is_dir():
        print(f"error: no candidate artifact {args.run!r} under {loaded.data_root / 'processed'}", file=sys.stderr)
        return 1
    print(f"candidate_key: {args.run}")
    return _print_checks(verify_candidate_artifact(artifact_dir, loaded.repo_root))


def _literature_path(loaded, args) -> Path:
    return args.literature or loaded.repo_root / "configs" / "literature.yaml"


def _print_stage(outcome, root: Path) -> int:
    print(f"status: {outcome.status.value}")
    print(f"key: {outcome.key}")
    print(f"artifact: {outcome.artifact_dir.relative_to(root).as_posix()}")
    print(f"execution_id: {outcome.execution_id}")
    # This execution's actual requests; the counts below are the stored build counts of the artifact.
    print(f"execution_requests: {json.dumps(outcome.network_requests, sort_keys=True)}")
    for name, value in outcome.counts.items():
        shown = json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else value
        print(f"build.{name}: {shown}")
    return 0


def cmd_literature(args: argparse.Namespace) -> int:
    from regkg.workflows import literature as flow

    loaded = load_project_config(args.config)
    path = _literature_path(loaded, args)
    if args.action == "search":
        outcome = flow.run_search(loaded, args.run, args.max_papers, path)
    elif args.action == "fetch":
        outcome = flow.run_fetch(loaded, args.run, path)
    else:
        outcome = flow.run_retrieve(loaded, args.run, path)
    return _print_stage(outcome, loaded.repo_root)


def cmd_corpus(args: argparse.Namespace) -> int:
    from regkg.workflows import corpus

    loaded = load_project_config(args.config)
    path = _literature_path(loaded, args)
    if args.action == "corpus-audit":
        result = corpus.run_corpus_audit(loaded, args.run, path, args.max_batches)
    elif args.action == "discover":
        result = corpus.run_corpus_discovery(loaded, args.run, path, args.max_batches)
    elif args.action == "synonym-discover":
        result = corpus.run_synonym_discovery(loaded, args.run, path, args.max_batches)
    elif args.action == "ontology-setup":
        from regkg.literature.ontology import setup_pinned
        from regkg.resources import Fetcher

        fetcher = Fetcher()
        pins = setup_pinned(
            loaded.repo_root / "configs" / "ontology_scope.yaml", loaded.data_root / "external", fetcher
        )
        result = {
            "status": "SUCCEEDED",
            "key": "(pinned ontology releases)",
            "artifact": loaded.data_root / "external" / "ontologies",
            "corpus_id": "-",
            "counts": {"releases": pins, "network_requests": fetcher.requests},
        }
    elif args.action == "intake":
        from regkg.workflows.corpus_prepare import run_intake_step

        result = run_intake_step(loaded, args.run, path)
    elif args.action == "screen-run":
        from regkg.workflows.screening import run_screening_command

        result = run_screening_command(
            loaded,
            args.run,
            path,
            args.corpus,
            args.limit,
            args.pmids.split(",") if args.pmids else None,
            args.label,
            args.pool,
            args.repair_failed,
        )
    elif args.action == "screen-dry-run":
        from regkg.workflows.screening import run_screening_dry_run

        result = run_screening_dry_run(loaded, args.run, path, args.corpus, args.limit)
    elif args.action == "full-text-retry":
        result = corpus.run_full_text_retry(loaded, args.run, path, args.pmids.split(","))
    elif args.action == "gap-discover":
        result = corpus.run_gap_discovery(loaded, args.run, path)
    elif args.action == "scope-closure":
        from regkg.workflows.scope_closure import run_scope_closure

        result = run_scope_closure(loaded, args.run, path)
    elif args.action == "pilot-propose":
        from regkg.workflows.corpus_pilot import run_pilot_proposal

        result = run_pilot_proposal(loaded, args.run, path, args.corpus)
    elif args.action == "corpus-prepare":
        from regkg.workflows.corpus_prepare import run_corpus_prepare

        result = run_corpus_prepare(loaded, args.run, path)
    else:
        raise ValueError(f"unknown corpus action {args.action}")
    print(f"status: {result['status']}")
    print(f"key: {result['key']}")
    print(f"artifact: {result['artifact'].relative_to(loaded.repo_root).as_posix()}")
    print(f"corpus_id: {result['corpus_id']}")
    for name, value in result["counts"].items():
        shown = json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else value
        print(f"{name}: {shown}")
    return 0


def cmd_verify_literature(args: argparse.Namespace) -> int:
    from regkg.literature.verify import verify_literature

    loaded = load_project_config(args.config)
    directory = loaded.data_root / "processed" / args.run
    if not args.run.startswith("litretrieval-") or not directory.is_dir():
        print(f"error: no retrieval artifact {args.run!r} under {loaded.data_root / 'processed'}", file=sys.stderr)
        return 1
    print(f"retrieval_key: {args.run}")
    return _print_checks(verify_literature(directory, loaded.repo_root, _literature_path(loaded, args)))


def cmd_verify_config(args: argparse.Namespace) -> int:
    settings = load_model_settings(args.repo_root or _package_repo_root())
    # Only nonsecret selections and credential presence are printed, never credential values.
    print(json.dumps(settings.to_record(), indent=2, sort_keys=True))
    missing = settings.missing_credentials
    print(f"status: {'PARTIAL' if missing else 'PASSED'}; missing credentials for live calls: {missing or 'none'}")
    return 0


def cmd_extract(args: argparse.Namespace) -> int:
    import fcntl

    from regkg.workflows.extraction import run

    root = _package_repo_root()
    path = root / "data/work/p4.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = run(
            root,
            args.run,
            args.limit,
            args.live,
            args.assembly,
            args.retry_failed,
            batch_index=args.batch,
            assembly_repair=args.assembly_repair,
        )
    print(json.dumps(result, indent=2))
    return 1 if result["status"] in {"PREFLIGHT_FAILED", "PARTIAL_WORKFLOW"} else 0


def cmd_verify_evidence(args: argparse.Namespace) -> int:
    from regkg.workflows.extraction import verify_evidence

    print(json.dumps(verify_evidence(_package_repo_root(), args.run), indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="regkg", description="Spatial NicheLinker regulatory evidence KG")
    commands = parser.add_subparsers(dest="command", required=True)

    extract = commands.add_parser("extract", help="prepare or validate P4 against a verified P3 selection")
    extract.add_argument("--run", required=True, help="p3selection-* source artifact")
    choice = extract.add_mutually_exclusive_group()
    choice.add_argument("--limit", type=int, default=8, help="representative validation bundles, maximum 20")
    choice.add_argument("--batch", type=int, default=None, help="consume one complete numbered P3 ready batch")
    execution = extract.add_mutually_exclusive_group()
    execution.add_argument("--dry-run", action="store_true", help="pin and verify inputs without model calls (default)")
    execution.add_argument("--live", action="store_true")
    extract.add_argument("--assembly", action="store_true", help="also validate one source-context investigation")
    extract.add_argument("--assembly-repair", default=None, help="named repair of a stopped, reconciled assembly case")
    extract.add_argument("--retry-failed", action="store_true", help="retry known failures within remaining allowance")
    extract.set_defaults(handler=cmd_extract)

    ingest = commands.add_parser("ingest", help="audit and ingest all supplied project data")
    ingest.add_argument("--config", type=Path, required=True, help="project configuration YAML")
    ingest.set_defaults(handler=cmd_ingest)

    candidates = commands.add_parser("candidates", help="build AT1 candidates, curated prior, and retrieval queue")
    candidates.add_argument("--run", required=True, help="accepted ingest key")
    candidates.add_argument("--cell-type", required=True)
    candidates.add_argument("--config", type=Path, default=None, help="project configuration")
    candidates.add_argument("--ranking", type=Path, default=None, help="default: configs/ranking.yaml")
    candidates.add_argument("--literature", type=Path, default=None, help="default: configs/literature.yaml")
    candidates.set_defaults(handler=cmd_candidates)

    manuscript = commands.add_parser(
        "manuscript-candidates", help="candidates and fair query batches for every manuscript regulatory case"
    )
    manuscript.add_argument("--run", required=True, help="accepted ingest key")
    manuscript.add_argument("--config", type=Path, default=None, help="project configuration")
    manuscript.add_argument("--scope", type=Path, default=None, help="default: configs/manuscript_scope.yaml")
    manuscript.add_argument("--ranking", type=Path, default=None, help="default: configs/ranking.yaml")
    manuscript.add_argument("--literature", type=Path, default=None, help="default: configs/literature.yaml")
    manuscript.set_defaults(handler=cmd_manuscript_candidates)

    literature = commands.add_parser("literature", help="bounded literature search, fetch/parse, and retrieval")
    actions = literature.add_subparsers(dest="action", required=True)
    for action, help_text in (
        ("search", "execute the queued queries and select the corpus"),
        ("fetch", "fetch eligible assets and parse canonical documents"),
        ("retrieve", "rank passages and assemble evidence bundles"),
    ):
        sub = actions.add_parser(action, help=help_text)
        sub.add_argument("--run", required=True, help="upstream artifact key")
        sub.add_argument("--config", type=Path, default=None, help="project configuration")
        sub.add_argument("--literature", type=Path, default=None, help="default: configs/literature.yaml")
        if action == "search":
            sub.add_argument("--max-papers", type=int, required=True)
        sub.set_defaults(handler=cmd_literature)

    audit = actions.add_parser(
        "corpus-audit",
        help="reconcile and audit the whole advisor corpus; publish the coverage ledger and manual-download report",
    )
    audit.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    audit.add_argument("--max-batches", type=int, default=None, help="stop after this many new batches (resumable)")
    audit.add_argument("--config", type=Path, default=None)
    audit.add_argument("--literature", type=Path, default=None)
    audit.set_defaults(handler=cmd_corpus)

    discover = actions.add_parser("discover", help="execute the manuscript query queue in resumable batches")
    discover.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    discover.add_argument("--max-batches", type=int, default=None, help="stop after this many new batches (resumable)")
    discover.add_argument("--config", type=Path, default=None)
    discover.add_argument("--literature", type=Path, default=None)
    discover.set_defaults(handler=cmd_corpus)

    synonym = actions.add_parser(
        "synonym-discover", help="run the separate supplemental ontology-synonym queue and bounded tier-1 acquisition"
    )
    synonym.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    synonym.add_argument("--max-batches", type=int, default=None, help="unused; kept for command symmetry")
    synonym.add_argument("--config", type=Path, default=None)
    synonym.add_argument("--literature", type=Path, default=None)
    synonym.set_defaults(handler=cmd_corpus)

    pilot = actions.add_parser(
        "pilot-propose", help="propose a <=10-paper/<=20-bundle P4 pilot from a corpus artifact (reports/ only)"
    )
    pilot.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    pilot.add_argument("--corpus", required=True, help="published corpus artifact key (litcorpus-*)")
    pilot.add_argument("--config", type=Path, default=None)
    pilot.add_argument("--literature", type=Path, default=None)
    pilot.set_defaults(handler=cmd_corpus)

    closure = actions.add_parser(
        "scope-closure", help="validate the audited validation selection and publish frontier dispositions"
    )
    closure.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    closure.add_argument("--config", type=Path, default=None)
    closure.add_argument("--literature", type=Path, default=None)
    closure.set_defaults(handler=cmd_corpus)

    gap = actions.add_parser(
        "gap-discover", help="run the bounded gap-directed queue for lineages without exact-population evidence"
    )
    gap.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    gap.add_argument("--config", type=Path, default=None)
    gap.add_argument("--literature", type=Path, default=None)
    gap.set_defaults(handler=cmd_corpus)

    retry = actions.add_parser(
        "full-text-retry", help="re-fetch full text for named PMIDs whose JATS record carries no body"
    )
    retry.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    retry.add_argument("--pmids", required=True, help="comma-separated PMIDs")
    retry.add_argument("--config", type=Path, default=None)
    retry.add_argument("--literature", type=Path, default=None)
    retry.set_defaults(handler=cmd_corpus)

    dry = actions.add_parser(
        "screen-dry-run", help="estimate LLM screening coverage, windows and tokens; makes no chat call"
    )
    dry.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    dry.add_argument("--corpus", required=True, help="published corpus artifact key (litcorpus-*)")
    dry.add_argument("--limit", type=int, default=None, help="estimate only the first N papers")
    dry.add_argument("--config", type=Path, default=None)
    dry.add_argument("--literature", type=Path, default=None)
    dry.set_defaults(handler=cmd_corpus)

    live = actions.add_parser("screen-run", help="screen frozen acquired/discovered pools within the allowance")
    live.add_argument("--pool", choices=["all", "acquired", "discovery"], default="all")
    live.add_argument(
        "--repair-failed",
        action="store_true",
        help="repair failed windows in separate provenance-linked caches; reuse valid windows",
    )
    live.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
    live.add_argument("--corpus", required=True, help="published corpus artifact key (litcorpus-*)")
    live.add_argument("--limit", type=int, default=None, help="screen at most N papers in this invocation")
    live.add_argument("--pmids", default=None, help="comma-separated PMIDs (validation slice)")
    live.add_argument("--label", default="run", help="name for this run's ledger files")
    live.add_argument("--config", type=Path, default=None)
    live.add_argument("--literature", type=Path, default=None)
    live.set_defaults(handler=cmd_corpus)

    for action, help_text in (
        ("intake", "ingest user-supplied files from data/papers/manual_inbox (identity-checked)"),
        ("ontology-setup", "fetch/verify exactly the pinned CL, UBERON, and MONDO releases"),
        ("corpus-prepare", "parse, screen, retrieve; publish readiness, ready batches, and the inference budget"),
    ):
        sub = actions.add_parser(action, help=help_text)
        sub.add_argument("--run", required=True, help="accepted manuscript candidate key (mcandidates-*)")
        sub.add_argument("--config", type=Path, default=None)
        sub.add_argument("--literature", type=Path, default=None)
        sub.set_defaults(handler=cmd_corpus)

    verify = commands.add_parser("verify", help="verify a stage artifact or configuration")
    targets = verify.add_subparsers(dest="target", required=True)
    evidence_check = targets.add_parser("evidence", help="verify P4 file hashes, joins and exact source spans")
    evidence_check.add_argument("--run", required=True)
    evidence_check.set_defaults(handler=cmd_verify_evidence)
    project_data = targets.add_parser("project-data", help="verify an ingest artifact")
    project_data.add_argument("--run", required=True, help="ingest key printed by 'regkg ingest'")
    project_data.add_argument(
        "--config", type=Path, default=None, help="project configuration (default: configs/project.yaml)"
    )
    project_data.set_defaults(handler=cmd_verify_project_data)
    candidate_check = targets.add_parser("candidates", help="verify a candidate artifact")
    candidate_check.add_argument("--run", required=True, help="candidate key printed by 'regkg candidates'")
    candidate_check.add_argument("--config", type=Path, default=None, help="project configuration")
    candidate_check.set_defaults(handler=cmd_verify_candidates)
    manuscript_check = targets.add_parser("manuscript-candidates", help="verify a manuscript candidate artifact")
    manuscript_check.add_argument("--run", required=True, help="key printed by 'regkg manuscript-candidates'")
    manuscript_check.add_argument("--config", type=Path, default=None, help="project configuration")
    manuscript_check.set_defaults(handler=cmd_verify_manuscript_candidates)
    literature_check = targets.add_parser("literature", help="verify a literature retrieval artifact chain")
    literature_check.add_argument("--run", required=True, help="retrieval key printed by 'regkg literature retrieve'")
    literature_check.add_argument("--config", type=Path, default=None)
    literature_check.add_argument("--literature", type=Path, default=None)
    literature_check.set_defaults(handler=cmd_verify_literature)
    config = targets.add_parser("config", help="resolve model selections without SDKs, network, or secrets")
    config.add_argument("--repo-root", type=Path, default=None)
    config.set_defaults(handler=cmd_verify_config)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if getattr(args, "config", "unset") is None:
        args.config = _default_config()
    try:
        return args.handler(args)
    except ConfigError as error:
        print(f"configuration error: {error}", file=sys.stderr)
        return 2
    except Exception as error:  # noqa: BLE001 - surface stage failures as a nonzero exit with the reason
        print(f"status: FAILED\nerror: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
