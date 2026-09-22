---
title: "HostExecutionPolicy"
description: "Run the shell directly on the host process."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_execution/HostExecutionPolicy"
category: "reference"
tags: [reference, langchain, agents, middleware, execution, hostexecutionpolicy]
---

# HostExecutionPolicy

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_execution/HostExecutionPolicy)

Run the shell directly on the host process.

This policy is best suited for trusted or single-tenant environments (CI jobs,
developer workstations, pre-sandboxed containers) where the agent must access the
host filesystem and tooling without additional isolation. Enforces optional CPU and
memory limits to prevent runaway commands but offers **no** filesystem or network
sandboxing; commands can modify anything the process user can reach.

On Linux platforms resource limits are applied with `resource.prlimit` after the
shell starts. On macOS, where `prlimit` is unavailable, limits are set in a
`preexec_fn` before `exec`. In both cases the shell runs in its own process group
so timeouts can terminate the full subtree.

## Signature

```python
HostExecutionPolicy(
    self,
    command_timeout: float = 30.0,
    startup_timeout: float = 30.0,
    termination_timeout: float = 10.0,
    max_output_lines: int = 100,
    max_output_bytes: int | None = None,
    cpu_time_seconds: int | None = None,
    memory_bytes: int | None = None,
    create_process_group: bool = True,
)
```

## Extends

- `BaseExecutionPolicy`

## Constructors

```python
__init__(
    self,
    command_timeout: float = 30.0,
    startup_timeout: float = 30.0,
    termination_timeout: float = 10.0,
    max_output_lines: int = 100,
    max_output_bytes: int | None = None,
    cpu_time_seconds: int | None = None,
    memory_bytes: int | None = None,
    create_process_group: bool = True,
) -> None
```

| Name | Type |
|------|------|
| `command_timeout` | `float` |
| `startup_timeout` | `float` |
| `termination_timeout` | `float` |
| `max_output_lines` | `int` |
| `max_output_bytes` | `int \| None` |
| `cpu_time_seconds` | `int \| None` |
| `memory_bytes` | `int \| None` |
| `create_process_group` | `bool` |

## Properties

- `cpu_time_seconds`
- `memory_bytes`
- `create_process_group`

## Methods

- [`spawn()`](https://reference.langchain.com/python/langchain/agents/middleware/_execution/HostExecutionPolicy/spawn)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_execution.py#L91)
