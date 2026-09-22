---
title: "CronUpdate"
description: "Payload for updating a cron job. All fields are optional."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/CronUpdate"
category: "reference"
tags: [reference, langgraph-sdk, schema, cronupdate]
---

# CronUpdate

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/CronUpdate)

Payload for updating a cron job. All fields are optional.

## Signature

```python
CronUpdate()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    schedule: str,
    timezone: str,
    end_time: datetime,
    input: Input,
    metadata: dict[str, Any],
    config: Config,
    context: Context,
    webhook: str,
    interrupt_before: All | list[str],
    interrupt_after: All | list[str],
    on_run_completed: OnCompletionBehavior,
    enabled: bool,
    stream_mode: StreamMode | list[StreamMode],
    stream_subgraphs: bool,
    stream_resumable: bool,
    durability: Durability,
)
```

| Name | Type |
|------|------|
| `schedule` | `str` |
| `timezone` | `str` |
| `end_time` | `datetime` |
| `input` | `Input` |
| `metadata` | `dict[str, Any]` |
| `config` | `Config` |
| `context` | `Context` |
| `webhook` | `str` |
| `interrupt_before` | `All \| list[str]` |
| `interrupt_after` | `All \| list[str]` |
| `on_run_completed` | `OnCompletionBehavior` |
| `enabled` | `bool` |
| `stream_mode` | `StreamMode \| list[StreamMode]` |
| `stream_subgraphs` | `bool` |
| `stream_resumable` | `bool` |
| `durability` | `Durability` |

## Properties

- `schedule`
- `timezone`
- `end_time`
- `input`
- `metadata`
- `config`
- `context`
- `webhook`
- `interrupt_before`
- `interrupt_after`
- `on_run_completed`
- `enabled`
- `stream_mode`
- `stream_subgraphs`
- `stream_resumable`
- `durability`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L416)
