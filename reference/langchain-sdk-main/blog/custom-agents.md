---
title: "Custom Agents"
description: "Build custom AI agents with LangChain&#39;s BaseSingleActionAgent and LLMSingleActionAgent abstractions. Customize prompts, models, and parsing."
source: "https://www.langchain.com/blog/custom-agents"
category: "blog"
published: "2023-04-03T16:05:55.000Z"
author: "LangChain Accounts"
tags: [blog, custom-agents]
---

# Custom Agents

One of the most common requests we've heard is better functionality and documentation for creating custom agents. This has always been a bit tricky - because in our mind it's actually still very unclear what an "agent" actually is, and therefor what the "right" abstractions for them may be. Recently, we've felt some of the abstractions starting to come together, so we did a big push across both our [Python](https://github.com/hwchase17/langchain?ref=blog.langchain.com) and [TypeScript](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com) modules to better enforce and document these abstractions. Please see below for links to those technical docs, and then a description of the abstractions we've introduced and future directions.

- [Python Custom Agent Docs](https://python.langchain.com/docs/modules/agents/how_to/custom_llm_agent?ref=blog.langchain.com)
- [TypeScript Custom Agent Docs](https://js.langchain.com/docs/modules/agents/agents/custom_llm?ref=blog.langchain.com)

**TL;DR:** we've introduced a `BaseSingleActionAgent` as the highest level abstraction for an agent that can be used in our current `AgentExecutor`. We've added a more practical `LLMSingleActionAgent` that implements this interface in a simple and extensible way (PromptTemplate + LLM + OutputParser).

## BaseSingleActionAgent

The most base abstraction we've introduced is a `BaseSingleActionAgent`. As you can tell by the name, we don't consider this a base abstraction for all agents. Rather, we consider this the base abstraction for a family of agents that predicts a single action at a time.

A `SingleActionAgent` is used in an our current `AgentExecutor`. This `AgentExecutor` can largely be thought of as a loop that:

1. Passes user input and any previous steps to the Agent
2. If the Agent returns an `AgentFinish`, then return that directly to the user
3. If the Agent returns an `AgentAction`, then use that to call a tool and get an `Observation`
4. Repeat, passing the `AgentAction` and `Observation` back to the Agent until an `AgentFinish` is emitted.

`AgentAction` is a response that consists of `action` and `action_input`. `action` refers to which tool to use, and `action_input` refers to the input to that tool.

`AgentFinish` is a response that contains the final message to be sent back to the user. This should be used to end an agent run.

If you are interested in this level of customizability, check out [this walkthrough](https://python.langchain.com/docs/modules/agents/how_to/custom_agent?ref=blog.langchain.com). For most use cases, however, we would recommend using the abstraction below.

## LLMSingleActionAgent

Another class we've introduced is the `LLMSingleActionAgent`. This is a concrete implementation of the `BaseSingleActionAgent`, but is highly modular so therefor is highly customizable.

The `LLMSingleActionAgent` consists of four parts:

- `PromptTemplate`: This is the prompt template that can be used to instruct the language model on what to do
- `LLM`: This is the language model that powers the agent
- `stop` sequence: Instructs the `LLM` to stop generating as soon as this string is found
- `OutputParser`: This determines how to parse the output of an `LLM` into an `AgentAction` or `AgentFinish` object

The logic for combining these is:

- Use the `PromptTemplate` to turn the input variables (inlcuding user input and any previous `AgentAction`, `Observation` pairs) into a prompt
- Pass the prompt to the `LLM`, with a specific `stop` sequence
- Parse the output of the `LLM` into an `AgentAction` or `AgentFinish` object

These abstraction can be used to customize your agent in a lot of ways. For example:

- Want to give your agent some personality? Use the `PromptTemplate`!
- Want to format the previous `AgentAction`, `Observation` pairs in a specific way? Use the `PromptTemplate`!
- Want to use a custom or local model? Write a custom LLM wrapper and pass that in as the LLM!
- **Is the output parsing too brittle, or you want to handle errors in a different way? Use a custom OutputParser!**

(The last one is in bold, because that's the one we'v maybe heard the most)

We imagine this being the most practically useful abstraction. Please see the documentation links at the beginning of the blog for links to concrete Python/TypeScripts guides for getting started here.

## Future Directions

We hope these abstractions have clarified some of our thinking around agents, as well as open up places where we hope the community can contribute. In particular:

We are very excited about other examples of `SingleActionAgents`, like:

- Using embeddings to do tool selection before calling an `LLM`
- Using a `ConstitutionalChain` instead of an `LLMChain` to improve reliability

We are also excited about other types of agents (which will require new `AgentExecutors`), like:

- Multi-action agents
- Plan-execute agents

If any of those sound interesting, we are always willing to work with folks to implement their ideas! The best way is probably to do some initial work, open a RFC pull request, and we're happy to go from there :)
