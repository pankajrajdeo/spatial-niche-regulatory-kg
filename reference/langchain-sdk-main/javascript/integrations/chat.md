---
title: "Chat model integrations"
description: "Integrate with chat models using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/chat"
category: "docs"
tags: [docs, javascript, integrations, chat]
---

# Chat model integrations

> Integrate with chat models using LangChain JavaScript.

[Chat models](../langchain/models.md) are language models that use a sequence of [messages](../langchain/messages.md) as inputs and return messages as outputs (as opposed to plaintext).

## Install and use

> [!TIP]
> See [this section for general instructions on installing LangChain packages](../langchain/install.md).

<details>
<summary>OpenAI</summary>

Install:

**npm**

```bash
npm install @langchain/openai @langchain/core
```

**yarn**

```bash
yarn add @langchain/openai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/openai @langchain/core
```

Add environment variables:

```bash
OPENAI_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({ model: "gpt-5.4-mini" });
```

```javascript
await model.invoke("Hello, world!")
```

</details>

<details>
<summary>Anthropic</summary>

Install:

**npm**

```bash
npm i @langchain/anthropic @langchain/core
```

**yarn**

```bash
yarn add @langchain/anthropic @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/anthropic @langchain/core
```

Add environment variables:

```bash
ANTHROPIC_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { ChatAnthropic } from "@langchain/anthropic";

const model = new ChatAnthropic({
model: "claude-sonnet-4-6",
temperature: 0
});
```

```javascript
await model.invoke("Hello, world!")
```

</details>

<details>
<summary>Google Gemini</summary>

Install:

**npm**

```bash
npm install @langchain/google @langchain/core
```

**yarn**

```bash
yarn add @langchain/google @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/google @langchain/core
```

Add environment variables:

```bash
GOOGLE_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { ChatGoogle } from "@langchain/google";

const model = new ChatGoogle("gemini-2.5-flash");
```

```javascript
await model.invoke("Hello, world!")
```

</details>

<details>
<summary>MistralAI</summary>

Install:

**npm**

```bash
npm install @langchain/mistralai @langchain/core
```

**yarn**

```bash
yarn add @langchain/mistralai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/mistralai @langchain/core
```

Add environment variables:

```bash
MISTRAL_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { ChatMistralAI } from "@langchain/mistralai";

const model = new ChatMistralAI({
model: "mistral-large-latest",
temperature: 0
});
```

```javascript
await model.invoke("Hello, world!")
```

</details>

<details>
<summary>Groq</summary>

Install:

**npm**

```bash
npm install @langchain/groq @langchain/core
```

**yarn**

```bash
yarn add @langchain/groq @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/groq @langchain/core
```

Add environment variables:

```bash
GROQ_API_KEY=your-api-key
```

Instantiate the model:

```typescript
import { ChatGroq } from "@langchain/groq";

const model = new ChatGroq({
model: "openai/gpt-oss-120b",
temperature: 0
});
```

```javascript
await model.invoke("Hello, world!")
```

</details>

## Featured models

> [!NOTE]
> **While these LangChain classes support the indicated advanced feature**, you may need to refer to provider-specific documentation to learn which hosted models or backends support the feature.

| Model                                                                               | Stream                             | [Tool Calling](../langchain/tools.md) | [`withStructuredOutput()`](../langchain/models.md#structured-output) | [`Multimodal`](../langchain/messages.md#multimodal) | Downloads                                                                                                                                                                                                                                                                           |
| :---------------------------------------------------------------------------------- | :--------------------------------- | :----------------------------------------------- | :----------------------------------------------------------------------------- | :------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ChatOpenAI`](chat/openai.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="14480022"><a href="https://www.npmjs.com/package/@langchain/openai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/openai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>       |
| [`ChatAnthropic`](chat/anthropic.md)                      | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="4980649"><a href="https://www.npmjs.com/package/@langchain/anthropic" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/anthropic?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>  |
| [`ChatBedrockConverse`](chat/bedrock_converse.md)         | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="3181274"><a href="https://www.npmjs.com/package/@langchain/aws" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/aws?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>              |
| [`ChatGroq`](chat/groq.md)                                | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="965028"><a href="https://www.npmjs.com/package/@langchain/groq" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/groq?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`ChatOllama`](chat/ollama.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="833544"><a href="https://www.npmjs.com/package/@langchain/ollama" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/ollama?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>         |
| [`ChatMistralAI`](chat/mistral.md)                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="764540"><a href="https://www.npmjs.com/package/@langchain/mistralai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/mistralai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>   |
| [`ChatCohere`](chat/cohere.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="494553"><a href="https://www.npmjs.com/package/@langchain/cohere" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/cohere?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>         |
| [`ChatXAI`](chat/xai.md)                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="382392"><a href="https://www.npmjs.com/package/@langchain/xai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/xai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>               |
| [`ChatGoogle`](chat/google.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="322141"><a href="https://www.npmjs.com/package/@langchain/google" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/google?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>         |
| [`ChatCloudflareWorkersAI`](chat/cloudflare_workersai.md) | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span>               | <span data-sort-value="1">❌</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="17423"><a href="https://www.npmjs.com/package/@langchain/cloudflare" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/cloudflare?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>  |
| [`ChatFireworks`](chat/fireworks.md)                      | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="6462"><a href="https://www.npmjs.com/package/@langchain/fireworks" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/fireworks?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>     |
| [`ChatTogetherAI`](chat/togetherai.md)                    | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="1237"><a href="https://www.npmjs.com/package/@langchain/together-ai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/together-ai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`ChatPerplexity`](chat/perplexity.md)                    | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="750"><a href="https://www.npmjs.com/package/@langchain/perplexity" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/perplexity?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>    |

See the [full list of chat model integrations](#all-chat-models) below for more options.

## Routers & proxies

Routers and proxies give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks.

| Provider                             | Integration                                                      | Description                                                                 |
| ------------------------------------ | ---------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](chat/openrouter.md) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more     |
| [FuturMix](https://futurmix.ai/)     | [`ChatOpenAI`](https://futurmix.ai/)                             | Unified AI gateway for 22+ models with OpenAI-compatible API and 99.99% SLA |

## Chat Completions API

Certain model providers offer endpoints that are compatible with OpenAI's (legacy) [Chat Completions API](https://platform.openai.com/docs/guides/completions). In such case, you can use [`ChatOpenAI`](chat/openai.md) with a custom `base_url` to connect to these endpoints. Note that features built on top of the Chat Completions API may not be fully supported by `ChatOpenAI`; in such cases, consider using a provider-specific class if available.

[Auxen](https://auxen.ai) hosts dedicated per-customer LLM endpoints with an OpenAI-compatible Chat Completions API. Use `ChatOpenAI` with a custom base URL and per-instance API key.

[Tuning Engines](https://www.tuningengines.com/) provides a governed OpenAI-compatible Chat Completions API. Use `ChatOpenAI` with `baseURL` `https://api.tuningengines.com/v1` and a Tuning Engines inference key.

## All chat models

| Model                                                                               | Stream                             | [Tool Calling](../langchain/tools.md) | [`withStructuredOutput()`](../langchain/models.md#structured-output) | [`Multimodal`](../langchain/messages.md#multimodal) | Downloads                                                                                                                                                                                                                                                                                      |
| :---------------------------------------------------------------------------------- | :--------------------------------- | :----------------------------------------------- | :----------------------------------------------------------------------------- | :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`AzureChatOpenAI`](chat/azure.md)                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="14480022"><a href="https://www.npmjs.com/package/@langchain/openai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/openai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`ChatOpenAI`](chat/openai.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="14480022"><a href="https://www.npmjs.com/package/@langchain/openai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/openai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                  |
| [`ChatAnthropic`](chat/anthropic.md)                      | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="4980649"><a href="https://www.npmjs.com/package/@langchain/anthropic" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/anthropic?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`ChatBedrockConverse`](chat/bedrock_converse.md)         | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="3181274"><a href="https://www.npmjs.com/package/@langchain/aws" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/aws?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                         |
| [`ChatGoogleGenerativeAI`](chat/google_generative_ai.md)  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="3132743"><a href="https://www.npmjs.com/package/@langchain/google-genai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/google-genai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>       |
| [`ChatVertexAI`](chat/google_vertex_ai.md)                | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="1813550"><a href="https://www.npmjs.com/package/@langchain/google-vertexai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/google-vertexai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`ChatGroq`](chat/groq.md)                                | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="965028"><a href="https://www.npmjs.com/package/@langchain/groq" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/groq?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                        |
| [`ChatOllama`](chat/ollama.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="833544"><a href="https://www.npmjs.com/package/@langchain/ollama" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/ollama?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`ChatMistralAI`](chat/mistral.md)                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="764540"><a href="https://www.npmjs.com/package/@langchain/mistralai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/mistralai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>              |
| [`ChatCohere`](chat/cohere.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="494553"><a href="https://www.npmjs.com/package/@langchain/cohere" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/cohere?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`ChatXAI`](chat/xai.md)                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="382392"><a href="https://www.npmjs.com/package/@langchain/xai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/xai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                          |
| [`ChatGoogle`](chat/google.md)                            | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="322141"><a href="https://www.npmjs.com/package/@langchain/google" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/google?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                    |
| [`ChatDeepSeek`](chat/deepseek.md)                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="310817"><a href="https://www.npmjs.com/package/@langchain/deepseek" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/deepseek?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                |
| [`ChatOpenRouter`](chat/openrouter.md)                    | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="273014"><a href="https://www.npmjs.com/package/@langchain/openrouter" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/openrouter?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>            |
| [`ChatCerebras`](chat/cerebras.md)                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="82853"><a href="https://www.npmjs.com/package/@langchain/cerebras" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/cerebras?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                 |
| [`ChatBaiduQianfan`](chat/baidu_qianfan.md)               | <span data-sort-value="0" />       | <span data-sort-value="0" />                     | <span data-sort-value="0" />                                                   | <span data-sort-value="0" />                                  | <span data-sort-value="23195"><a href="https://www.npmjs.com/package/@langchain/baidu-qianfan" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/baidu-qianfan?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>       |
| [`ChatCloudflareWorkersAI`](chat/cloudflare_workersai.md) | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span>               | <span data-sort-value="1">❌</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="17423"><a href="https://www.npmjs.com/package/@langchain/cloudflare" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/cloudflare?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`ChatFireworks`](chat/fireworks.md)                      | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="6462"><a href="https://www.npmjs.com/package/@langchain/fireworks" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/fireworks?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                |
| [`ChatWatsonx`](chat/ibm.md)                              | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="3845"><a href="https://www.npmjs.com/package/@langchain/ibm" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/ibm?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                            |
| [`ChatTogetherAI`](chat/togetherai.md)                    | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="1237"><a href="https://www.npmjs.com/package/@langchain/together-ai" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/together-ai?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>            |
| [`ChatYandexGPT`](chat/yandex.md)                         | <span data-sort-value="0" />       | <span data-sort-value="0" />                     | <span data-sort-value="0" />                                                   | <span data-sort-value="0" />                                  | <span data-sort-value="970"><a href="https://www.npmjs.com/package/@langchain/yandex" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/yandex?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                       |
| [`ChatPerplexity`](chat/perplexity.md)                    | <span data-sort-value="2">✅</span> | <span data-sort-value="1">❌</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="750"><a href="https://www.npmjs.com/package/@langchain/perplexity" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/perplexity?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>               |
| [`ChatKServe`](https://gitlab.com/bitkaio/langchain/kserve-provider)                | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="49"><a href="https://www.npmjs.com/package/@bitkaio/langchain-kserve" target="_blank">  <img src="https://img.shields.io/npm/dm/@bitkaio/langchain-kserve?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>        |
| [`ChatInterfaze`](https://interfaze.ai/docs)                                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="39"><a href="https://www.npmjs.com/package/@interfaze-ai/langchain" target="_blank">  <img src="https://img.shields.io/npm/dm/@interfaze-ai/langchain?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>            |
| [`ChatSCX`](https://scx.ai/)                                                        | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="27"><a href="https://www.npmjs.com/package/@scx-ai/langchain" target="_blank">  <img src="https://img.shields.io/npm/dm/@scx-ai/langchain?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span>                        |
| [`Auxen`](https://auxen.ai)                                                         | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                          |
| [`FakeListChatModel`](chat/fake.md)                       | <span data-sort-value="0" />       | <span data-sort-value="0" />                     | <span data-sort-value="0" />                                                   | <span data-sort-value="0" />                                  | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                          |
| [`FuturMix`](https://futurmix.ai/)                                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="2">✅</span>                            | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                          |
| [`Tuning Engines`](https://www.tuningengines.com/)                                  | <span data-sort-value="2">✅</span> | <span data-sort-value="2">✅</span>               | <span data-sort-value="2">✅</span>                                             | <span data-sort-value="1">❌</span>                            | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                                          |

> [!NOTE]
> If you'd like to contribute an integration, see [Contributing integrations](../contributing.md#add-a-new-integration).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
