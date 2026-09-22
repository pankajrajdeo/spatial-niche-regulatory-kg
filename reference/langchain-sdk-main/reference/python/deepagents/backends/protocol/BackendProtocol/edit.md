---
title: "edit"
description: "Perform exact string replacements in an existing file."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/edit"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, edit]
---

# edit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/edit)

Perform exact string replacements in an existing file.

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
| `file_path` | `str` | Yes | Absolute path to the file to edit. Must start with `'/'`. |
| `old_string` | `str` | Yes | Exact string to search for and replace.  Must match exactly including whitespace and indentation. |
| `new_string` | `str` | Yes | String to replace old_string with.  Must be different from old_string. |
| `replace_all` | `bool` | No | If True, replace all occurrences.  If `False` (default), `old_string` must be unique in the file or the edit fails. (default: `False`) |

## Returns

`EditResult`

EditResult

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L685)
