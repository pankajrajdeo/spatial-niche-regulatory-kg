---
title: "to_posix_path"
description: "Normalize backslash separators to forward slashes for PurePosixPath use."
source: "https://reference.langchain.com/python/deepagents/backends/utils/to_posix_path"
category: "reference"
tags: [reference, deepagents, backends, utils, to_posix_path]
---

# to_posix_path

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/to_posix_path)

Normalize backslash separators to forward slashes for `PurePosixPath` use.

Backends running on Windows return OS-native paths using backslashes.
`PurePosixPath` treats backslashes as literal filename characters,
so `PurePosixPath(r"C:\a\b").name` yields the full string instead
of `"b"`. Normalize before constructing a `PurePosixPath`.

This is best-effort: a POSIX directory literally named with a backslash
will also be rewritten. That trade-off is accepted because such filenames
are vanishingly rare in practice and the alternative (gating on `os.sep`)
fails when a Windows-style path is handed to a non-Windows process.

## Signature

```python
to_posix_path(
    path: str,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `str` | Yes | Path string that may use backslash separators. |

## Returns

`str`

The same path with every `\\` replaced by `/`.

Inputs that already use forward slashes are returned unchanged.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L668)
