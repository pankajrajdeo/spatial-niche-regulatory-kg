---
title: "DockerExecutionPolicy"
description: "Run the shell inside a dedicated Docker container."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_execution/DockerExecutionPolicy"
category: "reference"
tags: [reference, langchain, agents, middleware, execution, dockerexecutionpolicy]
---

# DockerExecutionPolicy

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_execution/DockerExecutionPolicy)

Run the shell inside a dedicated Docker container.

Choose this policy when commands originate from untrusted users or you require
strong isolation between sessions. By default the workspace is bind-mounted only
when it refers to an existing non-temporary directory; ephemeral sessions run
without a mount to minimise host exposure. The container's network namespace is
disabled by default (`--network none`) and you can enable further hardening via
`read_only_rootfs` and `user`.

The security guarantees depend on your Docker daemon configuration. Run the agent on
a host where Docker is locked down (rootless mode, AppArmor/SELinux, etc.) and
review any additional volumes or capabilities passed through `extra_run_args`. The
default image is `python:3.12-alpine3.19`; supply a custom image if you need
preinstalled tooling.

## Signature

```python
DockerExecutionPolicy(
    self,
    command_timeout: float = 30.0,
    startup_timeout: float = 30.0,
    termination_timeout: float = 10.0,
    max_output_lines: int = 100,
    max_output_bytes: int | None = None,
    binary: str = 'docker',
    image: str = 'python:3.12-alpine3.19',
    remove_container_on_exit: bool = True,
    network_enabled: bool = False,
    extra_run_args: Sequence[str] | None = None,
    memory_bytes: int | None = None,
    cpu_time_seconds: typing.Any | None = None,
    cpus: str | None = None,
    read_only_rootfs: bool = False,
    user: str | None = None,
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
    binary: str = 'docker',
    image: str = 'python:3.12-alpine3.19',
    remove_container_on_exit: bool = True,
    network_enabled: bool = False,
    extra_run_args: Sequence[str] | None = None,
    memory_bytes: int | None = None,
    cpu_time_seconds: typing.Any | None = None,
    cpus: str | None = None,
    read_only_rootfs: bool = False,
    user: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `command_timeout` | `float` |
| `startup_timeout` | `float` |
| `termination_timeout` | `float` |
| `max_output_lines` | `int` |
| `max_output_bytes` | `int \| None` |
| `binary` | `str` |
| `image` | `str` |
| `remove_container_on_exit` | `bool` |
| `network_enabled` | `bool` |
| `extra_run_args` | `Sequence[str] \| None` |
| `memory_bytes` | `int \| None` |
| `cpu_time_seconds` | `typing.Any \| None` |
| `cpus` | `str \| None` |
| `read_only_rootfs` | `bool` |
| `user` | `str \| None` |

## Properties

- `binary`
- `image`
- `remove_container_on_exit`
- `network_enabled`
- `extra_run_args`
- `memory_bytes`
- `cpu_time_seconds`
- `cpus`
- `read_only_rootfs`
- `user`

## Methods

- [`spawn()`](https://reference.langchain.com/python/langchain/agents/middleware/_execution/DockerExecutionPolicy/spawn)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_execution.py#L266)
