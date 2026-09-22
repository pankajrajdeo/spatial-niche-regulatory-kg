---
title: "Minimax integration"
description: "Integrate with the Minimax embedding model using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/embeddings/minimax"
category: "docs"
tags: [docs, javascript, integrations, embeddings, minimax]
---

# Minimax integration

> Integrate with the Minimax embedding model using LangChain JavaScript.

The `MinimaxEmbeddings` class uses the Minimax API to generate embeddings for a given text.

# Setup

To use Minimax model, you'll need a Minimax account, an API key, and a Group ID.

# Usage

```typescript
import { MinimaxEmbeddings } from "@langchain/classic/embeddings/minimax";

export const run = async () => {
  /* Embed queries */
  const embeddings = new MinimaxEmbeddings();
  const res = await embeddings.embedQuery("Hello world");
  console.log(res);
  /* Embed documents */
  const documentRes = await embeddings.embedDocuments([
    "Hello world",
    "Bye bye",
  ]);
  console.log({ documentRes });
};
```

## Related

* Embedding model [conceptual guide](../embeddings.md)
* Embedding model [how-to guides](../embeddings.md)

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/minimax.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
