---
title: "Delete a data plane"
description: "Verifies that the stored customer AWS role has delete permissions, removes linked workspaces, and starts asynchronous deprovisioning for an active or provisioning_failed data plane owned by the..."
source: "https://docs.langchain.com/langsmith/smith-api/data_planes/delete-a-data-plane"
category: "docs"
tags: [docs, langsmith, smith-api, data_planes, delete-a-data-plane]
---

# Delete a data plane

> Verifies that the stored customer AWS role has delete permissions, removes linked workspaces, and starts asynchronous deprovisioning for an active or provisioning_failed data plane owned by the caller's organization. Requires BYOC to be enabled for the org and org admin permissions.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json delete /orgs/current/data-planes/{id}**

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
  /orgs/current/data-planes/{id}:
    delete:
      tags:
        - data_planes
      summary: Delete a data plane
      description: >-
        Verifies that the stored customer AWS role has delete permissions,
        removes linked workspaces, and starts asynchronous deprovisioning for an
        active or provisioning_failed data plane owned by the caller's
        organization. Requires BYOC to be enabled for the org and org admin
        permissions.
      parameters:
        - description: Data plane ID
          name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '202':
          description: Data plane deprovisioning started
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/data_planes.PublicDataPlane'
        '400':
          description: Invalid data plane ID or confirmed missing delete permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/data_planes.ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: string
        '403':
          description: BYOC not enabled or insufficient permissions
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: string
        '404':
          description: Data plane not found
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: string
        '409':
          description: Data plane cannot be deleted from its current status
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: string
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: string
      security:
        - API Key: []
        - Organization ID: []
        - Bearer Auth: []
components:
  schemas:
    data_planes.PublicDataPlane:
      type: object
      properties:
        api_url:
          type: string
        created_at:
          type: string
        firewall:
          $ref: '#/components/schemas/data_planes.DataPlaneFirewallSettings'
        id:
          type: string
        maintenance_window:
          type: string
        name:
          type: string
        region:
          type: string
        status:
          $ref: '#/components/schemas/data_planes.Status'
        status_updated_at:
          type: string
        ttl:
          $ref: '#/components/schemas/data_planes.DataPlaneTTLSettings'
        workspaces:
          type: array
          items:
            $ref: '#/components/schemas/data_planes.PublicDataPlaneWorkspace'
    data_planes.ErrorResponse:
      type: object
      properties:
        code:
          type: string
        error:
          type: string
        missing_permissions:
          type: array
          items:
            $ref: '#/components/schemas/data_planes.MissingPermission'
    data_planes.DataPlaneFirewallSettings:
      type: object
      required:
        - allow_http
        - allowed_cidrs
        - allowed_domains
      properties:
        allow_http:
          type: boolean
        allowed_cidrs:
          type: object
          additionalProperties:
            items:
              type: integer
            type: array
        allowed_domains:
          items:
            type: string
          type: array
    data_planes.Status:
      type: string
      enum:
        - requested
        - provisioning
        - provisioning_failed
        - active
        - updating
        - inactive
        - deprovisioning
        - deleted
        - revoked
      x-enum-varnames:
        - DataPlaneStatusRequested
        - DataPlaneStatusProvisioning
        - DataPlaneStatusProvisioningFailed
        - DataPlaneStatusActive
        - DataPlaneStatusUpdating
        - DataPlaneStatusInactive
        - DataPlaneStatusDeprovisioning
        - DataPlaneStatusDeleted
        - DataPlaneStatusRevoked
    data_planes.DataPlaneTTLSettings:
      type: object
      required:
        - enabled
        - long_days
        - short_days
      properties:
        enabled:
          type: boolean
        long_days:
          type: integer
        short_days:
          type: integer
    data_planes.PublicDataPlaneWorkspace:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
    data_planes.MissingPermission:
      type: object
      properties:
        action:
          type: string
        decision:
          type: string
        resource_arn:
          type: string
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
