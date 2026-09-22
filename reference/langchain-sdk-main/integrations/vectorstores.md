---
title: "Vector store integrations"
description: "Integrate with vector stores using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/vectorstores"
category: "docs"
tags: [docs, integrations, vectorstores]
---

# Vector store integrations

> Integrate with vector stores using LangChain Python.

## Overview

A vector stores [embedded](embeddings.md) data and performs similarity search.

```mermaid
flowchart LR

    subgraph "📥 Indexing phase (store)"
        A[📄 Documents] --> B[🔢 Embedding model]
        B --> C[🔘 Embedding vectors]
        C --> D[(Vector store)]
    end

    subgraph "📤 Query phase (retrieval)"
        E[❓ Query text] --> F[🔢 Embedding model]
        F --> G[🔘 Query vector]
        G --> H[🔍 Similarity search]
        H --> D
        D --> I[📄 Top-k results]
    end

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    class A,B,C,D,E,F,G,H,I process
```

<a id="cockroachdb"></a>

### Interface

LangChain provides a unified interface for vector stores, allowing you to:

* `add_documents` - Add documents to the store.
* `delete` - Remove stored documents by ID.
* `similarity_search` - Query for semantically similar documents.

This abstraction lets you switch between different implementations without altering your application logic.

### Initialization

To initialize a vector store, provide it with an embedding model:

```python
from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embedding=SomeEmbeddingModel())
```

### Adding documents

Add [`Document`](https://reference.langchain.com/python/langchain-core/documents/base/Document) objects (holding `page_content` and optional metadata) like so:

```python
vector_store.add_documents(documents=[doc1, doc2], ids=["id1", "id2"])
```

### Deleting documents

Delete by specifying IDs:

```python
vector_store.delete(ids=["id1"])
```

### Similarity search

Issue a semantic query using `similarity_search`, which returns the closest embedded documents:

```python
similar_docs = vector_store.similarity_search("your query here")
```

Many vector stores support parameters like:

* `k` — number of results to return
* `filter` — conditional filtering based on metadata

### Similarity metrics & indexing

Embedding similarity may be computed using:

* **Cosine similarity**
* **Euclidean distance**
* **Dot product**

Efficient search often employs indexing methods such as HNSW (Hierarchical Navigable Small World), though specifics depend on the vector store.

### Metadata filtering

Filtering by metadata (e.g., source, date) can refine search results:

```python
vector_store.similarity_search(
  "query",
  k=3,
  filter={"source": "tweets"}
)
```

> [!IMPORTANT]
>   Support for metadata-based filtering varies between implementations.
>   Check the documentation of your chosen vector store for details.

## Top integrations

**Select embedding model:**

<details>
<summary>OpenAI</summary>

**pip**

```bash
pip install -qU langchain-openai
```

**uv**

```bash
uv add langchain-openai
```

```python
import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

</details>

<details>
<summary>Azure</summary>

```bash
pip install -qU langchain-azure-ai
```

```python
import getpass
import os

if not os.environ.get("AZURE_OPENAI_API_KEY"):
  os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass("Enter API key for Azure: ")

from langchain_openai import AzureOpenAIEmbeddings

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)
```

</details>

<details>
<summary>Google Gemini</summary>

```bash
pip install -qU langchain-google-genai
```

```python
import getpass
import os

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
```

</details>

<details>
<summary>Gemini Enterprise Agent Platform</summary>

```bash
pip install -qU langchain-google-vertexai
```

```python
from langchain_google_vertexai import VertexAIEmbeddings

embeddings = VertexAIEmbeddings(model="text-embedding-005")
```

</details>

<details>
<summary>AWS</summary>

```bash
pip install -qU langchain-aws
```

```python
from langchain_aws import BedrockEmbeddings

embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0")
```

</details>

<details>
<summary>HuggingFace</summary>

```bash
pip install -qU langchain-huggingface
```

```python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
```

</details>

<details>
<summary>Ollama</summary>

```bash
pip install -qU langchain-ollama
```

```python
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")
```

</details>

<details>
<summary>Cohere</summary>

```bash
pip install -qU langchain-cohere
```

```python
import getpass
import os

if not os.environ.get("COHERE_API_KEY"):
  os.environ["COHERE_API_KEY"] = getpass.getpass("Enter API key for Cohere: ")

from langchain_cohere import CohereEmbeddings

embeddings = CohereEmbeddings(model="embed-english-v3.0")
```

</details>

<details>
<summary>Mistral AI</summary>

```bash
pip install -qU langchain-mistralai
```

```python
import getpass
import os

if not os.environ.get("MISTRALAI_API_KEY"):
  os.environ["MISTRALAI_API_KEY"] = getpass.getpass("Enter API key for MistralAI: ")

from langchain_mistralai import MistralAIEmbeddings

embeddings = MistralAIEmbeddings(model="mistral-embed")
```

</details>

<details>
<summary>Nomic</summary>

```bash
pip install -qU langchain-nomic
```

```python
import getpass
import os

if not os.environ.get("NOMIC_API_KEY"):
  os.environ["NOMIC_API_KEY"] = getpass.getpass("Enter API key for Nomic: ")

from langchain_nomic import NomicEmbeddings

embeddings = NomicEmbeddings(model="nomic-embed-text-v1.5")
```

</details>

<details>
<summary>NVIDIA</summary>

```bash
pip install -qU langchain-nvidia-ai-endpoints
```

```python
import getpass
import os

if not os.environ.get("NVIDIA_API_KEY"):
  os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter API key for NVIDIA: ")

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

embeddings = NVIDIAEmbeddings(model="NV-Embed-QA")
```

</details>

<details>
<summary>Voyage AI</summary>

```bash
pip install -qU langchain-voyageai
```

```python
import getpass
import os

if not os.environ.get("VOYAGE_API_KEY"):
  os.environ["VOYAGE_API_KEY"] = getpass.getpass("Enter API key for Voyage AI: ")

from langchain_voyageai import VoyageAIEmbeddings

embeddings = VoyageAIEmbeddings(model="voyage-3")
```

For more information, see the [Voyage AI documentation](https://www.mongodb.com/docs/voyageai/models/text-embeddings/).

</details>

<details>
<summary>IBM watsonx</summary>

```bash
pip install -qU langchain-ibm
```

```python
import getpass
import os

if not os.environ.get("WATSONX_APIKEY"):
  os.environ["WATSONX_APIKEY"] = getpass.getpass("Enter API key for IBM watsonx: ")

from langchain_ibm import WatsonxEmbeddings

embeddings = WatsonxEmbeddings(
    model_id="ibm/slate-125m-english-rtrvr",
    url="https://us-south.ml.cloud.ibm.com",
    project_id="<WATSONX PROJECT_ID>",
)
```

</details>

<details>
<summary>Fake</summary>

```bash
pip install -qU langchain-core
```

```python
from langchain_core.embeddings import DeterministicFakeEmbedding

embeddings = DeterministicFakeEmbedding(size=4096)
```

</details>

<details>
<summary>xAI</summary>

```bash
pip install -qU langchain-xai
```

```python
import getpass
import os

if not os.environ.get("XAI_API_KEY"):
  os.environ["XAI_API_KEY"] = getpass.getpass("Enter API key for xAI: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("grok-2", model_provider="xai")
```

</details>

<details>
<summary>Perplexity</summary>

```bash
pip install -qU langchain-perplexity
```

```python
import getpass
import os

if not os.environ.get("PPLX_API_KEY"):
  os.environ["PPLX_API_KEY"] = getpass.getpass("Enter API key for Perplexity: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("llama-3.1-sonar-small-128k-online", model_provider="perplexity")
```

</details>

<details>
<summary>DeepSeek</summary>

```bash
pip install -qU langchain-deepseek
```

```python
import getpass
import os

if not os.environ.get("DEEPSEEK_API_KEY"):
  os.environ["DEEPSEEK_API_KEY"] = getpass.getpass("Enter API key for DeepSeek: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("deepseek-chat", model_provider="deepseek")
```

</details>

**Select vector store:**

<details>
<summary>In-memory</summary>

**pip**

```bash
pip install -qU langchain-core
```

**uv**

```bash
uv add langchain-core
```

```python
from langchain_core.vectorstores import InMemoryVectorStore

vector_store = InMemoryVectorStore(embeddings)
```

</details>

<details>
<summary>Amazon OpenSearch</summary>

**pip**

```bash
pip install -qU boto3
```

```python
from opensearchpy import RequestsHttpConnection

service = "es"  # must set the service as 'es'
region = "us-east-2"
credentials = boto3.Session(
    aws_access_key_id="xxxxxx", aws_secret_access_key="xxxxx"
).get_credentials()
awsauth = AWS4Auth("xxxxx", "xxxxxx", region, service, session_token=credentials.token)

vector_store = OpenSearchVectorSearch.from_documents(
    docs,
    embeddings,
    opensearch_url="host url",
    http_auth=awsauth,
    timeout=300,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
    index_name="test-index",
)
```

</details>

<details>
<summary>Astra DB</summary>

**pip**

```bash
pip install -qU langchain-astradb
```

**uv**

```bash
uv add langchain-astradb
```

```python
from langchain_astradb import AstraDBVectorStore

vector_store = AstraDBVectorStore(
    embedding=embeddings,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    collection_name="astra_vector_langchain",
    token=ASTRA_DB_APPLICATION_TOKEN,
    namespace=ASTRA_DB_NAMESPACE,
)
```

</details>

<details>
<summary>Azure Cosmos DB NoSQL</summary>

**pip**

```bash
pip install -qU langchain-azure-cosmosdb azure-cosmos
```

**uv**

```bash
uv add langchain-azure-cosmosdb azure-cosmos
```

```python
from langchain_azure_cosmosdb import AzureCosmosDBNoSqlVectorSearch

vector_search = AzureCosmosDBNoSqlVectorSearch.from_documents(
    documents=docs,
    embedding=openai_embeddings,
    cosmos_client=cosmos_client,
    database_name=database_name,
    container_name=container_name,
    vector_embedding_policy=vector_embedding_policy,
    full_text_policy=full_text_policy,
    indexing_policy=indexing_policy,
    cosmos_container_properties=cosmos_container_properties,
    cosmos_database_properties={},
    full_text_search_enabled=True,
)
```

</details>

<details>
<summary>Azure Cosmos DB Mongo vCore</summary>

**pip**

```bash
pip install -qU langchain-azure-ai pymongo
```

**uv**

```bash
uv add pymongo
```

```python
from langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore import (
    AzureCosmosDBMongoVCoreVectorSearch,
)

vectorstore = AzureCosmosDBMongoVCoreVectorSearch.from_documents(
    docs,
    openai_embeddings,
    collection=collection,
    index_name=INDEX_NAME,
)
```

</details>

<details>
<summary>Chroma</summary>

**pip**

```bash
pip install -qU langchain-chroma
```

**uv**

```bash
uv add langchain-chroma
```

```python
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)
```

</details>

<details>
<summary>CockroachDB</summary>

**pip**

```bash
pip install -qU langchain-cockroachdb
```

**uv**

```bash
uv add langchain-cockroachdb
```

```python
from langchain_cockroachdb import AsyncCockroachDBVectorStore, CockroachDBEngine

CONNECTION_STRING = "cockroachdb://user:pass@host:26257/db?sslmode=verify-full"

engine = CockroachDBEngine.from_connection_string(CONNECTION_STRING)
await engine.ainit_vectorstore_table(
    table_name="vectors",
    vector_dimension=1536,
)

vector_store = AsyncCockroachDBVectorStore(
    engine=engine,
    embeddings=embeddings,
    collection_name="vectors",
)
```

</details>

<details>
<summary>Elasticsearch</summary>

Install the package and start Elasticsearch locally using the [start-local](https://github.com/elastic/start-local) script:

```bash
pip install -qU langchain-elasticsearch
curl -fsSL https://elastic.co/start-local | sh
```

This creates an `elastic-start-local` folder. To start Elasticsearch:

```bash
cd elastic-start-local
./start.sh
```

Elasticsearch will be available at `http://localhost:9200`. The password for the `elastic` user and API key are stored in the `.env` file in the `elastic-start-local` folder.

```python
from langchain_elasticsearch import ElasticsearchStore

vector_store = ElasticsearchStore(
    index_name="langchain-demo",
    embedding=embeddings,
    es_url="http://localhost:9200",
)
```

</details>

<details>
<summary>Google AlloyDB</summary>

**pip**

```bash
pip install -qU langchain-google-alloydb-pg
```

**uv**

```bash
uv add langchain-google-alloydb-pg
```

```python
from langchain_google_alloydb_pg import AlloyDBEngine, AlloyDBVectorStore

engine = AlloyDBEngine.from_instance(
    project_id="my-project",
    region="us-central1",
    cluster="my-cluster",
    instance="my-instance",
    database="my-database",
)

vector_store = AlloyDBVectorStore.create_sync(
    engine=engine,
    table_name="my_vectors",
    embedding_service=embeddings
)
```

</details>

<details>
<summary>Milvus</summary>

**pip**

```bash
pip install -qU langchain-milvus
```

**uv**

```bash
uv add langchain-milvus
```

```python
from langchain_milvus import Milvus

URI = "./milvus_example.db"

vector_store = Milvus(
    embedding_function=embeddings,
    connection_args={"uri": URI},
    index_params={"index_type": "FLAT", "metric_type": "L2"},
)
```

</details>

<details>
<summary>MongoDB</summary>

```bash
pip install -qU langchain-mongodb
```

```python
from langchain_mongodb import MongoDBAtlasVectorSearch

vector_store = MongoDBAtlasVectorSearch(
    embedding=embeddings,
    collection=MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)
```

For more information, see the [MongoDB LangChain integration docs](https://www.mongodb.com/docs/atlas/ai-integrations/langchain/#vector-store).

</details>

<details>
<summary>PGVector</summary>

**pip**

```bash
pip install -qU langchain-postgres
```

**uv**

```bash
uv add langchain-postgres
```

```python
from langchain_postgres import PGVector

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection="postgresql+psycopg://..."
)
```

</details>

<details>
<summary>PGVectorStore</summary>

**pip**

```bash
pip install -qU langchain-postgres
```

**uv**

```bash
uv add langchain-postgres
```

```python
from langchain_postgres import PGEngine, PGVectorStore

pg_engine = PGEngine.from_connection_string(
    url="postgresql+psycopg://..."
)

vector_store = PGVectorStore.create_sync(
    engine=pg_engine,
    table_name='test_table',
    embedding_service=embedding
)
```

</details>

<details>
<summary>Pinecone</summary>

**pip**

```bash
pip install -qU langchain-pinecone
```

**uv**

```bash
uv add langchain-pinecone
```

```python
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

pc = Pinecone(api_key=...)
index = pc.Index(index_name)

vector_store = PineconeVectorStore(embedding=embeddings, index=index)
```

</details>

<details>
<summary>Qdrant</summary>

**pip**

```bash
pip install -qU langchain-qdrant
```

**uv**

```bash
uv add langchain-qdrant
```

```python
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

client = QdrantClient(":memory:")

vector_size = len(embeddings.embed_query("sample text"))

if not client.collection_exists("test"):
    client.create_collection(
        collection_name="test",
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
vector_store = QdrantVectorStore(
    client=client,
    collection_name="test",
    embedding=embeddings,
)
```

</details>

<details>
<summary>Redis</summary>

**pip**

```bash
pip install -qU langchain-redis
```

**uv**

```bash
uv add langchain-redis
```

```python
import os
from langchain_redis import RedisConfig, RedisVectorStore

config = RedisConfig(
    index_name="my_vectors",
    redis_url=os.getenv("REDIS_URL", "redis://localhost:6379"),
    distance_metric="COSINE"
)

vector_store = RedisVectorStore(embeddings=embeddings, config=config)
```

</details>

<details>
<summary>Oracle AI Database</summary>

**pip**

```bash
pip install -qU langchain-oracledb
```

**uv**

```bash
uv add langchain-oracledb
```

> [!WARNING]
> The `langchain-community` package is no longer maintained. Examples that import from `langchain_community` may be outdated or broken. Use with caution.

```python
import oracledb
from langchain_oracledb.vectorstores import OracleVS
from langchain_oracledb.vectorstores.oraclevs import create_index
from langchain_community.vectorstores.utils import DistanceStrategy

username = "<username>"
password = "<password>"
dsn = "<hostname>:<port>/<service_name>"

connection = oracledb.connect(user=username, password=password, dsn=dsn)

vector_store = OracleVS(
    client=connection,
    embedding_function=embedding_model,
    table_name="VECTOR_SEARCH_DEMO",
    distance_strategy=DistanceStrategy.EUCLIDEAN_DISTANCE
)
```

</details>

<details>
<summary>turbopuffer</summary>

**pip**

```bash
pip install -qU langchain-turbopuffer
```

**uv**

```bash
uv add langchain-turbopuffer
```

```python
from langchain_turbopuffer import TurbopufferVectorStore
from turbopuffer import Turbopuffer

tpuf = Turbopuffer(region="gcp-us-central1")
ns = tpuf.namespace("langchain-test")

vector_store = TurbopufferVectorStore(embedding=embeddings, namespace=ns)
```

</details>

<details>
<summary>Valkey</summary>

**pip**

```bash
pip install -qU "langchain-aws[valkey]"
```

**uv**

```bash
uv add langchain-aws --extra valkey
```

```python
from langchain_aws.vectorstores import ValkeyVectorStore

vector_store = ValkeyVectorStore(
    embedding=embeddings,
    valkey_url="valkey://localhost:6379",
    index_name="my_index"
)
```

</details>

<details>
<summary>Weaviate</summary>

**pip**

```bash
pip install -qU langchain-weaviate
```

**uv**

```bash
uv add langchain-weaviate
```

```python
import weaviate
from langchain_weaviate import WeaviateVectorStore

# Assumes a local Weaviate instance on http://localhost:8080 with gRPC on 50051.
# See the Weaviate guide for other deployment options (Weaviate Cloud, Docker, etc.).
weaviate_client = weaviate.connect_to_local()

vector_store = WeaviateVectorStore(
    client=weaviate_client,
    index_name="langchain_example",
    text_key="text",
    embedding=embeddings,
)
```

</details>

| Vectorstore                                                                                               | Delete by ID                       | Filtering                          | Search by Vector                   | Search with score                  | Async                              | Passes Standard Tests              | Multi Tenancy                      | IDs in add Documents               | Downloads                                                                                                                                                                                                                                                            |
| :-------------------------------------------------------------------------------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ValkeyVectorStore`](vectorstores/valkey.md)                                       | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="11000000"><a href="https://pypi.org/project/langchain-aws/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-aws/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                          |
| [`DatabricksVectorSearch`](vectorstores/databricks_vector_search.md)                | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2000000"><a href="https://pypi.org/project/databricks-langchain/" target="_blank">  <img src="https://static.pepy.tech/badge/databricks-langchain/month" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`AzureCosmosDBMongoVCoreVectorStore`](vectorstores/azure_cosmos_db_mongo_vcore.md) | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="951000"><a href="https://pypi.org/project/langchain-azure-ai/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-azure-ai/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`MongoDBAtlasVectorSearch`](vectorstores/mongodb_atlas.md)                         | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="818000"><a href="https://pypi.org/project/langchain-mongodb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-mongodb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`QdrantVectorStore`](vectorstores/qdrant.md)                                       | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="765000"><a href="https://pypi.org/project/langchain-qdrant/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-qdrant/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                      |
| [`PineconeVectorStore`](vectorstores/pinecone.md)                                   | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="744000"><a href="https://pypi.org/project/langchain-pinecone/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-pinecone/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`Milvus`](vectorstores/milvus.md)                                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="455000"><a href="https://pypi.org/project/langchain-milvus/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-milvus/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                      |
| [`Oracle AI Database`](vectorstores/oracle.md)                                      | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="225000"><a href="https://pypi.org/project/langchain-oracledb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-oracledb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`ElasticsearchStore`](vectorstores/elasticsearch.md)                               | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="215000"><a href="https://pypi.org/project/langchain-elasticsearch/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-elasticsearch/month" alt="Downloads per month" class="rounded not-prose" /></a></span>        |
| [`Weaviate`](vectorstores/weaviate.md)                                              | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="203000"><a href="https://pypi.org/project/langchain-weaviate/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-weaviate/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`AstraDBVectorStore`](vectorstores/astradb.md)                                     | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="178000"><a href="https://pypi.org/project/langchain-astradb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-astradb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`RedisVectorStore`](vectorstores/redis.md)                                         | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="89000"><a href="https://pypi.org/project/langchain-redis/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-redis/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                         |
| [`AzureCosmosDBNoSqlVectorStore`](vectorstores/azure_cosmos_db_no_sql.md)           | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="67000"><a href="https://pypi.org/project/langchain-azure-cosmosdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-azure-cosmosdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>       |
| [`Google AlloyDB`](vectorstores/google_alloydb.md)                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="34000"><a href="https://pypi.org/project/langchain-google-alloydb-pg/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-alloydb-pg/month" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`InMemoryVectorStore`](vectorstores/in_memory.md)                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                |

## All vector stores

| Vectorstore                                                                                                                                 | Delete by ID                       | Filtering                          | Search by Vector                   | Search with score                  | Async                              | Passes Standard Tests              | Multi Tenancy                      | IDs in add Documents               | Downloads                                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Feature Store on Gemini Enterprise Agent Platform`](vectorstores/google_vertex_ai_feature_store.md)                 | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="32000000"><a href="https://pypi.org/project/langchain-google-vertexai/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-vertexai/month" alt="Downloads per month" class="rounded not-prose" /></a></span>              |
| [`Google bigquery vector search`](vectorstores/google_bigquery_vector_search.md)                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="32000000"><a href="https://pypi.org/project/langchain-google-vertexai/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-vertexai/month" alt="Downloads per month" class="rounded not-prose" /></a></span>              |
| [`Vector Search on Gemini Enterprise Agent Platform`](vectorstores/google_vertex_ai_vector_search.md)                 | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="32000000"><a href="https://pypi.org/project/langchain-google-vertexai/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-vertexai/month" alt="Downloads per month" class="rounded not-prose" /></a></span>              |
| [`Amazon memorydb`](vectorstores/memorydb.md)                                                                         | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="11000000"><a href="https://pypi.org/project/langchain-aws/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-aws/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                      |
| [`ValkeyVectorStore`](vectorstores/valkey.md)                                                                         | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="11000000"><a href="https://pypi.org/project/langchain-aws/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-aws/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                      |
| [`DatabricksVectorSearch`](vectorstores/databricks_vector_search.md)                                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2000000"><a href="https://pypi.org/project/databricks-langchain/" target="_blank">  <img src="https://static.pepy.tech/badge/databricks-langchain/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                         |
| [`Chroma`](vectorstores/chroma.md)                                                                                    | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="1000000"><a href="https://pypi.org/project/langchain-chroma/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-chroma/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`PGVector`](vectorstores/pgvector.md)                                                                                | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="1000000"><a href="https://pypi.org/project/langchain-postgres/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-postgres/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                             |
| [`PGVectorStore`](vectorstores/pgvectorstore.md)                                                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="1000000"><a href="https://pypi.org/project/langchain-postgres/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-postgres/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                             |
| [`AzureCosmosDBMongoVCoreVectorStore`](vectorstores/azure_cosmos_db_mongo_vcore.md)                                   | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="951000"><a href="https://pypi.org/project/langchain-azure-ai/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-azure-ai/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                              |
| [`MongoDBAtlasVectorSearch`](vectorstores/mongodb_atlas.md)                                                           | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="818000"><a href="https://pypi.org/project/langchain-mongodb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-mongodb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                |
| [`QdrantVectorStore`](vectorstores/qdrant.md)                                                                         | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="765000"><a href="https://pypi.org/project/langchain-qdrant/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-qdrant/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                  |
| [`Pinecone (Sparse)`](vectorstores/pinecone_sparse.md)                                                                | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="744000"><a href="https://pypi.org/project/langchain-pinecone/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-pinecone/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                              |
| [`PineconeVectorStore`](vectorstores/pinecone.md)                                                                     | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="744000"><a href="https://pypi.org/project/langchain-pinecone/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-pinecone/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                              |
| [`Milvus`](vectorstores/milvus.md)                                                                                    | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="455000"><a href="https://pypi.org/project/langchain-milvus/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-milvus/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                  |
| [`Oracle AI Database`](vectorstores/oracle.md)                                                                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="225000"><a href="https://pypi.org/project/langchain-oracledb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-oracledb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                              |
| [`ElasticsearchStore`](vectorstores/elasticsearch.md)                                                                 | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="215000"><a href="https://pypi.org/project/langchain-elasticsearch/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-elasticsearch/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`Weaviate`](vectorstores/weaviate.md)                                                                                | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="203000"><a href="https://pypi.org/project/langchain-weaviate/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-weaviate/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                              |
| [`AstraDBVectorStore`](vectorstores/astradb.md)                                                                       | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="178000"><a href="https://pypi.org/project/langchain-astradb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-astradb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                |
| [`Neo4j vector index`](vectorstores/neo4jvector.md)                                                                   | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="171000"><a href="https://pypi.org/project/langchain-neo4j/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-neo4j/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                    |
| [`RedisVectorStore`](vectorstores/redis.md)                                                                           | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="89000"><a href="https://pypi.org/project/langchain-redis/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-redis/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                     |
| [`AzureCosmosDBNoSqlVectorStore`](vectorstores/azure_cosmos_db_no_sql.md)                                             | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="67000"><a href="https://pypi.org/project/langchain-azure-cosmosdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-azure-cosmosdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                   |
| [`Google AlloyDB`](vectorstores/google_alloydb.md)                                                                    | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="34000"><a href="https://pypi.org/project/langchain-google-alloydb-pg/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-alloydb-pg/month" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`Google firestore`](vectorstores/google_firestore.md)                                                                | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="29000"><a href="https://pypi.org/project/langchain-google-firestore/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-firestore/month" alt="Downloads per month" class="rounded not-prose" /></a></span>               |
| [`Sap hana cloud vector engine`](vectorstores/sap_hanavector.md)                                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="27000"><a href="https://pypi.org/project/langchain-hana/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-hana/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                       |
| [`Google spanner`](vectorstores/google_spanner.md)                                                                    | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="24000"><a href="https://pypi.org/project/langchain-google-spanner/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-spanner/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                   |
| [`Google cloud SQL for postgresql`](vectorstores/google_cloud_sql_pg.md)                                              | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="22000"><a href="https://pypi.org/project/langchain-google-cloud-sql-pg/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-cloud-sql-pg/month" alt="Downloads per month" class="rounded not-prose" /></a></span>         |
| [`OpensolrVectorStore`](https://opensolr.com/langchain)                                                                                     | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="6000"><a href="https://pypi.org/project/langchain-opensolr/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-opensolr/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                |
| [`OceanbaseVectorStore`](https://pypi.org/project/langchain-oceanbase/)                                                                     | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="5000"><a href="https://pypi.org/project/langchain-oceanbase/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-oceanbase/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                              |
| [`IBM db2 vector store and vector search`](https://github.com/langchain-ai/langchain-ibm/tree/main/libs/langchain-db2)                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="3000"><a href="https://pypi.org/project/langchain-db2/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-db2/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                          |
| [`PolarDBXVectorStore`](https://github.com/polardb/langchain-polardbx)                                                                      | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="3000"><a href="https://pypi.org/project/langchain-polardbx/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-polardbx/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                |
| [`AsyncCockroachDBVectorStore`](https://github.com/cockroachdb/langchain-cockroachdb/)                                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="2000"><a href="https://pypi.org/project/langchain-cockroachdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-cockroachdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                          |
| [`InfinoVectorStore`](https://infino.ai/docs)                                                                                               | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2000"><a href="https://pypi.org/project/langchain-infino/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-infino/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                    |
| [`CouchbaseSearchVectorStore`](https://docs.couchbase.com/server/current/vector-search/vector-search.html)                                  | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="1000"><a href="https://pypi.org/project/langchain-couchbase/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-couchbase/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                              |
| [`SingleStoreVectorStore`](https://docs.singlestore.com/cloud/developer-resources/functional-extensions/working-with-vector-data/)          | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="1000"><a href="https://pypi.org/project/langchain-singlestore/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-singlestore/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                          |
| [`TeradataVectorStore`](https://github.com/Teradata/langchain-teradata)                                                                     | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="1000"><a href="https://pypi.org/project/langchain-teradata/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-teradata/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                |
| [`PolarDBPGVector`](https://github.com/polardb/langchain-polardb-pg)                                                                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="968"><a href="https://pypi.org/project/langchain-polardb-pg/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-polardb-pg/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                             |
| [`SurrealDBVectorStore`](https://surrealdb.com/docs/build/deployment/surrealdb-cloud/getting-started)                                       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="758"><a href="https://pypi.org/project/langchain-surrealdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-surrealdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                               |
| [`SQLServer`](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql) | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="699"><a href="https://pypi.org/project/langchain-sqlserver/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-sqlserver/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                               |
| [`YDB`](https://ydb.tech/)                                                                                                                  | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="694"><a href="https://pypi.org/project/langchain-ydb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-ydb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                           |
| [`Mariadb`](https://mariadb.com/docs/connectors/other/langchain-mariadb/api-reference)                                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="627"><a href="https://pypi.org/project/langchain-mariadb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-mariadb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                   |
| [`Intel's visual data management system (VDMS)`](https://github.com/IntelLabs/vdms)                                                         | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="624"><a href="https://pypi.org/project/langchain-vdms/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-vdms/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                         |
| [`ChronoVecVectorStore`](https://mchl-labs.github.io/chronovec/integrations/langchain)                                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="585"><a href="https://pypi.org/project/chronovec/" target="_blank">  <img src="https://static.pepy.tech/badge/chronovec/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                                   |
| [`Google memorystore for Redis`](vectorstores/google_memorystore_redis.md)                                            | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="552"><a href="https://pypi.org/project/langchain-google-memorystore-redis/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-memorystore-redis/month" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`ShannonBaseVectorStore`](https://github.com/apoorva-01/langchain-shannonbase)                                                             | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="519"><a href="https://pypi.org/project/langchain-shannonbase/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-shannonbase/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                           |
| [`TypesenseVectorStore`](https://github.com/typesense/langchain-typesense#readme)                                                           | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="519"><a href="https://pypi.org/project/langchain-typesense/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-typesense/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                               |
| [`YantrikDBVectorStore`](https://github.com/yantrikos/langchain-yantrikdb)                                                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="0" />       | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="497"><a href="https://pypi.org/project/langchain-yantrikdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-yantrikdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                               |
| [`FalkorDBVector`](https://docs.falkordb.com/genai-tools/langchain.html)                                                                    | <span data-sort-value="0" />       | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="496"><a href="https://pypi.org/project/langchain-falkordb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-falkordb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`BigtableVectorStore`](https://cloud.google.com/bigtable)                                                                                  | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="435"><a href="https://pypi.org/project/langchain-google-bigtable/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-bigtable/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                   |
| [`RostamVectorStore`](https://github.com/rostamlabs/rostam/tree/main/clients/langchain-rostam)                                              | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="420"><a href="https://pypi.org/project/langchain-rostam/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-rostam/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                     |
| [`VectorPandaStore`](https://www.vectorpanda.com/docs/tutorials/langchain)                                                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="10"><a href="https://pypi.org/project/langchain-vectorpanda/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-vectorpanda/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                            |
| [`MixpeekVectorStore`](https://mixpeek.com/docs/agent-integrations/langchain)                                                               | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="417"><a href="https://pypi.org/project/langchain-mixpeek/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-mixpeek/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                   |
| [`openGauss`](https://github.com/mpb159753/langchain-opengauss)                                                                             | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="410"><a href="https://pypi.org/project/langchain-opengauss/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-opengauss/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                               |
| [`VastDBVectorStore`](https://github.com/vast-data/vast-vector-store)                                                                       | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="408"><a href="https://pypi.org/project/langchain-vastdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-vastdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                     |
| [`SereneDB`](https://serenedb.com/docs/clients/langchain-serenedb)                                                                          | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="355"><a href="https://pypi.org/project/langchain-serenedb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-serenedb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`Azure database for postgresql - flexible server`](vectorstores/azure_db_for_postgresql.md)                          | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="293"><a href="https://pypi.org/project/langchain-azure-postgresql/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-azure-postgresql/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                 |
| [`turbopuffer`](vectorstores/turbopuffer.md)                                                                          | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="266"><a href="https://pypi.org/project/langchain-turbopuffer/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-turbopuffer/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                           |
| [`ZeusDB`](https://docs.zeusdb.com/en/latest/)                                                                                              | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="236"><a href="https://pypi.org/project/langchain-zeusdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-zeusdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                     |
| [`Kinetica vectorstore`](https://github.com/kineticadb/langchain-kinetica)                                                                  | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="231"><a href="https://pypi.org/project/langchain-kinetica/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-kinetica/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`Google cloud SQL for mysql`](vectorstores/google_cloud_sql_mysql.md)                                                | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="227"><a href="https://pypi.org/project/langchain-google-cloud-sql-mysql/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-cloud-sql-mysql/month" alt="Downloads per month" class="rounded not-prose" /></a></span>     |
| [`LambdaDB`](https://docs.lambdadb.ai/guides/get-started/quickstart)                                                                        | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="221"><a href="https://pypi.org/project/langchain-lambdadb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-lambdadb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`Vectara`](https://docs.vectara.com/)                                                                                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="214"><a href="https://pypi.org/project/langchain-vectara/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-vectara/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                   |
| [`PixeltableVectorStore`](https://docs.pixeltable.com/overview/pixeltable)                                                                  | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="213"><a href="https://pypi.org/project/langchain-pixeltable/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-pixeltable/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                             |
| [`Activeloop Deep lake`](https://docs.deeplake.ai/)                                                                                         | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="194"><a href="https://pypi.org/project/langchain-deeplake/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-deeplake/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`Gel`](https://github.com/geldata/langchain-gel)                                                                                           | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="189"><a href="https://pypi.org/project/langchain-gel/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-gel/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                           |
| [`Moorcheh`](https://www.moorcheh.ai/)                                                                                                      | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="189"><a href="https://pypi.org/project/langchain-moorcheh/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-moorcheh/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`ActianVectorAIVectorStore`](https://docs.vectoraidb.actian.com)                                                                           | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="178"><a href="https://pypi.org/project/langchain-actian-vectorai/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-actian-vectorai/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                   |
| [`Firebolt`](https://docs.firebolt.io/guides/integrations/langchain)                                                                        | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="176"><a href="https://pypi.org/project/langchain-firebolt/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-firebolt/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`DeweyVectorStore`](https://github.com/meetdewey/langchain-dewey)                                                                          | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="164"><a href="https://pypi.org/project/langchain-dewey/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-dewey/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                       |
| [`LindormVectorStore`](https://help.aliyun.com/en/lindorm/user-guide/enable-vector-engine)                                                  | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="139"><a href="https://pypi.org/project/langchain-lindorm-integration/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-lindorm-integration/month" alt="Downloads per month" class="rounded not-prose" /></a></span>           |
| [`Vedb for mysql`](https://docs.volcengine.com/docs/6357?lang=en)                                                                           | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="125"><a href="https://pypi.org/project/langchain-volcengine-mysql/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-volcengine-mysql/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                 |
| [`Volcengine rds for mysql`](https://docs.volcengine.com/docs/6313?lang=en)                                                                 | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="125"><a href="https://pypi.org/project/langchain-volcengine-mysql/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-volcengine-mysql/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                 |
| [`Alibaba cloud mysql`](https://github.com/wangkuahai/langchain-alibabacloud-mysql)                                                         | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="122"><a href="https://pypi.org/project/langchain-alibabacloud-mysql/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-alibabacloud-mysql/month" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`ChDBVectorStore`](https://github.com/chdb-io/langchain-chdb)                                                                              | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="122"><a href="https://pypi.org/project/langchain-chdb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-chdb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                         |
| [`CosVectors`](https://github.com/hushengquan/langchain-cos-vectors)                                                                        | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="116"><a href="https://pypi.org/project/langchain-cos-vectors/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-cos-vectors/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                           |
| [`FAISS`](https://github.com/facebookresearch/faiss)                                                                                        | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="0" />       | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                            |
| [`InMemoryVectorStore`](vectorstores/in_memory.md)                                                                    | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                            |
| [`PolignVectorStore`](https://github.com/Polign/polign/tree/main/python/langchain-polign)                                                   | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span> | <span data-sort-value="2">✅</span> | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                            |

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/vectorstores/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
