---
title: "output_parsers"
description: "OutputParser classes parse the output of an LLM call into structured data."
source: "https://reference.langchain.com/python/langchain-core/output_parsers"
category: "reference"
tags: [reference, langchain-core, output_parsers]
---

# output_parsers

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers)

`OutputParser` classes parse the output of an LLM call into structured data.

!!! tip "Structured output"

    Output parsers emerged as an early solution to the challenge of obtaining structured
    output from LLMs.

    Today, most LLMs support [structured output](../../../langchain/models.md#structured-outputs)
    natively. In such cases, using output parsers may be unnecessary, and you should
    leverage the model's built-in capabilities for structured output. Refer to the
    [documentation of your chosen model](../../../integrations/providers/overview.md)
    for guidance on how to achieve structured output directly.

    Output parsers remain valuable when working with models that do not support
    structured output natively, or when you require additional processing or validation
    of the model's output beyond its inherent capabilities.

## Properties

- `SimpleJsonOutputParser`

## Methods

- [`import_attr()`](https://reference.langchain.com/python/langchain-core/output_parsers/import_attr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/__init__.py)
