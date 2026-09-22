---
title: "What is an AI sandbox?"
description: "- An AI sandbox gives an agent an isolated workspace for running code and completing tasks while keeping host systems outside the execution boundary. - An agent needs a sandbox when it runs generated..."
source: "https://www.langchain.com/resources/what-is-an-ai-sandbox"
category: "resources"
published: "2026-09-07"
author: "LangChain"
tags: [resources, what-is-an-ai-sandbox]
---

# What is an AI sandbox?

## Key Takeaways

- An AI sandbox gives an agent an isolated workspace for running code and completing tasks while keeping host systems outside the execution boundary.
- An agent needs a sandbox when it runs generated code, especially when untrusted inputs can influence access to private data or external systems.
- A real sandbox requires more than a temporary directory or timed process. It combines filesystem and kernel isolation with controls for network access, compute, credentials, and retained state.
- A sandbox limits what a compromised agent can access or send, but it does not replace narrow tool permissions or human review for consequential actions.
- LangSmith Sandboxes make isolated execution part of deployment, so teams can manage sandbox policies alongside tracing, evals, and deployments through the same platform.

An AI sandbox is an isolated execution environment with its own filesystem, processes, network policy, and kernel boundary. It lets an agent install packages, run code, and create artifacts without inheriting access to the machine that launched it.

Agents can handle more complex tasks when they can read files, run code, and act on connected systems. That access becomes a security concern when untrusted content can steer an agent toward sensitive data or credentials.

We built[LangSmith Sandboxes](https://www.langchain.com/langsmith/sandboxes) to give agents [an isolated machine of their own](https://www.langchain.com/blog/give-your-ai-agent-its-own-computer), where they can install packages, run code, inspect the result, and continue working across a multi-step task without touching host infrastructure. This lets them test generated code, analyze data, or render a finished artifact within the same task. Engineers preparing an agent for production still need to decide when that execution capability is necessary and which controls belong around it. LangSmith Sandboxes is framework agnostic and can be used with any agents.

## The boundary between host and sandbox

Agent-generated code can be wrong, compromised, or redirected by untrusted input even when the surrounding application behaves as designed. Inside a sandbox, the agent gets a shell, files, package installation, and network calls while the host remains outside the boundary. That boundary should keep host files, secrets, and the systems that manage your infrastructure out of the agent’s reach. When a task needs a protected service, the application should grant only the limited access it requires.

Running code in a separate place does not make it a sandbox. The boundary has to stop that code from reaching the host. These controls can be part of a sandbox, but a temporary folder, time limit, or container alone is not enough. Containers separate processes but still share the host kernel. For agents that run untrusted code, a VM or microVM gives the sandbox a separate kernel. That helps prevent a flaw in agent-generated code or a vulnerable dependency from becoming direct access to the host. Filesystem, network, and resource limits then control what the agent can do inside that boundary. Wrong, compromised, or prompt-injected code can affect only the files, compute resources, and network destinations that the sandbox explicitly permits.

## Does your agent need a sandbox?

Simon Willison’s[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) describes the combination of agent capabilities that can let untrusted content steer an agent into sending private data outside your systems. An agent has the trifecta when it can access private data, process untrusted content, and communicate externally. Models can't reliably distinguish trusted instructions from hostile text once both enter the same context. A malicious page, email, repository, or tool response can then cause the agent to misuse its approved access, for example by reading private data or sending it outside your systems.

Meta’s[Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) says that, until systems can reliably detect and refuse prompt injection, an agent should not operate autonomously with all three of the following capabilities in the same session:

- Process content from untrusted sources
- Access private data or sensitive systems
- Change state or communicate externally

Under Meta’s guidance, an agent that combines all three capabilities requires human approval or another reliable validation step before it sends information or makes a change. Sandboxes are one way to apply Meta’s Rule of Two in practice. By withholding private files and preloaded browser sessions, then restricting network access, a sandbox can reduce an agent’s access to sensitive data and its ability to communicate externally. Sandboxing does not change the permissions an application gives the agent through tools, so consequential actions still need least privilege and review.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aa742827b55c753b195cba2_threat-path%20(1).png)

## The controls an AI sandbox needs

A sandbox only reduces risk when it can enforce its limits. Five core[sandbox properties](https://www.langchain.com/blog/how-to-choose-the-right-sandbox-for-your-agent) determine what an agent can access, where it can send data, how much compute it can use, what state it can retain, and whether its code can reach the host. Credential isolation adds another control for protected services.

### Filesystem isolation

Filesystem isolation keeps the host filesystem unreachable and exposes only task-specific files to the sandbox. Files move in and out only when the application explicitly allows it, keeping generated code from browsing or copying unrelated files.

### Network policy

Network policy controls where code in the sandbox can connect and what it can send. Instead of giving the sandbox open network access, a secure configuration permits only the specific websites, APIs, or internal services a task needs. It can also limit the kinds of requests and data the agent sends. Without those limits, prompt-injected code could send task data to an unapproved destination even if the host filesystem remains protected.

### Resource limits

Resource limits cap the CPU, memory, and running time available to a task. They keep a buggy or runaway script from running indefinitely, using too much memory, or creating too many processes. That prevents one task from consuming unbounded compute or disrupting other work.

### Sandbox reuse policy

Sandbox reuse policy determines how long a sandbox and its files persist. Ephemeral sandboxes give every task a fresh workspace, while persistent storage and snapshots let longer-running work resume. Reusing state is convenient, but it can also carry a compromised file or unwanted package into the next task. The policy defines when a sandbox is reused, reset, copied, or destroyed.

### Kernel isolation

Kernel isolation gives the sandbox its own kernel, the part of the operating system that controls direct access to the machine. Containers separate applications but still share the host’s kernel. If a vulnerability exists in that shared layer, it can potentially reach the host. VMs and microVMs avoid that risk by giving the sandbox a separate kernel.

### Credential isolation

When an agent needs to call a protected service without being allowed to read the credential that authorizes the call, credential isolation supports the filesystem and network controls above. The secret stays outside the sandbox, and a proxy attaches it only to approved outbound requests. This prevents agent-generated code from reading an API key from a file or environment variable. Destination, method, and credential permissions still need to remain narrow so the agent cannot misuse that access.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aa7429524ac5a67c5693ddd_sandbox-layers%20(1).png)

## What can agents do with a sandbox?

With the controls above in place, teams can let agents write and run code without executing it on a team member’s machine or production systems. A data analysis agent can install a library, analyze a dataset, and export a report. A research agent can browse and scrape sources, run analysis, and assemble its findings. Content pipelines can render finished artifacts. Teams can also use sandboxes to run evaluations or reinforcement learning tasks in parallel, with each run isolated from the others.

Snapshots save a prepared sandbox so teams do not have to reinstall the same dependencies for every run. Forks create independent copies of that starting point, allowing parallel runs without one changing another. The same saved state gives research and data agents a known checkpoint when a task needs to be retried.

At[monday.com](https://monday.com/), LangSmith Sandboxes power Sidekick, its built-in AI assistant for work. Sidekick can handle advanced tasks such as data analysis and multimedia generation, and the sandbox gives it a secure place to run the code those tasks require. [Omri Bruchim](https://www.langchain.com/blog/give-your-ai-agent-its-own-computer), AI Platform Group Manager at [monday.com](http://monday.com), described how secure sandboxes let Sidekick handle more advanced workflows:

“LangSmith Sandboxes are helping us make our Sidekick much more capable for[monday.com](http://monday.com) users. With secure environments, Sidekick can write and run code, and use the results to create richer workflows, like running data analysis and generating multimedia.”

## LangSmith Sandboxes in deployment

[LangSmith Sandboxes](https://www.langchain.com/blog/langsmith-sandboxes-generally-available) bring these controls into[LangSmith](https://www.langchain.com/langsmith-platform), our framework-agnostic agent engineering platform for observing, evaluating, and deploying agents. Teams manage the execution boundary as a deployment policy. Each sandbox runs in a dedicated microVM with its own filesystem and kernel, isolated from the underlying infrastructure and other sandboxes.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a0209c52694d59e5e59b3e3_sandboxes-2%20(1).png)

### Sandbox policies and credentials

Reusable snapshots capture a starting filesystem. Resource limits and network access are set on each sandbox at creation. For longer-running work, teams can restore a snapshot or fork it into independent sandboxes. Auth Proxy keeps credentials such as API keys outside the sandbox. When the agent calls an approved service, it adds the credential to the request without exposing it to the agent’s code. Destination, method, and credential permissions still need to remain narrow so the agent cannot misuse that access.

### Sandboxes in the agent development lifecycle

In production, sandboxing becomes a Deploy-phase policy in the[Agent Development Lifecycle (ADLC)](https://www.langchain.com/blog/the-agent-development-lifecycle), which moves through Build → Test → Deploy → Monitor. Deployment policy determines the sandbox, its input data, network access, state lifetime, and retained evidence. Those choices define the agent's production authority alongside its tool permissions.

Teams manage LangSmith Sandboxes through the same LangSmith SDK and authentication used across tracing, evals, and deployment. During an evaluation, the same SDK can create a separate sandbox for each test run. This lets teams run many test cases at once without the files or changes from one run affecting another.

For agents built on Deep Agents with a sandbox backend, LangSmith traces show which shell commands the agent ran inside the sandbox and how it used filesystem tools. LangSmith Cloud deployments send traces to a project named after the deployment, so a failed run stays visible alongside the rest of that deployment's history.

With a standalone sandbox, teams must carry identity and policy context across separate tracing, evals, and deployment systems. LangSmith keeps that context together under the same API and authentication surface.

## Keep agent code isolated in production

An agent that writes and runs code should have access only to the files, services, and compute its task requires. LangSmith Sandboxes let teams enforce those limits in production.[Explore LangSmith Sandboxes](https://www.langchain.com/langsmith/sandboxes) or [read the sandbox documentation](../langsmith/sandboxes.md) to get started.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a0209a49904bd86527f61da_sandboxes-1%20(1).png)

‍
