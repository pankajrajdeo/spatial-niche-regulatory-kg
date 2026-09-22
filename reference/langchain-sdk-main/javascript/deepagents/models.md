---
title: "Models"
description: "Configure model providers and parameters for Deep Agents"
source: "https://docs.langchain.com/oss/javascript/deepagents/models"
category: "docs"
tags: [docs, javascript, deepagents, models]
---

# Models

> Configure model providers and parameters for Deep Agents

Deep Agents work with any [LangChain chat model](../langchain/models.md) that supports [tool calling](../langchain/models.md#tool-calling).

## Supported models

Specify models in `provider:model` format (for example, `google_genai:gemini-3.6-flash`, `openai:gpt-5.4`, or `anthropic:claude-sonnet-4-6`). The provider prefix selects the LangChain integration, and everything after the colon is passed through to that provider as the model identifier. For valid provider strings, see the `model_provider` parameter of [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel). For provider-specific configuration, see [chat model integrations](../integrations/chat.md).

The model identifier must match the format expected by the provider. Some providers use simple names like `gpt-5.5`; others use namespaced IDs or deployment paths like `zai-org/GLM-5.2`, so the full Deep Agents string would be `baseten:zai-org/GLM-5.2`. Check the provider's model catalog or integration docs for the current identifiers.

### Suggested models

These models perform well on the [Deep Agents eval suite](https://github.com/langchain-ai/deepagents/tree/main/libs/evals#readme), which tests basic agent operations. Passing these evals is necessary but not sufficient for strong performance on longer, more complex tasks.

| Provider                                                      | Models                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| [Google](../integrations/providers/google.md)       | `gemini-3.1-pro-preview`, `gemini-3.6-flash`            |
| [OpenAI](../integrations/providers/openai.md)       | `gpt-5.5`, `gpt-5.4`                                    |
| [Anthropic](../integrations/providers/anthropic.md) | `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6` |
| Open-weight                                                   | `GLM-5.2`, `Kimi-K2.7 Code`, `MiniMax-M3`               |

Open-weight models are available through providers like [OpenRouter](../integrations/chat/openrouter.md) and [Ollama](../integrations/chat/ollama.md).

### Model evaluations

The [Deep Agents eval suite](https://github.com/langchain-ai/deepagents/tree/main/libs/evals#readme) tests popular models:

| Model                                            |                                                                        Overall |                                                                        File Ops |                                                                       Retrieval |                                                                       Tool Use |                                                                         Memory |                                                                   Conversation |                                                                   Summarization |
| :----------------------------------------------- | -----------------------------------------------------------------------------: | ------------------------------------------------------------------------------: | ------------------------------------------------------------------------------: | -----------------------------------------------------------------------------: | -----------------------------------------------------------------------------: | -----------------------------------------------------------------------------: | ------------------------------------------------------------------------------: |
| google\_genai:gemini-3.6-flash                   |     [82%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** | **[90%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [54%](https://github.com/langchain-ai/deepagents/actions/runs/25290479270) |     [38%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |
| openai:gpt-5.4                                   |     [18%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |     [18%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) |     [51%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583) |     [38%](https://github.com/langchain-ai/deepagents/actions/runs/24425363630) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |
| openai:gpt-5.5                                   |     [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [84%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |     [64%](https://github.com/langchain-ai/deepagents/actions/runs/25345307822) | **[52%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |
| anthropic:claude-opus-4-6                        |     [26%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |     [26%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) | **[69%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |     [22%](https://github.com/langchain-ai/deepagents/actions/runs/24363491527) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |
| anthropic:claude-opus-4-7                        |     [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [82%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |                                                                              — |     [48%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |
| baseten:moonshotai/Kimi-K2.6                     |     [79%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906)** |     [84%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |                                                                              — |     [43%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |
| baseten:zai-org/GLM-5                            |     [77%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424)** |     [89%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) |     [44%](https://github.com/langchain-ai/deepagents/actions/runs/23872647281) |     [24%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) |
| fireworks:accounts/fireworks/models/glm-5p1      |     [81%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650)** |     [87%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) |                                                                              — |     [33%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) |
| fireworks:accounts/fireworks/models/minimax-m2p7 |     [79%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412)** |     [85%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) |                                                                              — |     [43%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) |
| ollama:minimax-m2.7:cloud                        |     [73%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |      [90%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |     [82%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |     [38%](https://github.com/langchain-ai/deepagents/actions/runs/23872647281) |     [29%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |
| openrouter:deepseek/deepseek-v4-flash            |     [81%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395)** |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) | **[90%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395)** |                                                                              — |     [33%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) |
| openrouter:minimax/minimax-m2.7                  |     [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [89%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |                                                                              — |     [43%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |
| openrouter:z-ai/glm-5.1                          | **[89%](https://github.com/langchain-ai/deepagents/actions/runs/25387853856)** |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25234719085) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25234686782)** |     [89%](https://github.com/langchain-ai/deepagents/actions/runs/25387853856) |                                                                              — |     [33%](https://github.com/langchain-ai/deepagents/actions/runs/25225620506) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25235579950) |

For more information, see the [Eval runs](https://github.com/langchain-ai/deepagents/actions/workflows/evals.yml).

## Configure model parameters

Pass a model string to [`createDeepAgent`](https://reference.langchain.com/javascript/deepagents/agent/createDeepAgent) in `provider:model` format, or pass a configured model instance for full control. Under the hood, model strings are resolved via [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel).

To configure model-specific parameters, use [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel) or instantiate a provider model class directly:

**initChatModel**

```ts
import { initChatModel } from "langchain/chat_models/universal";
import { createDeepAgent } from "deepagents";

const model = await initChatModel("google-genai:gemini-3.6-flash", {
  reasoningEffort: "medium", // [!code highlight]
});
const agent = createDeepAgent({ model });
```

**Provider package**

```ts
import { ChatGoogle } from "@langchain/google";
import { createDeepAgent } from "deepagents";

const model = new ChatGoogle({
  model: "gemini-3.1-pro-preview",
  reasoningEffort: "medium", // [!code highlight]
});
const agent = createDeepAgent({ model });
```

> [!NOTE]
> Available parameters vary by provider. See the [chat model integrations](../integrations/chat.md) page for provider-specific configuration options.

### Provider profiles

A [`ProviderProfile`](profiles.md#provider-profiles) packages initialization parameters that apply when you provide a `provider:model` string when creating the deep agent. It does not apply when you pass a preconfigured model with [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel).

You can register at two levels, and both can coexist:

* **Provider level**: a bare provider key like `"openai"` applies to every model from the `openai` provider.
* **Model level**: a `provider:model` key like `"openai:gpt-5.4"` applies only to that specific model, and merges on top of any matching provider-level profile.

See [Profiles](profiles.md) for the full field list, merge semantics, and plugin packaging.

> [!TIP]
> For shaping how the *agent* behaves once the model is built, use a [harness profile](profiles.md#harness-profiles).

### OpenAI and the Responses API

When you pass an `openai:...` string as the model, Deep Agents uses the built-in OpenAI [provider profile](profiles.md#provider-profiles) to enable the [Responses API](../integrations/chat/openai.md#responses-api) by default. That path supports OpenAI conversation state and related features; see the [OpenAI provider](../integrations/providers/openai.md) and [chat model](../integrations/chat/openai.md) docs for current API options.

> [!NOTE]
> The built-in OpenAI provider profile applies only to model strings. To set kwargs such as `use_responses_api`, `store`, or `include`, pass a configured model instance, or, in Python, layer them through a [provider profile](profiles.md#provider-profiles) `init_kwargs`. Build the instance with [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel) (Python) or `initChatModel` / `ChatOpenAI` (TypeScript).

Use the [OpenAI chat integration](../integrations/chat/openai.md#responses-api) to choose the Responses API versus Chat Completions (`useResponsesApi`, model kwargs, and any storage or output options your version exposes). Pass the resulting model instance to `createDeepAgent({ model })` so those settings are preserved.

## Select a model at runtime

If your application lets users choose a model (for example using a dropdown in the UI), use [middleware](../langchain/middleware.md) to swap the model at runtime without rebuilding the agent.

```ts
import { createMiddleware, initChatModel } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const contextSchema = z.object({
  model: z.string(),
});

const configurableModel = createMiddleware({
  name: "ConfigurableModel",
  wrapModelCall: async (request, handler) => {
    const modelName = request.runtime.context.model;
    const model = await initChatModel(modelName);
    return handler({ ...request, model });
  },
});

const agent = await createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  middleware: [configurableModel],
  contextSchema,
});

// Invoke with the user's model selection
const result = await agent.invoke(
  { messages: [{ role: "user", content: "Hello!" }] },
  { context: { model: "openai:gpt-5.5" } },
);
```

#### [View example trace](https://smith.langchain.com/public/89e1089d-632c-4338-b4bb-c019f4c18e14/r)
Open a public LangSmith run for this example.

> [!TIP]
> For more dynamic model patterns (for example routing based on conversation complexity or cost optimization), see [Dynamic model](../langchain/models.md#dynamic-model-selection) in the LangChain agents guide.

## Learn more

* [Models in LangChain](../langchain/models.md): chat model features including tool calling, structured output, and multimodality

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/models.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
