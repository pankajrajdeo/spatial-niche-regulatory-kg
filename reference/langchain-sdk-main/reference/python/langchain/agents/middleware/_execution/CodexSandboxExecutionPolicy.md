---
title: "CodexSandboxExecutionPolicy"
description: "Launch the shell through the Codex CLI sandbox."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_execution/CodexSandboxExecutionPolicy"
category: "reference"
tags: [reference, langchain, agents, middleware, execution, codexsandboxexecutionpolicy]
---

# CodexSandboxExecutionPolicy

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_execution/CodexSandboxExecutionPolicy)

Launch the shell through the Codex CLI sandbox.

Ideal when you have the Codex CLI installed and want the additional syscall and
filesystem restrictions provided by Anthropic's Seatbelt (macOS) or Landlock/seccomp
(Linux) profiles. Commands still run on the host, but within the sandbox requested by
the CLI. If the Codex binary is unavailable or the runtime lacks the required
kernel features (e.g., Landlock inside some containers), process startup fails with a
`RuntimeError`.

Configure sandbox behavior via `config_overrides` to align with your Codex CLI
profile. This policy does not add its own resource limits; combine it with
host-level guards (cgroups, container resource limits) as needed.

## Signature

```python
CodexSandboxExecutionPolicy(
    self,
    command_timeout: float = 30.0,
    startup_timeout: float = 30.0,
    termination_timeout: float = 10.0,
    max_output_lines: int = 100,
    max_output_bytes: int | None = None,
    binary: str = 'codex',
    platform: typing.Literal['auto', 'macos', 'linux'] = 'auto',
    config_overrides: Mapping[str, typing.Any] = dict(),
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
    binary: str = 'codex',
    platform: typing.Literal['auto', 'macos', 'linux'] = 'auto',
    config_overrides: Mapping[str, typing.Any] = dict(),
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
| `platform` | `typing.Literal['auto', 'macos', 'linux']` |
| `config_overrides` | `Mapping[str, typing.Any]` |

## Properties

- `binary`
- `platform`
- `config_overrides`

## Methods

- [`spawn()`](https://reference.langchain.com/python/langchain/agents/middleware/_execution/CodexSandboxExecutionPolicy/spawn)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_execution.py#L190)
