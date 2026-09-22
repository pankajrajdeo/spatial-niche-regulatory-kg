---
title: "jinja2_formatter"
description: "Format a template using jinja2."
source: "https://reference.langchain.com/python/langchain-core/prompts/string/jinja2_formatter"
category: "reference"
tags: [reference, langchain-core, prompts, string, jinja2_formatter]
---

# jinja2_formatter

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/jinja2_formatter)

Format a template using jinja2.

!!! warning "Security"

    As of LangChain 0.0.329, this method uses Jinja2's `SandboxedEnvironment` by
    default. However, this sandboxing should be treated as a best-effort approach
    rather than a guarantee of security.

    Do not accept jinja2 templates from untrusted sources as they may lead
    to arbitrary Python code execution.

    [More information.](https://jinja.palletsprojects.com/en/3.1.x/sandbox/)

## Signature

```python
jinja2_formatter(
    template: str,
    /,
    **kwargs: Any = {},
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |
| `**kwargs` | `Any` | No | The variables to format the template with. (default: `{}`) |

## Returns

`str`

The formatted string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/string.py#L33)
