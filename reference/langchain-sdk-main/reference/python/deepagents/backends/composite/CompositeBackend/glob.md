---
title: "glob"
description: "Find files matching a glob pattern, routing by path prefix."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/glob"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/glob)

Find files matching a glob pattern, routing by path prefix.

Routes to backends based on path: a routed path searches that route,
`"/"` or `None` searches every backend, and a non-route path searches
only the default backend.

When merging across routes, a pattern that targets a route is rewritten
relative to that route's internal root (see `_strip_route_from_pattern`);
a bare pattern is forwarded unchanged and matches recursively within
every route; and a root-anchored pattern that targets no route skips the
routed backends entirely, since their results are always deeper than the
anchor permits (see `_route_glob_pattern`).

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/composite.py#L613)
