---
title: "get_provider_profile"
description: "Look up the ProviderProfile for a model spec."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/get_provider_profile"
category: "reference"
tags: [reference, deepagents, profiles, provider, get_provider_profile]
---

# get_provider_profile

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/get_provider_profile)

Look up the `ProviderProfile` for a model spec.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../versioning.md)
    for more details.

Resolution order:

1. Exact match on `spec`.
2. Provider prefix (everything before the first `:`), when `spec`
    contains a colon and both halves are non-empty.
3. `None` when neither matches.

When both an exact-model profile and a provider-level profile exist, they
are merged via `_merge_provider_profiles` with the exact-model entry
overriding the provider-level entry on conflicts.

When only the provider-level profile matches, a debug breadcrumb is
emitted so registrations layered on an exact key can be traced when they
don't apply (e.g. typo'd specs falling through to the provider default).

!!! note "Prefer `apply_provider_profile` for model construction"

    This function is intended for *inspection* (tooling, conditional logic
    on `pre_init` presence). To actually build a model, reach for
    `apply_provider_profile` — it composes lookup, `pre_init` invocation,
    and kwargs merging into a single call.

## Signature

```python
get_provider_profile(
    spec: str,
) -> ProviderProfile | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `spec` | `str` | Yes | Model spec in `provider:model` format, or a bare provider/model identifier. Only the first colon is a separator. |

## Returns

`ProviderProfile | None`

The matching `ProviderProfile`, or `None` when no registered profile matches.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L277)
