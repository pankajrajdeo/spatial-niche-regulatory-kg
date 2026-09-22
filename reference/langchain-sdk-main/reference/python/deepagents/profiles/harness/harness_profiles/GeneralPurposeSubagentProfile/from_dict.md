---
title: "from_dict"
description: "Construct a sub-profile from a plain dict."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/from_dict"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, generalpurposesubagentprofile, from_dict]
---

# from_dict

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/from_dict)

Construct a sub-profile from a plain dict.

## Signature

```python
from_dict(
    cls,
    data: Mapping[str, Any],
) -> GeneralPurposeSubagentProfile
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `data` | `Mapping[str, Any]` | Yes | Mapping with any subset of `enabled`, `description`, and `system_prompt` keys. |

## Returns

`GeneralPurposeSubagentProfile`

A new `GeneralPurposeSubagentProfile`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L157)
