---
title: "Langchain x Predibase: The easiest way to fine-tune and productionize OSS LLMs"
description: "Deploy, fine-tune, and query open-source LLMs with LangChain and Predibase. Build production-ready RAG with privacy-first, cost-effective AI alternatives."
source: "https://www.langchain.com/blog/langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms"
category: "blog"
published: "2023-08-17T16:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms]
---

# Langchain x Predibase: The easiest way to fine-tune and productionize OSS LLMs

*Editor's Note: This post was written in collaboration with the Predibase team. We're really excited about the way their integration with LangChain helps bring production-grade standards and workflows to open-source to open-source models. *

Today, we’re announcing a Langchain Integration for [Predibase](https://predibase.com/?ref=blog.langchain.com). This integration allows Langchain developers to seamlessly integrate hosted OSS models on Predibase into their workflows.

## What is Predibase?

 Predibase is a Developer platform for OSS LLMs. Predibase allows builders to:

- Deploy and query pre-trained or custom open source LLMs without the hassle
- Operationalize an end-to-end Retrieval Augmented Generation (RAG) system
- Fine-tune their own LLM in just a few lines of code

If using commercial LLM providers like OpenAI / Anthropic / Cohere might not be a good fit due to privacy or cost, Predibase might be a natural choice to explore. While Predibase is focused on helping you productionize open-source LLMs, the platform itself is also built on top of open-source foundations including Ludwig and Horovod. It supports multiple interfaces including a UI and a Python SDK, making it accessible to users of all levels. Best of all, the platform can be deployed on Predibase-managed infrastructure or securely inside your own Cloud VPC so your data and models stay within your secure environment.

## Langchain + Predibase

Setup:

1. Sign up for Predibase for free: [https://predibase.com/free-trial](https://predibase.com/free-trial?ref=blog.langchain.com)
2. Create an Account
3. Go to Settings &gt; My profile and Generate a new API Token

### Q/A Example ([Colab Notebook](https://colab.research.google.com/drive/1ASRX6BOVMfgAEkTmcCDYATCSbfzfg3S4?usp=sharing&ref=blog.langchain.com))

Below is an example of a simple Q/A system you can build using Langchain and Predibase-hosted LLMs.

`pip install predibase
pip install langchain
pip install chromadb
pip install sentence_transformers

# Replace with your Predibase API Token
import os
os.environ[“PREDIBASE_API_TOKEN”] = “{PREDIBASE_API_TOKEN}”

from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import Predibase

# Document loader
from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

# Split into Chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(data)

# Store Embeddings in Chroma
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
vectorstore = Chroma.from_documents(documents=all_splits,embedding = HuggingFaceEmbeddings())

# Pull in any LLM from Predibase, including fine-tuned LLM’s
llm = Predibase(model="llama-2-13b", predibase_api_key=os.environ.get("PREDIBASE_API_TOKEN"))

# Fetch relevant chunks into LLM
from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
qa_chain({"query": question})
`

We’re very excited to make these capabilities available for all LangChain users and we couldn’t be more excited to see what the community builds! If you have ideas, comments, or questions, feel free to reach out on the [LangChain](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com) Discord or via support@predibase.com.
