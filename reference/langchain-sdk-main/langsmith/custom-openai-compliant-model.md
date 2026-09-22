---
title: "Connect to an OpenAI compliant model provider/proxy"
description: "The Playground allows you to use any model that is compliant with the OpenAI API. You can utilize your model by setting the Proxy Provider for in the Playground."
source: "https://docs.langchain.com/langsmith/custom-openai-compliant-model"
category: "docs"
tags: [docs, langsmith, custom-openai-compliant-model]
---

# Connect to an OpenAI compliant model provider/proxy

The Playground allows you to use any model that is compliant with the OpenAI API. You can utilize your model by setting the Proxy Provider for  in the Playground.

## Deploy an OpenAI compliant model

Many providers offer OpenAI compliant models or proxy services. Some examples of this include:

* [LiteLLM Proxy](https://github.com/BerriAI/litellm?tab=readme-ov-file#quick-start-proxy---cli)
* [Ollama](https://ollama.com/)

You can use these providers to deploy your model and get an API endpoint that is compliant with the OpenAI API.

Take a look at the full [specification](https://platform.openai.com/docs/api-reference/chat) for more information.

## Use the model in the Playground

Once you have deployed a model server, you can use it in the [Playground](prompt-engineering-concepts.md#playground).

To access the **Prompt Settings** menu:

1. Under the **Prompts** heading select the gear  icon next to the model name.
2. In the **Model Configuration** tab, select the model to edit in the dropdown.
3. For the **Provider** dropdown, select **OpenAI Compatible Endpoint**.
4. Add your OpenAI Compatible Endpoint to the **Base URL** input. See [Base URL format](#base-url-format) for examples.

   <img src="https://mintcdn.com/langchain-5e9cc07a/cemWY9w7h0W8uMbk/langsmith/images/openai-compatible-endpoint.png?fit=max&auto=format&n=cemWY9w7h0W8uMbk&q=85&s=fdbe548e512ed40fb512578d02986b45" alt="Model Configuration window in the LangSmith UI with a model selected and the Provider dropdown with OpenAI Compatible Endpoint selected." width="897" height="572" data-path="langsmith/images/openai-compatible-endpoint.png" />

   <img src="https://mintcdn.com/langchain-5e9cc07a/cemWY9w7h0W8uMbk/langsmith/images/openai-compatible-endpoint-dark.png?fit=max&auto=format&n=cemWY9w7h0W8uMbk&q=85&s=97459563da21d17228a1bb94a1b9edf3" alt="Model Configuration window in the LangSmith UI with a model selected and the Provider dropdown with OpenAI Compatible Endpoint selected." width="896" height="552" data-path="langsmith/images/openai-compatible-endpoint-dark.png" />

If everything is set up correctly, you should see the model's response in the Playground. You can also use this functionality to invoke downstream pipelines.

For information on how to store your model configuration, refer to [Configure prompt settings](managing-model-configurations.md).

If your OpenAI-compatible endpoint sits behind an OAuth2 gateway, store the OAuth `client_credentials` on the model configuration instead of distributing a static API key as a workspace secret. See [OAuth client credentials](model-configurations.md#oauth-client-credentials).

## Base URL format

The **Base URL** should point to the root of your OpenAI-compatible API server.
LangSmith appends `/chat/completions` automatically—do not include it in the Base URL.

### Example Base URLs

| Provider                                                    | Example Base URL                         |
| ----------------------------------------------------------- | ---------------------------------------- |
| [Ollama](https://ollama.com/) (local)                       | `http://localhost:11434/v1`              |
| [LiteLLM Proxy](https://github.com/BerriAI/litellm) (local) | `http://localhost:4000`                  |
| [vLLM](https://docs.vllm.ai/) (local)                       | `http://localhost:8000/v1`               |
| Self-hosted (remote)                                        | `https://my-model-server.example.com/v1` |

Custom path prefixes are supported. If your server exposes completions at `/api/v2/chat/completions`,
set the Base URL to `https://my-server.example.com/api/v2`.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/custom-openai-compliant-model.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
