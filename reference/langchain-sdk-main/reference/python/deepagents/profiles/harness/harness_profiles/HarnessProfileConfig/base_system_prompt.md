---
title: "base_system_prompt"
description: "BASE slot in the prompt assembly order."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/base_system_prompt"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, base_system_prompt]
---

# base_system_prompt

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/base_system_prompt)

`BASE` slot in the prompt assembly order.

When applied to a stack, this replaces its authored base prompt. `None`
(the default) leaves that base unchanged; the main agent has no authored
base prompt by default.

For the main agent, a caller-supplied `system_prompt=` (`USER`) is placed
before this `BASE`, and `system_prompt_suffix` (`SUFFIX`) follows it. See
`create_deep_agent`'s `system_prompt` parameter or
[Prompt assembly](https://docs.langchain.com/oss/deepagents/customization#prompt-assembly)
for the full assembly order.

## Signature

```python
base_system_prompt: str | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L256)
