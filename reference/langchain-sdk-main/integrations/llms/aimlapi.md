---
title: "AIMLAPI integration"
description: "Integrate with the AIMLAPI LLM using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/llms/aimlapi"
category: "docs"
tags: [docs, integrations, llms, aimlapi]
---

# AIMLAPI integration

> Integrate with the AIMLAPI LLM using LangChain Python.

> [!WARNING]
> **You are currently on a page documenting the use of AI/ML API models as text completion models. Many of the latest and most popular AI/ML API models are [chat completion models](../../langchain/models.md).**
>
> You may be looking for the [AI/ML API chat docs](https://docs.aimlapi.com/).

This page helps you get started with AI/ML API text completion models.

## Overview

### Integration details

| Class        | Package             | Local | Serializable | JS support |                                              Downloads                                             |                                             Version                                             |
| :----------- | :------------------ | :---: | :----------: | :--------: | :------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: |
| `AimlapiLLM` | `langchain-aimlapi` |   ❌   |     beta     |      ❌     | ![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain-aimlapi?style=flat-square\&label=%20) | ![PyPI - Version](https://img.shields.io/pypi/v/langchain-aimlapi?style=flat-square\&label=%20) |

### Model features

| [Tool calling](../../langchain/tools.md) | [Structured output](../../langchain/structured-output.md) | [Image input](../../langchain/messages.md#multimodal) | Audio input | Video input | [Token-level streaming](../../langchain/streaming.md) | Native async | [Token usage](../../langchain/models.md#token-usage) | [Logprobs](../../langchain/models.md#log-probabilities) |
| :-----------------------------------------: | :----------------------------------------------------------: | :------------------------------------------------------: | :---------: | :---------: | :-------------------------------------------------------: | :----------: | :-----------------------------------------------------: | :--------------------------------------------------------: |
|                      ❌                      |                               ❌                              |                             ❌                            |      ❌      |      ❌      |                             ❌                             |       ✅      |                            ❌                            |                              ❌                             |

## Setup

To access AI/ML API models you'll need to create an account, get an API key, and install the `langchain-aimlapi` integration package.

### Credentials

Head to [aimlapi.com](https://aimlapi.com/app/?utm_source=langchain\&utm_medium=github\&utm_campaign=integration) to sign up and generate an API key. Once you've done this set the `AIMLAPI_API_KEY` environment variable:

```python
import getpass
import os

if not os.getenv("AIMLAPI_API_KEY"):
    os.environ["AIMLAPI_API_KEY"] = getpass.getpass("Enter your AI/ML API key: ")
```

To enable automated tracing of your model calls, set your [LangSmith](../../langsmith/observability.md) API key:

```python
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
```

### Installation

The LangChain AI/ML API integration lives in the `langchain-aimlapi` package:

```python
pip install -qU langchain-aimlapi
```

## Instantiation

Now we can instantiate our model object and generate text completions:

```python
from langchain_aimlapi import AimlapiLLM

llm = AimlapiLLM(
    model="openai/gpt-5-5",
    temperature=0.5,
    max_tokens=1024,
)
```

## Invocation

```python
response = llm.invoke("Explain the bubble sort algorithm in Python.")
print(response)
```

```text
Bubble sort is a simple sorting algorithm that repeatedly steps through a list, compares adjacent items, and swaps them when they are out of order. The process repeats until the entire list is sorted. While easy to understand and implement, bubble sort is inefficient on large datasets because it has quadratic time complexity.
```

***

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/aimlapi.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
