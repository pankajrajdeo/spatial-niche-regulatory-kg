---
title: "aexecute_with_offload"
description: "Async version of execute_with_offload, delegating to aexecute."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aexecute_with_offload"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, aexecute_with_offload]
---

# aexecute_with_offload

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aexecute_with_offload)

Async version of `execute_with_offload`, delegating to `aexecute`.

## Signature

```python
aexecute_with_offload(
    self,
    command: str,
    capture_path: str,
    *,
    max_inline_bytes: int,
    max_capture_bytes: int | None = None,
    timeout: int | None = None,
) -> ExecuteOffloadResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1497)
