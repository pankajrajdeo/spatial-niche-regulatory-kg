---
title: "HarnessProfile"
description: "Runtime configuration for deep agent behavior."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofile]
---

# HarnessProfile

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile)

Runtime configuration for deep agent behavior.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../../versioning.md)
    for more details.

A `HarnessProfile` describes prompt-assembly, tool visibility, middleware,
and default-subagent adjustments applied by `create_deep_agent` once a
chat model has been constructed. Profiles are registered via
`register_harness_profile` under a provider key (`"openai"`) or a full
`provider:model` key (`"openai:gpt-5.4"`).

This complements `ProviderProfile`, which controls the model-construction
phase (e.g. `init_chat_model` kwargs, pre-init side effects). Concerns
that shape *how the model is built* belong in `ProviderProfile`; concerns
that shape *how the agent runs* belong here.

For YAML/JSON-backed profiles, use `HarnessProfileConfig`, which contains
only the declarative subset and can be passed directly to
`register_harness_profile`.

The `extra_middleware` field expects
`langchain.agents.middleware.types.AgentMiddleware` instances or a
factory returning a sequence of them.

## Signature

```python
HarnessProfile(
    self,
    base_system_prompt: str | None = None,
    system_prompt_suffix: str | None = None,
    tool_description_overrides: Mapping[str, str] = dict(),
    excluded_tools: frozenset[str] = frozenset(),
    excluded_middleware: frozenset[type[AgentMiddleware] | str] = frozenset(),
    extra_middleware: Sequence[AgentMiddleware] | Callable[[], Sequence[AgentMiddleware]] = (),
    general_purpose_subagent: GeneralPurposeSubagentProfile | None = None,
)
```

## Description

**Example:**

Minimal — append a model-specific system-prompt suffix:

```python
from deepagents import HarnessProfile, register_harness_profile

register_harness_profile(
    "openai:gpt-5.4",
    HarnessProfile(system_prompt_suffix="Think step by step."),
)
```

Richer — combine prompt tuning, tool exclusion, and a tweak to the
auto-added general-purpose subagent:

```python
from deepagents import (
    GeneralPurposeSubagentProfile,
    HarnessProfile,
    register_harness_profile,
)

register_harness_profile(
    "openai:gpt-5.4",
    HarnessProfile(
        system_prompt_suffix="Respond in under 100 words.",
        excluded_tools=frozenset({"execute"}),
        general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False),
    ),
)
```

## Constructors

```python
__init__(
    self,
    base_system_prompt: str | None = None,
    system_prompt_suffix: str | None = None,
    tool_description_overrides: Mapping[str, str] = dict(),
    excluded_tools: frozenset[str] = frozenset(),
    excluded_middleware: frozenset[type[AgentMiddleware] | str] = frozenset(),
    extra_middleware: Sequence[AgentMiddleware] | Callable[[], Sequence[AgentMiddleware]] = (),
    general_purpose_subagent: GeneralPurposeSubagentProfile | None = None,
) -> None
```

| Name | Type |
|------|------|
| `base_system_prompt` | `str \| None` |
| `system_prompt_suffix` | `str \| None` |
| `tool_description_overrides` | `Mapping[str, str]` |
| `excluded_tools` | `frozenset[str]` |
| `excluded_middleware` | `frozenset[type[AgentMiddleware] \| str]` |
| `extra_middleware` | `Sequence[AgentMiddleware] \| Callable[[], Sequence[AgentMiddleware]]` |
| `general_purpose_subagent` | `GeneralPurposeSubagentProfile \| None` |

## Properties

- `base_system_prompt`
- `system_prompt_suffix`
- `tool_description_overrides`
- `excluded_tools`
- `excluded_middleware`
- `extra_middleware`
- `general_purpose_subagent`

## Methods

- [`materialize_extra_middleware()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/materialize_extra_middleware)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L482)
