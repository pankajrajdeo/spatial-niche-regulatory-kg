---
title: "tags"
description: "Tags to tell the LLM to expect in the XML output."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/tags"
category: "reference"
tags: [reference, langchain-core, output_parsers, xml, xmloutputparser, tags]
---

# tags

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/tags)

Tags to tell the LLM to expect in the XML output.

    Note this may not be perfect depending on the LLM implementation.

    For example, with `tags=["foo", "bar", "baz"]`:

    1. A well-formatted XML instance:
        `'<foo>
   <bar>
      <baz></baz>
   </bar>
</foo>'`

    2. A badly-formatted XML instance (missing closing tag for 'bar'):
        `'<foo>
   <bar>
   </foo>'`

    3. A badly-formatted XML instance (unexpected 'tag' element):
        `'<foo>
   <tag>
   </tag>
</foo>'`

## Signature

```python
tags: list[str] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/xml.py#L158)
