---
title: "init_kwargs"
description: "Static keyword arguments forwarded to init_chat_model."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile/init_kwargs"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, providerprofile, init_kwargs]
---

# init_kwargs

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile/init_kwargs)

Static keyword arguments forwarded to `init_chat_model`.

Once a profile is constructed, its kwargs can be read but not
rewritten — for example, `profile.init_kwargs["temperature"] = 2.0`
raises `TypeError`. The registry stores its own defensive copy, so
mutating the dict you passed into the constructor after the fact won't
affect the registered profile either. To change a registered profile's
kwargs, re-register (which merges on top) or construct a new profile.

When both `init_kwargs` and `init_kwargs_factory` are set on the same
profile, the factory's output overrides `init_kwargs` on key collision.

## Signature

```python
init_kwargs: Mapping[str, Any] = field(default_factory=dict)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L79)
