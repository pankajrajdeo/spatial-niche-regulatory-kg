---
title: "LangSmith BYOC is now generally available on AWS"
description: "LangSmith Bring Your Own Cloud is now generally available on AWS, giving Enterprise teams managed observability, evaluation, and deployment inside their own VPC."
source: "https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws"
category: "blog"
published: "2026-08-12T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, langsmith-byoc-is-now-generally-available-on-aws]
---

# LangSmith BYOC is now generally available on AWS

Today, LangSmith Bring Your Own Cloud (BYOC) is generally available on Amazon Web Services (AWS).

BYOC gives enterprises a managed LangSmith deployment that runs in their own AWS account and VPC. Sensitive application data, including traces, datasets, experiments, prompts, agent deployments, and sandbox data, stays in the customer's AWS environment. LangChain provisions and operates the deployment, including monitoring, upgrades, scaling, and cluster lifecycle management.

For teams taking AI agents from pilot to production, this removes a common blocker. Agent traces and runtime data often include PII, PHI, customer records, internal API responses, tool outputs, and other sensitive context. Those teams need LangSmith's observability, evaluation, deployment, and management capabilities, but they also need their data to stay inside the cloud boundary they already govern.

With BYOC on AWS, customers can:

- Keep sensitive LangSmith data in their own AWS account and VPC
- Spend less time managing infrastructure and more time building, evaluating, and improving agents
- Scale agent development across teams and regions while keeping agents close to private systems

BYOC is available for Enterprise customers across 15 AWS regions in the US, EU, and APAC.

[Contact us](https://www.langchain.com/contact-sales) to enable BYOC for your organization.

## Why we built BYOC

Teams adopt LangSmith in different ways depending on their security, compliance, and operational requirements.

LangSmith Cloud remains the fastest way to get started when a managed SaaS deployment fits the organization's data and network requirements. Self-hosted LangSmith gives teams full control over how the platform is deployed and operated in their own environment. But that control comes with real operational responsibility.

A self-hosted deployment needs dedicated infrastructure support to size and maintain databases, manage Kubernetes, configure networking, apply upgrades, monitor reliability, handle backups, and support the deployment over time. For teams scaling agents across the enterprise, that operating model adds cost and takes time away from deploying and improving agent workloads.

LangSmith BYOC is designed for teams that want the data residency and network isolation of a self-hosted deployment, with the operational experience of a managed service. The customer owns the AWS account, VPC, databases, object storage, and sensitive application data. LangChain operates the LangSmith deployment on the customer's behalf.

This model is especially useful for teams in regulated or security-sensitive environments, including financial services, healthcare, cybersecurity, and large enterprises with strict data governance requirements.

## A managed LangSmith deployment inside your AWS boundary

A BYOC deployment runs across two planes.

- **The control plane runs in LangChain's cloud.** It handles authentication, user management, organization and workspace configuration, billing and usage metadata, and the LangSmith frontend. It also provisions, monitors, and orchestrates customer data planes. The control plane does not hold sensitive application data.
- **The data plane runs in the customer's AWS account.** It contains the VPC, private Amazon Elastic Kubernetes Service (EKS) cluster, databases, object storage, and sensitive LangSmith data. This includes traces, prompts, datasets, experiments, evaluators, Insights runs, annotation queues, agent deployments, sandboxes, and other runtime data.

Communication between the control plane and data plane uses AWS PrivateLink and does not cross the public internet.

The management path exposes only the Kubernetes API server for the customer's cluster, which LangChain's control plane uses to install and reconcile LangSmith components in customer data planes. The runtime path lets the data plane call the control plane for authentication, workspace configuration, telemetry, and billing metadata. The Amazon EKS cluster is private, with no public API server endpoint and no public IPs on worker nodes.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7bb395231c0217a4374115_boyc-boundaries.png)

## What BYOC offers

BYOC gives teams the LangSmith capabilities they need to trace, evaluate, deploy, and manage agents in production from a data plane in their own AWS environment, with LangChain handling the operational work needed to scale across teams and regions.

**Data stays in the customer's account.** Sensitive application data is stored in the customer's AWS account, in the region they choose. LangChain can operate the platform without moving traces, datasets, prompts, experiments, or deployment data into LangChain's network.

**Agents can access private systems.** Because the data plane runs in the customer's VPC, agents and sandboxes can connect to internal databases, private APIs, and on-premises systems over existing network paths.

**Setup is faster than building a platform deployment from scratch.** Customers apply a Terraform module to create the IAM role LangChain uses for provisioning, then create a data plane in LangSmith. LangChain provisions the VPC, Amazon EKS cluster, databases, storage, ingress, and in-cluster services.

**LangChain manages the operational lifecycle.** LangChain handles infrastructure upgrades, LangSmith version upgrades, scaling, patching, backups, and health monitoring. Customer engineering teams can focus on building and improving agents instead of operating the LangSmith stack.

**The architecture scales across teams and regions.** Additional data planes can be created across environments, AWS accounts, and regions. Organization-level configuration such as users and roles carries across deployments, so teams can scale LangSmith adoption without creating separate operating models for every group.

**Operational access is auditable.** Urgent support uses explicit, customer-approved access patterns. LangSmith audit logs live in the data plane, Amazon EKS audit logs go to Amazon CloudWatch in the customer's account, and VPC flow logs land in an Amazon Simple Storage Service (Amazon S3) bucket the customer owns.

Customers are already using BYOC to bring LangSmith to production agent workloads in AWS environments with strict data and security requirements.

> *Our partners trust us to protect their data, and we take that responsibility very seriously. That’s why we work with LangChain and AWS to use LangSmith through BYOC. It gives our team the observability tooling we need to build and improve our AI agents while keeping sensitive data in our own highly secure environment.

-Rishabh Jain, Cofounder, Latent Health*

## Built on a standardized AWS architecture

Every BYOC data plane is provisioned from a standardized architecture similar to the one LangChain uses to run LangSmith Cloud.

Each deployment includes:

- A dedicated VPC in the customer's AWS account
- A private Amazon EKS cluster with no public API server endpoint
- Worker nodes with no public IPs
- A private load balancer
- DNS and ingress configured on the LangChain BYOC domain
- Daily backups for Amazon RDS and the trace store, written to Amazon S3 in the customer's account
- Autoscaling for LangSmith services and node capacity
- Multi-AZ Amazon RDS and Amazon ElastiCache with automatic failover

LangChain provisions and reconciles the data plane using Crossplane. Customers create an IAM role with the provided Terraform module, and Crossplane assumes that role to create and manage infrastructure in the customer's account.

The role is scoped to infrastructure management. Wherever AWS supports it, permissions are limited to resources with the `managed_by=langsmith` tag and specific name prefixes. The role does not include data-read permissions such as `s3:GetObject` on the trace bucket, `rds-db:connect` to PostgreSQL, or `elasticache:Connect` to Redis.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7bb470c8a145aa43954ec7_byoc-aws-architecture.png)

## LangSmith features available on BYOC

Most LangSmith capabilities are available on BYOC today, including the core workflows teams use to build, evaluate, deploy, and operate agents.

Available today:

- **Observability:** tracing, projects, dashboards, and alerts
- **Evaluation:** datasets, experiments, evaluators, and annotation queues
- **Insights:** automatic analysis of traces to surface usage patterns, recurring behaviors, and failure modes
- **Context Hub:** prompts, memory, and other context files
- **LangSmith Deployment:** deploy and manage agents inside the customer data plane
- **Sandboxes:** code execution and filesystem work on a dedicated node group in the customer account
- **LLM Gateway:** model access through one LangSmith API key with centralized spend, rate limit, and data protection policies
- **Fleet:** build and run no-code agents
- **SmithDB:** LangChain's observability backend for trace data, persisting to Amazon S3 in the customer account

Managed Deep Agents, the LLM auth proxy, and Engine are planned for BYOC support soon.

## Getting started

BYOC is available on AWS for customers on the LangSmith Enterprise plan.

To get started, [contact us](https://www.langchain.com/contact-sales) to discuss BYOC for your organization and [read the docs](../langsmith/byoc.md) for more detail.
