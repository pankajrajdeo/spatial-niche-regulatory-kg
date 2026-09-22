---
title: "stream"
description: "Stream the results of a request using SSE."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/stream"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, stream]
---

# stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/stream)

Stream the results of a request using SSE.

## Signature

```python
stream(
    self,
    path: str,
    method: str,
    *,
    json: dict[str, Any] | None = None,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> Iterator[StreamPart]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/http.py#L187)
