---
title: "Customize the error support message"
description: "Customize support contact information in the LangSmith frontend for self-hosted deployments."
source: "https://docs.langchain.com/langsmith/self-host-ui-customization"
category: "docs"
tags: [docs, langsmith, self-host-ui-customization]
---

# Customize the error support message

> Customize support contact information in the LangSmith frontend for self-hosted deployments.

## Custom error support message

By default, error messages in LangSmith direct users to the [Support Portal](https://support.langchain.com). You can replace this with your own support contact information.

When set, all error and support messages throughout the UI will display your custom text instead of the default LangChain support email.

> [!NOTE]
> The custom message is rendered as **plain text** only. HTML tags will not be interpreted and will display as literal text.

**Helm**

```yaml
config:
  customErrorSupportMessage: "For help, contact your internal IT team at helpdesk@example.com"
```

To revert to the default behavior, remove the setting or set it to an empty string.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-ui-customization.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
