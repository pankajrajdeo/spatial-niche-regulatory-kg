---
title: "Introducing Airbyte sources within LangChain"
description: "Connect 300+ data sources to LangChain with Airbyte document loaders. Load from Stripe, Salesforce, Hubspot &amp; more directly in Python."
source: "https://www.langchain.com/blog/introducing-airbyte-sources-within-langchain"
category: "blog"
published: "2023-08-22T15:05:56.000Z"
author: "LangChain Accounts"
tags: [blog, introducing-airbyte-sources-within-langchain]
---

# Introducing Airbyte sources within LangChain

*Editor's Note: This post was written in collaboration with the *[*Airbyte*](https://airbyte.com/?ref=blog.langchain.com)* team. They've made it really easy to connect even more data sources to LangChain as document loaders.*

It’s now possible to utilize the Airbyte sources for [Gong](https://reference.langchain.com/python/langchain-community/document_loaders/airbyte/AirbyteGongLoader), [Hubspot](https://reference.langchain.com/python/langchain-community/document_loaders/airbyte/AirbyteHubspotLoader), [Salesforce](https://reference.langchain.com/python/langchain-community/document_loaders/airbyte/AirbyteSalesforceLoader), [Shopify](https://reference.langchain.com/python/langchain-community/document_loaders/airbyte/AirbyteShopifyLoader), Stripe, [Typeform](https://reference.langchain.com/python/langchain-community/document_loaders/airbyte/AirbyteTypeformLoader) and [Zendesk Support](https://reference.langchain.com/python/langchain-community/document_loaders/airbyte/AirbyteZendeskSupportLoader) directly within your LangChain-based application, implemented as [document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/?ref=blog.langchain.com).

For example, to load the Stripe invoices for a user, you can use the AirbyteStripeLoader. Installing it is super simple, when you have LangChain installed locally you only need to install the source you are interested in, and you are ready to go:

`pip install airbyte-source-stripe`

After that, simply import the loader and pass in configuration and the stream you want to load:

`from langchain.document_loaders.airbyte import AirbyteStripeLoader
config = {
 "client_secret": "&lt;secret key&gt;",
 "account_id": "&lt;account id&gt;",
 "start_date": "&lt;date from which to start retrieving records from in ISO format, e.g. 2020-10-20T00:00:00Z&gt;"
}
loader = AirbyteStripeLoader(config=config, stream_name="invoices")
documents = loader.load()
# use documents in vector store or otherwise
`

## Why does this matter?

This is the beginning of making Airbyte’s [300+ sources](http://docs.airbyte.com/integrations?ref=blog.langchain.com) available as document loaders in LangChain.

Airbyte can move data from just about any source to your warehouse or vector database to power your LLM use case (check out this[tutorial](https://airbyte.com/tutorials/chat-with-your-data-using-openai-pinecone-airbyte-and-langchain?ref=blog.langchain.com) for setting up such a data pipeline!). This is normally done by using Airbyte Cloud or a local Airbyte instance, setting up a connection, and running it on a schedule (or via API trigger) to make sure your data stays fresh.

But if you are just getting started and are running everything locally, using a full Airbyte instance (including the UI, scheduling service, scale-out capabilities, etc..) may be overkill.

With this release, it’s easier than ever to run any Python-based source in LangChain directly within your Python runtime - no need to spin up an Airbyte instance or make API calls to Airbyte Cloud.

## Moving between hosted and embedded Airbyte

As it’s the same code running under the hood, every Airbyte-built loader is compatible with the respective source in the Airbyte service. This means it’s trivial to lift your embedded loading pipeline into your self-hosted Airbyte installation or your Airbyte Cloud instance. The shape of the configuration object and the records is 100% compatible.

Running syncs on hosted Airbyte means:

- UI to keep track of running pipelines
- Alerting on failing syncs
- Easily running pipelines on a schedule

Running syncs with LangChain loaders means:

- No overhead for running yet another service
- Full control over timing and pipeline execution

## Mapping Airbyte records to LangChain documents

By default, each record gets mapped to a Document as part of the loader, with all the various fields in the record becoming the metadata of the record. The text portion of the document is left as an empty string. You can pass in a record handler to customize this behavior to build the text part of a record depending on the data:

`def handle_record(record, id):
 return Document(page_content=record.data["title"], metadata=record.data)
loader = AirbyteGongLoader(config=config, record_handler=handle_record, stream_name="calls")`

## Incremental loads

Since your python application is basically acting as the Airbyte platform, you have full control over how the “sync” is executed. For example you can still benefit from [incremental syncs](https://glossary.airbyte.com/term/incremental-synchronization/?ref=blog.langchain.com) if your stream supports it by accessing the “last_state” property of the loader. This allows you to load only documents that changed since the last time you loaded, allowing you to update an existing vector database effectively:

`import airbyte_cdk.models.airbyte_protocol import AirbyteMessage
with open('stripe_sync_checkpoint.json', 'wb') as file:
 file.write(loader.last_state.json())

// ... later
with open('stripe_sync_checkpoint.json', 'r') as file:
 current_state = AirbyteStateMessage.parse_raw(file.read())
incremental_loader = AirbyteStripeLoader(config=config, stream_name="invoices", state=current_state)
new_docs = incremental_loader.load()
`

## Custom sources

For now, the following Airbyte sources are available as pip packages (with more to come):

- [Gong](https://python.langchain.com/docs/integrations/document_loaders/airbyte_gong?ref=blog.langchain.com) pip install airbyte-source-gong
- [Hubspot](https://python.langchain.com/docs/integrations/document_loaders/airbyte_hubspot?ref=blog.langchain.com) pip install airbyte-source-hubspot
- [Salesforce](https://python.langchain.com/docs/integrations/document_loaders/airbyte_salesforce?ref=blog.langchain.com) pip install airbyte-source-salesforce
- [Shopify](https://python.langchain.com/docs/integrations/document_loaders/airbyte_shopify?ref=blog.langchain.com) pip install airbyte-source-shopify
- [Stripe](https://python.langchain.com/docs/integrations/document_loaders/airbyte_stripe?ref=blog.langchain.com) pip install airbyte-source-stripe
- [Typeform](https://python.langchain.com/docs/integrations/document_loaders/airbyte_typeform?ref=blog.langchain.com) pip install airbyte-source-typeform
- [Zendesk Support](https://python.langchain.com/docs/integrations/document_loaders/airbyte_zendesk_support?ref=blog.langchain.com) pip install airbyte-source-zendesk-support

However, if you have implemented your own custom Airbyte sources, it’s also possible to integrate them by using the AirbyteCDKLoader base class that works with the Source interface of the Airbyte CDK:

`from langchain.document_loaders.airbyte import AirbyteCDKLoader
from my_source.source import MyCustomSource # plug in your own source here
config = {
 # your custom configuration
}
loader = AirbyteCDKLoader(source_class=MyCustomSource, config=config, stream_name="my-stream")`

You can also install sources from the main Airbyte repository by installing directly via git - for example, to fetch the Github source, simply run

`pip install "source_github@git+https://github.com/airbytehq/airbyte.git@master#subdirectory=airbyte-integrations/connectors/source-github"`

After that, the source is available to be plucked into the AirbyteCDKLoader:

`from source_github.source import SourceGithub
issues_loader = AirbyteCDKLoader(source_class=SourceGithub, config=config, stream_name="issues")`

Check out [the connector development documentation](https://docs.airbyte.com/connector-development/?ref=blog.langchain.com) for how to get started writing your own sources - it’s easy to get started with them and will allow you to move from local embedded loaders to using a hosted Airbyte instance seamlessly depending on your needs.

## Any questions? We would love to hear from you

If you are interested in leveraging Airbyte to ship data to your LLM-based applications, [please take a moment](https://docs.google.com/forms/d/e/1FAIpQLSduobMZwbqiFlPxsWDG-hrBw6NLYMDu_7zRfo4j7AsaO1QtfQ/viewform?usp=sf_link&_gl=1*m4v6ic*_ga*MTM4ODAyNjg4NS4xNjY5ODkyNDQ1*_ga_HDBMVFQGBH*MTY5MjM2MzY0Ni45NS4xLjE2OTIzNjU2NDUuMC4wLjA.&ref=blog.langchain.com) to fill out our survey so we can make sure to prioritize the most important features.

If you have questions or are interested in other existing sources being exposed as loaders this way, do not hesitate to reach out on our [community slack channel](https://airbyte.com/community/community?ref=blog.langchain.com) or in the [Airbyte channel](https://discord.com/channels/1038097195422978059/1131406672972218430?ref=blog.langchain.com) on the LangChain discord server.
