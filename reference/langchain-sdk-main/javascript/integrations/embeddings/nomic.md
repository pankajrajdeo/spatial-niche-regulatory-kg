---
title: "Nomic integration"
description: "Integrate with the Nomic embedding model using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/embeddings/nomic"
category: "docs"
tags: [docs, javascript, integrations, embeddings, nomic]
---

# Nomic integration

> Integrate with the Nomic embedding model using LangChain JavaScript.

The `NomicEmbeddings` class uses the Nomic AI API to generate embeddings for a given text.

## Setup

In order to use the Nomic API you'll need to [sign up for a Nomic account and create an API key](https://atlas.nomic.ai/).

You'll first need to install the [`@langchain/nomic`](https://www.npmjs.com/package/@langchain/nomic) package:

> [!TIP]
> See [this section for general instructions on installing LangChain packages](../../langchain/install.md).

**npm**

```bash
npm install @langchain/nomic @langchain/core
```

## Usage

```typescript
import { NomicEmbeddings } from "@langchain/nomic";

/* Embed queries */
const nomicEmbeddings = new NomicEmbeddings();
const res = await nomicEmbeddings.embedQuery("Hello world");
console.log(res);
/* Embed documents */
const documentRes = await nomicEmbeddings.embedDocuments([
  "Hello world",
  "Bye bye",
]);
console.log(documentRes);
```

## Related

* Embedding model [conceptual guide](../embeddings.md)
* Embedding model [how-to guides](../embeddings.md)

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/nomic.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
