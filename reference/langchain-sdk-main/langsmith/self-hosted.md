---
title: "Self-hosted LangSmith"
description: "Self-hosted LangSmith is an add-on to the Enterprise plan designed for our largest, most security-conscious customers. For more details, refer to Pricing. Contact our sales team if you want to get a..."
source: "https://docs.langchain.com/langsmith/self-hosted"
category: "docs"
tags: [docs, langsmith, self-hosted]
---

# Self-hosted LangSmith

> [!NOTE]
> Self-hosted LangSmith is an add-on to the Enterprise plan designed for our largest, most security-conscious customers. For more details, refer to [Pricing](https://www.langchain.com/pricing). [Contact our sales team](https://www.langchain.com/contact-sales) if you want to get a license key to trial LangSmith in your environment.

Host an instance of LangSmith in your own infrastructure for [observability](observability.md), [evaluation](evaluation.md), and [prompt engineering](prompt-context-hub.md#prompts). You can optionally enable [LangSmith Deployment](deploy-self-hosted-full-platform.md) to deploy and manage agents through the LangSmith UI.

> [!TIP]
> **For step-by-step setup instructions for self-hosted LangSmith on AWS, GCP, or Azure**, refer to our cloud architecture guides: [AWS](aws-self-hosted.md), [GCP](gcp-self-hosted.md), or [Azure](azure-self-hosted.md).

> [!NOTE]
> Before installing or upgrading, review the [minimum versions for self-hosting dependencies](self-host-dependency-versions.md).

<a id="langsmith" />

## What's included

A self-hosted LangSmith instance includes:

**Services:**

* LangSmith frontend UI
* LangSmith backend API
* LangSmith Platform backend
* LangSmith Playground
* LangSmith queue
* LangSmith ACE (Arbitrary Code Execution) backend

**Storage services:**

* ClickHouse (traces and feedback data)
* PostgreSQL (operational data)
* Redis (queuing and caching)
* Blob storage (optional, but recommended for production)

<img src="https://mintcdn.com/langchain-5e9cc07a/rqYqeBEA_2oeiw17/langsmith/images/cloud-arch-light.png?fit=max&auto=format&n=rqYqeBEA_2oeiw17&q=85&s=0790cbdf4fe131c74d1e60bb120834e3" alt="LangSmith architecture showing services and datastores" width="2210" height="1463" data-path="langsmith/images/cloud-arch-light.png" />

<img src="https://mintcdn.com/langchain-5e9cc07a/rqYqeBEA_2oeiw17/langsmith/images/cloud-arch-dark.png?fit=max&auto=format&n=rqYqeBEA_2oeiw17&q=85&s=767f3bc3dc73ffe1a806f54e0aaa428b" alt="LangSmith architecture showing services and datastores" width="2210" height="1463" data-path="langsmith/images/cloud-arch-dark.png" />

To access the LangSmith UI and send API requests, you will need to expose the [LangSmith frontend](#services) service. Depending on your installation method, this can be a load balancer or a port exposed on the host machine.

### Services

| Service                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="langsmith-frontend" /> **LangSmith frontend**                                                           | The frontend uses Nginx to serve the LangSmith UI and route API requests to the other servers. This serves as the entrypoint for the application and is the only component that must be exposed to users.                                                                                                                                                |
| <a id="langsmith-backend" /> **LangSmith backend**                                                             | The backend is the main entrypoint for CRUD API requests and handles the majority of the business logic for the application. This includes handling requests from the frontend and SDK, preparing traces for ingestion, and supporting the hub API.                                                                                                      |
| <a id="langsmith-queue" /> **LangSmith queue**                                                                 | The queue handles incoming traces and feedback to ensure that they are ingested and persisted into the traces and feedback datastore asynchronously, handling checks for data integrity and ensuring successful insert into the datastore, handling retries in situations such as database errors or the temporary inability to connect to the database. |
| <a id="langsmith-platform-backend" /> **LangSmith platform backend**                                           | The platform backend is another critical service that primarily handles authentication, run ingestion, and other high-volume tasks.                                                                                                                                                                                                                      |
| <a id="langsmith-playground" /> **LangSmith Playground**                                                       | The Playground is a service that handles forwarding requests to various LLM APIs to support the Playground feature. This can also be used to connect to your own custom model servers.                                                                                                                                                                   |
| <a id="langsmith-ace-arbitrary-code-execution-backend" /> **LangSmith ACE (Arbitrary Code Execution) backend** | The ACE backend is a service that handles executing arbitrary code in a secure environment. This is used to support running custom code within LangSmith.                                                                                                                                                                                                |

### Storage services

> [!NOTE]
> LangSmith will bundle all storage services by default. You can configure it to use external versions of all storage services. In a production setting, we **strongly recommend using external storage services**.

| Service                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="clickhouse" /> **ClickHouse**     | [ClickHouse](https://clickhouse.com/docs/en/intro) is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP).<br /><br />LangSmith uses ClickHouse as the primary data store for traces and feedback (high-volume data).<br /><br />💡 [Connect to external ClickHouse](self-host-external-clickhouse.md)                                                                                                                                                                                                  |
| <a id="postgresql" /> **PostgreSQL**     | [PostgreSQL](https://www.postgresql.org/about/) is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.<br /><br />LangSmith uses PostgreSQL as the primary data store for transactional workloads and operational data (almost everything besides traces and feedback).<br /><br />💡 [Connect to external PostgreSQL](self-host-external-postgres.md) - AWS RDS, GCP Cloud SQL, Azure Database                             |
| <a id="redis" /> **Redis / Valkey**      | [Redis](https://github.com/redis/redis) is a powerful in-memory key-value database that persists on disk. By holding data in memory, Redis offers high performance for operations like caching.<br /><br />LangSmith uses Redis to back queuing and caching operations. [Valkey](https://valkey.io/) is also officially supported as a drop-in replacement for Redis.<br /><br />💡 [Connect to external Redis or Valkey](self-host-external-redis.md) - AWS ElastiCache, GCP Memorystore, Azure Cache                                                                |
| <a id="blob-storage" /> **Blob storage** | LangSmith supports several blob storage providers, including [AWS S3](https://aws.amazon.com/s3/), [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/), and [Google Cloud Storage](https://cloud.google.com/storage).<br /><br />LangSmith uses blob storage to store large files, such as trace artifacts, feedback attachments, and other large data objects. Blob storage is optional, but highly recommended for production deployments.<br /><br />💡 [Enable blob storage](self-host-blob-storage.md) - AWS S3, GCP GCS, Azure Blob |

To install, follow the [Kubernetes setup guide](kubernetes.md).

## Next steps

* **[Enable LangSmith Deployment](deploy-self-hosted-full-platform.md)**: add a [control plane](control-plane.md) and [data plane](data-plane.md) to deploy and manage agents through the LangSmith UI.
* **[Enable LangSmith Sandboxes](deploy-self-hosted-full-platform.md#enable-sandboxes)**: allow users to run code, expose temporary services, and create memory snapshots from self-hosted LangSmith.
* **[Deploy standalone Agent Servers](deploy-standalone-server.md)**: deploy Agent Servers directly without enabling LangSmith Deployment.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
