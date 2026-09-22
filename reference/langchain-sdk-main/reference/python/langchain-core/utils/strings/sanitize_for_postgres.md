---
title: "sanitize_for_postgres"
description: "Sanitize text by removing NUL bytes that are incompatible with PostgreSQL."
source: "https://reference.langchain.com/python/langchain-core/utils/strings/sanitize_for_postgres"
category: "reference"
tags: [reference, langchain-core, utils, strings, sanitize_for_postgres]
---

# sanitize_for_postgres

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/strings/sanitize_for_postgres)

Sanitize text by removing NUL bytes that are incompatible with PostgreSQL.

PostgreSQL text fields cannot contain `NUL (0x00)` bytes, which can cause
`psycopg.DataError` when inserting documents. This function removes or replaces
such characters to ensure compatibility.

## Signature

```python
sanitize_for_postgres(
    text: str,
    replacement: str = '',
) -> str
```

## Description

**Example:**

>>> sanitize_for_postgres("Hello\\x00world")
'Helloworld'
>>> sanitize_for_postgres("Hello\\x00world", " ")
'Hello world'

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The text to sanitize. |
| `replacement` | `str` | No | String to replace `NUL` bytes with. (default: `''`) |

## Returns

`str`

The sanitized text with `NUL` bytes removed or replaced.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/strings.py#L49)
