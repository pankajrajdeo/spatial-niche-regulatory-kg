---
title: "ShellToolMiddleware"
description: "Middleware that registers a persistent shell tool for agents."
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, shelltoolmiddleware]
---

# ShellToolMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware)

Middleware that registers a persistent shell tool for agents.

The middleware exposes a single long-lived shell session. Use the execution policy
to match your deployment's security posture:

* `HostExecutionPolicy` – full host access; best for trusted environments where the
    agent already runs inside a container or VM that provides isolation.
* `CodexSandboxExecutionPolicy` – reuses the Codex CLI sandbox for additional
    syscall/filesystem restrictions when the CLI is available.
* `DockerExecutionPolicy` – launches a separate Docker container for each agent run,
    providing harder isolation, optional read-only root filesystems, and user
    remapping.

When no policy is provided the middleware defaults to `HostExecutionPolicy`.

## Signature

```python
ShellToolMiddleware(
    self,
    workspace_root: str | Path | None = None,
    *,
    startup_commands: tuple[str, ...] | list[str] | str | None = None,
    shutdown_commands: tuple[str, ...] | list[str] | str | None = None,
    execution_policy: BaseExecutionPolicy | None = None,
    redaction_rules: tuple[RedactionRule, ...] | list[RedactionRule] | None = None,
    tool_description: str | None = None,
    tool_name: str = SHELL_TOOL_NAME,
    shell_command: Sequence[str] | str | None = None,
    env: Mapping[str, Any] | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspace_root` | `str \| Path \| None` | No | Base directory for the shell session.  If omitted, a temporary directory is created when the agent starts and removed when it ends. (default: `None`) |
| `startup_commands` | `tuple[str, ...] \| list[str] \| str \| None` | No | Optional commands executed sequentially after the session starts. (default: `None`) |
| `shutdown_commands` | `tuple[str, ...] \| list[str] \| str \| None` | No | Optional commands executed before the session shuts down. (default: `None`) |
| `execution_policy` | `BaseExecutionPolicy \| None` | No | Execution policy controlling timeouts, output limits, and resource configuration.  Defaults to `HostExecutionPolicy` for native execution. (default: `None`) |
| `redaction_rules` | `tuple[RedactionRule, ...] \| list[RedactionRule] \| None` | No | Optional redaction rules to sanitize command output before returning it to the model.  !!! warning     Redaction rules are applied post execution and do not prevent     exfiltration of secrets or sensitive data when using     `HostExecutionPolicy`. (default: `None`) |
| `tool_description` | `str \| None` | No | Optional override for the registered shell tool description. (default: `None`) |
| `tool_name` | `str` | No | Name for the registered shell tool.  Defaults to `"shell"`. (default: `SHELL_TOOL_NAME`) |
| `shell_command` | `Sequence[str] \| str \| None` | No | Optional shell executable (string) or argument sequence used to launch the persistent session.  Defaults to an implementation-defined bash command. (default: `None`) |
| `env` | `Mapping[str, Any] \| None` | No | Optional environment variables to supply to the shell session.  Values are coerced to strings before command execution. If omitted, the session inherits the parent process environment. (default: `None`) |

## Extends

- `AgentMiddleware[ShellToolState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    workspace_root: str | Path | None = None,
    *,
    startup_commands: tuple[str, ...] | list[str] | str | None = None,
    shutdown_commands: tuple[str, ...] | list[str] | str | None = None,
    execution_policy: BaseExecutionPolicy | None = None,
    redaction_rules: tuple[RedactionRule, ...] | list[RedactionRule] | None = None,
    tool_description: str | None = None,
    tool_name: str = SHELL_TOOL_NAME,
    shell_command: Sequence[str] | str | None = None,
    env: Mapping[str, Any] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `workspace_root` | `str \| Path \| None` |
| `startup_commands` | `tuple[str, ...] \| list[str] \| str \| None` |
| `shutdown_commands` | `tuple[str, ...] \| list[str] \| str \| None` |
| `execution_policy` | `BaseExecutionPolicy \| None` |
| `redaction_rules` | `tuple[RedactionRule, ...] \| list[RedactionRule] \| None` |
| `tool_description` | `str \| None` |
| `tool_name` | `str` |
| `shell_command` | `Sequence[str] \| str \| None` |
| `env` | `Mapping[str, Any] \| None` |

## Properties

- `state_schema`
- `tools`

## Methods

- [`before_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/abefore_agent)
- [`after_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/after_agent)
- [`aafter_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/aafter_agent)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L518)
