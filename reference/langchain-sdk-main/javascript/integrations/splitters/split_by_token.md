---
title: "Splitting by token - Text splitter integration guide"
description: "Language models have a token limit. You should not exceed the token limit. When you split your text into chunks it is therefore a good idea to count the number of tokens. There are many tokenizers..."
source: "https://docs.langchain.com/oss/javascript/integrations/splitters/split_by_token"
category: "docs"
tags: [docs, javascript, integrations, splitters, split_by_token]
---

# Splitting by token - Text splitter integration guide

Language models have a token limit. You should not exceed the token limit. When you [split your text](../splitters.md) into chunks it is therefore a good idea to count the number of tokens. There are many tokenizers. When you count tokens in your text you should use the same tokenizer as used in the language model.

## js-tiktoken

> [!NOTE]
> **[js-tiktoken](https://github.com/dqbd/tiktoken) is a JavaScript vesrion of the `BPE` tokenizer created by `OpenAI`.**

We can use `tiktoken` to estimate tokens used using [TokenTextSplitter](https://reference.langchain.com/javascript/langchain-textsplitters/TokenTextSplitter). It will probably be more accurate for OpenAI models.

1. How the text is split: by character passed in.
2. How the chunk size is measured: by `tiktoken` tokenizer.

**npm**

```bash
npm install @langchain/textsplitters
```

**pnpm**

```bash
pnpm install @langchain/textsplitters
```

**yarn**

```bash
yarn add @langchain/textsplitters
```

**bun**

```bash
bun add @langchain/textsplitters
```

```ts
import { TokenTextSplitter } from "@langchain/textsplitters";
import { readFileSync } from "fs";

// Example: read a long document
const stateOfTheUnion = readFileSync("state_of_the_union.txt", "utf8");
```

To split with a [TokenTextSplitter](https://reference.langchain.com/javascript/langchain-textsplitters/TokenTextSplitter) and then merge chunks with `tiktoken`, pass in an `encodingName` (e.g. cl100k\_base) when initializing the [TokenTextSplitter](https://reference.langchain.com/javascript/langchain-textsplitters/TokenTextSplitter). Note that splits from this method can be larger than the chunk size measured by the `tiktoken` tokenizer.

```ts
import { TokenTextSplitter } from "@langchain/textsplitters";

// Example: use cl100k_base encoding
const splitter = new TokenTextSplitter({ encodingName: "cl100k_base", chunkSize: 10, chunkOverlap: 0 });

const texts = splitter.splitText(stateOfTheUnion);
console.log(texts[0]);
```

```text
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.

Last year COVID-19 kept us apart. This year we are finally together again.

Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans.

With a duty to one another to the American people to the Constitution.
```

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/integrations/splitters/split_by_token.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
