---
title: "Get Free Deployment Count"
description: "Return the number of free deployments used by the caller's organization."
source: "https://docs.langchain.com/api-reference/deployments-v2/get-free-deployment-count"
category: "docs"
tags: [docs, api-reference, deployments-v2, get-free-deployment-count]
---

# Get Free Deployment Count

> Return the number of free deployments used by the caller's organization.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/deployments/free-count**

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
  /v2/deployments/free-count:
    get:
      tags:
        - Deployments (v2)
      summary: Get Free Deployment Count
      description: Return the number of free deployments used by the caller's organization.
      operationId: get_free_deployment_count_v2_deployments_free_count_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreeDeploymentCountResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    FreeDeploymentCountResponse:
      properties:
        count:
          type: integer
          title: Count
          description: >-
            Number of free deployments currently used by the caller's
            organization.
      type: object
      required:
        - count
      title: FreeDeploymentCountResponse
      description: Response body for the free-deployment count endpoint.

````
