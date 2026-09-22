---
title: "SyncHttpClient"
description: "Handle synchronous requests to the LangGraph API."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient]
---

<a id="HttpClient"></a>

# SyncHttpClient

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient)

Handle synchronous requests to the LangGraph API.

Provides error messaging and content handling enhancements above the
underlying httpx client, mirroring the interface of [HttpClient](#HttpClient)
but for sync usage.

## Signature

```python
SyncHttpClient(
    self,
    client: httpx.Client,
)
```

## Constructors

```python
__init__(
    self,
    client: httpx.Client,
) -> None
```

| Name | Type |
|------|------|
| `client` | `httpx.Client` |

## Properties

- `client`

## Methods

- [`get()`](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/get)
- [`post()`](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/post)
- [`put()`](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/put)
- [`patch()`](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/patch)
- [`delete()`](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/delete)
- [`request_reconnect()`](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/request_reconnect)
- [`stream()`](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/stream)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/http.py#L25)
