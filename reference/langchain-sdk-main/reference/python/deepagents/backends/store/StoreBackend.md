---
title: "StoreBackend"
description: "Backend that stores files in LangGraph's BaseStore (persistent)."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend]
---

# StoreBackend

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend)

Backend that stores files in LangGraph's BaseStore (persistent).

Uses LangGraph's Store for persistent, cross-conversation storage.
Files are organized via namespaces and persist across all threads.

Files are scoped by the caller-supplied `namespace` factory (e.g. per-user
or per-assistant isolation).

## Signature

```python
StoreBackend(
    self,
    *,
    namespace: NamespaceFactory,
    store: BaseStore | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | `NamespaceFactory` | Yes | Callable that receives a `Runtime` and returns a namespace tuple for scoping store operations. Wildcards (`*`) are forbidden. |
| `store` | `BaseStore \| None` | No | Optional `BaseStore` instance. When provided, this store is used directly. When `None`, the store is obtained at call time via `get_store()`, which requires a LangGraph graph execution context. (default: `None`) |

## Extends

- `BackendProtocol`

## Constructors

```python
__init__(
    self,
    *,
    namespace: NamespaceFactory,
    store: BaseStore | None = None,
) -> None
```

| Name | Type |
|------|------|
| `namespace` | `NamespaceFactory` |
| `store` | `BaseStore \| None` |

## Methods

- [`ls()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/ls)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/read)
- [`aread()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aread)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/write)
- [`awrite()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/awrite)
- [`edit()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/edit)
- [`aedit()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aedit)
- [`delete()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/delete)
- [`adelete()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/adelete)
- [`grep()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/grep)
- [`glob()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/glob)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/upload_files)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/download_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L90)
