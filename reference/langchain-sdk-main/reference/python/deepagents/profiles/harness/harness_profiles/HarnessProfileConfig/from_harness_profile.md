---
title: "from_harness_profile"
description: "Export a runtime HarnessProfile back to declarative config."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/from_harness_profile"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, from_harness_profile]
---

# from_harness_profile

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/from_harness_profile)

Export a runtime `HarnessProfile` back to declarative config.

String-form `excluded_middleware` entries are preserved as-is.
Class-form entries are only serializable when the class advertises a
public `serialized_name` alias; arbitrary class-path serialization is
not currently supported.

## Signature

```python
from_harness_profile(
    cls,
    profile: HarnessProfile,
) -> HarnessProfileConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `profile` | `HarnessProfile` | Yes | Runtime profile to export. |

## Returns

`HarnessProfileConfig`

A declarative `HarnessProfileConfig`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L438)
