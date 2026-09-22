---
title: "BaseExecutionPolicy"
description: "Configuration contract for persistent shell sessions."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_execution/BaseExecutionPolicy"
category: "reference"
tags: [reference, langchain, agents, middleware, execution, baseexecutionpolicy]
---

# BaseExecutionPolicy

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_execution/BaseExecutionPolicy)

Configuration contract for persistent shell sessions.

Concrete subclasses encapsulate how a shell process is launched and constrained.

Each policy documents its security guarantees and the operating environments in
which it is appropriate. Use `HostExecutionPolicy` for trusted, same-host execution;
`CodexSandboxExecutionPolicy` when the Codex CLI sandbox is available and you want
additional syscall restrictions; and `DockerExecutionPolicy` for container-level
isolation using Docker.

## Signature

```python
BaseExecutionPolicy(
    self,
    command_timeout: float = 30.0,
    startup_timeout: float = 30.0,
    termination_timeout: float = 10.0,
    max_output_lines: int = 100,
    max_output_bytes: int | None = None,
)
```

## Extends

- `abc.ABC`

## Constructors

```python
__init__(
    self,
    command_timeout: float = 30.0,
    startup_timeout: float = 30.0,
    termination_timeout: float = 10.0,
    max_output_lines: int = 100,
    max_output_bytes: int | None = None,
) -> None
```

| Name | Type |
|------|------|
| `command_timeout` | `float` |
| `startup_timeout` | `float` |
| `termination_timeout` | `float` |
| `max_output_lines` | `int` |
| `max_output_bytes` | `int \| None` |

## Properties

- `command_timeout`
- `startup_timeout`
- `termination_timeout`
- `max_output_lines`
- `max_output_bytes`

## Methods

- [`spawn()`](https://reference.langchain.com/python/langchain/agents/middleware/_execution/BaseExecutionPolicy/spawn)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_execution.py#L56)
