---
title: "LangSmith Sandboxes"
description: "Use LangSmith managed sandboxes to safely execute code and interact with the filesystem in isolated environments."
source: "https://docs.langchain.com/langsmith/sandboxes"
category: "docs"
tags: [docs, langsmith, sandboxes]
---

# LangSmith Sandboxes

> Use LangSmith managed sandboxes to safely execute code and interact with the filesystem in isolated environments.

Sandboxes are isolated environments that allow agents to safely execute potentially risky operations, like running arbitrary code or interacting with the filesystem, without affecting your main infrastructure.

From the [LangSmith homepage](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-sandboxes), select **Sandboxes** to manage all your sandbox resources.

<img src="https://mintcdn.com/langchain-5e9cc07a/5nd3ca6haxRbnJZj/images/langsmith/sandboxes/sb-overview.png?fit=max&auto=format&n=5nd3ca6haxRbnJZj&q=85&s=6c2848ea69c0a99cbdd0930ceb91daa5" alt="Sandboxes overview page" width="2846" height="1936" data-path="images/langsmith/sandboxes/sb-overview.png" />

## Environment availability

| Environment                                   | Status              |
| --------------------------------------------- | ------------------- |
| GCP US (`smith.langchain.com`)                | Generally available |
| GCP EU (`eu.smith.langchain.com`)             | Generally available |
| GCP APAC (`apac.smith.langchain.com`)         | Generally available |
| AWS US (`aws.smith.langchain.com`)            | Generally available |
| [BYOC](byoc.md) (your data plane URL) | Generally available |

> [!WARNING]
> On BYOC, use an API key that belongs to a BYOC workspace.

For self-hosted LangSmith deployments, see [Enable Sandboxes on self-hosted deployments](deploy-self-hosted-full-platform.md#enable-sandboxes).

## Network access

Restricted egress applies to non-Enterprise organizations by default and to organizations that request it. Organizations with an approved exemption can use unrestricted egress. Restricted sandboxes use a managed allowlist for common package registries, source repositories, and model APIs. LangSmith blocks destinations outside the allowlist, even if you add them to a sandbox's proxy configuration.

If you need unrestricted egress, [file a support ticket](https://support.langchain.com) with your organization or workspace ID, region, required destinations and ports, and use case. For more information, see [restricted egress and access requests](sandbox-auth-proxy.md#organization-level-restricted-egress).

## Get started

### 1. Install the SDK

**Python**

```bash
# uv
uv add "langsmith[sandbox]"

# pip
pip install "langsmith[sandbox]"
```

**TypeScript**

```bash
npm install langsmith
```

### 2. Set your API key

```bash
export LANGSMITH_API_KEY="<your-api-key>"
```

### 3. Create and run a sandbox

**Python**

```python
from langsmith.sandbox import SandboxClient

client = SandboxClient()

with client.sandbox() as sb:
    result = sb.run("python -c 'print(2 + 2)'")
    print(result.stdout)  # "4\n"
```

**TypeScript**

```ts
import { SandboxClient } from "langsmith/sandbox";

const client = new SandboxClient();
const sandbox = await client.createSandbox();
const result = await sandbox.run("node -e 'console.log(2 + 2)'");
console.log(result.stdout); // "4\n"
await sandbox.delete();
```

> [!TIP]
> Prefer the command line? The [Sandbox CLI](sandbox-cli.md) lets you create sandboxes, run commands, and open interactive shells without writing any code.

### 4. Use sandboxes with your agents

To wire sandboxes into agent code, see the Open Source docs:

* **Deep Agents**: [Use `LangSmithSandbox` as a backend](../integrations/sandboxes/langsmith.md), covering installation, backend creation, and cleanup.
* **Sandboxes as agent backends**: [Configure any sandbox as the execution backend](../deepagents/sandboxes.md) to give your agent `execute` and filesystem tools automatically.
* **LangChain / LangGraph integrations**: Use LangSmith sandboxes as a first-party option, or [connect third-party providers](../integrations/sandboxes.md) such as AgentCore, Daytona, E2B, Modal, Runloop, and Vercel.

## Resources

#### [Snapshots](sandbox-snapshots.md)
Build filesystem images from Docker images or capture a running sandbox, then boot sandboxes from them.

#### [Service URLs](sandbox-service-urls.md)
Access HTTP services running inside sandboxes via authenticated URLs.

#### [Auth proxy](sandbox-auth-proxy.md)
Inject credentials into outbound API requests without hardcoding secrets.

#### [Mounts](sandbox-mounts.md)
Attach S3 buckets, GCS buckets, and public Git repositories to a sandbox filesystem.

#### [Permissions](sandbox-permissions.md)
Control which workspace members can interact with a sandbox after it is created.

#### [CLI](sandbox-cli.md)
Build snapshots, manage sandboxes, open consoles, and tunnel TCP ports from the command line.

#### [SDK usage](sandbox-sdk.md)
Create and manage sandboxes programmatically with the Python or TypeScript SDK.

#### [Self-hosted setup](deploy-self-hosted-full-platform.md#enable-sandboxes)
Enable Sandboxes on self-hosted LangSmith deployments with Helm or Terraform.

#### [Harbor](harbor-integrations.md#sandboxes)
Run Harbor evaluations and rollouts on LangSmith sandboxes.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandboxes.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
