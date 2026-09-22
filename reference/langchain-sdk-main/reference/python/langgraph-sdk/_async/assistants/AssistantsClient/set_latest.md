---
title: "set_latest"
description: "Change the version of an assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/set_latest"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, set_latest]
---

# set_latest

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/set_latest)

Change the version of an assistant.

## Signature

```python
set_latest(
    self,
    assistant_id: str,
    version: int,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Assistant
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
new_version_assistant = await client.assistants.set_latest(
    assistant_id="my_assistant_id",
    version=3
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | The assistant ID to delete. |
| `version` | `int` | Yes | The version to change to. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Assistant`

Assistant Object.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L702)
