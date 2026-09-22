---
title: "excluded_middleware"
description: "Middleware to strip from every stack this profile applies to."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/excluded_middleware"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofile, excluded_middleware]
---

# excluded_middleware

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/excluded_middleware)

Middleware to strip from every stack this profile applies to.

Entries may be a middleware *class* (matched by exact type, not subclass —
consistent with `extra_middleware` slot merging) or a *string* matching
`AgentMiddleware.name` exactly. `.name` defaults to the class's
`__name__` but is overridable, so `{FilesystemMiddleware}` (class form) and
`{"FilesystemMiddleware"}` (name form) behave identically for stock
middleware.

Prefer class form when the class is importable: typos surface at import
time rather than at agent construction. Reserve string form for
YAML/JSON-loaded profiles and for middleware whose class isn't part of
the public import surface (e.g. `"SummarizationMiddleware"` drops the
private `_DeepAgentsSummarizationMiddleware` via its public alias).

The filter runs over the fully assembled stack, so exclusions remove
middleware regardless of which layer added it — including instances
passed via `create_deep_agent(middleware=[...])`. Merged profiles union
their exclusion sets; mixed class/string sets are allowed. For config-file
usage, `HarnessProfileConfig` stores the same exclusions using string names
only.

!!! tip "Stable string aliases for private impl classes"

    Middleware whose concrete class name differs from the public alias
    users would type (e.g. `_DeepAgentsSummarizationMiddleware` vs.
    `"SummarizationMiddleware"`) can expose a `serialized_name: ClassVar[str]`
    for stable config-file round-trips. `.name` on the instance returns
    the alias so string-form exclusion matches, and
    `HarnessProfileConfig.from_harness_profile` serializes the class back
    to that alias.

!!! warning "Restrictions"

    - String grammar is checked at construction: empty, colon-containing,
        and underscore-prefixed names raise `ValueError` immediately.
        Class-path (`module:Class`) entries are not currently supported
        and may be added in a future revision; pass the class itself
        through the runtime `HarnessProfile` instead.
    - Scaffolding classes (`FilesystemMiddleware`, `SubAgentMiddleware`)
        cannot be excluded as class or as their `.name` string. The check
        fires at `HarnessProfile` construction,
        so register-site typos fail fast rather than waiting until
        `create_deep_agent` resolves the profile. To hide their tools
        from the model without removing the middleware, use
        `excluded_tools` instead — the runtime rejection message points
        at the same workaround.
    - Entries that match no middleware in the assembled stack are
        rejected as likely typos or stale profiles.

!!! note "Removing the `task` tool"

    Don't reach for `excluded_middleware` here — it intentionally raises
    `ValueError` on `SubAgentMiddleware`. Instead, set
    `general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)`
    and pass no synchronous subagents via `subagents=` on
    `create_deep_agent`. With nothing to back, the `task` tool is gone.
    Async subagents are independent.

## Signature

```python
excluded_middleware: frozenset[type[AgentMiddleware] | str] = frozenset()
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L629)
