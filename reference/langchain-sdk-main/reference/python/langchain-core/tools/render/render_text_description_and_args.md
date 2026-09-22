---
title: "render_text_description_and_args"
description: "Render the tool name, description, and args in plain text."
source: "https://reference.langchain.com/python/langchain-core/tools/render/render_text_description_and_args"
category: "reference"
tags: [reference, langchain-core, tools, render, render_text_description_and_args]
---

# render_text_description_and_args

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/render/render_text_description_and_args)

Render the tool name, description, and args in plain text.

## Signature

```python
render_text_description_and_args(
    tools: list[BaseTool],
) -> str
```

## Description

Output will be in the format of:

```txt
search: This tool is used for search, args: {"query": {"type": "string"}}
calculator: This tool is used for math,     args: {"expression": {"type": "string"}}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tools` | `list[BaseTool]` | Yes | The tools to render. |

## Returns

`str`

The rendered text.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/render.py#L41)
