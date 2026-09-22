---
title: "private_state_field_names"
description: "Return fields annotated with PrivateStateAttr across state schemas."
source: "https://reference.langchain.com/python/deepagents/middleware/_state/private_state_field_names"
category: "reference"
tags: [reference, deepagents, middleware, state, private_state_field_names]
---

# private_state_field_names

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_state/private_state_field_names)

Return fields annotated with `PrivateStateAttr` across state schemas.

Annotations are resolved at runtime, so a schema whose `PrivateStateAttr`
annotation references a `TYPE_CHECKING`-only name cannot be inspected. That
schema is skipped with a warning rather than failing the whole agent, because
the caller may own several unrelated schemas -- but the warning matters: a
skipped schema keeps none of its private fields, so they will be forwarded to
and merged back from subagents.

## Signature

```python
private_state_field_names(
    *state_schemas: type[object] = (),
) -> frozenset[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/_state.py#L13)
