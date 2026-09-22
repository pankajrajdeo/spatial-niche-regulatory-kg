---
title: "wrap_tool_call"
description: "Annotate read_file results that may have more pages."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ReadFileContinuationNoticeMiddleware/wrap_tool_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, readfilecontinuationnoticemiddleware, wrap_tool_call]
---

# wrap_tool_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ReadFileContinuationNoticeMiddleware/wrap_tool_call)

Annotate `read_file` results that may have more pages.

## Signature

```python
wrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]],
) -> ToolMessage | Command[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L211)
