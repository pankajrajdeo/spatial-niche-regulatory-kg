---
title: "LangChain + Vectara: better together"
description: "Build accurate LLM apps with LangChain + Vectara. Eliminate hallucinations through Grounded Generation for retrieval-augmented question answering."
source: "https://www.langchain.com/blog/langchain-vectara-better-together"
category: "blog"
published: "2023-06-06T14:07:16.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-vectara-better-together]
---

# LangChain + Vectara: better together

## Introduction

One of the main use cases of LangChain is connecting LLMs to user data, allowing users to build personalized LLM applications. A key part of this is retrieval - fetching relevant documents based on user queries.

Today we’re happy to announce the integration of [Vectara](http://www.vectara.com/?ref=blog.langchain.com) into LangChain to help make retrieval easier. In this blog post, we’ll dig deeper into why retrieval is so important and how to use Vectara’s LangChain integration to build scalable LLM-powered applications.

## What is Vectara?

Vectara is a GenAI [conversational search](http://vectara.com/?ref=blog.langchain.com) platform, providing an easy-to-use “ChatGPT for your own data'' experience using “[Grounded Generation](https://vectara.com/grounded-generation/?ref=blog.langchain.com)”.

Developers can use Vectara’s API, based on a neural search core, which enables highly accurate matching between queries and relevant documents, to build GenAI conversational search applications, such as our [AskNews](http://asknews.demo.vectara.com/?ref=blog.langchain.com) sample application.

Using Vectara simplifies LLM application development: the search platform does a lot of the heavy lifting of interfacing with user data, letting developers focus on the application logic unique to their product.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb21590227306de7e7901_830391a7.png)**Figure 1:** Vectara’s API platform for “Grounded Generation”

## Grounded Generation with LangChain

LLMs are extremely powerful models, but they have a problem with data recency and hallucinations. For example, as mentioned in this blog post about [LLM hallucinations](https://vectara.com/avoiding-hallucinations-in-llm-powered-applications/?ref=blog.langchain.com), if you ask ChatGPT about Silicon Valley Bank, it will provide a response based on the pre-2022 data it was trained on, and will have no idea above the bank’s recent collapse.

“Grounded Generation” is a general approach to address this issue and is one of the main use cases available through LangChain.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb21590227306de7e790f_screenshot-2023-06-05-at-8.49.41-pm.png)**Figure 2: Grounded Generation. **Content is first transformed into embeddings, and stored in a vector store. When a user issues a query, we first identify relevant facts by matching the query embedding with relevant pieces of content previously indexed and provide those facts to the summarization model (along with the query) to provide an accurate response based on all the relevant known facts.

Let’s look at a simple [example](https://github.com/hwchase17/langchain/blob/b95002289409077965d99636b15a45300d9c0b9d/docs/use_cases/evaluation/data_augmented_question_answering.ipynb?ref=blog.langchain.com#L8) of question-answering with retrieval augmented generation from the LangChain codebase.

`from langchain.document_loaders import TextLoader
from langcain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitters import CharacterTextSplitter
from langchain.vectorstores import FAISS

raw_docs = TextLoader(‘state_of_the_union.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(raw_docs)
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
qa = RetrievalQA.from_llm(llm=OpenAI(), retriever=vectorstore.as_retriever())`

**Figure 3:** Default implementation of retrieval augmented generation with LangChain

First, we take the document text (in this case, a transcript of the 2022 State of the Union) and use langchain.text_splitter.CharacterTextSplitter to split the text into small chunks (1000 characters each).

Then we get embeddings for each chunk using OpenAIEmbeddings, and store them in a vector database like FAISS.

Finally, we build a RetrievalQA ( retrieval question-answer) chain.

And the answer we get is.

> “Putin miscalculated that the world would roll over when he rolled into Ukraine.”

Pretty cool!

## LangChain question-answering with Vectara

Let’s run the same program, but this time use Vectara as the vector store. Doing this will take advantage of Vectara’s “Grounded Generation”.

First, we [set up](https://console.vectara.com/signup?ref=blog.langchain.com) a Vectara account and create a corpus. After creating an API key for that corpus, we can set up the required arguments as environment variables:

`export VECTARA_CUSTOMER_ID=&lt;your-customer-id&gt;
export VECTARA_CORPUS_ID=&lt;the-corpus-id&gt;
export VECTARA_API_KEY=&lt;...API-KEY…&gt;`

Vectara provides its own embeddings that are optimized for accurate retrieval, so we actually don’t have to use (or pay for) an additional embedding model. Instead, we simply use Vectara.from_documents() to upload the documents into Vectara’s index for this corpus, and use that as a retriever in the chain:

`from langchain.vectorstores import Vectara
loader = TextLoader(“state_of_the_union.txt”)
documents = loader.load()
vectara = Vectara.from_documents(documents)
qa = RetrievalQA.from_llm(llm=OpenAI(), retriever=vectara.as_retriever())
print(qa({“query”: “According to the document, what did Vladimir Putin miscalculate?”}))`

**Figure 3:** Question answering with LangChain + Vectara. Architecture is much simpler and more robust as the storage of document embedding and matching queries to relevant facts is taken care of by the Vectara platform/API.

Vectara takes the source documents and automatically chunks it in an optimized manner and creates the embeddings, so we don’t even have to use the TextSplitter (and decide on chunk size), nor do we need to call (or pay for) OpenAIEmbeddings. Since Vectara has its own internal vector storage, we don’t need to use FAISS or any other commercial vector database.

Finally, we build a RetrievalQA (retrieval question-answer) chain in the same way as before, and again we get the response:

> “Putin miscalculated that the world would roll over when he rolled into Ukraine.”

## Summary

We are excited to have Vectara fully integrated with LangChain, making it easier for developers who already love LangChain to build LLM-powered applications with Grounded Generation.

Big thanks to the Vectara team ([Ofer](https://twitter.com/ofermend?ref=blog.langchain.com), [Amr](https://twitter.com/awadallah?ref=blog.langchain.com) and many others) for their support and contribution.

If you’d like to experience the benefits of Vectara + LangChain firsthand, you can sign up for a free Vectara account [here](https://console.vectara.com/signup?ref=blog.langchain.com).
