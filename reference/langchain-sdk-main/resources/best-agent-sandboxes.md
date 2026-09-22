---
title: "The 6 Best AI Agent Sandboxes for Isolated Code Execution"
description: "Compare six AI agent sandboxes by isolation, credentials, egress, state, deployment model, and lifecycle cost."
source: "https://www.langchain.com/resources/best-agent-sandboxes"
category: "resources"
author: "LangChain"
tags: [resources, best-agent-sandboxes]
---

# The 6 Best AI Agent Sandboxes for Isolated Code Execution

## The 6 Best AI Agent Sandboxes for Isolated Code Execution

The best agent sandbox for a workload depends on four boundaries: what authority the code receives, where credentials and network policy live, what survives between runs, and who manages the sandbox infrastructure.

Teams usually choose between two common deployment patterns. Some run the entire agent inside a remote environment with a shell, filesystem, and long-running workspace. Others keep the agent in their application and provision a sandbox only when it needs to execute code, render a page, or validate an answer.

We built[LangSmith Sandboxes](https://www.langchain.com/langsmith/sandboxes) and publish and maintain this guide. [LangSmith is a framework-agnostic agent engineering platform](https://www.langchain.com/langsmith-platform), so teams using LangSmith can use any framework or model and bring their own cloud or sandbox.

### 6 AI agent sandboxes at a glance

Use this table to shortlist two or three tools. The sections below compare security controls, deployment, and pricing.

| Tool | Best fit | Runtime and persistence | Main tradeoff |
| --- | --- | --- | --- |
| LangSmith Sandboxes | Full-root workspaces with brokered credentials | MicroVM; filesystem snapshots; REST-only memory snapshots | Web egress is open until restricted |
| E2B | Code interpretation and computer use | Firecracker microVM; pause and resume; memory and filesystem snapshots | Creating a snapshot interrupts active streams |
| Daytona | Multiple runtimes and deployment models | Containers, VMs, and GPUs; snapshots and volumes | Persistence and storage costs vary by sandbox type |
| Blaxel | Long-running agents that enter standby | Lightweight VM; standby preserves the filesystem, memory, and running processes | Outbound proxy remains in public preview |
| Modal | Sandboxed jobs in serverless CPU or GPU apps | gVisor container; snapshots and persistent volumes | Secrets become readable environment variables |
| Vercel Sandbox | Privileged execution with filesystem persistence | Firecracker microVM; filesystem snapshots | Memory bills for the full session |

### Selection criteria

To make the cut, a product needed a documented API or SDK for creating isolated environments and enough public information to evaluate runtime authority, network egress and credential handling, state after an idle, stop, pause, or standby event, and who manages the sandbox infrastructure.

That scope excludes local container libraries, general-purpose VM providers, CI runners, and browser-only automation. Those tools can be part of an agent execution stack, but the buyer must build out more of the sandbox management layer, including provisioning, state management, network controls, and cleanup.

### Which agent sandbox should you choose?

**LangSmith Sandboxes:** Best when the workload needs full-root authority, credentials brokered outside the sandbox, configurable egress controls, reusable filesystem snapshots, and opt-in memory capture.

**E2B:** Best for a standalone code-interpreter or computer-use platform, pause and resume, and managed BYOC through its Enterprise offering.

**Daytona:** Best when you need containers, Linux or Windows VMs, GPUs, dedicated regions, or customer-managed compute.

**Blaxel:** Best for an agent that should enter standby and retain its processes and filesystem.

**Modal:** Best when sandboxed execution is one stage in a broader serverless CPU or GPU application.

**Vercel Sandbox:** Best for privileged Firecracker environments with stop-to-snapshot persistence, especially alongside Vercel applications.

### Four questions to answer before you choose

#### What authority does the code receive?

[Private data, untrusted content, and external communication](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/) form a dangerous combination. Know what the agent can read, which processes it can start, whether it runs with root/admin privileges (or as a locked-down, non-privileged user), and what sits beyond the network boundary.

#### Where do credentials and network policy live?

Environment variables are readable by code inside the sandbox. A credential broker can keep the real secret outside the guest and inject it only for an approved request. Output checks alone cannot protect a secret that untrusted code can read and send elsewhere. Keep credentials outside the sandbox where possible, and restrict egress to approved destinations.

#### What must survive?

A running workspace, a restored filesystem, a memory snapshot, and an external volume preserve different things. Because files may survive when processes or connections don't, write down whether the task needs installed packages, live processes, sockets, or shared data after an idle or stop event.

#### Who manages the sandbox infrastructure?

Estimate the total cost and operational work required to run the sandbox, not just its active compute rate. Include image builds, idle compute and memory, snapshots, storage retention, concurrency, and the engineering time to configure, monitor, secure, and troubleshoot the environment. Then choose the operating model that fits your residency requirements and incident-response capacity: managed SaaS, a dedicated region, BYOC, or self-hosting.

### Estimate costs for ephemeral and stateful workloads

Ephemeral tool calls and stateful coding sessions produce different bills. Price both before comparing vendors, then record any plan minimums and image-build charges. Those inputs still do not capture every line item. Add egress and concurrency charges that sit outside the usage estimate.

**Pricing scenarios for sandbox evaluation**

| Input | Ephemeral tool execution | Stateful coding agent |
| --- | --- | --- |
| Monthly volume | 10,000 jobs | 500 sessions |
| Active runtime | Two minutes per job | Three 15-minute active windows |
| Paused or idle time | None | Two three-hour pauses between active windows |
| Resources | 2 vCPU and 4 GiB | 2 vCPU and 8 GiB |
| State | Deleted after each job | 5 GiB retained for seven days after the final stop |
| Resume requirement | None | Files and installed packages return; record whether processes and sockets survive |
| Lifecycle | Create, run, and delete | Run, pause, resume twice, stop compute, and retain state |
| Peak concurrency | 100 jobs | 25 sessions |

The ephemeral workload exposes startup overhead, minimum billing increments, and concurrency limits. The stateful workload exposes idle-memory charges, snapshot and volume costs, and whether a resume restores files, memory, or live processes.

Record the plan, including concurrency, infrastructure charges, and storage retention. Also include the cost of any supporting services the workload needs, such as persistent storage, a database, or an orchestration layer. Exclude any plan that cannot meet the workload's persistence or deployment requirements.

## Comparing agent sandbox options

The sections below compare each product on runtime authority, credential and egress controls, persistence, and infrastructure ownership.

### LangSmith Sandboxes: Best for full-root workspaces with brokered credentials

We built[LangSmith Sandboxes](https://www.langchain.com/langsmith/sandboxes) to work any framework or custom code, including with [Deep Agents](https://www.langchain.com/deep-agents), [LangGraph](https://www.langchain.com/langgraph), and the [LangChain framework](https://www.langchain.com/langchain), so teams can keep their existing agent framework and use the models they already run. Use them for workloads that need a full-root environment with built-in credential brokering, reusable filesystem snapshots, and opt-in memory capture.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a0209c52694d59e5e59b3e3_sandboxes-2%20(1).png)

#### How it works

Each sandbox runs in a dedicated microVM with root access, so an agent can install packages, run Docker, start a web server, or use the machine like a Linux development environment without sharing a kernel with your application or another sandbox. Prewarming keeps p50 start latency under one second, and a single SDK call can launch sandboxes in parallel.

An agent can run inside the sandbox, or an application can create one as a tool for a bounded task.[Configurable idle-stop and post-stop deletion timers](../langsmith/sandbox-sdk.md) control idle compute and retained state. Sandboxes stop automatically after a configurable idle period, 10 minutes by default, which ends compute and memory metering for a workspace left waiting.

By default, SDK and CLI snapshots preserve the persistent filesystem, including installed packages, files you wrote, and temporary files stored in /tmp. Running processes, open sockets, and in-memory state don't carry over, and /dev/shm is the only filesystem path not preserved. The REST capture endpoint can also[include full VM memory](../langsmith/smith-api/sandboxes/capture-a-snapshot-from-a-sandbox.md) when the sandbox is running, then warm-restore a new sandbox from that state. Snapshots can be forked to explore parallel branches. For data that has to outlive the sandbox, [S3, GCS, and public Git repository mounts](../langsmith/sandbox-mounts.md) attach external storage to the filesystem directly. Authenticated service URLs and TCP tunnels let you preview a generated application or connect to a service the agent starts.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a0209a49904bd86527f61da_sandboxes-1%20(1).png)

#### Security boundary

The[auth proxy](../langsmith/sandbox-auth-proxy.md) keeps approved credentials outside the guest and injects headers only when outbound requests match configured hosts and paths. Static workspace secrets work for fixed service accounts, and callbacks resolve short-lived or user-scoped credentials. Separate access-control rules govern allowed hosts and raw TCP ports. By default, each sandbox is private to the person who created it. Other workspace members can run commands in that sandbox only if their workspace role includes the [sandboxes:exec permission](../langsmith/sandbox-permissions.md). This lets teams control who can inspect or troubleshoot a sandbox created by someone else.

Secret isolation doesn't make an approved API call least-privileged. A least-privilege setup still requires narrow service scopes or user-scoped callbacks, along with controls that keep an agent from using an approved connection to reach an unauthorized destination.

HTTP and HTTPS can reach any host until you set access controls, but other raw TCP destinations are blocked by default. Adding an allow list makes outbound access default-deny, including web traffic. Teams handling private code or data should make that policy a required part of the sandbox template.

#### Deployment and pricing

**Deployment**

- **LangSmith Cloud:** Generally available in GCP US, GCP EU, GCP APAC, and AWS US
- **Bring your own cloud (BYOC):** Available for customer-managed deployments on the Enterprise plan
- **Self-hosted:** Available on EKS or GKE with the Enterprise plan; AKS is available by request
- Sandboxes can be created and managed through the Python and TypeScript SDKs or the CLI.

**Compliance:** LangSmith is[SOC 2 Type II certified, ISO 27001:2022 certified, HIPAA compliant, and GDPR compliant](https://trust.langchain.com/).

**Pricing**

**Usage rates**

All usage is[billed per second](https://www.langchain.com/pricing). At published rates:

- **Compute:** about $0.0576 per vCPU-hour
- **Memory:** about $0.01845 per GiB-hour
- **Storage:** about $0.000123 per GiB-hour

**Plans**

- **Developer:** Free; includes $7.50 in compute and memory credit and $1 in storage credit each month; limited to 10 sandboxes
- **Plus:** $39 per seat; includes the same monthly credits
- **Enterprise:** Custom pricing

**When a sandbox goes idle**

A sandbox can stop automatically after a configurable period of inactivity. This ends compute and memory billing, but its retained filesystem continues to incur storage charges until it is deleted.

#### Limitations

[Sandboxes provide root access](https://www.langchain.com/langsmith/sandboxes), including Docker. If your execution policy prohibits root inside the guest, use a more restricted runtime.

Regulated teams should inventory where code, prompts, artifacts, logs, lifecycle metadata, and support access reside before approving the managed boundary.

A standard SDK or CLI snapshot restores the filesystem, not live processes, open sockets, or in-memory state. Use the REST memory capture endpoint when a warm restore is required.

### E2B: Best for standalone code interpretation and computer use

#### How it works

E2B's Firecracker microVMs support code interpretation, computer use, long-running sessions, and reusable environment templates. The[LangChain E2B package](https://docs.e2b.dev/agents/deep-agents) provides a Deep Agents backend that sends filesystem and shell tools to E2B instead of the developer machine.

Templates serialize the filesystem and running processes after setup, so a sandbox created from a template starts with its processes already running; E2B advertises same-region sandbox starts of 80 ms.[Snapshots capture memory and filesystem state](https://docs.e2b.dev/sandbox/snapshots) and can create new sandboxes from one point in time. Pause and resume restore the same sandbox, while snapshots let an agent branch a coding task or launch parallel rollouts from a prepared browser session.

#### Security boundary

Outbound internet access is enabled by default. E2B can disable it or restrict destinations by IP, CIDR, and hostname rules.

E2B’s[public-beta per-host request transforms](https://docs.e2b.dev/network/internet-access) let its egress proxy add headers to requests for a named service. When configured with workload identity, currently in private beta, the proxy can attach a short-lived token without exposing its value to code inside the sandbox. A transform does not grant network access by itself: the service must also be in the egress allow list, so the rule cannot bypass the outbound policy.

#### Deployment and pricing

**Deployment:** E2B Cloud operates the control plane. E2B’s[managed BYOC offering](https://docs.e2b.dev/byoc), sold through its Enterprise offering, places templates, snapshots, and runtime logs inside a customer's AWS or GCP VPC. However, anonymized system metrics still go to E2B Cloud, and the BYOC autoscaler does not yet add orchestrator nodes automatically. Teams can also [self-host E2B](https://github.com/e2b-dev/e2b) if they are prepared to operate the control plane themselves.

**Pricing**

E2B combines plan limits with separate usage charges.[Compute and memory are billed per second](https://e2b.dev/pricing).

**Usage rates**

- **Compute:** $0.0504 per vCPU-hour. The default 2-vCPU sandbox costs $0.1008 per hour; 4 vCPU costs $0.2016 per hour.
- **Memory:** $0.0162 per GiB-hour.

**Plans**

- **Hobby:** $0 base price plus usage; includes a one-time $100 usage credit, 20 concurrent sandboxes, and a 10 GiB maximum disk size
- **Pro:** $150 per month plus usage; 100 concurrent sandboxes and a 20+ GiB maximum disk size
- **Additional concurrency:** Paid add-ons can raise the limit to 1,100 concurrent sandboxes
- **Enterprise: **[$3,000 per month minimum](https://pricing.e2b.dev/)

#### Limitations

[Snapshot creation](https://docs.e2b.dev/sandbox/snapshots) briefly pauses the original sandbox and drops active command streams, WebSocket sessions, and PTYs. This means a snapshot is not a seamless checkpoint during an interactive coding or computer-use session: the client must reconnect and resume work afterward.

[Auto-resume](https://docs.e2b.dev/sandbox/auto-resume) only works with memory-retaining pause behavior.

Managed BYOC keeps E2B responsible for the control plane. Self-hosting shifts running and maintaining that control plane to your team.

### Daytona: Best for multiple runtime classes and deployment models

#### How it works

By default, a newly created Daytona sandbox runs as a Linux container. Containers use process and network namespaces plus filesystem and IPC isolation, and Daytona reserves vCPU, RAM, and disk for each sandbox. Teams can instead choose a dedicated Linux VM, Windows VM, or GPU sandbox when the workload needs a different operating system or hardware boundary.

Python and TypeScript SDKs sit alongside Ruby, Go, and Java support. The platform also provides a CLI and dashboard, an MCP server, a REST API, and SSH.

Snapshots can start from a Dockerfile or OCI image, or capture an existing sandbox. Container captures preserve the filesystem, and VM captures can include memory. For data that must outlive the sandbox,[S3-backed FUSE volumes](https://www.daytona.io/docs/en/volumes/) can mount into multiple environments and isolate tenants by subpath.

#### Security boundary

Daytona Secrets place a non-secret placeholder in a sandbox environment variable instead of the plaintext credential. When code sends that placeholder in an HTTPS request header to a host allowed for that secret, Daytona’s outbound proxy replaces it with the real value. The code can authenticate to the approved service without being able to read the credential itself. Network policy supports domain and CIDR allow lists or a full outbound block. Lower account tiers can't override organization-level restrictions for an individual sandbox.

#### Deployment and pricing

**Deployment:** In Daytona’s shared US and EU regions, sandboxes run on compute shared with other organizations, while Daytona handles provisioning, maintenance, monitoring, and scaling. Dedicated regions reserve Daytona-managed infrastructure for one organization. Custom regions run on compute that the customer provides and manages, giving the customer control over locality, compliance, and capacity.

**Pricing:**[** **Daytona charges](https://www.daytona.io/pricing) $0.0504 per vCPU-hour, $0.0162 per GiB-hour of memory, and $0.000108 per GiB-hour of storage after the first 5 GiB.

Stopped and paused sandboxes still incur reserved disk charges, and archiving a container sandbox releases those charges. Ephemeral and GPU sandboxes are deleted when stopped.

#### Limitations

Whether an individual sandbox can have its own outbound-network policy depends on the Daytona account tier. Teams that need to give a sensitive agent a separate domain or IP allow list, or block its internet access entirely, should confirm that their account tier supports per-sandbox network controls.

[Dedicated regions](https://www.daytona.io/docs/en/regions/) require contacting Daytona sales, and custom regions require attaching your own compute.

A non-ephemeral container sandbox keeps its filesystem after it stops, so Daytona continues to charge for its reserved disk. Daytona can archive container sandboxes only, moving the filesystem to object storage and restoring the files when the sandbox starts again. Ephemeral sandboxes and GPU sandboxes are deleted on stop, so use a volume or snapshot for anything the workload needs to keep.

### Blaxel: Best for long-running agents that enter standby

#### How it works

Blaxel's lightweight VMs enter standby after inactivity, preserve the filesystem and running processes, and[resume in under 25 ms](https://docs.blaxel.ai/Sandboxes/Overview). Blaxel's guidance is to [treat sandboxes as persistent computers](https://docs.blaxel.ai/Sandboxes/best-practices) and let them suspend when idle rather than destroying them after each task, and for workloads that do churn sandboxes it documents a pool pattern that provisions replacements in the background.

By default, files written inside a Blaxel sandbox use RAM. Teams that install large packages, run builds, or create large temporary artifacts can add disk-backed root storage instead of increasing the sandbox’s memory allocation. Use a volume when data must outlive the sandbox.

Blaxel provides TypeScript, Python, and Go SDKs, plus a REST API, CLI, Console, and MCP server. Teams can use any of those tools to create a sandbox from a prebuilt or custom image and set its memory, root storage, ports, labels, and region.

#### Security boundary

The[outbound proxy](https://docs.blaxel.ai/Sandboxes/Proxy) can inject write-only, encrypted secrets and restrict domains without placing the credential in the sandbox. The proxy is in public preview and isn't yet recommended for production. Rules and secrets can change after a proxy-enabled sandbox starts, but enabling or disabling the proxy requires a new sandbox.

#### Deployment and pricing

**Deployment:** Sandboxes deploy to a single region. You can pin a region at creation or let Blaxel select a default, subject to deployment policies. Blaxel holds SOC 2 Type II and ISO 27001 certifications. HIPAA support with a signed BAA is available as a[$250 per month add-on](https://blaxel.ai/pricing). Private network connectivity and connecting servers from your own infrastructure are available on a Custom plan.

**Pricing:** Standby stops compute charges, but snapshot and volume storage continue to bill. Lower quota tiers enforce TTLs, while higher tiers have no configured maximum lifetime. Under[Blaxel's usage rates](https://blaxel.ai/pricing), active compute costs $0.0000115 per GB of RAM per second, snapshot storage costs $0.20 per GB-month, images cost $0.045 per GB-month, and volumes cost $0.12 per GB-month.

#### Limitations

Standby preserves the sandbox’s files and processes, but not live connections to databases, queues, or external services. When the sandbox resumes, the application must reconnect before making its next request to those services. This matters for agents that depend on persistent database sessions, queue consumers, or long-lived HTTP connections.

Blaxel’s[outbound proxy](https://docs.blaxel.ai/Sandboxes/Proxy) routes sandbox traffic through a service that can inject secrets into approved requests and restrict which external domains sandbox code can reach. Because it is in public preview and isn't recommended for production, a team should not make it the required credential or egress control for a production workload.

The proxy is part of the sandbox’s initial setup, not a setting that can be changed in place. If a team later needs proxy-based credential handling or domain restrictions, or decides to remove them, it must create a new sandbox, so choose that security boundary before provisioning a long-lived workspace.

### Modal: Best for sandboxes inside a serverless application

#### How it works

Modal treats a sandbox as a runtime component of a Modal application, rather than a standalone agent workspace. An application can create one on demand to run untrusted or model-generated code, test a repository, or use an isolated environment with arbitrary dependencies. Standard sandboxes use gVisor, a container isolation layer rather than a full virtual machine with its own Linux kernel. Because sandboxes use the same Images, Volumes, and resource configuration as other Modal components, they fit best when code execution is one step in a broader Modal application.

Modal also offers a beta VM Sandbox for workloads such as Docker that need a real Linux kernel.

Modal supports filesystem snapshots, plus directory snapshots, and memory snapshots through an[experimental API](https://modal.com/docs/guide/sandbox-snapshots). Modal Volumes provide persistent mounted storage, with background commits every few seconds and a final commit on container shutdown.

#### Security boundary

The default sandbox can't accept inbound connections or access other Modal workspace resources. By default, code inside a Modal sandbox can send requests to any public IP address. The application that creates the sandbox can instead block all internet access, allow only specified IP ranges, or, in beta, allow only specified HTTPS domains on port 443. For an agent that runs untrusted code, the important point is that outbound access is open until the application explicitly restricts it.

Modal Secrets are passed to the sandbox as environment variables, which means code running inside the sandbox can read their plaintext values. If that code is untrusted or model-generated and the sandbox has public outbound access, it could send a secret to an external destination. For that combination of private credentials, untrusted code, and public egress, restrict one of those capabilities or use a credential broker that keeps the real secret outside the sandbox.

#### Deployment and pricing

**Deployment:** Modal runs sandbox containers across multiple clouds and offers a choice of regions worldwide. Teams can place a sandbox near users or an external database when latency matters. Choosing a specific region increases usage costs, so confirm availability and pricing before committing to a location-sensitive workload.

**Pricing:** Modal bills sandbox CPU and memory by the second. At published Sandbox and Notebooks rates, CPU costs $0.00003942 per physical core-second, where a physical core is two vCPUs with a minimum of 0.125 cores per container, and memory costs $0.00000667 per GiB-second; GPUs use Modal’s standard rates.

**Regional pricing:** Choosing a region increases the base price by 1.5x for a broad region or 1.75x for a narrower one.

#### Limitations

[Modal Secrets](https://modal.com/docs/guide/secrets) are environment variables, and[outbound access](https://modal.com/docs/guide/sandbox-networking) starts open, so users should not pair long-lived credentials with untrusted or model-generated code without restricting network access.

The beta[VM Sandbox](https://modal.com/docs/guide/vm-sandboxes) provides a real Linux kernel for Docker-style work, but it does not support GPUs or runtime Volume reloads, and VM memory snapshots are limited to customers Modal has enabled.

Taking a memory snapshot terminates the current sandbox and closes open TCP connections. You cannot take one while a `Sandbox.exec` command is running, and background processes launched through `Sandbox.exec` do not restore reliably.

Filesystem and directory snapshots are retained for 30 days by default, while memory snapshots expire after seven days and cannot currently be extended.

### Vercel Sandbox: Best for privileged execution on filesystem snapshots

#### How it works

Vercel Sandbox gives each task an isolated Linux environment with its own files and network access. Its JavaScript, TypeScript, and Python SDKs manage a general Linux runtime that can run arbitrary compatible languages and command-line tools. An agent can install software, run Docker, or work in a customized development environment. Teams can start with Vercel’s managed setup or use their own Linux image when a workload needs specific tools or configuration.

Vercel separates the named sandbox from a running session. When a session stops, Vercel snapshots the filesystem. Resuming starts a new VM from that state and reapplies the configuration. Snapshots include files and installed packages, expire after 30 days without use by default, and can give way to[Vercel Drives](https://vercel.com/docs/sandbox/concepts/drives), a private beta on Pro and Enterprise plans, when data must outlive a sandbox or be reused across sandbox runs.

#### Security boundary

Vercel's firewall can forward selected HTTPS requests to a customer proxy and match on path, method, query, or headers.[Outbound access starts at an allow-all default](https://vercel.com/docs/sandbox/concepts/firewall) that reaches the public internet, and a deny-all or user-defined policy can narrow it. Teams that need this as a security boundary should verify the allowed destinations, failure behavior, and audit trail in their own account before launch.

#### Deployment and pricing

**Deployment:** Vercel Sandbox is available in `iad1` in Washington, D.C., `sfo1` in San Francisco, `cle1` in Cleveland, and `cdg1` in Paris. `iad1` is the default. Pro and Enterprise teams can configure failover regions. Teams with latency or data-residency requirements should confirm which location and prices fit their needs. You can use Vercel Sandbox even if the rest of your application is not hosted on Vercel.

**Pricing:** Vercel bills CPU, memory, data transfer, and snapshot storage separately. The default timeout is five minutes. You can configure a session for up to 45 minutes on Hobby and 24 hours on Pro or Enterprise.

CPU is charged only while code is working, but memory is charged for the full running session. An agent that spends long periods waiting on model or network responses may be cheaper to stop and resume than to keep a large sandbox running.

At the default `iad1` location, active CPU costs $0.128 per vCPU-hour and provisioned memory costs $0.0212 per GB-hour on paid plans. Snapshots preserve a sandbox’s files for 30 days without use by default, while network use and snapshot storage are billed separately.

#### Limitations

[Memory is billed for the full running session](https://vercel.com/kb/guide/vercel-sandbox-duration-and-persistence) even when CPU waits on a model or network call. This matters for agents that spend long periods waiting on model responses, database queries, or downloads: a large sandbox can keep adding to the bill even when it is doing little active work.

[Snapshots can't be moved between regions](https://vercel.com/docs/sandbox/concepts/regions#regions-and-snapshots), and a sandbox that mounts a drive must run in the drive's region. This makes location a long-term choice. Moving a persistent agent means starting a new sandbox and rebuilding its saved state. Teams should choose a region based on where data must stay before building a long-lived workflow.

A[resumed named sandbox](https://vercel.com/kb/guide/vercel-sandbox-duration-and-persistence) starts a new VM from a filesystem snapshot and doesn't preserve live processes or sockets. Files and installed packages return, but running commands and connections do not. An agent that needs a background task, server, or database connection to stay alive must restart it after every resume.

### How to evaluate agent sandboxes for a production workload

Feature comparisons can narrow the field, but the final choice should be tested with the same production-shaped task in each shortlisted sandbox. The task should reflect the permissions, external services, runtime, and state the agent will actually need.

The evaluation should cover the full lifecycle. That includes creating the environment, installing dependencies, connecting to an approved service, confirming that an unauthorized destination is blocked, writing a file, stopping or pausing the sandbox, and then resuming it. Teams should record what happens to files, processes, and connections, along with startup time, idle charges, storage costs, and the work required to configure and operate each option.

The best fit is the sandbox that meets the workload’s security, persistence, deployment, and cost requirements without adding more operational complexity than the team can support.

Teams can[create a LangSmith Sandbox](https://smith.langchain.com/) and run the same production-shaped test through the [Python or TypeScript SDK](../langsmith/sandbox-sdk.md) or [Sandbox CLI](../langsmith/sandbox-cli.md). This makes it possible to compare LangSmith’s security controls, persistence behavior, and lifecycle costs against every other option.
