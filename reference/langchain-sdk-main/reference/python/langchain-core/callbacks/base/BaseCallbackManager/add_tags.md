---
title: "add_tags"
description: "Add tags to the callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/add_tags"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackmanager, add_tags]
---

# add_tags

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/add_tags)

Add tags to the callback manager.

## Signature

```python
add_tags(
    self,
    tags: list[str],
    inherit: bool = True,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tags` | `list[str]` | Yes | The tags to add. |
| `inherit` | `bool` | No | Whether to inherit the tags. (default: `True`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L1167)
