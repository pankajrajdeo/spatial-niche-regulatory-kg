---
title: "parser"
description: "Parser to use for XML parsing."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/parser"
category: "reference"
tags: [reference, langchain-core, output_parsers, xml, xmloutputparser, parser]
---

# parser

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/parser)

Parser to use for XML parsing.

Can be either `'defusedxml'` or `'xml'`.

- `'defusedxml'` is the default parser and is used to prevent XML vulnerabilities
    present in some distributions of Python's standard library xml. `defusedxml` is
    a wrapper around the standard library parser that sets up the parser with secure
    defaults.
- `'xml'` is the standard library parser.

!!! warning

    Use `xml` only if you are sure that your distribution of the standard library is
    not vulnerable to XML vulnerabilities.

Review the following resources for more information:

* https://docs.python.org/3/library/xml.html#xml-vulnerabilities
* https://github.com/tiran/defusedxml

The standard library relies on [`libexpat`](https://github.com/libexpat/libexpat)
for parsing XML.

## Signature

```python
parser: Literal['defusedxml', 'xml'] = 'defusedxml'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/xml.py#L178)
