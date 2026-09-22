---
title: "Connections: Managed credentials and per-caller identity for Managed Deep Agents"
description: "Learn how Connections in Managed Deep Agents securely manage credentials, support per-user OAuth, and let agents act with each caller’s identity."
source: "https://www.langchain.com/blog/connections-managed-credentials-and-per-caller-identity-for-managed-deep-agents"
category: "blog"
published: "2026-09-09T20:05:00.000Z"
author: "LangChain Accounts"
tags: [blog, connections-managed-credentials-and-per-caller-identity-for-managed-deep-agents]
---

# Connections: Managed credentials and per-caller identity for Managed Deep Agents

- **Keep credentials out of your project.** A connection lives in your LangSmith workspace, not in `.env` and not in the build. Rotate or revoke it without touching code or redeploying.
- **Give each caller their own identity.** A user-owned connection resolves to whoever is asking, so the ticket your agent files carries their handle rather than a bot’s.
- **Skip the OAuth plumbing.** Managed Deep Agents runs the authorization round-trip. No callback route, no token store, no refresh logic, no consent screen in your project.

Connections are available now in Managed Deep Agents v0.7.0+.
