---
title: "file_data_to_string"
description: "Convert current or legacy persisted file content to a string."
source: "https://reference.langchain.com/python/deepagents/backends/store/file_data_to_string"
category: "reference"
tags: [reference, deepagents, backends, store, file_data_to_string]
---

# file_data_to_string

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/file_data_to_string)

Convert current or legacy persisted file content to a string.

## Signature

```python
file_data_to_string(
    file_data: FileData,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_data` | `FileData` | Yes | File data whose content is a string or legacy list of strings. |

## Returns

`str`

Content as a single string.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L344)
