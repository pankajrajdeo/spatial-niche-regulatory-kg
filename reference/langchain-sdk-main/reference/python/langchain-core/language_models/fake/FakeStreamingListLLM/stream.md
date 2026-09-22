---
title: "stream"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/language_models/fake/FakeStreamingListLLM/stream"
category: "reference"
tags: [reference, langchain-core, language_models, fake, fakestreaminglistllm, stream]
---

# stream

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/fake/FakeStreamingListLLM/stream)

## Signature

```python
stream(
    self,
    input: LanguageModelInput,
    config: RunnableConfig | None = None,
    *,
    stop: list[str] | None = None,
    **kwargs: Any = {},
) -> Iterator[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/fake.py#L97)
