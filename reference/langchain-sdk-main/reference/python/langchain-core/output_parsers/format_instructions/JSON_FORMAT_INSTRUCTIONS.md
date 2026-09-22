---
title: "JSON_FORMAT_INSTRUCTIONS"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/output_parsers/format_instructions/JSON_FORMAT_INSTRUCTIONS"
category: "reference"
tags: [reference, langchain-core, output_parsers, format_instructions, json_format_instructions]
---

# JSON_FORMAT_INSTRUCTIONS

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/format_instructions/JSON_FORMAT_INSTRUCTIONS)

## Signature

```python
JSON_FORMAT_INSTRUCTIONS = 'STRICT OUTPUT FORMAT:\n- Return only the JSON value that conforms to the schema. Do not include any additional text, explanations, headings, or separators.\n- Do not wrap the JSON in Markdown or code fences (no ``` or ```json).\n- Do not prepend or append any text (e.g., do not write "Here is the JSON:").\n- The response must be a single top-level JSON value exactly as required by the schema (object/array/etc.), with no trailing commas or comments.\n\nThe output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}} the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schema. The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.\n\nHere is the output schema (shown in a code block for readability only — do not include any backticks or Markdown in your output):\n```\n{schema}\n```'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/format_instructions.py#L3)
