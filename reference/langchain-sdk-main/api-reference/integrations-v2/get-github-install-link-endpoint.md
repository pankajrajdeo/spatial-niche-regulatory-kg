---
title: "Get Github Install Link Endpoint"
description: "Create a GitHub App installation link."
source: "https://docs.langchain.com/api-reference/integrations-v2/get-github-install-link-endpoint"
category: "docs"
tags: [docs, api-reference, integrations-v2, get-github-install-link-endpoint]
---

# Get Github Install Link Endpoint

> Create a GitHub App installation link.

## OpenAPI

**https://api.host.langchain.com/openapi.json post /v2/integrations/github/installation-link**

````yaml
openapi: 3.1.0
info:
  title: LangSmith Deployment Control Plane API
  description: >
    The LangSmith Deployment Control Plane API is used to programmatically
    create and manage

    Agent Server deployments. For example, the APIs can be orchestrated to

    create custom CI/CD workflows.

    ## Host

    https://api.host.langchain.com

    ## Authentication

    To authenticate with the LangSmith Deployment Control Plane API, set the
    `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).

    ## Versioning

    Each endpoint path is prefixed with a version (e.g. `v1`, `v2`).

    ## Quick Start

    1. Call `POST /v2/deployments` to create a new Deployment. The response body
    contains the Deployment ID (`id`) and the ID of the latest (and first)
    revision (`latest_revision_id`).

    1. Call `GET /v2/deployments/{deployment_id}` to retrieve the Deployment.
    Set `deployment_id` in the URL to the value of Deployment ID (`id`).

    1. Poll for revision `status` until `status` is `DEPLOYED` by calling `GET
    /v2/deployments/{deployment_id}/revisions/{latest_revision_id}`.

    1. Call `PATCH /v2/deployments/{deployment_id}` to update the deployment.
  version: 0.1.0
servers: []
security: []
paths:
  /v2/integrations/github/installation-link:
    post:
      tags:
        - Integrations (v2)
      summary: Get Github Install Link Endpoint
      description: Create a GitHub App installation link.
      operationId: >-
        get_github_install_link_endpoint_v2_integrations_github_installation_link_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GithubInstallLink'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    GithubInstallLink:
      properties:
        install_url:
          type: string
          title: Install Url
        oauth_reuse_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Oauth Reuse Url
      type: object
      required:
        - install_url
      title: GithubInstallLink

````
