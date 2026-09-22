---
title: "How we build an autonomous SRE Agent for Kubernetes Deployments"
description: "Learn how LangChain built an autonomous SRE agent for Kubernetes deployments with Deep Agents, human approval for changes, LangSmith tracing, and evals."
source: "https://www.langchain.com/blog/how-we-build-an-autonomous-sre-agent-for-kubernetes-deployments"
category: "blog"
published: "2026-08-05T16:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-we-build-an-autonomous-sre-agent-for-kubernetes-deployments]
---

# How we build an autonomous SRE Agent for Kubernetes Deployments

How we build an autonomous SRE Agent for Kubernetes Deployments

I'm a Deployed Engineer at LangChain, and a good part of my job lives on top of Kubernetes. I maintain our internal self-hosted cluster (also where new self-hosted features land first, so our team can test them as they arrive), and I help customers stand up and upgrade their own self-hosted environments. Doing this requires a mental model of a live cluster deep enough that when ours goes down I can read the architecture, find the fault, and fix it. Doing that continuously, on top of a full-time job, is exhausting, and it isn't unique to me. Anyone who works on infrastructure knows these pains.

So we built an autonomous SRE Agent to reduce time to triage and time to remediation. The goal was to improve infrastructure reliability and reduce cognitive load on the team. We wanted it to triage Kubernetes health, propose fixes, and pull in a human only when a cluster or infrastructure changes need to happen. This post covers why, how we built it, why LangSmith makes it trustworthy, and the benefits we've seen.

## Part 1: Why We Built It

Kubernetes emits a firehose of signals (pod phases, restart counts, HPA (Horizontal Pod Autoscaling) states, node conditions, warning events, deployment readiness, across dozens of namespaces) and almost no synthesis. On-call engineers use these signals to answer three questions: Is anything broken now (a crash loop, an OOM kill, zero ready endpoints); Is anything about to break (an HPA pinned at max, a single-replica service, :latest image tags); What do we do about it? Answering these questions well takes judgment, so it falls to infrastructure engineers or subject matter experts, but 90% of this work is mechanical triage that mostly comes back clean. This is the toil that burns people out and trains them to inadvertently skim past important alerts.

## Part 2: What we built

**Proactive monitoring. **A scheduler checks health every N minutes without waking the full agent. It collects raw cluster state through the Kubernetes Python client (zero LLM tokens), then makes one Claude Haiku call with forced tool-use to produce a structured health report that lands in Slack, sorted by severity.

**On-demand investigation. **When an issue needs diagnosis, the orchestrator fans out to specialized subagents in parallel: pod-inspector, scaling-analyzer, performance-analyzer, log-analyzer, security-auditor, reliability-auditor, and more. Each reads the cluster independently before it synthesizes one prioritized report.

**The safety model**

The agent can read the entire cluster but change nothing on its own. Every write (scaling a deployment, restarting a rollout, patching an HPA) lives inside a single change-executor subagent, and each write tool is gated by a human-in-the-loop (HITL) interrupt. The agent proposes a remediation, a person approves, rejects, or edits, right from a Slack message. Read is autonomous and writing is always gated through HITL. It’s enforced structurally and mirrored by in-cluster RBAC (cluster-wide read, tightly scoped write).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7360fed14e0b1304caaf08_Agent%20architecture%20diagram%402x.png)SRE Agent Architecture

## Part 3: How We Built It (and Why)

Each choice below was a fork where the obvious path and the right path diverged.

- **Deep Agents, not a raw loop. **We build on [Deep Agents](../deepagents/overview.md) (create_deep_agent()) over LangGraph, which gives us a planning loop (write_todos), first-class subagents, and built-in HITL interrupts out of the box, all things we'd otherwise need to hand-build. Our rule of thumb is to reach for the highest-level framework that doesn't fight you on the workflow you need to build.
- **Narrow subagents, not one omniscient prompt. **Specialist agents each own a slice of the cluster, which buys parallelism, tighter context (fewer hallucinations), and the option to run well-scoped tasks on a cheaper model.
- **Sonnet where it thinks and Haiku for scale. **The synthesizing orchestrator runs on Claude Sonnet; the read-only subagents and the scheduled check run on Claude Haiku. Pay for intelligence only where it's needed.
- **The scheduler bypasses the agent. **It used to run the full orchestrator (~20 model calls) just to confirm "all healthy." Now it collects state in plain Python and makes one Haiku call. This approach achieves a 95 to 99% cost cut per check with no loss in catching issues. We reserve full power for on-demand investigations.
- ** Give the human an approval they can actually read. **The changes that are proposed need to be clear in all the components they affect. Scaling a deployment to 3 is legible in a glance; a helm upgrade is one click that rewrites dozens of resources you can't see from the approval prompt. So we kept write tools narrow and legible and deliberately withheld coarse, high-blast-radius ones, even useful ones. This gate protects production only when the human can truly judge what they're approving.
- **The read/write split is structural. **Read and write tools live in separate modules, and write tools exist only inside the change-executor subagent behind an interrupt gate. The orchestrator literally can't access a write tool. In-cluster RBAC mirrors the same split.
- **Runs anywhere, no public ingress. **The Kubernetes client auto-detects in-cluster vs. local (no kubectl binary in the image), and Slack runs over Socket Mode, an outbound WebSocket, so approvals flow with no inbound endpoint to expose. The container is non-root with a read-only root filesystem.

The through-line in our architecture is to keep things as simple and cost-effective as possible. We spend tokens, model power, and increase network surface only where it improves agent outcomes for the infrastructure we’re managing. That's what makes the agent cheap enough to run every few minutes and safe enough to point at production.

## Part 4: How LangSmith Helps Us Debug and Improve the Agent

Every decision in Part 2 runs as a LangSmith trace: the scheduled Haiku check, each subagent investigation, every read and proposed write. The Deep Agents and LangGraph pieces trace automatically; the scheduler's direct Anthropic calls are wrapped with @traceable.

### What the traces caught

- **The ~20-call scheduled check was llm waste. **The scheduler redesign in Part 2 started with an investigation into the LangSmith per-run cost breakdown. We saw that checks coming back "all healthy" were quietly fanning out to ~20 Sonnet calls across subagents. Seeing the tokens and dollars per run pointed us toward the one-Haiku-call rewrite that cut costs 95 to 99%.
- **A** **runaway loop is obvious from the trace**. We'd watched another agent get stuck calling its filesystem grep/read_file tools in a tight loop and burn ~$5 before anyone noticed. In the trace, the same tool call was stacking up dozens of times down a single run. This told us to cap it, so the bot now runs under hard recursion, model-call, per-tool limits, and prompt caching on top.
- **A false positive showed up as a pattern. **The scaling-analyzer kept flagging intentionally single-replica services as CRITICAL. The trace shows the exact snapshot the subagent saw and the reasoning that got there. It provides a view across all namespaces at once, so we were able to fix the behavior with a prompt change tied to direct evidence.
- **Every HITL edit is graded data. **The approve/edit/reject from Part 1's safety model attaches as feedback on that run. "Proposed 10 replicas; human edited to 4" is a labeled example on the highest-stakes call the agent makes. Every interaction with the agent is signal on the trace we can use to improve the agent and its recommendations.

### From those findings to a regression suite

Those labeled runs form the backbone of our evaluations. A misclassified pod or a missed OOM gets promoted into a LangSmith dataset with the correct answer attached, and every prompt or model tweak then runs against it with LLM-as-judge and code-based evaluators, so a change that regresses shows up as a red number and doesn't merge. The single-replica false positive above becomes a permanent test case for our eval suite.

### LangSmith Engine: running that loop for us

The improvement loop above still relies on a human noticing undesirable behavior, finding the trace, and promoting it to a dataset. It’s time intensive for whoever maintains the agent. [LangSmith Engine](../langsmith/engine-overview.md) automates this manual work. It's like a proactive agent engineer that watches our tracing project in three stages.

- Detect: it clusters related traces into ranked issues (e.g. "the scaling-analyzer flags intentionally single-replica services as CRITICAL across six namespaces" as one issue, not forty traces), and it does this reading our traces under zero data retention, so they never train anyone's model.
- Fix: it summarizes the failure, writes the prompt or code change, and opens it as a GitHub PR with a diff and explanation.
- Prevent: it suggests online evaluators and dataset examples so the regression can't return.

Engine has grouped our traces into open issues we had not filed ourselves. One example is that the scheduled health check was collecting no utilization data at all. The collector queried nodes, pods, warning events, HPAs, and deployments, and the analysis step was a single forced-tool call with no tools available, so the model couldn’t fetch what the collector skipped. Every hourly report raised a capacity question it structurally could not answer and handed it back to us as a recommended action like "check pod CPU/memory metrics". The kubectl_top_pods and kubectl_top_nodes capability was already in the repo for the interactive agent and had never been wired into the scheduled path. Engine proposed wiring pod and node metrics into the collector, reusing the existing unit parsing rather than inventing new logic, and scoped the change to the collector so the analysis prompt and the zero-token property stay untouched. It arrived as a pull request that was reviewed, added as an example to our dataset, tested against our dataset to prevent regressions and prove the fix worked, and then merged.

## Part 5: What’s Next

We will continue to use SRE Agent internally and have begun rolling this out to some current LangSmith customers. We’re actively working to develop it and expand its capabilities for Kubernetes and other parts of the stack. Some of the next improvements will be making the state durable for HITL, and making the monitoring loop stateful so it has memory of the recent incidents reported. It is open source and available here. [https://github.com/langchain-samples/sre-agent](https://github.com/langchain-samples/sre-agent) . Feel free to try it out, contribute, or provide feedback.
