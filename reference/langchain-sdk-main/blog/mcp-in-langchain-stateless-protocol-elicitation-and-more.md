---
title: "MCP in LangChain: Stateless Protocol, Elicitation, and More!"
description: "MCP support now lives in langchain.mcp, built on FastMCP for the 2026-07-28 spec, with elicitation handled as a LangGraph interrupt and tool lists cached."
source: "https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more"
category: "blog"
published: "2026-09-03T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, mcp-in-langchain-stateless-protocol-elicitation-and-more]
---

# MCP in LangChain: Stateless Protocol, Elicitation, and More!

MCP's official [Tier 1 SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk#available-sdks) are pulling close to half a billion [downloads a month,](https://pypistats.org/packages/mcp) and usage is climbing faster still: MCP tool calls from ChatGPT users are [up 98x across 2026](https://x.com/mxstbr/status/2094541583307678165), having more than doubled in August alone.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a99a85ae6d25387709b0017_mcp-tool-call-growth.png)

Model Context Protocol (MCP) is the most popular way to connect agents to tools. In July, the protocol got its [largest rewrite since launch](https://blog.modelcontextprotocol.io/posts/2026-07-28/). We've revamped MCP support in LangChain to match the new spec and the growing demand behind it.

Three things have changed:

- **MCP support moves into the main package.** It lives in `langchain.mcp` now, not a separate `langchain-mcp-adapters` install.
- **It's built on **[**FastMCP**](https://gofastmcp.com/)**.** Transports, auth, connection management, and protocol negotiation come from the client underneath, so servers on the old and the new spec both work.
- **Elicitation via interrupts and client-side caching are now supported.** The new spec turned a server's mid-call elicitation into a retry-able round, which we surface as a LangGraph interrupt. It also made tool lists cacheable, so a tool catalog no longer has to be re-fetched on every run.

## The new, stateless spec

Historically (with the old spec) every MCP call ran through a protocol built around sessions. Calling a tool over MCP used to mean opening a session first. The client and server shook hands, the server handed back a session ID, and every later request had to carry it, which pinned that client to the one server instance that issued it.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a99a89cedef6b0a2f29359a_mcp-request-flow.png)

Running a remote server at any scale meant sticky routing and a shared session store.

This all changed in the new MCP spec, which enabled a stateless core. The MCP team [describes](https://blog.modelcontextprotocol.io/posts/2026-07-28/) the stateless core as one of the most highly-requested features from developers, who wanted better reliability and scalability out of their servers. In the new spec there is nothing left to pin. A redeploy no longer kills live sessions, because there are none.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a99a8aee0028cebca2f82a6_mcp-stateless-topology.png)

That opened up two things, and both are now in `langchain.mcp`:

- **Caching**: a server can say how long its tool list stays fresh, so clients stop re-fetching it every run.
- **Elicitation**: a tool can pause to ask the caller something, like confirming a delete or supplying a parameter the model left out, without holding a connection open while it waits.

Read the MCP team's [announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) for more information on the revision

## First-class MCP support

We moved MCP support into `langchain` so it's first class for agents. It installs with the `mcp` extra:`‍`

```
pip install "langchain[mcp]"
```

Coming from the old package, `MultiServerMCPClient` collapses into a single `MCPAdapter` class. Read the [migration guide](../migrate/langchain-mcp-adapters.md) for more detailed instructions on how to adopt. Basic usage looks like this:`‍`

```
from deepagents import create_deep_agent
from langchain.mcp import MCPAdapter

async def main():
    async with MCPAdapter("https://example.com/mcp") as adapter:
        agent = create_deep_agent(
            model="google_genai:gemini-3.8-flash", tools=
            await adapter.list_tools()
        )
        return await agent.ainvoke(
            {"messages": [{"role": "user", "content": "..."}]}
        )
```

The tools are ordinary LangChain tools, so they go anywhere tools go: [`create_deep_agent`](https://reference.langchain.com/python/deepagents/graph/create_deep_agent), [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent), or a graph you wired yourself.

## Built on FastMCP

[FastMCP](https://gofastmcp.com/clients/client) provides clean abstractions over the transport layer: [connections](https://gofastmcp.com/clients/transports), [authentication](https://gofastmcp.com/clients/auth/oauth), [caching](https://gofastmcp.com/clients/client#response-caching), and [protocol negotiation](https://gofastmcp.com/clients/client#protocol-negotiation). Its client surface is available to you directly.

MCP now has two distinct "eras" of the protocol, which means the client needs to be able to negotiate with two distinct protocols. FastMCP does that per connection: it tries the new protocol and falls back to the handshake for a server that hasn't upgraded. Your code doesn't change either way. [What's new in FastMCP 4](https://gofastmcp.com/getting-started/whats-new) has the details.

Give each server its own connection with a `ClientGroup` and each keeps the best era it supports, along with its own credentials:`‍`

```
from langchain.mcp import MCPAdapter
from deepagents import create_deep_agent
from fastmcp import ClientGroup

group = ClientGroup(
    {
        # Hasn't upgraded yet, so pin the handshake era. Auth is OAuth 2.1.
        "billing": Client("https://billing.internal/mcp", mode="legacy", auth="oauth"),
        # Negotiates the newest era it understands, with a bearer token.
        "docs": Client("https://docs.internal/mcp", mode="auto", auth=docs_token),
    }
)

async with MCPAdapter(group) as adapter:
    # billing_search and docs_search, so the two stay distinct.
    tools = await adapter.list_tools()
    agent = create_deep_agent(model="google_genai:gemini-3.8-flash", tools=tools)
```

Tool names are prefixed with the server they came from, so a `search` tool on each server arrives as `billing_search` and `docs_search`. If your servers don't need to differ from each other, a plain config dict is enough; the [connections guide](../langchain/mcp/connections.md) covers when to use which.

The rest of the client is yours to use directly:

- [**Auth**](https://gofastmcp.com/clients/auth/oauth): bearer tokens, the full OAuth 2.1 flow, machine-to-machine credentials, CIMD, or any `httpx2.Auth`
- [**Transports**](https://gofastmcp.com/clients/transports): streamable HTTP, stdio, and in-memory, inferred from the target or configured for headers, SSL, and a shared `httpx2` pool
- [**Caching**](https://gofastmcp.com/clients/client#response-caching): list results held for as long as the server's TTL allows
- [**Progress and logs**](https://gofastmcp.com/clients/progress): notifications from long-running calls

FastMCP also makes it easy to [build](https://gofastmcp.com/servers/server) and [test](https://gofastmcp.com/servers/testing) servers of your own. A `FastMCP` instance is a valid adapter target, with no subprocess and no socket, so an agent can run against a real MCP server in-process.

## Elicitation via interrupts

Elicitation is MCP's human-in-the-loop support: a tool that can't finish without asking the caller something first. The stateless spec turned that into an ordinary request the client retries with an answer attached, which let us support it with the interrupt primitive you already use. The run pauses, whoever is reviewing the agent's work answers, and it resumes:`‍`

```
paused = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "Book a table for 4."}]}, config
)
question = paused["__interrupt__"][0].value.requests[0]

answer = {"action": "accept", "content": {"date": "2026-09-14"}}
result = await agent.ainvoke(
    Command(resume={"responses": {question["key"]: answer}}), config
)
```

`‍`No setup beyond a checkpointer, so the paused run has somewhere to wait. The [elicitation docs](https://docs.langchain.com/oss/python/langchain/mcp/elicitation) cover declining a question, and gating destructive tools behind the same approval flow.

## Client-side caching

Every agent run starts by discovering what tools exist, which means a round trip request to discover tools before the model sees anything. Servers can now say how long their tool list stays fresh, so the catalog can be served from cache instead. `cache=True` gives you an in-memory cache that respects those hints:

```
from fastmcp import Client
from langchain.mcp import MCPAdapter

client = Client("https://billing.internal/mcp", cache=True)

async with MCPAdapter(client) as adapter:
    # "use" is the default once a cache is configured: serve a cached catalog
    # while the server's TTL holds, and store what it does fetch.
    tools = await adapter.list_tools(cache_mode="use")
    agent = create_deep_agent(
        model="google_genai:gemini-3.8-flash",
        tools=tools
    )
```

The cache belongs to the client, so one client per caller keeps catalogs from crossing. See [response caching](https://gofastmcp.com/clients/client#response-caching) for TTLs, shared stores, and the other cache modes.

## Get started

```
uv pip install "langchain[mcp]"
```

The namespace requires `langchain[mcp]&gt;=1.4.0` and is in beta, so the API may still change. We're shipping Python support today, with TypeScript soon to follow.

- [MCP in LangChain](../langchain/mcp.md): quickstart, connections, auth, elicitation, and tool results
- [Migrate from `langchain-mcp-adapters`](../migrate/langchain-mcp-adapters.md): every public feature mapped to its replacement
- [FastMCP client docs](https://gofastmcp.com/clients/client): the client underneath
- [MCP `2026-07-28` specification](https://modelcontextprotocol.io/specification/2026-07-28)
