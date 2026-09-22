---
title: "PromptTemplate"
description: "Prompt template for a language model."
source: "https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, prompt, prompttemplate]
---

# PromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate)

Prompt template for a language model.

A prompt template consists of a string template. It accepts a set of parameters
from the user that can be used to generate a prompt for a language model.

The template can be formatted using either f-strings (default), jinja2, or mustache
syntax.

!!! warning "Security"

    Prefer using `template_format='f-string'` instead of `template_format='jinja2'`,
    or make sure to NEVER accept jinja2 templates from untrusted sources as they may
    lead to arbitrary Python code execution.

    As of LangChain 0.0.329, Jinja2 templates will be rendered using Jinja2's
    SandboxedEnvironment by default. This sand-boxing should be treated as a
    best-effort approach rather than a guarantee of security, as it is an opt-out
    rather than opt-in approach.

    Despite the sandboxing, we recommend to never use jinja2 templates from
    untrusted sources.

## Signature

```python
PromptTemplate(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
from langchain_core.prompts import PromptTemplate

# Instantiation using from_template (recommended)
prompt = PromptTemplate.from_template("Say {foo}")
prompt.format(foo="bar")

# Instantiation using initializer
prompt = PromptTemplate(template="Say {foo}")
```

## Extends

- `StringPromptTemplate`

## Properties

- `lc_attributes`
- `template`
- `template_format`
- `validate_template`

## Methods

- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/get_lc_namespace)
- [`pre_init_validation()`](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/pre_init_validation)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/get_input_schema)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/format)
- [`from_examples()`](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_examples)
- [`from_file()`](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_file)
- [`from_template()`](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_template)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/prompt.py#L24)
