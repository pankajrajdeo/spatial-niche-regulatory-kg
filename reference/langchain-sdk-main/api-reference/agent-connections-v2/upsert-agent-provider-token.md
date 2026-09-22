---
title: "Upsert Agent Provider Token"
description: "Import an OAuth token and bind it to the agent for the given provider."
source: "https://docs.langchain.com/api-reference/agent-connections-v2/upsert-agent-provider-token"
category: "docs"
tags: [docs, api-reference, agent-connections-v2, upsert-agent-provider-token]
---

# Upsert Agent Provider Token

> Import an OAuth token and bind it to the agent for the given provider.

Replaces any prior connection for the same agent+provider. The previously
linked token is deleted only when it is agent-owned (no user owner) and no
other agent connections still reference it — user vault credentials and
shared tokens are left intact. Tokens are stored without a LangSmith user
owner so synthetic MDA actor agent_ids resolve via the agent-connection path.

## OpenAPI

**https://api.host.langchain.com/openapi.json post /v2/auth/agents/{agent_id}/providers/{provider_id}/tokens**

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
  /v2/auth/agents/{agent_id}/providers/{provider_id}/tokens:
    post:
      tags:
        - Agent Connections (v2)
      summary: Upsert Agent Provider Token
      description: >-
        Import an OAuth token and bind it to the agent for the given provider.

        Replaces any prior connection for the same agent+provider. The
        previously

        linked token is deleted only when it is agent-owned (no user owner) and
        no

        other agent connections still reference it — user vault credentials and

        shared tokens are left intact. Tokens are stored without a LangSmith
        user

        owner so synthetic MDA actor agent_ids resolve via the agent-connection
        path.
      operationId: >-
        upsert_agent_provider_token_v2_auth_agents__agent_id__providers__provider_id__tokens_post
      parameters:
        - name: agent_id
          in: path
          required: true
          schema:
            type: string
            description: Agent ID
            title: Agent Id
          description: Agent ID
        - name: provider_id
          in: path
          required: true
          schema:
            type: string
            description: OAuth provider ID
            title: Provider Id
          description: OAuth provider ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpsertAgentProviderTokenRequest'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentConnectionResponse'
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
    UpsertAgentProviderTokenRequest:
      properties:
        access_token:
          type: string
          title: Access Token
        refresh_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Refresh Token
        expires_in_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          title: Expires In Seconds
        scopes:
          items:
            type: string
          type: array
          title: Scopes
          default: []
        provider_account_label:
          anyOf:
            - type: string
            - type: 'null'
          title: Provider Account Label
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Metadata
      type: object
      required:
        - access_token
      title: UpsertAgentProviderTokenRequest
      description: |-
        Import an OAuth token and bind it to an agent for a provider.

        Used by Managed Deep Agents Connect flows that obtain tokens out-of-band
        (e.g. Google OAuth for Gmail) and need them stored under a synthetic
        agent_id for toolserver resolution.
    AgentConnectionResponse:
      properties:
        id:
          type: string
          title: Id
        agent_id:
          type: string
          title: Agent Id
        oauth_token_id:
          type: string
          title: Oauth Token Id
        provider_id:
          type: string
          title: Provider Id
        provider_account_label:
          anyOf:
            - type: string
            - type: 'null'
          title: Provider Account Label
        scopes:
          items:
            type: string
          type: array
          title: Scopes
        expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expires At
        created_by:
          type: string
          title: Created By
        created_at:
          type: string
          format: date-time
          title: Created At
      type: object
      required:
        - id
        - agent_id
        - oauth_token_id
        - provider_id
        - provider_account_label
        - scopes
        - expires_at
        - created_by
        - created_at
      title: AgentConnectionResponse
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
