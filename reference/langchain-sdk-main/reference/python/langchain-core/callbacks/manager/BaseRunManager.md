---
title: "BaseRunManager"
description: "Base class for run manager (a bound callback manager)."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/BaseRunManager"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, baserunmanager]
---

# BaseRunManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/BaseRunManager)

Base class for run manager (a bound callback manager).

## Signature

```python
BaseRunManager(
    self,
    *,
    run_id: UUID,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler],
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | `UUID` | Yes | The ID of the run. |
| `handlers` | `list[BaseCallbackHandler]` | Yes | The list of handlers. |
| `inheritable_handlers` | `list[BaseCallbackHandler]` | Yes | The list of inheritable handlers. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The list of tags. (default: `None`) |
| `inheritable_tags` | `list[str] \| None` | No | The list of inheritable tags. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata. (default: `None`) |
| `inheritable_metadata` | `dict[str, Any] \| None` | No | The inheritable metadata. (default: `None`) |

## Extends

- `RunManagerMixin`

## Constructors

```python
__init__(
    self,
    *,
    run_id: UUID,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler],
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `run_id` | `UUID` |
| `handlers` | `list[BaseCallbackHandler]` |
| `inheritable_handlers` | `list[BaseCallbackHandler]` |
| `parent_run_id` | `UUID \| None` |
| `tags` | `list[str] \| None` |
| `inheritable_tags` | `list[str] \| None` |
| `metadata` | `dict[str, Any] \| None` |
| `inheritable_metadata` | `dict[str, Any] \| None` |

## Properties

- `run_id`
- `handlers`
- `inheritable_handlers`
- `parent_run_id`
- `tags`
- `inheritable_tags`
- `metadata`
- `inheritable_metadata`

## Methods

- [`get_noop_manager()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/BaseRunManager/get_noop_manager)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L490)
