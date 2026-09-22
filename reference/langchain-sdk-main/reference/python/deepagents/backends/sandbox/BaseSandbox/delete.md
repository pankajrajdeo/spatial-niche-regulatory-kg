---
title: "delete"
description: "Delete a file or directory from the sandbox via a server-side rm."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/delete"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/delete)

Delete a file or directory from the sandbox via a server-side `rm`.

Runs `test -e || test -L` first: a path that does not exist (and is not
a broken symlink) returns a not-found error, matching the contract of
`FilesystemBackend` and `StateBackend`. Because a shell `test` has no
error channel, a non-zero probe conflates "absent" with "unstattable"
(e.g. an unsearchable parent directory); an unknown exit code is not
treated as absent and falls through to the delete.

Uses `rm -rf`, so directories are removed recursively along with their
contents. A recursive delete may remove some entries before failing
partway; a non-zero `rm` exit (e.g. a permission error) is reported as
a failure.

## Signature

```python
delete(
    self,
    file_path: str,
) -> DeleteResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Absolute path to the file or directory to delete. |

## Returns

`DeleteResult`

`DeleteResult` with the deleted path on success, or an error if the
path does not exist or the deletion command fails.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1833)
