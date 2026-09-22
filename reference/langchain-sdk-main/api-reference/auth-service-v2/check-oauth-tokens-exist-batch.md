---
title: "Check Oauth Tokens Exist Batch"
description: "Batch token-presence check: per requested provider, whether the current user has any token."
source: "https://docs.langchain.com/api-reference/auth-service-v2/check-oauth-tokens-exist-batch"
category: "docs"
tags: [docs, api-reference, auth-service-v2, check-oauth-tokens-exist-batch]
---

# Check Oauth Tokens Exist Batch

> Batch token-presence check: per requested provider, whether the current user has any token.

## OpenAPI

**https://api.host.langchain.com/openapi.json post /v2/auth/tokens/exists/batch**

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
  /v2/auth/tokens/exists/batch:
    post:
      tags:
        - Auth Service (v2)
      summary: Check Oauth Tokens Exist Batch
      description: >-
        Batch token-presence check: per requested provider, whether the current
        user has any token.
      operationId: check_oauth_tokens_exist_batch_v2_auth_tokens_exists_batch_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OAuthTokenStatusBatchRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuthTokenStatusBatchResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    OAuthTokenStatusBatchRequest:
      properties:
        provider_ids:
          items:
            type: string
          type: array
          title: Provider Ids
      type: object
      required:
        - provider_ids
      title: OAuthTokenStatusBatchRequest
      description: Provider IDs to check token presence for, for the current user.
    OAuthTokenStatusBatchResponse:
      properties:
        has_token:
          additionalProperties:
            type: boolean
          type: object
          title: Has Token
      type: object
      required:
        - has_token
      title: OAuthTokenStatusBatchResponse
      description: >-
        Per-provider token presence for the current user (provider_id ->
        has_token).
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````
