---
title: "Count Threads"
description: "Get the count of threads matching the specified criteria."
source: "https://docs.langchain.com/langsmith/agent-server-api/threads/count-threads"
category: "docs"
tags: [docs, langsmith, agent-server-api, threads, count-threads]
---

# Count Threads

> Get the count of threads matching the specified criteria.

## OpenAPI

**/langsmith/agent-server-openapi.json post /threads/count**

````yaml
openapi: 3.1.0
info:
  title: LangSmith Deployment
  version: 0.1.0
servers: []
security: []
tags:
  - name: Assistants
    description: An assistant is a configured instance of a graph.
  - name: Threads
    description: A thread contains the accumulated outputs of a group of runs.
  - name: Thread Runs
    description: >-
      A run is an invocation of a graph / assistant on a thread. It updates the
      state of the thread.
  - name: Stateless Runs
    description: >-
      A run is an invocation of a graph / assistant, with no state or memory
      persistence.
  - name: Crons
    description: >-
      A cron is a periodic run that recurs on a given schedule. The repeats can
      be isolated, or share state in a thread
  - name: Store
    description: >-
      Store is an API for managing persistent key-value store (long-term memory)
      that is available from any thread.
  - name: A2A
    description: >-
      Agent-to-Agent Protocol related endpoints for exposing assistants as
      A2A-compliant agents.
  - name: MCP
    description: >-
      Model Context Protocol related endpoints for exposing an agent as an MCP
      server.
  - name: System
    description: System endpoints for health checks, metrics, and server information.
  - name: Streaming
    description: >-
      Thread-centric streaming endpoints. Provides a structured command/event
      surface over SSE+HTTP; WebSocket is also supported at
      `/threads/{thread_id}/stream/events` (not documented here — OpenAPI 3.1
      does not describe WebSocket).
paths:
  /threads/count:
    post:
      tags:
        - Threads
      summary: Count Threads
      description: Get the count of threads matching the specified criteria.
      operationId: count_threads_threads_count_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ThreadCountRequest'
        required: true
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: integer
                title: Count
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    ThreadCountRequest:
      properties:
        metadata:
          type: object
          title: Metadata
          description: Thread metadata to filter on.
        values:
          type: object
          title: Values
          description: State values to filter on.
        status:
          type: string
          enum:
            - idle
            - busy
            - interrupted
            - error
          title: Status
          description: Thread status to filter on.
      type: object
      title: ThreadCountRequest
      description: Payload for counting threads.
    ErrorResponse:
      type: object
      required:
        - detail
      properties:
        detail:
          type: string
          description: Human-readable error message
      title: ErrorResponse
      description: Error response returned from the server

````
