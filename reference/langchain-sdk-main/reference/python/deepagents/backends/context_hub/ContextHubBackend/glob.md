---
title: "glob"
description: "Return files matching pattern (path unused — flat namespace)."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/glob"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/glob)

Return files matching `pattern` (`path` unused — flat namespace).

Matching uses the shared backend contract (`compile_grep_include_glob`),
so a bare pattern matches the basename at any depth, a pattern with `/`
matches the namespace-relative path, and a leading `/` anchors. Plain
`fnmatch` would diverge on all three: its `*` crosses `/`, so `/*.py`
would widen to every depth instead of anchoring to the top level.

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/context_hub.py#L640)
