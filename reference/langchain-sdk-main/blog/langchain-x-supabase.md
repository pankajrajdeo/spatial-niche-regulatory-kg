---
title: "LangChain x Supabase"
description: "Build full-stack AI applications with LangChain and Supabase. Use vector stores, hybrid search, and edge functions to create ChatGPT-like apps with your data."
source: "https://www.langchain.com/blog/langchain-x-supabase"
category: "blog"
published: "2023-04-08T20:04:19.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-x-supabase]
---

# LangChain x Supabase

Supabase is holding an [AI Hackathon](https://supabase.com/blog/launch-week-7-hackathon?ref=blog.langchain.com) this week. Here at LangChain we are big fans of both Supabase and hackathons, so we thought this would be a perfect time to highlight the multiple ways you can use LangChain and Supabase together.

The reason we like Supabase so much is that it useful in multiple different ways. A big part of building interesting AI applications is connecting models like GPT-3 with your personal data. So in that way, the different types of databases that Supabase supports are incredibly helpful. But after you've built your application, you also need a way to share it with the world - Supabase can help with that as well.

## Supabase VectorStore

One of the main type of AI applications people have been building is ways to "chat" with your document data. Basically, ChatGPT but where it knows information about specific data, whether it be your personal writing or an esoteric website. For an in depth tutorial on this type of application, please see this [blog](https://blog.langchain.com/tutorial-chatgpt-over-your-data/). A big part of this application is storing embeddings of documents in a vectorstore. Supabase can do that! See our documentation [here](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase?ref=blog.langchain.com) for a walkthrough of how to do so.

## Supabase Hybrid Search

Vectorstores enable easy semantic search over documents, but that's not the only way to do retrieval of documents. The MendableAI team, for example, found a [20% increase in retrieval performance](https://twitter.com/ericciarla/status/1643318182369796096?s=20&ref=blog.langchain.com) by switching to a hybrid search technique. They used Supabase to so do! See our documentation [here](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid?ref=blog.langchain.com) for a walkthrough of how you can experiment with this as well.

## Supabase + LangChain Starter Template

To make it super easy to build a full stack application with Supabase and LangChain we've put together a GitHub repo [starter template](https://github.com/langchain-ai/langchain-template-supabase?ref=blog.langchain.com). Our template includes

- An empty Supabase project you can run locally and deploy to Supabase once ready, along with setup and deploy instructions
- In [`supabase/functions/chat`](https://github.com/langchain-ai/langchain-template-supabase/blob/main/supabase/functions/chat/index.ts?ref=blog.langchain.com) a Supabase Edge Function that uses LangChain to call the GPT-3.5 API, with support for both batch and streaming modes for an amazing user experience.
- In `supabase/migrations` a Postgres migration that sets you up for using the Supabase Vector Store for LangChain.
- In `src` a React + Next.js + Tailwind frontend already set up with the Supabase SDK, and with an [example of calling the Chat function](https://github.com/langchain-ai/langchain-template-supabase/blob/main/src/pages/index.tsx?ref=blog.langchain.com)

With this you can build a full-stack AI application with

- All the modules that LangChain offers, eg. Prompts, Chains, LLMs, Chat Models, Retrievers, Vector Stores, Document Loaders, Text Splitters, etc.
- All the amazing features that Supabase offers out-of-the-box, eg. database, auth, storage, realtime, etc.
- A frontend stack you can easily customise with React + Next.js + Tailwind

Supabase Edge Functions uses Deno under the hood, we've recently added support for running LangChain on Deno, any issues let us know on [Discord](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com) or [GitHub](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com)!
