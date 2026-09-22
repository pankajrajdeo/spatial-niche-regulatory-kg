---
title: "Retriever integrations"
description: "Integrate with retrievers using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/retrievers"
category: "docs"
tags: [docs, javascript, integrations, retrievers]
---

# Retriever integrations

> Integrate with retrievers using LangChain JavaScript.

A [retriever](../deepagents/retrieval.md) is an interface that returns documents given an unstructured query.
It is more general than a vector store.
A retriever does not need to be able to store documents, only to return (or retrieve) them.

Retrievers accept a string query as input and return a list of `Document` objects.

For specifics on how to use retrievers, see the [relevant how-to guides here](../deepagents/retrieval.md).

Note that all [vector stores](vectorstores.md) can be [cast to retrievers](../deepagents/retrieval.md).
Refer to the vector store [integration docs](vectorstores.md) for available vector store retrievers.

## All retrievers

| Retriever                                                                                                                     | Self-host                          | Cloud offering                     | Package                                                                                | Downloads                                                                                                                                                                                                                                                                               |
| :---------------------------------------------------------------------------------------------------------------------------- | :--------------------------------- | :--------------------------------- | :------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`AWSKendraRetriever`](retrievers/kendra-retriever.md)                                              | <span data-sort-value="0" />       | <span data-sort-value="0" />       | [`@langchain/aws`](https://www.npmjs.com/package/@langchain/aws)                       | <span data-sort-value="2940428"><a href="https://www.npmjs.com/package/@langchain/aws" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/aws?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`Knowledge bases for Amazon Bedrock`](retrievers/bedrock-knowledge-bases.md)                       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | [`@langchain/aws`](https://www.npmjs.com/package/@langchain/aws)                       | <span data-sort-value="2940428"><a href="https://www.npmjs.com/package/@langchain/aws" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/aws?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`ExaRetriever`](retrievers/exa.md)                                                                 | <span data-sort-value="0" />       | <span data-sort-value="0" />       | [`@langchain/exa`](https://www.npmjs.com/package/@langchain/exa)                       | <span data-sort-value="64698"><a href="https://www.npmjs.com/package/@langchain/exa" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/exa?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`PerplexitySearchRetriever`](retrievers/perplexity_search.md)                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | [`@langchain/perplexity`](https://www.npmjs.com/package/@langchain/perplexity)         | <span data-sort-value="706"><a href="https://www.npmjs.com/package/@langchain/perplexity" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/perplexity?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>        |
| [`AlchemystRetriever`](https://getalchemystai.com/docs)                                                                       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | [`@alchemystai/langchain-js`](https://www.npmjs.com/package/@alchemystai/langchain-js) | <span data-sort-value="50"><a href="https://www.npmjs.com/package/@alchemystai/langchain-js" target="_blank">  <img src="https://img.shields.io/npm/dm/@alchemystai/langchain-js?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`FoxNoseRetriever`](https://github.com/FoxNoseTech/langchain-foxnose-js#readme)                                              | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | [`@foxnose/langchain`](https://www.npmjs.com/package/@foxnose/langchain)               | <span data-sort-value="17"><a href="https://www.npmjs.com/package/@foxnose/langchain" target="_blank">  <img src="https://img.shields.io/npm/dm/@foxnose/langchain?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>               |
| [`SourceyRetriever`](retrievers/sourcey.md)                                                         | <span data-sort-value="0" />       | <span data-sort-value="0" />       | [`langchain-sourcey`](https://www.npmjs.com/package/langchain-sourcey)                 | <span data-sort-value="17"><a href="https://www.npmjs.com/package/langchain-sourcey" target="_blank">  <img src="https://img.shields.io/npm/dm/langchain-sourcey?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                 |
| [`Hyde`](retrievers/hyde.md)                                                                        | <span data-sort-value="0" />       | <span data-sort-value="0" />       |                                                                                        | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                   |
| [`Self Querying with SAP HANA Cloud Vector Engine`](retrievers/self_query/hanavector_self_query.md) | <span data-sort-value="0" />       | <span data-sort-value="0" />       |                                                                                        | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                   |
| [`Time-weighted`](retrievers/time-weighted-retriever.md)                                            | <span data-sort-value="0" />       | <span data-sort-value="0" />       |                                                                                        | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                   |

> [!NOTE]
> If you'd like to contribute an integration, see [Contributing integrations](../contributing.md#add-a-new-integration).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/retrievers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
