---
title: "Contributing integrations"
description: "Integrations are a core component of LangChain."
source: "https://docs.langchain.com/oss/javascript/contributing/integrations-langchain"
category: "docs"
tags: [docs, javascript, contributing, integrations-langchain]
---

# Contributing integrations

**Integrations are a core component of LangChain.**

LangChain provides standard interfaces for several different components (language models, vector stores, etc) that are crucial when building LLM applications. Implementing a new integration helps expand LangChain's ecosystem and makes your service discoverable to millions of developers.

> [!WARNING]
> New integrations are **not accepted as PRs** to any `langchain-ai` repository. All new integrations must be published as independent packages to PyPI (e.g., `langchain-yourprovider`). The only PR you should open to a `langchain-ai` repo is to list your published package in the docs: either a YAML row for the download table, or a hosted guide if you meet the [eligibility criteria](publish-langchain.md#eligibility-for-hosted-guides).

## Why implement a LangChain integration?

#### Discoverability
LangChain is the most used framework for building LLM applications, with over 200 million monthly downloads.

#### Interoperability
LangChain components expose a standard interface, allowing developers to easily swap them for each other. If you implement a LangChain integration, any developer using a different component will easily be able to swap yours in.

#### Best Practices
Through their standard interface, LangChain components encourage and facilitate best practices (streaming, async, etc.) that improve developer experience and application performance.

## Components to integrate

While any component can be integrated into LangChain, there are specific types of integrations we encourage more:

**Integrate these ✅**:

* [**Chat Models**](../integrations/chat.md): Most actively used component type
* [**Tools/Toolkits**](../integrations/tools.md): Enable agent capabilities
* [**Retrievers**](../integrations/retrievers.md): Core to RAG applications
* [**Embedding Models**](../integrations/embeddings.md): Foundation for vector operations
* [**Vector Stores**](../integrations/vectorstores.md): Essential for semantic search
* [**Middleware**](../integrations/middleware.md): Extend agent behavior with hooks
* [**Sandboxes**](../deepagents/sandboxes.md): Run code safely with Deep Agents

**Not these ❌**:

* **LLMs (Text-Completion Models)**: Deprecated in favor of [Chat Models](../integrations/chat.md)
* [**Document Loaders**](../integrations/document_loaders.md): High maintenance burden
* [**Key-Value Stores**](../integrations/stores.md): Limited usage
* **Document Transformers**: Niche use cases
* **Model Caches**: Infrastructure concerns
* **Graphs**: Complex abstractions
* **Message Histories**: Storage abstractions
* **Callbacks**: System-level components
* **Chat Loaders**: Limited demand
* **Adapters**: Edge case utilities

## How to contribute an integration

### Implement your package
#### [How to implement a LangChain integration](implement-langchain.md)

### Pass standard tests
If applicable, implement support for LangChain's [standard test](standard-tests-langchain.md) suite for your integration and successfully run them.

### Publish integration
#### [How to publish an integration](publish-langchain.md)

### List your integration
Open a PR in the LangChain [docs repo](https://github.com/langchain-ai/docs) so users can find your package. Hosted guides are limited; most integrations are listed via YAML.

<details>
<summary>How listing works</summary>

**Default (under 50,000 monthly downloads, not featured):** File an [Integration listing issue](https://github.com/langchain-ai/docs/issues/new?template=06-integration-submission.yml). After a maintainer applies `integration-run`, automation opens a PR that adds a row to [`scripts/data/integration_external_docs.yaml`](https://github.com/langchain-ai/docs/blob/main/scripts/data/integration_external_docs.yaml). The name column links to your `docs_url` (partner docs preferred, then GitHub, then PyPI or npm). Do not add a new MDX page.

**Hosted guide (50,000+ monthly downloads, or featured by maintainers):** Create a page under `src/oss/python/integrations/<component_type>/` from a template:

* [Chat models](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/chat/TEMPLATE.mdx)
* [Tools and toolkits](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/tools/TEMPLATE.mdx)
* [Middleware](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/middleware/TEMPLATE.mdx)
* [Vector stores](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/vectorstores/TEMPLATE.mdx)

For full steps, eligibility details, and rejection criteria, see [Publish an integration](publish-langchain.md#make-your-integration-discoverable).

</details>

### Co-marketing
(Optional) Engage with the LangChain team for joint [co-marketing](comarketing.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/integrations-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
