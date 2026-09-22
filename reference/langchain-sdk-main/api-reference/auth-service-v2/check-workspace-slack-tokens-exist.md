---
title: "Check Workspace Slack Tokens Exist"
description: "Check if the workspace has any Slack tokens."
source: "https://docs.langchain.com/api-reference/auth-service-v2/check-workspace-slack-tokens-exist"
category: "docs"
tags: [docs, api-reference, auth-service-v2, check-workspace-slack-tokens-exist]
---

# Check Workspace Slack Tokens Exist

> Check if the workspace has any Slack tokens.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/auth/tokens/workspace/slack/exists**

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
  /v2/auth/tokens/workspace/slack/exists:
    get:
      tags:
        - Auth Service (v2)
      summary: Check Workspace Slack Tokens Exist
      description: Check if the workspace has any Slack tokens.
      operationId: >-
        check_workspace_slack_tokens_exist_v2_auth_tokens_workspace_slack_exists_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuthTokenStatusResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    OAuthTokenStatusResponse:
      properties:
        has_token:
          type: boolean
          title: Has Token
      type: object
      required:
        - has_token
      title: OAuthTokenStatusResponse
      description: Simple status indicating if a user has a token for a provider/agent.

````
