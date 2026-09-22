---
title: "Microsoft Foundry middleware integration"
description: "Integrate with the Azure AI middleware using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/middleware/azure_ai"
category: "docs"
tags: [docs, integrations, middleware, azure_ai]
---

# Microsoft Foundry middleware integration

> Integrate with the Azure AI middleware using LangChain Python.

Middleware specifically designed for Microsoft Foundry and Azure AI Content Safety. Learn more about [middleware](../../langchain/middleware/overview.md).

These middleware classes live in the `langchain-azure-ai` package and are exported from `langchain_azure_ai.agents.middleware`.

> [!NOTE]
> Azure AI Content Safety middleware is currently marked experimental upstream. Expect the API surface to evolve as Azure AI Content Safety and LangChain middleware support continue to mature.

## Overview

| Middleware                                | Description                                                                  |
| ----------------------------------------- | ---------------------------------------------------------------------------- |
| [Text moderation](#text-moderation)       | Screen input and output text for harmful content and blocklist matches       |
| [Image moderation](#image-moderation)     | Screen image inputs and outputs using Azure AI Content Safety image analysis |
| [Prompt shield](#prompt-shield)           | Detect direct and indirect prompt injection attempts                         |
| [Protected material](#protected-material) | Detect copyrighted or otherwise protected text or code                       |
| [Groundedness](#groundedness)             | Evaluate model outputs against grounding sources and flag hallucinations     |

### Features

* Text moderation for harmful content and custom blocklists.
* Image moderation for data URLs and public HTTP(S) image inputs.
* Prompt injection detection with Prompt Shield.
* Protected material detection for text and code.
* Groundedness evaluation for generated answers against retrieved context.
* Custom `context_extractor` hooks to adapt screening and evaluation to your agent state.

## Setup

To use the Azure AI Content Safety middleware, install the integration package, configure either an Azure AI Foundry project endpoint or an Azure Content Safety endpoint, and provide a credential.

### Installation

Install the package:

**pip**

```bash
pip install -U langchain-azure-ai
```

**uv**

```bash
uv add langchain-azure-ai
```

### Credentials

For authentication, pass either `DefaultAzureCredential()` or an API-key string through the `credential` argument. Using a Foundry Project requires the use of Microsoft Entra ID for authentication.

**Initialize credential**

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```

### Instantiation

The middleware supports two endpoint styles:

* An Azure Content Safety resource endpoint via `AZURE_CONTENT_SAFETY_ENDPOINT`
* An Azure AI Foundry project endpoint via `AZURE_AI_PROJECT_ENDPOINT`

If both are available, prefer `project_endpoint` because it gives better defaults for Azure AI Foundry-based workflows. In most setups, you can set the environment variable once and omit `endpoint` or `project_endpoint` from each middleware instantiation.

**Configure endpoint**

```python
import os

os.environ["AZURE_AI_PROJECT_ENDPOINT"] = "https://<resource>.services.ai.azure.com/api/projects/<project>"
```

Import and configure your middleware from `langchain_azure_ai.agents.middleware`.

**Initialize middleware**

```python
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.agents.middleware import AzureContentModerationMiddleware

middleware = AzureContentModerationMiddleware(
    project_endpoint="https://<resource>.services.ai.azure.com/api/projects/<project>",
    credential=DefaultAzureCredential(),
    categories=["Hate", "Violence"],
    exit_behavior="error",
)
```

## Use with an agent

Pass middleware to [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) in order. You can combine Azure AI middleware with [built-in middleware](../../langchain/middleware/built-in.md).

**Agent with middleware**

```python
from azure.identity import DefaultAzureCredential
from langchain.agents import create_agent
from langchain_azure_ai.agents.middleware import AzureContentModerationMiddleware

agent = create_agent(
    model="azure_ai:gpt-5.5",
    middleware=[
        AzureContentModerationMiddleware(
            project_endpoint="https://<resource>.services.ai.azure.com/api/projects/<project>",
            credential=DefaultAzureCredential(),
            categories=["Hate", "Violence"],
            exit_behavior="error",
        )
    ],
)
```

> [!TIP]
> If `AZURE_AI_PROJECT_ENDPOINT` is already set, you can usually omit `project_endpoint` during instantiation.

## Azure AI Content Safety

### Text moderation

Use `AzureContentModerationMiddleware` to screen the last `HumanMessage` before the agent runs and the last `AIMessage` after the agent runs. This middleware uses Azure AI Content Safety harm detection and can also check custom blocklists configured in your resource.

Text moderation is useful for the following:

* Blocking harmful user input before a model call
* Screening model output before it reaches end users
* Enforcing custom blocklists in regulated or enterprise deployments
* Composing multiple moderation passes with different category and direction settings

```python
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.agents.middleware import AzureContentModerationMiddleware

middleware = AzureContentModerationMiddleware(
    project_endpoint="https://<resource>.services.ai.azure.com/api/projects/<project>",
    credential=DefaultAzureCredential(),
    categories=["Hate", "SelfHarm", "Sexual", "Violence"],
    severity_threshold=4,
    exit_behavior="error",
    apply_to_input=True,
    apply_to_output=True,
)
```

<details>
<summary>Configuration options</summary>

#### `Field` — `list[str] | None`
Harm categories to analyze. Valid values are `'Hate'`, `'SelfHarm'`, `'Sexual'`, and `'Violence'`. Defaults to all four categories.

#### `Field` — `int`
Minimum severity score from `0` to `6` that triggers the configured behavior.

#### `Field` — `string`
One of `'error'`, `'continue'`, or `'replace'`.

#### `Field` — `bool`
Whether to screen the last `HumanMessage` before the agent runs.

#### `Field` — `bool`
Whether to screen the last `AIMessage` after the agent runs.

#### `Field` — `list[str] | None`
Names of custom blocklists configured in your Azure Content Safety resource.

#### `Field` — `Callable | None`
Optional callable that extracts the text to screen from agent state and runtime.

</details>

### Image moderation

Use `AzureContentModerationForImagesMiddleware` when your agent handles visual content. It extracts images from the latest input or output message and screens them with the Azure AI Content Safety image analysis API.

This middleware supports:

* Base64 data URLs such as `data:image/png;base64,...`
* Public HTTP(S) image URLs

```python
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.agents.middleware import (
    AzureContentModerationForImagesMiddleware,
)

middleware = AzureContentModerationForImagesMiddleware(
    endpoint="https://<resource>.cognitiveservices.azure.com/",
    credential=DefaultAzureCredential(),
    categories=["Hate", "SelfHarm", "Sexual", "Violence"],
    severity_threshold=4,
    exit_behavior="error",
    apply_to_input=True,
    apply_to_output=False,
)
```

<details>
<summary>Configuration options</summary>

#### `Field` — `list[str] | None`
Image harm categories to analyze. Defaults to all four supported categories.

#### `Field` — `int`
Minimum severity score from `0` to `6` that triggers the configured behavior.

#### `Field` — `string`
One of `'error'` or `'continue'`.

#### `Field` — `bool`
Whether to screen images in the latest `HumanMessage`.

#### `Field` — `bool`
Whether to screen images in the latest `AIMessage`.

#### `Field` — `Callable | None`
Optional callable that extracts images from agent state and runtime.

</details>

### Prompt shield

Use `AzurePromptShieldMiddleware` to detect prompt injection in user prompts and optional supporting documents. By default it screens input only, because prompt injection is usually an input-side attack, but you can also enable output screening.

```python
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.agents.middleware import AzurePromptShieldMiddleware

middleware = AzurePromptShieldMiddleware(
    project_endpoint="https://<resource>.services.ai.azure.com/api/projects/<project>",
    credential=DefaultAzureCredential(),
    exit_behavior="continue",
    apply_to_input=True,
    apply_to_output=False,
)
```

<details>
<summary>Configuration options</summary>

#### `Field` — `string`
One of `'error'`, `'continue'`, or `'replace'`.

#### `Field` — `bool`
Whether to screen the latest `HumanMessage` before the agent runs.

#### `Field` — `bool`
Whether to screen the latest `AIMessage` after the agent runs.

#### `Field` — `Callable | None`
Optional callable that extracts the user prompt and grounding documents from agent state and runtime.

</details>

### Protected material

Use `AzureProtectedMaterialMiddleware` to detect protected content such as copyrighted text or code. This middleware can screen both the latest user input and the latest model output.

```python
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.agents.middleware import AzureProtectedMaterialMiddleware

middleware = AzureProtectedMaterialMiddleware(
    endpoint="https://<resource>.cognitiveservices.azure.com/",
    credential=DefaultAzureCredential(),
    type="code",
    exit_behavior="replace",
    apply_to_input=False,
    apply_to_output=True,
    violation_message="Protected material detected. Please provide a higher-level summary instead.",
)
```

<details>
<summary>Configuration options</summary>

#### `Field` — `string`
The content type to screen: `'text'` or `'code'`.

#### `Field` — `string`
One of `'error'`, `'continue'`, or `'replace'`.

#### `Field` — `bool`
Whether to screen the latest `HumanMessage`.

#### `Field` — `bool`
Whether to screen the latest `AIMessage`.

#### `Field` — `Callable | None`
Optional callable that extracts text from agent state and runtime.

</details>

### Groundedness

Use `AzureGroundednessMiddleware` to evaluate whether a model response is grounded in the context available to the agent. Unlike the other middleware classes on this page, groundedness runs after model generation and inspects the generated answer against supporting sources.

By default, groundedness collects sources from the current conversation, including system content, tool outputs, and relevant annotations attached to model responses.

```python
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.agents.middleware import AzureGroundednessMiddleware

middleware = AzureGroundednessMiddleware(
    project_endpoint="https://<resource>.services.ai.azure.com/api/projects/<project>",
    credential=DefaultAzureCredential(),
    domain="Generic",
    task="QnA",
    exit_behavior="continue",
)
```

<details>
<summary>Configuration options</summary>

#### `Field` — `string`
The analysis domain. Supported values are `'Generic'` and `'Medical'`.

#### `Field` — `string`
The task type for the analysis. Supported values are `'Summarization'` and `'QnA'`.

#### `Field` — `string`
One of `'error'` or `'continue'`.

#### `Field` — `Callable | None`
Optional callable that extracts the answer, grounding sources, and optional question from agent state and runtime.

</details>

## API reference

For the full public API, see the middleware exports in [`langchain_azure_ai.agents.middleware`](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-ai/langchain_azure_ai/agents/middleware) and the underlying Content Safety middleware package in [`langchain_azure_ai.agents.middleware.content_safety`](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-ai/langchain_azure_ai/agents/middleware/content_safety).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/middleware/azure_ai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
