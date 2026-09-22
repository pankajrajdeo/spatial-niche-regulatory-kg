---
title: "general_purpose_subagent"
description: "Edits for the auto-added general-purpose subagent."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/general_purpose_subagent"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, general_purpose_subagent]
---

# general_purpose_subagent

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/general_purpose_subagent)

Edits for the auto-added `general-purpose` subagent.

Unset is equivalent to passing a default-constructed
`GeneralPurposeSubagentProfile()` — the auto-added subagent runs with
its stock description and prompt.

Set `enabled` to `false` on a populated sub-profile to remove
the default `general-purpose` subagent. Pair that with no synchronous
subagents via `subagents=` on `create_deep_agent` and the `task` tool
is dropped too. Async subagents are unaffected.

## Signature

```python
general_purpose_subagent: GeneralPurposeSubagentProfile | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L308)
