---
title: "write"
description: "Write content using the LangSmith SDK to avoid ARG_MAX."
source: "https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/write"
category: "reference"
tags: [reference, deepagents, backends, langsmith, langsmithsandbox, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/write)

Write content using the LangSmith SDK to avoid ARG_MAX.

`BaseSandbox.write()` sends the full content in a shell command, which
can exceed ARG_MAX for large content. This override uses the SDK's
native `write()`, which sends content in the HTTP body, but preserves
the same existence check and parent-directory creation as
`BaseSandbox.write()`.

## Signature

```python
write(
    self,
    file_path: str,
    content: str,
) -> WriteResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Destination path inside the sandbox. |
| `content` | `str` | Yes | Text content to write. |

## Returns

`WriteResult`

`WriteResult` with the written path on success, or an error message.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/langsmith.py#L141)
