---
title: "aupdate"
description: "Asynchronously upsert records into the database."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/aupdate"
category: "reference"
tags: [reference, langchain-core, indexing, base, recordmanager, aupdate]
---

# aupdate

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/aupdate)

Asynchronously upsert records into the database.

## Signature

```python
aupdate(
    self,
    keys: Sequence[str],
    *,
    group_ids: Sequence[str | None] | None = None,
    time_at_least: float | None = None,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `Sequence[str]` | Yes | A list of record keys to upsert. |
| `group_ids` | `Sequence[str \| None] \| None` | No | A list of group IDs corresponding to the keys. (default: `None`) |
| `time_at_least` | `float \| None` | No | Optional timestamp. Implementation can use this to optionally verify that the timestamp IS at least this time in the system that stores the data.  e.g., use to validate that the time in the postgres database is equal to or larger than the given timestamp, if not raise an error.  This is meant to help prevent time-drift issues since time may not be monotonically increasing! (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L126)
