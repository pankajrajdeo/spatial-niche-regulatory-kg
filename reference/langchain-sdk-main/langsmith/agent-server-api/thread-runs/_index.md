---
title: "langsmith/agent-server-api/thread-runs"
description: "Index of 10 pages and 0 subdirectories under langsmith/agent-server-api/thread-runs."
category: "index"
tags: [index, langsmith, agent-server-api, thread-runs]
---

# langsmith/agent-server-api/thread-runs

10 pages here.

## Files

- [Cancel Run](cancel-run.md) - /langsmith/agent-server-openapi.json post /threads/{thread_id}/runs/{run_id}/cancel
- [Cancel Runs](cancel-runs.md) - Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.
- [Create Background Run](create-background-run.md) - Create a run in existing thread, return the run ID immediately. Don't wait for the final run output.
- [Create Run, Stream Output](create-run-stream-output.md) - Create a run in existing thread. Stream the output.
- [Create Run, Wait for Output](create-run-wait-for-output.md) - Create a run in existing thread. Wait for the final output and then return it.
- [Delete Run](delete-run.md) - Delete a run by ID.
- [Get Run](get-run.md) - Get a run by ID.
- [Join Run Stream](join-run-stream.md) - Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with stream_resumable=true, the stream...
- [Join Run](join-run.md) - Wait for a run to finish.
- [List Runs](list-runs.md) - List runs for a thread.
