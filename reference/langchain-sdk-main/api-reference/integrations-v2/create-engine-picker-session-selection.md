---
title: "Create Engine Picker Session Selection"
description: "Select an installation or begin a new GitHub App installation."
source: "https://docs.langchain.com/api-reference/integrations-v2/create-engine-picker-session-selection"
category: "docs"
tags: [docs, api-reference, integrations-v2, create-engine-picker-session-selection]
---

# Create Engine Picker Session Selection

> Select an installation or begin a new GitHub App installation.

## OpenAPI

**https://api.host.langchain.com/openapi.json post /v2/integrations/forge-github/picker-sessions/{session_id}/selection**

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
  /v2/integrations/forge-github/picker-sessions/{session_id}/selection:
    post:
      tags:
        - Integrations (v2)
      summary: Create Engine Picker Session Selection
      description: Select an installation or begin a new GitHub App installation.
      operationId: >-
        create_engine_picker_session_selection_v2_integrations_forge_github_picker_sessions__session_id__selection_post
      parameters:
        - name: session_id
          in: path
          required: true
          schema:
            type: string
            title: Picker session ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ForgeGithubPickerSelectionRequest'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnginePickerSelectResponse'
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
    ForgeGithubPickerSelectionRequest:
      properties:
        action:
          type: string
          enum:
            - ATTACH
            - INSTALL_NEW
          title: Action
          description: Whether to attach an installation or install the GitHub App.
        installation_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Installation Id
          description: GitHub installation ID required when action is ATTACH.
      type: object
      required:
        - action
      title: ForgeGithubPickerSelectionRequest
      description: Selection from a Forge GitHub App installation picker.
    EnginePickerSelectResponse:
      properties:
        redirect_url:
          type: string
          title: Redirect Url
      type: object
      required:
        - redirect_url
      title: EnginePickerSelectResponse
      description: |-
        Response for POST /forge/github/picker-session/{id}/select. The FE
        navigates the browser to `redirect_url` — that URL is either the FE
        result page (for "attach") or a github.com install picker (for
        "install_new"). Returning JSON instead of 302 keeps the FE's POST-as-API
        flow predictable and lets it surface errors before navigating.
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
