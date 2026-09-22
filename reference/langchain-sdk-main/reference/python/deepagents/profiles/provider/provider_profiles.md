---
title: "provider_profiles"
description: "Beta APIs for configuring model-construction behavior."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles]
---

# provider_profiles

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles)

Beta APIs for configuring model-construction behavior.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../versioning.md)
    for more details.

Provider profiles declare how Deep Agents should construct a chat model for a
given provider or specific model spec. The registry is consumed by
`resolve_model` and is the extension point for controlling `init_chat_model`
kwargs, running pre-initialization side effects, and deriving kwargs from
runtime state (e.g. environment variables).

## Properties

- `logger`

## Methods

- [`validate_profile_key()`](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/validate_profile_key)
- [`register_provider_profile()`](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/register_provider_profile)
- [`get_provider_profile()`](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/get_provider_profile)
- [`apply_provider_profile()`](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/apply_provider_profile)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/provider/provider_profiles.py)
