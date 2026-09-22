---
title: "Perplexity integrations"
description: "Integrate with Perplexity using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/perplexity"
category: "docs"
tags: [docs, integrations, providers, perplexity]
---

# Perplexity integrations

> Integrate with Perplexity using LangChain Python.

> [Perplexity](https://www.perplexity.ai/pro) is the most powerful way to search
> the internet with unlimited Pro Search, upgraded AI models, unlimited file upload,
> image generation, and API credits.
>
> You can check a [list of available models](https://docs.perplexity.ai/docs/model-cards).

## Installation and setup

Install the Perplexity x LangChain integration package:

**pip**

```bash
pip install langchain-perplexity
```

**uv**

```bash
uv add langchain-perplexity
```

Get your API key from the [Perplexity API key dashboard](https://www.perplexity.ai/account/api/keys) and set it as the `PERPLEXITY_API_KEY` (or `PPLX_API_KEY`) environment variable. See the [Perplexity getting started guide](https://docs.perplexity.ai/docs/getting-started) for more details.

## Chat models

See a variety of [Perplexity usage examples](../chat/perplexity.md).

```python
from langchain_perplexity import ChatPerplexity
```

`ChatPerplexity` can also target the [Perplexity Agent API](https://docs.perplexity.ai/api-reference/agent-api) by passing `use_responses_api=True` (or by passing `tools=[{"type": "web_search"}]`, which auto-enables it). See [Agent API support](../chat/perplexity.md#agent-api-support-use_responses_api) on the chat page for details and examples.

## Retriever

You can use the [`PerplexitySearchRetriever`](../retrievers/perplexity_search.md) to fetch web search results from the [Perplexity Search API](https://docs.perplexity.ai/docs/search/quickstart) as [`Document`](https://reference.langchain.com/python/langchain-core/documents/base/Document) objects in a standard retrieval pipeline.

See a [usage example](../retrievers/perplexity_search.md).

```python
from langchain_perplexity import PerplexitySearchRetriever
```

## Tools

You can use Perplexity as an agent tool to give your agent access to the Perplexity Search API.

See a [usage example](../tools/perplexity_search.md).

### PerplexitySearchResults

A tool that queries the Perplexity Search API and returns a JSON array of results (title, URL, snippet, date, last updated).

```python
from langchain_perplexity import PerplexitySearchResults
```

## Embedding models

You can use [`PerplexityEmbeddings`](../embeddings/perplexity.md) to generate embeddings via the [Perplexity Embeddings API](https://docs.perplexity.ai/api-reference/embeddings-post).

See a [usage example](../embeddings/perplexity.md).

```python
from langchain_perplexity import PerplexityEmbeddings
```

## Deep Agents Code

Use Perplexity as a first-class provider in [Deep Agents Code](../../deepagents/code/providers.md).

Install Deep Agents Code with the Perplexity extra:

**uv**

```bash
uv tool install 'deepagents-code[perplexity]'
```

Then set `PERPLEXITY_API_KEY` and reference Perplexity models with the `perplexity:` prefix (e.g. `perplexity:sonar-pro`) in the interactive `/model` switcher or your config.

## Components reference

| Class                       | Abstraction | Import path                                                  | Description                                                                 |
| --------------------------- | ----------- | ------------------------------------------------------------ | --------------------------------------------------------------------------- |
| `ChatPerplexity`            | Chat model  | `from langchain_perplexity import ChatPerplexity`            | Chat model wrapping the Perplexity API for grounded chat completions.       |
| `PerplexitySearchRetriever` | Retriever   | `from langchain_perplexity import PerplexitySearchRetriever` | Retriever that returns `Document` objects from the Perplexity Search API.   |
| `PerplexitySearchResults`   | Tool        | `from langchain_perplexity import PerplexitySearchResults`   | Tool that returns Perplexity Search API results as a JSON array for agents. |
| `PerplexityEmbeddings`      | Embeddings  | `from langchain_perplexity import PerplexityEmbeddings`      | Embedding model wrapping the Perplexity Embeddings API.                     |

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/perplexity.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
