---
title: "AsyncThreadStream"
description: "Async context manager for one thread's v3 streaming session."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, asyncthreadstream]
---

# AsyncThreadStream

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream)

Async context manager for one thread's v3 streaming session.

Construct via `client.threads.stream(thread_id=None, *, assistant_id, ...)`
rather than instantiating directly.

## Signature

```python
AsyncThreadStream(
    self,
    *,
    http: HttpClient,
    thread_id: str,
    assistant_id: str,
    headers: Mapping[str, str] | None = None,
    max_queue_size: int = 1024,
    run_start_timeout: float | None = None,
    explicit_thread_id: bool = False,
    transport_kind: Literal['sse', 'websocket'] = 'sse',
)
```

## Constructors

```python
__init__(
    self,
    *,
    http: HttpClient,
    thread_id: str,
    assistant_id: str,
    headers: Mapping[str, str] | None = None,
    max_queue_size: int = 1024,
    run_start_timeout: float | None = None,
    explicit_thread_id: bool = False,
    transport_kind: Literal['sse', 'websocket'] = 'sse',
) -> None
```

| Name | Type |
|------|------|
| `http` | `HttpClient` |
| `thread_id` | `str` |
| `assistant_id` | `str` |
| `headers` | `Mapping[str, str] \| None` |
| `max_queue_size` | `int` |
| `run_start_timeout` | `float \| None` |
| `explicit_thread_id` | `bool` |
| `transport_kind` | `Literal['sse', 'websocket']` |

## Properties

- `thread_id`
- `assistant_id`
- `interrupted`
- `interrupts`
- `run`
- `agent`
- `output`
- `values`
- `messages`
- `tool_calls`
- `subgraphs`
- `subagents`
- `extensions`
- `events`

## Methods

- [`close()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream/close)
- [`observe_applied_through_seq()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream/observe_applied_through_seq)
- [`subscribe()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream/subscribe)
- [`interleave_projections()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream/interleave_projections)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/stream.py#L1160)
