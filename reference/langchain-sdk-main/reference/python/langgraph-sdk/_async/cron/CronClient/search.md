---
title: "search"
description: "Get a list of cron jobs."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/search"
category: "reference"
tags: [reference, langgraph-sdk, async, cron, cronclient, search]
---

# search

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/search)

Get a list of cron jobs.

## Signature

```python
search(
    self,
    *,
    assistant_id: str | None = None,
    thread_id: str | None = None,
    enabled: bool | None = None,
    metadata: Json = None,
    limit: int = 10,
    offset: int = 0,
    sort_by: CronSortBy | None = None,
    sort_order: SortOrder | None = None,
    select: list[CronSelectField] | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> list[Cron]
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
cron_jobs = await client.crons.search(
    assistant_id="my_assistant_id",
    thread_id="my_thread_id",
    enabled=True,
    limit=5,
    offset=5,
)
print(cron_jobs)
```
```shell

----------------------------------------------------------

[
    {
        'cron_id': '1ef3cefa-4c09-6926-96d0-3dc97fd5e39b',
        'assistant_id': 'my_assistant_id',
        'thread_id': 'my_thread_id',
        'user_id': None,
        'payload':
            {
                'input': {'start_time': ''},
                'schedule': '4 * * * *',
                'assistant_id': 'my_assistant_id'
            },
        'schedule': '4 * * * *',
        'next_run_date': '2024-07-25T17:04:00+00:00',
        'end_time': None,
        'created_at': '2024-07-08T06:02:23.073257+00:00',
        'updated_at': '2024-07-08T06:02:23.073257+00:00'
    }
]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str \| None` | No | The assistant ID or graph name to search for. (default: `None`) |
| `thread_id` | `str \| None` | No | the thread ID to search for. (default: `None`) |
| `enabled` | `bool \| None` | No | The enabled status to search for. (default: `None`) |
| `metadata` | `Json` | No | Metadata to filter by. Exact match filter for each KV pair. !!! version-added "Added in Agent Server version 0.9.0" (default: `None`) |
| `limit` | `int` | No | The maximum number of results to return. (default: `10`) |
| `offset` | `int` | No | The number of results to skip. (default: `0`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`list[Cron]`

The list of cron jobs returned by the search,

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/cron.py#L421)
