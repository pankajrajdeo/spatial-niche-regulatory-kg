---
title: "List Github Installation Repositories"
description: "List repositories available through a GitHub App installation."
source: "https://docs.langchain.com/api-reference/integrations-v2/list-github-installation-repositories"
category: "docs"
tags: [docs, api-reference, integrations-v2, list-github-installation-repositories]
---

# List Github Installation Repositories

> List repositories available through a GitHub App installation.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/integrations/github/installations/{integration_id}/repositories**

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
  /v2/integrations/github/installations/{integration_id}/repositories:
    get:
      tags:
        - Integrations (v2)
      summary: List Github Installation Repositories
      description: List repositories available through a GitHub App installation.
      operationId: >-
        list_github_installation_repositories_v2_integrations_github_installations__integration_id__repositories_get
      parameters:
        - name: integration_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Integration ID
            description: GitHub integration ID.
          description: GitHub integration ID.
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
                $ref: '#/components/schemas/GithubRepositoriesList'
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
    GithubRepositoriesList:
      properties:
        items:
          items:
            $ref: '#/components/schemas/GithubRepository'
          type: array
          title: Items
          description: GitHub repositories available through the installation.
        next_cursor:
          anyOf:
            - type: string
            - type: 'null'
          title: Next Cursor
          description: Opaque cursor for the next page, if one exists.
      type: object
      required:
        - items
      title: GithubRepositoriesList
      description: A page of GitHub repositories.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    GithubRepository:
      properties:
        host_integration_id:
          type: string
          format: uuid
          title: GitHub Integration ID
          description: >-
            GitHub Integration ID.<br><br>For example, in the `POST
            /v2/deployments` request body, set `integration_id` to the value of
            this field.
        id:
          type: integer
          title: ID
          description: GitHub repository ID.
        name:
          type: string
          title: Name
          description: GitHub repository name.
        owner:
          type: string
          title: Owner
          description: GitHub repository owner.
        url:
          type: string
          title: URL
          description: >-
            GitHub repository URL.<br><br>For example, in the `POST
            /v2/deployments` request body, set `source_config.repo_url` to the
            value of this field.
        default_branch:
          type: string
          title: Default Branch
          description: >-
            GitHub repository default branch.<br><br>For example, in the `POST
            /v2/deployments` request body, set `source_revision_config.repo_ref`
            to the value of this field.
      type: object
      required:
        - host_integration_id
        - id
        - name
        - owner
        - url
        - default_branch
      title: GithubRepository
      description: Metadata for a GitHub repository.
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
