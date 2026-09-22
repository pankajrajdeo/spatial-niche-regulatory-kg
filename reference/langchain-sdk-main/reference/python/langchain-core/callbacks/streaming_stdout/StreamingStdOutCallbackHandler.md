---
title: "StreamingStdOutCallbackHandler"
description: "Callback handler for streaming."
source: "https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler"
category: "reference"
tags: [reference, langchain-core, callbacks, streaming_stdout, streamingstdoutcallbackhandler]
---

# StreamingStdOutCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler)

Callback handler for streaming.

!!! warning "Only works with LLMs that support streaming."

## Signature

```python
StreamingStdOutCallbackHandler()
```

## Extends

- `BaseCallbackHandler`

## Methods

- [`on_llm_start()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_llm_start)
- [`on_chat_model_start()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_chat_model_start)
- [`on_llm_new_token()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_llm_new_token)
- [`on_llm_end()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_llm_end)
- [`on_llm_error()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_llm_error)
- [`on_chain_start()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_chain_start)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_chain_end)
- [`on_chain_error()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_chain_error)
- [`on_tool_start()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_tool_start)
- [`on_agent_action()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_agent_action)
- [`on_tool_end()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_tool_end)
- [`on_tool_error()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_tool_error)
- [`on_text()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_text)
- [`on_agent_finish()`](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_agent_finish)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/streaming_stdout.py#L18)
