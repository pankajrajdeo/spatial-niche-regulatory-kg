---
title: "read"
description: "Read file content using the LangSmith SDK."
source: "https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/read"
category: "reference"
tags: [reference, deepagents, backends, langsmith, langsmithsandbox, read]
---

# read

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/read)

Read file content using the LangSmith SDK.

`BaseSandbox.read()` pipes file content through `execute()`, which
can hang or exceed transport limits for large files. This override
fetches bytes directly via the SDK and reproduces the base-class
pagination semantics locally:

- Empty files surface the "empty contents" reminder.
- Files routed as binary by extension (or that fail UTF-8 decode) are
    returned base64-encoded, capped at `MAX_BINARY_BYTES`.
- Text content is normalized for universal newlines (`\r\n` and bare
    `\r` collapse to `\n`), split on `\n`, paginated by `offset` /
    `limit`, joined back with `\n`, and capped at `MAX_OUTPUT_BYTES`
    with `TRUNCATION_MSG` appended on overflow.
- A negative `offset` is clamped to the start of the file, and a
    non-positive `limit` returns empty content with no pagination
    metadata.

## Signature

```python
read(
    self,
    file_path: str,
    offset: int = 0,
    limit: int = 2000,
) -> ReadResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Absolute path to the file to read. |
| `offset` | `int` | No | Number of leading text lines to skip. (default: `0`) |
| `limit` | `int` | No | Maximum number of text lines to return. (default: `2000`) |

## Returns

`ReadResult`

`ReadResult` with `file_data` on success or `error` on failure.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/langsmith.py#L169)
