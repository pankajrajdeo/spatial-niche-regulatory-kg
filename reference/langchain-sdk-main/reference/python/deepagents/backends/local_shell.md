---
title: "local_shell"
description: "LocalShellBackend: Filesystem backend with unrestricted local shell execution."
source: "https://reference.langchain.com/python/deepagents/backends/local_shell"
category: "reference"
tags: [reference, deepagents, backends, local_shell]
---

# local_shell

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/local_shell)

`LocalShellBackend`: Filesystem backend with unrestricted local shell execution.

This backend extends `FilesystemBackend` to add shell command execution on
the local host system. It provides NO sandboxing or isolation - all operations
run directly on the host machine with full system access.

## Properties

- `DEFAULT_EXECUTE_TIMEOUT`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/local_shell.py)
