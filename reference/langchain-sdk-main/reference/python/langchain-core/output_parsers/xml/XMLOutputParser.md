---
title: "XMLOutputParser"
description: "Parse an output using xml format."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser"
category: "reference"
tags: [reference, langchain-core, output_parsers, xml, xmloutputparser]
---

# XMLOutputParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser)

Parse an output using xml format.

Returns a dictionary of tags.

## Signature

```python
XMLOutputParser(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseTransformOutputParser[dict[str, Any]]`

## Properties

- `tags`
- `encoding_matcher`
- `parser`

## Methods

- [`get_format_instructions()`](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/get_format_instructions)
- [`parse()`](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/parse)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/xml.py#L152)
