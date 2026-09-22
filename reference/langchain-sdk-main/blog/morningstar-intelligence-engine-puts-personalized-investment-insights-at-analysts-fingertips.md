---
title: "Morningstar Intelligence Engine puts personalized investment insights at analysts&#39; fingertips"
description: "Learn how Morningstar built Intelligence Engine with LangChain to deliver personalized investment insights through AI-powered chatbots in under 60 days."
source: "https://www.langchain.com/blog/morningstar-intelligence-engine-puts-personalized-investment-insights-at-analysts-fingertips"
category: "blog"
published: "2023-11-14T12:26:32.000Z"
author: "LangChain Accounts"
tags: [blog, morningstar-intelligence-engine-puts-personalized-investment-insights-at-analysts-fingertips]
---

# Morningstar Intelligence Engine puts personalized investment insights at analysts&#39; fingertips

## **Challenge**

Financial services is one of the most data-driven industries and financial professionals are always hungry for more data and better tools to drive value for their clients. [Morningstar](https://www.morningstar.com/company/about-us?ref=blog.langchain.com)–a publicly-traded investment research firm–has been compiling and analyzing fund, stock, and general market data for finance professionals since its founding in 1984.

Getting the most out of Morningstar and its products has historically required a deep familiarity with the financial landscape, an ability to parse meticulous research reports, and a mastery of their proprietary–and powerful–toolkit. With the rise of Generative AI, the Morningstar team saw an opportunity to make their data more accessible and more immediately useful to a wider range of users.

## **Solution**

Morningstar started by building a chatbot, Mo, that allows Morningstar customers to query their extensive research database using natural language in a conversational format to generate concise yet nuanced insights in seconds.

The team also decided to extend the benefits of this innovation to their customers–often asset managers and wealth advisors–and enable them to build white-labeled chatbots and other AI tools of their own. Using their new platform, [Morningstar Intelligence Engine](https://www.morningstar.com/products/morningstar-intelligence-engine?ref=blog.langchain.com), Morningstar customers can now securely upload their own research information - to provide more context and personalization to Morningstar data - and then “whitelist” the chatbot for their end customers to use.

Several Morningstar team members were already familiar with LangChain through their contributions to the open source repository. The collaborative, community-driven spirit first drew the team to LangChain. When it came time to build a production-ready application, LangChain was the obvious choice because:

- **LangChain offered a robust framework** **for initiating LLM-powered application** development. The concepts and ideas presented in LangChain were easily comprehensible and implementable from prototype to production, which expedited the team’s development process.
- **LangChain had a blueprint for RAG applications**, making discovery and summarization easy. Morningstar integrated various essential concepts from LangChain, including prompt templates, RAG-based approach, the ReAct framework, creating vector embeddings, LangChain evaluators, function calling, and output parsing. The choice of retrieval techniques improved performance out-of-the-box.
- **LangChain helped with edge cases like retries** that helped harden Morningstar’s application
- **LangChain integrations provided **wide-ranging support across various vector databases, enhancing its versatility and applicability.
- **“LangChain introduced critical cognitive architectures that facilitate a better grasp of generative AI**, enriching our team’s understanding of this evolving technology,” said Jinyoung Kim, Head of Development. “The LangChain team keeps up the rapidly-evolving corpus of research, and then implements that into LangChain so we can benefit from the latest advances.”

Morningstar Intelligence Engine went from idea to production in under 60 days with a lean team of 5 developers.

## **Results**

“Customers have been coming to us for almost 40 years to deliver cutting-edge insights and tools that help them make better investment decisions," said Adam Wheat, Chief Technology Officer. “By launching and evolving the Intelligence Engine, Morningstar continues its tradition of creating innovative products that help drive more value for their clients.”
