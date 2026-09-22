---
title: "SyncProtocolWebSocketTransport"
description: "Sync v3 protocol transport using HTTP commands and WebSocket events."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_ws/SyncProtocolWebSocketTransport"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, sync_ws, syncprotocolwebsockettransport]
---

# SyncProtocolWebSocketTransport

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_ws/SyncProtocolWebSocketTransport)

Sync v3 protocol transport using HTTP commands and WebSocket events.

## Signature

```python
SyncProtocolWebSocketTransport(
    self,
    *,
    client: httpx.Client,
    thread_id: str,
    commands_path: str | None = None,
    stream_path: str | None = None,
    headers: Mapping[str, str] | None = None,
    connect: Callable[..., Any] = websocket_connect,
    ping_interval: float | None = 20.0,
    ping_timeout: float | None = 20.0,
)
```

## Constructors

```python
__init__(
    self,
    *,
    client: httpx.Client,
    thread_id: str,
    commands_path: str | None = None,
    stream_path: str | None = None,
    headers: Mapping[str, str] | None = None,
    connect: Callable[..., Any] = websocket_connect,
    ping_interval: float | None = 20.0,
    ping_timeout: float | None = 20.0,
) -> None
```

| Name | Type |
|------|------|
| `client` | `httpx.Client` |
| `thread_id` | `str` |
| `commands_path` | `str \| None` |
| `stream_path` | `str \| None` |
| `headers` | `Mapping[str, str] \| None` |
| `connect` | `Callable[..., Any]` |
| `ping_interval` | `float \| None` |
| `ping_timeout` | `float \| None` |

## Properties

- `thread_id`

## Methods

- [`send_command()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_ws/SyncProtocolWebSocketTransport/send_command)
- [`open_event_stream()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_ws/SyncProtocolWebSocketTransport/open_event_stream)
- [`close()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_ws/SyncProtocolWebSocketTransport/close)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/transport/sync_ws.py#L23)
