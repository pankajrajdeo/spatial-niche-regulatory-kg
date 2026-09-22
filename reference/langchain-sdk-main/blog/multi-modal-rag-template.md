---
title: "Multi-modal RAG on slide decks"
description: "Build multi-modal RAG apps for slide decks using GPT-4V. Compare approaches, evaluate with benchmarks, and deploy with LangChain templates for visual Q&amp;A."
source: "https://www.langchain.com/blog/multi-modal-rag-template"
category: "blog"
published: "2023-12-06T16:30:07.000Z"
author: "LangChain Accounts"
tags: [blog, multi-modal-rag-template]
---

# Multi-modal RAG on slide decks

## Key Links

- LangChain public benchmark evaluation[notebooks](https://langchain-ai.github.io/langchain-benchmarks/notebooks/retrieval/multi_modal_benchmarking/multi_modal_eval.html?ref=blog.langchain.com)
- LangChain [template](https://templates.langchain.com/?integration_name=rag-chroma-multi-modal&ref=blog.langchain.com) for multi-modal RAG on presentations

## Motivation

Retrieval augmented generation (RAG) is one of the most important concepts in LLM app development. Documents of [many types](https://www.youtube.com/watch?v=O8sQxPgw8Ws&ref=blog.langchain.com) can be [passed into the context window](https://blog.langchain.com/deconstructing-rag/) of an LLM, enabling interactive chat or Q+A assistants. While many of the RAG apps to date have focused on text, a great deal of information is conveyed as visual content. As an example, slide decks are common for use-cases ranging from investor presentations to internal company communications. With the advent of multi-modal LLMs like [GPT-4V](https://openai.com/research/gpt-4v-system-card?ref=blog.langchain.com), it is now becoming possible to unlock RAG on the visual content often captured in slide decks. Below, we show two different ways to tackle this problem. We share a public benchmark for evaluating RAG on slide decks and use it highlight the trade-offs between these approaches. Finally, we provide a template for quickly creating multi-modal RAG apps for slide decks.

## Design

The task is analogous to RAG apps on text documents: retrieve the relevant slide(s) based upon a user question and pass them to a multi-modal LLM (GPT-4V) for the answer synthesis. There are at least two general ways to approach this problem.

(1) **Multi-modal embeddings**: Extract the slides as images, use multi-model embeddings to embed each image, retrieve the relevant slide image(s) based upon the user input, and pass those images to GPT-4V for answer synthesis. We have previously released a [cookbook](https://github.com/langchain-ai/langchain/blob/master/cookbook/multi_modal_RAG_chroma.ipynb?ref=blog.langchain.com) for this with [Chroma](https://www.trychroma.com/?ref=blog.langchain.com) and [OpenCLIP embeddings](https://github.com/mlfoundations/open_clip?ref=blog.langchain.com).

(2) **Multi-vector retriever**: Extract the slides as images, use GPT-4V to summarize each image, embed the image summaries with a link to the original images, retrieve relevant image based on similarity between the image summary and the user input, and finally pass those images to GPT-4V for answer synthesis. We have previously released a [cookbook](https://github.com/langchain-ai/langchain/blob/master/cookbook/Multi_modal_RAG.ipynb?ref=blog.langchain.com) for this with the [multi-vector retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector?ref=blog.langchain.com).

The trade-off between the approaches is straightforward: multi-modal embeddings are a simpler design, mirroring what we do with text-based RAG apps, but there are limited options and some questions about the ability to retrieve graphs or tables that appear visually similar. In contrast, image summaries use mature text embedding models and can describe graphs or figures with considerable detail. But this design suffers from higher complexity and cost of image summarization.

## Evaluation

To evaluate these methods, we chose a recent [earnings presentation](https://investors.datadoghq.com/static-files/986ca4cd-9507-4c9d-b56f-4bae59d3dd47?ref=blog.langchain.com) from Datadog as a realistic slide deck with a mixture of visual and qualitative elements. We create a small public [LangChain benchmark](https://github.com/langchain-ai/langchain-benchmarks/pull/101?ref=blog.langchain.com) for this slide deck with 10 questions: you can see documentation for evaluating on this benchmark [here](https://langchain-ai.github.io/langchain-benchmarks/notebooks/retrieval/multi_modal_benchmarking/multi_modal_eval_baseline.html?ref=blog.langchain.com) and [here](https://langchain-ai.github.io/langchain-benchmarks/notebooks/retrieval/multi_modal_benchmarking/multi_modal_eval.html?ref=blog.langchain.com).

As a sanity check, we can see that it is possible to retrieve slides based upon a natural language description of the slide content (below, see code [here](https://langchain-ai.github.io/langchain-benchmarks/notebooks/retrieval/multi_modal_benchmarking/multi_modal_eval.html?ref=blog.langchain.com)).

The question-answer pairs in our benchmark are based on the visual content of the slides. We evaluated the above two RAG methods with [LangSmith](https://docs.smith.langchain.com/evaluation/faq/evaluator-implementations?ref=blog.langchain.com) and compare against RAG using text extraction (`Top K RAG (text only)`).

**Approach**

**Score (**[**CoT accuracy**](https://docs.smith.langchain.com/evaluation/evaluator-implementations?ref=blog.langchain.com#correctness-qa-evaluation)**)**

Top k RAG (text only)

**20%**

Multi-modal embeddings

**60%**

Multi-vector retriever w/ image summary

**90%**

LangSmith offers a comparison view where we can review the results of each experiment side-by-side. [Here](https://smith.langchain.com/public/b738420f-3cd5-46c4-a0e1-894aff3cf37e/d?ref=blog.langchain.com) is a public page where the evaluation runs can be compared in detail. The image below shows the run comparison view.

Using the above comparative analysis, we can compare the retrieved content for each question. These [slides](https://docs.google.com/presentation/d/19x0dvHGhbJOOUWqvPKrECPi1yI3makcoc-8tFLj9Sos/edit?usp=sharing&ref=blog.langchain.com) provide a deep dive of every question - answer pair in the evaluation set along with the associated LangSmith traces.

## Insights

1. **Multi-modal approaches far exceed the performance of text-only RAG**. We saw notable improvement with multi-modal approaches (60% and 90%) over the RAG that loads only the text (20%), an expected result given the importance of retaining visual context for reasoning about the slide content.
2. **GPT-4V is powerful for structured data extraction from images**. For example, see this [trace](https://smith.langchain.com/public/63c73da7-0001-4bb9-aa83-94cb9e63b24c/r?ref=blog.langchain.com). The question asks for the count of customers, which can only be retrieved from a slide that contains a broad mix of visual content. GPT-4V is able to correctly extract this information from the slide

1. **Retrieval of the correct image is the central challenge. **As noted in the [slides](https://docs.google.com/presentation/d/19x0dvHGhbJOOUWqvPKrECPi1yI3makcoc-8tFLj9Sos/edit?ref=blog.langchain.com#slide=id.g262b753d5b7_0_183) and mentioned above, if the correct image was retrieved then GPT-4V was typically able to answer the question correctly. However, image retrieval was the central challenge. We found that image summarization **does** improve retrieval significantly over multi-modal embeddings but comes with higher complexity and cost to pre-compute the summaries. The central need is for multi-modal embeddings that can differentiate between visually similar slides. OpenCLIP has a [wide variety of different models](https://github.com/mlfoundations/open_clip/blob/main/docs/openclip_results.csv?ref=blog.langchain.com) that are worth experimenting with.

## Deployment

To ease testing of multi-modal RAG application for this use-case, we are releasing a [template](https://templates.langchain.com/?integration_name=rag-chroma-multi-modal&ref=blog.langchain.com) that uses both Chroma and OpenCLIP multi-modal embeddings. This makes it extremely easy to get started: simply upload a presentation and follow the README (just two command to build the vectorstore and run the playground). Below we can see the interactive chat playground (left) on the [Datadog earnings presentation](https://investors.datadoghq.com/static-files/986ca4cd-9507-4c9d-b56f-4bae59d3dd47?ref=blog.langchain.com) with the LangSmith trace (right) showing retrieval of the right slide.

## Conclusion

Multi-modal LLMs have potential to unlock the visual content in slide decks for RAG applications. We build a public benchmark evaluation set of question-answer pairs on an investor presentation slide deck for Datadog ([here](https://investors.datadoghq.com/static-files/986ca4cd-9507-4c9d-b56f-4bae59d3dd47?ref=blog.langchain.com)). We tested multi-modal RAG using two approaches on this benchmark. We found that both exceed the performance of text-only RAG. We identified trade-offs between approaches for multi-modal RAG: text summarization of each slide can improve retrieval but comes at the cost of pre-generating summaries of each slide. Multi-model are likely to have a higher performance ceiling, but current options are somewhat limited and, in our test, under-perform text summarization. To aid in the testing and deployment of multi-modal RAG apps, we also are releasing a [template](https://templates.langchain.com/?integration_name=rag-chroma-multi-modal&ref=blog.langchain.com).
