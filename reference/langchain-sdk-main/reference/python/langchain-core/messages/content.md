---
title: "content"
description: "Standard, multimodal content blocks for Large Language Model I/O."
source: "https://reference.langchain.com/python/langchain-core/messages/content"
category: "reference"
tags: [reference, langchain-core, messages, content]
---

# content

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content)

Standard, multimodal content blocks for Large Language Model I/O.

This module provides standardized data structures for representing inputs to and outputs
from LLMs. The core abstraction is the **Content Block**, a `TypedDict`.

**Rationale**

Different LLM providers use distinct and incompatible API schemas. This module provides
a unified, provider-agnostic format to facilitate these interactions. A message to or
from a model is simply a list of content blocks, allowing for the natural interleaving
of text, images, and other content in a single ordered sequence.

An adapter for a specific provider is responsible for translating this standard list of
blocks into the format required by its API.

**Extensibility**

Data **not yet mapped** to a standard block may be represented using the
`NonStandardContentBlock`, which allows for provider-specific data to be included
without losing the benefits of type checking and validation.

Furthermore, provider-specific fields **within** a standard block are fully supported
by default in the `extras` field of each block. This allows for additional metadata
to be included without breaking the standard structure. For example, Google's thought
signature:

```python
AIMessage(
    content=[
        {
            "type": "text",
            "text": "J'adore la programmation.",
            "extras": {"signature": "EpoWCpc..."},  # Thought signature
        }
    ], ...
)
```

!!! note

    Following widespread adoption of [PEP 728](https://peps.python.org/pep-0728/), we
    intend to add `extra_items=Any` as a param to Content Blocks. This will signify to
    type checkers that additional provider-specific fields are allowed outside of the
    `extras` field, and that will become the new standard approach to adding
    provider-specific metadata.

    ??? note

        **Example with PEP 728 provider-specific fields:**

```python
        # Content block definition
        # NOTE: `extra_items=Any`
        class TextContentBlock(TypedDict, extra_items=Any):
            type: Literal["text"]
            id: NotRequired[str]
            text: str
            annotations: NotRequired[list[Annotation]]
            index: NotRequired[int]
```

```python
        from langchain_core.messages.content import TextContentBlock

        # Create a text content block with provider-specific fields
        my_block: TextContentBlock = {
            # Add required fields
            "type": "text",
            "text": "Hello, world!",
            # Additional fields not specified in the TypedDict
            # These are valid with PEP 728 and are typed as Any
            "openai_metadata": {"model": "gpt-5.5", "temperature": 0.7},
            "anthropic_usage": {"input_tokens": 10, "output_tokens": 20},
            "custom_field": "any value",
        }

        # Mutating an existing block to add provider-specific fields
        openai_data = my_block["openai_metadata"]  # Type: Any
```

**Example Usage**

```python
# Direct construction
from langchain_core.messages.content import TextContentBlock, ImageContentBlock

multimodal_message: AIMessage(
    content_blocks=[
        TextContentBlock(type="text", text="What is shown in this image?"),
        ImageContentBlock(
            type="image",
            url="https://www.langchain.com/images/brand/langchain_logo_text_w_white.png",
            mime_type="image/png",
        ),
    ]
)

# Using factories
from langchain_core.messages.content import create_text_block, create_image_block

multimodal_message: AIMessage(
    content=[
        create_text_block("What is shown in this image?"),
        create_image_block(
            url="https://www.langchain.com/images/brand/langchain_logo_text_w_white.png",
            mime_type="image/png",
        ),
    ]
)
```

Factory functions offer benefits such as:

- Automatic ID generation (when not provided)
- No need to manually specify the `type` field

## Properties

- `KNOWN_BLOCK_TYPES`

## Methods

- [`ensure_id()`](https://reference.langchain.com/python/langchain-core/messages/content/ensure_id)
- [`is_data_content_block()`](https://reference.langchain.com/python/langchain-core/messages/content/is_data_content_block)
- [`create_text_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_text_block)
- [`create_image_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_image_block)
- [`create_video_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_video_block)
- [`create_audio_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_audio_block)
- [`create_file_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_file_block)
- [`create_plaintext_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_plaintext_block)
- [`create_tool_call()`](https://reference.langchain.com/python/langchain-core/messages/content/create_tool_call)
- [`create_reasoning_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_reasoning_block)
- [`create_citation()`](https://reference.langchain.com/python/langchain-core/messages/content/create_citation)
- [`create_non_standard_block()`](https://reference.langchain.com/python/langchain-core/messages/content/create_non_standard_block)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py)
