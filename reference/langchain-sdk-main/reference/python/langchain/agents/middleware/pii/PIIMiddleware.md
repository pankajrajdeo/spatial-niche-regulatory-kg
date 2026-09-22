---
title: "PIIMiddleware"
description: "Detect and handle Personally Identifiable Information (PII) in conversations."
source: "https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, pii, piimiddleware]
---

# PIIMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware)

Detect and handle Personally Identifiable Information (PII) in conversations.

This middleware detects common PII types and applies configurable strategies
to handle them. It can detect emails, credit cards, IP addresses, MAC addresses, and
URLs in both user input and agent output.

Built-in PII types:

- `email`: Email addresses
- `credit_card`: Credit card numbers (validated with Luhn algorithm)
- `ip`: IP addresses (validated with stdlib)
- `mac_address`: MAC addresses
- `url`: URLs (both `http`/`https` and bare URLs)

Strategies:

- `block`: Raise an exception when PII is detected
- `redact`: Replace PII with `[REDACTED_TYPE]` placeholders
- `mask`: Partially mask PII (e.g., `****-****-****-1234` for credit card)
- `hash`: Replace PII with deterministic hash (e.g., `<email_hash:a1b2c3d4>`)

Strategy Selection Guide:

| Strategy | Preserves Identity? | Best For                                |
| -------- | ------------------- | --------------------------------------- |
| `block`  | N/A                 | Avoid PII completely                    |
| `redact` | No                  | General compliance, log sanitization    |
| `mask`   | No                  | Human readability, customer service UIs |
| `hash`   | Yes (pseudonymous)  | Analytics, debugging                    |

## Signature

```python
PIIMiddleware(
    self,
    pii_type: Literal['email', 'credit_card', 'ip', 'mac_address', 'url'] | str,
    *,
    strategy: Literal['block', 'redact', 'mask', 'hash'] = 'redact',
    detector: Callable[[str], list[PIIMatch]] | str | None = None,
    apply_to_input: bool = True,
    apply_to_output: bool = False,
    apply_to_tool_results: bool = False,
)
```

## Description

**Example:**

```python
from langchain.agents.middleware import PIIMiddleware
from langchain.agents import create_agent

# Redact all emails in user input
agent = create_agent(
    "openai:gpt-5.5",
    middleware=[
        PIIMiddleware("email", strategy="redact"),
    ],
)

# Use different strategies for different PII types
agent = create_agent(
    "openai:gpt-5.5",
    middleware=[
        PIIMiddleware("credit_card", strategy="mask"),
        PIIMiddleware("url", strategy="redact"),
        PIIMiddleware("ip", strategy="hash"),
    ],
)

# Custom PII type with regex
agent = create_agent(
    "openai:gpt-5.5",
    middleware=[
        PIIMiddleware("api_key", detector=r"sk-[a-zA-Z0-9]{32}", strategy="block"),
    ],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pii_type` | `Literal['email', 'credit_card', 'ip', 'mac_address', 'url'] \| str` | Yes | Type of PII to detect.  Can be a built-in type (`email`, `credit_card`, `ip`, `mac_address`, `url`) or a custom type name. |
| `strategy` | `Literal['block', 'redact', 'mask', 'hash']` | No | How to handle detected PII.  Options:  * `block`: Raise `PIIDetectionError` when PII is detected * `redact`: Replace with `[REDACTED_TYPE]` placeholders * `mask`: Partially mask PII (show last few characters) * `hash`: Replace with deterministic hash (format: `<type_hash:digest>`) (default: `'redact'`) |
| `detector` | `Callable[[str], list[PIIMatch]] \| str \| None` | No | Custom detector function or regex pattern.  * If `Callable`: Function that takes content string and returns     list of `PIIMatch` objects * If `str`: Regex pattern to match PII * If `None`: Uses built-in detector for the `pii_type` (default: `None`) |
| `apply_to_input` | `bool` | No | Whether to check user messages before model call. (default: `True`) |
| `apply_to_output` | `bool` | No | Whether to check AI messages after model call.  When `True`, a stream transformer is also installed so that every wire surface of an agent run is redacted in flight:  * Streamed AI text deltas (`content-block-delta` of type   `text-delta`) * Streamed tool-call arguments (`content-block-delta`   with `tool_call_chunk` / `server_tool_call_chunk`   fields, plus the finalized `tool_call` content block   on `content-block-finish`) * Tool execution events on the `tools` channel   (`tool-started.input`, `tool-output-delta`,   `tool-finished.output`, `tool-error.message`) * State snapshots on the `values` channel — message   lists are walked and each message's `.content` is   redacted on a fresh copy (state itself stays intact   for `before_model` / `after_model` to act on   independently)  State-level redaction via `after_model` (and `before_model` with `apply_to_tool_results`) remains the canonical enforcer; the streaming transformer ensures consumers reading `astream_events(version="v3")` or `run.messages` / `run.tool_calls` / `run.values` never see PII on the wire. (default: `False`) |
| `apply_to_tool_results` | `bool` | No | Whether to check tool result messages after tool execution. (default: `False`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    pii_type: Literal['email', 'credit_card', 'ip', 'mac_address', 'url'] | str,
    *,
    strategy: Literal['block', 'redact', 'mask', 'hash'] = 'redact',
    detector: Callable[[str], list[PIIMatch]] | str | None = None,
    apply_to_input: bool = True,
    apply_to_output: bool = False,
    apply_to_tool_results: bool = False,
) -> None
```

| Name | Type |
|------|------|
| `pii_type` | `Literal['email', 'credit_card', 'ip', 'mac_address', 'url'] \| str` |
| `strategy` | `Literal['block', 'redact', 'mask', 'hash']` |
| `detector` | `Callable[[str], list[PIIMatch]] \| str \| None` |
| `apply_to_input` | `bool` |
| `apply_to_output` | `bool` |
| `apply_to_tool_results` | `bool` |

## Properties

- `apply_to_input`
- `apply_to_output`
- `apply_to_tool_results`
- `pii_type`
- `strategy`
- `detector`
- `transformers`
- `name`

## Methods

- [`before_model()`](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/before_model)
- [`abefore_model()`](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/abefore_model)
- [`after_model()`](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/aafter_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/pii.py#L492)
