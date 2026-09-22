---
title: "OVERRIDABLE_LANGSMITH_INHERITABLE_METADATA_KEYS"
description: "Allowlist of LangSmith-only tracing metadata keys that bypass the default \"first wins\" merge semantics used when propagating tracer metadata to nested runs."
source: "https://reference.langchain.com/python/langchain-core/tracers/langchain/OVERRIDABLE_LANGSMITH_INHERITABLE_METADATA_KEYS"
category: "reference"
tags: [reference, langchain-core, tracers, langchain, overridable_langsmith_inheritable_metadata_keys]
---

# OVERRIDABLE_LANGSMITH_INHERITABLE_METADATA_KEYS

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/langchain/OVERRIDABLE_LANGSMITH_INHERITABLE_METADATA_KEYS)

Allowlist of LangSmith-only tracing metadata keys that bypass the default
"first wins" merge semantics used when propagating tracer metadata to nested
runs.

Keys in this set are ALWAYS overridden by the nearest enclosing tracer config,
so nested callers (e.g. a subagent) can replace a value inherited from an
ancestor.

Keep this list very small: every key here loses the default "first wins"
protection and is always clobbered by the nearest enclosing tracer config.
Only keys that are strictly for LangSmith tracing bookkeeping should be added.

## Signature

```python
OVERRIDABLE_LANGSMITH_INHERITABLE_METADATA_KEYS: frozenset[str] = frozenset({'ls_agent_type'})
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/langchain.py#L39)
