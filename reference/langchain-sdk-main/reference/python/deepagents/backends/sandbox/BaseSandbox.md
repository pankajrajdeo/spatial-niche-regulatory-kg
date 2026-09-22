---
title: "BaseSandbox"
description: "Base sandbox implementation with execute() as the core abstract method."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox]
---

# BaseSandbox

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox)

Base sandbox implementation with `execute()` as the core abstract method.

This class provides default implementations for all protocol methods.
File listing, grep, and glob use shell commands via `execute()`. Read uses
a server-side Python script via `execute()` for paginated access. Write
delegates content transfer to `upload_files()`. Edit uses a server-side
script for small payloads and uploads old/new strings as temp files with
a server-side replace for large ones.

!!! note

    `BaseSandbox` does not reduce or partition the trust boundary of
    `execute()`. Its helper methods are convenience wrappers built on top of
    the subclass-provided command-execution primitive and assume callers who
    can use `BaseSandbox` already have whatever shell-execution capability
    that backend exposes.

Subclasses must implement `execute()`, `upload_files()`, `download_files()`,
and the `id` property.

## Signature

```python
BaseSandbox()
```

## Extends

- `SandboxBackendProtocol`
- `ABC`

## Properties

- `enable_capture_offload`
- `id`

## Methods

- [`execute()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/execute)
- [`execute_with_offload()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/execute_with_offload)
- [`aexecute_with_offload()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aexecute_with_offload)
- [`ls()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/ls)
- [`als()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/als)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/read)
- [`aread()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aread)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/write)
- [`awrite()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/awrite)
- [`edit()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/edit)
- [`aedit()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aedit)
- [`delete()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/delete)
- [`grep()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/grep)
- [`agrep()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/agrep)
- [`glob()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/glob)
- [`aglob()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aglob)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/upload_files)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/download_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1411)
