---
title: "StateBackend"
description: "Backend that stores files in agent state (ephemeral)."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend]
---

# StateBackend

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend)

Backend that stores files in agent state (ephemeral).

Uses LangGraph's state management and checkpointing. Files persist within
a conversation thread but not across threads. State is automatically
checkpointed after each agent step.

Reads and writes go through LangGraph's `CONFIG_KEY_READ` /
`CONFIG_KEY_SEND` so that state updates are applied as channel writes
to the `files` state key.

## Signature

```python
StateBackend(
    self,
)
```

## Extends

- `BackendProtocol`

## Constructors

```python
__init__(
    self,
) -> None
```

## Methods

- [`ls()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/ls)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/read)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/write)
- [`edit()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/edit)
- [`delete()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/delete)
- [`grep()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/grep)
- [`glob()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/glob)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/upload_files)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/download_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/state.py#L38)
