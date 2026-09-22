---
title: "harness_profiles"
description: "Beta APIs for configuring deep agent runtime behavior."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles]
---

# harness_profiles

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles)

Beta APIs for configuring deep agent runtime behavior.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../versioning.md)
    for more details.

Harness profiles declare how `create_deep_agent` should shape the agent's
runtime behavior for a given provider or specific model spec. They tune
prompt assembly, tool visibility, middleware, and default subagent behavior
*after* the chat model has been constructed — orthogonal to
`ProviderProfile`, which controls the model-construction phase.

Users may register profiles via `register_harness_profile`. Deep Agents
ships built-in harness profiles for several frontier model specs.
They may be layered on top of via additive merge semantics.

## Properties

- `logger`

## Methods

- [`validate_profile_key()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/validate_profile_key)
- [`register_harness_profile()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/register_harness_profile)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py)
