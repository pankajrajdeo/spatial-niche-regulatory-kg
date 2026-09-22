---
title: "create_for_thread"
description: "Create a cron job for a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/create_for_thread"
category: "reference"
tags: [reference, langgraph-sdk, async, cron, cronclient, create_for_thread]
---

# create_for_thread

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/create_for_thread)

Create a cron job for a thread.

## Signature

```python
create_for_thread(
    self,
    thread_id: str,
    assistant_id: str,
    *,
    schedule: str,
    input: Input | None = None,
    metadata: Mapping[str, Any] | None = None,
    config: Config | None = None,
    context: Context | None = None,
    checkpoint_during: bool | None = None,
    interrupt_before: All | list[str] | None = None,
    interrupt_after: All | list[str] | None = None,
    webhook: str | None = None,
    multitask_strategy: str | None = None,
    end_time: datetime | None = None,
    enabled: bool | None = None,
    timezone: str | tzinfo | None = None,
    stream_mode: StreamMode | Sequence[StreamMode] | None = None,
    stream_subgraphs: bool | None = None,
    stream_resumable: bool | None = None,
    durability: Durability | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Run
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
cron_run = await client.crons.create_for_thread(
    thread_id="my-thread-id",
    assistant_id="agent",
    schedule="27 15 * * *",
    input={"messages": [{"role": "user", "content": "hello!"}]},
    metadata={"name":"my_run"},
    context={"model_name": "openai"},
    interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
    interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
    webhook="https://my.fake.webhook.com",
    multitask_strategy="interrupt",
    enabled=True,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | the thread ID to run the cron job on. |
| `assistant_id` | `str` | Yes | The assistant ID or graph name to use for the cron job. If using graph name, will default to first assistant created from that graph. |
| `schedule` | `str` | Yes | The cron schedule to execute this job on. Schedules are interpreted in UTC unless a timezone is specified. |
| `input` | `Input \| None` | No | The input to the graph. (default: `None`) |
| `metadata` | `Mapping[str, Any] \| None` | No | Metadata to assign to the cron job runs. (default: `None`) |
| `config` | `Config \| None` | No | The configuration for the assistant. (default: `None`) |
| `context` | `Context \| None` | No | Static context to add to the assistant. !!! version-added "Added in version 0.6.0" (default: `None`) |
| `checkpoint_during` | `bool \| None` | No | (deprecated) Whether to checkpoint during the run (or only at the end/interruption). (default: `None`) |
| `interrupt_before` | `All \| list[str] \| None` | No | Nodes to interrupt immediately before they get executed. (default: `None`) |
| `interrupt_after` | `All \| list[str] \| None` | No | Nodes to Nodes to interrupt immediately after they get executed. (default: `None`) |
| `webhook` | `str \| None` | No | Webhook to call after LangGraph API call is done. (default: `None`) |
| `multitask_strategy` | `str \| None` | No | Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'. (default: `None`) |
| `end_time` | `datetime \| None` | No | The time to stop running the cron job. If not provided, the cron job will run indefinitely. (default: `None`) |
| `enabled` | `bool \| None` | No | Whether the cron job is enabled or not. (default: `None`) |
| `timezone` | `str \| tzinfo \| None` | No | IANA timezone for the cron schedule. Accepts a string (e.g. 'America/New_York') or a ``datetime.tzinfo`` instance (e.g. ``ZoneInfo("America/New_York")``). (default: `None`) |
| `stream_mode` | `StreamMode \| Sequence[StreamMode] \| None` | No | The stream mode(s) to use. (default: `None`) |
| `stream_subgraphs` | `bool \| None` | No | Whether to stream output from subgraphs. (default: `None`) |
| `stream_resumable` | `bool \| None` | No | Whether to persist the stream chunks in order to resume the stream later. (default: `None`) |
| `durability` | `Durability \| None` | No | Durability level for the run. Must be one of 'sync', 'async', or 'exit'. "async" means checkpoints are persisted async while next graph step executes, replaces checkpoint_during=True "sync" means checkpoints are persisted sync after graph step executes, replaces checkpoint_during=False "exit" means checkpoints are only persisted when the run exits, does not save intermediate steps (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Run`

The cron run.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/cron.py#L62)
