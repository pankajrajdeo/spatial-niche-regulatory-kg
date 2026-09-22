---
title: "CompositeBackend"
description: "Routes file operations to different backends by path prefix."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend]
---

# CompositeBackend

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend)

Routes file operations to different backends by path prefix.

Matches paths against route prefixes (longest first) and delegates to the
corresponding backend. Unmatched paths use the default backend.

## Signature

```python
CompositeBackend(
    self,
    default: BackendProtocol | StateBackend,
    routes: dict[str, BackendProtocol],
    *,
    artifacts_root: str = '/',
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `default` | `BackendProtocol \| StateBackend` | Yes | Backend for paths that don't match any route. |
| `routes` | `dict[str, BackendProtocol]` | Yes | Map of path prefixes to backends.  Prefixes must start with `"/"` and should end with `"/"` (e.g., `"/memories/"`). |
| `artifacts_root` | `str` | No | Root path for artifacts, such as messages offloaded by middleware.  Defaults to `"/"`. (default: `'/'`) |

## Extends

- `BackendProtocol`

## Constructors

```python
__init__(
    self,
    default: BackendProtocol | StateBackend,
    routes: dict[str, BackendProtocol],
    *,
    artifacts_root: str = '/',
) -> None
```

| Name | Type |
|------|------|
| `default` | `BackendProtocol \| StateBackend` |
| `routes` | `dict[str, BackendProtocol]` |
| `artifacts_root` | `str` |

## Properties

- `default`
- `routes`
- `sorted_routes`
- `artifacts_root`

## Methods

- [`ls()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/ls)
- [`als()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/als)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/read)
- [`aread()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/aread)
- [`grep()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/grep)
- [`agrep()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/agrep)
- [`glob()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/glob)
- [`aglob()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/aglob)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/write)
- [`awrite()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/awrite)
- [`edit()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/edit)
- [`aedit()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/aedit)
- [`delete()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/delete)
- [`adelete()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/adelete)
- [`execute()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/execute)
- [`aexecute()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/aexecute)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/upload_files)
- [`aupload_files()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/aupload_files)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/download_files)
- [`adownload_files()`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/adownload_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/composite.py#L228)
