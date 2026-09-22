---
title: "LocalShellBackend"
description: "Filesystem backend with unrestricted local shell command execution."
source: "https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend"
category: "reference"
tags: [reference, deepagents, backends, local_shell, localshellbackend]
---

# LocalShellBackend

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend)

Filesystem backend with unrestricted local shell command execution.

This backend extends `FilesystemBackend` to add shell command execution
capabilities. Commands are executed directly on the host system without any
sandboxing, process isolation, or security restrictions.

!!! warning "Security Warning"

    This backend grants agents BOTH direct filesystem access AND
    unrestricted shell execution on your local machine. Use with extreme
    caution and only in appropriate environments.

    **Appropriate use cases:**

    - Local development CLIs (coding assistants, development tools)
    - Personal development environments where you trust the agent's code
    - CI/CD pipelines with proper secret management (see
        security considerations)

    **Inappropriate use cases:**

    - Production environments (e.g., web servers, APIs, multi-tenant systems)
    - Processing untrusted user input or executing untrusted code

    Use `StateBackend`, `StoreBackend`, or extend `BaseSandbox` for production.

    **Security risks:**

    - Agents can execute **arbitrary shell commands** with your
        user's permissions
    - Agents can read **any accessible file**, including secrets (API keys,
        credentials, `.env` files, SSH keys, etc.)
    - Combined with network tools, secrets may be exfiltrated via SSRF attacks
    - File modifications and command execution are **permanent and irreversible**
    - Agents can install packages, modify system files, spawn processes, etc.
    - **No process isolation** - commands run directly on your host system
    - **No resource limits** - commands can consume unlimited CPU, memory, disk

    **Recommended safeguards:**

    Since shell access is unrestricted and can bypass
    filesystem restrictions:

    1. **Enable Human-in-the-Loop (HITL) middleware** to review and
        approve ALL operations before execution. This is
        STRONGLY RECOMMENDED as your primary safeguard when using this backend.
    2. Run in dedicated development environments only - never on shared or
        production systems
    3. Never expose to untrusted users or allow execution of untrusted code
    4. For production environments requiring code execution, extend `BaseSandbox`
        to create a properly isolated backend (Docker containers, VMs, or
        other sandboxed execution environments)

    !!! note

        `virtual_mode=True` and path-based restrictions provide NO security
        with shell access enabled, since commands can access any path on
        the system

## Signature

```python
LocalShellBackend(
    self,
    root_dir: str | Path | None = None,
    *,
    virtual_mode: bool = True,
    timeout: int = DEFAULT_EXECUTE_TIMEOUT,
    max_output_bytes: int = 100000,
    env: dict[str, str] | None = None,
    inherit_env: bool = False,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `root_dir` | `str \| Path \| None` | No | Working directory for both filesystem operations and shell commands.  - If not provided, defaults to the current working directory. - Shell commands execute with this as their working directory. - When `virtual_mode=False`: Paths are used as-is.      Agents can access any file using absolute paths or `..` sequences. - When `virtual_mode=True` (default): Acts as a virtual root for filesystem operations.      Useful with `CompositeBackend` to support routing file     operations across different backend implementations.      **Note:** This does NOT restrict shell commands. (default: `None`) |
| `virtual_mode` | `bool` | No | Enable virtual path mode for filesystem operations.  When `True` (default), treats `root_dir` as a virtual root filesystem. All paths are interpreted relative to `root_dir` (e.g., `/file.txt` maps to `{root_dir}/file.txt`). Path traversal (`..`, `~`) is blocked.  **Primary use case:** Working with `CompositeBackend`, which routes different path prefixes to different backends. Virtual mode allows the `CompositeBackend` to strip route prefixes and pass normalized paths to each backend, enabling file operations to work correctly across multiple backend implementations.  **Important:** This only affects filesystem operations. Shell commands executed via `execute()` are NOT restricted and can access any path. (default: `True`) |
| `timeout` | `int` | No | Default maximum time in seconds to wait for shell command execution.  Defaults to 120 seconds (2 minutes).  Commands exceeding this timeout will be terminated.  Can be overridden per-command via the `timeout` parameter on `execute()`. (default: `DEFAULT_EXECUTE_TIMEOUT`) |
| `max_output_bytes` | `int` | No | Maximum number of bytes to capture from command output. Output exceeding this limit will be truncated.  Defaults to 100,000 bytes. (default: `100000`) |
| `env` | `dict[str, str] \| None` | No | Environment variables for shell commands.  If `None`, starts with an empty environment (unless `inherit_env=True`). (default: `None`) |
| `inherit_env` | `bool` | No | Whether to inherit the parent process's environment variables.  When `False` (default), only variables in `env` dict are available.  When `True`, inherits all `os.environ` variables and applies `env` overrides. (default: `False`) |

## Extends

- `FilesystemBackend`
- `SandboxBackendProtocol`

## Constructors

```python
__init__(
    self,
    root_dir: str | Path | None = None,
    *,
    virtual_mode: bool = True,
    timeout: int = DEFAULT_EXECUTE_TIMEOUT,
    max_output_bytes: int = 100000,
    env: dict[str, str] | None = None,
    inherit_env: bool = False,
) -> None
```

| Name | Type |
|------|------|
| `root_dir` | `str \| Path \| None` |
| `virtual_mode` | `bool` |
| `timeout` | `int` |
| `max_output_bytes` | `int` |
| `env` | `dict[str, str] \| None` |
| `inherit_env` | `bool` |

## Properties

- `id`

## Methods

- [`execute()`](https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend/execute)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/local_shell.py#L27)
