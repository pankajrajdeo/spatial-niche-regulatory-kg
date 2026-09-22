---
title: "langsmith/smith-api/runs"
description: "Index of 13 pages and 0 subdirectories under langsmith/smith-api/runs."
category: "index"
tags: [index, langsmith, smith-api, runs]
---

# langsmith/smith-api/runs

13 pages here.

## Files

- [Create a run](create-a-run.md) - Queues a single run for ingestion. The request body must be a JSON-encoded run object that follows the Run schema.
- [Get a public shared trace run](get-a-public-shared-trace-run.md) - Returns one run within the trace identified by the share token. The request supplies only the run ID and that run's exact start_time coordinate.
- [Get a single run](get-a-single-run.md) - Returns one run by ID for the given session. Use the selects query parameter (repeatable) to select fields to return.
- [Get the LangSmith UI URL for a run](get-the-langsmith-ui-url-for-a-run.md) - Returns the URL to view a specific run in the LangSmith UI. The caller must supply the run's project_id and trace_id as query parameters; start_time is optional.
- [Ingest runs (batch json)](ingest-runs-batch-json.md) - Ingests a batch of runs in a single JSON payload. The payload must have post and/or patch arrays containing run objects. Prefer this endpoint over single‑run ingestion when submitting hundreds of...
- [Ingest runs (multipart)](ingest-runs-multipart.md) - Ingests multiple runs, feedback objects, and binary attachments in a single multipart/form-data request. Part‑name pattern: .[.] where event ∈ {post, patch, feedback, attachment}. post|patch. – JSON...
- [List runs in a trace](list-runs-in-a-trace.md) - Returns runs for a trace ID within min/max start time. Optional filter; repeatable selects to select fields to return.
- [Query public shared trace runs](query-public-shared-trace-runs.md) - Returns all runs within the trace identified by the share token. The share token supplies the tenant, project, and trace scope.
- [Query runs](query-runs.md) - Returns a paginated list of runs for the given projects within min/max start_time. Supports filters, cursor pagination, and selects to select fields to return.
- [Query traces](query-traces.md) - Returns a paginated list of traces (root runs) for a single tracing project. Each item carries the trace's root run plus optional trace-wide aggregates (total_tokens, total_cost, first_token_time)...
- [Share a run](share-a-run.md) - Creates or returns a share token for a run. Child runs share their trace root.
- [Unshare a run](unshare-a-run.md) - Deletes the share token for the trace identified by trace_id and session_id. Idempotent: returns 204 whether or not a share token existed.
- [Update a run](update-a-run.md) - Updates a run identified by its ID. The body should contain only the fields to be changed; unknown fields are ignored.
