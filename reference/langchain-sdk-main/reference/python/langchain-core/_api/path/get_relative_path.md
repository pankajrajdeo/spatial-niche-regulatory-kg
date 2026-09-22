---
title: "get_relative_path"
description: "Get the path of the file as a relative path to the package directory."
source: "https://reference.langchain.com/python/langchain-core/_api/path/get_relative_path"
category: "reference"
tags: [reference, langchain-core, api, path, get_relative_path]
---

# get_relative_path

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/path/get_relative_path)

Get the path of the file as a relative path to the package directory.

## Signature

```python
get_relative_path(
    file: Path | str,
    *,
    relative_to: Path = PACKAGE_DIR,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file` | `Path \| str` | Yes | The file path to convert. |
| `relative_to` | `Path` | No | The base path to make the file path relative to. (default: `PACKAGE_DIR`) |

## Returns

`str`

The relative path as a string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_api/path.py#L11)
