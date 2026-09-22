---
title: "register_provider_profile"
description: "Register a ProviderProfile for a provider or specific model."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/register_provider_profile"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, register_provider_profile]
---

# register_provider_profile

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/register_provider_profile)

Register a `ProviderProfile` for a provider or specific model.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../../versioning.md)
    for more details.

Register under a provider name to set defaults for its models, or under
`provider:model` to customize one model. Model-specific settings override
conflicting provider defaults and inherit the remaining settings.

For example, set defaults for a hypothetical provider, then lower the
temperature for one model:

```python
from deepagents import ProviderProfile, register_provider_profile

register_provider_profile(
    "my_provider",
    ProviderProfile(init_kwargs={"temperature": 0.7, "timeout": 30}),
)
register_provider_profile(
    "my_provider:my-model:tag",
    ProviderProfile(init_kwargs={"temperature": 0}),
)
```

When Deep Agents constructs `my_provider:my-model:tag`, the profile supplies
`temperature=0` and `timeout=30`. Other models from `my_provider` receive
`temperature=0.7` and `timeout=30`. The model identifier is `my-model:tag`;
only the first colon separates it from the provider.

Register profiles before constructing the agent. Passing a model instance
to `create_deep_agent` leaves its construction settings unchanged; see
`register_harness_profile` for examples of both forms.

Re-registering merges with the existing profile: new values override
conflicts and unspecified fields remain. Continuing the example, give
this model a longer timeout:

```python
register_provider_profile(
    "my_provider:my-model:tag",
    ProviderProfile(init_kwargs={"timeout": 60}),
)
```

Future construction of this model uses `temperature=0` and `timeout=60`;
other models still use the provider's defaults.

Deep Agents also ships **built-in profiles**: model-construction defaults
registered automatically for selected providers. Registering under one of
those keys customizes the shipped settings using the same merge rules.

`pre_init` callables run existing first, then new.
Both `init_kwargs_factory` callables run in that order too, with the new
factory's output winning on shared keys.

See the [Profiles guide](../../../../../../deepagents/profiles.md)
for registration workflows and configuration files.

## Signature

```python
register_provider_profile(
    key: str,
    profile: ProviderProfile,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | Either a provider name (no colon) for provider-wide defaults, or a full `provider:model` spec for a per-model override. Only the first colon separates the provider from the model identifier:  - `"openai"` — provider-wide - `"openai:gpt-5.4"` — specific model - `"ollama:glm-5.2:cloud"` — model identifier containing a colon |
| `profile` | `ProviderProfile` | Yes | The provider profile to register. |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L195)
