---
title: "dereference_refs"
description: "Resolve and inline JSON Schema $ref references in a schema object."
source: "https://reference.langchain.com/python/langchain-core/utils/function_calling/dereference_refs"
category: "reference"
tags: [reference, langchain-core, utils, function_calling, dereference_refs]
---

# dereference_refs

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/json_schema/dereference_refs)

Resolve and inline JSON Schema `$ref` references in a schema object.

This function processes a JSON Schema and resolves all `$ref` references by
replacing them with the actual referenced content.

Handles both simple references and complex cases like circular references and mixed
`$ref` objects that contain additional properties alongside the `$ref`.

## Signature

```python
dereference_refs(
    schema_obj: dict[str, Any],
    *,
    full_schema: dict[str, Any] | None = None,
    skip_keys: Sequence[str] | None = None,
) -> dict[str, Any]
```

## Description

!!! note

- Circular references are handled gracefully by breaking cycles
- Mixed `$ref` objects (with both `$ref` and other properties) are supported
- Additional properties in mixed `$refs` override resolved properties
- The `$defs` section is preserved in the output by default

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema_obj` | `dict[str, Any]` | Yes | The JSON Schema object or fragment to process.  This can be a complete schema or just a portion of one. |
| `full_schema` | `dict[str, Any] \| None` | No | The complete schema containing all definitions that `$refs` might point to.  If not provided, defaults to `schema_obj` (useful when the schema is self-contained). (default: `None`) |
| `skip_keys` | `Sequence[str] \| None` | No | Controls recursion behavior and reference resolution depth.  - If `None` (Default): Only recurse under `'$defs'` and use shallow     reference resolution (break cycles but don't deep-inline nested refs) - If provided (even as `[]`): Recurse under all keys and use deep reference     resolution (fully inline all nested references) (default: `None`) |

## Returns

`dict[str, Any]`

A new dictionary with all $ref references resolved and inlined.

The original `schema_obj` is not modified.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/json_schema.py#L188)
