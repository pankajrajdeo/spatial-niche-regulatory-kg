import unittest
from unittest.mock import patch

from update_docs import (
    Download,
    MissingPage,
    OUTPUT_ROOT,
    add_fragment_aliases,
    canonical_page_url,
    derive_page_metadata,
    directory_index_documents,
    discover_seed_urls,
    download_one,
    links_from,
    local_path_for,
    markdown_url,
    normalize_markdown,
    render_frontmatter,
    section_for,
    validate_mirror_links,
)


PAGE_URL = "https://docs.langchain.com/oss/python/deepagents/example"


class MarkdownNormalizationTests(unittest.TestCase):
    def normalize(self, text: str) -> str:
        body, warnings = normalize_markdown(text.encode(), PAGE_URL)
        self.assertEqual(warnings, [])
        return body.decode()

    def test_openwiki_paths_use_lowercase_directory(self) -> None:
        path = local_path_for(
            "https://docs.langchain.com/oss/openwiki/automate-updates"
        )
        self.assertEqual(path.parent.name, "openwiki")
        self.assertEqual(path.name, "automate-updates.md")

    @patch("update_docs.request_bytes")
    def test_page_markdown_is_fresher_than_llms_full(self, request) -> None:
        page = "https://docs.langchain.com/langsmith/example"
        request.return_value = (
            b"# Current\n\n## Example agent\n",
            f"{page}.md",
            "text/markdown",
        )
        result = download_one(page, 30, {page: b"# Older aggregate\n"})
        self.assertEqual(result.raw_body, b"# Current\n\n## Example agent\n")
        self.assertEqual(result.content_source, "page-markdown")
        request.assert_called_once_with(f"{page}.md", 30)

    @patch("update_docs.request_bytes", side_effect=RuntimeError("temporary failure"))
    def test_llms_full_is_only_a_download_fallback(self, request) -> None:
        page = "https://docs.langchain.com/langsmith/example"
        result = download_one(page, 30, {page: b"# Aggregate fallback\n"})
        self.assertEqual(result.raw_body, b"# Aggregate fallback\n")
        self.assertEqual(result.content_source, "llms-full.txt-fallback")
        request.assert_called_once_with(f"{page}.md", 30)

    def test_nested_tabs_and_code_groups_become_gfm(self) -> None:
        output = self.normalize(
            '''# Setup
<Tabs>
  <Tab title="pip">
    <CodeGroup>
      ```bash theme={"dark":"example"}
      pip install deepagents
      ```
    </CodeGroup>
  </Tab>
</Tabs>
'''
        )
        self.assertIn("#### pip\n```bash\npip install deepagents\n```", output)
        self.assertNotIn("<Tabs>", output)
        self.assertNotIn("theme=", output)

    def test_generated_embed_source_is_removed_but_invocation_is_preserved(self) -> None:
        output = self.normalize(
            '''# Demo
export const PatternEmbed = ({pattern}) => { return <div>{pattern}</div>; }
<PatternEmbed pattern="sandbox" />
'''
        )
        self.assertNotIn("export const", output)
        self.assertIn("Interactive example", output)
        self.assertIn(PAGE_URL, output)

    def test_generated_undefined_placeholders_are_removed(self) -> None:
        output = self.normalize(
            "# Changelog\n\n"
            "export const sandbox_slug_0 = undefined\n\n"
            "export const snapshot_id_0 = undefined;\n\n"
            'export const prefix_0 = "api.smith"\n\n'
            "export const protocol_0 = false\n\n"
            "Weekly updates.\n"
        )
        self.assertEqual(output, "# Changelog\n\nWeekly updates.\n")

    @patch("update_docs.request_bytes")
    def test_new_python_project_is_discovered_and_mapped_dynamically(self, request) -> None:
        project = "https://docs.langchain.com/oss/python/future-project"
        page = f"{project}/guides/get-started"

        def response(url, timeout):
            self.assertEqual(timeout, 30)
            if url.endswith("/sitemap.xml"):
                return (
                    f"<urlset><url><loc>{page}</loc></url></urlset>".encode(),
                    url,
                    "application/xml",
                )
            if url.endswith("/llms.txt"):
                return f"- [Future project]({project})\n".encode(), url, "text/plain"
            if url.endswith("/llms-full.txt"):
                return b"", url, "text/plain"
            self.fail(f"unexpected discovery URL: {url}")

        request.side_effect = response
        seeds, full_pages, errors = discover_seed_urls(30)

        self.assertEqual(errors, [])
        self.assertEqual(full_pages, {})
        self.assertIn(project, seeds)
        self.assertIn(page, seeds)
        self.assertEqual(canonical_page_url(page), page)
        self.assertEqual(
            local_path_for(page).relative_to(OUTPUT_ROOT).as_posix(),
            "future-project/guides/get-started.md",
        )

    def test_mirrored_links_and_fragments_become_repository_relative(self) -> None:
        mirrored = {
            PAGE_URL,
            "https://docs.langchain.com/oss/python/deepagents/overview",
            "https://docs.langchain.com/oss/python/langchain",
        }
        body, warnings = normalize_markdown(
            b"[section](#setup) [sibling](overview) [root](/oss/python/langchain)\n",
            PAGE_URL,
            mirrored,
        )
        self.assertEqual(warnings, [])
        output = body.decode()
        self.assertIn("[section](#setup)", output)
        self.assertIn("[sibling](overview.md)", output)
        self.assertIn("[root](../langchain/index.md)", output)

    def test_unmirrored_document_link_stays_on_official_site(self) -> None:
        output = self.normalize("[JavaScript docs](/oss/javascript/langchain/overview)\n")
        self.assertIn(
            "https://docs.langchain.com/oss/javascript/langchain/overview",
            output,
        )

    def test_code_that_looks_like_markdown_link_is_not_rewritten(self) -> None:
        output = self.normalize(
            "```javascript\n"
            "const response = toolNameMap[functionName](functionArguments);\n"
            "```\n"
        )
        self.assertIn("toolNameMap[functionName](functionArguments)", output)
        self.assertNotIn("docs.langchain.com/langsmith/functionArguments", output)

    def test_code_that_looks_like_markdown_link_is_not_discovered(self) -> None:
        download = Download(
            page_url="https://docs.langchain.com/langsmith/example",
            raw_body=(
                b"```javascript\n"
                b"toolNameMap[functionName](functionArguments);\n"
                b"```\n"
                b"[Real page](/langsmith/observability)\n"
            ),
        )
        self.assertEqual(
            links_from(download),
            {"https://docs.langchain.com/langsmith/observability"},
        )

    def test_missing_mintlify_fragment_gets_local_anchor_alias(self) -> None:
        source = "https://docs.langchain.com/oss/python/deepagents/example"
        target = "https://docs.langchain.com/oss/python/deepagents/overview"
        completed = {
            source: Download(
                page_url=source,
                body=b"# Example\n[Concepts](overview.md#configuration-file-concepts)\n",
            ),
            target: Download(
                page_url=target,
                body=b"# Overview\n\n## Configuration file\n",
            ),
        }
        self.assertEqual(add_fragment_aliases(completed), 1)
        self.assertIn(
            b'<a id="configuration-file-concepts"></a>',
            completed[target].body,
        )

    def test_encoded_ampersand_fragment_alias_validates(self) -> None:
        source = "https://docs.langchain.com/oss/python/deepagents/example"
        target = "https://docs.langchain.com/oss/python/deepagents/overview"
        completed = {
            source: Download(
                page_url=source,
                body=b"# Example\n[Projects](overview.md#projects-%26-datasets)\n",
            ),
            target: Download(
                page_url=target,
                body=b"# Overview\n\n## Projects & datasets\n",
            ),
        }
        self.assertEqual(add_fragment_aliases(completed), 1)
        self.assertIn(b'<a id="projects-&amp;-datasets"></a>', completed[target].body)
        self.assertEqual(validate_mirror_links(completed), {})

    def test_root_namespace_without_leading_slash_does_not_nest(self) -> None:
        output = self.normalize("[Gateway](langsmith/llm-gateway)\n")
        self.assertIn("https://docs.langchain.com/langsmith/llm-gateway", output)
        self.assertNotIn("/oss/python/deepagents/langsmith/", output)

    def test_html_heading_and_missing_iframe_source_become_native_markdown(self) -> None:
        output = self.normalize(
            '<h2 className="styled">Setup</h2>\n<iframe title="Demo" />\n'
        )
        self.assertIn("## Setup", output)
        self.assertIn(
            f"> **Embedded Content:** Demo — [Open it in the original LangChain documentation]({PAGE_URL}).",
            output,
        )
        self.assertNotIn("<iframe", output)

    def test_file_tree_and_prompt_remain_semantic(self) -> None:
        output = self.normalize(
            '''<Tree>
  <Tree.Folder name="skills">
    <Tree.File name="SKILL.md" />
  </Tree.Folder>
</Tree>
<Prompt description="Turn this fix into a skill.">
Use the current conversation.
</Prompt>
'''
        )
        self.assertIn('- 📁 `skills/`\n  - 📄 `SKILL.md`', output)
        self.assertIn("> **Prompt:** Turn this fix into a skill.", output)
        self.assertIn("Use the current conversation.", output)

    def test_jsx_logo_card_becomes_single_markdown_link(self) -> None:
        output = self.normalize(
            '''<a href="/langsmith/trace-openai" className="grid-item">
  <img className="light" src="/light.svg" alt="" />
  <img className="dark" src="/dark.svg" alt="" />
  <span className="font-semibold">OpenAI</span>
</a>
'''
        )
        self.assertEqual(
            output,
            "- [OpenAI](https://docs.langchain.com/langsmith/trace-openai)\n",
        )

    def test_adjacent_logo_cards_remain_separate_list_items(self) -> None:
        output = self.normalize(
            '''<a href="/one">
  <img src="/one.svg" alt="" />
  <span>One</span>
</a>

<a href="/two">
  <img src="/two.svg" alt="" />
  <span>Two</span>
</a>
'''
        )
        self.assertIn(
            "- [One](https://docs.langchain.com/one)\n\n"
            "- [Two](https://docs.langchain.com/two)",
            output,
        )


class MultiHostRoutingTests(unittest.TestCase):
    def test_reference_packages_keep_separate_directories(self) -> None:
        for package in ("langchain", "langgraph"):
            url = f"https://reference.langchain.com/python/{package}/agents/factory"
            path = local_path_for(url).relative_to(OUTPUT_ROOT).as_posix()
            self.assertEqual(path, f"reference/python/{package}/agents/factory.md")

    def test_reference_pages_use_the_markdown_endpoint(self) -> None:
        url = "https://reference.langchain.com/python/langchain/agents"
        self.assertEqual(section_for(url).kind, "mdx")
        self.assertEqual(markdown_url(url), f"{url}.md")

    def test_blog_pages_are_fetched_as_rendered_html(self) -> None:
        url = "https://www.langchain.com/blog/how-to"
        self.assertEqual(section_for(url).kind, "html")
        self.assertEqual(markdown_url(url), url)
        self.assertEqual(
            local_path_for(url).relative_to(OUTPUT_ROOT).as_posix(), "blog/how-to.md"
        )

    def test_unmirrored_hosts_are_rejected(self) -> None:
        self.assertIsNone(canonical_page_url("https://example.com/oss/python/langchain"))

    def test_dot_segments_resolve_to_a_real_route(self) -> None:
        self.assertEqual(
            canonical_page_url("https://docs.langchain.com/."),
            "https://docs.langchain.com/",
        )
        self.assertEqual(
            local_path_for("https://docs.langchain.com/.").name, "home.md"
        )

    def test_traversal_above_the_host_root_is_rejected(self) -> None:
        self.assertIsNone(canonical_page_url("https://docs.langchain.com/../../etc/passwd"))

    def test_a_page_named_like_an_index_does_not_shadow_one(self) -> None:
        path = local_path_for("https://docs.langchain.com/oss/python/langchain/_index")
        self.assertEqual(path.name, "_index-page.md")

    def test_a_host_root_keeps_its_hostname_intact(self) -> None:
        self.assertEqual(
            markdown_url("https://docs.langchain.com/"),
            "https://docs.langchain.com/index.md",
        )

    def test_a_url_in_a_code_span_excludes_the_closing_backtick(self) -> None:
        body = "Call `https://reference.langchain.com/python/langchain/agents.md` first."
        self.assertEqual(
            links_from(Download(page_url=PAGE_URL, body=body.encode())),
            {"https://reference.langchain.com/python/langchain/agents"},
        )

    def test_a_typed_fence_in_rich_text_stays_literal(self) -> None:
        html = (
            '<div class="w-richtext"><p>```<br/>llm = EdenAI()</p>'
            "<p>" + "Prose that follows the code sample. " * 4 + "</p></div>"
        )
        body, warnings = normalize_markdown(
            html.encode(), "https://www.langchain.com/blog/eden-ai"
        )
        self.assertEqual(warnings, [])
        self.assertIn("\\`\\`\\`", body.decode())

    def test_prose_quoting_javascript_is_not_a_conversion_leftover(self) -> None:
        html = (
            '<div class="w-richtext"><p>export const judge = new Prompt({</p>'
            "<p>" + "Prose explaining the evaluator above. " * 4 + "</p></div>"
        )
        _, warnings = normalize_markdown(
            html.encode(), "https://www.langchain.com/blog/customers"
        )
        self.assertEqual(warnings, [])

    def test_a_gated_landing_page_is_not_mirrored(self) -> None:
        html = '<main><h1>State of AI</h1><a href="/x">Share</a></main>'
        body, warnings = normalize_markdown(
            html.encode(), "https://www.langchain.com/resources/state-of-ai"
        )
        self.assertEqual(body, b"")
        self.assertEqual(warnings, ["page has no article content"])

    @patch("update_docs.request_bytes")
    def test_a_route_upstream_no_longer_serves_is_not_a_failure(self, request) -> None:
        page = "https://reference.langchain.com/python/deepagents/removed"
        request.side_effect = MissingPage("HTTP 404")
        result = download_one(page, 30, {})
        self.assertEqual(result.missing, "HTTP 404")
        self.assertIsNone(result.error)


class FrontMatterTests(unittest.TestCase):
    def metadata(self, body: str, url: str = PAGE_URL, **upstream: str) -> dict:
        return derive_page_metadata(body, url, upstream)

    def test_title_and_description_come_from_the_page(self) -> None:
        metadata = self.metadata("# Agents\n\nAn agent calls tools in a loop.\n")
        self.assertEqual(metadata["title"], "Agents")
        self.assertEqual(metadata["description"], "An agent calls tools in a loop.")

    def test_snake_case_identifiers_survive_the_title(self) -> None:
        self.assertEqual(self.metadata("# `create_agent`\n")["title"], "create_agent")

    def test_reference_boilerplate_is_not_a_description(self) -> None:
        metadata = self.metadata(
            "# create_agent\n\n> **Function** in `langchain`\n\n"
            "\U0001F4D6 [View in docs](https://reference.langchain.com/x)\n\n"
            "Creates an agent graph.\n"
        )
        self.assertEqual(metadata["description"], "Creates an agent graph.")

    def test_code_blocks_are_not_a_description(self) -> None:
        metadata = self.metadata("# Install\n\n```bash\npip install langchain\n```\n\nThen import it.\n")
        self.assertEqual(metadata["description"], "Then import it.")

    def test_upstream_metadata_wins_and_carries_blog_fields(self) -> None:
        metadata = self.metadata(
            "# Post\n\nBody text.\n",
            "https://www.langchain.com/blog/post",
            description="Upstream summary.",
            published="2025-04-20T17:32:47.000Z",
            author="LangChain",
        )
        self.assertEqual(metadata["description"], "Upstream summary.")
        self.assertEqual(metadata["category"], "blog")
        rendered = render_frontmatter(metadata).decode()
        self.assertIn('published: "2025-04-20T17:32:47.000Z"', rendered)
        self.assertIn('author: "LangChain"', rendered)

    def test_tags_describe_the_url_and_omit_routing_noise(self) -> None:
        metadata = self.metadata(
            "# Agents\n", "https://docs.langchain.com/oss/python/langchain/agents"
        )
        self.assertEqual(metadata["tags"], ["docs", "langchain", "agents"])

    def test_quotes_are_escaped_in_rendered_front_matter(self) -> None:
        rendered = render_frontmatter({"title": 'A "quoted" name'}).decode()
        self.assertIn('title: "A \\"quoted\\" name"', rendered)

    def test_front_matter_carries_no_run_timestamp(self) -> None:
        body = "# Agents\n\nAn agent calls tools in a loop.\n"
        self.assertEqual(
            render_frontmatter(self.metadata(body)),
            render_frontmatter(self.metadata(body)),
        )


class DirectoryIndexTests(unittest.TestCase):
    def documents(self) -> dict:
        return directory_index_documents(
            {
                "langchain/agents.md": {"title": "Agents", "description": "Tool loop."},
                "reference/python/langchain/create_agent.md": {
                    "title": "create_agent",
                    "description": "Creates an agent graph.",
                },
            }
        )

    def test_every_ancestor_directory_gets_an_index(self) -> None:
        self.assertEqual(
            sorted(self.documents()),
            [
                "_index.md",
                "langchain/_index.md",
                "reference/_index.md",
                "reference/python/_index.md",
                "reference/python/langchain/_index.md",
            ],
        )

    def test_files_are_listed_with_titles_and_descriptions(self) -> None:
        self.assertIn(
            "- [Agents](agents.md) - Tool loop.",
            self.documents()["langchain/_index.md"].decode(),
        )

    def test_directories_report_their_whole_subtree(self) -> None:
        self.assertIn(
            "- [python/](python/_index.md) - 1 page",
            self.documents()["reference/_index.md"].decode(),
        )


if __name__ == "__main__":
    unittest.main()
