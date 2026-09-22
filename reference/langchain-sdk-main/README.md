# LangChain SDK documentation mirror

This repository is an automatically updated Markdown mirror of the LangChain
documentation set: the [documentation site](https://docs.langchain.com/), the
[generated API reference](https://reference.langchain.com/), and the long-form
writing on [langchain.com](https://www.langchain.com/blog).

The mirror preserves URL hierarchy: a page such as `/oss/python/langchain/agents`
is stored as `langchain/agents.md`, and
`reference.langchain.com/python/langchain/agents/factory/create_agent` is stored
as `reference/python/langchain/agents/factory/create_agent.md`. New categories
and nested pages are discovered and created automatically.

## Included documentation

- Complete `/oss/python` documentation, discovered dynamically
- `/oss/javascript` documentation
- Deep Agents Code documentation from `/oss/deepagents`
- OpenWiki documentation from `/oss/openwiki`
- LangSmith documentation from `/langsmith`
- The `/api-reference` section and every other current or future
  `docs.langchain.com` route, through a final catch-all scope
- Generated Python API reference for `langchain`, `langchain-core`, `langgraph`,
  `langgraph-sdk`, and `deepagents`
- The LangChain blog, resources, and Breakout Agents write-ups

The reference host publishes over 42,000 pages across every language and
community package. Mirroring all of them would take gigabytes, so the scopes
above cover the Python packages this mirror is used to build against. Adding a
`Section` widens the scope.

## How pages are found and converted

Discovery combines each host's sitemap, each host's `llms.txt`, the
`llms-full.txt` aggregate, configured entry points, and recursive links found
inside downloaded content. Arbitrarily deep subdirectories and newly published
categories appear automatically on the next run without waiting for a stale
aggregate index.

Documentation and reference pages expose a dedicated Markdown endpoint, used as
the authoritative source, with `llms-full.txt` retained as a fallback when that
endpoint is briefly unavailable. Blog, resources, and Breakout Agents pages are
server-rendered HTML, converted from their content container to GitHub Flavored
Markdown.

The updater converts Mintlify MDX into GitHub Flavored Markdown. Tabs, code
groups, callouts, cards, accordions, file trees, prompts, interactive embeds,
JSX attributes, and links are normalized so their contents remain readable on
GitHub. Citations between successfully mirrored documents use repository-local
relative `.md` paths, including section fragments. Links to documentation outside
the configured mirror remain on the official website.

Conversion is entirely mechanical. Titles, descriptions, and tags come from each
page's own headings, upstream metadata, and URL. No language model is involved,
so a run is reproducible and costs nothing to execute.

## Navigation

Every page opens with YAML front matter:

```yaml
---
title: "create_agent"
description: "Creates an agent graph that calls tools in a loop until a stopping condition is met."
source: "https://reference.langchain.com/python/langchain/agents/factory/create_agent"
category: "reference"
tags: [reference, langchain, agents, factory, create_agent]
---
```

Blog posts additionally carry `published` and `author`, read from the page's
JSON-LD. No field is derived from the time of the run, so front matter changes
only when the page itself changes.

Every directory carries a generated `_index.md` listing its pages with their
descriptions and its subdirectories with recursive page counts. Start at
[`_index.md`](_index.md) and descend by description instead of grepping the
whole tree.

## Manifest and failure handling

`.mirror-manifest.json` records each source and resolved URL, normalized and
upstream byte sizes and SHA-256 checksums, content source, crawl failures, and
normalization warnings, plus a separate entry per generated index.

A route that a sitemap or index still lists but that upstream answers with 404 or
410 is recorded under `upstream_missing` rather than failing the run. Upstream
publishes stale entries, and treating them as errors would block every run and
freeze stale cleanup indefinitely.

A run exits unsuccessfully if it leaves unclosed code fences, executable MDX,
JSX attributes, malformed relative links, or local links whose mirrored target
file does not exist. Stale files are removed only when they were listed in the
previous managed manifest and the current crawl completed without failures. A
page that failed but was managed by the previous run counts as a failure rather
than a stale link, so a transient upstream error cannot delete a page that
upstream still publishes.

## Update locally

Python 3.10 or newer is required. Run:

```bash
python3 update_docs.py
```

The script uses `tqdm` for progress and `truststore` to honor the operating
system trust store on networks that terminate TLS with a private root. If either
is unavailable and `uv` is installed, the script provisions both automatically.
Otherwise install them first:

```bash
python3 -m pip install tqdm truststore
```

Useful options:

```bash
python3 update_docs.py --workers 12 --timeout 30
python3 update_docs.py --no-clean
```

Run the normalization regression tests with:

```bash
python3 -m unittest discover -s tests
```

## Automatic updates

The `Update LangChain documentation` GitHub Actions workflow runs weekly, on
Monday, and can also be started manually from the Actions tab. When upstream
documentation changes, the workflow commits the refreshed mirror to `main`.

This is an unofficial mirror. LangChain and its documentation belong to their
respective owners.
