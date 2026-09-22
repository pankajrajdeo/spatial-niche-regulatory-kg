---
title: "Read filter view"
description: "Get a specific filter view."
source: "https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-filter-view"
category: "docs"
tags: [docs, langsmith, smith-api, tracer-sessions, read-filter-view]
---

# Read filter view

> Get a specific filter view.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/views/{view_id}**

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
  /api/v1/sessions/{session_id}/views/{view_id}:
    get:
      tags:
        - tracer-sessions
      summary: Read filter view
      description: Get a specific filter view.
      operationId: read_filter_view_api_v1_sessions__session_id__views__view_id__get
      parameters:
        - name: session_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Session Id
        - name: view_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: View Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FilterView'
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
    FilterView:
      properties:
        filter_string:
          anyOf:
            - type: string
            - type: 'null'
          title: Filter String
        trace_filter_string:
          anyOf:
            - type: string
            - type: 'null'
          title: Trace Filter String
        tree_filter_string:
          anyOf:
            - type: string
            - type: 'null'
          title: Tree Filter String
        thread_filter_string:
          anyOf:
            - type: string
            - type: 'null'
          title: Thread Filter String
        display_name:
          type: string
          title: Display Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        type:
          $ref: '#/components/schemas/FilterViewType'
          default: runs
        syntax_version:
          type: integer
          title: Syntax Version
          default: 1
        start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Start Time
        end_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End Time
        duration:
          anyOf:
            - type: string
            - type: 'null'
          title: Duration
        id:
          type: string
          format: uuid
          title: Id
        session_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Session Id
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - display_name
        - id
        - created_at
        - updated_at
      title: FilterView
    HTTPValidationError:
      properties:
        detail:
          items:
            type: string
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    FilterViewType:
      type: string
      enum:
        - runs
        - threads
        - single_run
      title: FilterViewType
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
