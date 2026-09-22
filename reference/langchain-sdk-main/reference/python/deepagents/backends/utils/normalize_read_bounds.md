---
title: "normalize_read_bounds"
description: "Floor a requested read window at a zero offset and zero lines."
source: "https://reference.langchain.com/python/deepagents/backends/utils/normalize_read_bounds"
category: "reference"
tags: [reference, deepagents, backends, utils, normalize_read_bounds]
---

# normalize_read_bounds

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/normalize_read_bounds)

Floor a requested read window at a zero offset and zero lines.

Models occasionally emit degenerate `read_file` arguments (`offset=-1`,
`limit=0`). Clamping `offset` keeps backends from reporting a line range
that starts before line 1, which `ReadResult` rejects.

Clamping `limit` is *not* sufficient on its own: flooring a negative limit
at `0` produces a zero-length window, which still has no valid
`start_line`/`end_line` pair. Callers must additionally treat a returned
`limit` of `0` as an empty read — see `slice_read_response` below, or the
equivalent short-circuits in the sandbox and LangSmith backends, which
flag the result with `ReadResult.no_lines_requested`.

The `int()` coercion is deliberate and load-bearing, not redundant with the
annotations: `offset` and `limit` originate from model-supplied tool
arguments, and the sandbox backend interpolates them into the source of a
script it executes (`_READ_COMMAND_TEMPLATE`). Do not remove it.

## Signature

```python
normalize_read_bounds(
    offset: int,
    limit: int,
) -> tuple[int, int]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `offset` | `int` | Yes | Requested 0-indexed line offset. |
| `limit` | `int` | Yes | Requested maximum number of lines. |

## Returns

`tuple[int, int]`

Tuple of `(offset, limit)`, each coerced to `int` and floored at `0`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L431)
