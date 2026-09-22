---
title: "BaseOutputParser"
description: "Base class to parse the output of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser"
category: "reference"
tags: [reference, langchain-core, output_parsers, base, baseoutputparser]
---

# BaseOutputParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser)

Base class to parse the output of an LLM call.

Output parsers help structure language model responses.

## Signature

```python
BaseOutputParser(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
# Implement a simple boolean output parser

class BooleanOutputParser(BaseOutputParser[bool]):
    true_val: str = "YES"
    false_val: str = "NO"

    def parse(self, text: str) -> bool:
        cleaned_text = text.strip().upper()
        if cleaned_text not in (
            self.true_val.upper(),
            self.false_val.upper(),
        ):
            raise OutputParserException(
                f"BooleanOutputParser expected output value to either be "
                f"{self.true_val} or {self.false_val} (case-insensitive). "
                f"Received {cleaned_text}."
            )
        return cleaned_text == self.true_val.upper()

    @property
    def _type(self) -> str:
        return "boolean_output_parser"
```

## Extends

- `BaseLLMOutputParser[T]`
- `RunnableSerializable[LanguageModelOutput, T]`

## Properties

- `InputType`
- `OutputType`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/ainvoke)
- [`parse_result()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/parse_result)
- [`parse()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/parse)
- [`aparse_result()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/aparse_result)
- [`aparse()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/aparse)
- [`parse_with_prompt()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/parse_with_prompt)
- [`get_format_instructions()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/get_format_instructions)
- [`dict()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/dict)
- [`asdict()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/asdict)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/base.py#L140)
