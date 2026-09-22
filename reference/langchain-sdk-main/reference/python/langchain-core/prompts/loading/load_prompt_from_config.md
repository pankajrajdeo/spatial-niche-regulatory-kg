---
title: "load_prompt_from_config"
description: "Load prompt from config dict."
source: "https://reference.langchain.com/python/langchain-core/prompts/loading/load_prompt_from_config"
category: "reference"
tags: [reference, langchain-core, prompts, loading, load_prompt_from_config]
---

# load_prompt_from_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/loading/load_prompt_from_config)

Load prompt from config dict.

## Signature

```python
load_prompt_from_config(
    config: dict[str, Any],
    *,
    allow_dangerous_paths: bool = False,
) -> BasePromptTemplate[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `dict[str, Any]` | Yes | Dict containing the prompt configuration. |
| `allow_dangerous_paths` | `bool` | No | If `False` (default), file paths in the config (such as `template_path`, `examples`, and `example_prompt_path`) are validated to reject absolute paths and directory traversal (`..`) sequences. Set to `True` only if you trust the source of the config. (default: `False`) |

## Returns

`BasePromptTemplate[str]`

A `PromptTemplate` object.

## ⚠️ Deprecated

Deprecated since version 1.2.21. Use Use `dumpd`/`dumps` from `langchain_core.load` to serialize prompts and `load`/`loads` to deserialize them. instead. Will be removed in version 2.0.0.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/loading.py#L49)
