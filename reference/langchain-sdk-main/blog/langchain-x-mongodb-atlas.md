---
title: "LangChain &lt;&gt; MongoDB Atlas"
description: "LangChain&#39;s MongoDB Atlas integration lets you store vector embeddings with operational data, simplifying semantic search without separate infrastructure."
source: "https://www.langchain.com/blog/langchain-x-mongodb-atlas"
category: "blog"
published: "2023-06-22T18:23:16.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-x-mongodb-atlas]
---

# LangChain &lt;&gt; MongoDB Atlas

Today we’re announcing LangChain’s integration with MongoDB Atlas, adding support for one of the most popular developer data platforms in the world. This is an integration so anticipated that a few developers added the integration before we were ready to announce it :)

### Overview

One of the key components of AI powered applications is semantic search powered by embeddings and vector stores. Semantic Search is a capability that allows you to query your data based on its meaning rather than the data itself. This is made possible by being able to represent any form of data numerically as a Vector which can then be compared to one another through sophisticated algorithms.

While building semantic search capabilities in your production application, vector stores will need to work in conjunction with an application database. One of the largest pain points associated with having a separate vector search engine from your application database is the added complexity around syncing the data between these systems and managing the additional infrastructure. And this doesn’t even include the challenges around security and compliance as you get ready for selling to enterprises. All of this adds friction to both the process of building applications as well as the work to manage and maintain them in production.

### **MongoDB Atlas - The Developer Data Platform**

MongoDB Atlas was released in 2016 to provide a cloud native, fully managed database service offering, helping developers build applications faster than ever before. Over the years, Atlas has grown into a full fledged developer data platform, satisfying workloads from transactional to search to analytical and streaming. MongoDB Atlas is a battle-tested platform that provides for high availability, horizontal and vertical scale out, and world class security. And now it is thrilled to add native support for vectors in the form of Atlas Vector Search to streamline building the next generation of applications.

### **Introducing Atlas Vector Search**

Atlas Vector Search is natively built into MongoDB Atlas, so you don’t need to copy and transform your data, learn some new stack and syntax, or manage a whole new set of infrastructure. Atlas Vector Search allows you to store your vector embeddings right alongside your operational data, dynamically update your vector entries when your data changes using Atlas Triggers, and your application only needs to interact with a single query interface. This drastically reduces the overhead of adding support for vector search and you can utilize these powerful new capabilities all within a world class and battle tested platform to build applications faster than ever before.

Sign up for Atlas [here](https://www.mongodb.com/pricing?ref=blog.langchain.com) with our Free Forever Tier

### **LangChain and MongoDB Atlas**

LangChain and MongoDB Atlas are a natural fit, and it’s been demonstrated by the organic community enthusiasm which has led to several integrations in LangChain for MongoDB. In addition to now supporting Atlas Vector Search as a Vector Store there is already support to utilize MongoDB as a chat log history.

Both LangChain and MongoDB are keenly focused on developer productivity with both our core missions centralized around ensuring an amazing developer experience.

With today’s announcement you can head over to MongoDB Atlas, setup Vector Search, and then connect LangChain and start prompting! To simplify your first time setup, we’ve added some pre-embedded data (using text-embedding-ada-002 from Open AI) to our [MongoDB Atlas sample data](https://www.mongodb.com/developer/products/atlas/atlas-sample-datasets/?ref=blog.langchain.com) (sample_mflix.embedded_movies), so it’s as easy as loading the sample data, defining a vector index, and start finding those neighbors with our approximate nearest neighbors algorithm.

### **The Future**

We are extremely excited about this new capability, but it is just the beginning! The MongoDB team is going to be moving fast in this space and we’ll be making some additional announcements in the coming months to further evolve this capability. Most importantly though we are extremely excited to stay engaged with the community to ensure we’re providing the capabilities you need, so don’t be a stranger!

A big thank you and shout out to @P-E-B who kicked off the Python implementation and @floomby who started the JavaScript support!
