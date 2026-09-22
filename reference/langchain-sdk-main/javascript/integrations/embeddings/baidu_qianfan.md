---
title: "Baidu qianfan integration"
description: "Integrate with the Baidu qianfan embedding model using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/embeddings/baidu_qianfan"
category: "docs"
tags: [docs, javascript, integrations, embeddings, baidu_qianfan]
---

# Baidu qianfan integration

> Integrate with the Baidu qianfan embedding model using LangChain JavaScript.

The `BaiduQianfanEmbeddings` class uses the Baidu Qianfan API to generate embeddings for a given text.

## Setup

An API key is required to use this embedding model. You can get one by registering at [https://cloud.baidu.com/doc/WENXINWORKSHOP/s/alj562vvu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/alj562vvu).

Please set the acquired API key as an environment variable named BAIDU\_API\_KEY, and set your secret key as an environment variable named BAIDU\_SECRET\_KEY.

Then, you'll need to install the [`@langchain/baidu-qianfan`](https://www.npmjs.com/package/@langchain/baidu-qianfan) package:

> [!TIP]
> See [this section for general instructions on installing LangChain packages](../../langchain/install.md).

**npm**

```bash
npm install @langchain/baidu-qianfan @langchain/core
```

## Usage

```typescript
import { BaiduQianfanEmbeddings } from "@langchain/baidu-qianfan";

const embeddings = new BaiduQianfanEmbeddings();
const res = await embeddings.embedQuery(
  "What would be a good company name a company that makes colorful socks?"
);
console.log({ res });
```

## Related

* Embedding model [conceptual guide](../embeddings.md)
* Embedding model [how-to guides](../embeddings.md)

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/baidu_qianfan.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
