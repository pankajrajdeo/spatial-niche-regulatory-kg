---
title: "Handling PII data in LangChain"
description: "Learn how to handle PII data in LangChain using Microsoft Presidio and OpaquePrompts to anonymize sensitive information and maintain GDPR compliance."
source: "https://www.langchain.com/blog/handling-pii-data-in-langchain"
category: "blog"
published: "2023-10-03T15:06:31.000Z"
author: "LangChain Accounts"
tags: [blog, handling-pii-data-in-langchain]
---

# Handling PII data in LangChain

This blog post was written by Francisco, a founder at [Pampa Labs](https://www.pampa.ai/?ref=blog.langchain.com), who assists companies in developing LLM applications that are accurate and cost efficient.

### Introduction

PII stands for “personally identifiable information” and it refers to personal data that can be used to uncover an individual’s identity. Lately, regulations such as [GDPR](https://www.google.com/search?q=gdpr+regulation&oq=gdpr&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDsyBggCEEUYPDIGCAMQRRg80gEHNTY0ajBqMagCALACAA&sourceid=chrome&ie=UTF-8&ref=blog.langchain.com) make it so that companies find it increasingly important to find solutions that consider handling PII data effectively.

Managing PII data with LLMs can be tricky. In many applications, you know when you are handling PII data because you explicitly ask for it in the shape of a form. In the case of chatbots, the user might spontaneously send PII data within the conversation (like presenting themselves with their name and surname) and depending on the application, this information might be sent to an LLM provider and logged for quality purposes.

There are some questions that commonly arise:

- What are the available options to mask PII data?
- What about LangSmith? If LangSmith logs my apps conversations, will it be logging PII data as well?
- Do we risk PII data being leaked if we send it to OpenAI? What about other providers?

While we don’t propose to have the definitive answers to these questions, by presenting a few options that are available today we can ignite the conversation on which are the best ways to handle PII data when working with LLMs.

### Why you should care about masking inputs for LLM providers

LLM providers like OpenAI, Anthropic and Cohere all have their own privacy policies which detail how they use the data sent to them when using their API. For example, some companies might use that data for investigating how to make models better or even use the data to train new models. Since LLMs can sometimes remember explicitly what they have learned in training, this could mean that future versions of their LLMs could potentially reproduce your PII data to other users.

Given the importance of these privacy policies and the fact that they might change over time, we strongly suggest users to take a look at providers’ privacy policies before using their services. As an example, [here’s](https://openai.com/policies/privacy-policy?ref=blog.langchain.com) OpenAI’s privacy policy.

### Sanitizing data for LLM providers

The first question is: how can we anonymize the data? The LangChain ecosystem is integrated with tools that make it easy to mask the data before using it in the application. Let’s take a look a a few of them:

***Microsoft Presidio***

Microsoft Presidio is a tool that facilitates PII identification and anonymization in input text. In other words, it can replace your text’s PII elements by generic equivalents. It is quite handy as it can replace credit card numbers, emails, phones, addresses and full names among other such entities.

Presidio works in two steps. First, it analyzes the text searching for PII data. This is probably the key differentiating feature in Presidio, since it uses a combination of different methods to identify the PII data in the text, including both rule based logic and NER Machine Learning models. As a second step, it anonymizes the data by replacing it by a a generic equivalent (i.e. ‘&lt;PERSON&gt;’). If using it within LangChain, the library uses [faker](https://faker.readthedocs.io/en/master/?ref=blog.langchain.com) to replace the entities by a fake value (‘John Smith’) to make the text more natural to the LLM.

If you want more detail on how Presidio identifies PII data, [here](https://microsoft.github.io/presidio/supported_entities/?ref=blog.langchain.com) you can find the entities Presidio detects out of the box, plus the methods used to detect them.

Using Presidio with LangChain is quite straightforward; one needs to add an extra step to the chain where the anonymization takes place, like so:

`anonymizer = PresidioAnonymizer()
template = """Rewrite this text into an official, short email:
{anonymized_text}"""
prompt = PromptTemplate.from_template(template)
llm = ChatOpenAI(temperature=0)
chain = {"anonymized_text": anonymizer.anonymize} | prompt | llm
response = chain.invoke(text)`

In the LangChain documentation we can find a full [tutorial](https://python.langchain.com/docs/guides/privacy/presidio_data_anonymization/?ref=blog.langchain.com) on how to use Microsoft Presidio plus a [tutorial](https://python.langchain.com/docs/guides/privacy/presidio_data_anonymization/multi_language?ref=blog.langchain.com) on how to use Presidio with non-English languages. If planning on using Presidio, you can also consider using it with [LLMGuard](https://github.com/laiyer-ai/llm-guard?ref=blog.langchain.com) which contains a suite of tools for LLM security including both input controls and guards (anonymization for PII data, jailbreaks) and output controls (malicious links, toxicity).

***OpaquePrompts***

Another good option to anonymize data is using [OpaquePrompts](https://opaqueprompts.opaque.co/?ref=blog.langchain.com). Instead of using several techniques in unison, OpaquePrompts uses one ML model to detect PII data and mask it appropriately.

One of the main advantages of using OpaquePrompts is just how easy it is to use with LangChain, where we just use an `OpaquePrompts` LLM class which we initialize with a LangChain LLM like `OpenAI`.

`chain = LLMChain(
 prompt=prompt,
 # llm=OpenAI(),
 llm=OpaquePrompts(base_llm=OpenAI()),
 memory=memory,
)`

Another of its differential aspects is that it uses[confidential computing](https://en.wikipedia.org/wiki/Confidential_computing?ref=blog.langchain.com)which means that not even their anonymization service can access the original data; a great feature for privacy seeking users. Finally, it will deanonymize the data after getting the response from the LLM so the user will get an answer that contains the original entities that they mentioned / requested.

### Sanitizing data for LangSmith

In case we want to use LangSmith to log our app’s conversations, we might face another challenge: saving the data in a sanitized form. If we just use the aforementioned tools in the way described earlier, the LLM provider will receive the input in a sanitized form but we would be saving the original, unsanitized input to LangSmith. How can we avoid this?

***Option #1: do not save inputs or outputs***

If we want to make sure we are not saving any PII data to LangSmith, we can just hide the inputs and outputs of all of our queries from LangSmith. This can be done with a few environmental variables that LangSmith will use to understand whether it needs to log inputs/outputs or not:

`LANGCHAIN_HIDE_INPUTS=true
LANGCHAIN_HIDE_OUTPUTS=true`

In this way we can directly control what is logged and what is not. For more information on this, please refer to the [docs](https://docs.smith.langchain.com/tracing/tracing-faq?ref=blog.langchain.com#how-do-i-mask-sensitive-information-in-my-runs).

It is important to note that if using this functionality, we should consider hiding both the inputs and the outputs since the LLM might mention PII data points in its answer (‘Hi John Smith! Nice to meet you’).

***Option #2: mask before saving***

Say we want to use the data in LangSmith to debug our application or we were thinking of finetuning a model of our own. In this case, not having the logs of our user’s conversations would hinder us from using real data to improve the quality of our application.

Another option for cases like this is to mask* *the input so that the LLM **and **the tracing software both receive masked inputs. This can be achieved by masking the input *before* sending it as input to the chain. This method has the advantage of allowing us to trace and later use the conversation data while also keeping the data sanitized for the LLM providers and LangSmith tracing.

### Conclusion

Handling PII data effectively is an important aspect of building safe and reliable data applications. We have presented a few proposed solutions for this problem but the LangChain ecosystem is consistently integrating new and innovative alternatives. Stay tuned to the LangChain [newsletter](https://blog.langchain.com/) to be the first to hear of new developments on this front!

If you enjoyed this blog post, we're also doing a webinar on this subject next week - [sign up here](https://www.crowdcast.io/c/6es3zwnv0ygy?ref=blog.langchain.com) to join!
