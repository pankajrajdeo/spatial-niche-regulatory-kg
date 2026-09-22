---
title: "nested_element"
description: "Get nested element from path."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/xml/nested_element"
category: "reference"
tags: [reference, langchain-core, output_parsers, xml, nested_element]
---

# nested_element

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/xml/nested_element)

Get nested element from path.

## Signature

```python
nested_element(
    path: list[str],
    elem: ET.Element,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `list[str]` | Yes | The path to the element. |
| `elem` | `ET.Element` | Yes | The element to extract. |

## Returns

`Any`

The nested element.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/xml.py#L289)
