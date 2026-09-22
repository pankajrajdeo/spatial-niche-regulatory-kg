---
title: "delete_ui_message"
description: "Delete a UI message by ID from the UI state."
source: "https://reference.langchain.com/python/langgraph/graph/ui/delete_ui_message"
category: "reference"
tags: [reference, langgraph, graph, ui, delete_ui_message]
---

# delete_ui_message

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/ui/delete_ui_message)

Delete a UI message by ID from the UI state.

This function creates and sends a message to remove a UI component from the current state.
It also updates the graph state to remove the UI message.

## Signature

```python
delete_ui_message(
    id: str,
    *,
    state_key: str = 'ui',
) -> RemoveUIMessage
```

## Description

**Example:**

```python
delete_ui_message("message-123")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | `str` | Yes | Unique identifier of the UI component to remove. |
| `state_key` | `str` | No | Key in the graph state where the UI messages are stored. Defaults to "ui". (default: `'ui'`) |

## Returns

`RemoveUIMessage`

The remove UI message.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/ui.py#L133)
