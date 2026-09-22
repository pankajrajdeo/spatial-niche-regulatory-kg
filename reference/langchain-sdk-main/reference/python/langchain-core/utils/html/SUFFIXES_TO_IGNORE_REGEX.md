---
title: "SUFFIXES_TO_IGNORE_REGEX"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/utils/html/SUFFIXES_TO_IGNORE_REGEX"
category: "reference"
tags: [reference, langchain-core, utils, html, suffixes_to_ignore_regex]
---

# SUFFIXES_TO_IGNORE_REGEX

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/html/SUFFIXES_TO_IGNORE_REGEX)

## Signature

```python
SUFFIXES_TO_IGNORE_REGEX = '(?!' + '|'.join([re.escape(s) + '[\\#\'\\"]' for s in SUFFIXES_TO_IGNORE]) + ')'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/html.py#L33)
