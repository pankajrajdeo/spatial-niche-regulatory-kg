---
title: "put"
description: "Send a PUT request."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/put"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, put]
---

# put

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/put)

Send a `PUT` request.

## Signature

```python
put(
    self,
    path: str,
    *,
    json: dict,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/http.py#L78)
