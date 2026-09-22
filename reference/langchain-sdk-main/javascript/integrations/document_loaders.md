---
title: "Document loader integrations"
description: "Integrate with document loaders using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/document_loaders"
category: "docs"
tags: [docs, javascript, integrations, document_loaders]
---

# Document loader integrations

> Integrate with document loaders using LangChain JavaScript.

Document loaders provide a **standard interface** for reading data from different sources (such as Slack, Notion, or Google Drive) into LangChain's [Document](https://reference.langchain.com/javascript/langchain-core/documents/Document) format.
This ensures that data can be handled consistently regardless of the source.

All document loaders implement the [BaseLoader](https://reference.langchain.com/javascript/langchain-core/document_loaders/base/BaseDocumentLoader) interface.

> [!WARNING]
> Community document loaders are user-contributed and unverified. LangChain does not review or endorse these integrations; use them at your own risk.

## Interface

Each document loader may define its own parameters, but they share a common API:

* `load()`: Loads all documents at once.
* `loadAndSplit()`: Loads all documents at once and splits them into smaller documents.

```typescript
import { OracleDocLoader } from "@oracle/langchain-oracledb";

const loader = new OracleDocLoader(,
  ...  // <-- Integration specific parameters here
);
const data = await loader.load();
```

## By category

LangChain.js categorizes document loaders in two different ways:

* [File loaders](document_loaders/file_loaders.md), which load data into LangChain formats from your local filesystem.
* [Web loaders](document_loaders/web_loaders.md), which load data from remote sources.

### File loaders

> [!NOTE]
> If you'd like to contribute an integration, see [Contributing integrations](../contributing.md#add-a-new-integration).

#### Common file types

| Document Loader                                                                           | Description                                                 | Package/API |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------- |
| [`DirectoryLoader`](document_loaders/file_loaders/directory.md) | Load all files from a directory with custom loader mappings | Package     |
| [JSON](document_loaders/file_loaders/json.md)                   | Load JSON files using JSON pointer to target specific keys  | Package     |
| [`JSONLines`](document_loaders/file_loaders/jsonlines.md)       | Load data from JSONLines/JSONL files                        | Package     |
| [`Text`](document_loaders/file_loaders/text.md)                 | Load plain text files                                       | Package     |

#### Specialized file loaders

| Document Loader                                                                            | Description                                                          | Package/API |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ----------- |
| [`MultiFileLoader`](document_loaders/file_loaders/multi_file.md) | Load data from multiple individual file paths                        | Package     |
| [`OracleDocLoader`](document_loaders/file_loaders/oracleai.md)   | Ingest Oracle AI Vector Search tables or Oracle Text-supported files | Package     |

### Web loaders

#### Cloud providers

| Document Loader                                                                                                 | Description                                        | Web Support | Package/API |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | :---------: | ----------- |
| [Google Cloud SQL for PostgreSQL](document_loaders/web_loaders/google_cloudsql_pg.md) | Load documents from Cloud SQL PostgreSQL databases |      ✅      | Package     |

#### Audio & video

| Document Loader                                                              | Description                                                                    | Web Support | Package/API |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | :---------: | ----------- |
| [`Soniox`](document_loaders/web_loaders/soniox.md) | Transcribe multilingual audio files with optional translation using Soniox API |      ✅      | API         |

#### Other

| Document Loader                                                                    | Description                             | Web Support | Package/API |
| ---------------------------------------------------------------------------------- | --------------------------------------- | :---------: | ----------- |
| [`LangSmith`](document_loaders/web_loaders/langsmith.md) | Load datasets and traces from LangSmith |      ✅      | API         |

## All document loaders

| Integration                                                                                                       | Downloads                                                                                                                                                                                                                                                                                          |
| :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Google cloud SQL for postgresql`](document_loaders/web_loaders/google_cloudsql_pg.md) | <span data-sort-value="619"><a href="https://www.npmjs.com/package/@langchain/google-cloud-sql-pg" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/google-cloud-sql-pg?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`Soniox`](document_loaders/web_loaders/soniox.md)                                      | <span data-sort-value="27"><a href="https://www.npmjs.com/package/@soniox/langchain" target="_blank">  <img src="https://img.shields.io/npm/dm/@soniox/langchain?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                            |
| [`DirectoryLoader`](document_loaders/file_loaders/directory.md)                         | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                              |
| [`JSON files`](document_loaders/file_loaders/json.md)                                   | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                              |
| [`Jsonlines files -`](document_loaders/file_loaders/jsonlines.md)                       | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                              |
| [`LangSmithLoader`](document_loaders/web_loaders/langsmith.md)                          | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                              |
| [`Multiple individual files -`](document_loaders/file_loaders/multi_file.md)            | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                              |
| [`OracleDocLoader`](document_loaders/file_loaders/oracleai.md)                          | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                              |
| [`TextLoader`](document_loaders/file_loaders/text.md)                                   | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                              |

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/document_loaders/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
