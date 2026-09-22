---
title: "HarnessProfileConfig"
description: "Declarative harness-profile config for YAML/JSON-backed profiles."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig]
---

# HarnessProfileConfig

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig)

Declarative harness-profile config for YAML/JSON-backed profiles.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../../versioning.md)
    for more details.

A `HarnessProfileConfig` contains the file-friendly subset of harness
settings: plain strings, bools, lists, and nested dicts that can be loaded
from YAML or JSON. For in-code/runtime-only adjustments such as
`extra_middleware` or class-form `excluded_middleware`, use
`HarnessProfile` instead.

!!! note "Class-path serialization"

    `excluded_middleware` in config files currently only accepts plain
    middleware-name strings matched against `AgentMiddleware.name`. A
    future revision may add explicit class-path (`module:Class`) entries
    for excluding middleware whose class isn't part of the public import
    surface; until then, exclude such middleware via its `.name` (using
    `serialized_name` for stable public aliases) or stay on the runtime
    `HarnessProfile` and pass the class directly.

Config objects may be passed directly to `register_harness_profile`; the
helper converts them to runtime `HarnessProfile` objects automatically.

## Signature

```python
HarnessProfileConfig(
    self,
    base_system_prompt: str | None = None,
    system_prompt_suffix: str | None = None,
    tool_description_overrides: Mapping[str, str] = dict(),
    excluded_tools: frozenset[str] = frozenset(),
    excluded_middleware: frozenset[str] = frozenset(),
    general_purpose_subagent: GeneralPurposeSubagentProfile | None = None,
)
```

## Description

**Example:**

Construct a config object directly in Python:

```python
from deepagents import HarnessProfileConfig, register_harness_profile

register_harness_profile(
    "openai:gpt-5.4",
    HarnessProfileConfig(
        system_prompt_suffix="Think step by step.",
        excluded_middleware={"SummarizationMiddleware"},
    ),
)
```

Or load the equivalent declarative form from YAML:

```yaml
# openai-gpt-5.4.yaml
system_prompt_suffix: Think step by step.
excluded_middleware:
  - SummarizationMiddleware
```

```python
import yaml
from deepagents import HarnessProfileConfig, register_harness_profile

with open("openai-gpt-5.4.yaml") as f:
    register_harness_profile(
        "openai:gpt-5.4",
        HarnessProfileConfig.from_dict(yaml.safe_load(f)),
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
    excluded_middleware: frozenset[str] = frozenset(),
    general_purpose_subagent: GeneralPurposeSubagentProfile | None = None,
) -> None
```

| Name | Type |
|------|------|
| `base_system_prompt` | `str \| None` |
| `system_prompt_suffix` | `str \| None` |
| `tool_description_overrides` | `Mapping[str, str]` |
| `excluded_tools` | `frozenset[str]` |
| `excluded_middleware` | `frozenset[str]` |
| `general_purpose_subagent` | `GeneralPurposeSubagentProfile \| None` |

## Properties

- `base_system_prompt`
- `system_prompt_suffix`
- `tool_description_overrides`
- `excluded_tools`
- `excluded_middleware`
- `general_purpose_subagent`

## Methods

- [`to_dict()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_dict)
- [`from_dict()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/from_dict)
- [`to_harness_profile()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_harness_profile)
- [`from_harness_profile()`](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/from_harness_profile)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L191)
