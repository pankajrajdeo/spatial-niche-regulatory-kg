---
title: "LangChain &lt;&gt; Unstructured"
description: "Load documents of any type into LangChain with Unstructured integration. Extract text from PDFs, PowerPoints, images, and more to combine LLMs with your data."
source: "https://www.langchain.com/blog/langchain-unstructured"
category: "blog"
published: "2023-02-06T07:32:46.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-unstructured]
---

# LangChain &lt;&gt; Unstructured

One of the core value props of LangChain is the ability to combine Large Language Models with your own text data. There are multiple ([four!](https://python.langchain.com/docs/modules/chains/document/?ref=blog.langchain.com)) different methods of doing so, and [many](https://langchain.readthedocs.io/en/latest/use_cases/question_answering.html?ref=blog.langchain.com) [different](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com) applications this can power.

A step that sits upstream of using text data is the ability to get your data into a text form. This can be rather tricky due to the multitude of different formats that exist out there.

Enter... [unstructured.io](https://www.unstructured.io/?ref=blog.langchain.com).

Unstructured is a company with a mission of transforming natural language data from raw to machine ready. One of the main ways they do this is with an [open source Python package](https://github.com/Unstructured-IO/unstructured?ref=blog.langchain.com). This package as support for [MANY](https://github.com/Unstructured-IO/unstructured?ref=blog.langchain.com#document-parsing) different types of file extensions: `.txt`, `.docx`, `.pptx`, `.jpg`, `.png`, `.eml`, `.html`, and `.pdf` documents.

After playing around with Unstructured, we realized that by integrating with it we could easily start to build out first class support for loading documents of all types into a format that LangChains could work with. So we created the [Document Loaders module](https://python.langchain.com/docs/modules/data_connection/document_loaders/?ref=blog.langchain.com), a large part of which is powered by Unstructured.

There are currently two loaders that are powered by Unstructured. Both seem rather simple, but are quite powerful.

The first is the [UnstructuredFileLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/unstructured_file?ref=blog.langchain.com). This has a simple interface (you just pass it a file path) but under the hood Unstructured is doing a lot of smart logic to infer which data type it is (PDF, PowerPoint, image, etc) and extract text.

The second is the [DirectoryLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/how_to/file_directory?ref=blog.langchain.com). Again, this has a pretty simple interface: it takes only a path to a directory and an optional regex to glob for files against. But under the hood it is looping over all files and using the above UnstructuredFileLoader to load them. This makes it possible to load files of all types in a single call.

We're incredibly excited to have made this integration with Unstructured. With their focus on transforming raw data into clean text, it makes it incredibly easy to combine language models with your data, no matter what form it is in.
