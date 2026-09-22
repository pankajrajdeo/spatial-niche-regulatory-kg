---
title: "as_import_path"
description: "Path of the file as a LangChain import exclude langchain top namespace."
source: "https://reference.langchain.com/python/langchain-core/_api/path/as_import_path"
category: "reference"
tags: [reference, langchain-core, api, path, as_import_path]
---

# as_import_path

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/path/as_import_path)

Path of the file as a LangChain import exclude langchain top namespace.

## Signature

```python
as_import_path(
    file: Path | str,
    *,
    suffix: str | None = None,
    relative_to: Path = PACKAGE_DIR,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file` | `Path \| str` | Yes | The file path to convert. |
| `suffix` | `str \| None` | No | An optional suffix to append to the import path. (default: `None`) |
| `relative_to` | `Path` | No | The base path to make the file path relative to. (default: `PACKAGE_DIR`) |

## Returns

`str`

The import path as a string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_api/path.py#L26)
