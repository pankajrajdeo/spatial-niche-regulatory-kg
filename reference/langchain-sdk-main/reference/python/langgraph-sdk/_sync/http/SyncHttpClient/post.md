---
title: "post"
description: "Send a POST request."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/post"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, post]
---

# post

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/post)

Send a `POST` request.

## Signature

```python
post(
    self,
    path: str,
    *,
    json: dict[str, Any] | list | None,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/http.py#L54)
