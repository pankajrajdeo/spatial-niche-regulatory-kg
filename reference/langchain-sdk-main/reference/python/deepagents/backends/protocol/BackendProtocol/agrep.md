---
title: "agrep"
description: "Async version of grep."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/agrep"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, agrep]
---

# agrep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/agrep)

Async version of `grep`.

Wraps the sync call with an async timeout as a safety net. The timeout
bounds how long the caller waits; it does not stop the worker thread
created by `asyncio.to_thread`.

`max_count` is forwarded when the concrete `grep` accepts it (so the
search can bound itself); backends that don't accept it run uncapped and
are trimmed afterward. Either way the return value is always passed
through `_apply_grep_max_count` (a no-op when already within the cap), so
callers get the same guarantee regardless of which path runs.

## Signature

```python
agrep(
    self,
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
) -> GrepResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L558)
