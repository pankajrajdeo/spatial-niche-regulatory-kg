---
title: "FilesystemMiddleware"
description: "Middleware for providing filesystem and optional execution tools to an agent."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware]
---

# FilesystemMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware)

Middleware for providing filesystem and optional execution tools to an agent.

This middleware adds filesystem tools to the agent: `ls`, `read_file`, `write_file`,
`edit_file`, `glob`, and `grep`.

Files can be stored using any backend that implements the
[`BackendProtocol`][deepagents.backends.protocol.BackendProtocol].

If the backend implements
[`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol],
an `execute` tool is also added for running shell commands. Its results carry
[`ExecuteArtifact`][deepagents.backends.protocol.ExecuteArtifact] metadata on
`ToolMessage.artifact`.

This middleware also automatically evicts large tool results to the file system when
they exceed a token threshold, preventing context window saturation.

## Signature

```python
FilesystemMiddleware(
    self,
    *,
    backend: BackendProtocol | None = None,
    system_prompt: str | None = None,
    custom_tool_descriptions: Mapping[str, str] | None = None,
    tool_token_limit_before_evict: int | None = 20000,
    human_message_token_limit_before_evict: int | None = 50000,
    max_execute_timeout: int = 3600,
    grep_max_count: int | None = 1000,
    tools: list[FsToolName] | Literal['all'] | None = None,
    _permissions: list[FilesystemPermission] | None = None,
)
```

## Description

**Example:**

```python
from deepagents.middleware.filesystem import FilesystemMiddleware
from deepagents.backends import StateBackend, StoreBackend, CompositeBackend
from langchain.agents import create_agent

# Ephemeral storage only (default, no execution)
agent = create_agent(middleware=[FilesystemMiddleware()])

# With hybrid storage (ephemeral + persistent /memories/)
backend = CompositeBackend(
    default=StateBackend(), routes={"/memories/": StoreBackend(namespace=lambda rt: (rt.server_info.user.identity, "filesystem"))}
)
agent = create_agent(middleware=[FilesystemMiddleware(backend=backend)])

# With sandbox backend (supports execution)
from my_sandbox import DockerSandboxBackend

sandbox = DockerSandboxBackend(container_id="my-container")
agent = create_agent(middleware=[FilesystemMiddleware(backend=sandbox)])
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `backend` | `BackendProtocol \| None` | No | Backend for file storage and optional execution.  If not provided, defaults to [`StateBackend`][deepagents.backends.state.StateBackend] (ephemeral storage in agent state).  For persistent storage or hybrid setups, use [`CompositeBackend`][deepagents.backends.composite.CompositeBackend] with custom routes.  For execution support, use a backend that implements [`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol]. (default: `None`) |
| `system_prompt` | `str \| None` | No | Optional custom system prompt override. (default: `None`) |
| `custom_tool_descriptions` | `Mapping[str, str] \| None` | No | Optional custom tool descriptions override. (default: `None`) |
| `tool_token_limit_before_evict` | `int \| None` | No | Token limit before evicting a tool result to the filesystem.  When exceeded, writes the result using the configured backend and replaces it with a truncated preview and file reference. (default: `20000`) |

## Extends

- `AgentMiddleware[FilesystemState, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    backend: BackendProtocol | None = None,
    system_prompt: str | None = None,
    custom_tool_descriptions: Mapping[str, str] | None = None,
    tool_token_limit_before_evict: int | None = 20000,
    human_message_token_limit_before_evict: int | None = 50000,
    max_execute_timeout: int = 3600,
    grep_max_count: int | None = 1000,
    tools: list[FsToolName] | Literal['all'] | None = None,
    _permissions: list[FilesystemPermission] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `backend` | `BackendProtocol \| None` |
| `system_prompt` | `str \| None` |
| `custom_tool_descriptions` | `Mapping[str, str] \| None` |
| `tool_token_limit_before_evict` | `int \| None` |
| `human_message_token_limit_before_evict` | `int \| None` |
| `max_execute_timeout` | `int` |
| `grep_max_count` | `int \| None` |
| `tools` | `list[FsToolName] \| Literal['all'] \| None` |
| `_permissions` | `list[FilesystemPermission] \| None` |

## Properties

- `trace_policy`
- `state_schema`
- `backend`
- `tools`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_model_call)
- [`wrap_tool_call()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L1681)
