---
title: "Docugami integrations"
description: "Integrate with Docugami using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/docugami"
category: "docs"
tags: [docs, integrations, providers, docugami]
---

# Docugami integrations

> Integrate with Docugami using LangChain Python.

> [Docugami](https://docugami.com) converts business documents into a Document XML Knowledge Graph, generating forests
> of XML semantic trees representing entire documents. This is a rich representation that includes the semantic and
> structural characteristics of various chunks in the document as an XML tree.

## Installation and setup

**pip**

```bash
pip install dgml-utils
pip install docugami-langchain
```

**uv**

```bash
uv add dgml-utils
uv add docugami-langchain
```

## Document loader

See a [usage example](../document_loaders/docugami.md).

```python
from docugami_langchain.document_loaders import DocugamiLoader
```

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/docugami.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
