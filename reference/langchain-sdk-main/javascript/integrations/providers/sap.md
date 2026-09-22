---
title: "Sap integrations"
description: "Integrate with Sap using LangChain Python."
source: "https://docs.langchain.com/oss/javascript/integrations/providers/sap"
category: "docs"
tags: [docs, javascript, integrations, providers, sap]
---

# Sap integrations

> Integrate with Sap using LangChain Python.

> [SAP SE(Wikipedia)](https://www.sap.com/about/company.html) is a German multinational
> software company. It develops enterprise software to manage business operation and
> customer relations. The company is the world's leading
> `enterprise resource planning (ERP)` software vendor.

## Installation and setup

We need to install the `@sap/hana-langchain` package along with its peer dependencies.

**npm**

```bash
npm install @sap/hana-langchain @langchain/core@latest @langchain/classic@latest langchain@latest
```

**yarn**

```bash
yarn add @sap/hana-langchain @langchain/core@latest @langchain/classic@latest langchain@latest
```

**pnpm**

```bash
pnpm add @sap/hana-langchain @langchain/core@latest @langchain/classic@latest langchain@latest
```

## Vectorstore

> [SAP HANA Cloud Vector Engine](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-vector-engine-guide/sap-hana-cloud-sap-hana-database-vector-engine-guide) is
> a vector store fully integrated into the `SAP HANA Cloud` database.

See a [usage example](../vectorstores/sap_hanavector.md).

```typescript
import { HanaDB } from "@sap/hana-langchain";
```

## Self Query Retriever

> [SAP HANA Cloud Vector Engine](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-vector-engine-guide/sap-hana-cloud-sap-hana-database-vector-engine-guide)
> also provides a Self Query Retriever implementation using the `HanaTranslator` Class.

See a [usage example](https://pypi.org/project/langchain-hana/).

```typescript
import { HanaTranslator } from "@sap/hana-langchain";
```

## Graph

> [SAP HANA Cloud Knowledge Graph Engine](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-knowledge-graph-guide/sap-hana-cloud-sap-hana-database-knowledge-graph-engine-guide)
> provides support to utilise knowledge graphs through the `HanaRdfGraph` Class.

See a [usage example](../graphs/sap_hana_rdf_graph.md).

```typescript
import { HanaRdfGraph } from "@sap/hana-langchain";
```

## Chains

A `SparqlQAChain` is also provided which can be used with `HanaRdfGraph` for SPARQL-QA tasks.

See a [usage example](../chains/sap_hana_sparql_qa_chain.md).

```typescript
import { HanaSparqlQAChain } from "@sap/hana-langchain";
```

## Agents

A `HanaSparqlQAAgent` can generate and execute SPARQL queries iteratively over `HanaRdfGraph`, including ontology retrieval and self-correction.

See a [usage example](../agents/sap_hana_sparql_qa_agent.md).

```typescript
import { HanaSparqlQAAgent } from "@sap/hana-langchain";
```

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/sap.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
