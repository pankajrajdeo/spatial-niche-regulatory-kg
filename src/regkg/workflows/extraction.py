"""Deterministic P4 driver: freeze sources, extract, verify, validate, persist and replay."""

import argparse
import fcntl
import json
import os
from collections import Counter
from pathlib import Path

import pandas as pd

from regkg.config import load_environment, load_model_settings, parse_model_selector
from regkg.extraction.assembly import assemble
from regkg.extraction.config import load_config
from regkg.extraction.context_repair import recover_context
from regkg.extraction.grounded import extract_grounded, load_scientific_schema
from regkg.extraction.runtime import Runtime, build_chat_model
from regkg.extraction.schemas import Capability
from regkg.extraction.sources import (
    MAX_EVIDENCE_CHARS,
    MAX_EVIDENCE_PARTS,
    SourceRegistry,
    bundle_parts,
    pubtator_context,
)
from regkg.extraction.validation import EntityResolver
from regkg.provenance import canonical_json, code_fingerprint, read_json, sha256_file, sha256_text, write_json
from regkg.workflows.corpus_ready import serialize_evidence

LINEAGES = ("AT1", "Alveolar_Macrophages", "KRT5neg_KRT17pos", "Activated_Fibrotic_FBs")


def choose_bundles(bundles, limit, max_papers):
    selected, papers = [], set()

    def score(b):
        text = " ".join(p["text"] for p in b["parts"]).lower()
        return sum(text.count(t) for t in ("regulat", "knockdown", "knockout", "silenc", "bind", "transcription"))

    ordered = sorted(
        [b for b in bundles if b["readiness_state"].startswith("READY")], key=lambda b: (-score(b), b["payload_id"])
    )
    while len(selected) < limit:
        progressed = False
        for lineage in LINEAGES:
            candidates = [
                b
                for b in ordered
                if b not in selected
                and lineage in b.get("lineages", [])
                and (b["publication_id"] in papers or len(papers) < max_papers)
            ]
            # Prefer distinct sources for validation without giving one lineage priority.
            candidates.sort(key=lambda b: b["publication_id"] in papers)
            if candidates:
                chosen = candidates[0]
                selected.append(chosen)
                papers.add(chosen["publication_id"])
                progressed = True
            if len(selected) == limit:
                break
        if not progressed:
            break
    return selected


def _jsonl(path, rows):
    path.write_text("".join(canonical_json(r) + "\n" for r in rows))


def persist(out, findings, outcomes, manifest):
    out.mkdir(parents=True, exist_ok=True)
    grouped = {}
    for finding in findings:
        grouped.setdefault(finding["finding_id"], []).append(finding)
    severity = {"AUTO_ACCEPTED": 0, "UNCERTAIN": 1, "REJECTED": 2}
    findings = [
        {
            **max(group, key=lambda f: severity[f["status"]]),
            "bundle_ids": sorted({f["bundle_id"] for f in group}),
            "occurrence_reviews": [
                {"bundle_id": f["bundle_id"], "status": f["status"], "verification": f["verification"]} for f in group
            ],
        }
        for group in grouped.values()
    ]
    accepted = [f for f in findings if f["status"] == "AUTO_ACCEPTED"]
    # Intermediate propositions include phenotype/chemical/group findings. They are not
    # automatically RegulatoryClaim nodes. Legacy records need new-schema classification.
    for finding in accepted:
        projection = finding.get("kg_projection", {})
        finding["proposition_id"] = finding["claim_id"]
        finding["claim_id"] = projection.get("claim_id") if projection.get("core_claim_eligible") else None
    # Nested source contracts stay losslessly serialized; table columns provide stable join keys.
    columns = ["finding_id", "claim_id", "publication_id", "pmid", "bundle_id", "status", "record_json"]
    pd.DataFrame(
        [{**{k: f[k] for k in columns[:-1]}, "record_json": canonical_json(f)} for f in accepted], columns=columns
    ).astype("string").to_parquet(out / "accepted_findings.parquet", index=False)
    claims = {f["claim_id"]: f["kg_projection"]["claim"] for f in accepted if f["claim_id"] is not None}
    pd.DataFrame(
        [{"claim_id": k, "proposition_json": canonical_json(v)} for k, v in claims.items()],
        columns=["claim_id", "proposition_json"],
    ).astype("string").to_parquet(out / "claims.parquet", index=False)
    pd.DataFrame(
        [
            {
                "assertion_id": f["finding_id"],
                "claim_id": f["claim_id"],
                "publication_id": f["publication_id"],
                "finding_id": f["finding_id"],
                "source_spans_json": canonical_json(f["spans"]),
                "independent_study_id": None,
                "kg_projection_json": canonical_json(
                    f.get(
                        "kg_projection",
                        {"core_claim_eligible": False, "reasons": ["legacy_record_requires_schema_classification"]},
                    )
                ),
            }
            for f in accepted
        ],
        columns=[
            "assertion_id",
            "claim_id",
            "publication_id",
            "finding_id",
            "source_spans_json",
            "independent_study_id",
            "kg_projection_json",
        ],
    ).astype("string").to_parquet(out / "evidence_assertions.parquet", index=False)
    _jsonl(out / "uncertain.jsonl", [f for f in findings if f["status"] == "UNCERTAIN"])
    _jsonl(out / "rejected.jsonl", [f for f in findings if f["status"] == "REJECTED"])
    _jsonl(out / "bundle_outcomes.jsonl", outcomes)
    failed = any(
        o["status"] not in {"FINDINGS", "NO_RELATION", "INSUFFICIENT_CONTEXT"}
        or o.get("verification_status", "SUCCEEDED") != "SUCCEEDED"
        for o in outcomes
    )
    failed = failed or manifest.get("assembly_result") in {"FAILED_OR_LIMIT_REACHED", "INTERRUPTED_REVIEW_REQUIRED"}
    summary = {
        "status": "PARTIAL_WORKFLOW" if failed else "VALIDATION_BATCH",
        "bundles": len(outcomes),
        "dispositions": dict(Counter(f["status"] for f in findings)),
        "core_regulatory_claims": len(claims),
        "accepted_file_only_findings": sum(f["claim_id"] is None for f in accepted),
        "bundle_states": dict(Counter(o["status"] for o in outcomes)),
        "scope": manifest.get(
            "execution_scope", "bounded implementation validation; P3 expansion/P4 full corpus/P5/P6 remain pending"
        ),
    }
    write_json(out / "summary.json", summary)
    write_json(
        out / "manifest.json",
        {
            **manifest,
            "outputs": {
                p.name: sha256_file(p) for p in sorted(out.iterdir()) if p.is_file() and p.name != "manifest.json"
            },
        },
    )
    return summary


def verify_evidence(root: Path, run_key: str) -> dict:
    out = root / "data/processed" / run_key
    manifest = read_json(out / "manifest.json")
    for name, digest in manifest["outputs"].items():
        if sha256_file(out / name) != digest:
            raise ValueError(f"Evidence artifact changed: {name}")
    identity = manifest["identity"]
    registry = SourceRegistry(root, identity["selection"], root / "data/work/corpus-c700d6e584b7bccf")
    if registry.manifest_hash != identity["selection_manifest"]:
        raise ValueError("Parent source manifest changed")
    for doc_id, digest in identity["source_files"].items():
        registry.document(doc_id)
        if registry.file_hashes[doc_id] != digest:
            raise ValueError("Pinned canonical document changed")
    annotation_assets = dict(identity.get("pubtator_assets", {}))
    annotation_assets.update(manifest.get("assembled_pubtator_context", {}).get("assets", {}))
    annotation_assets.update(manifest.get("critic_context_pubtator_assets", {}))
    for name, digest in annotation_assets.items():
        if sha256_file(root / name) != digest:
            raise ValueError("Pinned PubTator annotations changed")
    accepted = pd.read_parquet(out / "accepted_findings.parquet")
    claims = pd.read_parquet(out / "claims.parquet")
    evidence = pd.read_parquet(out / "evidence_assertions.parquet")
    if (
        accepted.finding_id.duplicated().any()
        or claims.claim_id.duplicated().any()
        or evidence.assertion_id.duplicated().any()
    ):
        raise ValueError("Duplicate evidence identity")
    if set(evidence.finding_id) != set(accepted.finding_id) or not set(evidence.claim_id.dropna()) <= set(
        claims.claim_id
    ):
        raise ValueError("Broken claim/evidence joins")
    spans_checked = 0
    for row in accepted.itertuples():
        finding = json.loads(row.record_json)
        for span in finding["spans"]:
            doc = registry.document(span["document_id"])
            if doc.canonical_sha256 != span["document_sha256"] or doc.source_asset_sha256 != span["asset_sha256"]:
                raise ValueError("Finding source identity changed")
            if doc.canonical_text[span["start"] : span["end"]] != span["quote"]:
                raise ValueError("Finding quote/offset mismatch")
            spans_checked += 1
    return {
        "status": "VERIFIED",
        "run": run_key,
        "accepted_findings": len(accepted),
        "claims": len(claims),
        "evidence_assertions": len(evidence),
        "spans_checked": spans_checked,
    }


def run(
    root,
    selection,
    limit=8,
    execute=False,
    assembly=False,
    retry_failed=False,
    input_mode="real",
    batch_index=None,
    assembly_repair=None,
    execution_allowance=None,
):
    if assembly_repair and not assembly:
        raise ValueError("Assembly repair requires --assembly")
    if input_mode not in {"real", "fixture"}:
        raise ValueError("Unknown input mode")
    settings = load_config(root / "configs/extraction.yaml")
    cfg = settings["runtime"]
    policy = load_scientific_schema(root / "configs/extraction_schema.yaml")
    if not 1 <= limit <= cfg["max_bundles"] <= 20 or not 1 <= cfg["max_papers"] <= 10:
        raise ValueError("Invalid validation batch bounds")
    if batch_index is not None and (batch_index < 1 or assembly):
        raise ValueError("A numbered ready batch must be positive; validate assembly separately")
    work = root / "data/work/corpus-c700d6e584b7bccf"
    registry = SourceRegistry(root, selection, work)
    candidates = [
        b
        for b in registry.bundles.values()
        if b["readiness_state"] == "NEEDS_CONTEXT"
        and b["document_parse"]["state"] == "PARSED"
        and b["readiness_reasons"]
        and all(
            reason.startswith("context_not_included:referenced_figure_caption:") for reason in b["readiness_reasons"]
        )
    ]
    candidate, assembly_preflight = None, []
    if assembly:
        for option in sorted(candidates, key=lambda b: (b["serialized_chars"], b["payload_id"])):
            needed = registry.validate_bundle(option, require_ready=False)
            seen = {p["passage_id"] for p in needed}
            for reason in option["readiness_reasons"]:
                passage_id = reason.removeprefix("context_not_included:referenced_figure_caption:")
                if passage_id not in seen:
                    needed.append(registry.part(option["document_id"], passage_id))
                    seen.add(passage_id)
            chars = len(serialize_evidence(bundle_parts(needed)))
            fits = len(needed) <= MAX_EVIDENCE_PARTS and chars <= MAX_EVIDENCE_CHARS
            assembly_preflight.append(
                {
                    "bundle_id": option["payload_id"],
                    "required_parts": len(needed),
                    "serialized_chars": chars,
                    "status": "FEASIBLE" if fits else "CONTEXT_TOO_LARGE",
                }
            )
            if fits:
                candidate = option
                break
    selected = choose_bundles(
        list(registry.bundles.values()), limit - bool(candidate), cfg["max_papers"] - bool(candidate)
    )
    batch_sha = None
    if batch_index is not None:
        batch_path = registry.artifact / "ready_batches" / f"batch-{batch_index:03}.json"
        batch = read_json(batch_path)
        ids = batch["payload_ids"]
        if len(ids) != len(set(ids)) or not 1 <= len(ids) <= cfg["max_bundles"]:
            raise ValueError("Invalid ready-batch membership")
        selected = [registry.bundles[pid] for pid in ids]
        if len({b["publication_id"] for b in selected}) > cfg["max_papers"]:
            raise ValueError("Ready batch exceeds paper limit")
        batch_sha = sha256_file(batch_path)
    sources = {b["payload_id"]: registry.validate_bundle(b) for b in selected}
    annotations = {key: pubtator_context(registry, parts) for key, parts in sources.items()}
    model_settings = load_model_settings(root)
    env = load_environment(root / ".env")
    extractor, verifier = model_settings.extractor.spec, model_settings.verifier.spec
    if not extractor or not verifier:
        raise ValueError("Extractor/verifier model is not configured")
    assembler = parse_model_selector(env["ASSEMBLER_MODEL"], "chat") if env.get("ASSEMBLER_MODEL") else extractor
    mapping_path = root / "data/processed/mcandidates-c278c6625ff7c537/gene_mappings.parquet"
    identity = {
        "input_mode": input_mode,
        "selection": selection,
        "selection_manifest": registry.manifest_hash,
        "source_files": dict(registry.file_hashes),
        "bundles": [b["payload_id"] for b in selected],
        "models": {"extractor": extractor.selector, "verifier": verifier.selector, "assembler": assembler.selector},
        "endpoint_hash": sha256_text(env.get("LITELLM_BASE_URL", "")),
        "settings": settings,
        "scientific_schema": policy.model_dump(),
        "mapping_sha256": sha256_file(mapping_path),
        "external_identity_sha256": sha256_file(root / "data/external/p4-gene-identities.json")
        if (root / "data/external/p4-gene-identities.json").exists()
        else None,
        "pubtator_context_sha256": sha256_text(canonical_json(annotations)),
        "pubtator_assets": {k: v for a in annotations.values() for k, v in a["assets"].items()},
        "ready_batch_sha256": batch_sha,
        "assembly_requested": assembly,
        "assembly_repair": assembly_repair,
        "assembly_preflight": assembly_preflight,
        "assembly_parent_bundle": candidate["payload_id"] if candidate else None,
        "code": code_fingerprint(root / "src/regkg", ["extraction", "workflows/extraction.py"]),
    }
    key = "extraction-" + sha256_text(canonical_json(identity))[:16]
    directory, out = root / "data/work" / key, root / "data/processed" / key
    manifest = {
        "identity": identity,
        "key": key,
        "input_mode": input_mode,
        "stage": "P4",
        "pending_papers": read_json(registry.artifact / "extraction_readiness.json")["manual_article_requests"],
        "full_corpus_accepted": False,
        "source_subset_disposition": "User 2026-09-23: validate available sources; retain missing evidence pending",
        "lineages": {lineage: sum(lineage in b.get("lineages", []) for b in selected) for lineage in LINEAGES},
        "scheduled_extractor_calls": 2 * (len(selected) + bool(candidate)),
        "missing_mention_repair_calls_up_to": len(selected) + bool(candidate),
        "scheduled_verifier_calls_up_to": 6 * (len(selected) + bool(candidate)),
        "semantic_repair_calls_up_to": len(selected) + bool(candidate),
        "preflight_calls_up_to": len({extractor.selector, verifier.selector}),
        "assembly_model_attempts_up_to": settings["assembly"]["max_model_calls"] if assembly else 0,
        "critic_context_assembly_calls_up_to": settings["assembly"]["max_model_calls"]
        * (len(selected) + bool(candidate)),
        "proxy_dollar_price": "unknown",
        "token_method": "conservative UTF-8 byte bound, not exact GLM tokenizer",
    }
    directory.mkdir(parents=True, exist_ok=True)
    write_json(directory / "input_manifest.json", manifest)
    if not execute:
        return {
            "status": "PREPARED_NO_CALLS",
            "key": key,
            "manifest": str(directory / "input_manifest.json"),
            "lineages": manifest["lineages"],
            "bundles": len(selected),
        }
    # Do not enable remote tracing implicitly through inherited SDK environment settings.
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    os.environ["LANGSMITH_TRACING"] = "false"
    runtime_identity = {
        "models": identity["models"],
        "endpoint_hash": identity["endpoint_hash"],
        "settings": settings,
        "mention_reasoning_effort": "low",
    }
    cache_key = sha256_text(canonical_json(runtime_identity))[:16]
    runtime_settings = dict(cfg)
    if execution_allowance is not None:
        allowed = {"max_calls", "max_input_tokens_total", "max_output_tokens_total"}
        if set(execution_allowance) != allowed or any(
            type(v) is not int or v <= 0 for v in execution_allowance.values()
        ):
            raise ValueError("Invalid corpus execution allowance")
        runtime_settings.update(execution_allowance)
        manifest["execution_scope"] = "user-authorized complete ready corpus"
        manifest["execution_allowance"] = execution_allowance
    runtime = Runtime(
        root / "data/work/p4-validation" / cache_key,
        runtime_settings,
        runtime_identity,
        retry_failed,
        root / "data/work/p4-validation/budget.json",
    )
    manifest["call_cache"] = str(runtime.directory.relative_to(root))
    calls_before = runtime.budget.used["calls"]
    while (out / "manifest.json").exists():
        existing = read_json(out / "manifest.json")
        for name, sha in existing["outputs"].items():
            if sha256_file(out / name) != sha:
                raise ValueError("Extraction output changed")
        summary = read_json(out / "summary.json")
        if summary["status"] != "PARTIAL_WORKFLOW" or not retry_failed:
            return {
                "status": "REUSED_VERIFIED" if summary["status"] != "PARTIAL_WORKFLOW" else "PARTIAL_WORKFLOW",
                "key": key,
                "calls_this_invocation": 0,
                "summary": summary,
            }
        identity = {**identity, "repair_parent_manifest": sha256_file(out / "manifest.json")}
        key = "extraction-" + sha256_text(canonical_json(identity))[:16]
        directory, out = root / "data/work" / key, root / "data/processed" / key
        directory.mkdir(parents=True, exist_ok=True)
        manifest = {**manifest, "identity": identity, "key": key}
        write_json(directory / "input_manifest.json", manifest)
    models = {
        "extractor": build_chat_model(extractor, env, cfg),
        "verifier": build_chat_model(verifier, env, cfg),
        "mentions": build_chat_model(extractor, env, {**cfg, "reasoning_effort": "low"}),
    }
    for role in ("extractor", "verifier"):
        smoke = runtime.structured(
            models[role],
            Capability,
            "Copy the supplied text exactly into echoed_text.",
            {"text": "source-bound capability check"},
            "capability:" + identity["models"][role],
        )
        if smoke["status"] != "SUCCEEDED" or smoke["parsed"]["echoed_text"] != "source-bound capability check":
            write_json(directory / "preflight_failure.json", smoke)
            return {"status": "PREFLIGHT_FAILED", "key": key, "calls": runtime.budget.used["calls"]}
    mapping = pd.read_parquet(mapping_path)
    catalog_path = root / "data/external/p4-gene-identities.json"
    catalog = read_json(catalog_path) if catalog_path.exists() else {}
    resolver = EntityResolver(mapping.to_dict("records"), str(mapping.mapping_version.iloc[0]), catalog)
    findings, outcomes = [], []
    if candidate:
        assembly_cfg = {
            **cfg,
            "reasoning_effort": settings["assembly"]["reasoning_effort"],
            "max_output_tokens": settings["assembly"]["max_output_tokens"],
            "timeout_seconds": settings["assembly"]["model_timeout_seconds"],
        }
        result = assemble(
            registry,
            candidate,
            "Resolve the recorded context gap using original local source parts: "
            + str(candidate["readiness_reasons"]),
            build_chat_model(assembler, env, assembly_cfg),
            runtime,
            settings["assembly"],
            repair_id=assembly_repair,
        )
        write_json(directory / "assembly_validation.json", result)
        manifest["assembly_result"] = result["status"]
        if result.get("bundle"):
            child = result["bundle"]
            sources[child["payload_id"]] = registry.validate_bundle(child)
            annotations[child["payload_id"]] = pubtator_context(registry, sources[child["payload_id"]])
            manifest["assembled_pubtator_context"] = annotations[child["payload_id"]]
            selected.append(child)
            manifest["assembled_child_bundles"] = [child]
    for b in selected:
        # Direct-ready cases never invoke the context agent.
        bypass = assemble(registry, b, "", None, runtime, settings["assembly"])
        assert bypass["status"] == "BYPASSED_READY"
        parts = sources[b["payload_id"]]

        def resolve_context(parent, requests):
            return recover_context(
                registry,
                parent,
                requests,
                build_chat_model(
                    assembler,
                    env,
                    {
                        **cfg,
                        "reasoning_effort": settings["assembly"]["reasoning_effort"],
                        "max_output_tokens": settings["assembly"]["max_output_tokens"],
                        "timeout_seconds": settings["assembly"]["model_timeout_seconds"],
                    },
                ),
                runtime,
                settings["assembly"],
            )

        records, outcome = extract_grounded(
            parts,
            b,
            annotations[b["payload_id"]],
            policy,
            runtime,
            models,
            resolver,
            context_recovery=resolve_context,
        )
        registry.validate_bundle(b)
        findings.extend(records)
        outcomes.append(outcome)
        write_json(
            directory / "progress.json",
            {"completed": len(outcomes), "scheduled": len(selected), "last": outcome, "usage": runtime.budget.used},
        )
        print(f"P4 {len(outcomes)}/{len(selected)} {b['pmid']} {outcome['status']}", flush=True)
    manifest["usage"] = runtime.budget.used
    manifest["critic_context_pubtator_assets"] = {
        k: v
        for o in outcomes
        for k, v in o.get("context_recovery", {}).get("annotations", {}).get("assets", {}).items()
    }
    manifest["calls_this_invocation"] = runtime.budget.used["calls"] - calls_before
    summary = persist(out, findings, outcomes, manifest)
    return {"key": key, "output": str(out), "calls_this_invocation": manifest["calls_this_invocation"], **summary}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", default="p3selection-89efefdd214ee16e")
    choice = parser.add_mutually_exclusive_group()
    choice.add_argument("--limit", type=int, default=8)
    choice.add_argument("--batch", type=int, default=None, help="consume one complete numbered ready batch")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--assembly", action="store_true")
    parser.add_argument("--assembly-repair", default=None, help="named repair of a stopped, reconciled assembly case")
    parser.add_argument(
        "--retry-failed", action="store_true", help="retry known failures within the same remaining budget"
    )
    args = parser.parse_args()
    root = Path.cwd()
    lock_path = root / "data/work/p4.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = run(
            root,
            args.selection,
            args.limit,
            args.execute,
            args.assembly,
            args.retry_failed,
            batch_index=args.batch,
            assembly_repair=args.assembly_repair,
        )
        print(json.dumps(result, indent=2))
        if result["status"] in {"PREFLIGHT_FAILED", "PARTIAL_WORKFLOW"}:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
