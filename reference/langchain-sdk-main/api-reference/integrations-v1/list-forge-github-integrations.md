---
title: "List Forge GitHub Integrations"
description: "List available Forge GitHub integrations."
source: "https://docs.langchain.com/api-reference/integrations-v1/list-forge-github-integrations"
category: "docs"
tags: [docs, api-reference, integrations-v1, list-forge-github-integrations]
---

# List Forge GitHub Integrations

> List available Forge GitHub integrations.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v1/integrations/forge/github/install**

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
  /v1/integrations/forge/github/install:
    get:
      tags:
        - Integrations (v1)
      summary: List Forge GitHub Integrations
      description: List available Forge GitHub integrations.
      operationId: list_forge_github_integrations_v1_integrations_forge_github_install_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/ForgeGithubIntegration'
                type: array
                title: >-
                  Response List Forge Github Integrations V1 Integrations Forge
                  Github Install Get
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
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

````
