---
title: "AI-Powered Medical Knowledge: Revolutionizing Care for Rare Conditions"
description: "LangChain AI chatbots use retrieval-augmented generation to make specialized medical knowledge accessible for rare conditions like appendiceal cancer."
source: "https://www.langchain.com/blog/ai-powered-medical-knowledge"
category: "blog"
published: "2023-04-17T19:27:06.000Z"
author: "LangChain Accounts"
tags: [blog, ai-powered-medical-knowledge]
---

# AI-Powered Medical Knowledge: Revolutionizing Care for Rare Conditions

**[Editor's Note]: This is a guest post by Jack Simon, who recently participated in a hackathon at Williams College. He built a LangChain-powered chatbot focused on appendiceal cancer, aiming to make specialized knowledge more accessible to those in need. If you are interested in building a chatbot for another rare condition, please reach out to jms9@williams.edu.**

**The reason we are highlighting this is that we think it is a fantastic and under-appreciated use case for question-answering systems. While the underlying tech may be similar to other question-answering applications, we find this use case particularly high-impact for society.**

Last week, I participated in a hackathon at Williams College, where I built a chatbot that changes the landscape of how we access information about rare medical conditions. By incorporating literature reviews, clinical trial data, and academic papers, I created a LangChain-powered chatbot that provides valuable information on a specific rare medical condition, appendiceal cancer.

0:00/1×

While this demo focuses on one rare medical condition, I plan to expand the chatbot's knowledge base by adding information about as many rare conditions as possible. The ultimate vision is to create an AI-driven application that can serve as a reliable source of information for patients and healthcare professionals alike.

Rare conditions often leave patients isolated and without proper guidance, mainly because there are only a handful of experts who specialize in these conditions. Moreover, these professionals are often inundated with work, leaving little time to engage with individual patients. Few online resources are available, and most are written in medical jargon, making it difficult for patients to comprehend the information. ChatGPT, unfortunately, is no help with rare conditions; although the model was trained on a massive, web-scale dataset, most of the relevant information for less common conditions was either not included or was too sparse for the model to learn much about. As a result, ChatGPT's responses are incomplete and oftentimes blatantly wrong.

In light of these challenges, I used a [retrieval-augmented generation (RAG) approach](https://blog.langchain.com/retrieval/) to make use of multiple sources of knowledge—those that are baked into the model parameters and the information that is contained in the contextual passages—to design a model that [appears to outperform GPT-4](https://ai.facebook.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/?ref=blog.langchain.com), as well as Bio_ClinicalBERT, BioBERT, BlueBERT, PubMedBERT, and SciBERT on tasks that require specific knowledge on appendiceal cancer.

Retrieval-augmented generation is an NLP architecture that employs external documents to supplement its knowledge. The RAG approach offers a significant advantage by accessing more fine-grained data, even data that was not available during the base model's training. This method involves retrieving contextual documents from external datasets, such as a corpus of literature reviews, clinical trial information, and academic papers during its execution. The model then combines these contextual documents with the original input to generate an output.

Despite the progress made by existing models and datasets in offering more specific information about common medical conditions, they struggle to provide the necessary information for cases with fewer than 1,000 patients. This is because they lack sufficient details on clinical trials, community support forums, and expert practitioners for rare conditions. The challenges associated with these limitations arise from the high costs of training these models and the current infeasibility of collecting comprehensive data on rare conditions at scale.

By building a chatbot that can access and understand vast amounts of medical literature, we can bridge the gap between patients and the knowledge they need. This AI-driven approach is not only practical but also compelling in its potential to revolutionize healthcare.

With the advancements in AI and open source large language model frameworks like LangChain, the information problem surrounding rare medical conditions can now be addressed.

The chatbot I built serves as a proof of concept that such a tool can be created to assist patients and healthcare professionals. By expanding the chatbot's knowledge base to cover more rare conditions, I plan to create a platform that offers valuable insights and information without overwhelming patients and families with complex medical terminology.

I believe that AI-powered chatbots have the potential to significantly improve the healthcare industry, particularly in the realm of rare conditions. As we continue to develop and refine these AI-driven tools, we can create a more accessible and inclusive healthcare system that empowers patients and healthcare professionals alike.

If you're interested in learning more about this project or getting involved, please reach out to me via email or on [Twitter](https://twitter.com/jacktoowavy?ref=blog.langchain.com). Together, we can work towards making information about rare medical conditions more accessible and ultimately improve the lives of those affected by these conditions.
