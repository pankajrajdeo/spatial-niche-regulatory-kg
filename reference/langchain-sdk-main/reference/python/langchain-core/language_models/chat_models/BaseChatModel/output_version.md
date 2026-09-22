---
title: "output_version"
description: "Version of AIMessage output format to store in message content."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/output_version"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, output_version]
---

# output_version

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/output_version)

Version of `AIMessage` output format to store in message content.

`AIMessage.content_blocks` will lazily parse the contents of `content` into a
standard format. This flag can be used to additionally store the standard format
in message content, e.g., for serialization purposes.

Supported values:

- `'v0'`: provider-specific format in content (can lazily-parse with
    `content_blocks`)
- `'v1'`: standardized format in content (consistent with `content_blocks`)

Partner packages (e.g.,
[`langchain-openai`](https://pypi.org/project/langchain-openai)) can also use this
field to roll out new content formats in a backward-compatible way.

!!! version-added "Added in `langchain-core` 1.0.0"

## Signature

```python
output_version: str | None = Field(default_factory=from_env('LC_OUTPUT_VERSION', default=None))
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L355)
