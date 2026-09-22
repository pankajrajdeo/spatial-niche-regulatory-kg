---
title: "Configure prompt settings"
description: "The Playground enables you to control various settings for your prompts. The Prompt Settings window contains:"
source: "https://docs.langchain.com/langsmith/managing-model-configurations"
category: "docs"
tags: [docs, langsmith, managing-model-configurations]
---

# Configure prompt settings

The [Playground](prompt-engineering-concepts.md#playground) enables you to control various settings for your prompts. The **Prompt Settings** window contains:

* [Model configuration](#model-configurations)
* [Tool settings](#tool-settings)
* [Prompt formatting](#prompt-formatting)

To access **Prompt Settings**:

1. Navigate to the **Playground** in the left sidebar.
2. Under the **Prompts** heading select the gear  icon next to the model name, which will launch the **Prompt Settings** window.

   <img src="https://mintcdn.com/langchain-5e9cc07a/6r3GRtwWCl4ozaHW/langsmith/images/model-config-light.png?fit=max&auto=format&n=6r3GRtwWCl4ozaHW&q=85&s=6c0f7d7012b1e5295fe545149f955e6b" alt="Model Configuration window in the LangSmith UI, settings for Provider, Model, Temperature, Max Output Tokens, Top P, Presence Penalty, Frequency Penalty, Reasoning Effort, etc." width="886" height="689" data-path="langsmith/images/model-config-light.png" />

   <img src="https://mintcdn.com/langchain-5e9cc07a/ppc8uxWc01j4q7Ia/langsmith/images/model-config-dark.png?fit=max&auto=format&n=ppc8uxWc01j4q7Ia&q=85&s=2e9da272c3fc8f7ac958c6e6d1da85e3" alt="Model Configuration window in the LangSmith UI, settings for Provider, Model, Temperature, Max Output Tokens, Top P, Presence Penalty, Frequency Penalty, Reasoning Effort, etc." width="881" height="732" data-path="langsmith/images/model-config-dark.png" />

## Model configurations

[Model configurations](model-configurations.md) define the parameters your prompt runs against. Configurations are shared across your workspace—any configuration saved here is available in other LangSmith features and visible to admins in **Settings** > **Model configurations**. For details on specific settings, refer to your model provider’s documentation (for example, [Anthropic](https://platform.claude.com/docs/en/api/messages) or [OpenAI](https://platform.openai.com/docs/api-reference/responses/create)).

### Create saved configurations

1. In the **Model Configurations** tab, adjust the model configuration as needed—you can select a [saved configuration to edit](#edit-configurations).
2. Click the **Save As** button in the top bar.
3. Enter a name and optional description for your configuration and confirm.
4. Now that you've saved the configuration, anyone in your organization's [workspace](administration-overview.md#workspaces) can access it. All saved configurations are available in the **Model Configuration** dropdown.
5. Once you have created a saved configuration, you can set it as your default, so any new prompt you create will automatically use this configuration. To set a configuration as your default, click the **Set as default**  icon next to the model name in the dropdown.

> [!NOTE]
> OAuth client credential fields appear in this popover only after the configuration is saved as a preset. To attach OAuth to a one-off configuration, save it as a preset first (refer to [OAuth client credentials](model-configurations.md#oauth-client-credentials)).

### Edit configurations

1. To rename a saved configuration, or update the description, select the configuration name or description and make the necessary changes.
2. Update the current configuration's parameters as needed and click the **Save** button at the top.

### Delete configurations

1. Select the configuration you want to remove.
2. Click the trash  icon to delete it.

### Extra parameters

The **Extra Parameters** field allows you to pass additional model parameters that aren't directly supported in the LangSmith interface. This is particularly useful in two scenarios:

1. When model providers release new parameters that haven't yet been integrated into the LangSmith interface. You can specify these parameters in JSON format to use them right away. For example:

```json
   {
       "reasoning_effort": "medium"
   }
```

2. When troubleshooting parameter-related errors in the Playground, such as:

```
   TypeError: AsyncCompletions.create() got an unexpected keyword argument 'max_concurrency'
```

   If you receive an error about unnecessary parameters (which is more common when using [LangChain JS](../langchain/overview.md) for run tracing), you can use this field to remove the extra parameters.

## Tool settings

[*Tools*](prompt-engineering-concepts.md#tools) enable your LLM to perform tasks like searching the web, looking up information, and so on. In the **Tools Settings** tab, you can manage the ways your LLM uses and accesses the tools you have defined in your prompt, including:

* **Parallel Tool Calls**: Calling multiple tools in parallel when appropriate. This allows the model to gather information from different sources simultaneously. (Dependent on model support for parallel execution.)
* **Tool Choice**: Select the tools that the model can access. For more details, refer to [Use tools in a prompt](use-tools.md).

> [!NOTE]
> To manage which tools are available in your workspace, including enabling, disabling, and editing tools across prompts, refer to [Manage tools with the registry](use-tools.md#manage-tools-with-the-registry).

## Prompt formatting

The **Prompt Format** tab allows you to specify:

* The **Prompt type**. For details on chat and completion prompts, refer to [Prompt engineering](prompt-engineering-concepts.md#prompt-types) concepts.
* The **Template format**. For details on prompt templating and using variables, refer to [F-string vs. mustache](prompt-engineering-concepts.md#f-string-vs-mustache).

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managing-model-configurations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
