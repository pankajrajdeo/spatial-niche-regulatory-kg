---
title: "Sap integrations"
description: "Integrate with Sap using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/sap"
category: "docs"
tags: [docs, integrations, providers, sap]
---

# Sap integrations

> Integrate with Sap using LangChain Python.

> [SAP SE(Wikipedia)](https://www.sap.com/about/company.html) is a German multinational
> software company. It develops enterprise software to manage business operation and
> customer relations. The company is the world's leading
> `enterprise resource planning (ERP)` software vendor.

## Installation and setup

We need to install the `langchain-hana` python package.

**pip**

```bash
pip install langchain-hana
```

**uv**

```bash
uv add langchain-hana
```

## Vectorstore

> [SAP HANA Cloud Vector Engine](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-vector-engine-guide/sap-hana-cloud-sap-hana-database-vector-engine-guide) is
> a vector store fully integrated into the `SAP HANA Cloud` database.

See a [usage example](../vectorstores/sap_hanavector.md).

```python
from langchain_hana import HanaDB
```

## Self Query Retriever

> [SAP HANA Cloud Vector Engine](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-vector-engine-guide/sap-hana-cloud-sap-hana-database-vector-engine-guide)
> also provides a Self Query Retriever implementation using the `HanaTranslator` Class.

See a [usage example](https://pypi.org/project/langchain-hana/).

```python
from langchain_hana import HanaTranslator
```

## Graph

> [SAP HANA Cloud Knowledge Graph Engine](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-knowledge-graph-guide/sap-hana-cloud-sap-hana-database-knowledge-graph-engine-guide)
> provides support to utilise knowledge graphs through the `HanaRdfGraph` Class.

See a [usage example](../graphs/sap_hana_rdf_graph.md).

```python
from langchain_hana import HanaRdfGraph
```

## Chains

A `SparqlQAChain` is also provided which can be used with `HanaRdfGraph` for SPARQL-QA tasks.

See a [usage example](../chains/sap_hana_sparql_qa_chain.md).

```python
from langchain_hana import HanaSparqlQAChain
```

## Agents

A `HanaSparqlQAAgent` can generate and execute SPARQL queries iteratively over `HanaRdfGraph`, including ontology retrieval and self-correction.

See a [usage example](../agents/sap_hana_sparql_qa_agent.md).

```python
from langchain_hana import HanaSparqlQAAgent
```

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/sap.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
