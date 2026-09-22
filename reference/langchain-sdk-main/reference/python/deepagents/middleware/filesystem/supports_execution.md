---
title: "supports_execution"
description: "Check if a backend supports command execution."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/supports_execution"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, supports_execution]
---

# supports_execution

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/supports_execution)

Check if a backend supports command execution.

For [`CompositeBackend`][deepagents.backends.composite.CompositeBackend],
checks if the default backend supports execution.
For other backends, checks if they implement
[`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol].

## Signature

```python
supports_execution(
    backend: BackendProtocol,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `backend` | `BackendProtocol` | Yes | The backend to check. |

## Returns

`bool`

True if the backend supports execution, False otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L1568)
