---
title: "ASYNC_GLOB_TIMEOUT"
description: "Timeout in seconds for a sandbox glob round-trip."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ASYNC_GLOB_TIMEOUT"
category: "reference"
tags: [reference, deepagents, backends, protocol, async_glob_timeout]
---

# ASYNC_GLOB_TIMEOUT

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ASYNC_GLOB_TIMEOUT)

Timeout in seconds for a sandbox glob round-trip.

The remote script bounds its own walk (`TIME_BUDGET` in `sandbox.py`), but that
covers neither interpreter startup, the sandbox round-trip, nor transferring up
to `MAX_MATCHES` records. Without an outer bound a wedged sandbox hangs the
caller indefinitely.

## Signature

```python
ASYNC_GLOB_TIMEOUT: Final = 30
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L30)
