---
title: "tool_description_overrides"
description: "Per-tool description replacements keyed by tool name."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/tool_description_overrides"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofile, tool_description_overrides]
---

# tool_description_overrides

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/tool_description_overrides)

Per-tool description replacements keyed by tool name.

Applied only where Deep Agents has a stable description hook: built-in
filesystem tools, the `task` tool, and user-supplied `BaseTool` or dict
tools. Plain callable tools are left unchanged.

Once a profile is constructed, its overrides can be read but not
rewritten — for example, `profile.tool_description_overrides["ls"] =
"new"` raises `TypeError`. The registry stores its own defensive copy,
so mutating the dict you passed into the constructor after the fact
won't affect the registered profile either. To change a registered
profile's overrides, re-register (which merges on top) or construct a
new profile.

!!! warning

    Keys are matched by tool name string. If a built-in tool is renamed
    or removed, stale keys silently become no-ops with no error. Keep
    overrides minimal and verify against the current tool names.

!!! warning "Overriding task tool description"

    The `task` tool's default description contains an `{available_agents}`
    format placeholder that `SubAgentMiddleware` replaces at build time
    with the registered subagent name/description list. If your
    override string does not include `{available_agents}`, the final
    description is used as-is and the model will not see which
    subagents exist — making the tool much less useful. Include the
    placeholder in any `"task"` override, e.g.
    `"My custom instructions.\n\n{available_agents}"`.

## Signature

```python
tool_description_overrides: Mapping[str, str] = field(default_factory=dict)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L580)
