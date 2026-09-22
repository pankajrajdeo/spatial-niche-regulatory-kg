---
title: "Tracing"
description: "Visualize, debug, and troubleshoot LangChain chains and agents with native tracing support. Track inputs, outputs, and execution steps in real-time."
source: "https://www.langchain.com/blog/tracing"
category: "blog"
published: "2023-01-30T04:48:04.000Z"
author: "LangChain Accounts"
tags: [blog, tracing]
---

# Tracing

We’re excited to announce native tracing support in LangChain! By enabling tracing in your LangChain runs, you’ll be able to more effectively visualize, step through, and debug your chains and agents.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb26fba9d0fc723784461_explore.png)A view of a more complicated trace at a high level

## Motivation

Reasoning about your chain and agent executions is important for troubleshooting and debugging. However, it can be difficult for complex chains and agents, for a number of reasons:

1. There could be a high number of steps, making it hard to keep track of all of them
2. The sequence of steps could not be fixed, and could vary based on user input
3. The inputs/outputs at each stage may not be long and deserve more detailed inspection

Each step of a chain or agent might also involve nesting — for example, an agent might invoke a tool, which uses an `LLMMathChain`, which uses an `LLMChain`, which then invokes an `LLM`. If you notice strange or incorrect output from a top-level agent run, it is difficult to determine exactly where in the execution it was introduced.

Tracing solves this by allowing you to clearly see the inputs and outputs of each LangChain primitive involved in a particular chain or agent run, in the order in which they were invoked.

There has been some great work already for tracing and visualization for LLM compositions (see [ICE](https://github.com/oughtinc/ice?ref=blog.langchain.com) and [langchain-visualizer](https://github.com/amosjyng/langchain-visualizer?ref=blog.langchain.com)), and we’re now excited to incorporate tracing natively in LangChain. We hope to release new and exciting features that build upon tracing in the near future.

## Usage

As a starting point, we’re allowing everyone to leverage tracing in their LangChain compositions by using a locally hosted setup spun up by docker-compose. We’re also rolling out a hosted version to a small initial group of users. If you are interested in getting access to this, please fill out [this form](https://docs.google.com/forms/u/5/d/e/1FAIpQLScoDu0bJ5cGrlSJvbMW-LgPkq70ewiuBBpMCZgmwtJ3Iz-NLw/viewform?usp=send_form&ref=blog.langchain.com).

For full technical documentation on how to get started, please see [here](https://langchain.readthedocs.io/en/latest/tracing.html?ref=blog.langchain.com).

We hope to continuously iterate on this to make it as useful as possible. Please reach out with any feedback!

## Up Next

We’re just getting started with tracing and additional features. In the future we hope to add:

- UI improvements
- Better filtering and grouping of traces
- Logging the full serialized `LLM` and `Chain` for each run
- Other exciting features we’re still fleshing out ;)
