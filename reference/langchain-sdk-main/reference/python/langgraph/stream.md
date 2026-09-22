---
title: "stream"
description: "Streaming infrastructure for LangGraph."
source: "https://reference.langchain.com/python/langgraph/stream"
category: "reference"
tags: [reference, langgraph, stream]
---

# stream

> **Module** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream)

Streaming infrastructure for LangGraph.

Compile a graph with `transformers=[...]` and call `graph.stream_events(version="v3")` /
`graph.astream_events(version="v3")` to drive a transformer pipeline that projects the
graph's raw events into ergonomic per-channel streams.

## Properties

- `SubgraphStatus`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/__init__.py)
