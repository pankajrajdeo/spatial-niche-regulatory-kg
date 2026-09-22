---
title: "SyncStreamController"
description: "Owns the sync shared SSE handle, subscription registry, and fan-out thread."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController"
category: "reference"
tags: [reference, langgraph-sdk, stream, sync_controller, syncstreamcontroller]
---

# SyncStreamController

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController)

Owns the sync shared SSE handle, subscription registry, and fan-out thread.

## Signature

```python
SyncStreamController(
    self,
    transport: SyncProtocolTransport,
    *,
    run_start_gate: threading.Event | None = None,
    run_start_timeout: float = _DEFAULT_RUN_START_TIMEOUT,
    max_reconnect_attempts: int = 5,
    reconnect_backoff_base: float = 0.1,
    reconnect_backoff_cap: float = 10.0,
)
```

## Constructors

```python
__init__(
    self,
    transport: SyncProtocolTransport,
    *,
    run_start_gate: threading.Event | None = None,
    run_start_timeout: float = _DEFAULT_RUN_START_TIMEOUT,
    max_reconnect_attempts: int = 5,
    reconnect_backoff_base: float = 0.1,
    reconnect_backoff_cap: float = 10.0,
) -> None
```

| Name | Type |
|------|------|
| `transport` | `SyncProtocolTransport` |
| `run_start_gate` | `threading.Event \| None` |
| `run_start_timeout` | `float` |
| `max_reconnect_attempts` | `int` |
| `reconnect_backoff_base` | `float` |
| `reconnect_backoff_cap` | `float` |

## Methods

- [`register_subscription()`](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/register_subscription)
- [`unregister_subscription()`](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/unregister_subscription)
- [`signal_paused()`](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/signal_paused)
- [`reconcile_stream()`](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/reconcile_stream)
- [`ensure_fanout_running()`](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/ensure_fanout_running)
- [`observe_applied_through_seq()`](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/observe_applied_through_seq)
- [`close()`](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/close)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/sync_controller.py#L62)
