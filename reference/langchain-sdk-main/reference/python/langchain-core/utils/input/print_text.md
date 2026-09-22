---
title: "print_text"
description: "Print text with highlighting and no end characters."
source: "https://reference.langchain.com/python/langchain-core/utils/input/print_text"
category: "reference"
tags: [reference, langchain-core, utils, input, print_text]
---

# print_text

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/input/print_text)

Print text with highlighting and no end characters.

If a color is provided, the text will be printed in that color.

If a file is provided, the text will be written to that file.

## Signature

```python
print_text(
    text: str,
    color: str | None = None,
    end: str = '',
    file: TextIO | None = None,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The text to print. |
| `color` | `str \| None` | No | The color to use. (default: `None`) |
| `end` | `str` | No | The end character to use. (default: `''`) |
| `file` | `TextIO \| None` | No | The file to write to. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/input.py#L64)
