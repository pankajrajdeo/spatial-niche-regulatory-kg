---
title: "Azure Cosmos DB NoSQL semantic integration"
description: "Integrate with the Azure Cosmos DB NoSQL semantic cache using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/llm_caching/azure_cosmosdb_nosql"
category: "docs"
tags: [docs, javascript, integrations, llm_caching, azure_cosmosdb_nosql]
---

# Azure Cosmos DB NoSQL semantic integration

> Integrate with the Azure Cosmos DB NoSQL semantic cache using LangChain JavaScript.

> The Semantic Cache feature is supported with Azure Cosmos DB for NoSQL integration, enabling users to retrieve cached responses based on semantic similarity between the user input and previously cached results. It leverages [AzureCosmosDBNoSQLVectorStore](../vectorstores/azure_cosmosdb_nosql.md), which stores vector embeddings of cached prompts. These embeddings enable similarity-based searches, allowing the system to retrieve relevant cached results.

If you don't have an Azure account, you can [create a free account](https://azure.microsoft.com/free/) to get started.

## Setup

You'll first need to install the [`@langchain/azure-cosmosdb`](https://www.npmjs.com/package/@langchain/azure-cosmosdb) package:

> [!TIP]
> See [this section for general instructions on installing LangChain packages](../../langchain/install.md).

**npm**

```bash
npm install @langchain/azure-cosmosdb @langchain/core
```

You'll also need to have an Azure Cosmos DB for NoSQL instance running. You can deploy a free version on Azure Portal without any cost, following [this guide](https://learn.microsoft.com/azure/cosmos-db/nosql/quickstart-portal).

Once you have your instance running, make sure you have the connection string. If you are using Managed Identity, you need to have the endpoint. You can find them in the Azure Portal, under the "Settings / Keys" section of your instance.

> [!NOTE]
> **When using Azure Managed Identity and role-based access control, you must ensure that the database and container have been created beforehand. RBAC does not provide permissions to create databases and containers. You can get more information about the permission model in the [Azure Cosmos DB documentation](https://learn.microsoft.com/azure/cosmos-db/how-to-setup-rbac#permission-model).**

## Usage example

```typescript
import {
  AzureCosmosDBNoSQLConfig,
  AzureCosmosDBNoSQLSemanticCache,
} from "@langchain/azure-cosmosdb";
import { ChatOpenAI, OpenAIEmbeddings } from "@langchain/openai";

const embeddings = new OpenAIEmbeddings();
const config: AzureCosmosDBNoSQLConfig = {
  databaseName: "<DATABASE_NAME>",
  containerName: "<CONTAINER_NAME>",
  // use endpoint to initiate client with managed identity
  connectionString: "<CONNECTION_STRING>",
};

/**
 * Sets the threshold similarity score for returning cached results based on vector distance.
 * Cached output is returned only if the similarity score meets or exceeds this threshold;
 * otherwise, a new result is generated. Default is 0.6, adjustable via the constructor
 * to suit various distance functions and use cases.
 * (see: https://aka.ms/CosmosVectorSearch).
 */

const similarityScoreThreshold = 0.5;
const cache = new AzureCosmosDBNoSQLSemanticCache(
  embeddings,
  config,
  similarityScoreThreshold
);

const model = new ChatOpenAI({ model: "gpt-5.4-mini", cache });

// Invoke the model to perform an action
const response1 = await model.invoke("Do something random!");
console.log(response1);
/*
  AIMessage {
    content: "Sure! I'll generate a random number for you: 37",
    additional_kwargs: {}
  }
*/

const response2 = await model.invoke("Do something random!");
console.log(response2);
/*
  AIMessage {
    content: "Sure! I'll generate a random number for you: 37",
    additional_kwargs: {}
  }
*/
```

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/llm_caching/azure_cosmosdb_nosql.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
