#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["tqdm>=4.66,<5", "truststore>=0.10"]
# ///
"""Mirror LangChain documentation, blog posts, and API reference as Markdown.

Discovery uses each host's sitemap, llms.txt, llms-full.txt, configured entry
points, and links found in downloaded content. Mintlify MDX and server-rendered
HTML are both normalized to GitHub Flavored Markdown, every page receives
derived YAML front matter, and each directory receives a generated _index.md so
an agent can navigate by description instead of grepping the whole tree. Files
are written atomically, and only files recorded in the previous managed manifest
are eligible for stale-file cleanup.

Normalization is entirely mechanical: titles, descriptions, and tags come from
each page's own headings, upstream metadata, and URL. No language model is used.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import difflib
import hashlib
import html
import json
import os
import re
import shutil
import sys
import time
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Iterable
from http.client import HTTPException
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

try:
    from tqdm import tqdm
except ImportError:  # pragma: no cover - depends on the local environment
    tqdm = None  # type: ignore[assignment]

try:
    # Corporate networks terminate TLS with a private root that ships in the OS
    # trust store but not in the interpreter's bundled one.
    import truststore

    truststore.inject_into_ssl()
except ImportError:  # pragma: no cover - depends on the local environment
    pass


DOCS_HOST = "docs.langchain.com"
SITE_HOST = "www.langchain.com"
REFERENCE_HOST = "reference.langchain.com"
ORIGIN = f"https://{DOCS_HOST}"
SITE_ORIGIN = f"https://{SITE_HOST}"
REFERENCE_ORIGIN = f"https://{REFERENCE_HOST}"
SITEMAP_URL = f"{ORIGIN}/sitemap.xml"
LLMS_URL = f"{ORIGIN}/llms.txt"
LLMS_FULL_URL = f"{ORIGIN}/llms-full.txt"
SITEMAPS = (SITEMAP_URL, f"{SITE_ORIGIN}/sitemap.xml", f"{REFERENCE_ORIGIN}/sitemap.xml")
# Each host publishes its own plain-text index of every page it considers
# canonical, which surfaces pages the sitemap omits.
LLMS_INDEXES = (LLMS_URL, f"{REFERENCE_ORIGIN}/llms.txt")
OUTPUT_ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = OUTPUT_ROOT / ".mirror-manifest.json"
USER_AGENT = "langchain-docs-markdown-mirror/1.0"
INDEX_NAME = "_index.md"


@dataclass(frozen=True)
class Section:
    folder: str
    prefix: str
    entry_url: str | None
    local_subfolder: str = ""
    root_relative: str = "index"
    host: str = DOCS_HOST
    # "mdx" pages expose a dedicated .md endpoint; "html" pages are
    # server-rendered pages that must be converted from markup.
    kind: str = "mdx"
    # Element that holds an HTML page's body, as (tag, required class). Each
    # site nests content differently, and guessing by size picks up navigation
    # chrome on one layout and a single parameter block on another.
    content_selector: tuple[str, str | None] | None = None


SECTIONS = (
    Section(
        "deepagents",
        "/oss/deepagents",
        f"{ORIGIN}/oss/deepagents/",
        root_relative="code/index",
    ),
    Section("deepagents", "/oss/python/deepagents", f"{ORIGIN}/oss/python/deepagents/"),
    Section("langchain", "/oss/python/langchain", f"{ORIGIN}/oss/python/langchain/"),
    Section("langgraph", "/oss/python/langgraph", f"{ORIGIN}/oss/python/langgraph/"),
    Section("openwiki", "/oss/openwiki", f"{ORIGIN}/oss/openwiki/"),
    Section("integrations", "/oss/python/integrations", f"{ORIGIN}/oss/python/integrations/"),
    Section("langsmith", "/langsmith", f"{ORIGIN}/langsmith/"),
    # This user-requested route does not exist as of the latest run. Keeping
    # it as a discovery scope means sitemap/llms pages will mirror if LangChain
    # publishes the section later, without making today's run fail on its 404.
    Section("langsmith", "/oss/python/langsmith", None, local_subfolder="oss-python"),
    # Catch-all for the complete Python documentation namespace. Keep this
    # after the explicit scopes so their established destination paths win;
    # every other current or future /oss/python/<category>/... URL is mapped
    # directly to <category>/... beneath OUTPUT_ROOT.
    Section("", "/oss/python", f"{ORIGIN}/oss/python/"),
    Section("javascript", "/oss/javascript", f"{ORIGIN}/oss/javascript/"),
    Section("api-reference", "/api-reference", f"{ORIGIN}/api-reference/"),
    # Final docs catch-all. Any remaining current or future docs.langchain.com
    # route mirrors to its own URL path, so a new top-level documentation
    # section needs no code change. Keep it last so every explicit scope wins.
    Section("", "", f"{ORIGIN}/", root_relative="home"),
    # Long-form writing on the marketing host. These pages carry the design
    # rationale and postmortems that never reach the reference documentation.
    Section(
        "blog", "/blog", f"{SITE_ORIGIN}/blog", host=SITE_HOST,
        kind="html", content_selector=("div", "w-richtext"),
    ),
    Section(
        "resources", "/resources", f"{SITE_ORIGIN}/resources",
        host=SITE_HOST, kind="html",
        content_selector=("div", "w-richtext"),
    ),
    Section(
        "breakoutagents", "/breakoutagents", f"{SITE_ORIGIN}/breakoutagents",
        host=SITE_HOST, kind="html",
        content_selector=("div", "w-richtext"),
    ),
    # Generated Python API reference. Every reference page is available as
    # Markdown by appending .md, so these scopes need no HTML conversion. The
    # host publishes 42k pages across every language and community package;
    # mirroring all of them would take gigabytes and hours, so these are the
    # Python packages this repository is used to build against. Add a Section
    # to widen the scope.
    Section(
        "reference", "/python/langchain", f"{REFERENCE_ORIGIN}/python/langchain",
        host=REFERENCE_HOST, local_subfolder="python/langchain",
    ),
    Section(
        "reference", "/python/langchain-core", f"{REFERENCE_ORIGIN}/python/langchain-core",
        host=REFERENCE_HOST, local_subfolder="python/langchain-core",
    ),
    Section(
        "reference", "/python/langgraph", f"{REFERENCE_ORIGIN}/python/langgraph",
        host=REFERENCE_HOST, local_subfolder="python/langgraph",
    ),
    Section(
        "reference", "/python/langgraph-sdk", f"{REFERENCE_ORIGIN}/python/langgraph-sdk",
        host=REFERENCE_HOST, local_subfolder="python/langgraph-sdk",
    ),
    Section(
        "reference", "/python/deepagents", f"{REFERENCE_ORIGIN}/python/deepagents",
        host=REFERENCE_HOST, local_subfolder="python/deepagents",
    ),
)

ALLOWED_HOSTS = frozenset(section.host for section in SECTIONS)

URL_RE = re.compile(
    r"https://(?:%s)/[^\s<>\]\[()\"'`\\]+"
    % "|".join(re.escape(host) for host in sorted(ALLOWED_HOSTS))
)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^)]*[\"'])?\)")
HTML_LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
LLMS_FULL_PAGE_RE = re.compile(
    r"(?m)^# [^\n]+\nSource: (https://docs\.langchain\.com/\S+)\s*$"
)
GENERATED_COMPONENT_RE = re.compile(
    r"(?m)^export const (PatternEmbed|ExampleEmbed)\s*=.*$"
)
SIMPLE_EXPORT_RE = re.compile(
    # Mintlify emits page-local placeholders for interactive examples. They
    # carry no documentation content and cannot execute in rendered Markdown.
    r"(?m)^export const (?:"
    r"(?:protocol|prefix|suffix)_\d+\s*=.*"
    r"|[A-Za-z_$][\w$]*\s*=\s*undefined\s*;?\s*"
    r")\n?"
)
DOC_INDEX_RE = re.compile(
    r"\A> ## Documentation Index\n"
    r"> Fetch the complete documentation index at: https://docs\.langchain\.com/llms\.txt\n"
    r"> Use this file to discover all available pages before exploring further\.\n*"
)
SKIP_SUFFIXES = {
    ".7z", ".avif", ".bmp", ".css", ".csv", ".doc", ".docx", ".gif",
    ".gz", ".ico", ".jpeg", ".jpg", ".js", ".json", ".map", ".mov",
    ".mp3", ".mp4", ".pdf", ".png", ".py", ".svg", ".tar", ".toml",
    ".ts", ".tsx", ".txt", ".wav", ".webm", ".webp", ".xml", ".yaml",
    ".yml", ".zip",
}


@dataclass
class Download:
    page_url: str
    final_url: str | None = None
    raw_body: bytes | None = None
    body: bytes | None = None
    content_source: str = "page-markdown"
    metadata: dict[str, object] | None = None
    normalization_warnings: list[str] | None = None
    error: str | None = None
    skipped: str | None = None
    missing: str | None = None


class MissingPage(RuntimeError):
    """Upstream answers that a discovered route does not exist."""


class ExternalRedirect(RuntimeError):
    def __init__(self, url: str):
        super().__init__(url)
        self.url = url


class DocsRedirectHandler(HTTPRedirectHandler):
    """Follow redirects within the mirrored hosts but stop before other sites."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        absolute = urljoin(req.full_url, newurl)
        if urlsplit(absolute).netloc.lower() not in ALLOWED_HOSTS:
            raise ExternalRedirect(absolute)
        return super().redirect_request(req, fp, code, msg, headers, absolute)


OPENER = build_opener(DocsRedirectHandler())


def request_bytes(url: str, timeout: float, retries: int = 3) -> tuple[bytes, str, str]:
    """Return response body, final URL, and content type with bounded retries."""
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/markdown,text/plain,*/*"})
            with OPENER.open(req, timeout=timeout) as response:
                return response.read(), response.geturl(), response.headers.get_content_type()
        except (HTTPError, URLError, TimeoutError, OSError, HTTPException) as exc:
            last_error = exc
            if isinstance(exc, HTTPError) and exc.code in {404, 410}:
                raise MissingPage(f"HTTP {exc.code}") from exc
            if isinstance(exc, HTTPError) and exc.code in {400, 401, 403}:
                break
            if attempt + 1 < retries:
                time.sleep(0.5 * (2**attempt))
    raise RuntimeError(str(last_error) if last_error else f"Unable to fetch {url}")


def matching_section(host: str, path: str) -> Section | None:
    """Return the first configured scope that owns a host and path."""
    for section in SECTIONS:
        if section.host != host:
            continue
        if path == section.prefix or path.startswith(section.prefix + "/"):
            return section
    return None


def canonical_page_url(raw_url: str, base_url: str = ORIGIN) -> str | None:
    """Normalize a URL and return it only when it belongs to a configured scope."""
    raw_url = raw_url.strip().strip("<>")
    if not raw_url or raw_url.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    absolute = urljoin(base_url, raw_url)
    parts = urlsplit(absolute)
    host = parts.netloc.lower()
    if parts.scheme not in {"http", "https"} or host not in ALLOWED_HOSTS:
        return None
    path = unquote(parts.path)
    if path.endswith(".md"):
        path = path[:-3]
    # Resolve the dot segments a relative link can leave behind, so "/." and
    # "/oss/python/../langsmith" reduce to real routes instead of empty ones.
    segments: list[str] = []
    for segment in path.split("/"):
        if segment in {"", "."}:
            continue
        if segment == "..":
            if not segments:
                return None
            segments.pop()
            continue
        segments.append(segment)
    path = "/" + "/".join(segments)
    if Path(path).suffix.lower() in SKIP_SUFFIXES:
        return None
    # Template expressions and punctuation copied from code samples are not
    # documentation routes, even when a Markdown parser sees them as links.
    if any(character in path for character in '{}*"<>') or path.count("(") != path.count(")"):
        return None
    if matching_section(host, path) is None:
        return None
    return urlunsplit(("https", host, path, "", ""))


def section_for(page_url: str) -> Section:
    parts = urlsplit(page_url)
    section = matching_section(parts.netloc.lower(), parts.path)
    if section is None:
        raise ValueError(f"URL is outside configured sections: {page_url}")
    return section


def local_path_for(page_url: str) -> Path:
    section = section_for(page_url)
    path = urlsplit(page_url).path
    relative = path[len(section.prefix):].strip("/")
    if not relative or relative == ".":
        relative = section.root_relative
    safe_parts = []
    for part in PurePosixPath(relative).parts:
        if part in {"", ".", ".."}:
            raise ValueError(f"Unsafe page path: {page_url}")
        safe_parts.append(part)
    # Generated directory indexes own this name, so an upstream page that would
    # land on it is given a suffix instead of silently overwriting the index.
    if safe_parts[-1] == INDEX_NAME.removesuffix(".md"):
        safe_parts[-1] += "-page"
    target = OUTPUT_ROOT / section.folder
    if section.local_subfolder:
        target /= section.local_subfolder
    target /= Path(*safe_parts)
    return target.with_name(target.name + ".md")


def markdown_url(page_url: str) -> str:
    """Return the upstream address that serves a page's authoritative content."""
    if section_for(page_url).kind == "html":
        return page_url
    parts = urlsplit(page_url)
    # Trimming a trailing slash off a bare host would append ".md" to the
    # hostname itself; a host root serves its Markdown at /index.md.
    path = parts.path.rstrip("/") or "/index"
    return urlunsplit((parts.scheme, parts.netloc, f"{path}.md", "", ""))


def parse_llms_full(body: bytes) -> dict[str, bytes]:
    """Split llms-full.txt into canonical per-page Markdown documents."""
    text = body.decode("utf-8", errors="replace")
    matches = list(LLMS_FULL_PAGE_RE.finditer(text))
    pages: dict[str, bytes] = {}
    for index, match in enumerate(matches):
        page_url = canonical_page_url(match.group(1))
        if not page_url:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page = text[match.start():end].strip()
        if page:
            pages[page_url] = (page + "\n").encode("utf-8")
    return pages


def find_javascript_block_end(text: str, opening_brace: int) -> int | None:
    """Find the end of a generated JS function while respecting strings/comments."""
    depth = 0
    index = opening_brace
    quote: str | None = None
    escaped = False
    line_comment = False
    block_comment = False
    while index < len(text):
        char = text[index]
        following = text[index + 1] if index + 1 < len(text) else ""
        if line_comment:
            if char == "\n":
                line_comment = False
        elif block_comment:
            if char == "*" and following == "/":
                block_comment = False
                index += 1
        elif quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
        elif char == "/" and following == "/":
            line_comment = True
            index += 1
        elif char == "/" and following == "*":
            block_comment = True
            index += 1
        elif char in {"'", '"', "`"}:
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                index += 1
                while index < len(text) and text[index] in " \t;":
                    index += 1
                while index < len(text) and text[index] == "\n":
                    index += 1
                return index
        index += 1
    return None


def remove_generated_components(text: str) -> tuple[str, list[str]]:
    """Remove component implementation blobs emitted by the Mintlify endpoint."""
    warnings: list[str] = []
    while True:
        match = GENERATED_COMPONENT_RE.search(text)
        if not match:
            break
        arrow = text.find("=>", match.start(), match.end() + 500)
        opening_brace = text.find("{", arrow + 2) if arrow >= 0 else -1
        end = find_javascript_block_end(text, opening_brace) if opening_brace >= 0 else None
        if end is None:
            warnings.append(f"could not safely remove generated {match.group(1)} definition")
            break
        text = text[:match.start()] + text[end:]
    return SIMPLE_EXPORT_RE.sub("", text), warnings


def attribute(tag: str, name: str) -> str | None:
    match = re.search(rf"\b{re.escape(name)}=[\"']([^\"']*)[\"']", tag)
    return match.group(1) if match else None


def absolute_docs_link(target: str, page_url: str) -> str:
    # Mintlify content sometimes omits the leading slash from paths that are
    # nevertheless site-root namespaces (for example `langsmith/llm-gateway`).
    # Treat only known top-level namespaces this way; ordinary names remain
    # correctly relative to the current page.
    if target.startswith(("oss/", "langsmith/", "api-reference/")):
        target = "/" + target
    return urljoin(page_url, target)


def local_document_link(
    target: str,
    page_url: str,
    mirrored_urls: set[str],
) -> str:
    """Return a repository-relative link when the documentation page exists."""
    absolute = absolute_docs_link(target, page_url)
    parts = urlsplit(absolute)
    page_target = canonical_page_url(urlunsplit((parts.scheme, parts.netloc, parts.path, "", "")))
    if page_target not in mirrored_urls:
        return absolute

    if page_target == page_url and parts.fragment:
        return f"#{parts.fragment}"

    source_path = local_path_for(page_url)
    target_path = local_path_for(page_target)
    relative = os.path.relpath(target_path, start=source_path.parent)
    result = PurePosixPath(relative).as_posix()
    if parts.fragment:
        result += f"#{parts.fragment}"
    return result


def rewrite_markdown_links(
    text: str,
    page_url: str,
    mirrored_urls: set[str],
) -> str:
    """Use local links for mirrored documents and absolute URLs otherwise."""
    markdown_link = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target><[^>]+>|[^)\s]+)")

    def replace_markdown(match: re.Match[str]) -> str:
        target = match.group("target")
        wrapped = target.startswith("<") and target.endswith(">")
        plain = target[1:-1] if wrapped else target
        if plain.startswith(("mailto:", "tel:", "data:", "javascript:")):
            return match.group(0)
        parts = urlsplit(plain)
        prefix = match.group("prefix")
        is_image = prefix.startswith("!")
        explicitly_original = "original langchain documentation" in prefix.lower()
        if parts.scheme and parts.netloc.lower() != "docs.langchain.com":
            return match.group(0)
        if plain.startswith("//") or is_image or explicitly_original:
            rewritten = absolute_docs_link(plain, page_url)
        else:
            rewritten = local_document_link(plain, page_url, mirrored_urls)
        return prefix + (f"<{rewritten}>" if wrapped else rewritten)

    def replace_reference(match: re.Match[str]) -> str:
        target = match.group(2)
        parts = urlsplit(target)
        if target.startswith(("mailto:", "tel:", "data:", "//")):
            return match.group(0)
        if parts.scheme and parts.netloc.lower() != "docs.langchain.com":
            return match.group(0)
        return f"{match.group(1)}{local_document_link(target, page_url, mirrored_urls)}"

    def replace_html(match: re.Match[str]) -> str:
        attribute_name = match.group(1).lower()
        target = match.group(3)
        parts = urlsplit(target)
        if target.startswith(("mailto:", "tel:", "data:", "//")):
            return match.group(0)
        if parts.scheme and parts.netloc.lower() != "docs.langchain.com":
            return match.group(0)
        rewritten = (
            local_document_link(target, page_url, mirrored_urls)
            if attribute_name == "href"
            else absolute_docs_link(target, page_url)
        )
        return f"{match.group(1)}={match.group(2)}{rewritten}{match.group(2)}"

    output: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        while stripped.startswith("> "):
            stripped = stripped[2:].lstrip()
        marker_match = re.match(r"(`{3,}|~{3,})", stripped)
        if marker_match:
            marker = marker_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            output.append(line)
            continue
        if fence is not None:
            output.append(line)
            continue

        line = markdown_link.sub(replace_markdown, line)
        line = re.sub(r"^(\s*\[[^\]]+\]:\s*)(\S+)", replace_reference, line)
        line = re.sub(r"\b(href|src)=(['\"])([^'\"]+)\2", replace_html, line)
        output.append(line)
    return "".join(output)


def convert_html_link_cards(text: str, page_url: str) -> str:
    """Turn Mintlify's JSX-styled logo cards into simple, durable links."""
    card_re = re.compile(
        r"(?m)^[ \t]*<a\s+([^>]*\bhref=[\"'][^\"']+[\"'][^>]*)>\s*"
        r"(?P<body>(?:<img\b[^>]*/>\s*){1,2}"
        r"<span\b[^>]*>(?P<label>.*?)</span>)\s*</a>[ \t]*$"
    )

    def replace(match: re.Match[str]) -> str:
        href = attribute(match.group(1), "href")
        label = re.sub(r"<[^>]+>", "", match.group("label")).strip()
        if not href or not label:
            return match.group(0)
        return f"- [{label}]({absolute_docs_link(href, page_url)})"

    return card_re.sub(replace, text)


def dedent_mdx_children(text: str) -> str:
    """Remove presentation indentation introduced by nested MDX components."""
    output: list[str] = []
    stack: list[str] = []
    fence: str | None = None
    opening_re = re.compile(r"^<([A-Z][A-Za-z0-9.]*|div)\b[^>]*>$")
    closing_re = re.compile(r"^</([A-Z][A-Za-z0-9.]*|div)>$")

    for line in text.splitlines():
        stripped = line.strip()
        closing = closing_re.fullmatch(stripped)
        if fence is None and closing:
            name = closing.group(1)
            if name in stack:
                reverse_index = stack[::-1].index(name)
                del stack[len(stack) - reverse_index - 1:]

        remove = min(len(line) - len(line.lstrip(" ")), len(stack) * 2)
        adjusted = line[remove:]
        adjusted_stripped = adjusted.strip()
        if adjusted_stripped.startswith(("```", "~~~")):
            marker = adjusted_stripped[:3]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None

        output.append(adjusted)
        if fence is None:
            opening = opening_re.fullmatch(stripped)
            if opening and not stripped.endswith("/>") and not re.search(
                rf"</{re.escape(opening.group(1))}>\s*$", stripped
            ):
                stack.append(opening.group(1))
    return "\n".join(output)


FENCE_FLAGS = {"expandable", "wrap", "lines", "showlinenumbers", "diff"}


def code_fence_label(info: str) -> str:
    """Extract a CodeGroup tab label from the remainder of a fence info string."""
    info = info.strip()
    if not info:
        return ""
    if info[0] in "\"'":
        closing = info.find(info[0], 1)
        if closing != -1:
            return info[1:closing].strip()
    words: list[str] = []
    for word in info.split():
        if "=" in word or word.lower() in FENCE_FLAGS:
            break
        words.append(word)
    label = " ".join(words).strip()
    # Angle brackets would be reported as an unconverted MDX component, and a
    # label is display text rather than markup.
    return re.sub(r"[<>]", "", label)


def convert_mdx(text: str, page_url: str) -> str:
    """Convert common Mintlify MDX constructs to GitHub Flavored Markdown."""
    lines = text.splitlines()
    output: list[str] = []
    fence: str | None = None
    alerts: list[str] = []
    alert_names = {
        "Tip": "TIP",
        "Note": "NOTE",
        "Info": "NOTE",
        "Callout": "NOTE",
        "Warning": "WARNING",
        "Danger": "CAUTION",
        "Important": "IMPORTANT",
        "Check": "TIP",
    }
    drop_wrappers = {
        "AccordionGroup", "CardGroup", "CodeGroup", "Columns", "Frame",
        "Steps", "Tabs",
    }
    tree_depth = 0
    html_heading_level: int | None = None

    def emit(items: str | list[str]) -> None:
        values = [items] if isinstance(items, str) else items
        prefix = "> " * len(alerts)
        for value in values:
            output.append(prefix + value if value else (prefix.rstrip() if alerts else ""))

    def semantic_media_link(tag_text: str, kind: str) -> str:
        label = (
            attribute(tag_text, "aria-label")
            or attribute(tag_text, "title")
            or f"Embedded {kind}"
        )
        source = attribute(tag_text, "src")
        if source:
            return f"> **{kind.title()}:** [{label}]({absolute_docs_link(source, page_url)})"
        return (
            f"> **{kind.title()}:** {label} — [Open it in the original LangChain "
            f"documentation]({page_url})."
        )

    for line in lines:
        stripped = line.strip()
        fence_candidate = stripped.removeprefix("> ")
        if fence_candidate.startswith(("```", "~~~")):
            marker_match = re.match(r"(`{3,}|~{3,})", fence_candidate)
            marker = marker_match.group(1) if marker_match else fence_candidate[:3]
            if fence is None:
                info = fence_candidate[len(marker):].strip()
                language_match = re.match(r"[A-Za-z0-9_+.-]+", info)
                language = language_match.group(0) if language_match else ""
                # Mintlify puts a CodeGroup tab's label in the info string after
                # the language, as in ```python OpenAI theme={...}. Dropping it
                # leaves several indistinguishable blocks showing conflicting
                # code, so keep the label as a heading above the block.
                label = code_fence_label(info[len(language):])
                if label:
                    emit(f"**{label}**")
                    emit("")
                emit(marker + language)
            else:
                emit(marker)
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            emit(line)
            continue

        html_heading_open = re.fullmatch(r"<h([1-6])\b[^>]*>", stripped, flags=re.IGNORECASE)
        if html_heading_open:
            html_heading_level = int(html_heading_open.group(1))
            continue
        if html_heading_level is not None:
            if re.fullmatch(rf"</h{html_heading_level}>", stripped, flags=re.IGNORECASE):
                html_heading_level = None
            elif stripped:
                emit(f"{'#' * html_heading_level} {stripped}")
            continue

        # Generated interactive embeds cannot execute on GitHub.
        if re.fullmatch(r"<(?:PatternEmbed|ExampleEmbed)\b[^>]*/>", stripped):
            emit(
                f"> **Interactive example:** [Open it in the original LangChain documentation]({page_url})."
            )
            continue

        if re.fullmatch(r"<a\s*/>", stripped, flags=re.IGNORECASE):
            continue
        image_tag = re.fullmatch(r"<img\b[^>]*/>", stripped, flags=re.IGNORECASE)
        if image_tag and attribute(stripped, "src") is None:
            alt = attribute(stripped, "alt") or "Image"
            emit(f"> **Image:** [{alt}]({page_url})")
            continue
        if re.fullmatch(r"<iframe\b[^>]*(?:/>|>\s*</iframe>)", stripped, flags=re.IGNORECASE):
            emit(semantic_media_link(stripped, "embedded content"))
            continue
        if re.fullmatch(r"<video\b[^>]*>", stripped, flags=re.IGNORECASE):
            emit(semantic_media_link(stripped, "video"))
            continue
        if re.fullmatch(r"</video>", stripped, flags=re.IGNORECASE):
            continue
        if stripped == "Your browser does not support the video tag.":
            continue

        html_heading = re.fullmatch(
            r"<h([1-6])\b[^>]*>(.*?)</h\1>", stripped, flags=re.IGNORECASE
        )
        if html_heading:
            heading = f"{'#' * int(html_heading.group(1))} {html_heading.group(2).strip()}"
            if heading not in output:
                emit(heading)
            continue

        if re.fullmatch(r"<important\b[^>]*>", stripped, flags=re.IGNORECASE):
            alerts.append("Important")
            emit("[!IMPORTANT]")
            continue
        if re.fullmatch(r"</important>", stripped, flags=re.IGNORECASE):
            if alerts and alerts[-1] == "Important":
                alerts.pop()
            emit("")
            continue

        open_tag = re.fullmatch(r"<([A-Z][A-Za-z0-9.]*)\b([^>]*)>", stripped)
        close_tag = re.fullmatch(r"</([A-Z][A-Za-z0-9.]*)>", stripped)
        self_closing = re.fullmatch(r"<([A-Z][A-Za-z0-9.]*)\b([^>]*)/>", stripped)

        if open_tag and open_tag.group(1) in alert_names:
            name = open_tag.group(1)
            alerts.append(name)
            emit(f"[!{alert_names[name]}]")
            title = attribute(stripped, "title")
            if title:
                emit(f"**{title}**")
            continue
        if close_tag and alerts and close_tag.group(1) == alerts[-1]:
            alerts.pop()
            emit("")
            continue

        if open_tag and open_tag.group(1) == "Tree":
            tree_depth = 0
            continue
        if close_tag and close_tag.group(1) == "Tree":
            tree_depth = 0
            emit("")
            continue
        if open_tag and open_tag.group(1) == "Tree.Folder":
            name = attribute(stripped, "name") or "folder"
            emit(f"{'  ' * tree_depth}- 📁 `{name}/`")
            tree_depth += 1
            continue
        if close_tag and close_tag.group(1) == "Tree.Folder":
            tree_depth = max(0, tree_depth - 1)
            continue
        if self_closing and self_closing.group(1) == "Tree.File":
            name = attribute(stripped, "name") or "file"
            emit(f"{'  ' * tree_depth}- 📄 `{name}`")
            continue

        if open_tag and open_tag.group(1) == "Prompt":
            description = attribute(stripped, "description") or "Example prompt"
            emit(f"> **Prompt:** {description}")
            continue
        if self_closing and self_closing.group(1) == "Prompt":
            description = attribute(stripped, "description") or "Example prompt"
            emit(f"> **Prompt:** {description}")
            continue
        if close_tag and close_tag.group(1) == "Prompt":
            continue

        if (open_tag and open_tag.group(1) in drop_wrappers) or (
            close_tag and close_tag.group(1) in drop_wrappers
        ):
            continue

        if open_tag and open_tag.group(1) == "Tab":
            emit(f"#### {attribute(stripped, 'title') or 'Option'}")
            continue
        if close_tag and close_tag.group(1) == "Tab":
            continue

        if open_tag and open_tag.group(1) == "Card":
            title = attribute(stripped, "title") or "Related documentation"
            href = attribute(stripped, "href")
            heading = f"#### [{title}]({absolute_docs_link(href, page_url)})" if href else f"#### {title}"
            emit(heading)
            continue
        if self_closing and self_closing.group(1) == "Card":
            title = attribute(stripped, "title") or "Related documentation"
            href = attribute(stripped, "href")
            emit(f"- [{title}]({absolute_docs_link(href, page_url)})" if href else f"- **{title}**")
            continue
        if close_tag and close_tag.group(1) == "Card":
            continue

        if open_tag and open_tag.group(1) == "Accordion":
            title = attribute(stripped, "title") or "Details"
            emit(["<details>", f"<summary>{title}</summary>", ""])
            continue
        if close_tag and close_tag.group(1) == "Accordion":
            emit(["", "</details>"])
            continue

        if open_tag and open_tag.group(1) == "Step":
            emit(f"### {attribute(stripped, 'title') or 'Step'}")
            continue
        if close_tag and close_tag.group(1) == "Step":
            continue

        if open_tag and open_tag.group(1) == "Update":
            emit(f"## {attribute(stripped, 'label') or 'Update'}")
            continue
        if close_tag and close_tag.group(1) == "Update":
            continue

        if open_tag and open_tag.group(1) in {"ParamField", "ResponseField"}:
            name = attribute(stripped, "path") or attribute(stripped, "name") or "Field"
            kind = attribute(stripped, "type")
            emit(f"#### `{name}`{f' — `{kind}`' if kind else ''}")
            continue
        if close_tag and close_tag.group(1) in {"ParamField", "ResponseField"}:
            continue

        # Remove standalone layout divs; their children remain intact.
        if re.fullmatch(r"</?div(?:\s[^>]*)?>", stripped, flags=re.IGNORECASE):
            continue

        # Preserve the content of remaining inline MDX while dropping tags that
        # GitHub cannot execute. Standalone labeled components become headings.
        if open_tag or self_closing:
            tag_text = stripped
            title = attribute(tag_text, "title") or attribute(tag_text, "label")
            href = attribute(tag_text, "href")
            if title and href:
                emit(f"**[{title}]({absolute_docs_link(href, page_url)})**")
            elif title:
                emit(f"**{title}**")
            elif self_closing and self_closing.group(1) not in {"Anchor", "Icon"}:
                note = (
                    f"> **Interactive content:** [View this section in the original "
                    f"documentation]({page_url})."
                )
                if not output or output[-1] != note:
                    emit(note)
            continue
        if close_tag:
            continue

        cleaned = re.sub(r"</?[A-Z][A-Za-z0-9.]*\b[^>]*>", "", line)
        cleaned = re.sub(r"\s+style=\{\{.*?\}\}", "", cleaned)
        cleaned = re.sub(r"\s+className=(?:\{[^}]*\}|[\"'][^\"']*[\"'])", "", cleaned)
        cleaned = re.sub(r"\s+noZoom(?=\s|/?>)", "", cleaned)
        cleaned = re.sub(r"\bautoPlay\b", "autoplay", cleaned)
        cleaned = re.sub(r"\bplaysInline\b", "playsinline", cleaned)
        emit(cleaned)

    return "\n".join(output)


BLOCK_TAGS = {
    "address", "article", "aside", "blockquote", "div", "dl", "dd", "dt",
    "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3",
    "h4", "h5", "h6", "header", "hr", "li", "main", "nav", "ol", "p", "pre",
    "section", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul",
}
DROP_TAGS = {"script", "style", "noscript", "svg", "template", "iframe", "form", "button"}
CONTENT_SELECTORS = (
    # Most specific first: the blog's rich-text body, then a generic main.
    ("div", "w-richtext"),
    ("div", "markdown-content"),
    ("main", None),
    ("article", None),
)


class ContentExtractor(HTMLParser):
    """Collect the inner markup of the first matching content container."""

    def __init__(self, tag: str, class_token: str | None) -> None:
        super().__init__(convert_charrefs=False)
        self.tag = tag
        self.class_token = class_token
        self.depth = 0
        self.parts: list[str] = []
        self.done = False

    def _matches(self, tag: str, attrs: list[tuple[str, str | None]]) -> bool:
        if tag != self.tag:
            return False
        if self.class_token is None:
            return True
        classes = ""
        for name, value in attrs:
            if name.lower() == "class" and value:
                classes = value
        return self.class_token in classes.split()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.done:
            return
        if self.depth == 0:
            if self._matches(tag, attrs):
                self.depth = 1
            return
        if tag == self.tag:
            self.depth += 1
        self.parts.append(self.get_starttag_text() or "")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.depth and not self.done:
            self.parts.append(self.get_starttag_text() or "")

    def handle_endtag(self, tag: str) -> None:
        if self.done or not self.depth:
            return
        if tag == self.tag:
            self.depth -= 1
            if self.depth == 0:
                self.done = True
                return
        self.parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self.depth and not self.done:
            self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if self.depth and not self.done:
            self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if self.depth and not self.done:
            self.parts.append(f"&#{name};")

    @property
    def markup(self) -> str:
        return "".join(self.parts)


class MarkdownWriter(HTMLParser):
    """Convert a server-rendered content fragment to GitHub Flavored Markdown."""

    def __init__(self, page_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.out: list[str] = []
        self.drop_depth = 0
        self.pre_depth = 0
        self.list_stack: list[dict[str, int | bool]] = []
        self.link: str | None = None
        self.link_text: list[str] = []
        self.pending_heading: int | None = None
        self.in_table_cell = False
        self.table_row: list[str] = []
        self.table_rows: list[list[str]] = []
        self.table_depth = 0

    # -- helpers ---------------------------------------------------------
    def emit(self, text: str) -> None:
        if self.link is not None:
            self.link_text.append(text)
        elif self.in_table_cell:
            self.table_row.append(text)
        else:
            self.out.append(text)

    def newline(self, count: int = 1) -> None:
        if self.link is not None or self.in_table_cell:
            self.emit(" ")
            return
        self.out.append("\n" * count)

    # -- parser hooks ----------------------------------------------------
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name.lower(): (value or "") for name, value in attrs}
        if tag in DROP_TAGS:
            self.drop_depth += 1
            return
        if self.drop_depth:
            return
        if tag == "pre":
            self.pre_depth += 1
            self.newline(2)
            language = ""
            for token in values.get("class", "").split():
                if token.startswith(("language-", "lang-")):
                    language = token.split("-", 1)[1]
            self.out.append(f"```{language}\n")
            return
        if self.pre_depth:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.newline(2)
            self.pending_heading = int(tag[1])
            self.out.append("#" * self.pending_heading + " ")
            return
        if tag == "p":
            self.newline(2)
            return
        if tag == "br":
            self.out.append("  \n")
            return
        if tag == "hr":
            self.newline(2)
            self.out.append("***")
            self.newline(2)
            return
        if tag in {"ul", "ol"}:
            self.list_stack.append({"ordered": tag == "ol", "index": 0})
            self.newline(2 if len(self.list_stack) == 1 else 1)
            return
        if tag == "li":
            if not self.list_stack:
                self.list_stack.append({"ordered": False, "index": 0})
            frame = self.list_stack[-1]
            frame["index"] = int(frame["index"]) + 1
            self.newline()
            indent = "  " * (len(self.list_stack) - 1)
            marker = f"{frame['index']}." if frame["ordered"] else "-"
            self.out.append(f"{indent}{marker} ")
            return
        if tag in {"strong", "b"}:
            self.emit("**")
            return
        if tag in {"em", "i"}:
            self.emit("*")
            return
        if tag == "code":
            self.emit("`")
            return
        if tag == "blockquote":
            self.newline(2)
            self.out.append("> ")
            return
        if tag == "a":
            self.link = values.get("href", "")
            self.link_text = []
            return
        if tag == "img":
            source = absolute_media_url(values.get("src", ""), self.page_url)
            alt = re.sub(r"\s+", " ", values.get("alt", "")).strip()
            if source:
                self.emit(f"![{alt}]({source})")
            return
        if tag == "table":
            self.table_depth += 1
            self.table_rows = []
            return
        if tag == "tr" and self.table_depth:
            self.table_row = []
            return
        if tag in {"td", "th"} and self.table_depth:
            self.in_table_cell = True
            self.table_row = self.table_row or []
            self.table_row.append("\x00")
            return

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"br", "img", "hr"}:
            self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag in DROP_TAGS:
            self.drop_depth = max(0, self.drop_depth - 1)
            return
        if self.drop_depth:
            return
        if tag == "pre":
            if self.pre_depth:
                self.pre_depth -= 1
                if not self.out[-1].endswith("\n"):
                    self.out.append("\n")
                self.out.append("```")
                self.newline(2)
            return
        if self.pre_depth:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.pending_heading = None
            self.newline(2)
            return
        if tag == "p":
            self.newline(2)
            return
        if tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self.newline(2 if not self.list_stack else 1)
            return
        if tag in {"strong", "b"}:
            self.emit("**")
            return
        if tag in {"em", "i"}:
            self.emit("*")
            return
        if tag == "code":
            self.emit("`")
            return
        if tag == "blockquote":
            self.newline(2)
            return
        if tag == "a":
            text = re.sub(r"\s+", " ", "".join(self.link_text)).strip()
            target = self.link or ""
            self.link = None
            self.link_text = []
            if not text:
                return
            resolved = absolute_media_url(target, self.page_url)
            if not resolved or resolved.startswith("#"):
                self.emit(text)
            else:
                self.emit(f"[{text}]({resolved})")
            return
        if tag in {"td", "th"} and self.table_depth:
            self.in_table_cell = False
            return
        if tag == "tr" and self.table_depth:
            cells = "".join(self.table_row).split("\x00")[1:]
            self.table_rows.append([re.sub(r"\s+", " ", cell).strip() for cell in cells])
            self.table_row = []
            return
        if tag == "table" and self.table_depth:
            self.table_depth -= 1
            self.flush_table()
            return

    def flush_table(self) -> None:
        rows = [row for row in self.table_rows if any(row)]
        self.table_rows = []
        if not rows:
            return
        width = max(len(row) for row in rows)
        padded = [row + [""] * (width - len(row)) for row in rows]
        self.newline(2)
        self.out.append("| " + " | ".join(padded[0]) + " |\n")
        self.out.append("| " + " | ".join(["---"] * width) + " |\n")
        for row in padded[1:]:
            self.out.append("| " + " | ".join(row) + " |\n")
        self.newline()

    def handle_data(self, data: str) -> None:
        if self.drop_depth:
            return
        if self.pre_depth:
            self.out.append(data)
            return
        text = re.sub(r"\s+", " ", data)
        if not text.strip():
            if self.out and not self.out[-1].endswith((" ", "\n")):
                self.emit(" ")
            return
        if self.pending_heading is not None:
            text = text.strip()
        self.emit(escape_markdown(text))

    @property
    def markdown(self) -> str:
        text = "".join(self.out)
        text = text.replace("\x00", "")
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def escape_markdown(text: str) -> str:
    """Neutralize characters that would become accidental Markdown syntax."""
    text = re.sub(r"([<>])", lambda match: {"<": "&lt;", ">": "&gt;"}[match.group(1)], text)
    # An author who types a fence into rich text means the characters, not a code
    # block, and an unpaired one would swallow the rest of the page.
    return re.sub(r"(`{3,}|~{3,})", lambda match: "".join("\\" + c for c in match.group(1)), text)


def absolute_media_url(target: str, page_url: str) -> str:
    """Resolve a link or media reference found in server-rendered HTML."""
    target = (target or "").strip()
    if not target or target.startswith(("mailto:", "tel:", "data:", "javascript:")):
        return ""
    if target.startswith("#"):
        return ""
    return urljoin(page_url, target)


def extract_html_metadata(raw_html: str) -> dict[str, str]:
    """Read title, description, and dates from JSON-LD and meta tags."""
    found: dict[str, str] = {}
    for match in re.finditer(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        raw_html,
        re.S,
    ):
        try:
            payload = json.loads(match.group(1).strip())
        except (ValueError, TypeError):
            continue
        entries = payload if isinstance(payload, list) else [payload]
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            for key, field in (
                ("headline", "title"),
                ("description", "description"),
                ("datePublished", "published"),
                ("dateModified", "updated"),
            ):
                value = entry.get(key)
                if isinstance(value, str) and value.strip() and field not in found:
                    found[field] = value.strip()
            author = entry.get("author")
            if isinstance(author, dict) and isinstance(author.get("name"), str):
                found.setdefault("author", author["name"].strip())
    if "description" not in found:
        for pattern in (
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)',
            r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']*)',
        ):
            match = re.search(pattern, raw_html)
            if match and match.group(1).strip():
                found["description"] = html.unescape(match.group(1)).strip()
                break
    if "title" not in found:
        match = re.search(r"<h1[^>]*>(.*?)</h1>", raw_html, re.S)
        if match:
            found["title"] = html.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()
    if "title" not in found:
        match = re.search(r"<title[^>]*>(.*?)</title>", raw_html, re.S)
        if match:
            # Page titles are suffixed with the site name, as in
            # "create_agent | langchain | LangChain Reference".
            found["title"] = html.unescape(match.group(1)).split("|")[0].strip()
    return found


def convert_html(raw_html: str, page_url: str) -> tuple[str, list[str]]:
    """Convert a server-rendered page to Markdown using its declared container."""
    warnings: list[str] = []
    declared = section_for(page_url).content_selector
    selectors = (declared,) + CONTENT_SELECTORS if declared else CONTENT_SELECTORS
    markup = ""
    for tag, class_token in selectors:
        extractor = ContentExtractor(tag, class_token)
        extractor.feed(raw_html)
        extractor.close()
        if extractor.markup.strip():
            markup = extractor.markup
            break
    if not markup.strip():
        return "", ["no recognizable content container"]
    writer = MarkdownWriter(page_url)
    writer.feed(markup)
    writer.close()
    body = writer.markdown
    # A gated landing page renders a heading and a download form and no article.
    # Mirroring the shell would add a page every index then has to list.
    if len(body.strip()) < 80:
        return "", ["page has no article content"]
    metadata = extract_html_metadata(raw_html)
    title = metadata.get("title", "")
    if title and not re.match(r"^#\s", body):
        body = f"# {title}\n\n{body}"
    return body, warnings


def normalize_markdown(
    raw_body: bytes,
    page_url: str,
    mirrored_urls: set[str] | None = None,
) -> tuple[bytes, list[str]]:
    mirrored_urls = mirrored_urls or {page_url}
    text = raw_body.decode("utf-8")
    if section_for(page_url).kind == "html":
        text, warnings = convert_html(text, page_url)
        if not text.strip():
            return b"", warnings
        text = rewrite_markdown_links(text, page_url, mirrored_urls)
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
        warnings.extend(validate_gfm(text, mdx=False))
        return text.encode("utf-8"), warnings
    text = DOC_INDEX_RE.sub("", text)
    text, warnings = remove_generated_components(text)
    text = dedent_mdx_children(text)
    text = convert_html_link_cards(text, page_url)
    text = re.sub(
        r"(?m)^Source: (https://docs\.langchain\.com/\S+)\s*$",
        r"> Source: [Original LangChain documentation](\1)",
        text,
    )
    text = convert_mdx(text, page_url)
    text = rewrite_markdown_links(text, page_url, mirrored_urls)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    warnings.extend(validate_gfm(text))
    return text.encode("utf-8"), warnings


def validate_gfm(text: str, mdx: bool = True) -> list[str]:
    """Return structural issues that would make GitHub rendering unreliable."""
    warnings: list[str] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        while stripped.startswith("> "):
            stripped = stripped[2:].lstrip()
        marker_match = re.match(r"(`{3,}|~{3,})", stripped)
        if marker_match:
            marker = marker_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        if re.search(r"</?[A-Z][A-Za-z0-9.]*\b", line):
            warnings.append(f"line {number}: unconverted MDX component")
        # An article's prose can quote JavaScript outside a fence, so these only
        # signal a conversion leftover on a page that was authored as MDX.
        if mdx and re.match(r"\s*export const\b", line):
            warnings.append(f"line {number}: generated JavaScript export")
        if mdx and ("className=" in line or "style={{" in line):
            warnings.append(f"line {number}: unconverted JSX attribute")

        for match in re.finditer(r"(?P<image>!)?\[[^\]]*\]\((?P<target><[^>]+>|[^)\s]+)", line):
            target = match.group("target").strip("<>")
            if target.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            if not urlsplit(target).scheme and not target.startswith("//"):
                path = urlsplit(target).path
                if match.group("image") or (path and not path.endswith(".md")):
                    warnings.append(f"line {number}: invalid relative Markdown target")
                    break

        for match in re.finditer(r"\b(href|src)=['\"]([^'\"]+)['\"]", line):
            attribute_name, target = match.groups()
            if target.startswith(("mailto:", "tel:", "data:")):
                continue
            if not urlsplit(target).scheme and not target.startswith("//"):
                path = urlsplit(target).path
                if attribute_name == "src" or (path and not path.endswith(".md")):
                    warnings.append(f"line {number}: invalid relative HTML target")
                    break
    if fence is not None:
        warnings.append("unclosed fenced code block")
    return warnings[:20]


def validate_mirror_links(completed: dict[str, Download]) -> dict[str, list[str]]:
    """Ensure every generated repository-relative document link exists."""
    valid_paths = {local_path_for(url).resolve() for url in completed}
    anchors_by_path = {
        local_path_for(url).resolve(): github_heading_anchors((download.body or b"").decode("utf-8"))
        for url, download in completed.items()
    }
    issues: dict[str, list[str]] = {}

    for page_url, download in completed.items():
        text = (download.body or b"").decode("utf-8")
        source_path = local_path_for(page_url)
        page_issues: list[str] = []
        fence: str | None = None
        for number, line in enumerate(text.splitlines(), 1):
            stripped = line.lstrip()
            while stripped.startswith("> "):
                stripped = stripped[2:].lstrip()
            marker_match = re.match(r"(`{3,}|~{3,})", stripped)
            if marker_match:
                marker = marker_match.group(1)
                if fence is None:
                    fence = marker
                elif marker[0] == fence[0] and len(marker) >= len(fence):
                    fence = None
                continue
            if fence is not None:
                continue

            targets = [
                match.group(1).strip("<>")
                for match in re.finditer(r"(?<!!)\[[^\]]*\]\((<[^>]+>|[^)\s]+)", line)
            ]
            targets.extend(
                match.group(1)
                for match in re.finditer(r"\bhref=['\"]([^'\"]+)['\"]", line)
            )
            for target in targets:
                parts = urlsplit(target)
                if parts.scheme or target.startswith(("//", "mailto:", "tel:", "data:")):
                    continue
                resolved = (
                    source_path.resolve()
                    if not parts.path
                    else (source_path.parent / unquote(parts.path)).resolve()
                )
                if resolved not in valid_paths:
                    page_issues.append(f"line {number}: missing local target {target}")
                    continue
                fragment = unquote(parts.fragment).split(":~:text=", 1)[0]
                if fragment and fragment not in anchors_by_path.get(resolved, set()):
                    page_issues.append(f"line {number}: missing local fragment {target}")
        if page_issues:
            issues[page_url] = page_issues[:20]
    return issues


def github_heading_anchors(text: str) -> set[str]:
    """Approximate GitHub's heading IDs and include explicit HTML anchors."""
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        while stripped.startswith("> "):
            stripped = stripped[2:].lstrip()
        marker_match = re.match(r"(`{3,}|~{3,})", stripped)
        if marker_match:
            marker = marker_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue

        anchors.update(
            html.unescape(anchor)
            for anchor in re.findall(r"\b(?:id|name)=['\"]([^'\"]+)", line)
        )
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*$", stripped)
        if not heading:
            continue
        title = re.sub(r"<[^>]+>", "", heading.group(1))
        title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
        title = re.sub(r"[`*_~]", "", title).strip().lower()
        slug = "".join(
            character
            for character in title
            if not (
                unicodedata.category(character).startswith("P")
                and character not in {"-", "_"}
            )
        )
        slug = re.sub(r"\s", "-", slug)
        duplicate = seen.get(slug, 0)
        seen[slug] = duplicate + 1
        anchors.add(slug if duplicate == 0 else f"{slug}-{duplicate}")
    return anchors


def add_fragment_aliases(completed: dict[str, Download]) -> int:
    """Add GitHub-compatible anchors for upstream fragments Mintlify supplied."""
    url_by_path = {local_path_for(url).resolve(): url for url in completed}
    incoming: dict[str, set[str]] = {}

    for source_url, download in completed.items():
        text = (download.body or b"").decode("utf-8")
        source_path = local_path_for(source_url)
        fence: str | None = None
        for line in text.splitlines():
            stripped = line.lstrip()
            while stripped.startswith("> "):
                stripped = stripped[2:].lstrip()
            marker_match = re.match(r"(`{3,}|~{3,})", stripped)
            if marker_match:
                marker = marker_match.group(1)
                if fence is None:
                    fence = marker
                elif marker[0] == fence[0] and len(marker) >= len(fence):
                    fence = None
                continue
            if fence is not None:
                continue
            for match in re.finditer(r"(?<!!)\[[^\]]*\]\((<[^>]+>|[^)\s]+)", line):
                target = match.group(1).strip("<>")
                parts = urlsplit(target)
                if parts.scheme or not parts.fragment:
                    continue
                target_path = (
                    source_path.resolve()
                    if not parts.path
                    else (source_path.parent / unquote(parts.path)).resolve()
                )
                target_url = url_by_path.get(target_path)
                if target_url:
                    fragment = unquote(parts.fragment).split(":~:text=", 1)[0]
                    if fragment:
                        incoming.setdefault(target_url, set()).add(fragment)

    added = 0
    for target_url, fragments in incoming.items():
        download = completed[target_url]
        text = (download.body or b"").decode("utf-8")
        missing = sorted(fragments - github_heading_anchors(text))
        if not missing:
            continue

        lines = text.splitlines()
        heading_rows: list[tuple[int, str]] = []
        fence = None
        for index, line in enumerate(lines):
            stripped = line.lstrip()
            marker_match = re.match(r"(`{3,}|~{3,})", stripped)
            if marker_match:
                marker = marker_match.group(1)
                if fence is None:
                    fence = marker
                elif marker[0] == fence[0] and len(marker) >= len(fence):
                    fence = None
                continue
            if fence is None:
                heading = re.match(r"^#{1,6}\s+(.+?)\s*#*$", stripped)
                if heading:
                    normalized = re.sub(r"[^a-z0-9]+", "-", heading.group(1).lower()).strip("-")
                    heading_rows.append((index, normalized))

        insertions: dict[int, list[str]] = {}
        fallback = heading_rows[0][0] + 1 if heading_rows else 0
        for fragment in missing:
            normalized_fragment = re.sub(r"[^a-z0-9]+", "-", fragment.lower()).strip("-")
            best_index = fallback
            best_score = 0.0
            for heading_index, normalized_heading in heading_rows:
                score = difflib.SequenceMatcher(
                    None,
                    normalized_fragment,
                    normalized_heading,
                ).ratio()
                if score > best_score:
                    best_index, best_score = heading_index, score
            insertions.setdefault(best_index, []).append(
                f'<a id="{html.escape(fragment, quote=True)}"></a>'
            )
            added += 1

        for index in sorted(insertions, reverse=True):
            aliases = insertions[index]
            lines[index:index] = aliases + [""]
        download.body = ("\n".join(lines).strip() + "\n").encode("utf-8")
    return added


TAG_STOPWORDS = {"oss", "python", "index", "home", "docs", "page", "overview"}
CALLOUT_RE = re.compile(r"^\[!(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]")
# Reference pages open with a type line and a link back to the rendered site,
# and every page can carry a mirrored-source note. None of them describe the page.
BOILERPLATE_PROSE_RE = re.compile(r"^(?:\*\*\w+\*\*\s+in\s|\U0001F4D6\s|Source:)")


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_inline_markup(text: str) -> str:
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*`]+", "", text)
    # Unwrap underscore emphasis without touching snake_case identifiers.
    text = re.sub(r"(?<![\w])_{1,2}([^_]+)_{1,2}(?![\w])", r"\1", text)
    return collapse(text)


def truncate(text: str, limit: int = 200) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:.") + "..."


def page_category(section: Section) -> str:
    if section.host == REFERENCE_HOST:
        return "reference"
    if section.host == SITE_HOST:
        return section.prefix.strip("/") or "site"
    return "docs"


def slug_token(segment: str) -> str:
    token = unquote(segment).strip().lower().removesuffix(".md")
    return re.sub(r"[^a-z0-9._-]+", "-", token).strip("-._")


def derive_tags(page_url: str, section: Section) -> list[str]:
    tags = [page_category(section)]
    for segment in urlsplit(page_url).path.strip("/").split("/"):
        token = slug_token(segment)
        if token and token not in TAG_STOPWORDS and token not in tags:
            tags.append(token)
    return tags[:8]


def first_prose(lines: Iterable[str]) -> str:
    """Return the first descriptive paragraph, skipping non-prose blocks."""
    collected: list[str] = []
    fence: str | None = None
    for raw in lines:
        stripped = raw.strip()
        marker_match = re.match(r"(`{3,}|~{3,})", stripped)
        if marker_match:
            marker = marker_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        while stripped.startswith(">"):
            stripped = stripped[1:].strip()
        if not stripped or stripped.startswith(("#", "|", "<", "---", "===", ":::")):
            if collected:
                break
            continue
        if CALLOUT_RE.match(stripped) or BOILERPLATE_PROSE_RE.match(stripped):
            continue
        collected.append(stripped)
    return strip_inline_markup(" ".join(collected))


def humanize_slug(page_url: str) -> str:
    segment = urlsplit(page_url).path.rstrip("/").rsplit("/", 1)[-1]
    words = re.split(r"[-_]+", unquote(segment)) or ["Index"]
    return " ".join(word[:1].upper() + word[1:] for word in words if word) or "Index"


def derive_page_metadata(
    body: str, page_url: str, upstream: dict[str, str]
) -> dict[str, object]:
    """Derive front matter from the page's own headings, metadata, and URL."""
    section = section_for(page_url)
    lines = body.splitlines()
    title = ""
    for index, line in enumerate(lines):
        if line.startswith("# "):
            title = strip_inline_markup(line[2:])
            lines = lines[index + 1 :]
            break
    description = upstream.get("description", "") or first_prose(lines)
    metadata: dict[str, object] = {
        "title": title or upstream.get("title", "") or humanize_slug(page_url),
        "description": truncate(collapse(description)),
        "source": page_url,
        "category": page_category(section),
        "tags": derive_tags(page_url, section),
    }
    for key in ("published", "author"):
        if upstream.get(key):
            metadata[key] = collapse(upstream[key])
    return metadata


def yaml_scalar(value: object) -> str:
    text = collapse(str(value)).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def render_frontmatter(metadata: dict[str, object]) -> bytes:
    lines = ["---"]
    for key in ("title", "description", "source", "category", "published", "author"):
        value = metadata.get(key)
        if value:
            lines.append(f"{key}: {yaml_scalar(value)}")
    tags = metadata.get("tags")
    if isinstance(tags, list) and tags:
        lines.append("tags: [" + ", ".join(tags) + "]")
    lines.append("---")
    return ("\n".join(lines) + "\n\n").encode("utf-8")


def plural(count: int, noun: str, plural_form: str | None = None) -> str:
    return f"{count} {noun if count == 1 else plural_form or noun + 's'}"


def directory_index_documents(
    pages: dict[str, dict[str, object]],
) -> dict[str, bytes]:
    """Build one _index.md per directory so an agent can navigate by description."""
    children: dict[str, set[str]] = {}
    entries: dict[str, list[tuple[str, str, str]]] = {}
    for relative, metadata in pages.items():
        path = PurePosixPath(relative)
        parent = path.parent.as_posix()
        parent = "" if parent == "." else parent
        entries.setdefault(parent, []).append(
            (path.name, str(metadata.get("title", "")), str(metadata.get("description", "")))
        )
        ancestor = parent
        while True:
            grandparent = PurePosixPath(ancestor).parent.as_posix() if ancestor else None
            grandparent = "" if grandparent == "." else grandparent
            children.setdefault(ancestor, set())
            if ancestor == "":
                break
            children.setdefault(grandparent or "", set()).add(ancestor)
            ancestor = grandparent or ""

    subtree_totals: dict[str, int] = {}

    def subtree_total(directory: str) -> int:
        if directory not in subtree_totals:
            subtree_totals[directory] = len(entries.get(directory, [])) + sum(
                subtree_total(child) for child in children.get(directory, set())
            )
        return subtree_totals[directory]

    documents: dict[str, bytes] = {}
    for directory in sorted(children):
        files = sorted(entries.get(directory, []))
        subdirectories = sorted(children.get(directory, set()))
        title = directory or "LangChain mirror"
        total = subtree_total(directory)
        summary = plural(len(files), "page") + " here"
        if total != len(files):
            summary += f", {plural(total, 'page')} including subdirectories"
        body = [f"# {title}", "", summary + "."]
        if subdirectories:
            body += ["", "## Directories", ""]
            for child in subdirectories:
                name = PurePosixPath(child).name
                body.append(
                    f"- [{name}/]({name}/{INDEX_NAME}) - {plural(subtree_total(child), 'page')}"
                )
        if files:
            body += ["", "## Files", ""]
            for name, page_title, description in files:
                label = page_title or name.removesuffix(".md")
                suffix = f" - {description}" if description else ""
                body.append(f"- [{label}]({name}){suffix}")
        metadata = {
            "title": title,
            "description": (
                f"Index of {plural(len(files), 'page')} and "
                f"{plural(len(subdirectories), 'subdirectory', 'subdirectories')} under "
                f"{directory or 'the mirror root'}."
            ),
            "category": "index",
            "tags": ["index"]
            + [
                token
                for token in (slug_token(part) for part in PurePosixPath(directory).parts)
                if token
            ][:7],
        }
        relative = f"{directory}/{INDEX_NAME}" if directory else INDEX_NAME
        documents[relative] = render_frontmatter(metadata) + ("\n".join(body) + "\n").encode()
    return documents


def discover_seed_urls(timeout: float) -> tuple[set[str], dict[str, bytes], list[str]]:
    pages = {
        canonical_page_url(section.entry_url)
        for section in SECTIONS
        if section.entry_url is not None
    }
    errors: list[str] = []
    full_pages: dict[str, bytes] = {}

    for sitemap_url in SITEMAPS:
        try:
            sitemap, _, _ = request_bytes(sitemap_url, timeout)
            root = ET.fromstring(sitemap)
            for element in root.iter():
                if element.tag.endswith("loc") and element.text:
                    page = canonical_page_url(element.text)
                    if page:
                        pages.add(page)
        except Exception as exc:  # Continue with the other independent indexes.
            errors.append(f"{sitemap_url} discovery: {exc}")

    for llms_url in LLMS_INDEXES:
        try:
            llms, _, _ = request_bytes(llms_url, timeout)
            for raw_url in URL_RE.findall(llms.decode("utf-8", errors="replace")):
                page = canonical_page_url(raw_url.rstrip(".,:;"))
                if page:
                    pages.add(page)
        except Exception as exc:
            errors.append(f"{llms_url} discovery: {exc}")

    try:
        llms_full, _, _ = request_bytes(LLMS_FULL_URL, timeout)
        full_pages = parse_llms_full(llms_full)
        pages.update(full_pages)
    except Exception as exc:
        errors.append(f"llms-full.txt content discovery: {exc}")

    return {page for page in pages if page}, full_pages, errors


def download_one(page_url: str, timeout: float, full_pages: dict[str, bytes]) -> Download:
    section = section_for(page_url)

    def llms_full_fallback() -> Download | None:
        raw_body = full_pages.get(page_url)
        if raw_body is None:
            return None
        return Download(
            page_url=page_url,
            final_url=LLMS_FULL_URL,
            raw_body=raw_body,
            content_source="llms-full.txt-fallback",
        )

    # llms-full.txt is an excellent discovery index, but it can lag behind a
    # page's dedicated Markdown endpoint. Always request the page itself first
    # so edits and newly added heading anchors arrive on the next mirror run.
    try:
        raw_body, final_url, content_type = request_bytes(markdown_url(page_url), timeout)
        if urlsplit(final_url).netloc.lower() != section.host:
            fallback = llms_full_fallback()
            return fallback or Download(
                page_url=page_url,
                final_url=final_url,
                skipped=f"redirects outside {section.host}",
            )
        prefix = raw_body[:200].lstrip().lower()
        served_html = content_type == "text/html" or prefix.startswith(
            (b"<!doctype html", b"<html")
        )
        if section.kind == "mdx" and served_html:
            raise RuntimeError("server returned HTML instead of Markdown")
        raw_body.decode("utf-8")
        return Download(
            page_url=page_url,
            final_url=final_url,
            raw_body=raw_body,
        )
    except MissingPage as exc:
        fallback = llms_full_fallback()
        return fallback or Download(page_url=page_url, missing=str(exc))
    except ExternalRedirect as exc:
        fallback = llms_full_fallback()
        return fallback or Download(
            page_url=page_url,
            final_url=exc.url,
            skipped=f"redirects outside {section.host}",
        )
    except (RuntimeError, UnicodeDecodeError) as exc:
        fallback = llms_full_fallback()
        return fallback or Download(page_url=page_url, error=str(exc))


def links_from(download: Download) -> set[str]:
    source_body = download.raw_body or download.body
    if source_body is None:
        return set()
    text = source_body.decode("utf-8")
    renderable_lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        while stripped.startswith("> "):
            stripped = stripped[2:].lstrip()
        marker_match = re.match(r"(`{3,}|~{3,})", stripped)
        if marker_match:
            marker = marker_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            renderable_lines.append(line)
    text = "\n".join(renderable_lines)
    final_page = (
        download.page_url
        if download.content_source.startswith("llms-full.txt")
        else (download.final_url or download.page_url).removesuffix(".md")
    )
    candidates: Iterable[str] = (
        list(MARKDOWN_LINK_RE.findall(text))
        + list(HTML_LINK_RE.findall(text))
        + list(URL_RE.findall(text))
    )
    found = set()
    for candidate in candidates:
        page = canonical_page_url(absolute_docs_link(candidate, final_page), final_page)
        if page:
            found.add(page)
    return found


def atomic_write(path: Path, body: bytes) -> bool:
    """Write when changed and return whether file contents were updated."""
    if path.exists() and path.read_bytes() == body:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_bytes(body)
    os.replace(temporary, path)
    return True


def load_previous_manifest() -> dict:
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def relative_output_path(path: Path) -> str:
    return path.relative_to(OUTPUT_ROOT).as_posix()


def clean_stale_files(previous: dict, current_files: set[str]) -> list[str]:
    removed: list[str] = []
    directories_to_check: set[Path] = set()
    old_files: dict = {}
    for key in ("files", "index_files"):
        group = previous.get(key)
        if isinstance(group, dict):
            old_files.update(group)
    if not old_files:
        return removed
    root = OUTPUT_ROOT.resolve()
    for relative in sorted(set(old_files) - current_files):
        candidate = (OUTPUT_ROOT / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            continue
        if candidate.suffix == ".md" and candidate.is_file():
            candidate.unlink()
            removed.append(relative)
            parent = candidate.parent
            while parent != root:
                directories_to_check.add(parent)
                parent = parent.parent
    protected_directories = set()
    for section in SECTIONS:
        directory = OUTPUT_ROOT / section.folder
        if section.local_subfolder:
            directory /= section.local_subfolder
        protected_directories.add(directory.resolve())
    # Only consider directories made empty by the managed files removed above.
    # Never walk unrelated repository state such as .git or .github.
    for directory in sorted(directories_to_check, key=lambda path: len(path.parts), reverse=True):
        if directory.resolve() in protected_directories:
            continue
        try:
            directory.rmdir()
        except OSError:
            pass
    return removed


def mirror(*, workers: int, timeout: float, clean: bool) -> int:
    if tqdm is None:  # pragma: no cover - depends on the local environment
        uv = shutil.which("uv")
        if uv:
            os.execv(uv, [uv, "run", "--script", str(Path(__file__).resolve()), *sys.argv[1:]])
        raise SystemExit(
            "Missing dependency: install it with `python3 -m pip install tqdm`, "
            "or install uv so this script can provision tqdm automatically."
        )
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for section in SECTIONS:
        directory = OUTPUT_ROOT / section.folder
        if section.local_subfolder:
            directory /= section.local_subfolder
        directory.mkdir(parents=True, exist_ok=True)

    seeds, full_pages, discovery_errors = discover_seed_urls(timeout)
    if not seeds:
        print("No documentation pages were discovered; existing files were left untouched.", file=sys.stderr)
        for error in discovery_errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    queued = set(seeds)
    completed: dict[str, Download] = {}
    failures: dict[str, str] = {}
    broken_links: dict[str, str] = {}
    skipped: dict[str, str] = {}
    missing: dict[str, str] = {}
    changed = 0

    with tqdm(desc="Downloading Markdown", unit="page", total=len(queued), dynamic_ncols=True) as progress:
        while True:
            batch = sorted(
                queued
                - completed.keys()
                - failures.keys()
                - broken_links.keys()
                - skipped.keys()
                - missing.keys()
            )
            if not batch:
                break
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {
                    executor.submit(download_one, page, timeout, full_pages): page
                    for page in batch
                }
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result.missing:
                        # A route an upstream sitemap or index still lists but no
                        # longer serves is an upstream fact, not a mirror defect.
                        missing[result.page_url] = result.missing
                    elif result.skipped:
                        skipped[result.page_url] = f"{result.skipped}: {result.final_url}"
                    elif result.error:
                        target = failures if result.page_url in seeds else broken_links
                        target[result.page_url] = result.error
                    else:
                        completed[result.page_url] = result
                        new_links = links_from(result) - queued
                        if new_links:
                            queued.update(new_links)
                            progress.total = len(queued)
                            progress.refresh()
                    progress.update(1)

    # A link-discovered page that fails is normally a stale link in someone
    # else's prose. When the previous run managed its file, the failure is a
    # regression instead, and leaving it in broken_links would let stale
    # cleanup delete a page that upstream still publishes.
    previous = load_previous_manifest()
    previously_managed = set(previous.get("files", {}))
    for page_url in sorted(broken_links):
        if relative_output_path(local_path_for(page_url)) in previously_managed:
            failures[page_url] = broken_links.pop(page_url)

    # Conversion decides whether a rendered page carries an article at all, so
    # content-free pages leave before the set of mirrored URLs is fixed and other
    # pages start citing a file that is never written.
    empty: dict[str, str] = {}
    for page_url in [url for url in completed if section_for(url).kind == "html"]:
        raw = (completed[page_url].raw_body or b"").decode("utf-8", errors="replace")
        body, reasons = convert_html(raw, page_url)
        if not body.strip():
            empty[page_url] = reasons[0] if reasons else "no content"
            del completed[page_url]

    mirrored_urls = set(completed)
    for page_url, result in sorted(completed.items()):
        body, warnings = normalize_markdown(
            result.raw_body or b"",
            page_url,
            mirrored_urls,
        )
        result.body = body
        result.normalization_warnings = warnings

    fragment_alias_count = add_fragment_aliases(completed)

    link_warnings = validate_mirror_links(completed)
    for page_url, warnings in link_warnings.items():
        result = completed[page_url]
        result.normalization_warnings = (result.normalization_warnings or []) + warnings

    # Front matter is prepended after link and anchor validation so a leading
    # YAML block is never read as a heading or a link target.
    for page_url, result in sorted(completed.items()):
        upstream = (
            extract_html_metadata((result.raw_body or b"").decode("utf-8", errors="replace"))
            if section_for(page_url).kind == "html"
            else {}
        )
        result.metadata = derive_page_metadata(
            (result.body or b"").decode("utf-8"), page_url, upstream
        )
        result.body = render_frontmatter(result.metadata) + (result.body or b"")
        if atomic_write(local_path_for(page_url), result.body):
            changed += 1

    files: dict[str, dict[str, str | int]] = {}
    page_metadata: dict[str, dict[str, object]] = {}
    normalization_warnings: dict[str, list[str]] = {}
    for page_url, result in sorted(completed.items()):
        path = local_path_for(page_url)
        body = result.body or b""
        raw_body = result.raw_body or body
        relative = relative_output_path(path)
        files[relative] = {
            "source": page_url,
            "resolved_markdown": result.final_url or markdown_url(page_url),
            "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
            "upstream_bytes": len(raw_body),
            "upstream_sha256": hashlib.sha256(raw_body).hexdigest(),
            "content_source": result.content_source,
        }
        page_metadata[relative] = result.metadata or {}
        if result.normalization_warnings:
            normalization_warnings[page_url] = result.normalization_warnings

    index_files: dict[str, dict[str, str | int]] = {}
    for relative, document in sorted(directory_index_documents(page_metadata).items()):
        if atomic_write(OUTPUT_ROOT / relative, document):
            changed += 1
        index_files[relative] = {
            "bytes": len(document),
            "sha256": hashlib.sha256(document).hexdigest(),
            "content_source": "generated-index",
        }

    removed = (
        clean_stale_files(previous, set(files) | set(index_files))
        if clean and not failures
        else []
    )
    manifest = {
        "schema_version": 4,
        "source": ORIGIN,
        "hosts": sorted(ALLOWED_HOSTS),
        "page_count": len(files),
        "index_count": len(index_files),
        "files": files,
        "index_files": index_files,
        "failures": failures,
        "broken_or_non_page_links": broken_links,
        "external_redirects": skipped,
        "upstream_missing": missing,
        "pages_without_content": empty,
        "normalization_warnings": normalization_warnings,
        "llms_full_page_count": len(full_pages),
        "generated_fragment_alias_count": fragment_alias_count,
        "configured_unpublished_scopes": [
            f"https://{section.host}{section.prefix}"
            for section in SECTIONS
            if section.entry_url is None
        ],
        "discovery_warnings": discovery_errors,
    }
    atomic_write(MANIFEST_PATH, (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode())

    section_counts = {(section.host, section.prefix): 0 for section in SECTIONS}
    for page in completed:
        section = section_for(page)
        section_counts[(section.host, section.prefix)] += 1
    print(
        f"Mirrored {len(files)} pages and {len(index_files)} directory indexes "
        f"({changed} changed, {len(removed)} stale removed)."
    )
    print(
        "Used page-specific Markdown for "
        f"{sum(r.content_source == 'page-markdown' for r in completed.values())} pages; "
        "llms-full.txt fallback for "
        f"{sum(r.content_source == 'llms-full.txt-fallback' for r in completed.values())}."
    )
    print(
        "Scopes: "
        + ", ".join(
            f"{host}{prefix or '/'}={count}"
            for (host, prefix), count in sorted(section_counts.items())
            if count
        )
    )
    if discovery_errors:
        print("Discovery warnings:", file=sys.stderr)
        for error in discovery_errors:
            print(f"  - {error}", file=sys.stderr)
    if failures:
        print(f"Failed pages ({len(failures)}):", file=sys.stderr)
        for url, error in sorted(failures.items()):
            print(f"  - {url}: {error}", file=sys.stderr)
        print("Stale cleanup was skipped because the mirror was incomplete.", file=sys.stderr)
        return 1
    if broken_links:
        print(f"Ignored {len(broken_links)} broken/non-page links found inside documents.", file=sys.stderr)
    if missing:
        print(f"Ignored {len(missing)} discovered routes that upstream no longer serves.", file=sys.stderr)
    if empty:
        print(f"Ignored {len(empty)} pages that publish no article content.", file=sys.stderr)
    if skipped:
        print(f"Ignored {len(skipped)} routes that redirect off the mirrored hosts.", file=sys.stderr)
    if normalization_warnings:
        print(f"Normalization warnings in {len(normalization_warnings)} pages.", file=sys.stderr)
        for url, warnings in sorted(normalization_warnings.items()):
            print(f"  - {url}:", file=sys.stderr)
            for warning in warnings:
                print(f"      {warning}", file=sys.stderr)
        return 1
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=12, help="parallel downloads (default: 12)")
    parser.add_argument("--timeout", type=float, default=30.0, help="per-request timeout in seconds")
    parser.add_argument("--no-clean", action="store_true", help="keep previously managed pages removed upstream")
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be at least 1")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    return args


if __name__ == "__main__":
    arguments = parse_args()
    raise SystemExit(mirror(workers=arguments.workers, timeout=arguments.timeout, clean=not arguments.no_clean))
