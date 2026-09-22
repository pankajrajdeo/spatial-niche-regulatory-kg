---
title: "LogStreamCallbackHandler"
description: "Tracer that streams run logs to a stream."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, logstreamcallbackhandler]
---

# LogStreamCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler)

Tracer that streams run logs to a stream.

## Signature

```python
LogStreamCallbackHandler(
    self,
    *,
    auto_close: bool = True,
    include_names: Sequence[str] | None = None,
    include_types: Sequence[str] | None = None,
    include_tags: Sequence[str] | None = None,
    exclude_names: Sequence[str] | None = None,
    exclude_types: Sequence[str] | None = None,
    exclude_tags: Sequence[str] | None = None,
    _schema_format: Literal['original', 'streaming_events'] = 'streaming_events',
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `auto_close` | `bool` | No | Whether to close the stream when the root run finishes. (default: `True`) |
| `include_names` | `Sequence[str] \| None` | No | Only include runs from `Runnable` objects with matching names. (default: `None`) |
| `include_types` | `Sequence[str] \| None` | No | Only include runs from `Runnable` objects with matching types. (default: `None`) |
| `include_tags` | `Sequence[str] \| None` | No | Only include runs from `Runnable` objects with matching tags. (default: `None`) |
| `exclude_names` | `Sequence[str] \| None` | No | Exclude runs from `Runnable` objects with matching names. (default: `None`) |
| `exclude_types` | `Sequence[str] \| None` | No | Exclude runs from `Runnable` objects with matching types. (default: `None`) |
| `exclude_tags` | `Sequence[str] \| None` | No | Exclude runs from `Runnable` objects with matching tags. (default: `None`) |
| `_schema_format` | `Literal['original', 'streaming_events']` | No | Primarily changes how the inputs and outputs are handled.  **For internal use only. This API will change.**  - `'original'` is the format used by all current tracers. This format is     slightly inconsistent with respect to inputs and outputs. - 'streaming_events' is used for supporting streaming events, for     internal usage. It will likely change in the future,     or be deprecated entirely in favor of a dedicated async     tracer for streaming events. (default: `'streaming_events'`) |

## Extends

- `BaseTracer`
- `_StreamingCallbackHandler[Any]`

## Constructors

```python
__init__(
    self,
    *,
    auto_close: bool = True,
    include_names: Sequence[str] | None = None,
    include_types: Sequence[str] | None = None,
    include_tags: Sequence[str] | None = None,
    exclude_names: Sequence[str] | None = None,
    exclude_types: Sequence[str] | None = None,
    exclude_tags: Sequence[str] | None = None,
    _schema_format: Literal['original', 'streaming_events'] = 'streaming_events',
) -> None
```

| Name | Type |
|------|------|
| `auto_close` | `bool` |
| `include_names` | `Sequence[str] \| None` |
| `include_types` | `Sequence[str] \| None` |
| `include_tags` | `Sequence[str] \| None` |
| `exclude_names` | `Sequence[str] \| None` |
| `exclude_types` | `Sequence[str] \| None` |
| `exclude_tags` | `Sequence[str] \| None` |
| `_schema_format` | `Literal['original', 'streaming_events']` |

## Properties

- `auto_close`
- `include_names`
- `include_types`
- `include_tags`
- `exclude_names`
- `exclude_types`
- `exclude_tags`
- `lock`
- `send_stream`
- `receive_stream`
- `root_id`

## Methods

- [`send()`](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/send)
- [`tap_output_aiter()`](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/tap_output_aiter)
- [`tap_output_iter()`](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/tap_output_iter)
- [`include_run()`](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/include_run)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/log_stream.py#L232)
