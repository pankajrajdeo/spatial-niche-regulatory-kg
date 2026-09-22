---
title: "Managed Deep Agents is now in Public Beta"
description: "Deploy Deep Agents to a managed LangSmith runtime with durable execution, memory, sandboxes, channels, evals, and production-ready infrastructure."
source: "https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta"
category: "blog"
published: "2026-08-07T17:01:00.000Z"
author: "LangChain Accounts"
tags: [blog, managed-deep-agents-is-now-in-public-beta]
---

# Managed Deep Agents is now in Public Beta

Today, Managed Deep Agents is available in public beta. Go from prototype to production scale without managing the underlying infrastructure yourself. You can author a Deep Agent in Python or TypeScript, test it locally, and deploy it to a managed runtime with one command.

You control the model, instructions, tools, middleware, subagents, and more. LangSmith handles the runtime, including persistence, memory mounts, skill loading, sandbox lifecycle, and deployment.

Get started with the commands below:

```
# Install from the ecosystem you use to author the agent
uv tool install managed-deepagents      # Python
# or: npm install -g managed-deepagents # TypeScript

mda init research-assistant
cd research-assistant
uv sync                                 # Python
# or: npm install                       # TypeScript

mda dev        # run locally in LangSmith Studio
mda deploy     # deploy to LangSmith
```

## Deep Agents is an open source agent harness you can own

We built Deep Agents around a pattern we kept seeing in useful agents. Agents often need to:

- Call tools
- Have somewhere to keep working files
- Manage growing context over long runs
- Needs to delegate work to subagents
- Load domain-specific skills
- Pause for human approval before taking sensitive actions.

You can build all of that yourself on top of a lower-level framework, but the pattern is common enough that it should be available as a reusable harness that companies can own and control. Deep Agents is that harness. It's open source and model agnostic, allowing you to bring your model, your instructions, your tools, and your business logic.

## Managed Deep Agents helps you take the harness to production

Deep Agents makes it easier to build capable agents. Managed Deep Agents makes it easier to run those agents in production.

It handles the production infrastructure that’s costly to build and maintain, while keeping the parts that make your agent unique in your control. That means you can spend your time on the agent's behavior, including prompts, tools, middleware, identity rules, evals, and domain logic instead of rebuilding the same infra that every agent requires:

- **Durable execution** so long-running agents can pause, retry, and resume without losing work
- **Streaming** so users can see progress while the agent is working
- **Persistence** so thread state survives across turns, restarts, and failures
- **Sandboxes** so agents can work with files, run code, and use CLIs in isolated environments
- **Evals** so teams can test behavior, tool use, and state changes before and after deployment
- **Channels** so agents can meet users in tools like Slack
- **Memory** so agents can carry durable context and preferences across conversations
- **Identity** so agents can act with the right user context and access boundaries

A Managed Deep Agent is a code-first project in your repo. It allows you to easily organize all your agent’s primitives into a simple directory:

```
my-agent/
  agent.py | agent.ts | agent.tsx
  pyproject.toml | package.json    # project dependencies
  instructions.md                  # prompt synced to Context Hub
  identity.py | identity.ts        # auth, thread scoping, memory scoping
  memory.py | memory.ts            # define your agent's memory
  tools/                           # custom tools
  channels/                        # entry points like Slack and GitHub
  middleware/                      # custom middleware
  schedules/                       # managed cron schedules
  connectors/                      # managed cron schedules
  skills/                          # skills synced to Context Hub
  sandbox/                         # sandbox configuration
  evals/                           # agent evals
```

Once you author your project and run `mda deploy` , Managed Deep Agents compiles the project, syncs deploy-owned context to [LangSmith Context Hub](../langsmith/prompt-context-hub.md), uploads the build, and creates a hosted LangSmith deployment.

Here's what MDA looks like:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a761071905a9fbecf7bac8c_Managed%20Deep%20Agents%201%402x.png)

## Built on top of LangSmith Deployment

Most production infrastructure assumes short-lived, stateless requests. Agents often break both assumptions. Agents often run for minutes, hours, and even days. It may need to pause for approval, resume after a user replies, stream progress while it works, and recover from infrastructure restarts without losing state. It may need durable threads, persistent memory, cancellation, retry behavior, and traceability across model calls, tool calls, files, errors, and runtime state.

Building this infrastructure from scratch can take months or even quarters, and it has to be maintained. Durable execution, streaming, human approval, auth, scheduling, and conversation state all introduce edge cases around persistence, retries, timeouts, and reliability that directly impact user experience and agent usefulness.

Managed Deep Agents is built on the same LangSmith Deployment Agent Server that teams already use to run agents in production. It packages the operational patterns required for product agents into a more opinionated runtime for Deep Agents.

That gives you production primitives out of the box:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a76109b895eb43cf2617dd8_deployment-mda-primitives.png)

## Sandboxes for code execution and filesystem work

Many useful agents need an isolated working environment to inspect files, write outputs, run tests, install dependencies, call CLIs, or execute code securely.

Deep Agents supports sandbox backends for this kind of work. We have built first class support for [LangSmith Sandboxes](../langsmith/sandboxes.md) for Managed Deep Agents.

You configure a sandbox in just a few lines of code:

```
from managed_deepagents import define_sandbox

sandbox = define_sandbox(
    provider="langsmith",
    scope="thread",
)
```

By default, each durable thread gets its own sandbox. That works well for agents that need an isolated workspace per user conversation or task, such as a coding agent. You can also set the scope to `agent` when the agent process should share one sandbox across threads.

Managed Deep Agents gives agents a controlled place to work without making you manage sandbox provisioning, lifecycle, and cleanup yourself. Sandbox activity is traced to LangSmith , so you can inspect what happened when a run succeeds or fails.

## Harbor evals without the setup work

Verifying agent behavior requires more than evaluating just a prompt and expected answer. You need to check what actions the agent took along the way to get to the final answer. That's where evals come in. For example:

Did it call the right tools? Did it edit the right files? Did it create the expected artifact? Did the final workspace state match the task? For code and file-based agents, those state-based checks are often more useful than only scoring the final message.

Managed Deep Agents uses [Harbor](https://www.harborframework.com/docs) for this workflow. Harbor tasks give the agent an instruction, run it in an isolated environment, and grade the resulting files or state with a verifier.

The hard part is usually packaging your agent so Harbor can run it. Managed Deep Agents handles this packaging for you, in just a few short terminal commands:

```
mda evals init
mda evals compile
```

`mda evals init` creates checked-in Harbor tasks under `evals/`. `mda evals compile` builds a Harbor handoff under `.mda/evals/`, including the compiled agent artifact, the adapter Harbor uses to run the agent, and an example Harbor job config.

You still run Harbor directly, either locally in Docker or in another Harbor environment you configure. That keeps your evals portable. Managed Deep Agents gives you the bridge from your production-ready agent to a Harbor-ready artifact.

Once the agent is deployed, you can manage your evals and monitor production behavior in LangSmith. Every run is traced in LangSmith, so production failures become future test cases, closing the feedback loop.

## Channels bring agents into the tools where work happens

Channels are how you expose your agent to users. Managed Deep Agents has first class support for channels, making it straightforward to define how your agent connects to different channels, such as Slack. Add a file under `channels/`, and the runtime mounts the provider event endpoint, verifies provider signatures, invokes your agent with identity stamps, and can reply in the originating conversation.

For Slack, that can be as simple as defining a channel file:

```
from managed_deepagents import channels

channel = channels.slack(
    on=["app_mention", "direct_message"],
    auto_reply=True,
)
```

Channels let your agent receive events from systems like Slack and respond without a separate integration service. This is especially useful for agents that collaborate with users, such as a code review agent that can comment on GitHub or a support or operations agent that responds in Slack. Users can tag an agent where the team is already discussing the work.

## Memory that persists across threads

Thread state helps an agent manage a single conversation, but agents often need context that lasts longer than one thread. Memory gives them durable preferences and context they can carry across conversations.

Managed Deep Agents gives every deployment agent-scoped memory to start. You define memory behavior in `memory.py` or `memory.ts`, and the runtime backs memory with Context Hub. At runtime, the agent reads and writes memory files under `/memories/`.

Deploy syncs instructions and skills from your project, but it preserves runtime-created memories. That means you can redeploy your agent to update its harness behavior without wiping what the agent learned.

## Identity and auth for multi-user agents

Managed Deep Agents includes a basic identity model today, and we will keep adding more advanced auth and credential flows going forward.

Today, your agent can run with a fixed set of credentials. If you define an OIDC provider in `identity.py` or `identity.ts`, Managed Deep Agents scopes threads per end user id from your OIDC provider. That keeps each user's threads isolated under the same deployment.

The identity system is also the basis for scoped memory and future credential patterns. That gives your agent a trusted way to know who triggered the run without relying on prompt text or spoofable request fields.

## How teams are using Managed Deep Agents today

Teams are already using Managed Deep Agents to ship faster by focusing on agent behavior instead of infrastructure, scaling, and runtime logic.

> Managed Deep Agents was amazing to work with. Highly recommend for teams exploring agent infrastructure who want a more cohesive offering, while avoiding model or lab lock-in.

- Chip Lay, Director of Product, Fullstory

> Managed Deep Agents lets us scale our agentic workforce: an agent goes from idea to production in hours, not weeks. Our teacher agent wakes up every morning to review the runs of our entire fleet and drives improvements based on observability and live evals. We focus on the business logic; Managed Deep Agents handles the operational complexity, from persistent memory and the runtime to Slack and GitHub integration.

- Mathieu Mailhos, Staff Engineer, AI Runtime & Infrastructure, stealth-mode startup

## When to use Managed Deep Agents

Managed Deep Agents is useful when you want a code-first Deep Agent with LangSmith owning persistence, execution, deployment, and the common production scaffolding around the harness.

Use it when you want to:

- Build on the open source Deep Agents harness
- Keep control over your model, prompts, tools, middleware, and business logic
- Deploy without rebuilding agent infrastructure from scratch
- Give the agent durable threads, memory, sandboxes, channels, schedules, evals, and traces
- Move quickly from local development to a hosted LangSmith deployment

If you need custom routes, application code alongside the graph, custom auth logic, or direct control over the persistence layer, use LangSmith Deployment directly. If you want to operate the harness yourself, Deep Agents is open source, so you can run it on the infrastructure you choose.

The public beta scope today:

- LangSmith Cloud in the US region
- CLI-first while we finalize the supported API
- Additional regions and deployment methods will be available at a later date

These are beta primitives, and we are excited to hear evolve it as we hear feedback from teams running workloads on Managed Deep Agents

## Get started

Follow the [quickstart](../langsmith/python/managed-deep-agents-quickstart.md) to deploy your first Managed Deep Agent. The [tutorial](../langsmith/python/managed-deep-agents-tutorial.md) adds identity, memory, tools, and evals step by step.

If you want the open source harness first, start with the [Deep Agents overview](../deepagents/overview.md). When you are ready to productionize that harness, use Managed Deep Agents to deploy it to LangSmith.

We would love to hear what you build, where the defaults work, and where you need more control.
