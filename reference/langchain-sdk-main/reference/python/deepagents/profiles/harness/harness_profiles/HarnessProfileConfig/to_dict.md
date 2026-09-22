---
title: "to_dict"
description: "Dump this config to plain dict/list/scalar values."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_dict"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, to_dict]
---

# to_dict

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_dict)

Dump this config to plain dict/list/scalar values.

Suitable for `json.dumps` or `yaml.safe_dump`. Fields at their
default are omitted so the output stays minimal and round-trips
cleanly through `from_dict`.

## Signature

```python
to_dict(
    self,
) -> dict[str, Any]
```

## Returns

`dict[str, Any]`

A plain dict containing only the fields set on this config.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L338)
