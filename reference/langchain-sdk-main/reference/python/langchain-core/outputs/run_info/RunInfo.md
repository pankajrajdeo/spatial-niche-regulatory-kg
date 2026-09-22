---
title: "RunInfo"
description: "Class that contains metadata for a single execution of a chain or model."
source: "https://reference.langchain.com/python/langchain-core/outputs/run_info/RunInfo"
category: "reference"
tags: [reference, langchain-core, outputs, run_info, runinfo]
---

# RunInfo

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/run_info/RunInfo)

Class that contains metadata for a single execution of a chain or model.

Defined for backwards compatibility with older versions of `langchain_core`.

!!! warning "This model will likely be deprecated in the future."

Users can acquire the `run_id` information from callbacks or via `run_id`
information present in the `astream_event` API (depending on the use case).

## Signature

```python
RunInfo()
```

## Extends

- `BaseModel`

## Properties

- `run_id`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/outputs/run_info.py#L10)
