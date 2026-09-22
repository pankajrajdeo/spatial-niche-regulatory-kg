---
title: "MODEL_NOT_FOUND"
description: "Currently only used in langchainjs (JavaScript/TypeScript)."
source: "https://docs.langchain.com/oss/python/langchain/errors/MODEL_NOT_FOUND"
category: "docs"
tags: [docs, langchain, errors, model_not_found]
---

# MODEL_NOT_FOUND

> [!NOTE]
> Currently only used in `langchainjs` (JavaScript/TypeScript).

The model name you have specified is not acknowledged by your provider.

## Troubleshooting

To resolve this error:

1. **Verify the model identifier**: Double check the model string you are passing in. Ensure the spelling and format are correct
2. **Check proxy/wrapper configurations**: If you are using a proxy or other alternative host with a model wrapper, confirm that the permitted model names are not restricted or altered

The error typically stems from either a typo in the model name string itself or restrictions imposed by a proxy service or model wrapper between your code and the provider's API.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/errors/MODEL_NOT_FOUND.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
