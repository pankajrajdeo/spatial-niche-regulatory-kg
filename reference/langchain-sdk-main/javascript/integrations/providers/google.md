---
title: "Google integrations"
description: "Integrate with Google using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/providers/google"
category: "docs"
tags: [docs, javascript, integrations, providers, google]
---

# Google integrations

> Integrate with Google using LangChain JavaScript.

LangChain provides integrations with [Google AI Studio](https://aistudio.google.com/) and [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) through the `@langchain/google` package.

> [!NOTE]
> Looking for the older `@langchain/google-genai` or `@langchain/google-vertexai` packages? They are maintained under [long-term support](#legacy-packages) but are no longer recommended for new projects.

## Chat models

The [`ChatGoogle`](../chat/google.md) class is the recommended way to access Gemini models (such as `gemini-2.5-pro`, `gemini-2.5-flash`, and `gemini-3.1-pro-preview`) and open models like Gemma. It supports both Google AI Studio and Gemini Enterprise Agent Platform in a single interface

> [!TIP]
> See [this section for general instructions on installing LangChain packages](../../langchain/install.md).

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

Configure your API key:

```bash
export GOOGLE_API_KEY=your-api-key
```

```typescript
import { ChatGoogle } from "@langchain/google";

const model = new ChatGoogle("gemini-2.5-flash");

const res = await model.invoke([
  ["human", "What would be a good company name for a company that makes colorful socks?"],
]);
```

`ChatGoogle` supports tool calling, structured output, multimodal inputs (images, audio, video), reasoning/thinking, image generation, text-to-speech, and Gemini-specific native tools like Google Search grounding and code execution.

#### [ChatGoogle](../chat/google.md)
Full chat model documentation, including setup, invocation, streaming, structured output, and more.

#### [Gemini native tools](../tools/google.md)
Google Search, Code Execution, URL Context, Google Maps, File Search, Computer Use, and MCP servers.

### Third-party models on Gemini Enterprise Agent Platform

[Anthropic](../chat/anthropic.md) Claude models are also available through
the [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude)
platform. See [using Claude on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude)
for more information about enabling access to the models and the model names to use.

### Postgres vector store (Cloud SQL)

The [PostgresVectorStore](../vectorstores/google_cloudsql_pg.md) module from the
[`@langchain/google-cloud-sql-pg`](https://www.npmjs.com/package/@langchain/google-cloud-sql-pg) package provides a way to use CloudSQL for PostgreSQL to store
vector embeddings.

```bash
npm install @langchain/google-cloud-sql-pg @langchain/core
```

## Legacy packages

The following packages are maintained under long-term support for existing users. New projects should use `@langchain/google` instead.

### `@langchain/google-genai`

The `@langchain/google-genai` package provides [`ChatGoogleGenerativeAI`](../chat/google_generative_ai.md) and [`GoogleGenerativeAIEmbeddings`](../embeddings/google_generative_ai.md) for accessing Gemini models through Google AI Studio. This package is built on a deprecated Google SDK and will not receive new features.

```bash
npm install @langchain/google-genai @langchain/core
```

### `@langchain/google-vertexai`

The `@langchain/google-vertexai` package provides [`ChatVertexAI`](../chat/google_vertex_ai.md), [`VertexAIEmbeddings`](../embeddings/google_vertex_ai.md), and [`VertexAI`](../llms/google_vertex_ai.md) for Gemini Enterprise Agent Platform on Node.js. It depends on [`@langchain/google-gauth`](#%40langchain%2Fgoogle-gauth) for authentication. This package is superseded by the Gemini Enterprise Agent Platform support built into `@langchain/google` for chat.

```bash
npm install @langchain/google-vertexai @langchain/core
```

### `@langchain/google-vertexai-web`

The `@langchain/google-vertexai-web` package provides the same Gemini Enterprise Agent Platform chat, embedding, and LLM classes for browser and Edge runtimes. Install this package (not `@langchain/google-vertexai`) when running in web environments. It depends on [`@langchain/google-webauth`](#%40langchain%2Fgoogle-webauth).

```bash
npm install @langchain/google-vertexai-web @langchain/core
```

See the [Gemini Enterprise Agent Platform chat](../chat/google_vertex_ai.md) page for `GOOGLE_WEB_CREDENTIALS` and web import paths.

<a id="@langchain/google-webauth"></a>

### `@langchain/google-webauth`

The [`@langchain/google-webauth`](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-google-webauth) package provides browser and Edge authentication for legacy Gemini Enterprise Agent Platform integrations. It is installed automatically with `@langchain/google-vertexai-web`—do not install it alongside `@langchain/google-gauth`.

Set service account JSON in `GOOGLE_WEB_CREDENTIALS` (or the deprecated `GOOGLE_VERTEX_AI_WEB_CREDENTIALS`). You can also pass `apiKey` or `authOptions` to the model constructor, or set the `API_KEY` environment variable.

<a id="@langchain/google-gauth"></a>

### `@langchain/google-gauth`

The [`@langchain/google-gauth`](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-google-gauth) package provides Node.js authentication for legacy Google integrations built on [`@langchain/google-common`](#%40langchain%2Fgoogle-common). It is installed automatically when you add `@langchain/google-vertexai`—you typically do **not** install or import `@langchain/google-gauth` directly.

On Node.js, credentials are resolved in this order:

1. `apiKey` passed to the model constructor
2. `authOptions` passed to the model constructor
3. The `API_KEY` environment variable
4. Service account JSON at the path in `GOOGLE_APPLICATION_CREDENTIALS`
5. Application Default Credentials (for example after `gcloud auth application-default login`, or on Google Cloud)

Do not use `@langchain/google-gauth` and `@langchain/google-webauth` in the same project.

The unified [`@langchain/google`](../chat/google.md) package uses `google-auth-library` directly and does not require `@langchain/google-gauth` or `@langchain/google-webauth`.

### `@langchain/google-cloud-sql-pg`

The [`@langchain/google-cloud-sql-pg`](https://www.npmjs.com/package/@langchain/google-cloud-sql-pg) package provides [`PostgresVectorStore`](../vectorstores/google_cloudsql_pg.md) and [`PostgresLoader`](../document_loaders/web_loaders/google_cloudsql_pg.md) for Cloud SQL for PostgreSQL. It is separate from the Gemini chat packages above.

<a id="@langchain/google-common"></a>

### `@langchain/google-common`

The [`@langchain/google-common`](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-google-common) package provides shared Gemini client abstractions for legacy integrations such as [`@langchain/google-vertexai`](../chat/google_vertex_ai.md). It does not include authorization code and is **not** a stand-alone package—do not install or import it directly.

> [!TIP]
> To migrate from `@langchain/google-genai` or `@langchain/google-vertexai` to `@langchain/google`, see the [ChatGoogle](../chat/google.md) page for setup instructions. The `ChatGoogle` class provides equivalent functionality with unified access to both Google AI Studio and Gemini Enterprise Agent Platform.

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/google.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
