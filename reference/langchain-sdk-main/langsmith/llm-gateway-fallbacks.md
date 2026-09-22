---
title: "Model fallbacks"
description: "Automatically retry a request against backup models when the primary model rate-limits, errors, or returns another configured status code."
source: "https://docs.langchain.com/langsmith/llm-gateway-fallbacks"
category: "docs"
tags: [docs, langsmith, llm-gateway-fallbacks]
---

# Model fallbacks

> Automatically retry a request against backup models when the primary model rate-limits, errors, or returns another configured status code.

> [!NOTE]
> The LLM Gateway is in [beta](release-stages.md).

Model fallbacks retry a request against one or more backup models when the primary model returns a configured error, such as a rate limit or provider outage. Define the fallback order once in LangSmith, then continue using the standard LLM Gateway endpoint and model ID in your application.

## How it works

A fallback chain has:

* **A primary model**: the provider and model that trigger the chain when a request fails.
* **One to five fallbacks**: an ordered list of direct provider models or saved [model configurations](model-configurations.md).
* **Triggers**: the upstream HTTP status codes that move the request to the next model. For example, use `429` for rate limits, or `500`, `502`, `503`, and `504` for provider errors.

For each request, the gateway:

1. Calls the primary model selected by the request's provider-prefixed model ID.
2. If the request fails with a configured trigger status or a transport error, loads the matching fallback chain.
3. Calls each fallback in order until one succeeds, returns a status that does not trigger another fallback, or the chain is exhausted.
4. Returns the final response in the API format used by the client.

Fallbacks can use a different provider and API format than the primary model. The gateway translates requests and responses between [supported API formats](llm-gateway-api-formats.md), so an Anthropic primary can fall back to an OpenAI model without client-side changes.

Each attempt is traced and counted against [spend policies](llm-gateway-spend-policies.md) separately. A request that uses two fallbacks records three model calls: the primary attempt and two fallback attempts.

## Create a fallback chain

> [!WARNING]
> Creating and managing fallback chains requires `organization:manage` permission. For the full permissions breakdown, see [Access control](llm-gateway-access.md).

To create a fallback chain:

1. Go to **LLM Gateway** and select the **Model Fallbacks** tab.
2. Click **Create fallback chain**.
3. Select the **Workspace** where the chain applies.
4. Select the primary provider and model. Requests to this provider-prefixed model ID use the chain when the primary attempt fails.
5. Under **Fallbacks**, add one to five backup models in the order the gateway should try them. Choose a provider and model directly, select an existing model configuration, or create a custom model configuration.
6. Under **Configure fallback triggers (advanced)**, review the HTTP status codes that should trigger the next fallback. Add or remove status codes as needed.
7. Click **Create chain**.

A provider and model can have one fallback chain in each workspace. To change its behavior, edit the existing chain.

## Make a call

Call the standard LLM Gateway endpoint with the primary provider-prefixed model ID. You do not need a route-specific URL or additional request fields:

**Cloud**

```bash
curl https://gateway.smith.langchain.com/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-opus-5","messages":[{"role":"user","content":"Hello!"}]}'
```

**BYOC**

```bash
curl https://<data_plane_host>/gateway/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-opus-5","messages":[{"role":"user","content":"Hello!"}]}'
```

The gateway applies the fallback chain configured for `anthropic/claude-opus-5` in the API key's workspace. If no chain matches, the gateway returns the primary model's response without attempting a fallback.

## Choose fallback candidates

You can add two types of fallback candidates:

* **Direct provider model**: select a supported gateway provider and model. This option uses the workspace's secret for that provider, or Gateway Credits for eligible hosted models.
* **Model configuration**: select a saved workspace [model configuration](model-configurations.md). Use this option for a custom OpenAI-compatible or Anthropic endpoint, a custom model name, or configuration-specific parameters.

Model configurations are workspace-scoped. A fallback chain can only use configurations from its selected workspace.

For example, configure `anthropic/claude-opus-5` as the primary model, `openai/gpt-5.4-mini` as the first fallback, and a saved OpenAI-compatible model configuration as the second fallback. The application continues to request `anthropic/claude-opus-5`; the gateway selects and translates fallback calls when needed.

## See also

* [API formats](llm-gateway-api-formats.md): review supported request formats and translation behavior.
* [Spend policies](llm-gateway-spend-policies.md): apply cost limits alongside fallback routing.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-fallbacks.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
