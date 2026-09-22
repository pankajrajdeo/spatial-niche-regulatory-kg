---
title: "delete"
description: "Send a DELETE request."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/delete"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, delete]
---

# delete

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/delete)

Send a `DELETE` request.

## Signature

```python
delete(
    self,
    path: str,
    *,
    json: Any | None = None,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/http.py#L121)
