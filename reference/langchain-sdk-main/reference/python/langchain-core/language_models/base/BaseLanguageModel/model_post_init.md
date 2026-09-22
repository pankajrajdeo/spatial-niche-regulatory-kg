---
title: "model_post_init"
description: "Pydantic V2 lifecycle hook called automatically after init."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/model_post_init"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, model_post_init]
---

# model_post_init

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/model_post_init)

Pydantic V2 lifecycle hook called automatically after `__init__`.

Seeds `metadata["lc_versions"]` with the installed `langchain-core`
(and `langchain`, if installed) versions so that every LLM trace
carries the package versions that produced it.

Partner packages should **not** override this method. Instead, they
should define a `@model_validator(mode="after")` that calls
`_add_version` to append their own version to the same dict.

!!! warning "Validator naming"

    Each subclass's validator **must** have a unique name. Pydantic
    replaces — rather than chains — same-named `model_validator` methods
    in child classes. For example, a `BaseChatOpenAI` subclass should
    use `_set_<partner>_version`, not `_set_version`, to avoid silently
    dropping the parent's entry.

## Signature

```python
model_post_init(
    self,
    _context: Any,
    /,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `_context` | `Any` | Yes | Pydantic validation context (typically `None`). |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/base.py#L222)
