# Resume on another computer

Start with [CONTINUE_HERE.md](CONTINUE_HERE.md). The user authorized this GitHub migration and continuation on the destination LiteLLM quota. plan.md is now tracked intentionally; earlier instructions to transfer it separately are superseded. reference/, data/ and reports/ remain ignored as loose files and are transferred in the private LFS snapshot.

## Restore

On the destination, preserve any existing .env and uncommitted changes. Pull the latest main normally (do not reset local work), or clone the private repository. Install Git LFS (`brew install git-lfs` on macOS) and run:

```bash
git lfs install --local
git lfs pull
uv venv .venv --python 3.12 --seed
uv sync --locked --inexact --extra test --extra analysis --extra embeddings-ollama --extra pdf
.venv/bin/python scripts/restore_snapshot.py
.venv/bin/python -m pip check
.venv/bin/python -m regkg --help
```

Restore verifies the chunk and individual-file SHA-256 hashes and refuses to overwrite divergent existing files. Preserve/move only those conflicting local artifacts if you choose to restore this snapshot; never delete the destination's changes blindly. `--verify-only` checks an already restored tree. Allow roughly 20 GB free for snapshot restoration and environment, plus room for future outputs. Do not copy .venv between machines.

The snapshot contains the complete captured data/, reports/ and reference/ tree (excluding OS detritus), including paper assets, source/parse/vector caches, historical artifacts and partial screening results. It excludes .env, credentials and external home-directory model caches. Supplied files/ and code/config/docs are normal Git files. CLAUDE.md remains a relative symlink to AGENTS.md.

Set destination LiteLLM credentials privately using .env.example as a reference. Preserve existing credentials and use the actual proxy model alias. Do not run OpenRouter screening merely because its example is the default. The cache provider switch and concurrency/budget caveats are in CONTINUE_HERE.md.

Use the root .venv and pinned uv.lock. Models served by Ollama or Docling's external model cache may need separate installation only if a remaining operation requires them. Existing parse/vector caches should be used before downloading/recomputing. Most stored source paths are repository-relative; if a stale absolute path is encountered, resolve it against this root through the loader, preserving immutable artifact contents and original provenance.

Verify the latest transferred corpus manifest output checksums and run tests before substantive changes. Historical source snapshots are not lead acceptance, and a passing test suite alone is not completed extraction. The user stopped local screening; continuing it on LiteLLM is the active task. Full KG extraction has not yet run.
