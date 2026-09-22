---
title: "args_schema"
description: "Pydantic model class to validate and parse the tool's input arguments."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/args_schema"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, args_schema]
---

# args_schema

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/args_schema)

Pydantic model class to validate and parse the tool's input arguments.

Args schema should be either:

- A subclass of `pydantic.BaseModel`.
- A subclass of `pydantic.v1.BaseModel` if accessing v1 namespace in pydantic 2
- A JSON schema dict

## Signature

```python
args_schema: Annotated[ArgsSchema | None, SkipValidation()] = Field(default=None, description='The tool schema.')
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L483)
