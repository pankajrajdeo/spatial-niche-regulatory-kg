---
title: "PydanticOutputParser"
description: "Parse an output using a Pydantic model."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser"
category: "reference"
tags: [reference, langchain-core, output_parsers, pydantic, pydanticoutputparser]
---

# PydanticOutputParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser)

Parse an output using a Pydantic model.

## Signature

```python
PydanticOutputParser(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `JsonOutputParser`
- `Generic[TBaseModel]`

## Properties

- `pydantic_object`
- `OutputType`

## Methods

- [`parse_result()`](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse_result)
- [`parse()`](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse)
- [`get_format_instructions()`](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/get_format_instructions)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/pydantic.py#L19)
