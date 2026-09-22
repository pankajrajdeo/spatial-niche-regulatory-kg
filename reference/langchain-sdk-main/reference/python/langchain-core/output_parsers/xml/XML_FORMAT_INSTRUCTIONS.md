---
title: "XML_FORMAT_INSTRUCTIONS"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/output_parsers/xml/XML_FORMAT_INSTRUCTIONS"
category: "reference"
tags: [reference, langchain-core, output_parsers, xml, xml_format_instructions]
---

# XML_FORMAT_INSTRUCTIONS

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XML_FORMAT_INSTRUCTIONS)

## Signature

```python
XML_FORMAT_INSTRUCTIONS = 'The output should be formatted as a XML file.\n1. Output should conform to the tags below.\n2. If tags are not given, make them on your own.\n3. Remember to always open and close all the tags.\n\nAs an example, for the tags ["foo", "bar", "baz"]:\n1. String "<foo>\n   <bar>\n      <baz></baz>\n   </bar>\n</foo>" is a well-formatted instance of the schema.\n2. String "<foo>\n   <bar>\n   </foo>" is a badly-formatted instance.\n3. String "<foo>\n   <tag>\n   </tag>\n</foo>" is a badly-formatted instance.\n\nHere are the output tags:\n```\n{tags}\n```'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/xml.py#L26)
