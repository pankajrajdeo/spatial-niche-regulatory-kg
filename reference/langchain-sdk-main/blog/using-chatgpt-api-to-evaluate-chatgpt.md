---
title: "Using the ChatGPT API to evaluate the ChatGPT API"
description: "Compare ChatGPT API vs GPT-3 for question answering tasks. See evaluation results, prompt strategies, and insights on using ChatGPT to evaluate itself."
source: "https://www.langchain.com/blog/using-chatgpt-api-to-evaluate-chatgpt"
category: "blog"
published: "2023-03-02T15:54:38.000Z"
author: "LangChain Accounts"
tags: [blog, using-chatgpt-api-to-evaluate-chatgpt]
---

# Using the ChatGPT API to evaluate the ChatGPT API

OpenAI released a new [ChatGPT API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis?ref=blog.langchain.com) yesterday. Lots of people were excited to try it. But how does it actually compare to the existing API? It will take some time before there is a definitive answer, but here are some initial thoughts. Because I'm lazy, I also enrolled the help of the ChatGPT API itself to help do this evaluation. Confused? Don't be. Let's dive in.

Relevant links:

- [Evaluation Notebook](https://python.langchain.com/docs/guides/evaluation/data_augmented_question_answering?ref=blog.langchain.com)
- [ChatGPT PR](https://github.com/hwchase17/langchain/pull/1375?ref=blog.langchain.com)
- [ChatGPT PR Discussion](https://github.com/hwchase17/langchain/discussions/1376?ref=blog.langchain.com)

## What task are we evaluating?

In this article we will evaluate the performance of a chain on [question answering](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com) over a particular dataset. This chain takes a query, does a "retrieval" step to look up relevant documents in a vector store, and then does a "generation" step to pass them, along with the original query, to a model to get back an answer. We will hold the "retrieval" step constant, so we are just evaluating the "generation" step of the chain.

## What models/prompts are we comparing?

First up, we've got the standard `text-davinci-003` model, with the standard [`VectorDBQAChain`](https://python.langchain.com/docs/modules/chains/popular/vector_db_qa?ref=blog.langchain.com) prompts.

We want to compare this to ChatGPT. There would be two potential ways to do this. One would be to use a wrapper that and treat ChatGPT has just another LLM. Another would be to try to use the ChatGPT API more natively.

What do I mean by that? The ChatGPT API differs from the GPT-3 API in that it takes in a list of messages (rather than a single string) and returns a message. These messages are essentially dicts that have two fields: `content` and `role`. Both are used in the prompt. The `content` field can be anything, while the `role` field should be one of `user`, `system`, or `assistant`. Presumably, the model is trained to treat the `user` messages as human messages, `system` messages as some system level configuration, and `assistant` messages as previous chat responses from the assistant.

So how can we use this to do question answering? Let's think back to the information we need to pass in. There are three components:

- Instructions (about how it should answer, format, etc)
- The user question
- Retrieved pieces of content

Instructions seem like they should be the first message and have `role` of `system`. The user question seems like it should have `role` of `user`, but is a little bit less clear where it should go. It is extremely unclear what `role` or what position in the list of messages the retrieved pieces of content should go. Note that I say "should", but our understanding might change in the near future.

Some ideas for how to combine the user question and retrieved pieces of content:

1. Put the pieces of content in the system message and tell the model to only use that information.
2. Put each piece of content as its own message (with either `assistant` or `user` roles) in the middle of the conversation
3. Put the user question first, and then follow it with a message for each piece of content (with role `assistant`) and then another `user` message asking for it to answer given those pieces of content.

Lots of choices! For the purposes of this experiment I went with option 2, set role to be `user`, and instructed the model to only use pieces of information that the user had told it before when answering.

## How did we evaluate this?

We used the simple "State of the Union Address" that we commonly use as a toy example. We then generated a bunch of questions and corresponding answers from this dataset. This was done using GPT-3, using our [existing question/answering generation pipeline](https://python.langchain.com/docs/guides/evaluation/data_augmented_question_answering?ref=blog.langchain.com). We then ran each question through the two chains (GPT3 and ChatGPT). We then evaluated the answers - using GPT3 and ChatGPT. Specifically, we have another chain called the [`QAEvalChain`](https://python.langchain.com/docs/guides/evaluation/data_augmented_question_answering?ref=blog.langchain.com#evaluate), which uses GPT3 to evaluate question answering responses. We created a corresponding [`QAEvalChatChain`](https://github.com/hwchase17/langchain/blob/harrison/memory-chat/langchain/evaluation/qa/chat_eval_chain.py?ref=blog.langchain.com) which uses the ChatGPT API to do a similar thing. To add a cherry on top, we then created a [`QACompChatChain`](https://github.com/hwchase17/langchain/blob/harrison/memory-chat/langchain/evaluation/qa/chat_comp_chain.py?ref=blog.langchain.com) which takes in the question, the true answer, and both predicted answers and compares them.

In this post, we will look mostly as the results of the evaluators. So in a meta way, we are using a language model to evaluate a language model, but then (for the time being) we are still the ones evaluating the evaluator model.

## So what were the results?

See our full results [here](https://langchain.readthedocs.io/en/harrison-memory-chat/use_cases/evaluation/data_augmented_question_answering_comparision.html?ref=blog.langchain.com). For speed/simplicity, we only evaluated 7 questions, so this suffers from incredibly small sample size issues.

Note that the imported code is still on a branch as we work to figure out the best abstractions for this new Chat paradigm.

First of all, how did GPT3 grade the two models?

- GPT3 grading GPT3: 4/7
- GPT3 grading ChatGPT: 4/7

And how did ChatGPT grade the two models?

- ChatGPT grading GPT3: 5/7
- ChatGPT grading ChatGPT: 4/7

It's interesting to look where the differences lie. There was one example that GPT3 graded as incorrect for both GPT3 and ChatGPT, but ChatGPT graded as correct for both. And there was a separate example that GPT3 graded as correct for both, but ChatGPT graded as incorrect for ChatGPT. Let's take a look.

First, the example that GPT3 graded as incorrect but ChatGPT as correct:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb256a83bd2fbf570ce5a_example0.png)

Here it looks like GPT3 may have graded it as incorrect due it the verbosity of the answers, but ChatGPT didn't mind that. An alternative explanation could be that ChatGPT was more able to actually understand that "praised her legal ability" was consistent with the answers given.

Next, the example that GPT3 graded as correct for both, but ChatGPT graded as incorrect for ChatGPT.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb256a83bd2fbf570ce64_example4-1.png)

We can see in this example that the GPT3 is nearly exactly the same as the real answer. This is almost certainly due to the fact that we used GPT3 to generate the question/answer pairs. The ChatGPT answer is more verbose, and while not technically incorrectly it is not as specific and direct as the GPT3 answer. Again, this is likely due to using GPT3 to generate the question/answer pairs. Note for self: may want to manually curate a test set for the future.

## What about the direct comparison?

The final evaluation we did was give the question, the answer, and both predicted answers to ChatGPT and ask it to compare the answers. Synthesizing the results here:

- GPT3 is more succinct than ChatGPT
- ChatGPT is more detailed than GPT3
- ChatGPT is more polite than GPT3

Keep in mind, that this is not just the base model, but also the prompts used. So not truly a comparison between the two models, but rather the existing chains.

## Next steps

Still lots to be done in exploring the ChatGPT API! How can you best use the `role` parameter? What does the `system` role actually do? What are the right abstractions for this new type of API?

Only time will tell. Exciting times!
