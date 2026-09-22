---
title: "How to Evaluate LLMs and Agents: Benchmarks, Evals, and Guardrails"
description: "When GSM8K launched in 2021, GPT-3 solved roughly 35% of its grade school math problems. Today, GPT-5.3 Codex scores 99%, and the benchmark no longer separates good models from great ones. A public..."
source: "https://www.langchain.com/resources/how-to-evaluate-llms"
category: "resources"
published: "2026-06-23"
author: "LangChain"
tags: [resources, how-to-evaluate-llms]
---

# How to Evaluate LLMs and Agents: Benchmarks, Evals, and Guardrails

When [GSM8K launched in 2021](https://arxiv.org/abs/2110.14168), GPT-3 solved roughly 35% of its grade school math problems. Today, GPT-5.3 Codex scores 99%, and the benchmark no longer separates good models from great ones. A public benchmark can feel like the kind of test suite you ship with traditional software: run it, read the score, ship if it is green. The issue is that you are running someone else’s tests for someone else’s program. Benchmarks can help you narrow down which model to start with, but they cannot tell you whether your application works. For that, you need evals built on your own data and tuned to the failure modes you care about most.

## Two layers of LLM evaluation

LLM evaluation works at two layers, and confusing them is how teams end up shipping models that look good on paper and break in production. The first layer is benchmarks: public test suites that score a model's raw capabilities on a fixed set of tasks. The second layer is agent evaluation: tests you write against your own data, your own failure modes, and the way your users actually use the system. [Benchmarks are useful](https://www.langchain.com/resources/llm-evaluation-benchmarks) for picking a starting model. Agent evals are what tell you whether the thing you built is good enough to ship.

What a benchmark actually does is run the model in isolation, on a fixed set of inputs, against fixed expected answers. Some use zero-shot prompts, with no examples. Others use few-shot prompts, where a handful of worked examples are included so the model can mimic the expected approach. The well-known suites each probe a different slice of capability: MMLU scores multiple-choice knowledge, TruthfulQA probes for confidently repeated misconceptions, and Chatbot Arena ranks models head-to-head by human preference votes.

Even when benchmarks look rigorous, their scores don’t predict production performance for two reasons. The first is saturation: once the leading models all score within a few points of a perfect 100, the benchmark has hit its ceiling and can no longer distinguish good models from great ones. Those compressed top-of-the-scale scores are what researchers mean by ["near-ceiling"](https://www.lxt.ai/blog/llm-benchmarks/). The second is contamination: when test questions leak into training data, scores reflect memorization as much as reasoning.

By 2024, GPT-4o, Claude 3.5, and Gemini 1.5 all scored above 90% on GSM8K, so the benchmark had limited headroom. [Zhang et al. introduced GSM1k](https://arxiv.org/html/2405.00332v1), a fresh benchmark designed to mirror GSM8K, and found that several model families performed worse on the uncontaminated set, suggesting some GSM8K scores were inflated by partial memorization.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a38a20eca0e46e56c55375c_blog1.png)

Even a clean, uncontaminated score only reflects how a model performs in isolation. It doesn’t answer the question you care about: whether your application works.

Application-level evaluation asks a different question: does this system work for users on a specific task? Benchmarks can’t answer that. Two products can share the same base model and still need opposite definitions of success. A legal research assistant succeeds when it returns precise, verifiable citations. A customer support bot succeeds when it resolves the customer’s issue.

A benchmark is a borrowed test suite. It works because someone else already wrote it and validated it. Your application has no equivalent to borrow, so you have to build your own evaluation.

## Comparing LLM evaluation methods

Application-level evals use five methods, and each trades coverage against trust differently, which is why an evaluation framework needs more than one. All five run in [LangSmith](https://www.langchain.com/langsmith-platform), our framework-agnostic AI agent observability platform, and [LangSmith Evaluations](https://www.langchain.com/langsmith/evaluation) implements each method as an evaluator type, so the choice is about fit rather than tooling. The table below compares all five.

Reference-based metrics compare outputs against known-good answers. [BLEU](https://github.com/huggingface/evaluate/blob/main/metrics/bleu/README.md) and [ROUGE](https://aclanthology.org/W04-1013.pdf) measure n-gram overlap, [BERTScore](https://arxiv.org/abs/1904.09675) uses embeddings to accept paraphrasing, and answer-matching metrics like [F1](https://en.wikipedia.org/wiki/F-score) and exact match grade extraction tasks in the style of [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/).

Reference-free metrics, such as [perplexity](https://huggingface.co/docs/transformers/en/perplexity), score properties of the output itself when you do not have ground-truth answers. Perplexity requires access to a model’s token probabilities, which makes it a better fit for open or self-hosted models. It tells you how well the model predicts text, not whether the text is correct for your task.

[LLM-as-a-judge](https://www.langchain.com/resources/llm-as-a-judge) uses a model with an evaluation prompt to grade outputs, which scales quality review beyond what human raters or deterministic checks can cover. On [MT-Bench](https://arxiv.org/abs/2306.05685), strong LLM judges reached over 80% agreement with human evaluators, though calibrating a judge to that level is its own task.

Code-based evaluators are deterministic checks written as functions, the cheapest signal available when a correct output has to satisfy a rule you can express in code.

Human annotation puts expert reviewers in the loop to supply ground-truth labels. This is the most reliable but slowest signal, and the source of the golden data that calibrates the other four methods.

| Method | What it measures | Best for | Key tradeoff | How it runs in LangSmith |
| --- | --- | --- | --- | --- |
| Reference-based metrics | Overlap with a reference answer (BLEU, ROUGE, F1, exact match, BERTScore) | Structured tasks with ground truth | Surface similarity can miss meaning | Evaluators scored against dataset reference outputs |
| Reference-free metrics | Intrinsic output properties (perplexity, fluency, length) | Screening when no ground truth exists | Says little about task success | Evaluators that run without reference outputs, including on live traces |
| LLM-as-a-Judge | Rubric-graded quality such as helpfulness and faithfulness | Nuanced quality at scale | Bias and variance until calibrated | LLM-as-Judge evaluators calibrated with Align Evals |
| Code/functional evaluators | Deterministic pass/fail checks | Outputs with strict, checkable formats | Cannot judge nuance | Code evaluators returning structured feedback |
| Human annotation | Expert judgment and golden labels | Expert-judgment tasks and golden labels | Slow and expensive at volume | Annotation Queues routing traces to reviewers |

## Match methods to failure modes

Choose your evaluation method by starting from the failure mode you fear most.

1. **Hallucination (a groundedness judge):** RAG evaluation starts with hallucination detection. A faithfulness metric, often implemented as an LLM-as-a-judge evaluator, checks whether the response is grounded in the retrieved context. Victor Moreira, a product manager at LangChain, [describes the ideal setup in a recent LangSmith 101 video](https://www.youtube.com/watch?v=oSjAbx67f0k&t=2408s):

> "Typically, you would want to have in your ground truth the documents or data that your agent is retrieving or should reference. You can then check with your LLM-as-a-judge if the final response is grounded in the information from those documents."

1. **Format breakage (code/functional evaluators):** When the potential failure is malformed JSON, a missing field, or a blown token limit, the check belongs in code. It is deterministic, cheap to run on every example, and never disagrees with itself.

2. **Subjective quality drift (a calibrated judge):** Tone, helpfulness, and on-brand phrasing need an LLM-as-a-judge with a grading rubric, and the judge is itself a failure mode until you calibrate it. A December 2025 study of judge reliability found that even the top-performing judge models, Gemini-2.5-Pro and GPT-5, fail to [maintain consistent preferences](https://arxiv.org/abs/2512.16041) in nearly a quarter of difficult cases. The same research line documents verbosity bias, self-enhancement bias, and position bias, each varying across judges and tasks. [Align Evals](https://www.langchain.com/blog/introducing-align-evals) closes that gap by collecting human corrections on judge scores, calibrating the judge with few-shot examples built from those corrections, and tracking agreement over time.

3. **Adversarial inputs (red teaming):** Red teaming covers the inputs that no curated dataset anticipates, from prompt injections and jailbreaks to users probing for unsafe outputs. Treat every successful attack as a future test case rather than a one-off patch.

4. **High-stakes correctness (Annotation Queues):** Medical, legal, and financial outputs call for human-in-the-loop evaluation, and that review needs structure to scale. [Annotation Queues](../langsmith/annotation-queues.md) route traces to domain experts, product managers, and clinicians with task-specific instructions, let reviewers leave feedback and supply ground-truth corrections, and feed those corrections back into your dataset for future evals. Here’s Victor again [describing why the corrections are valuable](https://www.youtube.com/watch?v=oSjAbx67f0k&t=1481s):

> "As a reviewer, I might have way more context of what this agent should say in reality, the golden ground truth of what it should say here. Even if your agent made a mistake, it's helpful to correct that mistake and save that as part of your dataset."

The fastest way to make evals durable is to store reviewer corrections as labeled examples. That set becomes the regression suite that catches the same failure before it ships again.

## Correct answers can hide broken reasoning

An agent can return the right final answer and still be broken. Correctness emerges across tool calls, sub-agent choices, and conversation turns that output-only scoring never sees: an agent can hallucinate a tool call and still get lucky on the result, or pull irrelevant documents and still synthesize a passable answer. Score only final outputs and those failures stay invisible until they compound in production.

When logic lived in code, an error came with a stack trace. Model reasoning has none, so the trajectory, the sequence of tool calls and sub-agent choices a run actually made, is all you have to trace what went wrong. Trajectory evals give you that record: they check whether the agent chose the right sub-agents, used the right tools, and sequenced them correctly across the run. Pair them with isolated runtimes, because without a sandbox you cannot safely replay tool calls, run generated code, or reproduce side effects in a way that is both realistic and non-destructive. Treat the runtime like a staging environment for agent behavior: execute the same steps in a controlled, resettable container, then add deterministic checks (schema validation, unit tests, invariants) so each run yields compiler-style pass/fail signals instead of subjective “looks good” judgments.

Agent benchmarks confirm the pattern but won't carry your evals. τ-bench put leading [function-calling models](https://arxiv.org/abs/2406.12045) below 50% task success in 2024, while its successor [τ²-Bench is already saturating](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) above 98% on telecom, the same arc GSM8K traced. That is why the evals you own outlast any benchmark cycle, and why trajectory scoring matters most where step order determines correctness: in regulated healthcare, finance, and legal work, the scored trajectory is the audit trail proving the agent followed protocol.

For conversational agents, the unit widens to the full thread, since success emerges across turns. Thread evaluators score the exchange once it goes idle, catching the case where a response looks correct but the user immediately says it isn't.

## Turn production failures into test cases

The eval system only works if it runs as a loop. Production traces become datasets, datasets become experiments, and experiments become shipping decisions.

Judge prompts get the attention because that work is visible. But the harder problems live in the mechanics of routing a failed production trace into a dataset and rerunning it as a regression test on every change.

We learned this on [Chat LangChain](https://chat.langchain.com/), our documentation assistant, which screens incoming questions with a guardrail that went stale during a product launch. When we shipped [Deep Agents](https://www.langchain.com/deep-agents), users came to Chat LangChain asking how to build with it, but the guardrail hadn't been updated and blocked them. Monitoring clustered the blocked requests under one failure mode, and once the traces showed the guardrail firing on legitimate questions, the fix was a prompt update. Without the loop, that signal arrives as scattered complaints days later.

Every failure caught this way belongs in a dataset, and the dataset can be small and still be effective. Offline evals use those examples to test known scenarios before release; online evals monitor production traces without ground truth, flagging quality and safety patterns you did not know to test yet. Together, they turn production behavior into the next round of evals.

## The runtime layer evals can't see

Offline evals show how your agent behaves on the cases you thought to test. Runtime governance covers every request it actually makes. The most serious failures rarely show up in a dataset. For example, an agent can leak a customer’s name to a model provider, or burn through the monthly API budget over a weekend, on requests nobody sampled.

This layer of LLMOps runs in line with production traffic, and LangSmith covers it with two platform components: [Sandboxes](https://www.langchain.com/langsmith/sandboxes) and the [LLM Gateway](https://www.langchain.com/blog/introducing-llm-gateway).

Sandboxes are isolated environments where agents can execute risky operations, like running arbitrary code or touching a filesystem, without affecting your main infrastructure. They are the staging environment for code that writes itself: a code-executing agent gets evaluated inside the same isolation it can later run in, which narrows the gap between the behavior your evals certified and the behavior production gets.

The LLM Gateway is a proxy that sits between your agents and the model providers they call. Provider API keys are stored in LangSmith as provider secrets rather than on every client, and each request passing through the gateway moves through five steps:

1. Authenticate the caller with a LangSmith API key.
2. Resolve the actual provider key from the workspace's provider secrets.
3. Evaluate governance policies, including spend limits, PII redaction, and secrets redaction.
4. Proxy the request to the upstream provider.
5. Trace the call to LangSmith.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a38a22b235f0819a1e9169b_blog2.png)

Three policies run on every request:

- **Spend limits** hard-block at the organization, workspace, API key, or user level. A caller that hits a cap receives a 402 response with an actionable error message, which turns the weekend budget burn from a postmortem into a blocked request.
- **PII protection** detects and redacts names, places, nationality, religion, political affiliation, and ages before a request ever reaches the model.
- **Secrets redaction** does the same for US phone numbers, US SSNs, API keys, tokens, and credentials.

Governance feeds the same observability that the evals run on. Every gateway-proxied call appears as a trace, and when a policy fires, the event flows into [LangSmith Engine](https://www.langchain.com/langsmith/engine) for triage: a blocked request leads to the trace that triggered it, and the trace leads to the fix, without leaving the product. In traditional software, we didn’t need to control each request at runtime. With agents, we do, because each request can create cost, privacy, or security risk.

## Where the loop starts

Evaluation threads through the entire [agent development lifecycle](https://www.langchain.com/blog/the-agent-development-lifecycle): build, test, deploy, monitor. Each stage produces the evidence the next one needs. Offline evals decide whether a change is ready to ship, traces from production show what actually happened, and those traces become the dataset that tests the next version. Teams that run the stages as one loop stop arguing about benchmark scores, because they are deciding from their own traffic.

Start by turning production traces into a dataset. Pull 50 production traces from your agent today, or write 50 representative inputs if you haven't shipped yet, and label each one pass or fail yourself. That labeled set seeds your first offline eval suite, calibrates your first LLM-as-a-judge evaluator, and baselines every experiment after it.

[LangSmith](https://www.langchain.com/langsmith-platform) is framework agnostic and works with [LangChain](https://www.langchain.com/langchain), [LangGraph](https://www.langchain.com/langgraph), [Deep Agents](https://www.langchain.com/deep-agents), another framework, or custom code, so you can start evaluating with LangSmith in whatever stack your agent is built on.
