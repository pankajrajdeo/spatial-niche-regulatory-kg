---
title: "Store integrations"
description: "Integrate with store backends for LangGraph long-term memory."
source: "https://docs.langchain.com/oss/python/integrations/long-term-memory/index"
category: "docs"
tags: [docs, integrations, long-term-memory]
---

# Store integrations

> Integrate with store backends for LangGraph long-term memory.

Stores enable [long-term memory](../../langgraph/stores.md) in LangGraph, allowing agents to persist and retrieve information across threads.

To implement your own store for a custom storage backend, see [Build a custom store](../../langgraph/stores.md#build-a-custom-store).

| Backend                                                                                     | Package                                                                                    | Source                                                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| [In-memory](https://reference.langchain.com/python/langgraph.store/memory/InMemoryStore)    | [`langgraph-checkpoint`](https://pypi.org/project/langgraph-checkpoint/)                   | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint)                              |
| [PostgreSQL](https://reference.langchain.com/python/langgraph.store.postgres/PostgresStore) | [`langgraph-checkpoint-postgres`](https://pypi.org/project/langgraph-checkpoint-postgres/) | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-postgres)                     |
| Redis                                                                                       | [`langgraph-checkpoint-redis`](https://pypi.org/project/langgraph-checkpoint-redis/)       | [redis-developer/langgraph-redis](https://github.com/redis-developer/langgraph-redis)                                      |
| [MongoDB](../memory/mongodb-long-term-memory.md)                         | [`langgraph-store-mongodb`](https://pypi.org/project/langgraph-store-mongodb/)             | [langchain-ai/langchain-mongodb](https://github.com/langchain-ai/langchain-mongodb/tree/main/libs/langgraph-store-mongodb) |
| Upstash Redis                                                                               | [`langgraph-store-upstash`](https://pypi.org/project/langgraph-store-upstash/)             | [Tghez/langgraph-store-upstash](https://github.com/Tghez/langgraph-store-upstash)                                          |
| OMEM                                                                                        | [`omem-infrastructure`](https://pypi.org/project/omem-infrastructure/)                     | [OMEM docs](https://infrastructure.omem-cloud.com/docs)                                                                    |

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/long-term-memory/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
