"""Export a frozen trial's annotations for source review without any inference or training."""

import argparse
import os
from pathlib import Path

from regkg.extraction.annotations import annotation_candidates
from regkg.extraction.sources import SourceRegistry, pubtator_context
from regkg.provenance import canonical_json, read_json, sha256_file, write_json


def export_candidates(root, trial):
    manifest = read_json(trial / "manifest.json")
    cfg = manifest["identity"]["config"]
    registry = SourceRegistry(root, cfg["selection"], root / "data/work/corpus-c700d6e584b7bccf")
    if registry.manifest_hash != manifest["identity"]["source_manifest"]:
        raise ValueError("Frozen selection manifest changed")
    state = read_json(trial / "status.json")
    entries = {(r["case"], r["model"]): r for r in state.get("results", [])}
    rows, inputs = [], {}
    for case in manifest["cases"]:
        results = []
        for model in cfg["models"]:
            entry = entries.get((case["id"], model))
            if entry is None:
                continue
            path = root / entry["path"]
            if sha256_file(path) != entry["sha256"]:
                raise ValueError("Trial output checksum changed")
            inputs[entry["path"]] = entry["sha256"]
            results.append(read_json(path))
        if not results:
            continue
        parts = registry.validate_bundle(registry.bundles[case["bundle_id"]])
        by_id = {p["part_id"]: p for p in parts}
        for result in results:
            for key in ("pre_extraction_context_recovery", "context_recovery"):
                child = (result["outcome"].get(key) or {}).get("bundle")
                if child:
                    by_id.update({p["part_id"]: p for p in registry.validate_bundle(child)})
        parts = list(by_id.values())
        if any(registry.file_hashes[k] != manifest["identity"]["source_files"][k] for k in registry.file_hashes):
            raise ValueError("Frozen trial source changed")
        item = annotation_candidates(
            parts,
            pubtator_context(registry, parts),
            results,
            manifest["key"],
            manifest["identity"]["schema"]["version"],
        )
        rows.append(item.model_dump())
    output = trial / "annotation_candidates.jsonl"
    temporary = output.with_suffix(".tmp")
    temporary.write_text("".join(canonical_json(row) + "\n" for row in rows), encoding="utf-8")
    os.replace(temporary, output)
    receipt = {
        "status": "CANDIDATES_ONLY",
        "trial_status": state["status"],
        "bundles": len(rows),
        "model_outputs": len(inputs),
        "expected_model_outputs": len(manifest["cases"]) * len(cfg["models"]),
        "training_eligible": 0,
        "gold_labels": 0,
        "inputs": inputs,
        "trial_manifest_sha256": sha256_file(trial / "manifest.json"),
        "output": str(output.relative_to(root)),
        "output_sha256": sha256_file(output),
        "output_bytes": output.stat().st_size,
        "notes": [
            "All dispositions retained; agreement is not truth.",
            "Diagnostic bundles are reserved; do not use as encoder training examples.",
            "Future training requires source adjudication and paper/study-group separation from evaluation.",
            "No absent annotation or unextracted pair has been converted into a negative label.",
        ],
    }
    write_json(trial / "annotation_candidates_receipt.json", receipt)
    return receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trial", required=True, type=Path)
    args = parser.parse_args()
    print(canonical_json(export_candidates(Path.cwd(), args.trial.resolve())))


if __name__ == "__main__":
    main()
