---
title: "RecAlign - The smart content filter for social media feed"
description: "RecAlign: An open-source Chrome extension using LLMs to filter your social media feed. Take control with transparent, configurable AI-powered filtering."
source: "https://www.langchain.com/blog/recalign-the-smart-content-filter-for-social-media-feed"
category: "blog"
published: "2023-04-22T14:35:24.000Z"
author: "LangChain Accounts"
tags: [blog, recalign-the-smart-content-filter-for-social-media-feed]
---

# RecAlign - The smart content filter for social media feed

**[Editor's Note] This is a guest post by Tian Jin. We are highlighting this application as we think it is a novel use case. Specifically, we think recommendation systems are incredibly impactful in our everyday lives and there has not been a ton of discourse on how LLMs will impact these systems.**

We've all experienced the pains of using recommender systems: you signed up for Twitter to keep up with latest AI research, but a click on a funny meme will flood your timeline with similar distractions. These systems work to maximize their owner’s profit, not your welfare. Here, we outline the rationale behind our LangChain-powered solution to address this problem at its core.

**Transparency & configurability.** In Brian Christian’s book the Alignment Problem, he shares an anecdote: his friend is recovering from alcohol addiction, but the recommender system knows, perhaps a little too well, about his love for alcohol and infests his feed with ads for alcohol. This episode is a vivid illustration of a recurring problem — recommender systems are skilled at catering to who we are today, but leaves little freedom for us to decide who we aspire to become. The current recommender systems lacks transparency and configurability. As a result, it is difficult for us to identify any problematic inferences that the recommender system made about our preferences, let alone modify them.

**Conflict of interest.** We cannot expect the owners of recommender systems (e.g., Twitter) to solve this lack of transparency and configurability due to a conflict of interest: system owners aim to maximize revenue, often prioritizing this objective over other desirable goals for users. This lead us to believe that to improve recommender systems, we must address the underlying conflict of interest. Users must have direct control over what they see as recommendations.

**A solution.** We propose to use large language models (LLMs) such as ChatGPT as smart content filters for social media feed, which are the outputs of recommendation systems on social media platforms. We developed an open source Chrome extension RecAlign ([https://github.com/tjingrant/RecAlign](https://github.com/tjingrant/RecAlign?ref=blog.langchain.com)) where you can specify your viewing preference in words such as *“I love reading about AI research”.* We then ask the LLM to intelligently determine whether each entry in the social media feed fits the user preference and remove all entries that violates it. We plan to develop other highly configurable augmentations such as feed re-ranking in the near future.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb237cbdf13f9a165cb0c_image.png)

A LLM-based smart content filter has the following benefits:

- **Configurable.** In the age of ChatGPT, English is the new programming language. We let users easily configure a smart content filter and see its effects immediately.
- **Transparent**. Your preference is right there, stated in words, in its entirety.
- **Flexible**. Our preference can be ephemeral. An easily configurable preference enables users to flexibly switch between different preferences.

**Join the cause**. Try RecAlign on Github at [https://github.com/recalign/RecAlign](https://github.com/recalign/RecAlign?ref=blog.langchain.com)! Consider watching/staring us for future development!

**LangChain**. LangChain plays a central role in our project. We use LangChain as an ergonomic interface to communicate with the OpenAI backend. We also rely on LangChain’s ability to easily format and parse the input to and output from LLMs. We highly recommend LangChain as it enables rapid prototyping and fast iteration on projects building with LLMs.

**Who we are**. We started as a team of two Ph.D. students in Computer Science from MIT and Harvard. This project kicked off when Xin was just 2 weeks away from his Ph.D. defense. Despite his otherwise good judgement he decides to work on this project. Thanks to LangChain, we released our first prototype with plenty of time for Xin to prepare for his defense!
