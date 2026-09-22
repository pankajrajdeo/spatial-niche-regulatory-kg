---
title: "enable_capture_offload"
description: "Whether FilesystemMiddleware may use capture-at-source offload for execute."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/enable_capture_offload"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, enable_capture_offload]
---

# enable_capture_offload

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/enable_capture_offload)

Whether `FilesystemMiddleware` may use capture-at-source offload for `execute`.

When `True`, large `execute` output is captured to a file in the sandbox and
only a preview is returned, avoiding a round-trip back through the agent
process. Defaults to `False` (opt-in) because the capture wrapper's shell and
coreutils assumptions are not guaranteed on every sandbox image; subclasses
known to be compatible set it to `True`. When `False`, `execute_with_offload`
runs the command unwrapped and the middleware falls back to inline execution
plus generic eviction.

## Signature

```python
enable_capture_offload: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1433)
