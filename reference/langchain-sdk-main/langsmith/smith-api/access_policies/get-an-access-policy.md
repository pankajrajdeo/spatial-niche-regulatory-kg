---
title: "Get an access policy"
description: "Gets a specific access policy by ID."
source: "https://docs.langchain.com/langsmith/smith-api/access_policies/get-an-access-policy"
category: "docs"
tags: [docs, langsmith, smith-api, access_policies, get-an-access-policy]
---

# Get an access policy

> Gets a specific access policy by ID.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json get /api/v1/platform/orgs/current/access-policies/{access_policy_id}**

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
  /api/v1/platform/orgs/current/access-policies/{access_policy_id}:
    get:
      tags:
        - access_policies
      summary: Get an access policy
      description: Gets a specific access policy by ID.
      parameters:
        - description: Access Policy ID
          name: access_policy_id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Access policy details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/authz_internal.AccessPolicy'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '404':
          description: Access policy not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '503':
          description: Service unavailable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
      security:
        - API Key: []
        - Organization ID: []
        - Bearer Auth: []
components:
  schemas:
    authz_internal.AccessPolicy:
      type: object
      properties:
        condition_groups:
          type: array
          items:
            $ref: '#/components/schemas/authz_internal.ConditionGroup'
        created_at:
          type: string
        description:
          type: string
        effect:
          type: string
        id:
          type: string
        name:
          type: string
        role_ids:
          items:
            type: string
          type: array
        updated_at:
          type: string
    shared.ProblemDetails:
      description: RFC 7807 problem details returned on V2 API errors.
      type: object
      properties:
        detail:
          type: string
        details:
          description: >-
            Details is a LangSmith extension carrying structured fields for
            ErrorClass.
          allOf:
            - $ref: '#/components/schemas/shared.ParseErrorDetails'
        error_class:
          description: |-
            ErrorClass is a LangSmith extension sub-categorizing a status code.
            Additional values require expanding this enum and adding a oneOf
            discriminator on Details to keep the class↔details contract typed.
          type: string
          enum:
            - PARSE_FAILURE
        instance:
          type: string
        remedy:
          description: Remedy is a LangSmith extension for user-recoverable errors.
          type: string
        status:
          type: integer
        title:
          type: string
        type:
          type: string
    authz_internal.ConditionGroup:
      type: object
      properties:
        conditions:
          type: array
          items:
            $ref: '#/components/schemas/authz_internal.Condition'
        permission:
          $ref: '#/components/schemas/authz_internal.Permission'
        resource_type:
          type: string
    shared.ParseErrorDetails:
      description: Structured fields describing an adapter parse failure.
      type: object
      required:
        - adapter
        - item_type
      properties:
        adapter:
          type: string
        item_type:
          type: string
        run_id:
          type: string
    authz_internal.Condition:
      type: object
      properties:
        attribute_key:
          type: string
        attribute_name:
          $ref: '#/components/schemas/authz_internal.AbacAttributeName'
        attribute_value:
          type: string
        operator:
          $ref: '#/components/schemas/authz_internal.AbacOperator'
    authz_internal.Permission:
      type: string
      enum:
        - annotation-queues:create
        - annotation-queues:delete
        - annotation-queues:read
        - annotation-queues:update
        - charts:create
        - charts:delete
        - charts:read
        - charts:update
        - custom-apps:create
        - custom-apps:delete
        - custom-apps:download
        - custom-apps:read
        - custom-apps:update
        - datasets:clone
        - datasets:create
        - datasets:delete
        - datasets:download
        - datasets:read
        - datasets:share
        - datasets:tag-on-create
        - datasets:update
        - deployments:create
        - deployments:delete
        - deployments:read
        - deployments:update
        - feedback:create
        - feedback:delete
        - feedback:read
        - feedback:update
        - feedback-configs:create
        - feedback-configs:update
        - feedback-configs:delete
        - experiments:run
        - issues:create
        - issues:delete
        - issues:read
        - issues:update
        - projects:create
        - projects:delete
        - projects:read
        - projects:tag-on-create
        - projects:update
        - projects:increase-trace-tier
        - projects:decrease-trace-tier
        - prompts:create
        - prompts:delete
        - prompts:read
        - prompts:tag-on-create
        - prompts:update
        - prompts:share
        - rules:create
        - rules:delete
        - rules:read
        - rules:update
        - rules:configure-retention
        - runs:create
        - runs:read
        - runs:read-stats
        - runs:share
        - runs:delete
        - model-price-map:create
        - model-price-map:read
        - model-price-map:update
        - model-price-map:delete
        - sandboxes:create
        - sandboxes:delete
        - sandboxes:read
        - sandboxes:tag-on-create
        - sandboxes:update
        - sandboxes:exec
        - snapshots:create
        - snapshots:delete
        - snapshots:update
        - workspaces:manage-members
        - workspaces:manage-secrets
        - workspaces:manage
        - workspaces:manage-model-configs
        - workspaces:manage-keys
        - workspaces:read
        - alerts:create
        - alerts:update
        - alerts:delete
        - alerts:read
        - agent-auth-connections:read
        - agent-auth-connections:create
        - agent-auth-connections:update
        - agent-auth-connections:delete
        - agent-auth-connections:revoke
        - bulk-exports:read
        - bulk-exports:manage
        - mcp-servers:create
        - mcp-servers:delete
        - mcp-servers:invoke
        - mcp-servers:read
        - mcp-servers:update
        - gateway:invoke
        - fleet:read-admin-config
        - fleet:write-admin-config
        - organization:pats:create
        - organization:read
        - organization:read-metadata
        - organization:manage
        - organization:manage-model-configs
        - organization:manage-model-secrets
      x-enum-varnames:
        - AnnotationQueuesCreate
        - AnnotationQueuesDelete
        - AnnotationQueuesRead
        - AnnotationQueuesUpdate
        - ChartsCreate
        - ChartsDelete
        - ChartsRead
        - ChartsUpdate
        - CustomAppsCreate
        - CustomAppsDelete
        - CustomAppsDownload
        - CustomAppsRead
        - CustomAppsUpdate
        - DatasetsClone
        - DatasetsCreate
        - DatasetsDelete
        - DatasetsDownload
        - DatasetsRead
        - DatasetsShare
        - DatasetsTagOnCreate
        - DatasetsUpdate
        - DeploymentsCreate
        - DeploymentsDelete
        - DeploymentsRead
        - DeploymentsUpdate
        - FeedbackCreate
        - FeedbackDelete
        - FeedbackRead
        - FeedbackUpdate
        - FeedbackConfigsCreate
        - FeedbackConfigsUpdate
        - FeedbackConfigsDelete
        - ExperimentsRun
        - IssuesCreate
        - IssuesDelete
        - IssuesRead
        - IssuesUpdate
        - ProjectsCreate
        - ProjectsDelete
        - ProjectsRead
        - ProjectsTagOnCreate
        - ProjectsUpdate
        - ProjectsIncreaseTraceTier
        - ProjectsDecreaseTraceTier
        - PromptsCreate
        - PromptsDelete
        - PromptsRead
        - PromptsTagOnCreate
        - PromptsUpdate
        - PromptsShare
        - RulesCreate
        - RulesDelete
        - RulesRead
        - RulesUpdate
        - RulesConfigureRetention
        - RunsCreate
        - RunsRead
        - RunsReadStats
        - RunsShare
        - RunsDelete
        - ModelPriceMapCreate
        - ModelPriceMapRead
        - ModelPriceMapUpdate
        - ModelPriceMapDelete
        - SandboxesCreate
        - SandboxesDelete
        - SandboxesRead
        - SandboxesTagOnCreate
        - SandboxesUpdate
        - SandboxesExec
        - SnapshotsCreate
        - SnapshotsDelete
        - SnapshotsUpdate
        - WorkspacesManageMembers
        - WorkspacesManageSecrets
        - WorkspacesManage
        - WorkspacesManageModelConfigs
        - WorkspacesManageKeys
        - WorkspacesRead
        - AlertsCreate
        - AlertsUpdate
        - AlertsDelete
        - AlertsRead
        - AgentAuthConnectionsRead
        - AgentAuthConnectionsCreate
        - AgentAuthConnectionsUpdate
        - AgentAuthConnectionsDelete
        - AgentAuthConnectionsRevoke
        - BulkExportsRead
        - BulkExportsManage
        - McpServersCreate
        - McpServersDelete
        - McpServersInvoke
        - McpServersRead
        - McpServersUpdate
        - GatewayInvoke
        - FleetReadAdminConfig
        - FleetWriteAdminConfig
        - OrganizationPATsCreate
        - OrganizationRead
        - OrganizationReadMetadata
        - OrganizationManage
        - OrganizationManageModelConfigs
        - OrganizationManageModelSecrets
    authz_internal.AbacAttributeName:
      type: string
      enum:
        - resource_tag_key
      x-enum-varnames:
        - AbacAttributeNameResourceTagKey
    authz_internal.AbacOperator:
      type: string
      enum:
        - equals
        - not_equals
        - equals_ignore_case
        - not_equals_ignore_case
        - matches
        - not_matches
        - equals_if_exists
        - not_equals_if_exists
        - equals_ignore_case_if_exists
        - not_equals_ignore_case_if_exists
        - matches_if_exists
        - not_matches_if_exists
      x-enum-varnames:
        - AbacOperatorEquals
        - AbacOperatorNotEquals
        - AbacOperatorEqualsIgnoreCase
        - AbacOperatorNotEqualsIgnoreCase
        - AbacOperatorMatches
        - AbacOperatorNotMatches
        - AbacOperatorEqualsIfExists
        - AbacOperatorNotEqualsIfExists
        - AbacOperatorEqualsIgnoreCaseIfExists
        - AbacOperatorNotEqualsIgnoreCaseIfExists
        - AbacOperatorMatchesIfExists
        - AbacOperatorNotMatchesIfExists
  securitySchemes:
    API Key:
      type: apiKey
      in: header
      name: X-API-Key
    Organization ID:
      type: apiKey
      in: header
      name: X-Organization-Id
    Bearer Auth:
      type: http
      description: >-
        Bearer tokens are used to authenticate from the UI. Must also specify
        x-tenant-id or x-organization-id (for org scoped apis).
      scheme: bearer

````
