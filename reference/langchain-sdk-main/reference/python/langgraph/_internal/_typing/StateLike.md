---
title: "StateLike"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/_internal/_typing/StateLike"
category: "reference"
tags: [reference, langgraph, internal, typing, statelike]
---

# StateLike

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_typing/StateLike)

Type alias for state-like types.

It can either be a `TypedDict`, `dataclass`, or Pydantic `BaseModel`.
Note: we cannot use either `TypedDict` or `dataclass` directly due to limitations in type checking.

## Signature

```python
StateLike: TypeAlias = TypedDictLikeV1 | TypedDictLikeV2 | DataclassLike | BaseModel
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_typing.py#L38)
