"""Bounded paired-model trial of the ordinary grounded extraction engine."""

import argparse
import fcntl
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pandas as pd

from regkg.config import ModelSpec, load_environment, read_yaml
from regkg.extraction.config import load_config
from regkg.extraction.context_repair import recover_context
from regkg.extraction.grounded import extract_grounded, load_scientific_schema
from regkg.extraction.runtime import Runtime, build_chat_model
from regkg.extraction.sources import SourceRegistry, pubtator_context
from regkg.extraction.validation import EntityResolver
from regkg.provenance import canonical_json, code_fingerprint, read_json, sha256_file, sha256_text, write_json


def run_trial(
    root: Path,
    execute=False,
    split=None,
    case_ids=None,
    model_ids=None,
    critic_model=None,
    context_repair_id=None,
    retry_failed=False,
    request_timeout_seconds=None,
):
    cfg = read_yaml(root / "configs/extraction_trial.yaml")
    allowed_models = set(cfg["models"])
    if model_ids is not None:
        if not model_ids or len(model_ids) != len(set(model_ids)) or not set(model_ids) <= allowed_models:
            raise ValueError("Trial model is not one of the user-authorized aliases")
        cfg["models"] = model_ids
    if critic_model is not None and critic_model not in allowed_models:
        raise ValueError("Critic model is not one of the user-authorized aliases")
    cfg["critic_model"] = critic_model
    cfg["context_repair_id"] = context_repair_id
    cfg["retry_failed"] = retry_failed
    if request_timeout_seconds is not None and not 1 <= request_timeout_seconds <= 180:
        raise ValueError("Request timeout must be between 1 and 180 seconds")
    cfg["request_timeout_seconds"] = request_timeout_seconds
    policy = load_scientific_schema(root / "configs/extraction_schema.yaml")
    cases = [c for c in cfg["cases"] if split is None or c["split"] == split]
    if case_ids:
        cases = [c for c in cases if c["id"] in case_ids]
        if {c["id"] for c in cases} != set(case_ids):
            raise ValueError("Unknown trial case or incompatible split")
    if len(cases) > 20 or len(cfg["models"]) > 2 or not cases:
        raise ValueError("Trial must contain 1–20 cases and at most two configured models")
    registry = SourceRegistry(root, cfg["selection"], root / "data/work/corpus-c700d6e584b7bccf")
    sources, annotations = {}, {}
    for case in cases:
        bundle = registry.bundles[case["bundle_id"]]
        sources[case["id"]] = registry.validate_bundle(bundle)
        annotations[case["id"]] = pubtator_context(registry, sources[case["id"]])
    extraction_config = load_config(root / "configs/extraction.yaml")
    settings = extraction_config["runtime"]
    settings["reasoning_effort"] = cfg["reasoning_effort"]
    # Transport deadlines do not change messages/decoding; retain successful call
    # caches while recording the explicit override in the trial manifest.
    model_settings = {**settings, "timeout_seconds": request_timeout_seconds or settings["timeout_seconds"]}
    env = load_environment(root / ".env")
    identity = {
        "config": cfg,
        "split": split,
        "case_ids": case_ids,
        "schema": policy.model_dump(),
        "settings": settings,
        "assembly_limits": extraction_config["assembly"],
        "source_manifest": registry.manifest_hash,
        "external_identity_sha256": sha256_file(root / "data/external/p4-gene-identities.json")
        if (root / "data/external/p4-gene-identities.json").exists()
        else None,
        "source_files": registry.file_hashes,
        "annotations_sha256": sha256_text(canonical_json(annotations)),
        "code": code_fingerprint(root / "src/regkg", ["extraction", "workflows/extraction_trial.py"]),
    }
    key = "trial-" + sha256_text(canonical_json(identity))[:16]
    directory = root / "data/work/p4-accuracy" / key
    directory.mkdir(parents=True, exist_ok=True)
    manifest = {
        "key": key,
        "identity": identity,
        "cases": cases,
        "max_scheduled_calls": len(cases) * len(cfg["models"]) * 36,
        "reference_status": "No independent human gold labels; source audit required",
        "production_authorized": False,
    }
    write_json(directory / "manifest.json", manifest)
    if not execute:
        return {"status": "PREPARED_NO_CALLS", "directory": str(directory), **manifest}
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    os.environ["LANGSMITH_TRACING"] = "false"
    mapping_path = root / "data/processed/mcandidates-c278c6625ff7c537/gene_mappings.parquet"
    mapping = pd.read_parquet(mapping_path)
    catalog_path = root / "data/external/p4-gene-identities.json"
    catalog = read_json(catalog_path) if catalog_path.exists() else {}
    resolver = EntityResolver(mapping.to_dict("records"), str(mapping.mapping_version.iloc[0]), catalog)
    runtimes, models, shared_budget = {}, {}, None
    for alias in cfg["models"]:
        spec = ModelSpec("litellm", alias)
        verifier_spec = ModelSpec("litellm", critic_model or alias)
        rt = Runtime(
            root / "data/work/p4-accuracy" / alias,
            settings,
            {
                "model": spec.selector,
                "verifier_model": verifier_spec.selector,
                "settings": settings,
                "endpoint_hash": sha256_text(env.get("LITELLM_BASE_URL", "")),
                "mention_reasoning_effort": "low",
            },
            retry_failed=retry_failed,
            budget_path=root / "data/work/p4-validation/budget.json",
        )
        if shared_budget is None:
            shared_budget = rt.budget
        else:
            rt.budget = shared_budget
        runtimes[alias] = rt
        models[alias] = {
            "extractor": build_chat_model(spec, env, model_settings),
            "verifier": build_chat_model(verifier_spec, env, model_settings),
            "mentions": build_chat_model(spec, env, {**model_settings, "reasoning_effort": "low"}),
            "assembler": build_chat_model(
                verifier_spec,
                env,
                {
                    **settings,
                    "max_output_tokens": extraction_config["assembly"]["max_output_tokens"],
                    "timeout_seconds": extraction_config["assembly"]["model_timeout_seconds"],
                    "reasoning_effort": extraction_config["assembly"]["reasoning_effort"],
                },
            ),
        }
    before = shared_budget.used["calls"]
    results = []
    write_json(directory / "status.json", {"status": "RUNNING", "completed": 0, "total": len(cases) * len(models)})

    def execute_one(alias, case):
        print(f"TRIAL START {alias} {case['id']}", flush=True)
        bundle = registry.bundles[case["bundle_id"]]
        # Models have no access to evaluation labels, expected answers or other model results.
        records, outcome = extract_grounded(
            sources[case["id"]],
            bundle,
            annotations[case["id"]],
            policy,
            runtimes[alias],
            models[alias],
            resolver,
            context_recovery=lambda b, requests: recover_context(
                registry,
                b,
                requests,
                models[alias]["assembler"],
                runtimes[alias],
                extraction_config["assembly"],
                repair_id=context_repair_id,
            ),
        )
        result = {
            "model": alias,
            "model_roles": {
                "extractor": alias,
                "mentions": alias,
                "verifier": critic_model or alias,
                "assembler": critic_model or alias,
            },
            "case": case,
            "records": records,
            "outcome": outcome,
        }
        path = directory / alias / (case["id"] + ".json")
        write_json(path, result)
        print(f"TRIAL DONE {alias} {case['id']} {outcome['status']} findings={len(records)}", flush=True)
        return {
            "model": alias,
            "case": case["id"],
            "status": outcome["status"],
            "verification_status": outcome.get("verification_status"),
            "repair": outcome.get("repair"),
            "findings": len(records),
            "path": str(path.relative_to(root)),
            "sha256": sha256_file(path),
        }

    # Independent paired calls share one atomic accounting object and one process lock.
    with ThreadPoolExecutor(max_workers=1 if retry_failed else 2) as pool:
        futures = [pool.submit(execute_one, alias, case) for case in cases for alias in cfg["models"]]
        for future in as_completed(futures):
            results.append(future.result())
            write_json(
                directory / "status.json",
                {
                    "status": "RUNNING",
                    "completed": len(results),
                    "total": len(futures),
                    "results": results,
                    "usage": shared_budget.used,
                },
            )
    result = {
        "status": "COMPLETED_AWAITING_SOURCE_AUDIT",
        "key": key,
        "directory": str(directory),
        "results": results,
        "calls_this_invocation": shared_budget.used["calls"] - before,
        "usage": shared_budget.used,
        "production_authorized": False,
    }
    write_json(directory / "status.json", result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--split", choices=["development", "evaluation"])
    parser.add_argument("--case", action="append")
    parser.add_argument("--model", action="append", help="Select a configured, user-authorized extractor alias")
    parser.add_argument(
        "--critic-model", help="Use a configured alias for independent reading, critique and verification"
    )
    parser.add_argument("--context-repair-id", help="One named repair of a previously stopped, reconciled context case")
    parser.add_argument(
        "--retry-failed",
        action="store_true",
        help="Retry settled failed calls once; preserve successful caches and unknown reservations",
    )
    parser.add_argument(
        "--request-timeout-seconds",
        type=int,
        help="Recorded transport deadline override, up to 180 seconds; preserves completed call caches",
    )
    args = parser.parse_args()
    root = Path.cwd()
    with (root / "data/work/p4.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = run_trial(
            root,
            args.live,
            args.split,
            args.case,
            args.model,
            args.critic_model,
            args.context_repair_id,
            args.retry_failed,
            args.request_timeout_seconds,
        )
    print(canonical_json({k: result[k] for k in ("status", "key") if k in result}), flush=True)


if __name__ == "__main__":
    main()
