---
title: "regex_literal_hint"
description: "Return a hint when a pattern looks like an (unsupported) regex."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/regex_literal_hint"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, regex_literal_hint]
---

# regex_literal_hint

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/regex_literal_hint)

Return a hint when a pattern looks like an (unsupported) regex.

`grep` matches literal text, so regex metacharacters are searched verbatim
and silently miss. Callers gate this on a no-match result; the function
itself only inspects the pattern.

## Signature

```python
regex_literal_hint(
    pattern: str,
) -> str | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pattern` | `str` | Yes | The literal grep pattern to inspect for regex signals. |

## Returns

`str | None`

A one-line hint steering the caller toward literal search, or `None`
when the pattern has no regex signals.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L1073)
