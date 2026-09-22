---
title: "execute_with_offload"
description: "Run command, offloading large output to a file in the sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/execute_with_offload"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, execute_with_offload]
---

# execute_with_offload

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/execute_with_offload)

Run `command`, offloading large output to a file in the sandbox.

Captures the command's combined output: returned inline when it is at or
below `max_inline_bytes`, otherwise left at `capture_path` (so the caller
can surface a `read_file` pointer) with only a head/tail preview returned.
Captured output is hard-capped at `max_capture_bytes` (default
`_EXECUTE_CAPTURE_MAX_BYTES`) without killing the command, so the exit
code is preserved. When `enable_capture_offload` is `False`, the command
runs unwrapped and the full output is returned (`offloaded=False`), so
callers can fall back to their own handling (e.g. generic eviction).

## Signature

```python
execute_with_offload(
    self,
    command: str,
    capture_path: str,
    *,
    max_inline_bytes: int,
    max_capture_bytes: int | None = None,
    timeout: int | None = None,
) -> ExecuteOffloadResult
```

## Returns

`ExecuteOffloadResult`

An `ExecuteOffloadResult`. `offloaded=True` when the result was left

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1464)
