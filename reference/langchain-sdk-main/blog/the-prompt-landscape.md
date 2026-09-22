---
title: "The Prompt Landscape"
description: "Explore prompt engineering techniques for LLMs across reasoning, RAG, SQL, code generation, and more. Browse and manage prompts in LangChain Hub."
source: "https://www.langchain.com/blog/the-prompt-landscape"
category: "blog"
published: "2023-10-18T16:00:10.000Z"
author: "LangChain Accounts"
tags: [blog, the-prompt-landscape]
---

# The Prompt Landscape

### Context

Prompt Engineering can steer LLM behavior without updating the model weights. A variety of prompts for different uses-cases have emerged (e.g., see [@dair_ai](https://twitter.com/dair_ai?ref=blog.langchain.com)’s [prompt engineering guide](https://www.promptingguide.ai/techniques?ref=blog.langchain.com) and [this excellent review](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/?ref=blog.langchain.com) from Lilian Weng). As the [number of LLMs](https://www.promptingguide.ai/models/collection?ref=blog.langchain.com) and different use-cases expand, there is [increasing need](https://twitter.com/omarsar0/status/1702327692363018361?s=20&ref=blog.langchain.com) for prompt management to support discoverability, sharing, workshopping, and debugging prompts. We launched [the LangChain Hub](https://smith.langchain.com/hub?ref=blog.langchain.com) over a month ago to support these needs, serving as a home for both browsing community prompts and managing your own. Below we provide an overview of the major themes in prompting that we’ve seen since launch and highlight interesting examples.

### Reasoning

[Chain-of-thought](https://arxiv.org/abs/2201.11903?ref=blog.langchain.com) reasoning encourages the LLM to spread its “thinking” out across many tokens: it conditions the LLM to show its work using a simple statement e.g., `Let's think step by step`. This has found broad appeal because it [improves](https://twitter.com/_jasonwei/status/1712551642275655770?s=20&ref=blog.langchain.com) many reasoning tasks by a large margin and is easy to implement. More sophisticated approaches (e.g., [Tree-of-thought](https://arxiv.org/abs/2305.10601?ref=blog.langchain.com)) are also worth consideration, but the [benefit relative to the overhead](https://twitter.com/_jasonwei/status/1712551642275655770?s=20&ref=blog.langchain.com) (tokens) should be evaluated.

Deepmind recently used LLMs to optimize prompts, and converged to `Take a deep breath and work on this problem step-by-step` as the [best](https://twitter.com/ItakGol/status/1702306238141223100?s=20&ref=blog.langchain.com) performing optimization. Going forward, this points to some interesting potential for [translation modules](https://x.com/abacaj/status/1708847673732710718?s=20&ref=blog.langchain.com) between human instruction and LLM-optimized prompts.

[Reasoning prompts](https://x.com/cwolferesearch/status/1657122778984660993?s=20&ref=blog.langchain.com) as shown above can be appended as simple instructions to many tasks and have become particularly important for agents. For example, [ReAct agents](https://www.promptingguide.ai/techniques/react?ref=blog.langchain.com) combine tool use with reasoning in an interleaved manner. Agent prompts can encode multi-step reasoning in different ways, but often with the goal of updating action plans given observations. See Lilian Weng's [excellent post](https://lilianweng.github.io/posts/2023-06-23-agent/?ref=blog.langchain.com) on agents for a full review of the various approaches on agent design and prompting.

**Examples**

- [https://smith.langchain.com/hub/hwchase17/react](https://smith.langchain.com/hub/hwchase17/react?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/shoggoth13/react-chat-agent](https://smith.langchain.com/hub/shoggoth13/react-chat-agent?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/jacob/langchain-tsdoc-research-agent](https://smith.langchain.com/hub/jacob/langchain-tsdoc-research-agent?ref=blog.langchain.com)

### Writing

Prompts to improve writing have widespread appeal given the [impressive](https://www.reddit.com/r/singularity/comments/151hicw/writers_are_screwed_100k_context_claude_is_a/) displays of creativity from LLMs. [@mattshumer_](https://twitter.com/mattshumer_?ref=blog.langchain.com)’s popular GPT4 prompts provide ways to improve writing clarity or customize the style of LLM-generated text. Leveraging LLM's capacity for language translation is another good application for writing.

**Examples**

- [https://smith.langchain.com/hub/rlm/matt-shumer-writing](https://smith.langchain.com/hub/rlm/matt-shumer-writing?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/rlm/matt-shumer-writing-style](https://smith.langchain.com/hub/rlm/matt-shumer-writing-style?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/agola11/translator](https://smith.langchain.com/hub/agola11/translator?ref=blog.langchain.com)

There's also been a proliferation of prompts for producing diverse content (e.g., onboarding emails, blog posts, Tweet threads, learning materials for [education](https://twitter.com/LangChainAI/status/1699166512781905985?s=20&ref=blog.langchain.com)).

**Examples**

- [https://smith.langchain.com/hub/gitmaxd/onboard-email](https://smith.langchain.com/hub/gitmaxd/onboard-email?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/hardkothari/blog-generator](https://smith.langchain.com/hub/hardkothari/blog-generator?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/gregkamradt/test-question-making](https://smith.langchain.com/hub/gregkamradt/test-question-making?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/bradshimmin/favorite_prompts](https://smith.langchain.com/hub/bradshimmin/favorite_prompts?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/hardkothari/tweet-from-text](https://smith.langchain.com/hub/hardkothari/tweet-from-text?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/julia/podcaster-tweet-thread](https://smith.langchain.com/hub/julia/podcaster-tweet-thread?ref=blog.langchain.com)

### SQL

Because enterprise data is often captures in SQL databases, there is great interest in using LLMs as a natural language interface for SQL (see our [blog post](https://blog.langchain.com/llms-and-sql/)). [A number of papers](https://arxiv.org/pdf/2204.00498.pdf?ref=blog.langchain.com) have reported that LLMs can generate SQL given some specific information about the table, including a `CREATE TABLE` description for each table followed by three example rows in a `SELECT` statement. LangChain has numerous tools for querying SQL databases (see our [use case guide](https://python.langchain.com/docs/use_cases/qa_structured/sql?ref=blog.langchain.com) and [cookbook](https://python.langchain.com/docs/expression_language/cookbook/sql_db?ref=blog.langchain.com)).

**Examples**

- [https://smith.langchain.com/hub/rlm/text-to-sql](https://smith.langchain.com/hub/rlm/text-to-sql?ref=blog.langchain.com)

### Brainstorming

Many people have had instructive and / or entertaining conversations with LLMs. LLMs have proven broadly useful for brainstorming: one trick is to create multiple user personas that work through an idea collectively, as shown by [@mattshumer_](https://twitter.com/mattshumer_/status/1700590646149390418?s=20&ref=blog.langchain.com) business plan ideation prompt. The principle can be adapted broadly. As an example, [BIDARA](https://www1.grc.nasa.gov/research-and-engineering/vine/petal/?ref=blog.langchain.com) (Bio-inspired Design and Research Assistant) is a GPT-4 chatbot instructed to help scientists and engineers understand, learn from, and emulate the strategies used by living things for new designs and technologies.

**Examples**

- [https://smith.langchain.com/hub/hwchase17/matt-shumer-validate-business-idea](https://smith.langchain.com/hub/hwchase17/matt-shumer-validate-business-idea?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/bruffridge/bidara](https://smith.langchain.com/hub/bruffridge/bidara?ref=blog.langchain.com)

### Extraction

LLMs can be powerful tools for extracting text in particular formats, often aided by [function calling](https://openai.com/blog/function-calling-and-other-api-updates?ref=blog.langchain.com). This is a rich area with frameworks developed to support it, such as [@jxnlco](https://twitter.com/jxnlco?ref=blog.langchain.com)’s Instructor (see their [guide](https://jxnl.github.io/instructor/tips/?ref=blog.langchain.com) on prompt engineering). We've also seen prompts designed for specific extraction tasks, such as knowledge graph triple extraction (as shown by tools like [Instagraph](https://instagraph.ai/?ref=blog.langchain.com) or the [text-to-graph](https://twitter.com/RLanceMartin/status/1691880034058064365?ref=blog.langchain.com) playground).

**Examples**

- [https://smith.langchain.com/hub/langchain/knowledge-triple-extractor](https://smith.langchain.com/hub/langchain/knowledge-triple-extractor?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/homanp/superagent](https://smith.langchain.com/hub/homanp/superagent?ref=blog.langchain.com)

### RAG

Retrieval augmented generation (RAG) is a popular LLM application: it passes relevant context to the LLM via prompt. RAG has particular promise [for](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb?ref=blog.langchain.dev) [factual](https://www.youtube.com/watch?v=hhiLw5Q_UFg&ref=blog.langchain.com) [recall](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts?ref=blog.langchain.dev) because it marries the reasoning capability of LLMs with the content of external data sources, which is [particularly powerful](https://www.glean.com/blog/lessons-and-learnings-from-building-an-enterprise-ready-ai-assistant?ref=blog.langchain.com) for enterprise data.

**Examples**

- [https://smith.langchain.com/hub/rlm/rag-prompt](https://smith.langchain.com/hub/rlm/rag-prompt?ref=blog.langchain.com)

### Instruction-tuned LLMs

The landscape of open [source instruction-tuned LLMs](https://python.langchain.com/docs/guides/local_llms?ref=blog.langchain.com) has exploded over the past year. With this has come a variety of popular LLMs that each have specific prompt instructions (e.g., see instruction for [LLaMA2](https://huggingface.co/blog/llama2?ref=blog.langchain.com#how-to-prompt-llama-2) and [Mistral](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1?ref=blog.langchain.com#instruction-format)). Popular tasks such as retrieval augmented generation ([RAG](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com)) can benefit from LLM-specific-prompts.

**Examples**

- [https://smith.langchain.com/hub/rlm/rag-prompt-llama](https://smith.langchain.com/hub/rlm/rag-prompt-llama?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/rlm/rag-prompt-mistral](https://smith.langchain.com/hub/rlm/rag-prompt-mistral?ref=blog.langchain.com)

### LLM Graders

Using LLMs as graders is a powerful idea that has been broadly showcased in [OpenAI cookbooks](https://github.com/openai/openai-cookbook/blob/main/examples/evaluation/How_to_eval_abstractive_summarization.ipynb?ref=blog.langchain.com) and [open](https://twitter.com/RLanceMartin/status/1658499575626465283?ref=blog.langchain.com) [source](https://x.com/hwchase17/status/1692220493657485674?s=20&ref=blog.langchain.com) [projects](https://x.com/jerryjliu0/status/1703074710077260092?s=20&ref=blog.langchain.com): the central idea is to utilize the discrimination of an LLM to rank or grade a response relative to a ground truth answer (or for consistently relative to reference materials such as retrieved context). Much of the work on LangSmith has [focused](https://docs.smith.langchain.com/evaluation?ref=blog.langchain.com) [on](https://docs.smith.langchain.com/evaluation/quickstart?ref=blog.langchain.com) [evaluation](https://www.youtube.com/watch?app=desktop&v=ll-Xit_Khq0&ref=blog.langchain.com) support.

**Examples**

- [https://smith.langchain.com/hub/simonp/model-evaluator](https://smith.langchain.com/hub/simonp/model-evaluator?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/wfh/automated-feedback-example](https://smith.langchain.com/hub/wfh/automated-feedback-example?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/smithing-gold/assumption-checker](https://smith.langchain.com/hub/smithing-gold/assumption-checker?ref=blog.langchain.com)

### Synthetic Data generation

[Fine-tuning](https://blog.langchain.com/using-langsmith-to-support-fine-tuning-of-open-source-llms/) LLMs is one of the primary ways (along with RAG) to steer LLM behavior. Yet, gathering training data for fine-tuning is a challenge. [Considerable](https://x.com/johnjnay/status/1649792913109397508?s=20&ref=blog.langchain.com) [work](https://www.evals.anthropic.com/model-written/?ref=blog.langchain.com) [has focused](https://x.com/cwolferesearch/status/1616896609517817857?s=20&ref=blog.langchain.com) on using LLMs to generate synthetic datasets.

**Examples**

- [https://smith.langchain.com/hub/homanp/question-answer-pair](https://smith.langchain.com/hub/homanp/question-answer-pair?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/gitmaxd/synthetic-training-data](https://smith.langchain.com/hub/gitmaxd/synthetic-training-data?ref=blog.langchain.com)

### Prompt Optimization

The [Deepmind](https://arxiv.org/pdf/2309.03409.pdf?ref=blog.langchain.com) work showing that LLMs can optimize prompts offers the broad potential for [translation modules](https://x.com/abacaj/status/1708847673732710718?s=20&ref=blog.langchain.com) between human instruction and LLM-optimized prompts. We’ve seen a number of interesting prompts along these lines; one good example is for [Midjourney](https://www.midjourney.com/home/?callbackUrl=%2Fapp%2F&ref=blog.langchain.com), which has incredible creative potential to unlock through prompting and parameter flags. For a general input idea (`Freddie Mercury performing at the 2023 San Francisco Pride Parade hyper realistic`), it can produce a series of N prompts that embellish the idea, as shown below:

Freddie Mercury electrifying the San Francisco Pride Parade stage, shining in a gleaming golden outfit, iconic microphone stand in hand, evoking the hyper-realistic style of Caravaggio, vivid and dynamic --ar 16:9 --q 2)

**Examples**

- [https://smith.langchain.com/hub/hardkothari/prompt-maker](https://smith.langchain.com/hub/hardkothari/prompt-maker?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/aemonk/midjourney_prompt_generator](https://smith.langchain.com/hub/aemonk/midjourney_prompt_generator?ref=blog.langchain.com)

### Code Understanding and Generation

Code analysis is one of the most popular LLM use-cases, as demonstrated by the popularity of [GitHub co-pilot](https://github.com/features/copilot?ref=blog.langchain.com) and [Code Interpreter](https://www.pluralsight.com/resources/blog/data/chatgpt-code-interpreter-plugin-guide?ref=blog.langchain.com) as well as fine-tuned LLMs ([Code LLaMA](https://ai.meta.com/blog/code-llama-large-language-model-coding/?ref=blog.langchain.com)). We've seen a number of prompts related to this theme:

**Examples**

- [https://smith.langchain.com/hub/chuxij/open-interpreter-system](https://smith.langchain.com/hub/chuxij/open-interpreter-system?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/homanp/github-code-reviews](https://smith.langchain.com/hub/homanp/github-code-reviews?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/muhsinbashir/text-to-streamlit-webap](https://smith.langchain.com/hub/muhsinbashir/text-to-streamlit-webap?ref=blog.langchain.com)

### Summarization

[Summarization of content](https://blog.langchain.com/llms-to-improve-documentation/) is a powerful LLM use-case. Longer context LLMs, such as [Anthropic Claude2](https://www.anthropic.com/index/claude-2?ref=blog.langchain.com), can absorb &gt; 70 pages for direct summarization. [Prompting techniques](https://twitter.com/vimota/status/1702503466994982914?ref=blog.langchain.com) like [chain of density](https://browse.arxiv.org/pdf/2309.04269.pdf?ref=blog.langchain.com) offer a complimentary approach, resulting in dense yet human-preferable summaries.

**Examples**

- [https://smith.langchain.com/hub/lawwu/chain_of_density](https://smith.langchain.com/hub/lawwu/chain_of_density?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/hwchase17/anthropic-paper-qa](https://smith.langchain.com/hub/hwchase17/anthropic-paper-qa?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/muhsinbashir/youtube-transcript-to-article](https://smith.langchain.com/hub/muhsinbashir/youtube-transcript-to-article?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/hwchase17/anthropic-chain-of-density](https://smith.langchain.com/hub/hwchase17/anthropic-chain-of-density?ref=blog.langchain.com)

In addition, summarization can be applied to diverse content types like chat conversations (e.g., [compress the content](https://python.langchain.com/docs/modules/data_connection/retrievers/contextual_compression/?ref=blog.langchain.com) to pass as context into chat LLM memory) or domain specific data (financial table summarization)

**Examples**

- [https://smith.langchain.com/hub/langchain-ai/weblangchain-search-query](https://smith.langchain.com/hub/langchain-ai/weblangchain-search-query?ref=blog.langchain.com)
- [https://smith.langchain.com/hub/hwchase17/financial-table-insights](https://smith.langchain.com/hub/hwchase17/financial-table-insights?ref=blog.langchain.com)

### Conclusion

You can easily test any of these prompts for yourself using "Try It" button:

This will open a playground for workshopping and debugging prompts with a broad set of different LLMs, many of which are free to use:
