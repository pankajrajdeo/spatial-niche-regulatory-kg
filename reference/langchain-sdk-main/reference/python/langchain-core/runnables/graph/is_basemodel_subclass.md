---
title: "is_basemodel_subclass"
description: "Check if the given class is a subclass of Pydantic BaseModel."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/is_basemodel_subclass"
category: "reference"
tags: [reference, langchain-core, runnables, graph, is_basemodel_subclass]
---

# is_basemodel_subclass

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/is_basemodel_subclass)

Check if the given class is a subclass of Pydantic `BaseModel`.

Check if the given class is a subclass of any of the following:

* `pydantic.BaseModel` in Pydantic 2.x
* `pydantic.v1.BaseModel` in Pydantic 2.x

## Signature

```python
is_basemodel_subclass(
    cls: type,
) -> bool
```

## Returns

`bool`

`True` if the given class is a subclass of Pydantic `BaseModel`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/pydantic.py#L97)
