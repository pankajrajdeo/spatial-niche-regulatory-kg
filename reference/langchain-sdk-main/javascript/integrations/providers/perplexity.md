---
title: "Perplexity integrations"
description: "Integrate with Perplexity using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/providers/perplexity"
category: "docs"
tags: [docs, javascript, integrations, providers, perplexity]
---

# Perplexity integrations

> Integrate with Perplexity using LangChain JavaScript.

> [Perplexity](https://www.perplexity.ai/pro) is the most powerful way to search
> the internet with unlimited Pro Search, upgraded AI models, unlimited file upload,
> image generation, and API credits.

## Installation and setup

Install the Perplexity integration package for LangChain JavaScript:

**npm**

```bash
npm install @langchain/perplexity @langchain/core
```

**yarn**

```bash
yarn add @langchain/perplexity @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/perplexity @langchain/core
```

Get your API key from the [Perplexity API key dashboard](https://www.perplexity.ai/account/api/keys) and set it as the `PERPLEXITY_API_KEY` environment variable. See the [Perplexity getting started guide](https://docs.perplexity.ai/docs/getting-started) for more details.

```bash
export PERPLEXITY_API_KEY="your-api-key"
```

## Chat model

See a [usage example](../chat/perplexity.md).

```typescript
import { ChatPerplexity } from "@langchain/perplexity";
```

`ChatPerplexity` can also target the [Perplexity Agent API](https://docs.perplexity.ai/api-reference/agent-api) by passing `useResponsesApi: true` (or by passing `tools: [{ type: "web_search" }]`, which auto-enables it). See [Agent API support](../chat/perplexity.md#agent-api-support-useresponsesapi) on the chat page for details and examples.

## Retriever

You can use the [`PerplexitySearchRetriever`](../retrievers/perplexity_search.md) to fetch web search results from the [Perplexity Search API](https://docs.perplexity.ai/docs/search/quickstart) as `Document` objects in a standard retrieval pipeline.

See a [usage example](../retrievers/perplexity_search.md).

```typescript
import { PerplexitySearchRetriever } from "@langchain/perplexity";
```

## Tools

You can use Perplexity as an agent tool to give your agent access to the Perplexity Search API.

See a [usage example](../tools/perplexity_search.md).

### PerplexitySearchResults

A tool that queries the Perplexity Search API and returns a JSON array of results (title, URL, snippet, date, last updated).

```typescript
import { PerplexitySearchResults } from "@langchain/perplexity";
```

## Components reference

| Class                       | Abstraction | Import path                                                         | Description                                                                 |
| --------------------------- | ----------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `ChatPerplexity`            | Chat model  | `import { ChatPerplexity } from "@langchain/perplexity"`            | Chat model wrapping the Perplexity API for grounded chat completions.       |
| `PerplexitySearchRetriever` | Retriever   | `import { PerplexitySearchRetriever } from "@langchain/perplexity"` | Retriever that returns `Document` objects from the Perplexity Search API.   |
| `PerplexitySearchResults`   | Tool        | `import { PerplexitySearchResults } from "@langchain/perplexity"`   | Tool that returns Perplexity Search API results as a JSON array for agents. |

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/perplexity.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
