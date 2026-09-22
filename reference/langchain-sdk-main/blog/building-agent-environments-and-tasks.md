---
title: "How We Build Agent Environments &amp; Tasks"
description: "How we create synthetic agent environments and tasks: a spec generation step, a spec-to-task step, and a world spec that holds shared knowledge."
source: "https://www.langchain.com/blog/building-agent-environments-and-tasks"
category: "blog"
published: "2026-08-25T18:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, building-agent-environments-and-tasks]
---

# How We Build Agent Environments &amp; Tasks

> **TLDR: **This is a** **practical guide on how we create synthetic agent environments and tasks. By the end, we have a two-step pipeline. The first step takes traces, code, and/or human input to build a detailed spec. The second step takes that spec and creates an eval task and an environment for that task. In order to do this, we create a “world spec” to capture shared knowledge, scripts, and important definitions. This process is very iterative. We packaged our process in an updated [eval-engineering skill](https://www.skills.sh/langchain-ai/langchain-skills/eval-engineering) so every team can own this flow for themselves.

**Glossary:**

[*Agent:*](https://www.langchain.com/blog/what-is-an-agent)* system that uses an LLM to decide the control flow of an application*

*Environment: where the agent runs*

*Rubric: a set of criteria to judge the output of an agent run*

*Task: An input, an environment, and a test script. Agents run these instructions inside and environment to produce an output which gets scored by a test script*

*Dataset: A collection of tasks, also referred to as a benchmark*

*Evaluation: running an agent over a dataset to get a score*

*Harbor: a framework for defining tasks & datasets and running evals.*

*Traces: detailed run information on an agent’s input and trajectory*

*Task Spec: detailed natural language description about a task (input, environment, test script) that can be used to create a task*

*World Spec: project specific information, scripts, helper functions, or other artifacts that can be used to either help create specs or transform specs into tasks
*

## Creating a benchmark

To reliably improve agents, you need a good benchmark to run your agents over. This helps identify regression, find areas for improvement, and generally make sure you can iterate on your agent backed by real metrics.

Building a good benchmark is hard. Each task in the benchmark needs to have a representative input, an environment that closely aligns to the real world, and an aligned rubric to grade the result on. It takes a lot of time, effort and human alignment to create a single task, let alone a whole dataset.

We think a lot about how to create better evals, and being able to more reliably and efficiently create representative benchmarks is a key part of that. Over the past few months we’ve been iterating on a process to help with this.

## What is the ideal end state?

The end state we are working towards is a dataset of **high-quality, vetted tasks.** These tasks can then be used to evaluate, hill-climb, or post-train our agent.

Examples of tasks we create internally at LangChain include:

- Tasks for GTM engineering testing capabilities like company research & finding individuals despite missing data and entries across customer tables
- Tasks for prompt optimization where an agent is evaluated
- Tasks for code review given using data from real merged PRs
- Tasks for trace mining where a small number of issues exist in a massive corpus of trace data

## A pipeline to create tasks

In order to generate a large number of these tasks, we find it is most efficient to build a pipeline to produce these tasks. We find that a core piece of creating this pipeline is the concept of a “spec”.

A spec is a markdown file that describes what the task (input, environment, graders) looks like in natural language. Depending on the dataset you are trying to build, it may have different sections or information required.

The benefit of having this concept of a spec is that it separates:

1. figuring out what each task should look like
2. building a task

The first step - “figuring out what the task should look like” - can be done in multiple ways, and often requires human iteration to align on what matters to the team and users. The second step - “building the task” - can ideally be more automated with an agent. This separation allows you to create many of different specs, centralize the human review process there, and then parallelize building them.

Specs are a good medium for human-agent collaboration and editing. It’s much easier for humans review a markdown spec rather than the raw code and data of a task. Edits can be versioned and tracked just like code and shared across teams.

Overall, the ideal end state is a pipeline that consists of two steps:

- A spec generation step
- A Spec2Task creation step

## Assembling world knowledge

To do either of those steps well requires gathering specific information about the general dataset you’re trying to create. We call this information “world knowledge” ****and it lives in “world spec.”

This information is NOT specific to a single task - if it was, it would live in the task spec. Rather, it is general knowledge across all potential tasks in a dataset (ie. the “world”).

This knowledge can be in different formats (eg markdown vs python scripts) and used in different ways. For example:

- During world spec creation

  - Guidance on what pieces of information are helpful to store such as size/shape of data and
  - Scripts for parsing traces (or other data) to extract information

- During spec to task creation

  - Knowledge of how to create good rubrics for this task (ex: programmatic vs LLM-as-a-judge)
  - Scripts for generating specific data to populate the environment

Here are some examples of world knowledge from our internal benchmarks:

- Prompt optimization benchmark:

  - Which information is important to gather ahead of time to put in the spec (domain, input shape, output classes)
  - Processes and scripts for generating good datasets
  - Standard scoring function to use for all use cases

- GTM agent benchmark:

  - APIs and schemas for specific backend services (Salesforce, Notion) that need to mock
  - Common questions that users are asking mined from existing agent traces

## Why generating a world spec is an iterative process

In order to generate specs or transform specs into tasks you need a “world spec”. How do you get this world spec and make it useful?

We’ve found that the best way to get this spec is work hand in hand with a coding agent to generate a first task, and then have it write up a general world spec that it learned along the way to use in the future. In fact, you may even want to do this for the first two or three tasks to make sure the world spec is truly complete.

In order to help with this, we created a skill ([eval-engineering](https://www.skills.sh/langchain-ai/langchain-skills/eval-engineering)) that can help you both create your first task as well as generalize that process into a world spec.

What is the coding agent doing in practice when using the eval-engineering skill to create a first task and then build a world spec?

- Scanning the repository with subagents to fine the exact prompts, tools, skills, etc that an agent interacts with.
- Grouping traces to find real world patterns of what users are asking the agent to do. These groups are good for brainstorming potential types of tasks
- Mapping out what credentials would be needed to run an agent. Does the agent call any live tools via APIs such as web search? Should we simulate this behavior or call it live during a Task?
- Cataloging all services an agent interacts with and their data schemas. Systems like SalesForce or Gong including the tables + schemas the agent interacts with.
- Finding relationships/hierarchies in data, and planning how good approaches to do synthetic data generation depending on the types of input data.

A lot of this knowledge is specific to the agent or domain a user is trying to make Tasks for. A core part creating a world spec is iteratively gathering user feedback, which is why creating this world spec while also generating a first task is so useful.

## What does a task spec contain

The process of generating a single task requires writing down all of the implementation details specific to that task but informed by the overall world knowledge. The spec we create generally should cover three parts:

- What the agent environment looks like
- What the inputs should be
- How the outputs should be scored

Some of these may be optional, if they are the same for all tasks and can be covered by the “world spec”. For example:

- For general QA chatbots, the environment may always be the same (it’s just the inputs/outputs that change). In this case, the environment information could be consolidated in the “world spec” and shared across tasks.
- For a GTM research task, the inputs may stay fixed (and be specified in the “world spec”) but the environment and therefore the rubric to grade would be part of the task spec

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a8cb4481b5af51c8bef0a06_image.png)

## Spec2Task

Spec-to-task is the pipeline for taking a spec and generating a task in [Harbor format](https://www.harborframework.com/docs/tasks). This is most easily done with a coding agent. You can pass it a task specs, give it the “world spec” as a skill containing your specific knowledge on task creation, and the eval-engineering skill (contains some guidance on how to create tasks in Harbor format).

Some learnings we found on good Spec2Task creation:

- Have the pipeline refine tasks by running them with real agents and reading trajectories. This helps them find any flaws in environment design such as overly specific instructions or leaky abstractions. Ex: a poorly written table entry saying “Answer placeholder”
- The difficultly of tasks can be calibrated by having the pipeline run each task with different tier models (ex: gpt-5.6- Luna vs gpt-5.6-Sol). This gives feedback about whether tasks are too easy or too hard for a certain tier of model or if the task is broken for a stronger model because of a reward hack.
- Agents are bad at knowing what method to use for generating different types of data. So we give them overall guidance such as using LLMs with rubrics for free-text data and using scripts with sqlite + specified schemas for tabular data.

## End to end process

1. Use eval-engineering to create a first task

  1. Make sure the eval-engineering skill is loaded
  2. **Example Prompt: “**Use the eval-engineering skill, the traces from `{LangSmith project}`, and the `{current repository}` to help me create an eval Task for `{agent}`.”
  3. This will involve some back and forth, will create (and surface to user) a separate skill for the world spec, and after agreement will create a Task

2. Review the world spec skill and make any adjustments necessary

  1. Example Prompt: Review the `{world spec - insert name that was created}`skill, tell me the core parts of what it says so I can review it

3. Use “world spec” and eval-engineering to create a second task

  1. Switch thread so you can properly validate the world spec skill. Make sure the world spec skill AND eval engineering skill are loaded
  2. **Example Prompt: “**Use the `{world spec}` skill to create a new task. This task should…”
  3. This will involve some back and forth, and will update the `{world spec}` skill

4. Repeat step 2

  1. **Example Prompt: “**The customers in this task look too similar. Expand the customer set with bigger and smaller customers with varying amounts of revenue, total employees, emails sent, etc.”

5. Repeat steps 3-4 until confident
6. Scale this process with a coding agent with “world spec” to look at a bunch of traces and generate specs

  1. **Example Prompt: “**Use `{world spec}` to create 10 new, different task specs for me to review. Use traces from the last 10 days to find new patterns we’re not capturing today in our tasks.”

7. Run each of those specs through a coding agent with “world spec” to create a bunch of tasks

  1. **Example Prompt: “**Use `{world spec}` with `{task spec X}` to create a new task.”

## **Where human judgment is still needed**

The eval-engineering skill provides a general framework for building agent environments, but the process is not fully autonomous. Agents still need human guidance in two areas.

First, refining specs often requires several rounds of feedback. The agent needs help determining whether a spec accurately reflects the real-world domain, user behavior, and task requirements.

Second, agents tend to create tasks that are too easy. This helps validate that the environment works, but a useful benchmark needs tasks across a range of difficulty levels. Calibrating that difficulty usually requires running each task multiple times, reviewing the trajectories, and asking the agent to make the task easier or harder.

## Building Environments is a Continuous Process of Improving Agents

We are incredibly excited about a future where teams are **continuously building environments from production data.** The eval-engineering skill provides a framework for quickening that process.

Environments can be used for many types of agent optimizations like prompt tuning, harness tuning, or post-training. These environments can also answer questions like:

- Can I use a cheaper model for a subset of tasks? How much will that save me?
- Can I simplify the prompt?
- What if I remove all of the existing harness tools and just use bash for everything?

Production data and models change rapidly and so these environments need to be continuously updated to match what users care about and what the latest models can do. This is why building environments must be a continuous process and that is exactly what our eval-engineering skill is designed for.

If any of this interests you reach out and [try our skill](https://www.skills.sh/langchain-ai/langchain-skills/eval-engineering). We’re actively researching how to make this process easier so every can use their data to own & continuously improve their intelligence.

‍
