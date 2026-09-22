---
title: "Get started with Studio"
description: "Studio in the LangSmith Deployment UI supports connecting to two types of graphs:"
source: "https://docs.langchain.com/langsmith/quick-start-studio"
category: "docs"
tags: [docs, langsmith, quick-start-studio]
---

# Get started with Studio

[Studio](studio.md) in the [LangSmith Deployment UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-quick-start-studio) supports connecting to two types of graphs:

* Graphs deployed on [cloud or self-hosted](#deployed-graphs).
* Graphs running locally with [Agent Server](#local-development-server).

## Deployed graphs

Studio is accessed in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-quick-start-studio) from the **Deployments** navigation.

For applications that are [deployed](deployment-quickstart.md), you can access Studio as part of that deployment. To do so, navigate to the deployment in the UI and select **Studio**.

This will load Studio connected to your live deployment, allowing you to create, read, and update the [threads](../langgraph/checkpointers.md#threads), [assistants](assistants.md), and [memory](../concepts/memory.md) in that deployment.

## Local development server

### Prerequisites

To test your application locally using Studio:

* Follow the [local application quickstart](local-dev-testing.md) first.
* If you don't want data [traced](observability-concepts.md#traces) to LangSmith, set `LANGSMITH_TRACING=false` in your application's `.env` file. With tracing disabled, no data leaves your local server.

### Setup

1. Install the [LangGraph CLI](cli.md):

**pip**

```bash
   pip install -U "langgraph-cli[inmem]"
   langgraph dev
```

**uv**

```bash
   uv add "langgraph-cli[inmem]"
   langgraph dev
```

**npm**

```bash
   npx @langchain/langgraph-cli dev
```

> [!WARNING]
>    **Browser Compatibility**
>    Safari blocks `localhost` connections to Studio. To work around this, run the command with `--tunnel` to access Studio via a secure tunnel. You'll need to manually add the tunnel URL to allowed origins by clicking **Connect to a local server** in the Studio UI. See the [troubleshooting guide](troubleshooting-studio.md#safari-connection-issues) for steps.

   This will start the Agent Server locally, running in-memory. The server will run in watch mode, listening for and automatically restarting on code changes. Read this [reference](cli.md#dev) to learn about all the options for starting the API server.

   You will see the following logs:

```
   > Ready!
   >
   > - API: [http://localhost:2024](http://localhost:2024/)
   >
   > - Docs: http://localhost:2024/docs
   >
   > - LangSmith Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

   Once running, you will automatically be directed to Studio.

2. For a running server, access the Dbugger with one of the following:

   1. Directly navigate to the following URL: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`.
   2. Navigate to **Deployments** in the UI, click the **Studio** button on a deployment, enter `http://127.0.0.1:2024` and click **Connect**.

   If running your server at a different host or port, update the `baseUrl` to match.

### (Optional) Attach a debugger

For step-by-step debugging with breakpoints and variable inspection, run the following:

**pip**

```bash
# Install debugpy package
pip install debugpy
# Start server with debugging enabled
langgraph dev --debug-port 5678
```

**uv**

```bash
# Install debugpy package
uv add debugpy
# Start server with debugging enabled
langgraph dev --debug-port 5678
```

Then attach your preferred debugger:

#### VS Code
Add this configuration to `launch.json`:

```json
{
    "name": "Attach to LangGraph",
    "type": "debugpy",
    "request": "attach",
    "connect": {
      "host": "0.0.0.0",
      "port": 5678
    }
}
```

#### PyCharm
1. Go to Run > Edit Configurations
2. Click + and select "Python Debug Server"
3. Set IDE host name: `localhost`
4. Set port: `5678` (or the port number you chose in the previous step)
5. Click "OK" and start debugging

> [!TIP]
> For issues getting started, refer to the [troubleshooting guide](troubleshooting-studio.md).

## Next steps

For more information on how to run Studio, refer to the following guides:

* [Run application](use-studio.md#run-application)
* [Manage assistants](use-studio.md#manage-assistants)
* [Manage threads](use-studio.md#manage-threads)
* [Iterate on prompts](observability-studio.md)
* [Debug LangSmith traces](observability-studio.md#debug-langsmith-traces)
* [Add node to dataset](observability-studio.md#add-node-to-dataset)

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/quick-start-studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
