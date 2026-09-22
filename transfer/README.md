# Private continuation snapshot

This snapshot was requested for migration to the user's second laptop on 2026-09-22. It contains 31,110 files from data/, reports/ and reference/, totaling about 3.2 GB compressed in 12 Git LFS parts. The authoritative part/file hashes and sizes are in snapshot.json. No .env or Python environment is included. Keep this data-bearing repository private.

Read docs/CONTINUE_HERE.md and docs/RESUME.md. Run `git lfs pull`, then `.venv/bin/python scripts/restore_snapshot.py`. Loose data/report/reference files remain ignored to avoid accidental duplicate storage. Future snapshots should be deliberate checkpoints, not part of every code commit.

Source provenance, historical artifacts, and recorded source access/reuse metadata are preserved. Credentials must be configured privately on the destination. This is a resume snapshot, not a public dataset release.
