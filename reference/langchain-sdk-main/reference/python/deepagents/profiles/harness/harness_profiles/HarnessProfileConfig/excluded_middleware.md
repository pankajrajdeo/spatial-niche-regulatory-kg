---
title: "excluded_middleware"
description: "Middleware names to strip from every stack this profile applies to."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/excluded_middleware"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, excluded_middleware]
---

# excluded_middleware

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/excluded_middleware)

Middleware names to strip from every stack this profile applies to.

Strings match `AgentMiddleware.name` exactly. Entries are grammar-checked
at construction: empty/whitespace strings, colon-containing strings, and
underscore-prefixed names all raise `ValueError` immediately.

Class-path (`module:Class`) entries are not currently supported and may
be added in a future revision. Until then, expose a stable public alias
via `serialized_name` on the middleware class and exclude by that alias.

This is the canonical on-disk representation used by `to_dict` /
`from_dict`.

!!! note "Removing the `task` tool"

    `excluded_middleware` won't drop `"SubAgentMiddleware"` (or
    `"FilesystemMiddleware"`) — they're required scaffolding. To run
    without the `task` tool, set `general_purpose_subagent.enabled`
    to `false` on this config and pass no synchronous subagents via
    `subagents=` on `create_deep_agent`. Async subagents are
    unaffected.

## Signature

```python
excluded_middleware: frozenset[str] = frozenset()
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L284)
