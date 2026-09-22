---
title: "from_template"
description: "Load a prompt template from a template."
source: "https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_template"
category: "reference"
tags: [reference, langchain-core, prompts, prompt, prompttemplate, from_template]
---

# from_template

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_template)

Load a prompt template from a template.

!!! warning "Security"

    Prefer using `template_format='f-string'` instead of
    `template_format='jinja2'`, or make sure to NEVER accept jinja2 templates
    from untrusted sources as they may lead to arbitrary Python code execution.

    As of LangChain 0.0.329, Jinja2 templates will be rendered using Jinja2's
    SandboxedEnvironment by default. This sand-boxing should be treated as a
    best-effort approach rather than a guarantee of security, as it is an
    opt-out rather than opt-in approach.

    Despite the sandboxing, we recommend to never use jinja2 templates from
    untrusted sources.

## Signature

```python
from_template(
    cls,
    template: str,
    *,
    template_format: PromptTemplateFormat = 'f-string',
    partial_variables: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> PromptTemplate
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template to load. |
| `template_format` | `PromptTemplateFormat` | No | The format of the template.  Use `jinja2` for jinja2, `mustache` for mustache, and `f-string` for f-strings. (default: `'f-string'`) |
| `partial_variables` | `dict[str, Any] \| None` | No | A dictionary of variables that can be used to partially fill in the template.  For example, if the template is `'{variable1} {variable2}'`, and `partial_variables` is `{"variable1": "foo"}`, then the final prompt will be `'foo {variable2}'`. (default: `None`) |
| `**kwargs` | `Any` | No | Any other arguments to pass to the prompt template. (default: `{}`) |

## Returns

`PromptTemplate`

The prompt template loaded from the template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/prompt.py#L256)
