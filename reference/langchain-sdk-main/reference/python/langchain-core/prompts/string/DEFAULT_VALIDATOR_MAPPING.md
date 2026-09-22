---
title: "DEFAULT_VALIDATOR_MAPPING"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/prompts/string/DEFAULT_VALIDATOR_MAPPING"
category: "reference"
tags: [reference, langchain-core, prompts, string, default_validator_mapping]
---

# DEFAULT_VALIDATOR_MAPPING

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/DEFAULT_VALIDATOR_MAPPING)

## Signature

```python
DEFAULT_VALIDATOR_MAPPING: dict[str, Callable[[str, list[str]], None]] = {'f-string': formatter.validate_input_variables, 'jinja2': validate_jinja2}
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/string.py#L216)
