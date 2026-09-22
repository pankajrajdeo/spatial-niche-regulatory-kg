---
title: "TextAccessor"
description: "String-like object that supports both property and method access patterns."
source: "https://reference.langchain.com/python/langchain-core/messages/base/TextAccessor"
category: "reference"
tags: [reference, langchain-core, messages, base, textaccessor]
---

# TextAccessor

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/TextAccessor)

String-like object that supports both property and method access patterns.

Exists to maintain backward compatibility while transitioning from method-based to
property-based text access in message objects. In LangChain <v1.0, message text was
accessed via `.text()` method calls. In v1.0=<, the preferred pattern is property
access via `.text`.

Rather than breaking existing code immediately, `TextAccessor` allows both
patterns:
- Modern property access: `message.text` (returns string directly)
- Legacy method access: `message.text()` (callable, emits deprecation warning)

## Signature

```python
TextAccessor()
```

## Extends

- `str`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/base.py#L47)
