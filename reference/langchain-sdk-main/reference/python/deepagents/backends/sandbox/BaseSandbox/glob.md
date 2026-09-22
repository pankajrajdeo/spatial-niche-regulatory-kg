---
title: "glob"
description: "Structured glob matching returning GlobResult."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/glob"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/glob)

Structured glob matching returning `GlobResult`.

Returned paths are absolute (see `_absolutize_glob_path`), which
`_check_fs_permission` relies on to apply `deny` rules.

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1932)
