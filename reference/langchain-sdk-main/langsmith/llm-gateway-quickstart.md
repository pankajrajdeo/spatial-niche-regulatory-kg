---
title: "LLM Gateway quickstart"
description: "Call models across providers with one LangSmith API key, then view the trace and set a spend limit."
source: "https://docs.langchain.com/langsmith/llm-gateway-quickstart"
category: "docs"
tags: [docs, langsmith, llm-gateway-quickstart]
---

# LLM Gateway quickstart

> Call models across providers with one LangSmith API key, then view the trace and set a spend limit.

> [!NOTE]
> The LLM Gateway is in [beta](release-stages.md).

The LLM Gateway calls models across configured providers through one endpoint with one [LangSmith API key](create-account-api-key.md). Send a request, view its trace, then set a spend limit.

> [!NOTE]
> An administrator must [enable the gateway, add a provider secret, and grant access](llm-gateway-admin-setup.md) once for your workspace. After that, you need only a workspace-scoped LangSmith API key attached to a role with the `gateway:invoke` and `workspaces:read` [permissions](organization-workspace-operations.md).

### Send a request
A gateway call is an ordinary model request pointed at the gateway base URL and authenticated with your LangSmith API key. Use Chat completions to call the gateway from an application you already have, or Deep Agents to build an agent that routes through it.

#### Chat completions
Point any OpenAI-compatible client at `https://gateway.smith.langchain.com/v1` and set `model` to a provider-prefixed ID.

**cURL**

```bash
export LANGSMITH_API_KEY="lsv2_..."

curl https://gateway.smith.langchain.com/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-opus-5","messages":[{"role":"user","content":"Explain what an LLM gateway does in one sentence."}]}'
```

**Python**

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://gateway.smith.langchain.com/v1",
    api_key=os.environ["LANGSMITH_API_KEY"],
)
response = client.chat.completions.create(
    model="anthropic/claude-opus-5",
    messages=[{"role": "user", "content": "Explain what an LLM gateway does in one sentence."}],
)
print(response.choices[0].message.content)
```

**TypeScript**

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://gateway.smith.langchain.com/v1",
  apiKey: process.env.LANGSMITH_API_KEY,
});
const response = await client.chat.completions.create({
  model: "anthropic/claude-opus-5",
  messages: [{ role: "user", content: "Explain what an LLM gateway does in one sentence." }],
});
console.log(response.choices[0].message.content);
```

The same endpoint also accepts Anthropic Messages and OpenAI Responses requests. See [API formats](llm-gateway-api-formats.md).

#### Deep Agents
Set `LANGSMITH_GATEWAY` to route every supported chat model in the process through the gateway.

**Python**

```python
# pip install "deepagents>=0.1.0"
# export LANGSMITH_API_KEY="lsv2_..."
# export LANGSMITH_GATEWAY="true"
from deepagents import create_deep_agent

agent = create_deep_agent(model="anthropic:claude-opus-5")
result = agent.invoke({"messages": [{"role": "user", "content": "Explain what an LLM gateway does in one sentence."}]})
print(result["messages"][-1].content)
```

**TypeScript**

```typescript
// npm install deepagents
// export LANGSMITH_API_KEY="lsv2_..."
// export LANGSMITH_GATEWAY="true"
import { createDeepAgent } from "deepagents";

const agent = createDeepAgent({ model: "anthropic:claude-opus-5" });
const result = await agent.invoke({
  messages: [{ role: "user", content: "Explain what an LLM gateway does in one sentence." }],
});
console.log(result.messages[result.messages.length - 1].content);
```

To route specific calls rather than all calls, use the standard endpoint in the Chat completions tab and set `model` to a provider-prefixed ID.

### View the trace
Open [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-llm-gateway-quickstart) and go to the tracing project named `gateway` or `gateway-<short_api_key>-<api_key_id>` in your workspace. Your request appears there with its token counts, cost, and latency.

### Set a spend limit
Go to **LLM Gateway** in LangSmith and create a spend policy, such as a daily \$10 cap on your API key. Once the cap is reached, the gateway returns a `402` with a message naming the policy that blocked the request:

```json
{"error": "Request blocked by gateway policies: R&D Spend Cap"}
```

For the full guide, see [Spend policies](llm-gateway-spend-policies.md).

These examples use the US gateway. For the EU, APAC, and AWS hostnames, see [Use a regional gateway](llm-gateway-how-it-works.md#use-a-regional-gateway). For BYOC, see [Use a BYOC data plane](llm-gateway-how-it-works.md#use-a-byoc-data-plane).

## Next steps

* [Overview](llm-gateway.md): what the gateway provides, how credentials are managed, and when to use the standard API.
* [How the gateway works](llm-gateway-how-it-works.md): what happens to each request, how credentials resolve, and where the gateway is available.
* [API formats](llm-gateway-api-formats.md): use Chat Completions, Messages, or Responses through the standard endpoint.
* [Set up coding agents](llm-gateway-coding-agents.md): route Claude Code, Codex, Gemini CLI, or Deep Agents Code through the gateway.
* [Direct model access](llm-gateway-direct-model-access.md): use provider-native request and response formats.
* [Prompt Hub with the gateway](manage-prompts-programmatically.md#use-with-the-langsmith-gateway): route Prompt Hub model calls through the gateway.
* [Data policy](llm-gateway-data-policy.md): prevent sensitive data from reaching providers.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
