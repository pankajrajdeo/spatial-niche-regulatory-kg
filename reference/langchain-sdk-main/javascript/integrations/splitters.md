---
title: "Text splitter integrations"
description: "Integrate with text splitters using LangChain."
source: "https://docs.langchain.com/oss/javascript/integrations/splitters"
category: "docs"
tags: [docs, javascript, integrations, splitters]
---

# Text splitter integrations

> Integrate with text splitters using LangChain.

**npm**

```bash
npm install @langchain/textsplitters @langchain/core
# Requires Node.js 22+
```

**pnpm**

```bash
pnpm add @langchain/textsplitters @langchain/core
# Requires Node.js 22+
```

**yarn**

```bash
yarn add @langchain/textsplitters @langchain/core
# Requires Node.js 22+
```

**bun**

```bash
bun add @langchain/textsplitters @langchain/core
# Requires Node.js 22+
```

**Text splitters** break large docs into smaller chunks that will be retrievable individually and fit within model context window limit.

There are several strategies for splitting documents, each with its own advantages.

> [!TIP]
> For most use cases, start with the [`RecursiveCharacterTextSplitter`](splitters/recursive_text_splitter.md). It provides a solid balance between keeping context intact and managing chunk size. This default strategy works well out of the box, and you should only consider adjusting it if you need to fine-tune performance for your specific application.

## Text structure-based

Text is naturally organized into hierarchical units such as paragraphs, sentences, and words. We can leverage this inherent structure to inform our splitting strategy, creating split that maintain natural language flow, maintain semantic coherence within split, and adapts to varying levels of text granularity. LangChain's `RecursiveCharacterTextSplitter` implements this concept:

* The [`RecursiveCharacterTextSplitter`](splitters/recursive_text_splitter.md) attempts to keep larger units (e.g., paragraphs) intact.
* If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
* This process continues down to the word level if necessary.

Example usage:

```ts
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

const splitter = new RecursiveCharacterTextSplitter({ chunkSize: 100, chunkOverlap: 0 })
const texts = splitter.splitText(document)
```

**Available text splitters**:

* [Recursively split text](splitters/recursive_text_splitter.md)

## Length-based

An intuitive strategy is to split documents based on their length. This simple yet effective approach ensures that each chunk doesn't exceed a specified size limit. Key benefits of length-based splitting:

* Straightforward implementation
* Consistent chunk sizes
* Easily adaptable to different model requirements

Types of length-based splitting:

* Token-based: Splits text based on the number of tokens, which is useful when working with language models.
* Character-based: Splits text based on the number of characters, which can be more consistent across different types of text.

Example implementation using LangChain's `CharacterTextSplitter` with token-based splitting:

```ts
import { TokenTextSplitter } from "@langchain/textsplitters";

const splitter = new TokenTextSplitter({ encodingName: "cl100k_base", chunkSize: 100, chunkOverlap: 0 })
const texts = splitter.splitText(document)
```

**Available text splitters**:

* [Split by tokens](splitters/split_by_token.md)
* [Split by characters](splitters/character_text_splitter.md)

## Document structure-based

Some documents have an inherent structure, such as HTML, Markdown, or JSON files. In these cases, it's beneficial to split the document based on its structure, as it often naturally groups semantically related text. Key benefits of structure-based splitting:

* Preserves the logical organization of the document
* Maintains context within each chunk
* Can be more effective for downstream tasks like retrieval or summarization

**Available text splitters**:

* [Split code](splitters/code_splitter.md)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/integrations/splitters/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
