---
title: "Oauth Callback"
description: "Finalize an OAuth flow."
source: "https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback"
category: "docs"
tags: [docs, api-reference, auth-service-v2, oauth-callback]
---

# Oauth Callback

> Finalize an OAuth flow.

Claims the auth request, verifies the caller, exchanges the code, and saves the token.
Used by both the frontend bridge and the headless flow (where a customer-owned service
forwards the code/state, optionally proxied through smith-go).

User-subject sessions require the authenticated caller to match the initiator.
Agent-subject sessions (MDA Connect) skip that match — start is gated by
``deployments:create`` / service key, and the FE bridge may present a different
same-org workspace session to complete consent — then bind via
``host_oauth_agent_connections``.

## OpenAPI

**https://api.host.langchain.com/openapi.json post /v2/auth/callback/{provider_id}**

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
  /v2/auth/callback/{provider_id}:
    post:
      tags:
        - Auth Service (v2)
      summary: Oauth Callback
      description: >-
        Finalize an OAuth flow.

        Claims the auth request, verifies the caller, exchanges the code, and
        saves the token.

        Used by both the frontend bridge and the headless flow (where a
        customer-owned service

        forwards the code/state, optionally proxied through smith-go).

        User-subject sessions require the authenticated caller to match the
        initiator.

        Agent-subject sessions (MDA Connect) skip that match — start is gated by

        ``deployments:create`` / service key, and the FE bridge may present a
        different

        same-org workspace session to complete consent — then bind via

        ``host_oauth_agent_connections``.
      operationId: oauth_callback_v2_auth_callback__provider_id__post
      parameters:
        - name: provider_id
          in: path
          required: true
          schema:
            type: string
            title: Provider Id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OAuthFinalizeRequest'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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
    OAuthFinalizeRequest:
      properties:
        code:
          type: string
          title: Code
        state:
          type: string
          title: State
      type: object
      required:
        - code
        - state
      title: OAuthFinalizeRequest
      description: >-
        Request model for OAuth callback finalization (frontend bridge and
        headless).
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
