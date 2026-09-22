---
title: "BackendProtocol"
description: "Protocol for pluggable memory backends (single, unified)."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol]
---

# BackendProtocol

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol)

Protocol for pluggable memory backends (single, unified).

Backends can store files in different locations (state, filesystem,
database, etc.) and provide a uniform interface for file operations.

File operations (`grep`, `glob`, `ls`, `read`, etc.) live on this base
protocol rather than only on `SandboxBackendProtocol` because not every
backend has a shell. `StateBackend` and `StoreBackend` store files in
in-memory state or a remote store with no process to exec into, so they
implement `grep`/`glob` in pure Python and have no `execute` at all.
Even on shell-capable backends, the tools are not just convenience
wrappers around `execute`: they enforce literal-only matching (not
regex), return structured `GrepResult`/`GlobResult` objects, support
`max_count` truncation, and pass through filesystem permission rules —
none of which raw `execute` + shell `grep`/`find` provides. Agent-facing
prompt guidance should therefore recommend these tools only when they
are actually registered, and never assume a shell is available as a
fallback.

All file data is represented as dicts with the following structure:

```python
{
    "content": str,  # Text content (utf-8) or base64-encoded binary
    "encoding": str,  # "utf-8" for text, "base64" for binary data
    "created_at": str,  # ISO format timestamp
    "modified_at": str,  # ISO format timestamp
}
```

## Signature

```python
BackendProtocol()
```

## Extends

- `abc.ABC`

## Methods

- [`ls()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/ls)
- [`als()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/als)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/read)
- [`aread()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/aread)
- [`grep()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/grep)
- [`agrep()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/agrep)
- [`glob()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/glob)
- [`aglob()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/aglob)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/write)
- [`awrite()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/awrite)
- [`edit()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/edit)
- [`aedit()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/aedit)
- [`delete()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/delete)
- [`adelete()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/adelete)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/upload_files)
- [`aupload_files()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/aupload_files)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/download_files)
- [`adownload_files()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/adownload_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L404)
