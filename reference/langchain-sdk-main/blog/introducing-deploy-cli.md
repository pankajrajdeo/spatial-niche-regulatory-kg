---
title: "Introducing deploy cli"
description: "Deploy LangGraph agents in one command. The deploy cli automates Docker builds, infrastructure setup, and CI/CD integration for production."
source: "https://www.langchain.com/blog/introducing-deploy-cli"
category: "blog"
published: "2026-03-16T17:20:21.000Z"
author: "LangChain Accounts"
tags: [blog, introducing-deploy-cli]
---

# Introducing deploy cli

We’re excited to introduce the deploy cli, a new set of commands within the `langgraph-cli` package that makes it simple to deploy and manage agents directly from the command line.

The first command in this new set, `langgraph deploy`, lets you deploy an agent to [LangSmith Deployment](../langsmith/deployments.md#langsmith-deployment) in a single step. This makes it easy to integrate LangSmith Deployment into existing CI/CD workflows using tools like GitHub Actions, GitLab CI, or Bitbucket Pipelines.

When you run the command, the cli builds a Docker image for your local LangGraph project and provisions [the infrastructure](../langsmith/data-plane.md#server-infrastructure) needed to run it. This includes setting up supporting services like Postgres for persistence and Redis for streaming messages, so your agent can run reliably in production without any manual infrastructure setup.

Alongside `langgraph deploy`, we’re also introducing a few other commands to help create and manage deployments in your workspace.

You can:

- View all available commands using `langgraph deploy --help`
- List deployments in your workspace using `langgraph deploy list`
- View deployment logs using `langgraph deploy logs`
- Delete deployments using `langgraph deploy delete`

We’ve also released new [deep agent](https://github.com/langchain-ai/deep-agent-template?ref=blog.langchain.com) and [simple agent](https://github.com/langchain-ai/simple-agent-template?ref=blog.langchain.com) templates that you can generate with `langgraph new` .

To see how easy it is to deploy and manage your agents with the cli, see the below video:

## Try It Out

The new commands are available now in the latest version of **`langgraph-cli`**. You can use `uvx` to get started easily:

`uvx --from langgraph-cli langgraph deploy
`

See the docs here: [https://docs.langchain.com/langsmith/cli#deploy](../langsmith/cli.md#deploy).

As always, we’d love your feedback as we continue improving the developer experience around building and deploying agents.
