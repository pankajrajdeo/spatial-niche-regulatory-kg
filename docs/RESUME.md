Current checkpoint: [CONTINUE_HERE.md](CONTINUE_HERE.md). Extraction is paused for architecture review. The user has placed OpenWiki, GraphRAG and the LangChain documentation mirror under [reference/GitHub](../reference/GitHub/) for future implementation reference. Earlier execution statements below are historical; consult the current checkpoint before resuming work.

## Historical frame/patch repair — 2026-09-23

The user authorized all required P4 design repairs. `grounded-observations-6` implements pre-extraction source-grounded experiment frames/context recovery, source metadata preservation, bounded observation patches with unchanged-field enforcement, and finding-level disposition separate from bundle coverage. P4 context bounds are eight parts/16,000 serialized characters; frozen P3/source artifacts remain unchanged. Final KG vocabulary and models remain unchanged.

Bounded live validation is running as `trial-4ade5b51625020db` on joint_gene_loss, organoid_endpoints and expression_table, using GLM extraction/Kimi verification with the recorded 180-second deadline. Inspect `data/work/p4-accuracy/frame-patch.log`, the trial status and `frame-patch-state.json`; do not launch duplicates. 94 focused tests and 72 corpus/parser tests passed. The completed intermediate trial `trial-b98e14e6a0495cef` demonstrated a one-field table repair but exposed oversized joint-loss verification and incorrect frame selection. The current run uses two-finding review batches, matching-frame measured-variable enforcement and one bounded frame-amendment pass for missed/context-defective findings. The initial frame diagnostic `trial-9291684d0a824962` was stopped after duplicate field names were detected; fixed named frame slots supersede the list contract, with completed caches and unknown dispatch reservations preserved. No full-corpus restart or accuracy claim yet. Earlier pause text below is historical and superseded by this explicit user authorization.

Current checkpoint: [CONTINUE_HERE.md](CONTINUE_HERE.md). **Inference is paused at the user's request for a complete context reread.** All three reference synthesis/schema documents have now been read completely (5,900 lines including appended updates); see `reports/continuation/p4/context-review.json`. The current code is `grounded-observations-5` / `spatial-nichelinker-kg-2`, with 80 focused tests passing. The initial corrected trial completed, but its retry was interrupted for this pause; preserve completed calls and unknown usage. The later verifier-input clarification is not yet live-validated. Read the [P4 handoff](handoffs/P4.md) before continuing. No inference job remains scheduled.

Scope correction from the reread: independent annotation is necessary for a measured accuracy claim, not a mandatory new project before KG completion. The design permits conservative automatic acceptance with small regression/source checks and explicit uncertainty. Later user-authorized bounded critique/repair and candidate annotation export still apply.

Both named LiteLLM models and candidate annotation export are authorized for bounded validation. Full-corpus extraction remains stopped. Preserve existing diagnostic outputs, source/model caches, cumulative budget and `.env`; no snapshot restore or source reprocessing is needed on this laptop. The shared final KG vocabulary is in [KG_SCHEMA_ALIGNMENT.md](KG_SCHEMA_ALIGNMENT.md); annotation limits are in [P4_ANNOTATION_DESIGN.md](P4_ANNOTATION_DESIGN.md).

# Resume on another computer

Full-corpus P4 status: **STOPPED_FOR_ACCURACY_REPAIR**. The old production outputs/caches were deleted at user request; newer bounded diagnostics are retained and must not be deleted or confused with those old artifacts. Read the current checkpoint before any historical execution instructions. Do not restore deleted production artifacts or restart the corpus from a historical command. Source preparation remains intact.

Start with [CONTINUE_HERE.md](CONTINUE_HERE.md). The user authorized this GitHub migration and continuation on the destination LiteLLM quota. plan.md is now tracked intentionally; earlier instructions to transfer it separately are superseded. reference/, data/ and reports/ remain ignored as loose files and are transferred in the private LFS snapshot.

For the active P4 implementation, include `--extra chat --extra agent` in the locked `uv sync` command below. The existing laptop already has these extras; do not recreate its environment or restore the snapshot again. See [the P4 handoff](handoffs/P4.md) for the current live-validation state and exact validation command.

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
