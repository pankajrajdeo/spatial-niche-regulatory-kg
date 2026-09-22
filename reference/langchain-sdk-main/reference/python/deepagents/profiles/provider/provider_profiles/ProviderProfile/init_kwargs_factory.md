---
title: "init_kwargs_factory"
description: "Optional factory producing dynamic init kwargs at resolution time."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile/init_kwargs_factory"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, providerprofile, init_kwargs_factory]
---

# init_kwargs_factory

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile/init_kwargs_factory)

Optional factory producing dynamic init kwargs at resolution time.

Use when values depend on runtime state such as environment variables.

Within a single profile, whenever the factory and `init_kwargs` set the
same key, the factory's value wins. For example:

```python
ProviderProfile(
    init_kwargs={"temperature": 0, "timeout": 30},
    init_kwargs_factory=lambda: {"temperature": 0.7, "base_url": os.environ["BASE_URL"]},
)
```

At resolution, this forwards `temperature=0.7` (factory wins),
`timeout=30` (only in static), and `base_url=<env value>` (only from
factory) to `init_chat_model`.

When merging profiles, if both the base and override profiles define a
factory, both run at every resolution — base first, then override — and
their outputs merge with the override's values winning on any shared
keys. A worked example: the built-in OpenRouter factory always sets
`app_url` and `app_title`; layer a user profile whose factory reads a
per-tenant `OPENROUTER_APP_TITLE_TENANT` env var and sets `app_title`
from it. Every resolution runs both factories; the user's `app_title`
replaces the built-in, while the built-in's `app_url` is preserved.

## Signature

```python
init_kwargs_factory: Callable[[], dict[str, Any]] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L103)
