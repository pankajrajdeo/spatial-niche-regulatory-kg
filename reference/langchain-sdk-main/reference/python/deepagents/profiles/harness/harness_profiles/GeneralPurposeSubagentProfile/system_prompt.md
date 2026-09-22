---
title: "system_prompt"
description: "Override for the default general-purpose subagent system prompt."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/system_prompt"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, generalpurposesubagentprofile, system_prompt]
---

# system_prompt

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/system_prompt)

Override for the default general-purpose subagent system prompt.

`None` means keep the default system prompt.

!!! note "Precedence vs `HarnessProfile.base_system_prompt`"

    When a profile sets *both* this field and
    `HarnessProfile.base_system_prompt`, this field wins for the
    general-purpose subagent.

    The reasoning: `general_purpose_subagent.system_prompt` is GP-specific
    configuration, while `base_system_prompt` is a global override that
    applies to the main agent. The more-specific intent wins on the GP
    subagent so a user setting both never sees their GP override
    silently dropped. The profile's `system_prompt_suffix` still
    layers on top.

## Signature

```python
system_prompt: str | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L119)
