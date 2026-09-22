---
title: "langsmith/smith-api/evaluators"
description: "Index of 7 pages and 0 subdirectories under langsmith/smith-api/evaluators."
category: "index"
tags: [index, langsmith, smith-api, evaluators]
---

# langsmith/smith-api/evaluators

7 pages here.

## Files

- [Bulk delete evaluators](bulk-delete-evaluators.md) - Delete multiple evaluators by their IDs. Returns per-item success/failure.
- [Create evaluator](create-evaluator.md) - Create a new LLM or code evaluator for the current workspace.
- [Delete evaluator](delete-evaluator.md) - Delete an evaluator. Returns 409 when a code evaluator build is ENQUEUED or BUILDING, or when run rules still reference the evaluator and delete_run_rules is false. When delete_run_rules is true, all...
- [Get evaluator spend](get-evaluator-spend.md) - Returns per-day LLM evaluator spend for the requested 7-day period, grouped by evaluator, resource, or run rule. Exactly one of group_by, evaluator_id, session_id, or dataset_id is required...
- [Get evaluator](get-evaluator.md) - Retrieve a single evaluator by its ID.
- [List evaluators](list-evaluators.md) - List evaluators for the current workspace, with optional filtering by type, name, tag, feedback key, or resource ID.
- [Update evaluator](update-evaluator.md) - Update an existing evaluator's name, LLM configuration, or code configuration. Returns 409 when a code evaluator build is ENQUEUED or BUILDING.
