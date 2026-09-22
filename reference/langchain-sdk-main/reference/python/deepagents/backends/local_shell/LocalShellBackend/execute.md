---
title: "execute"
description: "Execute a shell command directly on the host system."
source: "https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend/execute"
category: "reference"
tags: [reference, deepagents, backends, local_shell, localshellbackend, execute]
---

# execute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend/execute)

Execute a shell command directly on the host system.

!!! danger "Unrestricted Execution"

    Commands are executed directly on your host system
    using `subprocess.run()` with `shell=True`. There is **no sandboxing,
    isolation, or security restrictions**. The command runs with
    your user's full permissions and can:

    - Access any file on the filesystem (regardless of `virtual_mode`)
    - Execute any program or script
    - Make network connections
    - Modify system configuration
    - Spawn additional processes
    - Install packages or modify dependencies

    **Always use Human-in-the-Loop (HITL) middleware when using this method.**

The command is executed using the system shell (`/bin/sh` or equivalent)
with the working directory set to the backend's `root_dir`.
Stdout and stderr are combined into a single output stream.

## Signature

```python
execute(
    self,
    command: str,
    *,
    timeout: int | None = None,
) -> ExecuteResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `command` | `str` | Yes | Shell command string to execute.  Examples: `"python script.py"`, `"ls -la"`, `"grep pattern file.txt"`  **Security:** This string is passed directly to the shell. Agents can execute arbitrary commands including pipes, redirects, command substitution, etc. |
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for this command.  Overrides the default timeout set at init.  If `None`, uses the default. (default: `None`) |

## Returns

`ExecuteResponse`

`ExecuteResponse` containing:
- `output`: Combined stdout and stderr (stderr lines prefixed with `[stderr]`)
- `exit_code`: Process exit code (0 for success, non-zero for failure)
- `truncated`: `True` if output was truncated due to size limits

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/local_shell.py#L216)
