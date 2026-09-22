---
title: "reset_deprecation_dedupe"
description: "Reset the @deprecated decorator's dedupe flag for testing."
source: "https://reference.langchain.com/python/deepagents/_api/deprecation/reset_deprecation_dedupe"
category: "reference"
tags: [reference, deepagents, api, deprecation, reset_deprecation_dedupe]
---

# reset_deprecation_dedupe

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_api/deprecation/reset_deprecation_dedupe)

Reset the `@deprecated` decorator's dedupe flag for testing.

The langchain_core `@deprecated` decorator emits each warning at most once
per process via a closure-bound `warned` flag. Tests that assert per-call
emission must reset that flag between cases — otherwise the assertions
become reorder-sensitive (notably under `pytest -n auto`).

Accepts decorated functions, methods, and `property` objects (in which
case the `fget` closure is reset). Targets without the expected `warned`
freevar are silently skipped, so passing non-decorated callables is safe.

## Signature

```python
reset_deprecation_dedupe(
    *targets: object = (),
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*targets` | `object` | No | Decorated callables (or properties wrapping them) to reset. (default: `()`) |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/_api/deprecation.py#L100)
