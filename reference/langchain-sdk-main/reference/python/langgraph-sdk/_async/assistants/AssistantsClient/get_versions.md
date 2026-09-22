---
title: "get_versions"
description: "List all versions of an assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/get_versions"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, get_versions]
---

# get_versions

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/get_versions)

List all versions of an assistant.

## Signature

```python
get_versions(
    self,
    assistant_id: str,
    metadata: Json = None,
    limit: int = 10,
    offset: int = 0,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> list[AssistantVersion]
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
assistant_versions = await client.assistants.get_versions(
    assistant_id="my_assistant_id"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | The assistant ID to get versions for. |
| `metadata` | `Json` | No | Metadata to filter versions by. Exact match filter for each KV pair. (default: `None`) |
| `limit` | `int` | No | The maximum number of versions to return. (default: `10`) |
| `offset` | `int` | No | The number of versions to skip. (default: `0`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`list[AssistantVersion]`

A list of assistant versions.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L656)
