---
title: "ImagePromptTemplate"
description: "Image prompt template for a multimodal model."
source: "https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, image, imageprompttemplate]
---

# ImagePromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate)

Image prompt template for a multimodal model.

## Signature

```python
ImagePromptTemplate(
    self,
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
prompt = ImagePromptTemplate(
    input_variables=["image_id"],
    template={"url": "https://example.com/{image_id}.png", "detail": "high"},
    template_format="f-string",
)
prompt.format(image_id="cat")
# {"url": "https://example.com/cat.png", "detail": "high"}
```

## Extends

- `BasePromptTemplate[ImageURL]`

## Constructors

```python
__init__(
    self,
    **kwargs: Any = {},
) -> None
```

## Properties

- `template`
- `template_format`

## Methods

- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/get_lc_namespace)
- [`format_prompt()`](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/format_prompt)
- [`aformat_prompt()`](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/aformat_prompt)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/format)
- [`aformat()`](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/aformat)
- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/pretty_repr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/image.py#L17)
