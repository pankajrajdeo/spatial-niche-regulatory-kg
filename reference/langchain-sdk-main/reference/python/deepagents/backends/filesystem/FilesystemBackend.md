---
title: "FilesystemBackend"
description: "Backend that reads and writes files directly from the filesystem."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend]
---

# FilesystemBackend

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend)

Backend that reads and writes files directly from the filesystem.

Files are accessed using their actual filesystem paths. Relative paths are
resolved relative to the current working directory. Content is read/written
as plain text, and metadata (timestamps) are derived from filesystem stats.

!!! warning "Security Warning"

    This backend grants agents direct filesystem read/write access. Use with
    caution and only in appropriate environments.

    **Appropriate use cases:**

    - Local development CLIs (coding assistants, development tools)
    - CI/CD pipelines (see security considerations below)

    **Inappropriate use cases:**

    - Web servers or HTTP APIs - use `StateBackend`, `StoreBackend`, or
        `SandboxBackend` instead

    **Security risks:**

    - Agents can read any accessible file, including secrets (API keys,
        credentials, `.env` files)
    - Combined with network tools, secrets may be exfiltrated via SSRF attacks
    - File modifications are permanent and irreversible

    **Recommended safeguards:**

    1. Enable Human-in-the-Loop (HITL) middleware to review sensitive operations
    2. Exclude secrets from accessible filesystem paths (especially in CI/CD)
    3. For production environments, prefer `StateBackend`, `StoreBackend` or `SandboxBackend`

    In general, we expect this backend to be used with Human-in-the-Loop (HITL)
    middleware, or within a properly sandboxed environment if you need to run
    untrusted workloads.

    !!! note

        `virtual_mode=True` is primarily for virtual path semantics (for example with
        `CompositeBackend`). It can also provide path-based guardrails by blocking
        traversal (`..`, `~`) and absolute paths outside `root_dir`, but it does not
        provide sandboxing or process isolation. Set `virtual_mode=False` only for
        trusted local development workflows that require unrestricted host paths.

## Signature

```python
FilesystemBackend(
    self,
    root_dir: str | Path | None = None,
    virtual_mode: bool = True,
    max_file_size_mb: int = 10,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `root_dir` | `str \| Path \| None` | No | Optional root directory for file operations.  Defaults to the current working directory.  - When `virtual_mode=True` (default): Acts as a virtual root for filesystem operations. - When `virtual_mode=False`: Only affects relative path resolution. (default: `None`) |
| `virtual_mode` | `bool` | No | Enable virtual path mode.  **Primary use case:** stable, backend-independent path semantics when used with `CompositeBackend`, which strips route prefixes and forwards normalized paths to the routed backend.  When `True` (default), all paths are treated as virtual paths anchored to `root_dir`. Path traversal (`..`, `~`) is blocked and all resolved paths are verified to remain within `root_dir`.  When `False`, absolute paths are used as-is and relative paths are resolved under `root_dir`. This provides no security against an agent choosing paths outside `root_dir`.  - Absolute paths (e.g., `/etc/passwd`) bypass `root_dir` entirely - Relative paths with `..` can escape `root_dir` - Agents have unrestricted filesystem access (default: `True`) |
| `max_file_size_mb` | `int` | No | Maximum file size in megabytes for operations like grep's Python fallback search.  Files exceeding this limit are skipped during search. Defaults to 10 MB. (default: `10`) |

## Extends

- `BackendProtocol`

## Constructors

```python
__init__(
    self,
    root_dir: str | Path | None = None,
    virtual_mode: bool = True,
    max_file_size_mb: int = 10,
) -> None
```

| Name | Type |
|------|------|
| `root_dir` | `str \| Path \| None` |
| `virtual_mode` | `bool` |
| `max_file_size_mb` | `int` |

## Properties

- `cwd`
- `virtual_mode`
- `max_file_size_bytes`

## Methods

- [`ls()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/ls)
- [`read()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/read)
- [`write()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/write)
- [`edit()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/edit)
- [`delete()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/delete)
- [`grep()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/grep)
- [`agrep()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/agrep)
- [`glob()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/glob)
- [`upload_files()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/upload_files)
- [`download_files()`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/download_files)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/filesystem.py#L91)
