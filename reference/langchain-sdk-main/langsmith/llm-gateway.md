---
title: "LLM Gateway"
description: "Access models across providers with one LangSmith API key while tracing calls and enforcing spend and data-protection policies."
source: "https://docs.langchain.com/langsmith/llm-gateway"
category: "docs"
tags: [docs, langsmith, llm-gateway]
---

# LLM Gateway

> Access models across providers with one LangSmith API key while tracing calls and enforcing spend and data-protection policies.

Use one [LangSmith API key](create-account-api-key.md) to call models across configured providers. Switch providers by changing the model ID, while the LLM Gateway traces every model call and applies centralized governance policies.

> [!NOTE]
> **Beta:** The LLM Gateway is in [beta](release-stages.md).
>
> The gateway is also available on [BYOC](byoc.md), where it runs inside your data plane. Send requests to your [data plane endpoint](byoc-usage.md#find-your-data-plane-endpoint) behind the `/gateway` path prefix, and authenticate with an API key scoped to a workspace in that data plane. For more information, see [Use a BYOC data plane](llm-gateway-how-it-works.md#use-a-byoc-data-plane).

> [!NOTE]
> **Self-hosted availability:** LLM Gateway is not included in the LangSmith v0.16.0 self-hosted stable release. It will be available in a future stable release. To express interest, submit the [LLM Gateway self-hosted access request](https://www.langchain.com/langsmith-llm-gateway-self-hosted-access-request). You can also try LLM Gateway on v17 RC versions or BYOC (bring your own cloud) ahead of the stable release.

## Make your first request

> [!NOTE]
> An administrator must [enable the gateway, add a provider secret, and grant access](llm-gateway-admin-setup.md) once for your workspace. After setup, developers need only a workspace-scoped LangSmith API key.

Set your key and make a standard Chat Completions request. This example assumes the workspace has an Anthropic provider secret:

**Cloud**

```bash
export LANGSMITH_API_KEY="lsv2_..._....cbed3e"

curl https://gateway.smith.langchain.com/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-sonnet-4-6","messages":[{"role":"user","content":"Hello!"}]}'
```

**BYOC**

```bash
export LANGSMITH_API_KEY="lsv2_..._....cbed3e"

curl https://<data_plane_host>/gateway/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-sonnet-4-6","messages":[{"role":"user","content":"Hello!"}]}'
```

A `200` response confirms that the gateway, your LangSmith API key, permissions, and the selected provider secret are configured correctly. For Python, TypeScript, alternative API formats, and troubleshooting, follow the [quickstart](llm-gateway-quickstart.md).

## What the gateway provides

* **One key, multiple providers:** Developers authenticate with a LangSmith API key instead of storing provider keys locally.
* **One request format, multiple models:** Use Chat Completions, Messages, or Responses with models across configured providers.
* **Built-in observability:** Every gateway call appears as a [LangSmith trace](llm-gateway-access.md).
* **Central governance:** Apply [spend limits](llm-gateway-spend-policies.md), [rate limits](llm-gateway-rate-limit-policies.md), and [data policies](llm-gateway-data-policy.md).

## Use the standard API

Choose the request format already used by your application. The format does not limit which configured provider you can call.

| API format              | Endpoint                    |
| ----------------------- | --------------------------- |
| OpenAI Chat Completions | `POST /v1/chat/completions` |
| Anthropic Messages      | `POST /v1/messages`         |
| OpenAI Responses        | `POST /v1/responses`        |

Set `model` to a provider-prefixed bring-your-own-key ID such as `openai/gpt-5.4-mini`, `anthropic/claude-opus-5`, or `azure/<deployment-name>`, or use a [Gateway Credits](llm-gateway-credits.md) model slug such as `moonshotai/kimi-k3`. The model ID determines the upstream route. When the selected provider uses a different native format, the gateway translates the request and response.

On BYOC, the same paths sit behind the `/gateway` prefix, such as `POST /gateway/v1/chat/completions`.

For base URLs, examples, translation behavior, regional endpoints, and BYOC data plane endpoints, see [API formats](llm-gateway-api-formats.md).

## Choose how credentials are managed

| Option                                            | Upstream credential                                                                                                                  | Setup and billing                                                                 |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Bring your own provider account                   | An administrator stores the provider key in workspace [Provider Secrets](llm-gateway-admin-setup.md#1-add-provider-secrets). | The provider bills usage to your provider account.                                |
| [Gateway Credits](llm-gateway-credits.md) | LangChain owns the upstream credential.                                                                                              | No provider secret is required. Invocations are billed to your LangSmith account. |

## Go further

#### [Quickstart](llm-gateway-quickstart.md)
Make a request with cURL, Python, or TypeScript, then view its trace.

#### [Administrator setup](llm-gateway-admin-setup.md)
Enable the gateway, add provider credentials, and grant developer access.

> [!TIP]
> Need to use the gateway with prompts stored in the Prompt Hub? See [Prompt Hub with the gateway](manage-prompts-programmatically.md#use-with-the-langsmith-gateway) for how to route Prompt Hub model calls through the gateway using two environment variables.
>
> Need provider-native request and response behavior? Use [Direct model access](llm-gateway-direct-model-access.md) to bypass the standardization layer. This is an advanced alternative to the standard API.
>
> For further questions, contact [LangChain support](https://support.langchain.com).

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
