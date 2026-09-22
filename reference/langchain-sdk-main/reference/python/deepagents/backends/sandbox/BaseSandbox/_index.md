---
title: "reference/python/deepagents/backends/sandbox/BaseSandbox"
description: "Index of 20 pages and 0 subdirectories under reference/python/deepagents/backends/sandbox/BaseSandbox."
category: "index"
tags: [index, reference, python, deepagents, backends, sandbox, basesandbox]
---

# reference/python/deepagents/backends/sandbox/BaseSandbox

20 pages here.

## Files

- [aedit](aedit.md) - Async version of edit, delegating to aexecute and aupload_files.
- [aexecute_with_offload](aexecute_with_offload.md) - Async version of execute_with_offload, delegating to aexecute.
- [aglob](aglob.md) - Async version of glob, delegating to aexecute.
- [agrep](agrep.md) - Async version of grep, delegating to aexecute with timeout guard.
- [als](als.md) - Async version of ls, delegating to aexecute.
- [aread](aread.md) - Async version of read, delegating to aexecute.
- [awrite](awrite.md) - Async version of write, delegating to aexecute and aupload_files.
- [delete](delete.md) - Delete a file or directory from the sandbox via a server-side rm.
- [download_files](download_files.md) - Download multiple files from the sandbox.
- [edit](edit.md) - Edit a file by replacing exact string occurrences.
- [enable_capture_offload](enable_capture_offload.md) - Whether FilesystemMiddleware may use capture-at-source offload for execute.
- [execute](execute.md) - Execute a command in the sandbox and return ExecuteResponse.
- [execute_with_offload](execute_with_offload.md) - Run command, offloading large output to a file in the sandbox.
- [glob](glob.md) - Structured glob matching returning GlobResult.
- [grep](grep.md) - Search file contents for a literal string using grep -F.
- [id](id.md) - Unique identifier for the sandbox backend.
- [ls](ls.md) - Structured listing with file metadata using os.scandir.
- [read](read.md) - Read file content with server-side line-based pagination.
- [upload_files](upload_files.md) - Upload multiple files to the sandbox.
- [write](write.md) - Write content to a file, creating or overwriting it if it already exists.
