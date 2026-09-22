---
title: "validate_profile_key"
description: "Validate a provider or provider:model profile registry key."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/validate_profile_key"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, validate_profile_key]
---

# validate_profile_key

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/_keys/validate_profile_key)

Validate a `provider` or `provider:model` profile registry key.

The first colon separates the provider from the complete model identifier.
Providers must not contain colons, while model identifiers may contain them;
for example, `ollama:glm-5.2:cloud` identifies provider `ollama` and model
`glm-5.2:cloud`.

Only the first colon is structural. The complete model identifier must be
nonempty and have no surrounding whitespace; its internal syntax belongs
to the provider. In particular, Bedrock foundation-model ARNs can contain
`::` because their account component is empty.

## Signature

```python
validate_profile_key(
    key: str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The registry key to check. |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/_keys.py#L11)
