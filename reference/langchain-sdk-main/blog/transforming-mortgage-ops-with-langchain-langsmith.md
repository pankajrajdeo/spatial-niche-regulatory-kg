---
title: "Transforming Mortgage Ops with LangChain &amp; LangSmith"
description: "See how InstaMortgage transformed mortgage operations with LangChain &amp; LangSmith, reducing resolution time by 67% and automating loan processing with AI."
source: "https://www.langchain.com/blog/transforming-mortgage-ops-with-langchain-langsmith"
category: "blog"
published: "2023-12-05T23:37:48.000Z"
author: "LangChain Accounts"
tags: [blog, transforming-mortgage-ops-with-langchain-langsmith]
---

# Transforming Mortgage Ops with LangChain &amp; LangSmith

*Editor's Note: This post was written by **Sasha Aptlin** at *[*Aptford*](https://aptford.com/?ref=blog.langchain.com) *through LangChain's Partner Program.*

Meet Maya, a loan officer at [InstaMortgage](https://instamortgage.com/?ref=blog.langchain.com), whose professional life was once consumed by the flood of loan applications and constant demands for accuracy and precision. Imagine her desk, buried under piles of paperwork, her inbox constantly filled with client requests, her days a never-ending cycle of entering data manually and conducting thorough reviews.

At InstaMortgage, Maya is not just a loan officer. She is a champion for customer service and education. Her objective is to make sure that the process of obtaining a home loan is transparent and straightforward. However, conventional methods frequently left her clients waiting for an answer for way too long, resulting in more confusion than empowerment.

Maya's experience was not unique. Loan officers throughout the mortgage industry encounter the same difficulties: outdated systems, manual procedures, and the need to juggle precision, accuracy, and client satisfaction. It was evident that the mortgage industry, which relied on traditional and error-prone methods, required a significant overhaul.

## Meet InstaAI

Leading the transformation, [InstaMortgage](https://instamortgage.com/?ref=blog.langchain.com) joined forces with [Aptford](https://aptford.com/?ref=blog.langchain.com) to create InstaAI, an AI platform reshaping the mortgage landscape with three core modules powered by Langchain & LangSmith:

- **Mortgage AI** navigates through complex data and guidelines, offering immediate, accurate guidance. Think of a challenging loan application that gets deciphered in minutes, not hours – Mortgage AI makes it possible.

![Mortgage AI](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a3a8_public.gif)

- **Content AI** enables the creation of clear, concise multi-media content, ensuring that clients are well informed. It also helps Loan Officers build credibility and reputation through content creation that is relevant and educational for future homeowners. Imagine a client receiving tailor-made insights that make complex mortgage concepts easily digestible in the distinctive voice of InstaMortgage – that's ContentAI at work.

![Content AI](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a3b0_public.gif)

- **Policy AI** clarifies InstaMortgage policies, employment practices, benefits, compliance, and communication standards. An ever-present guide, it nurtures a positive, productive workplace environment where every team member can thrive.

![Policy AI](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a3b3_public.gif)

With InstaAI, Maya's role underwent a radical change. Her job evolved from juggling tedious tasks to fostering meaningful relationships at scale. "InstaAI hasn't just changed how I work; it's redefined my role, supercharging my efforts of enriching the experience for our clients,” she remarks.

## InstaMagic of LangChain & LangSmith

LangChain's [LCEL](https://python.langchain.com/docs/expression_language/?ref=blog.langchain.com) has been instrumental in developing InstaAI's three core modules, simplifying the construction of dynamic prompts across various data sources, most of which are more than 500 pages long and include tabular data. Under the hood, each user request is rephrased into a question by a separate chain, which is then used to pick the sources to pull from in parallel. The retrieved chunks, enriched with metadata about their source, are then injected into the context before the final run of the “Writer” chain.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a39f_image-10.png)

To generate content ideas, InstaAI follows a straightforward multi-step process. Here's how it works:

1. Randomly select blog posts from the InstaMortgage sitemap.
2. Analyze the selected blog posts using an LLM to identify any missing points or generate related ideas.
3. Create a rough draft based on one of the seven content types and context from the knowledge base.
4. Refine the draft and extract important details such as summary, hashtags, duration (for video scripts), or call-to-action (CTA) into a Pydantic model for future user review.

LCEL has simplified the developer experience to a couple of lines of Python for each of the steps above.

LangSmith had an important role in debugging and logging throughout the development process, as well as monitoring performance in production. Its debugging capabilities enabled precise monitoring and improvement of interactions within each module. By visualizing the exact sequence of events in complex chains that retrieve context from various sources, LangSmith provided insights into the inputs and outputs of LLM calls and ensured that the conversational aspects of MortgageAI, ContentAI, and PolicyAI were logical, precise, and user-friendly.

## Results

Mortgage questions that used to take hours to research can now be completed in minutes or even seconds. InstaAI has not only improved efficiency but also strengthened client relationships. Early results show that speed to resolution has increased by an average of 67%, and error rates have significantly decreased. The impact on client satisfaction is clear, with testimonials like Rupert's, a long-term client who said, "The speed and accuracy in handling my request were unlike anything I've experienced before." This transformation also benefits our employees, as Shashank Shekhar, CEO of InstaMortgage, explains: "With our newfound capabilities, our team can focus on more challenging and fulfilling tasks, thus making their work at InstaMortgage less tedious and way more rewarding.” He further added that the company intends to continue working with LangChain to further its AI capabilities and become a truly AI-powered mortgage company that delivers the best experience for both its employees and clients.
