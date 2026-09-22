---
title: "Authenticate"
description: "Get OAuth token or start authentication flow if needed."
source: "https://docs.langchain.com/api-reference/auth-service-v2/authenticate"
category: "docs"
tags: [docs, api-reference, auth-service-v2, authenticate]
---

# Authenticate

> Get OAuth token or start authentication flow if needed.

## OpenAPI

**https://api.host.langchain.com/openapi.json post /v2/auth/authenticate**

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
  /v2/auth/authenticate:
    post:
      tags:
        - Auth Service (v2)
      summary: Authenticate
      description: Get OAuth token or start authentication flow if needed.
      operationId: authenticate_v2_auth_authenticate_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AuthAuthenticateRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthAuthenticateResponse'
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
    AuthAuthenticateRequest:
      properties:
        user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: User Id
        ls_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Ls User Id
        agent_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Agent Id
        provider:
          type: string
          title: Provider
        scopes:
          items:
            type: string
          type: array
          title: Scopes
        use_agent_builder_public_oauth:
          type: boolean
          title: Use Agent Builder Public Oauth
          default: false
          include_in_schema: false
        force_new:
          type: boolean
          title: Force New
          default: false
        token_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Token Id
        redirect_uri:
          anyOf:
            - type: string
            - type: 'null'
          title: Redirect Uri
        is_default:
          type: boolean
          title: Is Default
          default: true
        check_only:
          type: boolean
          title: Check Only
          default: false
          include_in_schema: false
      type: object
      required:
        - provider
        - scopes
      title: AuthAuthenticateRequest
      description: Auth authenticate request.
    AuthAuthenticateResponse:
      properties:
        status:
          $ref: '#/components/schemas/AuthStatus'
        url:
          anyOf:
            - type: string
            - type: 'null'
          title: Url
        auth_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Auth Id
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: User Id
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Metadata
      type: object
      required:
        - status
      title: AuthAuthenticateResponse
      description: Auth authenticate response.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AuthStatus:
      type: string
      enum:
        - completed
        - pending
        - connection_required
        - token_expired
      title: AuthStatus
      description: Valid authentication status values.
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
