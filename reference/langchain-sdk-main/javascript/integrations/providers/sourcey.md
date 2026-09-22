---
title: "Sourcey integrations"
description: "Retrieve from published Sourcey docs sites using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/providers/sourcey"
category: "docs"
tags: [docs, javascript, integrations, providers, sourcey]
---

# Sourcey integrations

> Retrieve from published Sourcey docs sites using LangChain JavaScript.

[Sourcey](https://sourcey.com) builds static docs sites.

Use `langchain-sourcey` to retrieve from a published Sourcey docs site. It
reads `search-index.json`, uses `llms-full.txt` when present, and returns
canonical page URLs for citation.

## Installation and setup

Install `langchain-sourcey`:

**npm**

```bash
npm install langchain-sourcey @langchain/core
```

**yarn**

```bash
yarn add langchain-sourcey @langchain/core
```

**pnpm**

```bash
pnpm add langchain-sourcey @langchain/core
```

No API key is required.

Point the retriever at the root of a published Sourcey docs build. It reads
`search-index.json` for candidate pages and `llms-full.txt` for full-page
content when that file is present.

## Retriever

You can use [`SourceyRetriever`](../retrievers/sourcey.md) in a
standard retrieval pipeline.

```typescript
import { SourceyRetriever } from "langchain-sourcey";
```

See the [usage example](../retrievers/sourcey.md) or the
[Sourcey guide](https://sourcey.com/docs/guides/guide-langchain-retriever).

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/sourcey.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
