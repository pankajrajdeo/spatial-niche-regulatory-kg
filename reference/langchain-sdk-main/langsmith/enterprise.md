---
title: "LangSmith for Enterprise"
description: "Hosting options, access control, data privacy, cost controls, and security compliance for Enterprise users."
source: "https://docs.langchain.com/langsmith/enterprise"
category: "docs"
tags: [docs, langsmith, enterprise]
---

# LangSmith for Enterprise

> Hosting options, access control, data privacy, cost controls, and security compliance for Enterprise users.

This page is a reference hub for enterprise teams and includes information on features that are important for your organization, like [hosting options](#hosting-options), [access control](#access-control), [data privacy](#data-privacy-and-pii), and [cost controls](#cost-controls-and-usage).

> [!NOTE]
> For questions about Enterprise [pricing](pricing-plans.md) or to get started, [contact our sales team](https://www.langchain.com/contact-sales).

## Hosting options

Choose how to host LangSmith to match your infrastructure and data residency requirements.

#### [Cloud](cloud.md)
Host LangSmith in LangSmith's managed cloud with US or EU data residency.

#### [Hybrid](hybrid.md)
Run the control plane in LangSmith's cloud and your data plane in your own VPC for full data isolation.

#### [Self-hosted](self-hosted.md)
Host LangSmith entirely within your own infrastructure using Kubernetes.

## User management

Manage users and automate provisioning across your organization.

#### [User management](user-management.md)
Invite users, assign roles, and configure SCIM for automated provisioning and deprovisioning.

#### [SSO & JIT provisioning](authentication-methods.md)
Configure SAML or OIDC single sign-on and just-in-time user provisioning for your identity provider.

#### [Organization setup](set-up-hierarchy.md)
Create and configure organizations, workspaces, and the user hierarchy within your enterprise.

#### [Manage by API](manage-organization-by-api.md)
Programmatically manage users, configure security settings, and administer your organization via API.

## Access control

Control who can access what within your organization.

#### [Role-based access control (RBAC)](rbac.md)
Define permissions per workspace using built-in or custom roles. Available exclusively on Enterprise plans.

#### [Attribute-based access control (ABAC)](abac.md)
Apply fine-grained, tag-based access policies to restrict resource access—including blocking PII data from specific users.

#### [Workload isolation](workload-isolation.md)
Use multi-workspace models to isolate teams, establish trust boundaries, and separate environments.

#### [Resource tags](set-up-resource-tags.md)
Tag resources for use with ABAC policies and to organize environments like dev, staging, and prod.

## Data privacy and PII

Control how sensitive data is stored and accessed.

#### [Data storage & privacy](data-storage-and-privacy.md)
Understand what LangSmith stores, how encryption works, and how to opt out of telemetry and tracing.

#### [PII controls with ABAC](abac.md)
Use ABAC deny policies to restrict access to traces and datasets that contain personally identifiable information.

## Data retention & cleanup

Configure how long data is retained and how to delete it.

#### [Data purging for compliance](data-purging-compliance.md)
Set custom retention periods, delete traces by metadata, and meet deletion requirements.

#### [Data retention settings](usage-and-billing.md#data-retention)
Understand base vs. extended retention tiers, auto-upgrades, and how retention affects billing.

## Cost controls and usage

Track and limit spending across your organization.

#### [Billing & spend limits](billing.md)
Set monthly usage limits, track prepaid contract usage, and optimize tracing spend.

#### [Granular usage reporting](granular-usage.md)
Break down trace usage by workspace, project, user, or API key to attribute costs across teams.

## Security & compliance

Review LangSmith's security posture and compliance certifications.

#### [Shared responsibility model](shared-responsibility-model.md)
Review the security responsibilities shared between LangChain and your organization. LangSmith holds SOC 2 Type II, HIPAA, and GDPR certifications.

#### [Scalability & resilience](scalability-and-resilience.md)
Review SLA guarantees, disaster recovery strategies, and high availability configurations.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/enterprise.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
