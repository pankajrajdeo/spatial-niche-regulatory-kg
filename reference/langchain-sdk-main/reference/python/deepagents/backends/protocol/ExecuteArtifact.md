---
title: "ExecuteArtifact"
description: "Machine-readable metadata attached to an execute tool result."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteArtifact"
category: "reference"
tags: [reference, deepagents, backends, protocol, executeartifact]
---

# ExecuteArtifact

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteArtifact)

Machine-readable metadata attached to an `execute` tool result.

Carried on `ToolMessage.artifact` alongside the model-facing `content`, so
callers can react to shell failures. `artifact` is `None` instead when no
command ran -- a validation or unsupported-backend error, where
`ToolMessage.status` is `"error"`.

Note that `status` is `"success"` for any command that ran, including one
that exited non-zero: the model is expected to read the output and decide
what to do. Use `exit_code`, not `status`, to detect command failure.

## Signature

```python
ExecuteArtifact()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    exit_code: NotRequired[int],
)
```

| Name | Type |
|------|------|
| `exit_code` | `NotRequired[int]` |

## Properties

- `exit_code`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L830)
