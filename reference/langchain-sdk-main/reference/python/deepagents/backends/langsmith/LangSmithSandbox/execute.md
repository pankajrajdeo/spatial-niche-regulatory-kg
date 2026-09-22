---
title: "execute"
description: "Execute a shell command inside the sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/execute"
category: "reference"
tags: [reference, deepagents, backends, langsmith, langsmithsandbox, execute]
---

# execute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/execute)

Execute a shell command inside the sandbox.

## Signature

```python
execute(
    self,
    command: str,
    *,
    timeout: int | None = None,
) -> ExecuteResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `command` | `str` | Yes | Shell command string to execute. |
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for the command to complete.  If `None`, uses the backend's default timeout.  A value of 0 disables the command timeout when the `langsmith[sandbox]` extra is installed. (default: `None`) |

## Returns

`ExecuteResponse`

`ExecuteResponse` containing output, exit code, and truncation flag.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/langsmith.py#L79)
