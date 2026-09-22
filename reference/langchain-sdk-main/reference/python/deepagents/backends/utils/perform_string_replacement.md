---
title: "perform_string_replacement"
description: "Perform string replacement with occurrence validation."
source: "https://reference.langchain.com/python/deepagents/backends/utils/perform_string_replacement"
category: "reference"
tags: [reference, deepagents, backends, utils, perform_string_replacement]
---

# perform_string_replacement

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/perform_string_replacement)

Perform string replacement with occurrence validation.

## Signature

```python
perform_string_replacement(
    content: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> tuple[str, int] | str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | Original content |
| `old_string` | `str` | Yes | String to replace |
| `new_string` | `str` | Yes | Replacement string |
| `replace_all` | `bool` | No | Whether to replace all occurrences (default: `False`) |

## Returns

`tuple[str, int] | str`

Tuple of `(new_content, occurrences)` on success, or error message string

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L543)
