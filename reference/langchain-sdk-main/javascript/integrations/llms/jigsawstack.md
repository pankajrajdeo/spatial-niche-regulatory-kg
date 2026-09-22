---
title: "Jigsawstack prompt engine integration"
description: "Integrate with the Jigsawstack prompt engine LLM using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/llms/jigsawstack"
category: "docs"
tags: [docs, javascript, integrations, llms, jigsawstack]
---

# Jigsawstack prompt engine integration

> Integrate with the Jigsawstack prompt engine LLM using LangChain JavaScript.

LangChain.js supports calling JigsawStack [Prompt Engine](https://docs.jigsawstack.com/api-reference/prompt-engine/run-direct) LLMs.

## Setup

* Set up an [account](https://jigsawstack.com/dashboard) (Get started for free)
* Create and retrieve your [API key](https://jigsawstack.com/dashboard)

## Credentials

```bash
export JIGSAWSTACK_API_KEY="your-api-key"
```

## Usage

> [!TIP]
> See [this section for general instructions on installing LangChain packages](../../langchain/install.md).

**npm**

```bash
npm install @langchain/jigsawstack
```

```ts
import { JigsawStackPromptEngine } from "@langchain/jigsawstack";

export const run = async () => {
  const model = new JigsawStackPromptEngine();
  const res = await model.invoke(
    "Tell me about the leaning tower of pisa?\nAnswer:"
  );
  console.log({ res });
};
```

## Related

* [Models guide](../../langchain/models.md)

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/llms/jigsawstack.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
