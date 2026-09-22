---
title: "VoyageEmbeddings integration"
description: "Integrate with the VoyageEmbeddings embedding model using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/embeddings/voyageai"
category: "docs"
tags: [docs, javascript, integrations, embeddings, voyageai]
---

# VoyageEmbeddings integration

> Integrate with the VoyageEmbeddings embedding model using LangChain JavaScript.

This will help you get started with VoyageEmbeddings [embedding models](../embeddings.md) using LangChain. For detailed documentation on `VoyageEmbeddings` features and configuration options, please refer to the [API reference](https://reference.langchain.com/javascript/langchain-mongodb/VoyageEmbeddings).

## Overview

### Integration details

| Class                                                                                               | Package                                                                  | Local | [Py support](https://python.langchain.com/docs/integrations/embeddings/voyageai/) |                                              Downloads                                             |                                             Version                                             |
| :-------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- | :---: | :-------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: |
| [`VoyageEmbeddings`](https://reference.langchain.com/javascript/langchain-mongodb/VoyageEmbeddings) | [`@langchain/mongodb`](https://www.npmjs.com/package/@langchain/mongodb) |   ❌   |                                         ✅                                         | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/mongodb?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/mongodb?style=flat-square\&label=%20&) |

## Setup

To access Voyage AI embedding models you'll need to create a Voyage AI account, get an API key, and install the `@langchain/mongodb` integration package.

### Credentials

Head to [voyageai.com](https://www.voyageai.com) to sign up and generate an API key. Once you've done this set the `VOYAGE_API_KEY` environment variable:

```bash
export VOYAGE_API_KEY="your-api-key"
```

If you want to get automated tracing of your model calls you can also set your [LangSmith](../../../langsmith/home.md) API key by uncommenting below:

```bash
# export LANGSMITH_TRACING="true"
# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain VoyageEmbeddings integration lives in the `@langchain/mongodb` package:

**npm**

```bash
npm install @langchain/mongodb @langchain/core
```

**yarn**

```bash
yarn add @langchain/mongodb @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/mongodb @langchain/core
```

## Instantiation

Now we can instantiate our model object and embed text:

```typescript
import { VoyageEmbeddings } from "@langchain/mongodb";

const embeddings = new VoyageEmbeddings({
  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.VOYAGE_API_KEY
  model: "voyage-4",
});
```

## Indexing and retrieval

Embedding models are often used in retrieval-augmented generation (RAG) flows, both as part of indexing data as well as later retrieving it. For more detailed instructions, please see our RAG tutorials under the [**Learn** tab](../../learn.md).

Below, see how to index and retrieve data using the `embeddings` object we initialized above. In this example, we will index and retrieve a sample document using the demo [`MemoryVectorStore`](../vectorstores/memory.md).

```typescript
// Create a vector store with a sample text
import { MemoryVectorStore } from "@langchain/classic/vectorstores/memory";

const text = "LangChain is the framework for building context-aware reasoning applications";

const vectorstore = await MemoryVectorStore.fromDocuments(
  [{ pageContent: text, metadata: {} }],
  embeddings,
);

// Use the vector store as a retriever that returns a single document
const retriever = vectorstore.asRetriever(1);

// Retrieve the most similar text
const retrievedDocuments = await retriever.invoke("What is LangChain?");

retrievedDocuments[0].pageContent;
```

```text
LangChain is the framework for building context-aware reasoning applications
```

## Direct usage

Under the hood, the vectorstore and retriever implementations are calling `embeddings.embedDocument(...)` and `embeddings.embedQuery(...)` to create embeddings for the text(s) used in `fromDocuments` and the retriever's `invoke` operations, respectively.

You can directly call these methods to get embeddings for your own use cases.

### Embed single texts

You can embed queries for search with `embedQuery`. This generates a vector representation specific to the query:

```typescript
const singleVector = await embeddings.embedQuery(text);

console.log(singleVector.slice(0, 3));
```

### Embed multiple texts

You can embed multiple texts for indexing with `embedDocuments`. The internals used for this method may (but do not have to) differ from embedding queries:

```typescript
const text2 = "LangGraph is a library for building stateful, multi-actor applications with LLMs";

const vectors = await embeddings.embedDocuments([text, text2]);

console.log(vectors[0].slice(0, 3));
console.log(vectors[1].slice(0, 3));
```

***

## API reference

For detailed documentation of all `VoyageEmbeddings` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-mongodb/VoyageEmbeddings).

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/voyageai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
