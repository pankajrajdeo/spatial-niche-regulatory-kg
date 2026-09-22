---
title: "from_examples"
description: "Take examples in list format with prefix and suffix to create a prompt."
source: "https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_examples"
category: "reference"
tags: [reference, langchain-core, prompts, prompt, prompttemplate, from_examples]
---

# from_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_examples)

Take examples in list format with prefix and suffix to create a prompt.

Intended to be used as a way to dynamically create a prompt from examples.

## Signature

```python
from_examples(
    cls,
    examples: list[str],
    suffix: str,
    input_variables: list[str],
    example_separator: str = '\n\n',
    prefix: str = '',
    **kwargs: Any = {},
) -> PromptTemplate
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `examples` | `list[str]` | Yes | List of examples to use in the prompt. |
| `suffix` | `str` | Yes | String to go after the list of examples.  Should generally set up the user's input. |
| `input_variables` | `list[str]` | Yes | A list of variable names the final prompt template will expect. |
| `example_separator` | `str` | No | The separator to use in between examples. (default: `'\n\n'`) |
| `prefix` | `str` | No | String that should go before any examples.  Generally includes examples. (default: `''`) |

## Returns

`PromptTemplate`

The final prompt generated.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/prompt.py#L203)
