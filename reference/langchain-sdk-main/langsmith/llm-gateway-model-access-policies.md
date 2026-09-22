---
title: "Model access policies"
description: "Control which model providers and models are accessible through the LLM Gateway for your organization, workspaces, users, or API keys."
source: "https://docs.langchain.com/langsmith/llm-gateway-model-access-policies"
category: "docs"
tags: [docs, langsmith, llm-gateway-model-access-policies]
---

# Model access policies

> Control which model providers and models are accessible through the LLM Gateway for your organization, workspaces, users, or API keys.

> [!NOTE]
> The LLM Gateway is in [beta](release-stages.md).

A model access policy defines which providers and models are permitted through the [LLM Gateway](llm-gateway.md). The gateway blocks requests for providers or models the policy does not include, returning a `403` response. If no policy applies, all providers and models are available.

## Policy configuration

A model access policy lists one or more providers, each with an access mode:

* **All models**: Every model the provider offers is permitted.
* **Selected models**: Only the models you specify are permitted. At least one model is required.

> [!NOTE]
> Model access policies do not yet support custom model providers. While a model access policy applies to a request, the gateway blocks the `/providers/{configName}` and `/models/{configName}` routes.

## Scopes and overrides

A model access policy is scoped to one subject tier:

| Tier         | Applies to                                   |
| ------------ | -------------------------------------------- |
| Organization | All users and workspaces in the organization |
| Workspace    | All users in a workspace                     |
| User         | A single user                                |
| API key      | A single API key                             |

### Policy overrides

Policy overrides let you grant a more specific subject different access than the broader default. A common case is giving one API key access to a premium model that is not available to the rest of the organization.

When a request matches policies at multiple tiers, only the most specific tier applies, in the order API key, user, workspace, then organization. The more specific policy replaces the broader one entirely. For example, if the organization policy permits OpenAI and Anthropic, and an API key policy permits only OpenAI and Gemini, requests using that key can access OpenAI and Gemini only. If multiple policies match at the same tier, a model must be permitted by all of them to be accessible.

## Create a model access policy

> [!WARNING]
> Creating and managing policies requires `organization:manage` permission. For the full permissions breakdown, refer to [Traces, Engine, and access control](llm-gateway-access.md).

1. Go to **LLM Gateway** and select **Model Access**.
2. Click **Create model access**.
3. Enter a **Policy name**.
4. Select the scope under **Applies to** (organization, workspace, user, or API key).
5. Configure the **Allowed providers and models**.
6. Save.

Policies take effect immediately.

## Next steps

* [Spend policies](llm-gateway-spend-policies.md): set cost caps on LLM usage.
* [Rate limit policies](llm-gateway-rate-limit-policies.md): limit request or token throughput.
* [Per-customer policies](llm-gateway-header-policies.md): split a policy by a custom request header so each end customer gets its own allowance.
* [Data protection](llm-gateway-data-protection.md): add data protection policies.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-model-access-policies.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
