---
title: "MISSING_CHECKPOINTER"
description: "You are attempting to use built-in LangGraph persistence without providing a checkpointer."
source: "https://docs.langchain.com/oss/python/langgraph/errors/MISSING_CHECKPOINTER"
category: "docs"
tags: [docs, langgraph, errors, missing_checkpointer]
---

# MISSING_CHECKPOINTER

You are attempting to use built-in LangGraph persistence without providing a checkpointer.

This happens when a `checkpointer` is missing in the `compile()` method of [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) or [`@entrypoint`](https://reference.langchain.com/python/langgraph/func/entrypoint).

## Troubleshooting

The following may help resolve this error:

* Initialize and pass a checkpointer to the `compile()` method of [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) or [`@entrypoint`](https://reference.langchain.com/python/langgraph/func/entrypoint).

```python
from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()

# Graph API
from langgraph.graph import StateGraph
graph = StateGraph(...).compile(checkpointer=checkpointer)

# Functional API
from langgraph.func import entrypoint
@entrypoint(checkpointer=checkpointer)
def workflow(messages: list[str]) -> str:
    ...
```

* Use the LangGraph API so you don't need to implement or configure checkpointers manually. The API handles all persistence infrastructure for you.

## Related

* Read more about [persistence](../persistence.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/errors/MISSING_CHECKPOINTER.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
