---
title: "Google integrations"
description: "Integrate with Google using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/google"
category: "docs"
tags: [docs, integrations, providers, google]
---

# Google integrations

> Integrate with Google using LangChain Python.

This page covers all LangChain integrations with [Google Gemini](https://ai.google.dev/gemini-api/docs), [Google Cloud](https://cloud.google.com/), and other Google products (such as Google Maps, YouTube, and [more](#other-google-products)).

> [!NOTE]
> **Unified SDK & package consolidation**
>
> As of `langchain-google-genai` 4.0.0, this package uses the consolidated [`google-genai`](https://googleapis.github.io/python-genai/) SDK and now supports **both the Gemini Developer API and Gemini Enterprise Agent Platform** backends.
>
> The `langchain-google-vertexai` package remains supported for Gemini Enterprise Agent Platform-specific features (Model Garden, Vector Search, evaluation services, etc.).
>
> Read the [full announcement and migration guide](https://github.com/langchain-ai/langchain-google/discussions/1422).

Not sure which package to use?

<details>
<summary>Google Generative AI (Gemini API & Gemini Enterprise Agent Platform)</summary>

Access Google Gemini models via the **[Gemini Developer API](https://ai.google.dev/)** or **[Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)**. The backend is selected automatically based on your configuration.

* **Gemini Developer API**: Quick setup with API key, ideal for individual developers and rapid prototyping
* **Gemini Enterprise Agent Platform**: Enterprise features with Google Cloud integration (requires GCP project)

Use the `langchain-google-genai` package for chat models, LLMs, and embeddings.

[See integrations.](#google-generative-ai)

</details>

<details>
<summary>Google Cloud (Gemini Enterprise Agent Platform Services)</summary>

Access Gemini Enterprise Agent Platform-specific services beyond Gemini models: Model Garden (Llama, Mistral, Anthropic), evaluation services, and specialized vision models.

Use the `langchain-google-vertexai` package for platform services and specific packages (e.g., `langchain-google-community`, `langchain-google-cloud-sql-pg`) for other cloud services like databases and storage.

[See integrations.](#google-cloud)

</details>

See Google's guide on [migrating from the Gemini API to Gemini Enterprise Agent Platform](https://ai.google.dev/gemini-api/docs/migrate-to-cloud) for more details on the differences.

***

## Google Generative AI

Access Google Gemini models via the [Gemini Developer API](https://ai.google.dev/gemini-api/docs) or [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) using the unified `langchain-google-genai` package.

### Chat models

#### [ChatGoogleGenerativeAI](../chat/google_generative_ai.md)
Google Gemini chat models via **Gemini Developer API** or **Gemini Enterprise Agent Platform**.

### LLMs

#### [GoogleGenerativeAI](../llms/google_generative_ai.md)
Gemini models using the (legacy) LLM text completion interface.

### Embedding models

#### [GoogleGenerativeAIEmbeddings](../embeddings/google_generative_ai.md)
Gemini embedding models via **Gemini Developer API** or **Gemini Enterprise Agent Platform**.

***

## Google Cloud

Access Gemini Enterprise Agent Platform-specific services including Model Garden (Llama, Mistral, Anthropic), Vector Search, evaluation services, and specialized vision models.

> [!NOTE]
> **For Gemini models**, use [`ChatGoogleGenerativeAI`](../chat/google_generative_ai.md) from `langchain-google-genai`. The classes below focus on **Gemini Enterprise Agent Platform services** not available in the consolidated SDK.

### Chat models

#### [ChatAnthropicVertex](../chat/google_anthropic_vertex.md)
Anthropic on Gemini Enterprise Agent Platform Model Garden

<details>
<summary>ChatVertexAI (deprecated)</summary>

**Deprecated**—Use [`ChatGoogleGenerativeAI`](../chat/google_generative_ai.md) for Gemini models instead.

```python
from langchain_google_vertexai import ChatVertexAI
```

</details>

<details>
<summary>VertexModelGardenLlama</summary>

Llama on Gemini Enterprise Agent Platform Model Garden

```python
from langchain_google_vertexai.model_garden_maas.llama import VertexModelGardenLlama
```

</details>

<details>
<summary>VertexModelGardenMistral</summary>

Mistral on Gemini Enterprise Agent Platform Model Garden

```python
from langchain_google_vertexai.model_garden_maas.mistral import VertexModelGardenMistral
```

</details>

<details>
<summary>GemmaChatLocalHF</summary>

Local Gemma model loaded from HuggingFace.

```python
from langchain_google_vertexai.gemma import GemmaChatLocalHF
```

</details>

<details>
<summary>GemmaChatLocalKaggle</summary>

Local Gemma model loaded from Kaggle.

```python
from langchain_google_vertexai.gemma import GemmaChatLocalKaggle
```

</details>

<details>
<summary>GemmaChatVertexAIModelGarden</summary>

Gemma on Gemini Enterprise Agent Platform Model Garden

```python
from langchain_google_vertexai.gemma import GemmaChatVertexAIModelGarden
```

</details>

<details>
<summary>VertexAIImageCaptioningChat</summary>

Image captioning model as a chat interface.

```python
from langchain_google_vertexai.vision_models import VertexAIImageCaptioningChat
```

</details>

<details>
<summary>VertexAIImageEditorChat</summary>

Edit images given a prompt. Currently supports mask-free editing only.

```python
from langchain_google_vertexai.vision_models import VertexAIImageEditorChat
```

</details>

<details>
<summary>VertexAIImageGeneratorChat</summary>

Generate images from a prompt.

```python
from langchain_google_vertexai.vision_models import VertexAIImageGeneratorChat
```

</details>

<details>
<summary>VertexAIVisualQnAChat</summary>

Visual question answering model as a chat interface.

```python
from langchain_google_vertexai.vision_models import VertexAIVisualQnAChat
```

</details>

### LLMs

(Legacy) string-in, string-out LLM interface.

#### [VertexAIModelGarden](../llms/google_vertex_ai.md#vertex-model-garden)
Hundreds of OSS models via Gemini Enterprise Agent Platform Model Garden.

<details>
<summary>VertexAI (deprecated)</summary>

**Deprecated**—Use [`GoogleGenerativeAI`](../llms/google_generative_ai.md) for Gemini models instead.

```python
from langchain_google_vertexai import VertexAI
```

</details>

<details>
<summary>Gemma local from Hugging Face</summary>

Local Gemma model loaded from HuggingFace.

```python
from langchain_google_vertexai.gemma import GemmaLocalHF
```

</details>

<details>
<summary>Gemma local from Kaggle</summary>

Local Gemma model loaded from Kaggle.

```python
from langchain_google_vertexai.gemma import GemmaLocalKaggle
```

</details>

<details>
<summary>Gemma on Gemini Enterprise Agent Platform Model Garden</summary>

```python
from langchain_google_vertexai.gemma import GemmaVertexAIModelGarden
```

</details>

<details>
<summary>Gemini Enterprise Agent Platform image captioning</summary>

Image captioning model as an LLM interface.

```python
from langchain_google_vertexai.vision_models import VertexAIImageCaptioning
```

</details>

### Embedding models

<details>
<summary>VertexAIEmbeddings (deprecated)</summary>

**Deprecated**—Use [`GoogleGenerativeAIEmbeddings`](../embeddings/google_generative_ai.md) instead.

```python
from langchain_google_vertexai import VertexAIEmbeddings
```

</details>

### Document loaders

#### [AlloyDB for PostgreSQL](../document_loaders/google_alloydb.md)
PostgreSQL-compatible database on Google Cloud.

#### [BigQuery](../document_loaders/google_bigquery.md)
Serverless data warehouse.

#### [Bigtable](../document_loaders/google_bigtable.md)
Key-value and wide-column store for structured and semi-structured data.

#### [Cloud SQL for MySQL](../document_loaders/google_cloud_sql_mysql.md)
Managed MySQL database.

#### [Cloud SQL for SQL Server](../document_loaders/google_cloud_sql_mssql.md)
Managed SQL Server database.

#### [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres)
Managed PostgreSQL database.

#### [Cloud Storage (directory)](../document_loaders/google_cloud_storage_directory.md)
Load documents from a GCS bucket directory.

#### [Cloud Storage (file)](../document_loaders/google_cloud_storage_file.md)
Load a single document from GCS.

#### [El Carro for Oracle Workloads](https://github.com/googleapis/langchain-google-el-carro-python/)
Oracle databases on Kubernetes via El Carro.

#### [Firestore (Native Mode)](../document_loaders/google_firestore.md)
NoSQL document database.

#### [Firestore (Datastore Mode)](../document_loaders/google_datastore.md)
Firestore in Datastore mode.

#### [Memorystore for Redis](../document_loaders/google_memorystore_redis.md)
Managed Redis service.

#### [Spanner](../document_loaders/google_spanner.md)
Globally distributed relational database.

#### [Speech-to-Text](../document_loaders/google_speech_to_text.md)
Transcribe audio files.

<details>
<summary>Cloud Vision loader</summary>

Load data using Google Cloud Vision API.

```python
from langchain_google_community.vision import CloudVisionLoader
```

</details>

### Document transformers

#### [Document AI](../document_transformers/google_docai.md)
Extract structured data from unstructured documents.

#### [Google Translate](../document_transformers/google_translate.md)
Translate text and HTML via Cloud Translation API.

### Vector stores

Store and search vectors using Google Cloud databases and Vector Search on Gemini Enterprise Agent Platform.

#### [AlloyDB for PostgreSQL](../vectorstores/google_alloydb.md)
PostgreSQL-compatible vector store on AlloyDB.

#### [BigQuery Vector Search](../vectorstores/google_bigquery_vector_search.md)
Semantic search using GoogleSQL with vector indexes.

#### [Memorystore for Redis](../vectorstores/google_memorystore_redis.md)
Vector store on Memorystore for Redis.

#### [Spanner](../vectorstores/google_spanner.md)
Vector store on Cloud Spanner.

#### [Bigtable](https://cloud.google.com/bigtable)
Vector store on Cloud Bigtable.

#### [Firestore (Native Mode)](../vectorstores/google_firestore.md)
Vector store on Firestore.

#### [Cloud SQL for MySQL](../vectorstores/google_cloud_sql_mysql.md)
Vector store on Cloud SQL for MySQL.

#### [Cloud SQL for PostgreSQL](../vectorstores/google_cloud_sql_pg.md)
Vector store on Cloud SQL for PostgreSQL.

#### [Vector Search on Gemini Enterprise Agent Platform](../vectorstores/google_vertex_ai_vector_search.md)
Formerly known as Vertex AI Matching Engine, provides a low latency vector database. These vector databases are commonly referred to as vector similarity-matching or an approximate nearest neighbor (ANN) service.

#### [Vector Search on Gemini Enterprise Agent Platform + Datastore](../vectorstores/google_vertex_ai_vector_search.md#optional--you-can-also-create-vector-and-store-chunks-in-a-datastore)
Vector search with Datastore for document storage.

### Retrievers

#### [Agent Search on Gemini Enterprise Agent Platform](../retrievers/google_vertex_ai_search.md)
Generative AI powered search via Agent Search on Gemini Enterprise Agent Platform.

#### [Document AI Warehouse](https://cloud.google.com/document-ai-warehouse)
Search, store, and manage documents using Document AI Warehouse.

**Other retrievers**

```python
from langchain_google_community import VertexAIMultiTurnSearchRetriever
from langchain_google_community import VertexAISearchRetriever
from langchain_google_community import VertexAISearchSummaryTool
```

### Tools

Integrate agents with various Google Cloud services.

#### [Text-to-Speech](../tools/google_cloud_texttospeech.md)
Synthesize natural-sounding speech with 100+ voices.

### Callbacks

Track LLM/Chat model usage.

<details>
<summary>Gemini Enterprise Agent Platform callback handler</summary>

Track `VertexAI` usage info.

```python
from langchain_google_vertexai.callbacks import VertexAICallbackHandler
```

</details>

<details>
<summary>Google BigQuery</summary>

See the [documentation](../callbacks/google_bigquery.md) for more details.

```python
from langchain_google_community.callbacks.bigquery_callback import BigQueryCallbackHandler
```

</details>

### Evaluators

Evaluate model outputs using Gemini Enterprise Agent Platform.

<details>
<summary>VertexPairWiseStringEvaluator</summary>

Pair-wise evaluation using Gemini Enterprise Agent Platform models.

```python
from langchain_google_vertexai.evaluators.evaluation import VertexPairWiseStringEvaluator
```

</details>

<details>
<summary>VertexStringEvaluator</summary>

Single prediction evaluation using Gemini Enterprise Agent Platform models.

```python
from langchain_google_vertexai.evaluators.evaluation import VertexStringEvaluator
```

</details>

***

## Other Google products

Integrations with various Google services beyond the core Cloud Platform.

### Document loaders

#### [Google Drive](../document_loaders/google_drive.md)
Load files from Google Drive. Currently supports Google Docs.

### Retrievers

#### [Google Drive](../retrievers/google_drive.md)
Retrieve documents from Google Drive.

### Tools

#### [Google Search](../tools/google_search.md)
Web search via Google Custom Search Engine (CSE).

#### [Google Drive](../tools/google_drive.md)
Interact with Google Drive.

### MCP

#### [MCP Toolbox](../tools/mcp_toolbox.md)
Connect to databases including Cloud SQL and AlloyDB.

### Toolkits

#### [Gmail](../tools/google_gmail.md)
Create, search, and send emails via the Gmail API.

***

## 3rd party integrations

Access Google services via unofficial third-party APIs.

### Search

#### [cloro](https://cloro.dev/docs)
Google Search results with AI Overview support.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/google.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
