---
title: "edit"
description: "Edit a file by replacing exact string occurrences."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/edit"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, edit]
---

# edit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/edit)

Edit a file by replacing exact string occurrences.

For small payloads (combined old/new under `_EDIT_INLINE_MAX_BYTES`),
runs a server-side Python script via `execute()` — single round-trip,
no file transfer.  For larger payloads, uploads old/new strings as
temp files and runs a server-side replace script — the source file
never leaves the sandbox.

`read()` normalizes CRLF to LF for the LLM, so `old_string` is
typically LF-only. The server-side script tries `old_string` as-is
first, then CRLF- and LF-normalized variants, and applies the same
transform to `new_string` so the file's line-ending style is
preserved on write. On mixed-ending files, `replace_all=True` only
touches occurrences in the first matching style — subsequent edits
can replace the rest.

## Signature

```python
edit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Absolute path to the file to edit. |
| `old_string` | `str` | Yes | The exact substring to find. |
| `new_string` | `str` | Yes | The replacement string. |
| `replace_all` | `bool` | No | If `True`, replace every occurrence.  If `False` (default), error when more than one occurrence exists. (default: `False`) |

## Returns

`EditResult`

`EditResult` with `path` and `occurrences` on success, or `error`
on failure.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1639)
