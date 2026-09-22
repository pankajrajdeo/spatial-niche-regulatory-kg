---
title: "langsmith/smith-api/threads"
description: "Index of 13 pages and 0 subdirectories under langsmith/smith-api/threads."
category: "index"
tags: [index, langsmith, smith-api, threads]
---

# langsmith/smith-api/threads

13 pages here.

## Files

- [Get a public shared thread's manifest](get-a-public-shared-threads-manifest.md) - Returns the thread and project a share token is scoped to, plus the project's conversations config.
- [Get one run in a public shared thread](get-one-run-in-a-public-shared-thread.md) - Returns a single run, including full inputs and outputs, provided its trace root belongs to the shared thread.
- [Get stats for a public shared thread](get-stats-for-a-public-shared-thread.md) - Returns aggregate stats for the thread identified by the share token.
- [List runs of one trace in a public shared thread](list-runs-of-one-trace-in-a-public-shared-thread.md) - Returns every run in the given trace, provided that trace's root belongs to the shared thread.
- [List traces in a public shared thread](list-traces-in-a-public-shared-thread.md) - Returns a page of root traces belonging to the thread identified by the share token. The share token supplies the tenant, project, and thread scope.
- [Query single thread stats](query-single-thread-stats.md) - Compute aggregate stats for a single thread (turn count, latency percentiles, token/cost sums, and detail breakdowns) within a project.
- [Query thread stats](query-thread-stats.md) - GET with body payload — no resources created. Returns aggregate statistics for threads in a tracing project. The response includes the thread counts, run counts, latency percentiles, rates, token...
- [Query thread traces](query-thread-traces.md) - Retrieve all traces belonging to a specific thread within a project.
- [Query threads](query-threads.md) - Query threads within a project (session), with cursor-based pagination. Returns threads matching the given time range and optional filters.
- [Read a thread's share state](read-a-threads-share-state.md) - Returns the share token for a thread. The token is omitted when the thread is not shared. Gated on runs:share so the control's state matches the control's permission.
- [Share a thread](share-a-thread.md) - Mints a public share token for a thread. Idempotent: sharing an already-shared thread returns the existing token.
- [Stream messages for a public shared thread](stream-messages-for-a-public-shared-thread.md) - Streams the thread's conversation as server-sent events. SSE only.
- [Unshare a thread](unshare-a-thread.md) - Deletes the share token for a thread. Idempotent: returns 204 whether or not a share token existed. Deliberately does not verify the thread still exists.
