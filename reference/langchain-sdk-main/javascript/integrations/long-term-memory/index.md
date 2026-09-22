---
title: "Store integrations"
description: "Integrate with store backends for LangGraph long-term memory."
source: "https://docs.langchain.com/oss/javascript/integrations/long-term-memory/index"
category: "docs"
tags: [docs, javascript, integrations, long-term-memory]
---

# Store integrations

> Integrate with store backends for LangGraph long-term memory.

Stores enable [long-term memory](../../langgraph/stores.md) in LangGraph, allowing agents to persist and retrieve information across threads.

To implement your own store for a custom storage backend, extend the [BaseStore](https://reference.langchain.com/javascript/langchain-langgraph-checkpoint/BaseStore) interface. To deploy a custom store on Agent Server, see [Add a custom store](../../../langsmith/custom-store.md).

| Backend                                                                                                              | Package                                                                                                              | Source                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [In-memory](https://reference.langchain.com/javascript/langchain-langgraph-checkpoint/InMemoryStore)                 | [`@langchain/langgraph-checkpoint`](https://www.npmjs.com/package/@langchain/langgraph-checkpoint)                   | [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs/tree/main/libs/checkpoint)          |
| [PostgreSQL](https://reference.langchain.com/javascript/langchain-langgraph-checkpoint-postgres/store/PostgresStore) | [`@langchain/langgraph-checkpoint-postgres`](https://www.npmjs.com/package/@langchain/langgraph-checkpoint-postgres) | [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs/tree/main/libs/checkpoint-postgres) |
| [Redis](https://reference.langchain.com/javascript/langchain-langgraph-checkpoint-redis/store/RedisStore)            | [`@langchain/langgraph-checkpoint-redis`](https://www.npmjs.com/package/@langchain/langgraph-checkpoint-redis)       | [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs/tree/main/libs/checkpoint-redis)    |
| [MongoDB](../memory/mongodb-long-term-memory.md)                                              | [`@langchain/langgraph-checkpoint-mongodb`](https://www.npmjs.com/package/@langchain/langgraph-checkpoint-mongodb)   | [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs/tree/main/libs/checkpoint-mongodb)  |

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/long-term-memory/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
