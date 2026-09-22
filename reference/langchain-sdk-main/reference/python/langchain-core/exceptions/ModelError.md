---
title: "ModelError"
description: "Base exception for failures related to model invocation."
source: "https://reference.langchain.com/python/langchain-core/exceptions/ModelError"
category: "reference"
tags: [reference, langchain-core, exceptions, modelerror]
---

# ModelError

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/exceptions/ModelError)

Base exception for failures related to model invocation.

Subclasses correspond to conditions that model providers report consistently,
keyed to the HTTP status they surface it with, so the same condition maps to
the same exception type regardless of provider.

Provider integrations raise subclasses that also inherit from the provider
SDK's own exception type, so code catching either continues to work.

## Signature

```python
ModelError()
```

## Extends

- `LangChainException`

## Properties

- `is_retryable`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/exceptions.py#L68)
