---
title: "Neon x LangChain: HNSW in Postgres with pg_embedding"
description: "Build faster vector search in Postgres with Neon&#39;s pg_embedding extension and LangChain. Get 20x faster queries with 99% accuracy using HNSW indexing."
source: "https://www.langchain.com/blog/neon-x-langchainhnsw-in-postgres-with-pg-embedding"
category: "blog"
published: "2023-07-12T14:27:30.000Z"
author: "LangChain Accounts"
tags: [blog, neon-x-langchainhnsw-in-postgres-with-pg-embedding]
---

# Neon x LangChain: HNSW in Postgres with pg_embedding

***Editor’s Note: This blog post was written in collaboration with the Neon team (Raouf Chebri in particular). The vectorstore space is on fire, and we’re excited to highlight new implementations and options. We’re also really excited by the detailed analysis done here, bringing some solid stats and insights to a novel space.***

We’re very excited to announce Neon’s collaboration with LangChain to release the pg_embedding extension and PGEmbedding integration in LangChain for vector similarity search in Postgres.

But wait. Aren’t they already two other vector stores in LangChain using Postgres and PGVector? Why did the Neon team add another?

The short answer is: the Neon team built and added it for faster execution time and scalable LLM applications.

PGVector is great, it does exact similarity search by default, which results in 100% accuracy (recall). At scale, however, exact search is costly. Neon found that you can use PGVector with the IVFFlat index to improve query execution time, but that often comes at the cost of accuracy, which increases the chance of hallucination.

The Neon team carried out benchmark tests to compare the performance of pgvector and PGEmbedding, and they found out that PGEmbedding performs 20x faster for 99% accuracy.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb204ba9d0fc72378098f_n4ejk30qpqs4a0nlo6k5rph1tol89txmolqfdjzhnlft56fwdp7nfrp7hvxr8ejr4v98lbsy1-qjqtko2s0selsy_iucu2dlsi01sif3vl5bdrdqlqcp56b7sn82o4j2uabbd2egyh81zebmeabk2ie.png)

Read the full article to learn more about the benchmark [here](https://neon.tech/blog/pg-embedding-extension-for-vector-search?ref=blog.langchain.com).

## Why is PGEmbedding faster?

The PGEmbedding integration uses the Hierarchical Navigable Small World (HNSW) index graph-based approach to indexing high-dimensional data. It constructs a hierarchy of graphs, where each layer is a subset of the previous one, which results in a time complexity of O(log(rows)). Search with IVFFlat optimal parameters, however, often has a time complexity of O(sqrt(rows)).

## How to get started with PGEmbedding

1. The first step is to login to your Neon account and create a project:

`npx neonctl auth`

The command above will direct you to the sign-up if you do not already have a Neon account.

Once logged in, create a project using the following command:

`npx neonctl projects create`

Expected output:

`┌─────────────────┬─────────────────┬───────────────┬──────────────────────┐
│ Id │ Name │ Region Id │ Created At │
├─────────────────┼─────────────────┼───────────────┼──────────────────────┤
│ dawn-sun-749604 │ dawn-sun-749604 │ aws-us-east-2 │ 2023-07-11T20:55:32Z │
└─────────────────┴─────────────────┴───────────────┴──────────────────────┘
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ Connection Uri │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ postgres://&lt;user&gt;:&lt;password&gt;@ep-lingering-moon-792025.us-east-2.aws.neon.tech/neondb │
└───────────────────────────────────────────────────────────────────────────────────────┘`

2. Follow the instructions in the documentation to [install LangChain](https://python.langchain.com/docs/get_started/installation?ref=blog.langchain.com) if you haven’t done so already.

3. The code below initializes the PGEmbedding vector store, and executes a similarity analysis

`import os
from typing import List, Tuple

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import PGEmbedding
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document

loader = TextLoader('state_of_the_union.txt')
raw_docs = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(raw_docs)
embeddings = OpenAIEmbeddings()
CONNECTION_STRING = os.environ["DATABASE_URL"]

# Initialize the vectorstore, create tables and store embeddings and
# metadata.
db = PGEmbedding.from_documents(
 embedding=embeddings,
 documents=docs,
 collection_name="state_of_the_union",
 connection_string=CONNECTION_STRING,
)

# Create the index using HNSW. This step is optional. By default the
# vectorstore uses exact search.
db.create_hnsw_index(max_elements=10000, dims=1536, m=8, ef_construction =16, ef_search=16)

# Execute the similarity search and return documents
query = "What did the president say about Ketanji Brown Jackson"
docs_with_score = db.similarity_search_with_score(query)

print('query done')

print("Results:")
for doc, score in docs_with_score:
 print("-" * 80)
 print("Score: ", score)
 print(doc.page_content)
 print("-" * 80)`

## PGEmbedding vs PGVector: Which vector store should you pick?

The Neon team compared both indexes using five criteria:

- Search speed
- Accuracy
- Memory usage
- Index construction speed
- Distance metrics

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb204ba9d0fc723780992_7ih9sd69xrpmejzwnphpciarrwqaaifn8xw2zme0n1skxgqnz3l76lqr2h3zume0uqruptwatetggn3qlk5ih4_gbmysqwj5taowsdtpoza_t-hrm9qlseyau7icmxyobzkt88rq8v8ycfqm4adrod8.png)

PGVector / SupabaseVectorStore

PGEmbedding

Search Speed

Fast, but the search speed depends on the number of clusters examined. More clusters mean higher accuracy but slower search times.

Typically faster than IVFFlat, especially in high-dimensional spaces, thanks to its graph-based nature.

Accuracy

Can achieve high accuracy but at the cost of examining more clusters and hence longer search times.

Generally achieves higher accuracy for the same memory footprint compared to IVFFlat.

Memory Usage

It uses relatively less memory since it only stores the centroids of clusters and the lists of vectors within these clusters.

Generally uses more memory because it maintains a graph structure with multiple layers.

Index Construction Speed

Index building process is relatively fast. The data points are assigned to the nearest centroid, and inverted lists are constructed.

Index construction involves building multiple layers of graphs, which can be computationally intensive, especially if you choose high values for the parameter ef_construction

Distance Metrics

Typically used for L2 distances, but pgvector supports inner product and cosine distance as well.

Only uses L2 distance metrics at the moment.

## Conclusion

With the introduction of the PGEmbedding integration, you now have a powerful new tool at your disposal for your LLM apps. PGVector remains a viable choice for applications with stringent memory constraints but at the expense of recall.

Ultimately, the choice between PGEmbedding and other vector stores should be informed by the specific demands of your application. We encourage you to experiment with both approaches to find the one that best meets your needs.

We are excited to see what you are going to build with PGEmbedding and look forward to your feedback!

Happy coding!
