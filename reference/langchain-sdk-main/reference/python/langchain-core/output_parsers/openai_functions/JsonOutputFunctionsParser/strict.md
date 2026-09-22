---
title: "strict"
description: "Whether to allow non-JSON-compliant strings."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/JsonOutputFunctionsParser/strict"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, jsonoutputfunctionsparser, strict]
---

# strict

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/JsonOutputFunctionsParser/strict)

Whether to allow non-JSON-compliant strings.

See: https://docs.python.org/3/library/json.html#encoders-and-decoders

Useful when the parsed output may include unicode characters or new lines.

## Signature

```python
strict: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/openai_functions.py#L61)
