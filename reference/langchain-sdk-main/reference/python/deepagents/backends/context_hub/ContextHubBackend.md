---
title: "ContextHubBackend"
description: "Backend that stores files in a LangSmith Hub agent repo (persistent)."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend]
---

# ContextHubBackend

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend)

Backend that stores files in a LangSmith Hub agent repo (persistent).

## Signature

```python
ContextHubBackend(
    self,
    identifier: str,
    *,
    client: Client | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `identifier` | `str` | Yes | Hub agent repo, as `"owner/name"` or `"-/name"`. |
| `client` | `Client \| None` | No | LangSmith client. Defaults to `Client()`. (default: `None`) |

## Extends

- `BackendProtocol`

## Constructors

```python
__init__(
    self,
    identifier: str,
    *,
    client: Client | None = None,
) -> None
```

| Name | Type |
|------|------|
| `identifier` | `str` |
| `client` | `Client \| None` |

## Methods

- [`get_linked_entries()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/get_linked_entries)
- [`has_prior_commits()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/has_prior_commits)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/read)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/write)
- [`edit()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/edit)
- [`delete()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/delete)
- [`ls()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/ls)
- [`grep()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/grep)
- [`glob()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/glob)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/upload_files)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/download_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/context_hub.py#L98)
