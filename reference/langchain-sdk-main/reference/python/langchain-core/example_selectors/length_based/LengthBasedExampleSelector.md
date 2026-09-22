---
title: "LengthBasedExampleSelector"
description: "Select examples based on length."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector"
category: "reference"
tags: [reference, langchain-core, example_selectors, length_based, lengthbasedexampleselector]
---

# LengthBasedExampleSelector

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector)

Select examples based on length.

## Signature

```python
LengthBasedExampleSelector()
```

## Description

**Example:**

```python
from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import PromptTemplate

# Define examples
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "fast", "output": "slow"},
]

# Create prompt template
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)

# Create selector with max length constraint
selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50,  # Maximum prompt length
)

# Select examples for a new input
selected = selector.select_examples({"input": "large", "output": "tiny"})
# Returns examples that fit within max_length constraint
```

## Extends

- `BaseExampleSelector`
- `BaseModel`

## Properties

- `examples`
- `example_prompt`
- `get_text_length`
- `max_length`
- `example_text_lengths`

## Methods

- [`add_example()`](https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector/add_example)
- [`aadd_example()`](https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector/aadd_example)
- [`post_init()`](https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector/post_init)
- [`select_examples()`](https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector/select_examples)
- [`aselect_examples()`](https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector/aselect_examples)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/example_selectors/length_based.py#L18)
