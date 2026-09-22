---
title: "set_verbose"
description: "If verbose is None, set it."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/set_verbose"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, set_verbose]
---

# set_verbose

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/set_verbose)

If verbose is `None`, set it.

This allows users to pass in `None` as verbose to access the global setting.

## Signature

```python
set_verbose(
    cls,
    verbose: bool | None,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `verbose` | `bool \| None` | Yes | The verbosity setting to use. |

## Returns

`bool`

The verbosity setting to use.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/base.py#L291)
