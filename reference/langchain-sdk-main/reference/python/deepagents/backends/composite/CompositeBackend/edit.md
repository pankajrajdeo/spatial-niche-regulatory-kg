---
title: "edit"
description: "Edit a file, routing to appropriate backend."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/edit"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, edit]
---

# edit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/edit)

Edit a file, routing to appropriate backend.

## Signature

```python
edit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Absolute file path. |
| `old_string` | `str` | Yes | String to find and replace. |
| `new_string` | `str` | Yes | Replacement string. |
| `replace_all` | `bool` | No | If `True`, replace all occurrences. (default: `False`) |

## Returns

`EditResult`

Success message or `Command` object, or error message on failure.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/composite.py#L740)
