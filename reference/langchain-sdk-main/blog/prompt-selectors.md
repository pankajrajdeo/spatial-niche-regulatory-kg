---
title: "Prompt Selectors"
description: "LangChain&#39;s Prompt Selectors automatically choose the right prompt template for any AI model, from ChatGPT to GPT-3, ensuring seamless chains."
source: "https://www.langchain.com/blog/prompt-selectors"
category: "blog"
published: "2023-03-08T17:45:44.000Z"
author: "LangChain Accounts"
tags: [blog, prompt-selectors]
---

# Prompt Selectors

One common complaint we've heard is that the default prompt templates do not work equally well for all models. This became especially pronounced this past week when OpenAI released a ChatGPT API. This new API had a completely new interface ([which required new abstractions](https://blog.langchain.com/chat-models/)) and as a result many users noticed issues with old prompts no longer working. Although we quickly added support for this model, many users noticed that prompt templates that worked well for GPT-3 did not work well in the chat setting.

All chains expose ways to customize these prompt templates, so there's always the option to let users pass in prompts that work better. But we want to do better than that. One goal of having chains with default prompt templates is to offer functionality that "Just Works" out of the box. If different models expect different types of prompts, this breaks down.

Our solution for this is to introduce a concept of a `PromptSelector`. Rather than define a default `PromptTemplate` for each chain, we will move towards defining a `PromptSelector` for each chain. If no prompt is specified by the user, the `PromptSelector` will select a `PromptTemplate` to use based on the model that is passed in.

For an example of this in action, check out the following examples:

### Python

[Code Definition](https://github.com/hwchase17/langchain/blob/master/langchain/chains/prompt_selector.py?ref=blog.langchain.com)

[Full Example](https://github.com/hwchase17/langchain/blob/master/langchain/chains/question_answering/stuff_prompt.py?ref=blog.langchain.com)

Snippet:

`PROMPT_SELECTOR = ConditionalPromptSelector(
 default_prompt=PROMPT, conditionals=[(is_chat_model, CHAT_PROMPT)]
)`

### In JS/TS:

[Code Definition](https://github.com/hwchase17/langchainjs/blob/main/langchain/src/chains/prompt_selector.ts?ref=blog.langchain.com)

[Full Example](https://github.com/hwchase17/langchainjs/blob/main/langchain/src/chains/question_answering/stuff_prompts.ts?ref=blog.langchain.com)

Snippet:

`export const QA_PROMPT_SELECTOR = new ConditionalPromptSelector(
 DEFAULT_QA_PROMPT,
 [[isChatModel, CHAT_PROMPT]]
);`

Both these examples show the same thing. We define a default prompt, but then if a condition (`isChatModel`) is met we switch to a different prompt. This is also extendable to an arbitrary list of "conditions" and corresponding prompts"

This is a very simple concept, but we hope it gives us (and other developers) the flexibility to define chains that "Just Work" out of the box for any model. Although the immediate use case is for switching between prompts for ChatModels (like ChatGPT) vs more traditional models (like GPT-3), we also envision this allow switching between different model providers (eg OpenAI vs Cohere) and even model versions (eg GPT-3 vs GPT-4) down the road.

It will take some time to transition over to these selectors, but we started with some of the more popular chains and intend to transition over as fast we can. As always, feedback and help from the community is greatly appreciated!
