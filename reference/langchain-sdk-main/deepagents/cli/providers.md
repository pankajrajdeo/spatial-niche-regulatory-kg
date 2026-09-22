---
title: "Model providers"
description: "Configure any LangChain-compatible model provider for Deep Agents Code"
source: "https://docs.langchain.com/oss/python/deepagents/cli/providers"
category: "docs"
tags: [docs, deepagents, cli, providers]
---

# Model providers

> Configure any LangChain-compatible model provider for Deep Agents Code

Deep Agents Code supports any [chat model provider compatible with LangChain](../../integrations/chat.md), unlocking use for virtually any LLM that supports tool calling. Any service that exposes an OpenAI-compatible or Anthropic-compatible API also works out of the box—see [Compatible APIs](../code/config-file.md#compatible-apis).

## Quickstart

Deep Agents Code integrates automatically with the [following model providers](#provider-reference): no extra configuration needed beyond installing the relevant provider package.

1. **Install provider packages**

   Each model provider requires its corresponding LangChain integration package. These ship as optional extras to keep the application lightweight. OpenAI, Anthropic, and Gemini are included by default. Install any other extra from within a session with `/install`, or from the shell with `dcode --install`:

**In session**

```txt
   /install groq
```

**Shell**

```bash
   dcode --install groq
```

   Run `/install` with no argument to list the valid extras. To preinstall extras during the initial CLI install, set `DEEPAGENTS_CODE_EXTRAS`:

```bash
   DEEPAGENTS_CODE_EXTRAS="baseten,groq" curl -LsSf https://langch.in/dcode | bash
```

2. **Set credentials**

   Add an API key for your provider with the [`/auth`](../code/credentials.md#use-%2Fauth-recommended) credential manager:

```txt
   /auth
```

   `/auth` shows a list of available providers and stores credentials for reuse across sessions.

   For non-interactive runs, CI/CD, or anywhere a TUI is not available, store the same key from the shell with [`dcode auth set`](../code/credentials.md#manage-credentials-from-the-shell-dcode-auth) or set the provider's environment variable instead. See [Provider credentials](../code/credentials.md) for the full key resolution order, the [`DEEPAGENTS_CODE_` prefix](../code/configuration.md#deepagents_code_-prefix) for scoping a key to Deep Agents Code, and the [Provider reference](#provider-reference) for each provider's environment variable.

   To configure model parameters, see [Model parameters](#model-parameters).

## Provider reference

Using a provider not listed here? See [Arbitrary providers](../code/config-file.md#arbitrary-providers): any LangChain-compatible provider can be used in Deep Agents Code with additional setup.

| Provider                                     | Package                                                                                    | Credential env var                                  | Model profiles |
| -------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------- | -------------- |
| OpenAI                                       | [`langchain-openai`](../../integrations/chat/openai.md)                                 | `OPENAI_API_KEY`                                    | ✅              |
| OpenAI (Codex)                               | [`langchain-openai`](../../integrations/chat/openai.md)                                 | None; [sign in with ChatGPT](#sign-in-with-chatgpt) | ✅              |
| Azure OpenAI                                 | [`langchain-openai`](../../integrations/chat/azure_chat_openai.md)                      | `AZURE_OPENAI_API_KEY`                              | ✅              |
| Anthropic                                    | [`langchain-anthropic`](../../integrations/chat/anthropic.md)                           | `ANTHROPIC_API_KEY`                                 | ✅              |
| Google Gemini API                            | [`langchain-google-genai`](../../integrations/chat/google_generative_ai.md)             | `GOOGLE_API_KEY`                                    | ✅              |
| Gemini Enterprise Agent Platform             | [`langchain-google-genai`](../../integrations/chat/google_generative_ai.md#credentials) | `GOOGLE_CLOUD_PROJECT`                              | ✅              |
| Gemini Enterprise Agent Platform (Anthropic) | [`langchain-google-vertexai`](../../integrations/chat/google_anthropic_vertex.md)       | `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`     | ✅              |
| Baseten                                      | [`langchain-baseten`](https://github.com/basetenlabs/langchain-baseten)                    | `BASETEN_API_KEY`                                   | ✅              |
| AWS Bedrock                                  | [`langchain-aws`](../../integrations/chat/bedrock.md)                                   | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`        | ✅              |
| AWS Bedrock Converse                         | [`langchain-aws`](../../integrations/chat/bedrock.md)                                   | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`        | ✅              |
| Hugging Face                                 | [`langchain-huggingface`](../../integrations/chat/huggingface.md)                       | `HUGGINGFACEHUB_API_TOKEN`                          | ✅              |
| Ollama                                       | [`langchain-ollama`](../../integrations/chat/ollama.md)                                 | `OLLAMA_API_KEY` (cloud only; optional)             | ❌              |
| Groq                                         | [`langchain-groq`](../../integrations/chat/groq.md)                                     | `GROQ_API_KEY`                                      | ✅              |
| Cohere                                       | [`langchain-cohere`](../../integrations/chat/cohere.md)                                 | `COHERE_API_KEY`                                    | ❌              |
| Fireworks                                    | [`langchain-fireworks`](../../integrations/chat/fireworks.md)                           | `FIREWORKS_API_KEY`                                 | ✅              |
| Together                                     | [`langchain-together`](../../integrations/chat/together.md)                             | `TOGETHER_API_KEY`                                  | ❌              |
| Meta                                         | [`langchain-meta`](https://github.com/langchain-ai/langchain-meta)                         | `MODEL_API_KEY`                                     | ✅              |
| Mistral AI                                   | [`langchain-mistralai`](../../integrations/chat/mistralai.md)                           | `MISTRAL_API_KEY`                                   | ✅              |
| DeepSeek                                     | [`langchain-deepseek`](../../integrations/chat/deepseek.md)                             | `DEEPSEEK_API_KEY`                                  | ✅              |
| IBM (watsonx.ai)                             | [`langchain-ibm`](../../integrations/chat/ibm_watsonx.md)                               | `WATSONX_APIKEY`                                    | ❌              |
| Nvidia                                       | [`langchain-nvidia-ai-endpoints`](../../integrations/chat/nvidia_ai_endpoints.md)       | `NVIDIA_API_KEY`                                    | ✅              |
| xAI                                          | [`langchain-xai`](../../integrations/chat/xai.md)                                       | `XAI_API_KEY`                                       | ✅              |
| Perplexity                                   | [`langchain-perplexity`](../../integrations/chat/perplexity.md)                         | `PERPLEXITY_API_KEY` (or `PPLX_API_KEY`)            | ✅              |
| OpenRouter                                   | [`langchain-openrouter`](../../integrations/chat/openrouter.md)                         | `OPENROUTER_API_KEY`                                | ✅              |
| LiteLLM                                      | [`langchain-litellm`](../../integrations/chat/litellm.md)                               | Per-provider (see [docs](https://docs.litellm.ai/)) | ❌              |

<details>
<summary>Configure Anthropic models on Gemini Enterprise Agent Platform</summary>

The `google_anthropic_vertex` provider runs Claude through Anthropic's Messages API on Gemini Enterprise Agent Platform. It uses Google Cloud Application Default Credentials (ADC) instead of an Anthropic API key.

To use the provider:

1. Install the Gemini Enterprise Agent Platform extra:

**In session**

```txt
     /install vertex
```

**Shell**

```bash
     dcode --install vertex
```

2. [Enable a Claude model in your Google Cloud project](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude), then configure ADC:

```bash
   gcloud auth application-default login
```

3. Set your Google Cloud project and location:

```bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   export GOOGLE_CLOUD_LOCATION="global"
```

   You can use `DEEPAGENTS_CODE_GOOGLE_CLOUD_PROJECT` and `DEEPAGENTS_CODE_GOOGLE_CLOUD_LOCATION` to scope these values to Deep Agents Code.

4. Select a Claude model with the `google_anthropic_vertex` provider:

**In session**

```txt
     /model google_anthropic_vertex:claude-sonnet-4-6
```

**Shell**

```bash
     dcode --model google_anthropic_vertex:claude-sonnet-4-6
```

Use `google_vertexai` for Google models. Claude models use Anthropic's Messages API and must use `google_anthropic_vertex` instead.

</details>

> [!TIP]
> You can scope any credential to Deep Agents Code by adding a `DEEPAGENTS_CODE_` prefix. For example, `DEEPAGENTS_CODE_OPENAI_API_KEY` takes priority over `OPENAI_API_KEY` within Deep Agents Code without affecting other tools. See [`DEEPAGENTS_CODE_` prefix](../code/configuration.md#deepagents_code_-prefix) for details.

> [!TIP]
> [Model profiles](../../langchain/models.md#model-profiles) provide model metadata used by the interactive `/model` switcher. If a model is missing from the switcher, pass the model name directly or add it via `config.toml`.

### Sign in with ChatGPT

The `openai_codex` provider lets you use OpenAI's Codex models with your paid **ChatGPT** subscription instead of an `OPENAI_API_KEY`. You sign in with your ChatGPT account, and it shows up as its own provider in both `/auth` and the `/model` switcher, separate from the API-key-based `openai` provider.

### Start the sign-in
Run `/auth` in any session and select **`openai_codex`**. Because ChatGPT signs you in through your browser, this starts a browser sign-in instead of asking for an API key.

### Authorize in your browser
Deep Agents Code opens your browser to the ChatGPT sign-in page. If it cannot open a browser (for example, over SSH), it also shows the sign-in URL on screen so you can copy it to a browser on another device.

### Select a Codex model
Once signed in, the Codex models appear in the `/model` switcher under the `openai_codex` provider. Switch to one directly with its spec:

```txt
/model openai_codex:gpt-5.5
```

Your sign-in persists across sessions. To check your status or sign out, run `/auth`, select `openai_codex`, and choose to re-authenticate or sign out.

> [!NOTE]
> `openai_codex` is separate from `openai`. To use OpenAI models with a standard API key instead, use the regular `openai` provider (e.g. `/model openai:gpt-5.5`).

> [!NOTE]
> Some provider-specific account types or key scopes may not work for API access. If a provider appears configured in `/auth` but requests still fail, verify that the account plan and API-key permissions match the provider's API requirements.

### Model routers and proxies

Model routers like [OpenRouter](https://openrouter.ai/) and [LiteLLM](https://docs.litellm.ai/) provide access to models from multiple providers through a single endpoint.

Use the dedicated integration packages for these services:

| Router     | Package                                                            | Config                                                                         |
| ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| OpenRouter | [`langchain-openrouter`](../../integrations/chat/openrouter.md) | `openrouter:<model>` (built-in, see [Provider reference](#provider-reference)) |
| LiteLLM    | [`langchain-litellm`](../../integrations/chat/litellm.md)       | `litellm:<model>` (built-in, see [Provider reference](#provider-reference))    |

**OpenRouter** is a built-in provider—install the extra and use it directly:

**In session**

```txt
/install openrouter
```

**Shell**

```bash
dcode --install openrouter
```

**LiteLLM** is also a built-in provider:

**In session**

```txt
/install litellm
```

**Shell**

```bash
dcode --install litellm
```

## Switch models

To switch models in Deep Agents Code, either:

1. **Use the interactive model switcher** with the `/model` command.

> [!NOTE]
>    Not all models appear here. If yours is missing, pass the model name directly (e.g. `/model gpt-5.5`) or add it to `config.toml`.

2. **Specify a model name directly** as an argument, e.g. `/model gpt-5.5`. You can use any model supported by the chosen provider, regardless of whether it appears in the list from option 1. The model name will be passed to the API request.
3. **Specify the model at launch** via `--model`, e.g.

```txt
   dcode --model openai:gpt-5.5
```

<details>
<summary>Model resolution order</summary>

When Deep Agents Code launches, it resolves which model to use in the following order:

1. **`--model` flag** always wins when provided.
2. **`[models].default`** in `~/.deepagents/config.toml`—the user's intentional long-term preference.
3. **`[models].recent`** in `~/.deepagents/config.toml`—the last model switched to via `/model`. Written automatically; never overwrites `[models].default`.
4. **Environment auto-detection**: falls back to the first available startup credential, checked in order: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `GOOGLE_CLOUD_PROJECT` (Gemini Enterprise Agent Platform).

This startup fallback intentionally checks only those four credentials. Other supported providers (for example, Groq) are still available via `--model`, `/model`, and saved defaults (`[models].default` / `[models].recent`).

</details>

### Which models appear in the switcher

The `/model` selector dynamically builds its list from installed provider packages. Expand below for the full criteria and troubleshooting.

<details>
<summary>How the switcher builds its model list</summary>

The interactive `/model` selector builds its list from installed provider packages and models configured in `config.toml`.

A model appears when:

1. The provider package is installed.
2. The model is available from the provider package, a local provider, or your `config.toml`.
3. The model profile does not mark text input or output as unsupported.

If a model is missing, use `/model <provider>:<model>` directly or add it to [`[models.providers.<name>].models`](/oss/deepagents/code/config-file#adding-models-to-the-interactive-switcher).

> [!TIP]
> Credential status does **not** affect whether a model is listed. You can still select a model with missing credentials. The provider reports an authentication error at request time.

</details>

### Open weights models

If you want to use an open weights model, there are two common paths depending on whether you prefer local or cloud-hosted inference.

**Local inference with Ollama** is the easiest way to get started for free, with no API key required:

1. [Install Ollama](https://ollama.com/) and pull a model, for example:

```bash
   ollama pull qwen3:4b
```

2. Install the Ollama extra:

**In session**

```txt
   /install ollama
```

**Shell**

```bash
   dcode --install ollama
```

3. Select the model:

**In session**

```txt
   /model
```

**Shell**

```bash
   dcode --model ollama:qwen3:4b
```

   Use the interactive switcher, or pass the model directly with `/model ollama:qwen3:4b`.

**Cloud-hosted open weights via Groq** gives you fast inference without running anything locally:

1. Get a free API key at [console.groq.com](https://console.groq.com/).

2. Install the Groq extra:

**In session**

```txt
   /install groq
```

**Shell**

```bash
   dcode --install groq
```

3. Select a model:

**In session**

```txt
   /model
```

**Shell**

```bash
   GROQ_API_KEY="your-api-key" dcode --model groq:openai/gpt-oss-120b
```

   Use the interactive switcher, or pass the model directly with `/model groq:openai/gpt-oss-120b`.

**Fireworks** is another popular cloud provider for open weights models:

**In session**

```txt
/install fireworks
/model
```

**Shell**

```bash
dcode --install fireworks
FIREWORKS_API_KEY="your-api-key" dcode --model fireworks:accounts/fireworks/models/deepseek-v4-pro
```

Use the interactive switcher, or pass the model directly with `/model fireworks:accounts/fireworks/models/deepseek-v4-pro`.

**Baseten** is another cloud provider for open weights models:

**In session**

```txt
/install baseten
/model
```

**Shell**

```bash
dcode --install baseten
BASETEN_API_KEY="your-api-key" dcode --model baseten:moonshotai/Kimi-K2.7-Code
```

Use the interactive switcher, or pass the model directly with `/model baseten:moonshotai/Kimi-K2.7-Code`.

> [!TIP]
> If you want a provider preinstalled at the same time as the CLI itself, use `DEEPAGENTS_CODE_EXTRAS` during the initial install:
>
> ```bash
> DEEPAGENTS_CODE_EXTRAS="fireworks" curl -LsSf https://langch.in/dcode | bash
> ```
>
> You can combine multiple providers: `DEEPAGENTS_CODE_EXTRAS="groq,fireworks,ollama"`. If Deep Agents Code is already installed, use `/install <extra>` in a session or `dcode --install <extra>` from the shell instead.

**Together**, **OpenRouter**, and **Hugging Face** (`langchain-huggingface`) are other options for cloud-hosted open weights. See the [Provider reference](#provider-reference) for credentials and package names.

### Set a default model

You can set a persistent default model that applies to all future CLI launches:

* **Via model selector:** Open `/model`, navigate to the desired model, and press `Ctrl+S` to pin it as the default. Pressing `Ctrl+S` again on the current default clears it.
* **Via command:** `/model --default provider:model` (e.g., `/model --default anthropic:claude-opus-4-8`)
* **Via config file:** Set `[models].default` in `~/.deepagents/config.toml` (see [Configuration](../code/configuration.md)).
* **From the shell:**

```bash
  dcode --default-model anthropic:claude-opus-4-8
```

To view the current default:

```bash
dcode --default-model
```

To clear the default:

* **From the shell:**

```bash
  dcode --clear-default-model
```

* **Via command:** `/model --default --clear`

* **Via model selector:** Press `Ctrl+S` on the currently pinned default model.

Without a default, Deep Agents Code uses the most recently used model.

### Model parameters

Pass extra constructor kwargs to the model—sampling controls, reasoning/thinking budgets, context window sizes, request timeouts, and anything else the underlying chat-model class accepts. Three places to set them, in priority order (highest first):

1. **One-off at launch with `--model-params`.** JSON string, session-only:

```bash
   # OpenAI reasoning effort
   dcode --model openai:gpt-5.5 --model-params '{"reasoning": {"effort": "high"}}'

   # Anthropic extended thinking
   dcode --model anthropic:claude-opus-4-8 --model-params '{"thinking": {"type": "enabled", "budget_tokens": 10000}, "max_tokens": 16000}'
```

2. **Mid-session via `/model --model-params`.** Same JSON syntax—swaps params (and optionally the model) without restarting:

```txt
   /model --model-params '{"temperature": 0.7}' anthropic:claude-opus-4-8
   /model --model-params '{"num_ctx": 16384}'           # opens selector, applies params to choice
```

3. **Persistent in `config.toml`.** Provider-level defaults (with optional per-model sub-tables) that apply on every launch:

```toml
   [models.providers.anthropic.params]
   thinking = { type = "enabled", budget_tokens = 10000 }
   max_tokens = 16000

   [models.providers.openai.params]
   reasoning = { effort = "high", summary = "auto" }
   output_version = "responses/v1"

   [models.providers.ollama.params]
   num_ctx = 16384
   temperature = 0

   # Per-model override—wins over provider-level keys
   [models.providers.ollama.params."qwen3:4b"]
   temperature = 0.5
```

CLI flags override config-file `params` and are session-only (mid-session changes are not persisted). Per-model sub-tables in `config.toml` override provider-level keys (shallow merge—see [Model constructor params](../code/config-file.md#model-constructor-params) for full semantics). `--model-params` cannot be combined with `--default`.

For retry counts, prefer `--max-retries` or the top-level [`[retries]` config](/oss/deepagents/code/config-file#retries).

> [!TIP]
> Any kwarg accepted by the underlying chat-model constructor is valid. Refer to the provider's reference docs for the full list—e.g. [`ChatAnthropic`](https://reference.langchain.com/python/langchain-anthropic/langchain_anthropic/chat_models/ChatAnthropic), [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/langchain_openai/chat_models/base/ChatOpenAI), [`ChatOllama`](https://reference.langchain.com/python/langchain-ollama/langchain_ollama/chat_models/ChatOllama). Unknown kwargs are forwarded to the upstream API request, so newly released parameters work without a CLI update.

> [!NOTE]
> Do not put credentials (`api_key`) in `params`—use [`api_key_env`](../code/config-file.md#provider-configuration) to point at an environment variable instead.

To override fields on the model's runtime *profile* (`max_input_tokens`, `tool_calling`, capability flags)—distinct from constructor params—see [Profile overrides](../code/config-file.md#profile-overrides-advanced).

## Advanced configuration

For detailed configuration of provider params, profile overrides, custom base URLs, compatible APIs, arbitrary providers, and lifecycle hooks, see [Config file](../code/config-file.md) and [Hooks](../code/hooks.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/providers.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
