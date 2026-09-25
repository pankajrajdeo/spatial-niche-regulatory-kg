"""Execute every frozen ready batch, with durable progress and existing call-cache reuse."""

import fcntl
import os
import time
from pathlib import Path

from regkg.extraction.sources import SourceRegistry
from regkg.provenance import read_json, write_json
from regkg.workflows.extraction import run, verify_evidence

SELECTION = "p3selection-89efefdd214ee16e"
ALLOWANCE = {"max_calls": 5000, "max_input_tokens_total": 120_000_000, "max_output_tokens_total": 30_000_000}


def main():
    root = Path.cwd()
    directory = root / "data/work/p4-corpus"
    directory.mkdir(parents=True, exist_ok=True)
    status_path = directory / "status.json"
    if status_path.exists() and read_json(status_path).get("restart_authorized") is False:
        raise RuntimeError("Full corpus remains stopped for accuracy; use bounded validation only")
    with (root / "data/work/p4.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        registry = SourceRegistry(root, SELECTION, root / "data/work/corpus-c700d6e584b7bccf")
        paths = sorted((registry.artifact / "ready_batches").glob("batch-*.json"))
        ids = [bid for path in paths for bid in read_json(path)["payload_ids"]]
        ready = {bid for bid, b in registry.bundles.items() if b["readiness_state"].startswith("READY")}
        if len(ids) != len(set(ids)) or set(ids) != ready:
            raise ValueError("Ready manifests do not cover the corpus exactly once")
        state = {
            "status": "RUNNING",
            "pid": os.getpid(),
            "started_unix": time.time(),
            "selection": SELECTION,
            "selection_manifest_sha256": registry.manifest_hash,
            "bundles_total": len(ids),
            "papers_total": len({registry.bundles[i]["publication_id"] for i in ids}),
            "batches_total": len(paths),
            "execution_allowance": ALLOWANCE,
            "pubtator": "cached source-aligned annotations in extractor and verifier inputs",
            "completed_batches": [],
            "failed_batches": [],
        }
        write_json(directory / "status.json", state)
        print(f"CORPUS START: {state['papers_total']} papers, {len(ids)} bundles, {len(paths)} batches", flush=True)
        for path in paths:
            index = read_json(path)["batch_index"]
            state.update(active_batch=index, updated_unix=time.time())
            write_json(directory / "status.json", state)
            print(f"CORPUS BATCH {index}/{len(paths)} START", flush=True)
            try:
                result = run(
                    root, SELECTION, execute=True, batch_index=index, retry_failed=True, execution_allowance=ALLOWANCE
                )
                if result["status"] == "PREFLIGHT_FAILED":
                    state.update(status="BLOCKED_PREFLIGHT", last_result=result)
                    write_json(directory / "status.json", state)
                    return
                verify_evidence(root, result["key"])
                record = {
                    "batch": index,
                    "run": result["key"],
                    "status": result["status"],
                    "bundles": len(read_json(path)["payload_ids"]),
                }
                state["completed_batches"].append(record)
                if result["status"] == "PARTIAL_WORKFLOW":
                    state["failed_batches"].append(record)
            except Exception as exc:
                state["failed_batches"].append({"batch": index, "error_type": type(exc).__name__})
                print(f"CORPUS BATCH {index} ERROR {type(exc).__name__}", flush=True)
            state["updated_unix"] = time.time()
            write_json(directory / "status.json", state)
        state.update(
            status="COMPLETED_WITH_FAILURES" if state["failed_batches"] else "COMPLETED",
            active_batch=None,
            updated_unix=time.time(),
        )
        write_json(directory / "status.json", state)
        print(state["status"], flush=True)


if __name__ == "__main__":
    main()
