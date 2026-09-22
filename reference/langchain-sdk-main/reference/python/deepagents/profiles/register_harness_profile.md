---
title: "register_harness_profile"
description: "Register a harness profile for a provider or specific model."
source: "https://reference.langchain.com/python/deepagents/profiles/register_harness_profile"
category: "reference"
tags: [reference, deepagents, profiles, register_harness_profile]
---

# register_harness_profile

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/register_harness_profile)

Register a harness profile for a provider or specific model.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../versioning.md)
    for more details.

Accepts a runtime `HarnessProfile` or converts a declarative
`HarnessProfileConfig` at registration time.

Register under a provider name to set defaults for its models, or under
`provider:model` to customize one model. Model-specific settings inherit
provider defaults, with explicit fields replacing or extending them.

For example, exclude a tool for a hypothetical provider's models, then
customize the response length for one model:

```python
from deepagents import HarnessProfile, register_harness_profile

register_harness_profile(
    "my_provider",
    HarnessProfile(
        excluded_tools=frozenset({"execute"}),
        system_prompt_suffix="Respond in under 500 words.",
    ),
)
register_harness_profile(
    "my_provider:my-model:tag",
    HarnessProfile(system_prompt_suffix="Respond in under 100 words."),
)
```

An agent using `my_provider:my-model:tag` excludes `execute` and receives
the 100-word prompt suffix. Other models from `my_provider` exclude
`execute` and receive the 500-word suffix.

Register profiles before calling `create_deep_agent`. Using the hypothetical
provider above, you can pass a model string or construct the model yourself:

```python
from langchain.chat_models import init_chat_model

from deepagents import create_deep_agent

# Deep Agents constructs the model from a string.
agent = create_deep_agent(model="my_provider:my-model:tag")

# Or construct a model object first, then pass it to Deep Agents.
model = init_chat_model("my-model:tag", model_provider="my_provider")
agent = create_deep_agent(model=model)
```

For the model object, Deep Agents looks up the harness profile using the
provider and model identifier reported by that object. If it reports
`my_provider` and `my-model:tag`, it matches the same registration above.

Re-registering merges with the existing profile: new values override
conflicts and unspecified fields remain. Continuing the example, exclude
one more tool:

```python
register_harness_profile(
    "my_provider:my-model:tag",
    HarnessProfile(excluded_tools=frozenset({"grep"})),
)
```

An agent created afterward with this model excludes both `execute` and
`grep` and still receives the 100-word prompt suffix.

Deep Agents also ships **built-in profiles**: default harness settings
registered automatically for selected models. Registering under one of
those keys customizes the shipped settings using the same merge rules.

Excluded-tool sets union, middleware sequences merge
by type, and `general_purpose_subagent` settings merge field-wise.

See the [Profiles guide](../../../../deepagents/profiles.md)
for registration workflows and configuration files.

## Signature

```python
register_harness_profile(
    key: str,
    profile: HarnessProfile | HarnessProfileConfig,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | Either a provider name (no colon) for provider-wide defaults, or a full `provider:model` spec for a per-model override. Only the first colon separates the provider from the model identifier:  - `"openai"` — provider-wide - `"openai:gpt-5.4"` — specific model - `"ollama:glm-5.2:cloud"` — model identifier containing a colon |
| `profile` | `HarnessProfile \| HarnessProfileConfig` | Yes | The runtime harness profile or declarative config to register. |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L980)
