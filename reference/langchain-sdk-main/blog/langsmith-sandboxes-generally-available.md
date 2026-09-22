---
title: "LangSmith Sandboxes are Generally Available"
description: "Run AI agents safely with LangSmith Sandboxes (GA): kernel-isolated microVMs with snapshots, parallel forks, service URLs, and auth proxies. Built for coding agents, CI agents, and data pipelines"
source: "https://www.langchain.com/blog/langsmith-sandboxes-generally-available"
category: "blog"
published: "2026-05-13T17:36:00.000Z"
author: "LangChain Accounts"
tags: [blog, langsmith-sandboxes-generally-available]
---

# LangSmith Sandboxes are Generally Available

- **LangSmith Sandboxes are now GA** — Each sandbox runs as a hardware-virtualized microVM, fully kernel-isolated from your services and other sandboxes, making them genuinely secure for running untrusted, model-generated code, something containers alone can't guarantee.
- ‍**Agents need real isolation, not just "sandbox" features** — Real-world supply chain attacks and kernel exploits (like the Shai-Hulud npm worm and Copy Fail CVE) show that running agent code in containers or eval boundaries is dangerously insufficient for production workloads.
- ‍**GA ships powerful new primitives for agent workflows** — Snapshots and cheap copy-on-write forks, Blueprints for pre-warmed environments, Service URLs, a Sandbox CLI, and an Auth Proxy make LangSmith Sandboxes a full execution platform.
