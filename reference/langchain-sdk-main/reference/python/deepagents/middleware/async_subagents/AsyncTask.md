---
title: "AsyncTask"
description: "A tracked async subagent task persisted in agent state."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asynctask]
---

# AsyncTask

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask)

A tracked async subagent task persisted in agent state.

## Signature

```python
AsyncTask()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    task_id: str,
    agent_name: str,
    thread_id: str,
    run_id: str,
    status: str,
    created_at: str,
    last_checked_at: str,
    last_updated_at: str,
)
```

| Name | Type |
|------|------|
| `task_id` | `str` |
| `agent_name` | `str` |
| `thread_id` | `str` |
| `run_id` | `str` |
| `status` | `str` |
| `created_at` | `str` |
| `last_checked_at` | `str` |
| `last_updated_at` | `str` |

## Properties

- `task_id`
- `agent_name`
- `thread_id`
- `run_id`
- `status`
- `created_at`
- `last_checked_at`
- `last_updated_at`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/async_subagents.py#L80)
