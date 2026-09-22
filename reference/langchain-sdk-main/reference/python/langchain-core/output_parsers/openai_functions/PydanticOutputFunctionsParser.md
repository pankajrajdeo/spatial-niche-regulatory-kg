---
title: "PydanticOutputFunctionsParser"
description: "Parse an output as a Pydantic object."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, pydanticoutputfunctionsparser]
---

# PydanticOutputFunctionsParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser)

Parse an output as a Pydantic object.

This parser is used to parse the output of a chat model that uses OpenAI function
format to invoke functions.

The parser extracts the function call invocation and matches them to the Pydantic
schema provided.

An exception will be raised if the function call does not match the provided schema.

## Signature

```python
PydanticOutputFunctionsParser(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
message = AIMessage(
    content="This is a test message",
    additional_kwargs={
        "function_call": {
            "name": "cookie",
            "arguments": json.dumps({"name": "value", "age": 10}),
        }
    },
)
chat_generation = ChatGeneration(message=message)

class Cookie(BaseModel):
    name: str
    age: int

class Dog(BaseModel):
    species: str

# Full output
parser = PydanticOutputFunctionsParser(
    pydantic_schema={"cookie": Cookie, "dog": Dog}
)
result = parser.parse_result([chat_generation])
```

## Extends

- `OutputFunctionsParser`

## Properties

- `pydantic_schema`

## Methods

- [`validate_schema()`](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/validate_schema)
- [`parse_result()`](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/parse_result)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/openai_functions.py#L179)
