---
title: "enabled"
description: "Whether to auto-add the default general-purpose subagent (three-state: None inherits / defaults on, True forces inclusion, False disables)."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/enabled"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, generalpurposesubagentprofile, enabled]
---

# enabled

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/enabled)

Whether to auto-add the default general-purpose subagent (three-state:
`None` inherits / defaults on, `True` forces inclusion, `False` disables).

`None` means inherit from a base profile when merging, or fall back to
the default of including the subagent. `True` forces inclusion and is
what a model-level profile can use to re-enable a subagent that a
provider-level profile disabled. `False` disables the auto-added
subagent entirely.

!!! note

    If the default subagent is disabled and no other synchronous subagents are
    configured, the main agent will not expose the `task` tool.

## Signature

```python
enabled: bool | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L97)
