---
title: "LangChain JavaScript integrations"
description: "Integrate with providers using LangChain JavaScript/TypeScript."
source: "https://docs.langchain.com/oss/javascript/integrations/providers/overview"
category: "docs"
tags: [docs, javascript, integrations, providers]
---

# LangChain JavaScript integrations

> Integrate with providers using LangChain JavaScript/TypeScript.

LangChain integrates with a wide variety of chat & embedding models, tools & toolkits, document loaders, vector stores, and more.

A **provider** is a third-party service or platform that LangChain integrates with to access AI capabilities like chat models, embeddings, and vector stores. These providers have standalone `langchain-provider` packages for improved versioning, dependency management, and testing.

## Popular providers

| Provider                                                                         | Package                                                                                  | Downloads                                                              | Latest                                                          |
| :------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :-------------------------------------------------------------- |
| [Anthropic](anthropic.md)                    | [`@langchain/anthropic`](https://www.npmjs.com/package/@langchain/anthropic)             | ![Downloads](https://img.shields.io/npm/dm/@langchain/anthropic)       | ![NPM](https://img.shields.io/npm/v/@langchain/anthropic)       |
| [Azure CosmosDB](../vectorstores/azure_cosmosdb_nosql.md) | [`@langchain/azure-cosmosdb`](https://www.npmjs.com/package/@langchain/azure-cosmosdb)   | ![Downloads](https://img.shields.io/npm/dm/@langchain/azure-cosmosdb)  | ![NPM](https://img.shields.io/npm/v/@langchain/azure-cosmosdb)  |
| [Cerebras](../chat/cerebras.md)                           | [`@langchain/cerebras`](https://www.npmjs.com/package/@langchain/cerebras)               | ![Downloads](https://img.shields.io/npm/dm/@langchain/cerebras)        | ![NPM](https://img.shields.io/npm/v/@langchain/cerebras)        |
| Cloudflare                                                                       | [`@langchain/cloudflare`](https://www.npmjs.com/package/@langchain/cloudflare)           | ![Downloads](https://img.shields.io/npm/dm/@langchain/cloudflare)      | ![NPM](https://img.shields.io/npm/v/@langchain/cloudflare)      |
| [Cohere](../chat/cohere.md)                               | [`@langchain/cohere`](https://www.npmjs.com/package/@langchain/cohere)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/cohere)          | ![NPM](https://img.shields.io/npm/v/@langchain/cohere)          |
| [Exa](../retrievers/exa.md)                               | [`@langchain/exa`](https://www.npmjs.com/package/@langchain/exa)                         | ![Downloads](https://img.shields.io/npm/dm/@langchain/exa)             | ![NPM](https://img.shields.io/npm/v/@langchain/exa)             |
| [Google](google.md)                          | [`@langchain/google`](https://www.npmjs.com/package/@langchain/google)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/google)          | ![NPM](https://img.shields.io/npm/v/@langchain/google)          |
| [Groq](../chat/groq.md)                                   | [`@langchain/groq`](https://www.npmjs.com/package/@langchain/groq)                       | ![Downloads](https://img.shields.io/npm/dm/@langchain/groq)            | ![NPM](https://img.shields.io/npm/v/@langchain/groq)            |
| [MistralAI](../chat/mistral.md)                           | [`@langchain/mistralai`](https://www.npmjs.com/package/@langchain/mistralai)             | ![Downloads](https://img.shields.io/npm/dm/@langchain/mistralai)       | ![NPM](https://img.shields.io/npm/v/@langchain/mistralai)       |
| [MongoDB](../vectorstores/mongodb_atlas.md)               | [`@langchain/mongodb`](https://www.npmjs.com/package/@langchain/mongodb)                 | ![Downloads](https://img.shields.io/npm/dm/@langchain/mongodb)         | ![NPM](https://img.shields.io/npm/v/@langchain/mongodb)         |
| [Neo4j](../vectorstores/neo4jvector.md)                   | [`@langchain/neo4j`](https://www.npmjs.com/package/@langchain/neo4j)                     | ![Downloads](https://img.shields.io/npm/dm/@langchain/neo4j)           | ![NPM](https://img.shields.io/npm/v/@langchain/neo4j)           |
| [Nomic](../embeddings/nomic.md)                           | [`@langchain/nomic`](https://www.npmjs.com/package/@langchain/nomic)                     | ![Downloads](https://img.shields.io/npm/dm/@langchain/nomic)           | ![NPM](https://img.shields.io/npm/v/@langchain/nomic)           |
| [Ollama](../chat/ollama.md)                               | [`@langchain/ollama`](https://www.npmjs.com/package/@langchain/ollama)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/ollama)          | ![NPM](https://img.shields.io/npm/v/@langchain/ollama)          |
| [OpenAI](openai.md)                          | [`@langchain/openai`](https://www.npmjs.com/package/@langchain/openai)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/openai)          | ![NPM](https://img.shields.io/npm/v/@langchain/openai)          |
| [OpenRouter](../chat/openrouter.md)                       | [`@langchain/openrouter`](https://www.npmjs.com/package/@langchain/openrouter)           | ![Downloads](https://img.shields.io/npm/dm/@langchain/openrouter)      | ![NPM](https://img.shields.io/npm/v/@langchain/openrouter)      |
| [Oracle AI Vector Search](../vectorstores/oracleai.md)    | [`@oracle/langchain-oracledb`](https://www.npmjs.com/package/@oracle/langchain-oracledb) | ![Downloads](https://img.shields.io/npm/dm/@oracle/langchain-oracledb) | ![NPM](https://img.shields.io/npm/v/@oracle/langchain-oracledb) |
| [Perplexity](perplexity.md)                  | [`@langchain/perplexity`](https://www.npmjs.com/package/@langchain/perplexity)           | ![Downloads](https://img.shields.io/npm/dm/@langchain/perplexity)      | ![NPM](https://img.shields.io/npm/v/@langchain/perplexity)      |
| [PGVector](../vectorstores/pgvector.md)                   | [`@langchain/pgvector`](https://www.npmjs.com/package/@langchain/pgvector)               | ![Downloads](https://img.shields.io/npm/dm/@langchain/pgvector)        | ![NPM](https://img.shields.io/npm/v/@langchain/pgvector)        |
| [Pinecone](../vectorstores/pinecone.md)                   | [`@langchain/pinecone`](https://www.npmjs.com/package/@langchain/pinecone)               | ![Downloads](https://img.shields.io/npm/dm/@langchain/pinecone)        | ![NPM](https://img.shields.io/npm/v/@langchain/pinecone)        |
| [Qdrant](../vectorstores/qdrant.md)                       | [`@langchain/qdrant`](https://www.npmjs.com/package/@langchain/qdrant)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/qdrant)          | ![NPM](https://img.shields.io/npm/v/@langchain/qdrant)          |
| [Redis](../vectorstores/redis.md)                         | [`@langchain/redis`](https://www.npmjs.com/package/@langchain/redis)                     | ![Downloads](https://img.shields.io/npm/dm/@langchain/redis)           | ![NPM](https://img.shields.io/npm/v/@langchain/redis)           |
| [SAP HANA Cloud](sap.md)                     | [`@sap/hana-langchain`](https://www.npmjs.com/package/@sap/hana-langchain)               | ![Downloads](https://img.shields.io/npm/dm/@sap/hana-langchain)        | ![NPM](https://img.shields.io/npm/v/@sap/hana-langchain)        |
| [SCX](https://scx.ai/)                                                           | [`@scx-ai/langchain`](https://www.npmjs.com/package/@scx-ai/langchain)                   | ![Downloads](https://img.shields.io/npm/dm/@scx-ai/langchain)          | ![NPM](https://img.shields.io/npm/v/@scx-ai/langchain)          |
| [Tavily](tavily.md)                          | [`@langchain/tavily`](https://www.npmjs.com/package/@langchain/tavily)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/tavily)          | ![NPM](https://img.shields.io/npm/v/@langchain/tavily)          |
| [Together AI](../chat/togetherai.md)                      | [`@langchain/together-ai`](https://www.npmjs.com/package/@langchain/together-ai)         | ![Downloads](https://img.shields.io/npm/dm/@langchain/together-ai)     | ![NPM](https://img.shields.io/npm/v/@langchain/together-ai)     |
| [turbopuffer](../vectorstores/turbopuffer.md)             | [`@langchain/turbopuffer`](https://www.npmjs.com/package/@langchain/turbopuffer)         | ![Downloads](https://img.shields.io/npm/dm/@langchain/turbopuffer)     | ![NPM](https://img.shields.io/npm/v/@langchain/turbopuffer)     |
| [Weaviate](../vectorstores/weaviate.md)                   | [`@langchain/weaviate`](https://www.npmjs.com/package/@langchain/weaviate)               | ![Downloads](https://img.shields.io/npm/dm/@langchain/weaviate)        | ![NPM](https://img.shields.io/npm/v/@langchain/weaviate)        |
| [xAI](../chat/xai.md)                                     | [`@langchain/xai`](https://www.npmjs.com/package/@langchain/xai)                         | ![Downloads](https://img.shields.io/npm/dm/@langchain/xai)             | ![NPM](https://img.shields.io/npm/v/@langchain/xai)             |

## All providers

See [all providers](all_providers.md) or search for a provider using the search field.

> [!NOTE]
> If you'd like to contribute an integration, see [Contributing integrations](../../contributing.md#add-a-new-integration).

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
