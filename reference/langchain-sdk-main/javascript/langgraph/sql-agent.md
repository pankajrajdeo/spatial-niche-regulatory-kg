---
title: "Build a custom SQL agent"
description: "In this tutorial we will build a custom agent that can answer questions about a SQL database using LangGraph."
source: "https://docs.langchain.com/oss/javascript/langgraph/sql-agent"
category: "docs"
tags: [docs, javascript, langgraph, sql-agent]
---

# Build a custom SQL agent

In this tutorial we will build a custom agent that can answer questions about a SQL database using LangGraph.

LangChain offers built-in [agent](../langchain/agents.md) implementations, implemented using [LangGraph](overview.md) primitives. If deeper customization is required, agents can be implemented directly in LangGraph. This guide demonstrates an example implementation of a SQL agent. For a practical introduction, see [building a SQL agent using higher-level LangChain abstractions](../langchain/sql-agent.md).

> [!WARNING]
> Building Q\&A systems of SQL databases requires executing model-generated SQL queries. There are inherent risks in doing this. Make sure that your database connection permissions are always scoped as narrowly as possible for your agent's needs. This will mitigate, though not eliminate, the risks of building a model-driven system.

The [prebuilt agent](../langchain/sql-agent.md) lets us get started quickly, but we relied on the system prompt to constrain its behavior—for example, we instructed the agent to always start with the "list tables" tool, and to always run a query-checker tool before executing the query.

We can enforce a higher degree of control in LangGraph by customizing the agent. Here, we implement a simple ReAct-agent setup, with dedicated nodes for specific tool-calls. We will use the same \[state] as the prebuilt agent.

### Concepts

We will cover the following concepts:

* [Tools](../langchain/tools.md) for reading from SQL databases
* The LangGraph [Graph API](graph-api.md), including state, nodes, edges, and conditional edges.
* [Human-in-the-loop](interrupts.md) processes

## Setup

### Installation

**npm**

```bash
npm i langchain @langchain/core @langchain/langgraph @langchain/openai sqlite3 zod
```

**yarn**

```bash
yarn add langchain @langchain/core @langchain/langgraph @langchain/openai sqlite3 zod
```

**pnpm**

```bash
pnpm add langchain @langchain/core @langchain/langgraph @langchain/openai sqlite3 zod
```

### LangSmith

Set up [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-sql-agent) to inspect what is happening inside your chain or agent. Then set the following environment variables:

```shell
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="..."
```

## 1. Select an LLM

Select a model that supports [tool-calling](../integrations/providers/overview.md):

#### OpenAI
👉 Read the [OpenAI chat model integration docs](../integrations/chat/openai.md)

**npm**

```bash
npm install @langchain/openai
```

**pnpm**

```bash
pnpm install @langchain/openai
```

**yarn**

```bash
yarn add @langchain/openai
```

**bun**

```bash
bun add @langchain/openai
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";

process.env.OPENAI_API_KEY = "your-api-key";

const model = await initChatModel("gpt-5.5");
```

**Model Class**

```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  model: "gpt-5.5",
  apiKey: "your-api-key"
});
```

#### Anthropic
👉 Read the [Anthropic chat model integration docs](../integrations/chat/anthropic.md)

**npm**

```bash
npm install @langchain/anthropic
```

**pnpm**

```bash
pnpm install @langchain/anthropic
```

**yarn**

```bash
yarn add @langchain/anthropic
```

**pnpm**

```bash
pnpm add @langchain/anthropic
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";

process.env.ANTHROPIC_API_KEY = "your-api-key";

const model = await initChatModel("claude-sonnet-4-6");
```

**Model Class**

```typescript
import { ChatAnthropic } from "@langchain/anthropic";

const model = new ChatAnthropic({
  model: "claude-sonnet-4-6",
  apiKey: "your-api-key"
});
```

#### Azure
👉 Read the [Azure chat model integration docs](../integrations/chat/azure.md)

**npm**

```bash
npm install @langchain/azure
```

**pnpm**

```bash
pnpm install @langchain/azure
```

**yarn**

```bash
yarn add @langchain/azure
```

**bun**

```bash
bun add @langchain/azure
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";

process.env.AZURE_OPENAI_API_KEY = "your-api-key";
process.env.AZURE_OPENAI_ENDPOINT = "your-endpoint";
process.env.OPENAI_API_VERSION = "your-api-version";

const model = await initChatModel("azure_openai:gpt-5.5");
```

**Model Class**

```typescript
import { AzureChatOpenAI } from "@langchain/openai";

const model = new AzureChatOpenAI({
  model: "gpt-5.5",
  azureOpenAIApiKey: "your-api-key",
  azureOpenAIApiEndpoint: "your-endpoint",
  azureOpenAIApiVersion: "your-api-version"
});
```

#### Google Gemini
👉 Read the [Google GenAI chat model integration docs](../integrations/chat/google_generative_ai.md)

**npm**

```bash
npm install @langchain/google-genai
```

**pnpm**

```bash
pnpm install @langchain/google-genai
```

**yarn**

```bash
yarn add @langchain/google-genai
```

**bun**

```bash
bun add @langchain/google-genai
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";

process.env.GOOGLE_API_KEY = "your-api-key";

const model = await initChatModel("google-genai:gemini-3.7-flash");
```

**Model Class**

```typescript
import { ChatGoogleGenerativeAI } from "@langchain/google-genai";

const model = new ChatGoogleGenerativeAI({
  model: "gemini-3.7-flash",
  apiKey: "your-api-key"
});
```

#### Bedrock Converse
👉 Read the [AWS Bedrock chat model integration docs](../integrations/chat/bedrock_converse.md)

**npm**

```bash
npm install @langchain/aws
```

**pnpm**

```bash
pnpm install @langchain/aws
```

**yarn**

```bash
yarn add @langchain/aws
```

**bun**

```bash
bun add @langchain/aws
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";

// Follow the steps here to configure your credentials:
// https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

const model = await initChatModel("bedrock:gpt-5.5");
```

**Model Class**

```typescript
import { ChatBedrockConverse } from "@langchain/aws";

// Follow the steps here to configure your credentials:
// https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

const model = new ChatBedrockConverse({
  model: "gpt-5.5",
  region: "us-east-2"
});
```

The output shown in the examples below used OpenAI.

## 2. Configure the database

You will be creating a [SQLite database](https://www.sqlitetutorial.net/sqlite-sample-database/) for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will be loading the `chinook` database, which is a sample database that represents a digital media store.

For convenience, we have hosted the database (`Chinook.db`) on a public GCS bucket.

```ts
import fs from "node:fs/promises";
import path from "node:path";

const url =
  "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db";
const localPath = path.resolve("Chinook.db");

async function resolveDbPath() {
  const exists = await fs
    .access(localPath)
    .then(() => true)
    .catch(() => false);
  if (exists) {
    console.log(`${localPath} already exists, skipping download.`);
    return localPath;
  }
  const resp = await fetch(url);
  if (!resp.ok)
    throw new Error(`Failed to download DB. Status code: ${resp.status}`);
  const buf = Buffer.from(await resp.arrayBuffer());
  await fs.writeFile(localPath, buf);
  console.log(`File downloaded and saved as ${localPath}`);
  return localPath;
}
```

We will use the `sqlite3` library to interact with the database:

```ts
import sqlite3 from "sqlite3";

const dialect = "sqlite";

async function runQuery(query: string, params: unknown[] = []): Promise<any[]> {
  const dbPath = await resolveDbPath();
  const db = new sqlite3.Database(dbPath);
  return new Promise((resolve, reject) => {
    db.all(query, params, (err, rows) => {
      db.close();
      if (err) reject(err);
      else resolve(rows);
    });
  });
}

const tableRows = await runQuery(
  "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';",
);
const tableNames = tableRows.map((row) => String(row.name));
console.log(`Dialect: ${dialect}`);
console.log(`Available tables: ${tableNames.join(", ")}`);
const sampleResults = await runQuery("SELECT * FROM Artist LIMIT 5;");
console.log(`Sample output: ${JSON.stringify(sampleResults)}`);
```

```
Dialect: sqlite
Available tables: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
Sample output: [{"ArtistId":1,"Name":"AC/DC"},{"ArtistId":2,"Name":"Accept"},{"ArtistId":3,"Name":"Aerosmith"},{"ArtistId":4,"Name":"Alanis Morissette"},{"ArtistId":5,"Name":"Alice In Chains"}]
```

## 3. Add tools for database interactions

> [!WARNING]
> The following database tools are minimal wrappers for demonstration purposes only. They are not intended to be secure or used in production. Use narrowly scoped database permissions and add application-specific validation before executing model-generated SQL.

We'll create custom tools to interact with the database:

```ts
import { tool } from "langchain";
import * as z from "zod";

async function getTableNames() {
  const rows = await runQuery(
    "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';",
  );
  return rows.map((row) => String(row.name));
}

function quoteSqliteIdentifier(identifier: string) {
  return `"${identifier.replaceAll('"', '""')}"`;
}

const listTablesTool = tool(
  async () => {
    const tableNames = await getTableNames();
    return tableNames.join(", ");
  },
  {
    name: "sql_db_list_tables",
    description:
      "Input is an empty string, output is a comma-separated list of tables in the database.",
    schema: z.object({}),
  },
);

const getSchemaTool = tool(
  async ({ table_names }) => {
    const validTables = new Set(await getTableNames());
    const results: string[] = [];
    for (const table of table_names.split(",").map((t) => t.trim())) {
      if (!validTables.has(table)) {
        results.push(`Error: table_names {'${table}'} not found in database`);
        continue;
      }
      const schemaRows = await runQuery(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name=?;",
        [table],
      );
      const schema = schemaRows[0]?.sql;
      if (schema) {
        results.push(String(schema));
        try {
          const rows = await runQuery(
            `SELECT * FROM ${quoteSqliteIdentifier(table)} LIMIT 3;`,
          );
          if (rows.length > 0) {
            const colNames = Object.keys(rows[0]);
            results.push(
              `/*\n3 rows from ${table} table:\n${colNames.join("\t")}\n` +
                rows
                  .map((row) =>
                    colNames.map((col) => String(row[col])).join("\t"),
                  )
                  .join("\n") +
                "\n*/",
            );
          }
        } catch (e) {
          results.push(`Error fetching sample rows: ${e}`);
        }
      }
    }
    return results.join("\n\n");
  },
  {
    name: "sql_db_schema",
    description:
      "Input to this tool is a comma-separated list of tables, output is the schema and sample rows for those tables. Be sure that the tables actually exist by calling sql_db_list_tables first! Example Input: table1, table2, table3",
    schema: z.object({
      table_names: z.string().describe("Comma-separated list of table names"),
    }),
  },
);

const queryTool = tool(
  async ({ query }) => {
    try {
      const result = await runQuery(query);
      return JSON.stringify(result);
    } catch (error) {
      return `Error: ${error instanceof Error ? error.message : String(error)}`;
    }
  },
  {
    name: "sql_db_query",
    description:
      "Input to this tool is a detailed and correct SQL query, output is a result from the database. If the query is not correct, an error message will be returned. If an error is returned, rewrite the query, check the query, and try again.",
    schema: z.object({
      query: z.string().describe("SQL query to execute"),
    }),
  },
);

const tools = [listTablesTool, getSchemaTool, queryTool];

for (const toolItem of tools) {
  console.log(`${toolItem.name}: ${toolItem.description}\n`);
}
```

```
sql_db_list_tables: Input is an empty string, output is a comma-separated list of tables in the database.

sql_db_schema: Input to this tool is a comma-separated list of tables, output is the schema and sample rows for those tables. Be sure that the tables actually exist by calling sql_db_list_tables first! Example Input: table1, table2, table3

sql_db_query: Input to this tool is a detailed and correct SQL query, output is a result from the database. If the query is not correct, an error message will be returned. If an error is returned, rewrite the query, check the query, and try again.
```

## 4. Define application steps

We construct dedicated nodes for the following steps:

* Listing DB tables
* Calling the "get schema" tool
* Generating a query
* Checking the query

Putting these steps in dedicated nodes lets us (1) force tool-calls when needed, and (2) customize the prompts associated with each step.

```ts
import {
  AIMessage,
  HumanMessage,
  SystemMessage,
  ToolMessage,
} from "@langchain/core/messages";
import { ToolNode } from "@langchain/langgraph/prebuilt";
import {
  END,
  GraphNode,
  MessagesValue,
  START,
  StateGraph,
  StateSchema,
} from "@langchain/langgraph";

// Create tool nodes for schema and query execution
const getSchemaNode = new ToolNode([getSchemaTool]);
const runQueryNode = new ToolNode([queryTool]);

// Define state schema
const MessagesState = new StateSchema({
  messages: MessagesValue,
});

// Example: create a predetermined tool call
const listTables: GraphNode<typeof MessagesState> = async (state) => {
  const toolCall = {
    name: "sql_db_list_tables",
    args: {},
    id: "abc123",
    type: "tool_call" as const,
  };
  const toolCallMessage = new AIMessage({
    content: "",
    tool_calls: [toolCall],
  });

  const toolMessage = await listTablesTool.invoke({});
  const response = new AIMessage(`Available tables: ${toolMessage}`);

  return {
    messages: [
      toolCallMessage,
      new ToolMessage({ content: toolMessage, tool_call_id: "abc123" }),
      response,
    ],
  };
};

// Example: force a model to create a tool call
const callGetSchema: GraphNode<typeof MessagesState> = async (state) => {
  const llmWithTools = model!.bindTools([getSchemaTool], {
    tool_choice: "any",
  });
  const response = await llmWithTools.invoke(state.messages);

  return { messages: [response] };
};

const topK = 5;

const generateQuerySystemPrompt = `
You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct ${dialect}
query to run, then look at the results of the query and return the answer. Unless
the user specifies a specific number of examples they wish to obtain, always limit
your query to at most ${topK} results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
`;

const generateQuery: GraphNode<typeof MessagesState> = async (state) => {
  const systemMessage = new SystemMessage(generateQuerySystemPrompt);
  // We do not force a tool call here, to allow the model to
  // respond naturally when it obtains the solution.
  const llmWithTools = model!.bindTools([queryTool]);
  const response = await llmWithTools.invoke([
    systemMessage,
    ...state.messages,
  ]);

  return { messages: [response] };
};

const checkQuerySystemPrompt = `
You are a SQL expert with a strong attention to detail.
Double check the ${dialect} query for common mistakes, including:
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Properly quoting identifiers
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

If there are any of the above mistakes, rewrite the query. If there are no mistakes,
just reproduce the original query.

You will call the appropriate tool to execute the query after running this check.
`;

const checkQuery: GraphNode<typeof MessagesState> = async (state) => {
  const systemMessage = new SystemMessage(checkQuerySystemPrompt);

  // Generate an artificial user message to check
  const lastMessage = state.messages[state.messages.length - 1];
  if (!lastMessage.tool_calls || lastMessage.tool_calls.length === 0) {
    throw new Error("No tool calls found in the last message");
  }
  const toolCall = lastMessage.tool_calls[0];
  const userMessage = new HumanMessage(toolCall.args.query);
  const llmWithTools = model!.bindTools([queryTool], {
    tool_choice: "any",
  });
  const response = await llmWithTools.invoke([systemMessage, userMessage]);
  // Preserve the original message ID
  response.id = lastMessage.id;

  return { messages: [response] };
};
```

## 5. Implement the agent

We can now assemble these steps into a workflow using the [Graph API](graph-api.md). We define a [conditional edge](graph-api.md#conditional-edges) at the query generation step that will route to the query checker if a query is generated, or end if there are no tool calls present, such that the LLM has delivered a response to the query.

```ts
import { ConditionalEdgeRouter } from "@langchain/langgraph";

const shouldContinue: ConditionalEdgeRouter<{ InputSchema: typeof MessagesState; Nodes: "check_query" }> = (state) => {
  const messages = state.messages;
  const lastMessage = messages[messages.length - 1];
  if (!lastMessage.tool_calls || lastMessage.tool_calls.length === 0) {
    return END;
  } else {
    return "check_query";
  }
};

const builder = new StateGraph(MessagesState)
  .addNode("list_tables", listTables)
  .addNode("call_get_schema", callGetSchema)
  .addNode("get_schema", getSchemaNode)
  .addNode("generate_query", generateQuery)
  .addNode("check_query", checkQuery)
  .addNode("run_query", runQueryNode)
  .addEdge(START, "list_tables")
  .addEdge("list_tables", "call_get_schema")
  .addEdge("call_get_schema", "get_schema")
  .addEdge("get_schema", "generate_query")
  .addConditionalEdges("generate_query", shouldContinue)
  .addEdge("check_query", "run_query")
  .addEdge("run_query", "generate_query");

const agent = builder.compile();
```

We visualize the application below:

```ts
import * as fs from "node:fs/promises";

const drawableGraph = await agent.getGraphAsync();
const image = await drawableGraph.drawMermaidPng();
const imageBuffer = new Uint8Array(await image.arrayBuffer());

await fs.writeFile("graph.png", imageBuffer);
```

<img src="https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=1ddd4aae369fb8c143edaccb0a09c81f" alt="SQL agent graph" width="308" height="645" data-path="oss/images/sql-agent-langgraph.png" />

We can now invoke the graph:

```ts
const question = "Which genre on average has the longest tracks?";

const stream = await agent.streamEvents(
  { messages: [{ role: "user", content: question }] },
  { version: "v3" },
);

for await (const message of stream.messages) {
  for await (const token of message.text) {
    process.stdout.write(token);
  }
}

const finalState = await stream.output;
```

```
================================ Human Message =================================

Which genre on average has the longest tracks?
================================== Ai Message ==================================

Available tables: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
================================== Ai Message ==================================
Tool Calls:
  sql_db_schema (call_yzje0tj7JK3TEzDx4QnRR3lL)
 Call ID: call_yzje0tj7JK3TEzDx4QnRR3lL
  Args:
    table_names: Genre, Track
================================= Tool Message =================================
Name: sql_db_schema

CREATE TABLE "Genre" (
	"GenreId" INTEGER NOT NULL,
	"Name" NVARCHAR(120),
	PRIMARY KEY ("GenreId")
)

/*
3 rows from Genre table:
GenreId	Name
1	Rock
2	Jazz
3	Metal
*/

CREATE TABLE "Track" (
	"TrackId" INTEGER NOT NULL,
	"Name" NVARCHAR(200) NOT NULL,
	"AlbumId" INTEGER,
	"MediaTypeId" INTEGER NOT NULL,
	"GenreId" INTEGER,
	"Composer" NVARCHAR(220),
	"Milliseconds" INTEGER NOT NULL,
	"Bytes" INTEGER,
	"UnitPrice" NUMERIC(10, 2) NOT NULL,
	PRIMARY KEY ("TrackId"),
	FOREIGN KEY("MediaTypeId") REFERENCES "MediaType" ("MediaTypeId"),
	FOREIGN KEY("GenreId") REFERENCES "Genre" ("GenreId"),
	FOREIGN KEY("AlbumId") REFERENCES "Album" ("AlbumId")
)

/*
3 rows from Track table:
TrackId	Name	AlbumId	MediaTypeId	GenreId	Composer	Milliseconds	Bytes	UnitPrice
1	For Those About To Rock (We Salute You)	1	1	1	Angus Young, Malcolm Young, Brian Johnson	343719	11170334	0.99
2	Balls to the Wall	2	2	1	U. Dirkschneider, W. Hoffmann, H. Frank, P. Baltes, S. Kaufmann, G. Hoffmann	342562	5510424	0.99
3	Fast As a Shark	3	2	1	F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman	230619	3990994	0.99
*/
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_cb9ApLfZLSq7CWg6jd0im90b)
 Call ID: call_cb9ApLfZLSq7CWg6jd0im90b
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgMilliseconds FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY AvgMilliseconds DESC LIMIT 5;
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_DMVALfnQ4kJsuF3Yl6jxbeAU)
 Call ID: call_DMVALfnQ4kJsuF3Yl6jxbeAU
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgMilliseconds FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY AvgMilliseconds DESC LIMIT 5;
================================= Tool Message =================================
Name: sql_db_query

[('Sci Fi & Fantasy', 2911783.0384615385), ('Science Fiction', 2625549.076923077), ('Drama', 2575283.78125), ('TV Shows', 2145041.0215053763), ('Comedy', 1585263.705882353)]
================================== Ai Message ==================================

The genre with the longest tracks on average is "Sci Fi & Fantasy," with an average track length of approximately 2,911,783 milliseconds. Other genres with relatively long tracks include "Science Fiction," "Drama," "TV Shows," and "Comedy."
```

> [!TIP]
> See [LangSmith trace](https://smith.langchain.com/public/a6a96896-686a-4040-b9b5-28d701453d6f/r) for the above run.

## 6. Implement human-in-the-loop review

It can be prudent to check the agent's SQL queries before they are executed for any unintended actions or inefficiencies.

Here we leverage LangGraph's [human-in-the-loop](interrupts.md) features to pause the run before executing a SQL query and wait for human review. Using LangGraph's [persistence layer](persistence.md), we can pause the run indefinitely (or at least as long as the persistence layer is alive).

Let's wrap the `sql_db_query` tool in a node that receives human input. We can implement this using the [interrupt](interrupts.md) function. Below, we allow for input to approve the tool call, edit its arguments, or provide user feedback.

```ts
import { RunnableConfig } from "@langchain/core/runnables";
import { interrupt } from "@langchain/langgraph";

const queryToolWithInterrupt = tool(
  async (input, config: RunnableConfig) => {
    const request = {
      action: queryTool.name,
      args: input,
      description: "Please review the tool call",
    };
    const response = interrupt([request]); // [!code highlight]
    // approve the tool call
    if (response.type === "accept") {
      const toolResponse = await queryTool.invoke(input, config);
      return toolResponse;
    }
    // update tool call args
    else if (response.type === "edit") {
      const editedInput = response.args.args;
      const toolResponse = await queryTool.invoke(editedInput, config);
      return toolResponse;
    }
    // respond to the LLM with user feedback
    else if (response.type === "response") {
      const userFeedback = response.args;
      return userFeedback;
    } else {
      throw new Error(`Unsupported interrupt response type: ${response.type}`);
    }
  },
  {
    name: queryTool.name,
    description: queryTool.description,
    schema: queryTool.schema,
  },
);
```

> [!NOTE]
> The above implementation follows the [tool interrupt example](interrupts.md#interrupts-in-tools) in the broader [human-in-the-loop](interrupts.md) guide. Refer to that guide for details and alternatives.

Let's now re-assemble our graph. We will replace the programmatic check with human review. Note that we now include a [checkpointer](persistence.md); this is required to pause and resume the run.

```ts
import { Command, MemorySaver } from "@langchain/langgraph";

const shouldContinueWithHuman: ConditionalEdgeRouter<{ InputSchema: typeof MessagesState; Nodes: "run_query" }> = (state) => {
  const messages = state.messages;
  const lastMessage = messages[messages.length - 1];
  if (!lastMessage.tool_calls || lastMessage.tool_calls.length === 0) {
    return END;
  } else {
    return "run_query";
  }
};

const builderWithHuman = new StateGraph(MessagesState)
  .addNode("list_tables", listTables)
  .addNode("call_get_schema", callGetSchema)
  .addNode("get_schema", getSchemaNode)
  .addNode("generate_query", generateQuery)
  .addNode("run_query", runQueryNodeWithInterrupt)
  .addEdge(START, "list_tables")
  .addEdge("list_tables", "call_get_schema")
  .addEdge("call_get_schema", "get_schema")
  .addEdge("get_schema", "generate_query")
  .addConditionalEdges("generate_query", shouldContinueWithHuman)
  .addEdge("run_query", "generate_query");

const checkpointer = new MemorySaver(); // [!code highlight]
const agentWithHuman = builderWithHuman.compile({ checkpointer }); // [!code highlight]
```

We can invoke the graph as before. This time, execution is interrupted:

```ts
const hitlQuestion = "Which genre on average has the longest tracks?";

const hitlStream = await agentWithHuman.streamEvents(
  { messages: [{ role: "user", content: hitlQuestion }] },
  { ...config, version: "v3" },
);

for await (const message of hitlStream.messages) {
  for await (const token of message.text) {
    process.stdout.write(token);
  }
}

// Check for interrupts
if (hitlStream.interrupted) {
  console.log("\nINTERRUPTED:");
  console.log(JSON.stringify(hitlStream.interrupts[0], null, 2));
}
```

```
...

INTERRUPTED:
{
  "action": "sql_db_query",
  "args": {
    "query": "SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgLength FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.Name ORDER BY AvgLength DESC LIMIT 5;"
  },
  "description": "Please review the tool call"
}
```

We can accept or edit the tool call using [Command](use-graph-api.md#combine-control-flow-and-state-updates-with-command):

```ts
const resumeStream = await agentWithHuman.streamEvents(
  new Command({ resume: { type: "accept" } }),
  // new Command({ resume: { type: "edit", args: { query: "..." } } }),
  { ...config, version: "v3" },
);

for await (const message of resumeStream.messages) {
  for await (const token of message.text) {
    process.stdout.write(token);
  }
}
```

```
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_t4yXkD6shwdTPuelXEmY3sAY)
 Call ID: call_t4yXkD6shwdTPuelXEmY3sAY
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgLength FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.Name ORDER BY AvgLength DESC LIMIT 5;
================================= Tool Message =================================
Name: sql_db_query

[('Sci Fi & Fantasy', 2911783.0384615385), ('Science Fiction', 2625549.076923077), ('Drama', 2575283.78125), ('TV Shows', 2145041.0215053763), ('Comedy', 1585263.705882353)]
================================== Ai Message ==================================

The genre with the longest average track length is "Sci Fi & Fantasy" with an average length of about 2,911,783 milliseconds. Other genres with long average track lengths include "Science Fiction," "Drama," "TV Shows," and "Comedy."
```

Refer to the [human-in-the-loop guide](interrupts.md) for details.

## Next steps

Check out the [Evaluate a graph](../../langsmith/evaluate-graph.md) guide for evaluating LangGraph applications, including SQL agents like this one, using LangSmith.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/sql-agent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
