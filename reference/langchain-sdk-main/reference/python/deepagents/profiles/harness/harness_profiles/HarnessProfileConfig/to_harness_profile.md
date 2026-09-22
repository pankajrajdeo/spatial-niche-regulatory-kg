---
title: "to_harness_profile"
description: "Convert this declarative config into a runtime HarnessProfile."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_harness_profile"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, to_harness_profile]
---

# to_harness_profile

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_harness_profile)

Convert this declarative config into a runtime `HarnessProfile`.

`excluded_middleware` entries are passed through as name-based
exclusions matched against `AgentMiddleware.name`.

!!! note "Intentional asymmetry with `from_harness_profile`"

    This direction is currently lossless because `HarnessProfileConfig`
    carries only the file-friendly subset of fields by design —
    `extra_middleware` instances and factories cannot be
    represented in YAML/JSON, so they are absent from this type
    and the resulting `HarnessProfile` will not have them
    populated. The reverse direction (`from_harness_profile`)
    *raises* when a runtime profile contains runtime-only state,
    rather than silently dropping it. Round-tripping a runtime
    profile that uses `extra_middleware` through config form is
    therefore not supported by design at this moment — keep
    such profiles in `HarnessProfile` form.

## Signature

```python
to_harness_profile(
    self,
) -> HarnessProfile
```

## Returns

`HarnessProfile`

A runtime `HarnessProfile` with equivalent declarative settings.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L406)
