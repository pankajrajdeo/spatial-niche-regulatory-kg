---
title: "LangChain x Context: Building Better Chat Products With User Analytics"
description: "Track user behavior in your LangChain chat product with Context&#39;s one-line analytics integration. Monitor satisfaction and identify conversation themes."
source: "https://www.langchain.com/blog/langchain-x-context-building-better-chat-products-with-user-analytics"
category: "blog"
published: "2023-07-13T05:34:59.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-x-context-building-better-chat-products-with-user-analytics]
---

# LangChain x Context: Building Better Chat Products With User Analytics

**Today we’re announcing a **[**Langchain integration**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com)** for **[**Context**](http://getcontext.ai/?ref=blog.langchain.com). This integration allows builders of Langchain chat products to receive user analytics with a one line plugin.

Building compelling chat products is hard. Developers need a deep understanding of user behaviour and user goals to iteratively improve their products. Common questions that builders ask include:*** how are people using my product? How well is my product meeting user needs?**** *And* ****where does my product need improvement?* **

Today, answering these questions can involve reading thousands of chat transcripts captured in logs, with little tooling to help identify conversation themes or areas of weak product performance. A better solution now exists with Langchain’s integration with Context.

## What is Context?

**Context is a product analytics platform for LLM-powered chat products.** Context gives builders visibility into how real people use their chat products, with analytics to help developers understand:

- **How people are using their products**, by automatically clustering conversations into groups and tracking user-defined conversation topics,
- **How their product is meeting user needs**, by reporting user satisfaction, sentiment, and regeneration rates for each conversation topics,
- **Where their product is introducing risk,** by monitoring discussion of risky topics like politics or gambling:
- **Exactly what users are discussing**, by providing filtering and search over transcripts to allow debugging

These analytics give builders an understanding of how people are using their product, how their product is performing, and where sensitive topics are being discussed. This user understanding helps ensure user needs are being met, and allows developers to improve their products over time.

## Getting Started

To get started, [Context](http://getcontext.ai/?ref=blog.langchain.com) can be accessed for free [here](http://getcontext.ai/?ref=blog.langchain.com), and the Context x LangChain documentation can be accessed [here](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com). The first 50 signups using *LANGCHAIN100* promo code will receive 3 free months of Context’s $100/month membership tier.

## Installation and Setup

To get started with the Context LangChain integration, install the Context Python package:

**`pip install context-python --upgrade`**

**Getting API Credentials**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#getting-api-credentials)

To get your Context API token:

1. Go to the settings page within your Context account ([https://go.getcontext.ai/settings](https://go.getcontext.ai/settings?ref=blog.langchain.com)).
2. Generate a new API Token.
3. Store this token somewhere secure.

**Setup Context**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#setup-context)

To use the ContextCallbackHandler, import the handler from Langchain and instantiate it with your Context API token.
Ensure you have installed the context-python package before using the handler.

`import os

from langchain.callbacks import ContextCallbackHandler

token = os.environ["CONTEXT_API_TOKEN"]

context_callback = ContextCallbackHandler(token)`

## Usage

**Using the Context callback within a Chat Model**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#using-the-context-callback-within-a-chat-model)

The Context callback handler can be used to directly record transcripts between users and AI assistants.

**Example**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#example)

`import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
 SystemMessage,
 HumanMessage,
)
from langchain.callbacks import ContextCallbackHandler

token = os.environ["CONTEXT_API_TOKEN"]

chat = ChatOpenAI(
 headers={"user_id": "123"}, temperature=0, callbacks=[ContextCallbackHandler(token)]
)

messages = [
 SystemMessage(
 content="You are a helpful assistant that translates English to French."
 ),
 HumanMessage(content="I love programming."),
]

print(chat(messages))`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb202ba9d0fc7237808fc_screenshot-2023-07-12-at-9.43.07-am.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb202ba9d0fc7237808f7_screenshot-2023-07-12-at-9.43.13-am.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb202ba9d0fc7237808f4_screenshot-2023-07-12-at-9.43.19-am.png)
