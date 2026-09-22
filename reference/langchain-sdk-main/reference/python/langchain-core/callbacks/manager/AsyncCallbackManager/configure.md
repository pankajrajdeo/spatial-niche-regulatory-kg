---
title: "configure"
description: "Configure the async callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/configure"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanager, configure]
---

# configure

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/configure)

Configure the async callback manager.

## Signature

```python
configure(
    cls,
    inheritable_callbacks: Callbacks = None,
    local_callbacks: Callbacks = None,
    verbose: bool = False,
    inheritable_tags: list[str] | None = None,
    local_tags: list[str] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
    local_metadata: dict[str, Any] | None = None,
    *,
    langsmith_inheritable_metadata: Mapping[str, Any] | None = None,
    langsmith_inheritable_tags: list[str] | None = None,
) -> AsyncCallbackManager
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `inheritable_callbacks` | `Callbacks` | No | The inheritable callbacks. (default: `None`) |
| `local_callbacks` | `Callbacks` | No | The local callbacks. (default: `None`) |
| `verbose` | `bool` | No | Whether to enable verbose mode. (default: `False`) |
| `inheritable_tags` | `list[str] \| None` | No | The inheritable tags. (default: `None`) |
| `local_tags` | `list[str] \| None` | No | The local tags. (default: `None`) |
| `inheritable_metadata` | `dict[str, Any] \| None` | No | The inheritable metadata. (default: `None`) |
| `local_metadata` | `dict[str, Any] \| None` | No | The local metadata. (default: `None`) |
| `langsmith_inheritable_metadata` | `Mapping[str, Any] \| None` | No | Default inheritable metadata applied to any `LangChainTracer` handlers via `set_defaults`. (default: `None`) |
| `langsmith_inheritable_tags` | `list[str] \| None` | No | Default inheritable tags applied to any `LangChainTracer` handlers via `set_defaults`. (default: `None`) |

## Returns

`AsyncCallbackManager`

The configured async callback manager.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L2211)
