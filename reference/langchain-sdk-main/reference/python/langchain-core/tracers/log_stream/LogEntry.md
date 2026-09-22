---
title: "LogEntry"
description: "A single entry in the run log."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogEntry"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, logentry]
---

# LogEntry

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogEntry)

A single entry in the run log.

## Signature

```python
LogEntry()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    type: str,
    tags: list[str],
    metadata: dict[str, Any],
    start_time: str,
    streamed_output_str: list[str],
    streamed_output: list[Any],
    inputs: NotRequired[Any | None],
    final_output: Any | None,
    end_time: str | None,
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `type` | `str` |
| `tags` | `list[str]` |
| `metadata` | `dict[str, Any]` |
| `start_time` | `str` |
| `streamed_output_str` | `list[str]` |
| `streamed_output` | `list[Any]` |
| `inputs` | `NotRequired[Any \| None]` |
| `final_output` | `Any \| None` |
| `end_time` | `str \| None` |

## Properties

- `id`
- `name`
- `type`
- `tags`
- `metadata`
- `start_time`
- `streamed_output_str`
- `streamed_output`
- `inputs`
- `final_output`
- `end_time`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/log_stream.py#L40)
