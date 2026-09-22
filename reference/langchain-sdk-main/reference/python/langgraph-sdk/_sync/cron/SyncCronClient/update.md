---
title: "update"
description: "Update a cron job by ID."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/cron/SyncCronClient/update"
category: "reference"
tags: [reference, langgraph-sdk, sync, cron, synccronclient, update]
---

# update

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/cron/SyncCronClient/update)

Update a cron job by ID.

## Signature

```python
update(
    self,
    cron_id: str,
    *,
    schedule: str | None = None,
    end_time: datetime | None = NOT_PROVIDED,
    input: Input | None = None,
    metadata: Mapping[str, Any] | None = None,
    config: Config | None = None,
    context: Context | None = None,
    webhook: str | None = None,
    interrupt_before: All | list[str] | None = None,
    interrupt_after: All | list[str] | None = None,
    on_run_completed: OnCompletionBehavior | None = None,
    enabled: bool | None = None,
    timezone: str | tzinfo | None = None,
    stream_mode: StreamMode | Sequence[StreamMode] | None = None,
    stream_subgraphs: bool | None = None,
    stream_resumable: bool | None = None,
    durability: Durability | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Cron
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:8123")
updated_cron = client.crons.update(
    cron_id="1ef3cefa-4c09-6926-96d0-3dc97fd5e39b",
    schedule="0 10 * * *",
    enabled=False,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cron_id` | `str` | Yes | The cron ID to update. |
| `schedule` | `str \| None` | No | The cron schedule to execute this job on. Schedules are interpreted in UTC unless a timezone is specified. (default: `None`) |
| `end_time` | `datetime \| None` | No | The end date to stop running the cron. Pass ``None`` to clear a previously set end time; omit to leave it unchanged. (default: `NOT_PROVIDED`) |
| `input` | `Input \| None` | No | The input to the graph. (default: `None`) |
| `metadata` | `Mapping[str, Any] \| None` | No | Metadata to assign to the cron job runs. (default: `None`) |
| `config` | `Config \| None` | No | The configuration for the assistant. (default: `None`) |
| `context` | `Context \| None` | No | Static context added to the assistant. (default: `None`) |
| `webhook` | `str \| None` | No | Webhook to call after LangGraph API call is done. (default: `None`) |
| `interrupt_before` | `All \| list[str] \| None` | No | Nodes to interrupt immediately before they get executed. (default: `None`) |
| `interrupt_after` | `All \| list[str] \| None` | No | Nodes to interrupt immediately after they get executed. (default: `None`) |
| `on_run_completed` | `OnCompletionBehavior \| None` | No | What to do with the thread after the run completes. Must be one of 'delete' or 'keep'. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up. (default: `None`) |
| `enabled` | `bool \| None` | No | Enable or disable the cron job. (default: `None`) |
| `timezone` | `str \| tzinfo \| None` | No | IANA timezone for the cron schedule. Accepts a string (e.g. 'America/New_York') or a ``datetime.tzinfo`` instance (e.g. ``ZoneInfo("America/New_York")``). (default: `None`) |
| `stream_mode` | `StreamMode \| Sequence[StreamMode] \| None` | No | The stream mode(s) to use. (default: `None`) |
| `stream_subgraphs` | `bool \| None` | No | Whether to stream output from subgraphs. (default: `None`) |
| `stream_resumable` | `bool \| None` | No | Whether to persist the stream chunks in order to resume the stream later. (default: `None`) |
| `durability` | `Durability \| None` | No | Durability level for the run. Must be one of 'sync', 'async', or 'exit'. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Cron`

The updated cron job.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/cron.py#L315)
