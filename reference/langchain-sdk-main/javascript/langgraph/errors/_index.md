---
title: "javascript/langgraph/errors"
description: "Index of 6 pages and 0 subdirectories under javascript/langgraph/errors."
category: "index"
tags: [index, javascript, langgraph, errors]
---

# javascript/langgraph/errors

6 pages here.

## Files

- [GRAPH_RECURSION_LIMIT](GRAPH_RECURSION_LIMIT.md) - Your LangGraph StateGraph reached the maximum number of steps before hitting a stop condition. This is often due to an infinite loop caused by code like the example below:
- [INVALID_CHAT_HISTORY](INVALID_CHAT_HISTORY.md) - This error is raised in the prebuilt createAgent when the callModel graph node receives a malformed list of messages. Specifically, it is malformed when there are AIMessages with tool_calls (LLM...
- [INVALID_CONCURRENT_GRAPH_UPDATE](INVALID_CONCURRENT_GRAPH_UPDATE.md) - A LangGraph StateGraph received concurrent updates to its state from multiple nodes to a state property that doesn't support it.
- [INVALID_GRAPH_NODE_RETURN_VALUE](INVALID_GRAPH_NODE_RETURN_VALUE.md) - A LangGraph StateGraph received a non-object return type from a node. Here's an example:
- [MISSING_CHECKPOINTER](MISSING_CHECKPOINTER.md) - You are attempting to use built-in LangGraph persistence without providing a checkpointer.
- [MULTIPLE_SUBGRAPHS](MULTIPLE_SUBGRAPHS.md) - This error occurs when you call a subgraph inside a node multiple times, and the subgraph is compiled with checkpointer=True (continuations mode).
