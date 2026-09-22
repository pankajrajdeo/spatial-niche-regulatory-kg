---
title: "get_subgraphs"
description: "Get the schemas of an assistant by ID."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/get_subgraphs"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, get_subgraphs]
---

# get_subgraphs

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/get_subgraphs)

Get the schemas of an assistant by ID.

## Signature

```python
get_subgraphs(
    self,
    assistant_id: str,
    namespace: str | None = None,
    recurse: bool = False,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Subgraphs
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | The ID of the assistant to get the schema of. |
| `namespace` | `str \| None` | No | Optional namespace to filter by. (default: `None`) |
| `recurse` | `bool` | No | Whether to recursively get subgraphs. (default: `False`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Subgraphs`

The graph schema for the assistant.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L276)
