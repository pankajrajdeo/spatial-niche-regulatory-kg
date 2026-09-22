---
title: "Connect a Managed Deep Agent to Slack"
description: "Start Managed Deep Agents runs from Slack messages and send responses to Slack conversations."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-channels-slack"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-channels-slack]
---

# Connect a Managed Deep Agent to Slack

> Start Managed Deep Agents runs from Slack messages and send responses to Slack conversations.

A Slack channel lets people invoke a managed deep agent through app mentions, direct messages, and replies in an active Slack thread. Managed Deep Agents verifies Slack events, maps each conversation to a thread, runs the agent as the resolved caller, and posts the response back to Slack.

Managed Deep Agents creates and configures the resources that connect Slack to the deployed agent. Add a channel declaration to the agent project, then deploy.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project structure

```text
my-agent/
  agent.ts
  channels/
    slack.ts
```

## Add a Slack channel

A managed deep agent deployment supports one Slack channel.

The channel declaration lives at `channels/slack.ts`.

To include Slack when you create a project, pass `--channel slack`:

**npm**

```bash
npx managed-deepagents init my-agent --channel slack
```

**pnpm**

```bash
pnpm dlx managed-deepagents init my-agent --channel slack
```

**bun**

```bash
bunx managed-deepagents init my-agent --channel slack
```

To add Slack to an existing project, run the channel initialization command from the project root:

**npm**

```bash
npx mda channels init slack
```

**pnpm**

```bash
pnpm exec mda channels init slack
```

**bun**

```bash
bunx mda channels init slack
```

**channels/slack.ts**

```ts
import { channels } from "managed-deepagents";

export const channel = channels.slack();
```

## Configure your agent's appearance in Slack

Edit the channel declaration to control how the agent appears in Slack.

#### `name` — `string`
The agent name in Slack. The name must contain 1–35 characters and can contain letters, numbers, spaces, underscores, dashes, and periods. It cannot start or end with a space or dash.

#### `description` — `string`
A description of what the agent does. The description can contain up to 139 characters.

#### `icon` — `string`
A path to the agent icon shown in Slack, relative to the `channels/` directory. The icon must be a 512 by 512 pixel PNG file no larger than 1 MB. If you omit this parameter, Managed Deep Agents will generate an icon for you.

#### `backgroundColor` — `string`
The background color behind the agent icon as a six-digit hexadecimal color, such as `#1d4ed8`.

For example, put an icon next to the channel declaration:

```text
my-agent/
  agent.ts
  channels/
    slack.ts
    support-agent.png
```

**channels/slack.ts**

```ts
import { channels } from "managed-deepagents";

export const channel = channels.slack({
  name: "Support Agent",
  description: "Answers customer questions about orders and returns",
  icon: "support-agent.png",
  backgroundColor: "#1d4ed8",
});
```

### Configure which messages start runs

#### `triggerOnAllMessages` — `boolean`
Whether every new channel message can start an agent run. When `false`, channel messages start runs only when they mention the agent; direct messages still start runs.

#### `allowBotTriggers` — `boolean`
Whether messages from other Slack bots can start agent runs.

## Deploy the agent

During deployment, Managed Deep Agents provisions your agent in Slack from the channel declaration.

### Deploy your agent
Run the deployment command from the project root:

**npm**

```bash
npx mda deploy
```

**pnpm**

```bash
pnpm exec mda deploy
```

**bun**

```bash
bunx mda deploy
```

Managed Deep Agents deploys the agent and sets up the resources it needs to appear in Slack.

### Authorize Slack if prompted
If you haven't authorized LangSmith before, the CLI displays an HTTPS authorization link. Open the link, select the Slack workspace, and approve the requested access.

Return to the terminal and press Enter. The CLI checks the authorization again and continues provisioning. If the Slack workspace requires admin approval, complete that approval before continuing.

### Use the agent in Slack
After the first deployment, your agent sends you a direct message in Slack. Reply to the message to start an agent run. The final response appears in the Slack conversation.

> [!NOTE]
> Human-in-the-loop requests in Slack support only the `approve` and `reject` [decision types](managed-deep-agents-tools.md#human-in-the-loop).

If Slack is already authorized, deployment completes without an authorization prompt.

After you change the agent's name, description, icon, or background color in the Slack channel declaration, redeploy the agent to apply the changes in Slack.

## See also

* [Channels overview](managed-deep-agents-channels.md): understand how channels connect messaging services to an agent.
* [Deploy an agent](managed-deep-agents-deploy.md): configure and deploy a managed deep agent.
* [CLI reference](managed-deep-agents-cli.md): review Managed Deep Agents commands and flags.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-channels-slack.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
