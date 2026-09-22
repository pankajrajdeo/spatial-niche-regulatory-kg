---
title: "system_prompt_suffix"
description: "SUFFIX slot in the prompt assembly order."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/system_prompt_suffix"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, system_prompt_suffix]
---

# system_prompt_suffix

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/system_prompt_suffix)

`SUFFIX` slot in the prompt assembly order.

This text is appended last — after `USER` and `BASE` for the main agent —
so model-tuning guidance lands closest to the conversation history. `None`
(the default) means no suffix.

## Signature

```python
system_prompt_suffix: str | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L270)
