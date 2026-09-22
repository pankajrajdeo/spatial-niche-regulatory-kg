---
title: "Dall-e integration"
description: "Integrate with the Dall-e tool using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/tools/dalle"
category: "docs"
tags: [docs, javascript, integrations, tools, dalle]
---

# Dall-e integration

> Integrate with the Dall-e tool using LangChain JavaScript.

```typescript
/* eslint-disable no-process-env */
import { DallEAPIWrapper } from "@langchain/openai";

const tool = new DallEAPIWrapper({
  n: 1, // Default
  model: "dall-e-3", // Default
  apiKey: process.env.OPENAI_API_KEY, // Default
});

const imageURL = await tool.invoke("a painting of a cat");

console.log(imageURL);
```

## Related

* Tool [conceptual guide](../../langchain/tools.md)
* Tool [how-to guides](../../langchain/tools.md)

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/tools/dalle.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
