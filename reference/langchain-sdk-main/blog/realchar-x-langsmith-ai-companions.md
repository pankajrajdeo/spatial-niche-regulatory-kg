---
title: "RealChar x LangSmith: Using Open Source tools to create an AI companion"
description: "Learn how RealChar built an open-source AI companion platform using LangSmith for monitoring, observability, and evaluation at production scale."
source: "https://www.langchain.com/blog/realchar-x-langsmith-ai-companions"
category: "blog"
published: "2023-07-24T16:33:44.000Z"
author: "LangChain Accounts"
tags: [blog, realchar-x-langsmith-ai-companions]
---

# RealChar x LangSmith: Using Open Source tools to create an AI companion

***Editor’s Note: This blog post was written in collaboration with RealChar, an early ***[***LangSmith***](https://www.langchain.com/langsmith?ref=blog.langchain.com)*** BETA user. They moved fast and created something really, really sophisticated and really, really fun to use–all with open source tools.***

***We're also very excited about AI characters and companions internally, which is part of the reason we're excited to highlight RealChar. As seen by the meteoric rise of platforms like CharacterAI, allowing people to converse with different personas can be really fun. ***

***RealChar may be the most complete and most exciting OSS AI character framework out there. Besides impressive underlying technology, it also offers a really polished UI and UX. They were one of the top trending GitHub repos for basically all of last week, and we'd highly recommend that you check it out if you haven't already.***

We (RealChar team) are pleased to share our experience using LangSmith and working with LangChain team.

In case you don’t know, [RealChar](http://realchar.ai/?ref=blog.langchain.com) is an open source project to let you create, customize and talk to your AI character/companion in realtime (all in one codebase). We offer users natural and seamless conversations with AI on all the common platforms (mobile, web, terminal and desktop soon). We built RealChar leveraging some of best open source tools in the Generative AI/LLM space, including LangChain.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4cf4_image-5.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4cfd_image-6.png)

*Just a fun demo: asking AI Elon about whether he is afraid of losing in the much anticipated cage fight. Full version *[*here*](https://youtu.be/VR61lsWGj6k?ref=blog.langchain.com)*.*

RealChar received a ton of attention and usage from the community after [releasing](https://github.com/Shaunwei/RealChar?ref=blog.langchain.com) it just a week ago, and our site has undergo significant traffic. With conversations piling up and logs get cluttered very quickly, we found LangSmith to be a perfect tool for us to monitor and observe the traffic.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4d00_image-7.png)

It’s also easy to filter logs easily based on various conditions, to allow us track issues more accurately. For example, we can easily see all the errors when interacting with the Language Model, which has helped us understand and maintain our reliability better.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4cfa_image-8.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4d05_image-9.png)

LangSmith also allows us to identify important conversations and add to dataset easily. This is then helpful for us to evaluate and safe checking the prompts going forward, using the Evaluation features of LangSmith.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4d08_image-10.png)

The UI of LangSmith is also top-notch and easy to work with. It largely replaced our monitoring tools previously built in-house.

All these features are almost free to get as we already use LangChain. As soon as the API Key are set up in LangSmith, only a few environment variables are needed:

`LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=YOUR_LANGCHAIN_API_KEY
LANGCHAIN_PROJECT=YOUR_LANGCHAIN_PROJECT
`

Overall, we see LangSmith as a great tool for Analytics, Observability, and Evaluation, all in one place. It’s very useful for a production-level application with large volume of traffic like RealChar.

[/content/media/5101573/253656635-5de0b023-6cf3-4947-84cb-596f429d109e.mp4](https://storage.ghost.io/c/97/88/97889716-a759-46f4-b63f-4f5c46a13333/content/media/5101573/253656635-5de0b023-6cf3-4947-84cb-596f429d109e.mp4?ref=blog.langchain.com)
