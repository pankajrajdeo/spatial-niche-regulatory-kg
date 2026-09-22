---
title: "TypeScript Support"
description: "LangChain now supports TypeScript with native prompts, chains, and agents. Seamlessly share artifacts between Python and TypeScript."
source: "https://www.langchain.com/blog/typescript-support"
category: "blog"
published: "2023-02-17T16:12:40.000Z"
author: "LangChain Accounts"
tags: [blog, typescript-support]
---

# TypeScript Support

It's finally here... TypeScript support for LangChain.

What does this mean? It means that all your favorite prompts, chains, and agents are all recreatable in TypeScript natively. Both the Python version and TypeScript version utilize the same serializable format, meaning that artifacts can seamlessly be shared between languages. As an example of using this, we've also recreated ChatLangChain with TypeScript.

A huge thank you to the community for helping with this.

Important Links:

- GitHub Repo: [https://github.com/hwchase17/langchainjs](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com)
- Documentation: [https://hwchase17.github.io/langchainjs/docs/overview/](https://hwchase17.github.io/langchainjs/docs/overview/?ref=blog.langchain.com)
- ChatLangChain-js: [https://github.com/sullivan-sean/chat-langchainjs](https://github.com/sullivan-sean/chat-langchainjs?ref=blog.langchain.com)

# Why TypeScript?

Initially, the crowd playing with language models was more of the researchy, ML-oriented folks - most of whom prefer Python. However, since the launch and quick success of ChatGPT, the idea of using LLMs has gone mainstream. As such, we saw a massive increase in interest in LangChain from folks across the stack, many of whom prefer to using javascript. As such, we thought it appropriate to develope a javascript native version of LangChain.

# What is in this package?

All of the same abstractions that are in the Python package are in the Typescript package.

- [Prompts](https://hwchase17.github.io/langchainjs/docs/modules/prompts/prompt_template?ref=blog.langchain.com)
- [LLMs](https://hwchase17.github.io/langchainjs/docs/modules/llms/openai?ref=blog.langchain.com)
- [Text Splitters](https://hwchase17.github.io/langchainjs/docs/modules/indexes/text_splitter?ref=blog.langchain.com)
- [Embeddings](https://hwchase17.github.io/langchainjs/docs/modules/indexes/embeddings?ref=blog.langchain.com)
- [Vectorstores](https://hwchase17.github.io/langchainjs/docs/modules/indexes/vectorstore?ref=blog.langchain.com)
- [Chains](https://hwchase17.github.io/langchainjs/docs/modules/chains/llm_chain?ref=blog.langchain.com)
- [Agents](https://hwchase17.github.io/langchainjs/docs/modules/agents/overview?ref=blog.langchain.com)
- [Memory](https://hwchase17.github.io/langchainjs/docs/modules/memory/buffer_memory?ref=blog.langchain.com)

Since the Typescript version is much newer, there are fewer of these implementations in there. Also, many of the more ML-centric functionality (tokenizers, LLMs, etc) have worse TypeScript support. Still, we intend to bring and grow that functionality over time.

With these abstractions, we found it very easy to recreate the "ChatLangChain" web application we previously made in Python to have a chatbot over our documentation. This utilizies many of those abstractions, and so is a perfect showcase. Check out the TypeScript version [here](https://github.com/sullivan-sean/chat-langchainjs?ref=blog.langchain.com).

# Relationship to the Python package

We intend the TypeScript package to mirror the Python package as closely as possible. To that end, it was a priority to make sure that serialized format we introduced for prompts, chains, and agents in Python worked for the TypeScript version.

We considered this a priority because as we grow the [LangChainHub](https://github.com/hwchase17/langchain-hub?ref=blog.langchain.com) over time, we want these artifacts to be shareable between languages. This will allow for largely and more widespread community adoption and sharing of best prompts, chains, and agents. This will also make it possible to prototype in one language and then switch to the other. At the moment, since the TypeScript package does have slightly less functionality than the Python package, not all the chains are portable between languages. However, we intend to push hard to make them equal.

Over time, it is not out of the question that the packages do diverge somewhat, in line with their respective audiences. For example, the Python package may start to include more researchy or data centric concepts, while the TypeScript package may include more features aimed at facilitating web dev. We are actually excited to explore the different priorities and use cases with the community. But throughout it all, we intended to keep on making the core set of prompts, chains, agents (and soon more) serializable and usable between languages.

# Thank You

A huge thank you to the community support and interest in "Langchain, but make it typescript". At one point there was a Discord group DM with 10 folks in it all contributing ideas, suggestion, and advice. In particular, large shoutout to [Sean Sullivan](https://twitter.com/_seanyneutron?ref=blog.langchain.com) and [Nuno Campos](https://twitter.com/nfcampos?ref=blog.langchain.com) for pushing hard on this.

We also pre-emptively thank the community for their feedback, contributions, and ideas for this package. We've already gotten a lot of interest in the short time we've been teasing it, and we're really excited to work on it together.
