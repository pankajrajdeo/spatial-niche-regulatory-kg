---
title: "How Auth Proxy secures network access for LangSmith agent sandboxes"
description: "Agents need credentials and network access to do useful work, but those capabilities create new security risks. This post explains how Auth Proxy keeps secrets out of LangSmith Sandboxes runtimes..."
source: "https://www.langchain.com/blog/how-auth-proxy-secures-network-access-for-langsmith-agent-sandboxes"
category: "blog"
published: "2026-05-21T16:45:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-auth-proxy-secures-network-access-for-langsmith-agent-sandboxes]
---

# How Auth Proxy secures network access for LangSmith agent sandboxes

- Agent sandboxes need stronger network controls because agents can run code, install packages, call APIs, and follow instructions from untrusted content.
- LangSmith Auth Proxy keeps credentials outside the sandbox by injecting auth headers at the network layer, reducing exposure from prompt injection, logs, files, and malicious dependencies.
- Teams can define egress policies and dynamic credential flows so agents reach approved services, package registries, and user-scoped APIs without direct access to long-lived secrets.
