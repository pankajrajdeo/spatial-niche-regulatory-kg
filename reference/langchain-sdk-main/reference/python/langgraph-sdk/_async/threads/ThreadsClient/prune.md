---
title: "prune"
description: "Prune threads by ID."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/prune"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, prune]
---

# prune

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/prune)

Prune threads by ID.

## Signature

```python
prune(
    self,
    thread_ids: Sequence[str],
    *,
    strategy: PruneStrategy = 'delete',
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> dict[str, Any]
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
result = await client.threads.prune(
    thread_ids=["thread_1", "thread_2"],
)
print(result)  # {'pruned_count': 2}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_ids` | `Sequence[str]` | Yes | List of thread IDs to prune. |
| `strategy` | `PruneStrategy` | No | The prune strategy. `"delete"` removes threads entirely. `"keep_latest"` prunes old checkpoints but keeps threads and their latest state. Defaults to `"delete"`. (default: `'delete'`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`dict[str, Any]`

A dict containing `pruned_count` (number of threads pruned).

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L444)
