---
title: "List Forge Github Installations"
description: "List Forge GitHub App installations available to the workspace."
source: "https://docs.langchain.com/api-reference/integrations-v2/list-forge-github-installations"
category: "docs"
tags: [docs, api-reference, integrations-v2, list-forge-github-installations]
---

# List Forge Github Installations

> List Forge GitHub App installations available to the workspace.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/integrations/forge-github/installations**

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
  /v2/integrations/forge-github/installations:
    get:
      tags:
        - Integrations (v2)
      summary: List Forge Github Installations
      description: List Forge GitHub App installations available to the workspace.
      operationId: >-
        list_forge_github_installations_v2_integrations_forge_github_installations_get
      parameters:
        - name: page_size
          in: query
          required: false
          schema:
            type: integer
            maximum: 100
            minimum: 1
            description: Maximum number of resources to return.
            default: 20
            title: Page Size
          description: Maximum number of resources to return.
        - name: cursor
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Opaque cursor returned by the previous page.
            title: Cursor
          description: Opaque cursor returned by the previous page.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForgeGithubInstallationsList'
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
    ForgeGithubInstallationsList:
      properties:
        items:
          items:
            $ref: '#/components/schemas/ForgeGithubIntegration'
          type: array
          title: Items
          description: Forge GitHub App installations available to the workspace.
        next_cursor:
          anyOf:
            - type: string
            - type: 'null'
          title: Next Cursor
          description: Opaque cursor for the next page, if one exists.
      type: object
      required:
        - items
      title: ForgeGithubInstallationsList
      description: A page of Forge GitHub App installations.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ForgeGithubIntegration:
      properties:
        id:
          type: string
          format: uuid
          title: ID
          description: >-
            GitHub Integration ID.<br><br>For example, in the `POST
            /v2/deployments` request body, set `integration_id` to the value of
            this field.
        installation_id:
          type: integer
          title: Installation ID
          description: GitHub installation ID.
        name:
          type: string
          title: Name
          description: GitHub accout name.
        repository_selection:
          anyOf:
            - type: string
            - type: 'null'
          title: Repository Selection
          description: >-
            Whether the GitHub App install grants access to 'all' repos or only
            'selected' ones. When 'selected', newly created repos are not
            auto-included and must be added on GitHub.
        settings_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Settings URL
          description: >-
            Deep link to the install's GitHub settings page, where repo access
            can be edited. GitHub's installation `html_url`.
      type: object
      required:
        - id
        - installation_id
        - name
      title: ForgeGithubIntegration
      description: >-
        Engine ("forge") install metadata. Extends the shared shape with two

        fields the Engine repo picker needs to recover from a "selected

        repositories" install that doesn't grant the repo the user wants:

        `repository_selection` and `settings_url` (GitHub's per-install settings

        page, where repo access is edited). Kept off the base
        `GithubIntegration`

        so the public Deployments API contract is unchanged.
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
