---
title: "get_field_default"
description: "Determine the default value for a field in a state schema."
source: "https://reference.langchain.com/python/langgraph/graph/state/get_field_default"
category: "reference"
tags: [reference, langgraph, graph, state, get_field_default]
---

# get_field_default

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_fields/get_field_default)

Determine the default value for a field in a state schema.

## Signature

```python
get_field_default(
    name: str,
    type_: Any,
    schema: type[Any],
) -> Any
```

## Description

**This is based on:**

If TypedDict:
    - Required/NotRequired
    - total=False -> everything optional
- Type annotation (Optional/Union[None])

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_fields.py#L79)
