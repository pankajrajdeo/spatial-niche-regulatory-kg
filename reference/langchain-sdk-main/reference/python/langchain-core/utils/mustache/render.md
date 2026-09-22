---
title: "render"
description: "Render a mustache template."
source: "https://reference.langchain.com/python/langchain-core/utils/mustache/render"
category: "reference"
tags: [reference, langchain-core, utils, mustache, render]
---

# render

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/mustache/render)

Render a mustache template.

Renders a mustache template with a data scope and inline partial capability.

## Signature

```python
render(
    template: str | list[tuple[str, str]] = '',
    data: Mapping[str, Any] = EMPTY_DICT,
    partials_dict: Mapping[str, str] = EMPTY_DICT,
    padding: str = '',
    def_ldel: str = '{{',
    def_rdel: str = '}}',
    scopes: Scopes | None = None,
    warn: bool = False,
    keep: bool = False,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str \| list[tuple[str, str]]` | No | A file-like object or a string containing the template. (default: `''`) |
| `data` | `Mapping[str, Any]` | No | A python dictionary with your data scope. (default: `EMPTY_DICT`) |
| `partials_dict` | `Mapping[str, str]` | No | A python dictionary which will be search for partials before the filesystem is.  `{'include': 'foo'}` is the same as a file called include.mustache (defaults to `{}`). (default: `EMPTY_DICT`) |
| `padding` | `str` | No | This is for padding partials, and shouldn't be used (but can be if you really want to). (default: `''`) |
| `def_ldel` | `str` | No | The default left delimiter  (`'{{'` by default, as in spec compliant mustache). (default: `'{{'`) |
| `def_rdel` | `str` | No | The default right delimiter  (`'}}'` by default, as in spec compliant mustache). (default: `'}}'`) |
| `scopes` | `Scopes \| None` | No | The list of scopes that `get_key` will look through. (default: `None`) |
| `warn` | `bool` | No | Log a warning when a template substitution isn't found in the data (default: `False`) |
| `keep` | `bool` | No | Keep unreplaced tags when a substitution isn't found in the data. (default: `False`) |

## Returns

`str`

A string containing the rendered template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/mustache.py#L468)
