---
title: "ProviderProfile"
description: "Declarative configuration for constructing a chat model."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, providerprofile]
---

# ProviderProfile

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile)

Declarative configuration for constructing a chat model.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../../versioning.md)
    for more details.

A `ProviderProfile` describes provider- or model-specific kwargs,
pre-initialization side effects, and runtime-derived kwargs that should be
applied when `resolve_model` turns a string spec (e.g. `"openai:gpt-5.4"`)
into a `BaseChatModel`. Profiles are registered via
`register_provider_profile` under a provider key (`"openai"`) or a full
`provider:model` key (`"openai:gpt-5.4"`).

Profiles handle model-construction concerns only — things that shape how
`init_chat_model` assembles the client instance. Typical examples:
constructor kwargs like `use_responses_api`, `temperature`, `max_tokens`,
or `base_url`; provider-specific headers such as OpenRouter app
attribution; pre-construction checks like minimum-version enforcement;
and env-var-aware defaults.

Runtime and harness behavior — system-prompt assembly, tool description
overrides, excluded tools, extra middleware, general-purpose subagent
configuration — belongs in `HarnessProfile`, the separate harness
profile system consumed by `create_deep_agent`, not here.

## Signature

```python
ProviderProfile(
    self,
    init_kwargs: Mapping[str, Any] = dict(),
    pre_init: Callable[[str], None] | None = None,
    init_kwargs_factory: Callable[[], dict[str, Any]] | None = None,
)
```

## Description

**Example:**

Set a default temperature for a hypothetical provider:

```python
from deepagents import ProviderProfile, register_provider_profile

register_provider_profile(
    "my_provider",
    ProviderProfile(init_kwargs={"temperature": 0.7}),
)
```

## Constructors

```python
__init__(
    self,
    init_kwargs: Mapping[str, Any] = dict(),
    pre_init: Callable[[str], None] | None = None,
    init_kwargs_factory: Callable[[], dict[str, Any]] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `init_kwargs` | `Mapping[str, Any]` |
| `pre_init` | `Callable[[str], None] \| None` |
| `init_kwargs_factory` | `Callable[[], dict[str, Any]] \| None` |

## Properties

- `init_kwargs`
- `pre_init`
- `init_kwargs_factory`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L37)
