---
title: "execute"
description: "Execute a shell command in the sandbox environment."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol/execute"
category: "reference"
tags: [reference, deepagents, backends, protocol, sandboxbackendprotocol, execute]
---

# execute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol/execute)

Execute a shell command in the sandbox environment.

Simplified interface optimized for LLM consumption.

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
| `command` | `str` | Yes | Full shell command string to execute. |
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for the command to complete.  If None, uses the backend's default timeout.  Callers should provide non-negative integer values for portable behavior across backends. A value of 0 may disable timeouts on backends that support no-timeout execution. (default: `None`) |

## Returns

`ExecuteResponse`

`ExecuteResponse` with combined output, exit code, and truncation flag.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L887)
