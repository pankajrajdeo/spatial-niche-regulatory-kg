---
title: "Tavily integrations"
description: "Integrate with Tavily using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/tavily"
category: "docs"
tags: [docs, integrations, providers, tavily]
---

# Tavily integrations

> Integrate with Tavily using LangChain Python.

[Tavily](https://tavily.com) is a search engine specifically designed for AI agents, providing search, extract, crawl, and map APIs so developers can connect their applications to real-time online information. Tavily's primary mission is to deliver factual and reliable information from trusted sources, enhancing the accuracy and reliability of AI-generated content and reasoning.

The `langchain-tavily` package exposes Tavily's Search, Extract, Crawl, and Map endpoints as LangChain tools.

## Installation and setup

Install the Tavily integration package for LangChain Python:

**pip**

```bash
pip install langchain-tavily
```

**uv**

```bash
uv add langchain-tavily
```

[Set up a Tavily API key](https://app.tavily.com) and set it as an environment variable named `TAVILY_API_KEY`:

```bash
export TAVILY_API_KEY="your-api-key"
```

## Tools

### TavilySearch

A search tool that returns real-time, LLM-ready results from Tavily's Search API.

See a [usage example](../tools/tavily_search.md).

```python
from langchain_tavily import TavilySearch
```

### TavilyExtract

A tool that returns the cleaned, parsed content of one or more URLs.

See a [usage example](../tools/tavily_extract.md).

```python
from langchain_tavily import TavilyExtract
```

### TavilyCrawl

A tool that performs a structured web traversal from a base URL, with optional natural-language instructions and path/domain filters.

See a [usage example](../tools/tavily_crawl.md).

```python
from langchain_tavily import TavilyCrawl
```

### TavilyMap

A tool that discovers the URL structure of a site without extracting page content.

See a [usage example](../tools/tavily_map.md).

```python
from langchain_tavily import TavilyMap
```

## Components reference

| Class                                                                                                   | Abstraction | Import path                                  | Description                                                             |
| ------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------- | ----------------------------------------------------------------------- |
| [`TavilySearch`](https://reference.langchain.com/python/langchain-tavily/tavily_search/TavilySearch)    | Tool        | `from langchain_tavily import TavilySearch`  | Returns search results from the Tavily Search API.                      |
| [`TavilyExtract`](https://reference.langchain.com/python/langchain-tavily/tavily_extract/TavilyExtract) | Tool        | `from langchain_tavily import TavilyExtract` | Extracts cleaned content from one or more URLs.                         |
| [`TavilyCrawl`](https://reference.langchain.com/python/langchain-tavily/tavily_crawl/TavilyCrawl)       | Tool        | `from langchain_tavily import TavilyCrawl`   | Crawls a site starting from a base URL with depth and breadth controls. |
| [`TavilyMap`](https://reference.langchain.com/python/langchain-tavily/tavily_map/TavilyMap)             | Tool        | `from langchain_tavily import TavilyMap`     | Discovers the URL structure of a site without extracting page content.  |

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/tavily.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
