---
title: "Embedding model integrations"
description: "Integrate with embedding models using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/embeddings"
category: "docs"
tags: [docs, javascript, integrations, embeddings]
---

# Embedding model integrations

> Integrate with embedding models using LangChain JavaScript.

## Overview

> [!NOTE]
> This overview covers **text-based embedding models**. LangChain does not currently support multimodal embeddings.

Embedding models transform raw text—such as a sentence, paragraph, or tweet—into a fixed-length vector of numbers that captures its **semantic meaning**. These vectors allow machines to compare and search text based on meaning rather than exact words.

In practice, this means that texts with similar ideas are placed close together in the vector space. For example, instead of matching only the phrase *"machine learning"*, embeddings can surface documents that discuss related concepts even when different wording is used.

### How it works

1. **Vectorization**: The model encodes each input string as a high-dimensional vector.
2. **Similarity scoring**: Vectors are compared using mathematical metrics to measure how closely related the underlying texts are.

### Similarity metrics

Several metrics are commonly used to compare embeddings:

* **Cosine similarity**: measures the angle between two vectors.
* **Euclidean distance**: measures the straight-line distance between points.
* **Dot product**: measures how much one vector projects onto another.

## Interface

LangChain provides a standard interface for text embedding models (e.g., OpenAI, Cohere, Hugging Face) via the [Embeddings](https://reference.langchain.com/javascript/langchain-core/embeddings/Embeddings) interface.

Two main methods are available:

* `embedDocuments(documents: string[]) → number[][]`: Embeds a list of documents.
* `embedQuery(text: string) → number[]`: Embeds a single query.

> [!NOTE]
> The interface allows queries and documents to be embedded with different strategies, though most providers handle them the same way in practice.

## Install and use

<details>
<summary>OpenAI</summary>

Install dependencies:

**npm**

```bash
npm install @langchain/openai @langchain/core
```

**yarn**

```bash
yarn add @langchain/openai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/openai @langchain/core
```

Add environment variables:

```bash
OPENAI_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { OpenAIEmbeddings } from "@langchain/openai";

const embeddings = new OpenAIEmbeddings({
  model: "text-embedding-3-large"
});
```

</details>

<details>
<summary>Azure</summary>

Install dependencies

**npm**

```bash
npm install @langchain/openai @langchain/core
```

**yarn**

```bash
yarn add @langchain/openai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/openai @langchain/core
```

Add environment variables:

```bash
AZURE_OPENAI_API_INSTANCE_NAME=<YOUR_INSTANCE_NAME>
AZURE_OPENAI_API_KEY=<YOUR_KEY>
AZURE_OPENAI_API_VERSION="2024-02-01"
```

Instantiate the model:

```typescript
import { AzureOpenAIEmbeddings } from "@langchain/openai";

const embeddings = new AzureOpenAIEmbeddings({
  azureOpenAIApiEmbeddingsDeploymentName: "text-embedding-ada-002"
});
```

</details>

<details>
<summary>AWS</summary>

Install dependencies:

**npm**

```bash
npm install @langchain/aws @langchain/core
```

**yarn**

```bash
yarn add @langchain/aws @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/aws @langchain/core
```

Add environment variables:

```bash
BEDROCK_AWS_REGION=your-region
```

Instantiate the model:

```typescript
import { BedrockEmbeddings } from "@langchain/aws";

const embeddings = new BedrockEmbeddings({
  model: "amazon.titan-embed-text-v1"
});
```

</details>

<details>
<summary>Google Gemini</summary>

Install dependencies:

**npm**

```bash
npm install @langchain/google-genai @langchain/core
```

**yarn**

```bash
yarn add @langchain/google-genai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/google-genai @langchain/core
```

Add environment variables:

```bash
GOOGLE_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";

const embeddings = new GoogleGenerativeAIEmbeddings({
  model: "text-embedding-004"
});
```

</details>

<details>
<summary>Gemini Enterprise Agent Platform</summary>

Install dependencies:

**npm**

```bash
npm install @langchain/google-vertexai @langchain/core
```

**yarn**

```bash
yarn add @langchain/google-vertexai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/google-vertexai @langchain/core
```

Add environment variables:

```bash
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

Instantiate the model:

```typescript
import { VertexAIEmbeddings } from "@langchain/google-vertexai";

const embeddings = new VertexAIEmbeddings({
  model: "gemini-embedding-001"
});
```

</details>

<details>
<summary>MistralAI</summary>

Install dependencies:

**npm**

```bash
npm install @langchain/mistralai @langchain/core
```

**yarn**

```bash
yarn add @langchain/mistralai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/mistralai @langchain/core
```

Add environment variables:

```bash
MISTRAL_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { MistralAIEmbeddings } from "@langchain/mistralai";

const embeddings = new MistralAIEmbeddings({
  model: "mistral-embed"
});
```

</details>

<details>
<summary>Cohere</summary>

Install dependencies:

**npm**

```bash
npm install @langchain/cohere @langchain/core
```

**yarn**

```bash
yarn add @langchain/cohere @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/cohere @langchain/core
```

Add environment variables:

```bash
COHERE_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { CohereEmbeddings } from "@langchain/cohere";

const embeddings = new CohereEmbeddings({
  model: "embed-english-v3.0"
});
```

</details>

<details>
<summary>Ollama</summary>

Install dependencies:

**npm**

```bash
npm install @langchain/ollama @langchain/core
```

**yarn**

```bash
yarn add @langchain/ollama @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/ollama @langchain/core
```

Instantiate the model:

```typescript
import { OllamaEmbeddings } from "@langchain/ollama";

const embeddings = new OllamaEmbeddings({
  model: "llama2",
  baseUrl: "http://localhost:11434", // Default value
});
```

</details>

<details>
<summary>Voyage AI</summary>

Install dependencies:

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

Add environment variables:

```bash
VOYAGE_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { VoyageEmbeddings } from "@langchain/mongodb";

const embeddings = new VoyageEmbeddings({
  model: "voyage-4"
});
```

</details>

## Caching

Embeddings can be stored or temporarily cached to avoid needing to recompute them.

Caching embeddings can be done using a `CacheBackedEmbeddings`. This wrapper stores embeddings in a key-value store, where the text is hashed and the hash is used as the key in the cache.

The main supported way to initialize a `CacheBackedEmbeddings` is `fromBytesStore`. It takes the following parameters:

* **underlyingEmbeddings**: The embedder to use for embedding.
* **documentEmbeddingStore**: Any [`BaseStore`](stores.md) for caching document embeddings.
* **options.namespace**: (optional, defaults to `""`) The namespace to use for the document cache. Helps avoid collisions (e.g., set it to the embedding model name).

> [!IMPORTANT]
> - Always set the `namespace` parameter to avoid collisions when using different embedding models.
> - `CacheBackedEmbeddings` does not cache query embeddings by default. To enable this, specify a `query_embedding_store`.

```typescript
import { CacheBackedEmbeddings } from "@langchain/classic/embeddings/cache_backed";
import { InMemoryStore } from "@langchain/core/stores";

const underlyingEmbeddings = new OpenAIEmbeddings();

const inMemoryStore = new InMemoryStore();

const cacheBackedEmbeddings = CacheBackedEmbeddings.fromBytesStore(
  underlyingEmbeddings,
  inMemoryStore,
  {
    namespace: underlyingEmbeddings.model,
  }
);

// Example: caching a query embedding
const tic = Date.now();
const queryEmbedding = cacheBackedEmbeddings.embedQuery("Hello, world!");
console.log(`First call took: ${Date.now() - tic}ms`);

// Example: caching a document embedding
const tic = Date.now();
const documentEmbedding = cacheBackedEmbeddings.embedDocuments(["Hello, world!"]);
console.log(`Cached creation time: ${Date.now() - tic}ms`);
```

In production, you would typically use a more robust persistent store, such as a database or cloud storage. Please see [stores integrations](stores.md) for options.

## All integrations

| Integration                                                                                    | Downloads                                                                                                                                                                                                                                                                                      |
| :--------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`AzureOpenAIEmbeddings`](embeddings/azure_openai.md)                | <span data-sort-value="14480022"><a href="https://www.npmjs.com/package/@langchain/openai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/openai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`OpenAIEmbeddings`](embeddings/openai.md)                           | <span data-sort-value="14480022"><a href="https://www.npmjs.com/package/@langchain/openai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/openai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`Bedrock`](embeddings/bedrock.md)                                   | <span data-sort-value="3181274"><a href="https://www.npmjs.com/package/@langchain/aws" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/aws?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                         |
| [`GoogleGenerativeAIEmbeddings`](embeddings/google_generative_ai.md) | <span data-sort-value="3132743"><a href="https://www.npmjs.com/package/@langchain/google-genai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/google-genai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>       |
| [`VertexAIEmbeddings`](embeddings/google_vertex_ai.md)               | <span data-sort-value="1813550"><a href="https://www.npmjs.com/package/@langchain/google-vertexai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/google-vertexai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`OllamaEmbeddings`](embeddings/ollama.md)                           | <span data-sort-value="833544"><a href="https://www.npmjs.com/package/@langchain/ollama" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/ollama?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`MistralAIEmbeddings`](embeddings/mistralai.md)                     | <span data-sort-value="764540"><a href="https://www.npmjs.com/package/@langchain/mistralai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/mistralai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>              |
| [`PineconeEmbeddings`](embeddings/pinecone.md)                       | <span data-sort-value="656824"><a href="https://www.npmjs.com/package/@langchain/pinecone" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/pinecone?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                |
| [`VoyageEmbeddings`](embeddings/voyageai.md)                         | <span data-sort-value="496248"><a href="https://www.npmjs.com/package/@langchain/mongodb" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/mongodb?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`CohereEmbeddings`](embeddings/cohere.md)                           | <span data-sort-value="494553"><a href="https://www.npmjs.com/package/@langchain/cohere" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/cohere?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`Baidu qianfan`](embeddings/baidu_qianfan.md)                       | <span data-sort-value="23195"><a href="https://www.npmjs.com/package/@langchain/baidu-qianfan" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/baidu-qianfan?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>       |
| [`Nomic`](embeddings/nomic.md)                                       | <span data-sort-value="20529"><a href="https://www.npmjs.com/package/@langchain/nomic" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/nomic?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                       |
| [`CloudflareWorkersAIEmbeddings`](embeddings/cloudflare_ai.md)       | <span data-sort-value="17423"><a href="https://www.npmjs.com/package/@langchain/cloudflare" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/cloudflare?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`FireworksEmbeddings`](embeddings/fireworks.md)                     | <span data-sort-value="6462"><a href="https://www.npmjs.com/package/@langchain/fireworks" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/fireworks?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                |
| [`WatsonxEmbeddings`](embeddings/ibm.md)                             | <span data-sort-value="3845"><a href="https://www.npmjs.com/package/@langchain/ibm" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/ibm?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                            |
| [`TogetherAIEmbeddings`](embeddings/togetherai.md)                   | <span data-sort-value="1237"><a href="https://www.npmjs.com/package/@langchain/together-ai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/together-ai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>            |
| [`Mixedbread AI`](embeddings/mixedbread_ai.md)                       | <span data-sort-value="163"><a href="https://www.npmjs.com/package/@langchain/mixedbread-ai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/mixedbread-ai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>         |
| [`SCXEmbeddings`](https://scx.ai/)                                                             | <span data-sort-value="27"><a href="https://www.npmjs.com/package/@scx-ai/langchain" target="_blank">  <img src="https://img.shields.io/npm/dm/@scx-ai/langchain?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                        |
| [`Minimax`](embeddings/minimax.md)                                   | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                          |
| [`OracleEmbeddings`](embeddings/oracleai.md)                         | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                          |

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
