---
title: "protocol"
description: "Protocol definition for pluggable memory backends."
source: "https://reference.langchain.com/python/deepagents/backends/protocol"
category: "reference"
tags: [reference, deepagents, backends, protocol]
---

# protocol

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol)

Protocol definition for pluggable memory backends.

This module defines the `BackendProtocol` that all backend implementations
must follow. Backends can store files in different locations (state, filesystem,
database, etc.) and provide a uniform interface for file operations.

## Properties

- `logger`
- `DEFAULT_GREP_TIMEOUT`
- `ASYNC_GREP_TIMEOUT`
- `ASYNC_GLOB_TIMEOUT`
- `FileOperationError`
- `FILE_NOT_FOUND`
- `PERMISSION_DENIED`
- `IS_DIRECTORY`
- `INVALID_PATH`
- `GlobTruncationReason`

## Methods

- [`execute_accepts_timeout()`](https://reference.langchain.com/python/deepagents/backends/protocol/execute_accepts_timeout)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py)
