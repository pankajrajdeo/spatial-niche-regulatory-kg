---
title: "BaseCallbackManager"
description: "Base callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackmanager]
---

# BaseCallbackManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager)

Base callback manager.

## Signature

```python
BaseCallbackManager(
    self,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler] | None = None,
    parent_run_id: UUID | None = None,
    *,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `handlers` | `list[BaseCallbackHandler]` | Yes | The handlers. |
| `inheritable_handlers` | `list[BaseCallbackHandler] \| None` | No | The inheritable handlers. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The parent run ID. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `inheritable_tags` | `list[str] \| None` | No | The inheritable tags. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata. (default: `None`) |
| `inheritable_metadata` | `dict[str, Any] \| None` | No | The inheritable metadata. (default: `None`) |

## Extends

- `CallbackManagerMixin`

## Constructors

```python
__init__(
    self,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler] | None = None,
    parent_run_id: UUID | None = None,
    *,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `handlers` | `list[BaseCallbackHandler]` |
| `inheritable_handlers` | `list[BaseCallbackHandler] \| None` |
| `parent_run_id` | `UUID \| None` |
| `tags` | `list[str] \| None` |
| `inheritable_tags` | `list[str] \| None` |
| `metadata` | `dict[str, Any] \| None` |
| `inheritable_metadata` | `dict[str, Any] \| None` |

## Properties

- `handlers`
- `inheritable_handlers`
- `parent_run_id`
- `tags`
- `inheritable_tags`
- `metadata`
- `inheritable_metadata`
- `is_async`

## Methods

- [`copy()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/copy)
- [`merge()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/merge)
- [`add_handler()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/add_handler)
- [`remove_handler()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/remove_handler)
- [`set_handlers()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/set_handlers)
- [`set_handler()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/set_handler)
- [`add_tags()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/add_tags)
- [`remove_tags()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/remove_tags)
- [`add_metadata()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/add_metadata)
- [`remove_metadata()`](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/remove_metadata)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L1004)
