---
title: "GeneralPurposeSubagentProfile"
description: "Edits applied to the auto-added general-purpose subagent."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, generalpurposesubagentprofile]
---

# GeneralPurposeSubagentProfile

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile)

Edits applied to the auto-added `general-purpose` subagent.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../../versioning.md)
    for more details.

These settings only affect the default subagent that `create_deep_agent`
inserts when the caller does not explicitly provide a subagent named
`general-purpose`.

## Signature

```python
GeneralPurposeSubagentProfile(
    self,
    enabled: bool | None = None,
    description: str | None = None,
    system_prompt: str | None = None,
)
```

## Constructors

```python
__init__(
    self,
    enabled: bool | None = None,
    description: str | None = None,
    system_prompt: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `enabled` | `bool \| None` |
| `description` | `str \| None` |
| `system_prompt` | `str \| None` |

## Properties

- `enabled`
- `description`
- `system_prompt`

## Methods

- [`to_dict()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/to_dict)
- [`from_dict()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/from_dict)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L82)
