---
title: "Deploy with control plane"
description: "Build Docker images and deploy applications to a self-hosted LangSmith instance using the control plane UI."
source: "https://docs.langchain.com/langsmith/deploy-with-control-plane"
category: "docs"
tags: [docs, langsmith, deploy-with-control-plane]
---

# Deploy with control plane

> Build Docker images and deploy applications to a self-hosted LangSmith instance using the control plane UI.

> [!NOTE]
> **This guide is for self-hosted LangSmith customers** who have [enabled LangSmith Deployment](deploy-self-hosted-full-platform.md#enable-langsmith-deployment) on their instance. For Cloud customers, see [Deploy on Cloud](deploy-to-cloud.md). For standalone Agent Servers without a control plane, see [Self-host standalone servers](deploy-standalone-server.md).

This guide shows you how to deploy your applications to a [self-hosted](self-hosted.md) LangSmith instance using a [control plane](control-plane.md). With a control plane, you build Docker images locally, push them to a registry that your Kubernetes cluster has access to, and deploy them with the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-with-control-plane).

## Topology

Enabling LangSmith Deployment on an existing self-hosted LangSmith instance adds a control plane, a data plane listener, and an operator that provisions Agent Servers in your cluster. The base LangSmith platform continues to handle observability, evaluation, and prompts; deployed Agent Servers send traces back to it.

For details on the components added by enabling LangSmith Deployment, see [Enable LangSmith Deployment](deploy-self-hosted-full-platform.md#enable-langsmith-deployment).

## Overview

Applications deployed to a self-hosted LangSmith instance with a control plane use Docker images. In this guide, the application deployment workflow is:

1. Test your application locally using `langgraph dev` or [Studio](studio.md).
2. Build a Docker image using the `langgraph build` command.
3. Push the image to a container registry accessible by your infrastructure.
4. Deploy from the [control plane UI](control-plane.md#control-plane-ui) by specifying the image URL.

## Prerequisites

Before completing this guide, you'll need the following:

* [LangSmith Deployment enabled](deploy-self-hosted-full-platform.md#enable-langsmith-deployment) on your self-hosted LangSmith instance.
* Access to the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-with-control-plane) with LangSmith Deployment enabled.
* A container registry accessible by your Kubernetes cluster. If using a private registry that requires authentication, you must configure image pull secrets as part of your infrastructure setup. Refer to [Private registry authentication](#private-registry-authentication).

## Step 1. Test locally

Before deploying, test your application locally. You can use the [LangGraph CLI](cli.md#dev) to run an Agent server in development mode:

```bash
langgraph dev
```

For a full guide local testing, refer to the [Local server quickstart](local-dev-testing.md).

## Step 2. Build Docker image

Build a Docker image of your application using the [`langgraph build`](cli.md#build) command:

```bash
langgraph build -t my-image
```

Build command options include:

| Option               | Default          | Description                                                       |
| -------------------- | ---------------- | ----------------------------------------------------------------- |
| `-t, --tag TEXT`     | Required         | Tag for the Docker image                                          |
| `--platform TEXT`    |                  | Target platform(s) to build for (e.g., `linux/amd64,linux/arm64`) |
| `--pull / --no-pull` | `--pull`         | Build with latest remote Docker image                             |
| `-c, --config FILE`  | `langgraph.json` | Path to configuration file                                        |

Example with platform specification:

```bash
langgraph build --platform linux/amd64 -t my-image:v1.0.0
```

For full details, see the [CLI reference](cli.md#build).

## Step 3. Push to container registry

Push your image to a container registry accessible by your Kubernetes cluster. The specific commands depend on your registry provider.

> [!TIP]
> Tag your images with version information (e.g., `my-registry.com/my-app:v1.0.0`) to make rollbacks easier.

## Step 4. Deploy with the control plane UI

The [control plane UI](control-plane.md#control-plane-ui) allows you to create and manage deployments, view logs and metrics, and update configurations. To create a new deployment in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-with-control-plane):

1. In the left-hand navigation panel, select **Deployments**.
2. In the top-right corner, select **+ New Deployment**.
3. In the deployment configuration panel, provide:
   * **Image URL**: The full image URL you pushed in [Step 3](#step-3-push-to-container-registry).
   * **Listener/Compute ID**: Select the listener configured for your infrastructure.
   * **Namespace**: The Kubernetes namespace to deploy to.
   * **Environment variables**: Any required configuration (API keys, etc.).
   * Other deployment settings as needed.
4. Select **Submit**.

The control plane will coordinate with your [data plane](data-plane.md) listener to deploy your application.

After creating a deployment, the infrastructure is [provisioned asynchronously](control-plane.md#asynchronous-deployment). Deployment can take up to several minutes, with initial deployments taking longer due to database creation.

From the control plane UI, you can view build logs, server logs, and deployment metrics including CPU/memory usage, replicas, and API performance. For more details, refer to the [control plane monitoring documentation](control-plane.md#monitoring).

> [!NOTE]
> A [LangSmith Observability tracing project](observability.md) is automatically created for each deployment with the same name as the deployment. Tracing environment variables are set automatically by the control plane.

## Update deployment

To deploy a new version of your application, create a [new revision](control-plane.md#revisions):

Starting from the LangSmith UI:

1. In the left-hand navigation panel, select **Deployments**.
2. Select an existing deployment.
3. In the Deployment view, select **+ New Revision** in the top-right corner.
4. Update the configuration:
   * Update the **Image URL** to your new image version.
   * Update environment variables if needed.
   * Adjust other settings as needed.
5. Select **Submit**.

## Private registry authentication

If your container registry requires authentication (e.g., AWS ECR, Azure ACR, GCP Artifact Registry, private Docker registry), you must configure Kubernetes image pull secrets before deploying applications. This is a one-time infrastructure configuration.

> [!NOTE]
> **This configuration is done at the infrastructure level, not per-deployment.** Once configured, all deployments automatically inherit the registry credentials.

Configure `imagePullSecrets` in your LangSmith Helm chart's `values.yaml` file. See the detailed steps in the [Enable LangSmith Deployment guide](deploy-self-hosted-full-platform.md#enable-langsmith-deployment).

For detailed steps on creating image pull secrets for different registry providers, refer to the [Kubernetes documentation on pulling images from private registries](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).

## Next steps

* **[Control plane](control-plane.md)**: Learn more about control plane features.
* **[Data plane](data-plane.md)**: Understand data plane architecture.
* **[Observability](observability.md)**: Monitor your deployments with automatic tracing.
* **[Studio](studio.md)**: Test and debug deployed applications.
* **[LangGraph CLI](cli.md)**: Full CLI reference documentation.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-with-control-plane.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
