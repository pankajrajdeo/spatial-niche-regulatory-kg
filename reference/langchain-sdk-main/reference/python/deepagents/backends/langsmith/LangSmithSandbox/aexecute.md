---
title: "aexecute"
description: "Execute a shell command inside the sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/aexecute"
category: "reference"
tags: [reference, deepagents, backends, langsmith, langsmithsandbox, aexecute]
---

# aexecute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/aexecute)

Execute a shell command inside the sandbox.

Overrides the protocol default, which offloads the blocking `execute()`
to a worker thread. `BaseSandbox` routes every async filesystem
operation through `aexecute`, so using the SDK's async client here keeps
all of them off the sync transport.

## Signature

```python
aexecute(
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
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for the command to complete.  If `None`, uses the backend's default timeout. (default: `None`) |

## Returns

`ExecuteResponse`

`ExecuteResponse` containing output, exit code, and truncation flag.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/langsmith.py#L113)
