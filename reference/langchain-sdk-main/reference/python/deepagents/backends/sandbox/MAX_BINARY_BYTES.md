---
title: "MAX_BINARY_BYTES"
description: "Maximum size of a binary file returned by read() as base64."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/MAX_BINARY_BYTES"
category: "reference"
tags: [reference, deepagents, backends, sandbox, max_binary_bytes]
---

# MAX_BINARY_BYTES

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/MAX_BINARY_BYTES)

Maximum size of a binary file returned by `read()` as base64.

Files exceeding this size return a `Binary file exceeds maximum preview size`
error rather than being base64-encoded in full. Backends overriding `read()`
should import and reuse this constant to stay in sync with the base
implementation. Kept in lockstep with the `MAX_BINARY_BYTES` literal in
`_READ_COMMAND_TEMPLATE` (asserted by `test_read_constants_match_template`).

## Signature

```python
MAX_BINARY_BYTES: Final = 500 * 1024
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L469)
