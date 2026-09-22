---
title: "init_chat_model"
description: "Initialize a chat model from any supported provider using a unified interface."
source: "https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model"
category: "reference"
tags: [reference, langchain, chat_models, base, init_chat_model]
---

# init_chat_model

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model)

Initialize a chat model from any supported provider using a unified interface.

**Two main use cases:**

1. **Fixed model** – specify the model upfront and get a
    ready-to-use chat model.
2. **Configurable model** – choose to specify parameters
    (including model name) at runtime via `config`. Makes it easy to
    switch between models/providers without changing your code

!!! note "Installation requirements"

    Requires the integration package for the chosen model provider to
    be installed.

    See the `model_provider` parameter below for specific package names
    (e.g., `pip install langchain-openai`).

    Refer to the [provider integration's API reference](../../../../../integrations/providers.md)
    for supported model parameters to use as `**kwargs`.

## Signature

```python
init_chat_model(
    model: str | None = None,
    *,
    model_provider: str | None = None,
    configurable_fields: Literal['any'] | list[str] | tuple[str, ...] | None = None,
    config_prefix: str | None = None,
    **kwargs: Any = {},
) -> BaseChatModel | _ConfigurableModel
```

## Description

???+ example "Initialize a non-configurable model"

```python
    # pip install langchain langchain-openai

    from langchain.chat_models import init_chat_model

    gpt_5 = init_chat_model("openai:gpt-5.5", temperature=0)
    gpt_5.invoke("what's your name")
```

??? example "Partially configurable model with no default"

```python
    # pip install langchain langchain-openai

    from langchain.chat_models import init_chat_model

    # (We don't need to specify configurable=True if a model isn't specified.)
    configurable_model = init_chat_model(temperature=0)

    # Use GPT-5.5 to generate the response
    configurable_model.invoke(
        "what's your name",
        config={"configurable": {"model": "gpt-5.5"}},
    )
```

??? example "Fully configurable model with a default"

```python
    # pip install langchain langchain-openai langchain-anthropic

    from langchain.chat_models import init_chat_model

    configurable_model_with_default = init_chat_model(
        "openai:gpt-5.5",
        configurable_fields="any",  # This allows us to configure other params like temperature, max_tokens, etc at runtime.
        config_prefix="foo",
        temperature=0,
    )

    configurable_model_with_default.invoke("what's your name")
    # GPT-5.5 response with temperature 0 (as set in default)

    # Invoke overriding model and temperature at runtime via config.
    # Note the use of the "foo_" prefix on the config keys, which matches
    # the config_prefix we set when initializing the model.
    configurable_model_with_default.invoke(
        "what's your name",
        config={
            "configurable": {
                "foo_model": "anthropic:claude-opus-4-7",
                "foo_temperature": 0.6,
            }
        },
    )
```

??? example "Bind tools to a configurable model"

    You can call any chat model declarative methods on a configurable model
    in the same way that you would with a normal model:

```python
    # pip install langchain langchain-openai langchain-anthropic

    from langchain.chat_models import init_chat_model
    from pydantic import BaseModel, Field

    class GetWeather(BaseModel):
        '''Get the current weather in a given location'''

        location: str = Field(..., description="The city and state, e.g. San Francisco, CA")

    class GetPopulation(BaseModel):
        '''Get the current population in a given location'''

        location: str = Field(..., description="The city and state, e.g. San Francisco, CA")

    configurable_model = init_chat_model(
        "gpt-5.5", configurable_fields=("model", "model_provider"), temperature=0
    )

    configurable_model_with_tools = configurable_model.bind_tools(
        [
            GetWeather,
            GetPopulation,
        ]
    )
    configurable_model_with_tools.invoke(
        "Which city is hotter today and which is bigger: LA or NY?"
    )
    # Use GPT-5.5

    configurable_model_with_tools.invoke(
        "Which city is hotter today and which is bigger: LA or NY?",
        config={"configurable": {"model": "claude-opus-4-7"}},
    )
    # Use Opus 4.7
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| None` | No | Name of the model to use, with provider prefix — e.g., `'openai:gpt-5.5'`.  A bare model name (e.g., `'claude-opus-4-7'`) is also accepted; we will attempt to infer the provider from the prefix using the mapping below. Inference is best-effort and not guaranteed, so prefer the prefixed form when possible.  Prefer pinned model IDs over moving aliases (e.g., `'claude-haiku-4-5-20251001'` rather than `'claude-haiku-4-5'`) so behavior does not drift if the alias is repointed upstream.  Inferred providers by prefix (case-insensitive):  - `gpt-...` \| `o1...` \| `o3...`               -> `openai` - `claude...`                                 -> `anthropic` - `amazon....` \| `anthropic....` \| `meta....` -> `bedrock` - `gemini...`                                 -> `google_vertexai` (default changes in next major; pass `model_provider` to lock in) - `command...`                                -> `cohere` - `accounts/fireworks...`                     -> `fireworks` - `mistral...` \| `mixtral...`                 -> `mistralai` - `deepseek...`                               -> `deepseek` - `grok...`                                   -> `xai` - `sonar...`                                  -> `perplexity` - `solar...`                                  -> `upstage` - `chatgpt...` \| `text-davinci...`            -> `openai` (legacy) (default: `None`) |
| `model_provider` | `str \| None` | No | Provider of the model, passed separately instead of as a prefix on `model`.  Equivalent to the prefix form — e.g., `model='claude-sonnet-4-5', model_provider='anthropic'` behaves the same as `model='anthropic:claude-sonnet-4-5'`.  Prefer the prefix form on `model` for most usage. Reach for this kwarg when:  - The provider is dynamic (read from config or an env var) and     you'd otherwise concatenate strings. - You want `model` and `model_provider` to be independently     swappable at runtime via `configurable_fields` (e.g., to route     the same model name to a different host).  Supported values and the integration package each requires:  - `openai`                  -> [`langchain-openai`](../../../../../integrations/providers/openai.md) - `anthropic`               -> [`langchain-anthropic`](../../../../../integrations/providers/anthropic.md) - `azure_openai`            -> [`langchain-openai`](../../../../../integrations/providers/openai.md) - `azure_ai`                -> [`langchain-azure-ai`](../../../../../integrations/providers/microsoft.md) - `google_vertexai`         -> [`langchain-google-vertexai`](../../../../../integrations/providers/google.md) - `google_genai`            -> [`langchain-google-genai`](../../../../../integrations/providers/google.md) - `anthropic_bedrock`       -> [`langchain-aws`](../../../../../integrations/providers/aws.md) - `bedrock`                 -> [`langchain-aws`](../../../../../integrations/providers/aws.md) - `bedrock_converse`        -> [`langchain-aws`](../../../../../integrations/providers/aws.md) - `cohere`                  -> [`langchain-cohere`](../../../../../integrations/providers/cohere.md) - `fireworks`               -> [`langchain-fireworks`](../../../../../integrations/providers/fireworks.md) - `together`                -> [`langchain-together`](../../../../../integrations/providers/together.md) - `mistralai`               -> [`langchain-mistralai`](../../../../../integrations/providers/mistralai.md) - `huggingface`             -> [`langchain-huggingface`](../../../../../integrations/providers/huggingface.md) - `groq`                    -> [`langchain-groq`](../../../../../integrations/providers/groq.md) - `ollama`                  -> [`langchain-ollama`](../../../../../integrations/providers/ollama.md) - `google_anthropic_vertex` -> [`langchain-google-vertexai`](../../../../../integrations/providers/google.md) - `deepseek`                -> [`langchain-deepseek`](../../../../../integrations/providers/deepseek.md) - `ibm`                     -> [`langchain-ibm`](../../../../../integrations/providers/ibm.md) - `nvidia`                  -> [`langchain-nvidia-ai-endpoints`](../../../../../integrations/providers/nvidia.md) - `xai`                     -> [`langchain-xai`](../../../../../integrations/providers/xai.md) - `openrouter`              -> [`langchain-openrouter`](../../../../../integrations/providers/openrouter.md) - `perplexity`              -> [`langchain-perplexity`](../../../../../integrations/providers/perplexity.md) - `upstage`                 -> [`langchain-upstage`](../../../../../integrations/providers/upstage.md) - `baseten`                 -> [`langchain-baseten`](../../../../../integrations/providers/baseten.md) - `litellm`                 -> [`langchain-litellm`](../../../../../integrations/providers/litellm.md) - `meta`                    -> [`langchain-meta`](https://pypi.org/project/langchain-meta) - `langsmith`               -> [`langchain-openai`](../../../../../langsmith/llm-gateway.md) (default: `None`) |
| `configurable_fields` | `Literal['any'] \| list[str] \| tuple[str, ...] \| None` | No | Which model parameters are configurable at runtime:  - `None`: No configurable fields (i.e., a fixed model). - `'any'`: All fields are configurable. **See security note below.** - `list[str] \| Tuple[str, ...]`: Specified fields are configurable.  Fields are assumed to have `config_prefix` stripped if a `config_prefix` is specified.  If `model` is specified, then defaults to `None`.  If `model` is not specified, then defaults to `("model", "model_provider")`.  !!! warning "Security note"      Setting `configurable_fields="any"` means fields like `api_key`,     `base_url`, etc., can be altered at runtime, potentially redirecting     model requests to a different service/user.      Make sure that if you're accepting untrusted configurations that you     enumerate the `configurable_fields=(...)` explicitly. (default: `None`) |
| `config_prefix` | `str \| None` | No | Optional prefix for configuration keys.  Useful when you have multiple configurable models in the same application.  If `'config_prefix'` is a non-empty string then `model` will be configurable at runtime via the `config["configurable"]["{config_prefix}_{param}"]` keys. See examples below.  If `'config_prefix'` is an empty string then model will be configurable via `config["configurable"]["{param}"]`. (default: `None`) |
| `**kwargs` | `Any` | No | Additional model-specific keyword args to pass to the underlying chat model's `__init__` method. Common parameters include:  - `temperature`: Model temperature for controlling randomness. - `max_tokens`: Maximum number of output tokens. - `timeout`: Maximum time (in seconds) to wait for a response. - `max_retries`: Maximum number of retry attempts for failed requests. - `base_url`: Custom API endpoint URL. - `rate_limiter`: A     [`BaseRateLimiter`][langchain_core.rate_limiters.BaseRateLimiter]     instance to control request rate.  Refer to the specific model provider's [integration reference](https://reference.langchain.com/python/integrations/) for all available parameters. (default: `{}`) |

## Returns

`BaseChatModel | _ConfigurableModel`

A `BaseChatModel` corresponding to the `model_name` and `model_provider`
specified if configurability is inferred to be `False`.
If configurable, a chat model emulator that initializes the
underlying model at runtime once a config is passed in.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/chat_models/base.py#L230)
