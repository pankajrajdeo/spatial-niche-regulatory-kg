---
title: "LangSmithSandbox"
description: "LangSmith sandbox implementation conforming to [SandboxBackendProtocol][deepagents.backends.protocol.SandboxBackendProtocol]."
source: "https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox"
category: "reference"
tags: [reference, deepagents, backends, langsmith, langsmithsandbox]
---

# LangSmithSandbox

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox)

LangSmith sandbox implementation conforming to [`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol].

## Signature

```python
LangSmithSandbox(
    self,
    sandbox: Sandbox,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sandbox` | `Sandbox` | Yes | LangSmith Sandbox instance to wrap. |

## Extends

- `BaseSandbox`

## Constructors

```python
__init__(
    self,
    sandbox: Sandbox,
) -> None
```

| Name | Type |
|------|------|
| `sandbox` | `Sandbox` |

## Properties

- `enable_capture_offload`
- `id`

## Methods

- [`execute()`](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/execute)
- [`aexecute()`](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/aexecute)
- [`aclose()`](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/aclose)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/write)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/read)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/download_files)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/upload_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/langsmith.py#L56)
