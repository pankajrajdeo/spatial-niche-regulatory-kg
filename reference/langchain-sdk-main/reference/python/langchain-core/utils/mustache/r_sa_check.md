---
title: "r_sa_check"
description: "Do a final check to see if a tag could be a standalone."
source: "https://reference.langchain.com/python/langchain-core/utils/mustache/r_sa_check"
category: "reference"
tags: [reference, langchain-core, utils, mustache, r_sa_check]
---

# r_sa_check

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/mustache/r_sa_check)

Do a final check to see if a tag could be a standalone.

## Signature

```python
r_sa_check(
    template: str,
    tag_type: str,
    is_standalone: bool,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template. |
| `tag_type` | `str` | Yes | The type of the tag. |
| `is_standalone` | `bool` | Yes | Whether the tag is standalone. |

## Returns

`bool`

Whether the tag could be a standalone.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/mustache.py#L92)
