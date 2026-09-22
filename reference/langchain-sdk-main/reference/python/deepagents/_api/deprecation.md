---
title: "deprecation"
description: "Adapter for langchain_core's private deprecation helpers."
source: "https://reference.langchain.com/python/deepagents/_api/deprecation"
category: "reference"
tags: [reference, deepagents, api, deprecation]
---

# deprecation

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_api/deprecation)

Adapter for `langchain_core`'s private deprecation helpers.

Centralizes the import surface so an upstream rename or move is a one-file
change.

Re-exports:
- `deprecated`: decorator for callables, classes, and properties.
- `warn_deprecated`: helper for parameter/value-level deprecations where the
    callable itself isn't being deprecated. Wraps the upstream helper to
    accept a `stacklevel` argument (the upstream version hardcodes
    `stacklevel=4`, which mis-attributes warnings emitted directly from a
    deprecated method body).
- `suppress_langchain_deprecation_warning`: context manager that silences
    emissions from this module's helpers (use sparingly — it is type-wide).
- `LangChainDeprecationWarning`: warning class emitted by the helpers above
    (subclass of `DeprecationWarning`).

## Methods

- [`warn_deprecated()`](https://reference.langchain.com/python/deepagents/_api/deprecation/warn_deprecated)
- [`reset_deprecation_dedupe()`](https://reference.langchain.com/python/deepagents/_api/deprecation/reset_deprecation_dedupe)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/_api/deprecation.py)
