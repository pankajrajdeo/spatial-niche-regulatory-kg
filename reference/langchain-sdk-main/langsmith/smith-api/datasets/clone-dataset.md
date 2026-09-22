---
title: "Clone dataset"
description: "Clone a dataset."
source: "https://docs.langchain.com/langsmith/smith-api/datasets/clone-dataset"
category: "docs"
tags: [docs, langsmith, smith-api, datasets, clone-dataset]
---

# Clone dataset

> Clone a dataset.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/clone**

````yaml
openapi: 3.1.0
info:
  title: LangSmith
  description: >+
    The LangSmith API is used to programmatically create and manage LangSmith
    resources.

    ## Host

    https://api.smith.langchain.com

    ## Authentication

    To authenticate with the LangSmith API, set the `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).

  version: 0.1.0
servers:
  - url: /
security: []
tags:
  - name: run
    x-group: Tracing
  - name: runs
    x-group: Tracing
  - name: sessions
    x-group: Tracing
  - name: tracer-sessions
    x-group: Tracing
  - name: threads
    x-group: Threads
  - name: datasets
    x-group: Datasets
  - name: examples
    x-group: Datasets
  - name: evaluators
    x-group: Evaluation
  - name: experiment-view-overrides
    x-group: Evaluation
  - name: experiments
    x-group: Evaluation
  - name: annotation-queues
    x-group: Feedback & Annotation
  - name: annotation_queues
    x-group: Feedback & Annotation
  - name: feedback
    x-group: Feedback & Annotation
  - name: feedback-configs
    x-group: Feedback & Annotation
  - name: alert_rules
    x-group: Monitoring
  - name: bulk-exports
    x-group: Monitoring
  - name: charts
    x-group: Monitoring
  - name: commits
    x-group: Prompts & Playground
  - name: directories
    x-group: Prompts & Playground
  - name: hub_environments
    x-group: Prompts & Playground
  - name: playground-settings
    x-group: Prompts & Playground
  - name: prompt-webhooks
    x-group: Prompts & Playground
  - name: prompts
    x-group: Prompts & Playground
  - name: tag-transitions
    x-group: Prompts & Playground
  - name: comments
    x-group: Prompt Hub
  - name: likes
    x-group: Prompt Hub
  - name: optimization-jobs
    x-group: Prompt Hub
  - name: ownerships
    x-group: Prompt Hub
  - name: repos
    x-group: Prompt Hub
  - name: settings
    x-group: Prompt Hub
  - name: tags
    x-group: Prompt Hub
  - name: integrations
    x-group: Integrations & Tools
  - name: mcp
    x-group: Integrations & Tools
  - name: mcp_vendors
    x-group: Integrations & Tools
  - name: oauth
    x-group: Integrations & Tools
  - name: tools
    x-group: Integrations & Tools
  - name: gateway-policies
    x-group: LLM Gateway
  - name: sandboxes
    x-group: Sandboxes
  - name: issues
    x-group: Issues
  - name: issues-agent
    x-group: Issues
  - name: Organizations
    x-group: Administration
  - name: SCIM Tokens
    x-group: Administration
  - name: TTL Settings
    x-group: Administration
  - name: access_policies
    x-group: Administration
  - name: api-key
    x-group: Administration
  - name: audit-logs
    x-group: Administration
  - name: auth
    x-group: Administration
  - name: aws_marketplace
    x-group: Administration
  - name: data_planes
    x-group: Administration
  - name: me
    x-group: Administration
  - name: orgs
    x-group: Administration
  - name: service-accounts
    x-group: Administration
  - name: tenant
    x-group: Administration
  - name: ttl-settings
    x-group: Administration
  - name: usage-limits
    x-group: Administration
  - name: workspaces
    x-group: Administration
  - name: ace
    x-group: System
  - name: backfills
    x-group: System
  - name: features
    x-group: System
  - name: info
    x-group: System
  - name: model-price-map
    x-group: System
  - name: public
    x-group: System
  - name: fleet orgs
  - name: fleet secrets
  - name: fleet tenants
  - name: fleet threads
    x-hidden: true
  - name: fleet users
  - name: productfeedback
    x-hidden: true
paths:
  /api/v1/datasets/clone:
    post:
      tags:
        - datasets
      summary: Clone dataset
      description: Clone a dataset.
      operationId: clone_dataset_api_v1_datasets_clone_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_clone_dataset_api_v1_datasets_clone_post
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                items:
                  additionalProperties: true
                  type: object
                type: array
                title: Response Clone Dataset Api V1 Datasets Clone Post
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
    Body_clone_dataset_api_v1_datasets_clone_post:
      properties:
        target_dataset_id:
          type: string
          format: uuid
          title: Target Dataset Id
        source_dataset_id:
          type: string
          format: uuid
          title: Source Dataset Id
        as_of:
          anyOf:
            - anyOf:
                - type: string
                  format: date-time
                - type: string
              description: >-
                Only modifications made on or before this time are included. If
                None, the latest version of the dataset is used.
            - type: 'null'
          title: As Of
        examples:
          items:
            type: string
            format: uuid
          type: array
          title: Examples
          default: []
        split:
          anyOf:
            - type: string
            - items:
                type: string
              type: array
            - type: 'null'
          title: Split
        tag_value_ids:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
              maxItems: 100
            - type: 'null'
          title: Tag Value Ids
      type: object
      required:
        - target_dataset_id
        - source_dataset_id
      title: Body_clone_dataset_api_v1_datasets_clone_post
    HTTPValidationError:
      properties:
        detail:
          items:
            type: string
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
  securitySchemes:
    API Key:
      type: apiKey
      in: header
      name: X-API-Key
    Tenant ID:
      type: apiKey
      in: header
      name: X-Tenant-Id
    Bearer Auth:
      type: http
      description: >-
        Bearer tokens are used to authenticate from the UI. Must also specify
        x-tenant-id or x-organization-id (for org scoped apis).
      scheme: bearer

````
