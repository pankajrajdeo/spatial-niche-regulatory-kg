---
title: "sandbox"
description: "Base sandbox implementation."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox"
category: "reference"
tags: [reference, deepagents, backends, sandbox]
---

# sandbox

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox)

Base sandbox implementation.

[`BaseSandbox`][deepagents.backends.sandbox.BaseSandbox] implements
[`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol].

File listing, grep, glob, and read use shell commands via `execute()`. Write
delegates content transfer to `upload_files()`. Edit uses server-side `execute()`
for payloads under `_EDIT_INLINE_MAX_BYTES` and falls back to uploading old/new
strings as temp files with a server-side replace script for larger ones.

Concrete subclasses implement `execute()` and `upload_files()`; all other
operations are derived from those.

## Properties

- `ASYNC_GLOB_TIMEOUT`
- `ASYNC_GREP_TIMEOUT`
- `GlobTruncationReason`
- `EMPTY_OLD_STRING_ERROR`
- `logger`
- `MAX_BINARY_BYTES`
- `MAX_OUTPUT_BYTES`
- `TRUNCATION_MSG`

## Methods

- [`execute_accepts_timeout()`](https://reference.langchain.com/python/deepagents/backends/sandbox/execute_accepts_timeout)
- [`normalize_read_bounds()`](https://reference.langchain.com/python/deepagents/backends/sandbox/normalize_read_bounds)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py)
