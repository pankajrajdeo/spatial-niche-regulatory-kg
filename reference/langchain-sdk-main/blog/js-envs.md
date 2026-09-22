---
title: "Announcing LangChainJS Support for Multiple JS Environments"
description: "Run LangChain.js across browsers, Cloudflare Workers, Vercel, Deno, and more. Smaller bundles, granular imports, and multi-environment support for AI apps."
source: "https://www.langchain.com/blog/js-envs"
category: "blog"
published: "2023-04-11T16:25:51.000Z"
author: "LangChain Accounts"
tags: [blog, js-envs]
---

# Announcing LangChainJS Support for Multiple JS Environments

**TLDR: **We're announcing support for running [LangChain.js](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com) in browsers, [Cloudflare Workers](https://workers.cloudflare.com/?ref=blog.langchain.com), [Vercel/Next.js](https://nextjs.org/?ref=blog.langchain.com), [Deno](https://deno.com/runtime?ref=blog.langchain.com), [Supabase Edge Functions](https://supabase.com/edge-functions?ref=blog.langchain.com), alongside existing support for Node.js ESM and CJS. See install/upgrade [docs](https://js.langchain.com/docs/getting-started/install?ref=blog.langchain.com) and **breaking changes ****list**.

## Context

Originally we designed LangChain.js to run in [Node.js](https://nodejs.org/en?ref=blog.langchain.com), which is the longstanding serverside JavaScript runtime. Back in February (time flies!) we started to [collect feedback](https://github.com/hwchase17/langchainjs/discussions/152?ref=blog.langchain.com) from the community on what other JS runtimes we should support, and have since received tons of requests for getting LangChain running on browsers, [Deno](https://deno.com/runtime?ref=blog.langchain.com), [Cloudflare Workers](https://workers.cloudflare.com/?ref=blog.langchain.com), [Vercel/Next.js](https://nextjs.org/?ref=blog.langchain.com), [Vite](https://vitejs.dev/?ref=blog.langchain.com), [Supabase Edge Functions](https://supabase.com/edge-functions?ref=blog.langchain.com), etc.

## Changes to Enable Multiple Environments

We've been on a journey since, together with community contributors, to enable support for as many JS environments as possible, some highlights along the way

- converted our codebase to ESM [here](https://github.com/hwchase17/langchainjs/pull/124?ref=blog.langchain.com) (CJS users don't have to worry we offer a CJS build too)
- removed usage of node-only APIs where possible [here](https://github.com/hwchase17/langchainjs/pull/97?ref=blog.langchain.com) and [here](https://github.com/hwchase17/langchainjs/pull/213?ref=blog.langchain.com)
- converted streaming and batch OpenAI requests to use `fetch` [here](https://github.com/hwchase17/langchainjs/pull/118?ref=blog.langchain.com) and [here](https://github.com/hwchase17/langchainjs/pull/526?ref=blog.langchain.com)
- worked with the folks at Replicate to convert their SDK to use `fetch`
- created packages that test importing LangChain in all the runtimes we support, see [here](https://github.com/hwchase17/langchainjs/blob/main/docker-compose.yml?ref=blog.langchain.com)
- and finally we have updated our exports to better support optional dependencies and produce smaller bundles, [here](https://github.com/hwchase17/langchainjs/pull/632?ref=blog.langchain.com)

At the beginning we designed the library so that you'd do use it like this

`import { LLMChain } from "langchain/chains";
import { PromptTemplate } from "langchain/prompts";
import { OpenAI } from "langchain/llms";
import { SupabaseVectorStore } from "langchain/vectorstores";
import { CohereEmbeddings } from "langchain/embeddings";
import { GithubRepoLoader } from "langchain/document_loaders";`

The old way

But that posed a few problems when running outside of Node.js

- In order to support the growing AI ecosystem we add new integrations all the time, but we don't want the install size of the library to grow unbounded. Therefore we make third-party SDKs optional dependencies of `langchain`. While that works fine in Node.js, in browsers and other environments where code is bundled, it ends up being a pretty poor experience, with some of the many bundlers out there needing either some custom configuration by the user, or asking the user to install all optional dependencies.
- When code is bundled, developers worry rightly about bundle size, and because not all bundlers support tree-shaking out-of-the-box, users of LangChain would end up with larger code bundles than they expected.

Not anymore! We've reworked how we expose third-party integrations, and the above code now becomes

`import { LLMChain } from "langchain/chains";
import { PromptTemplate } from "langchain/prompts";
import { OpenAI } from "langchain/llms/openai";
import { SupabaseVectorStore } from "langchain/vectorstores/supabase";
import { CohereEmbeddings } from "langchain/embeddings/openai";
import { GithubRepoLoader } from "langchain/document_loaders/web/github";`

This ensures you don't pull in code you're not using, and no bundlers choke on optional dependencies like before. Modules like `chains` and `prompts` that contain no third-party integrations remain as before.

Check out the install docs for more information on [how to upgrade](https://js.langchain.com/docs/getting-started/install?ref=blog.langchain.com).

### Breaking Changes

We had to make a few breaking changes to enable supporting multiple environments. These are limited to:

- `import { Calculator } from "langchain/tools";` moved to `import { Calculator } from "langchain/tools/calculator";`
- `import { loadLLM } from "langchain/llms";` moved to `import { loadLLM } from "langchain/llms/load";` and same for all other load* functions

**Deprecations**

- We now require more granular imports for all 3rd-party integrations (i.e. changing `import {OpenAI} from "langchain/llms";` to `import {OpenAI} from "langchain/llms/openai";`. However, the old imports are still left around but deprecated. Please transition your code to use the new imports soon, as we plan to phase out the old imports!

## Testing

Finally, a bit on how we test this to ensure we don't break compatibility with any environment in the future. For each new environment we want to support

- created a `test-exports-*` package in our monorepo containing a starter project created with that environment's tooling. eg. for Next.js with `npx create-next-app@latest`
- added some example usage of LangChain into that test package
- setup the package so that it contains both `build` and `test` scripts
- added to the list of packages tested in isolated docker containers in CI [here](https://github.com/hwchase17/langchainjs/blob/main/docker-compose.yml?ref=blog.langchain.com).
- finally fix whatever issues come up, ensuring it doesn't break any other environments

If we're not testing with your favorite environment yet, we're very open to PRs that add more environments to be tested. Please let us know if you run into any issues running LangChain.js in a particular environment – we'd love to help!
