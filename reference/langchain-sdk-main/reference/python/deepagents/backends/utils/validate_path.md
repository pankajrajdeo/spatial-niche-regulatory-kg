---
title: "validate_path"
description: "Validate and normalize file path for security."
source: "https://reference.langchain.com/python/deepagents/backends/utils/validate_path"
category: "reference"
tags: [reference, deepagents, backends, utils, validate_path]
---

# validate_path

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/validate_path)

Validate and normalize file path for security.

Ensures paths are safe to use by preventing directory traversal attacks
and enforcing consistent formatting. All paths are normalized to use
forward slashes and start with a leading slash.

This function is designed for virtual filesystem paths and rejects
Windows absolute paths (e.g., `C:/...`, `F:/...`) to maintain consistency
and prevent path format ambiguity.

## Signature

```python
validate_path(
    path: str,
    *,
    allowed_prefixes: Sequence[str] | None = None,
) -> str
```

## Description

**Example:**

```python
validate_path("foo/bar")  # Returns: "/foo/bar"
validate_path("/./foo//bar")  # Returns: "/foo/bar"
validate_path("../etc/passwd")  # Raises ValueError
validate_path(r"C:\\Users\\file.txt")  # Raises ValueError
validate_path("/data/file.txt", allowed_prefixes=["/data/"])  # OK
validate_path("/etc/file.txt", allowed_prefixes=["/data/"])  # Raises ValueError
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `str` | Yes | The path to validate and normalize. |
| `allowed_prefixes` | `Sequence[str] \| None` | No | Optional list of allowed path prefixes.  If provided, the normalized path must start with one of these prefixes. (default: `None`) |

## Returns

`str`

Normalized canonical path starting with `/` and using forward slashes.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L692)
