#!/usr/bin/env python3
"""Update a GitHub profile README with the latest arXiv physics.med-ph papers.

Fetches the most recent submissions from the arXiv API (Atom feed) for the
medical-physics category and splices a compact Markdown listing into a README
between two marker comments:

    <!-- ARXIV-FEED:START -->
    ... generated content ...
    <!-- ARXIV-FEED:END -->

Usage:
    python update_feed.py [--readme README.md] [--count 6]

Options:
    --readme PATH   Path to the README to update (default: README.md).
    --count N       Number of papers to include (default: 6).

Exit codes:
    0  README updated (or already up to date).
    1  Network/parse failure, missing markers, or missing README.

Uses only the Python standard library so it can run in bare CI runners.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime

API_URL = "https://export.arxiv.org/api/query"
CATEGORY = "physics.med-ph"
USER_AGENT = "arxiv-readme-feed/1.0 (github-actions; profile README updater)"
TIMEOUT_SECONDS = 30
ABSTRACT_LIMIT = 200
MAX_AUTHORS = 3
# arXiv rate-limits bursts (HTTP 429) and occasionally 503s; retry with backoff.
MAX_RETRIES = 4
RETRY_BACKOFF_SECONDS = 4

START_MARKER = "<!-- ARXIV-FEED:START -->"
END_MARKER = "<!-- ARXIV-FEED:END -->"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


def collapse_ws(text: str) -> str:
    """Collapse all runs of whitespace (incl. newlines) into single spaces."""
    return re.sub(r"\s+", " ", text or "").strip()


def trim_abstract(text: str, limit: int = ABSTRACT_LIMIT) -> str:
    """Collapse whitespace and trim to ~limit chars, cutting on a word boundary."""
    text = collapse_ws(text)
    if len(text) <= limit:
        return text
    cut = text[:limit]
    # Avoid chopping mid-word if there is a reasonable space to break on.
    space = cut.rfind(" ")
    if space > limit // 2:
        cut = cut[:space]
    return cut.rstrip(" .,;:") + "…"


def fetch_entries(count: int) -> list[dict]:
    """Query the arXiv API and return a list of parsed entry dicts.

    Each dict has keys: title, authors, summary, published, link.
    Raises RuntimeError on network or parse failure.
    """
    params = urllib.parse.urlencode(
        {
            "search_query": f"cat:{CATEGORY}",
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "start": 0,
            "max_results": count,
        }
    )
    url = f"{API_URL}?{params}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        if attempt:
            # Exponential backoff; arXiv asks callers to space out requests.
            time.sleep(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)))
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                payload = response.read()
            break
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
            last_exc = exc
            print(
                f"arXiv request attempt {attempt + 1}/{MAX_RETRIES} failed: {exc}",
                file=sys.stderr,
            )
    else:
        raise RuntimeError(f"arXiv API request failed after {MAX_RETRIES} attempts: {last_exc}")

    try:
        root = ET.fromstring(payload)
    except ET.ParseError as exc:
        raise RuntimeError(f"Could not parse arXiv Atom response: {exc}") from exc

    entries = []
    for entry in root.findall("atom:entry", NS):
        entries.append(parse_entry(entry))
    return entries


def parse_entry(entry: ET.Element) -> dict:
    """Extract the fields we render from a single <entry> element."""
    title = collapse_ws(entry.findtext("atom:title", default="(untitled)", namespaces=NS))
    summary = trim_abstract(entry.findtext("atom:summary", default="", namespaces=NS))

    authors = [
        collapse_ws(name.text or "")
        for name in entry.findall("atom:author/atom:name", NS)
    ]
    authors = [a for a in authors if a]

    published_raw = entry.findtext("atom:published", default="", namespaces=NS)
    published = published_raw[:10] if len(published_raw) >= 10 else ""
    try:
        # Validate the date fragment; fall back to raw text if unparseable.
        datetime.strptime(published, "%Y-%m-%d")
    except ValueError:
        published = collapse_ws(published_raw)

    # Prefer the alternate <link>; fall back to <id> (which is the abs URL).
    link = ""
    for link_el in entry.findall("atom:link", NS):
        if link_el.get("rel") == "alternate":
            link = link_el.get("href", "")
            break
    if not link:
        link = collapse_ws(entry.findtext("atom:id", default="", namespaces=NS))

    return {
        "title": title,
        "authors": authors,
        "summary": summary,
        "published": published,
        "link": link,
    }


def format_authors(authors: list[str]) -> str:
    """Render an author list as 'A, B, C et al.' (first MAX_AUTHORS shown)."""
    if not authors:
        return "Unknown authors"
    shown = ", ".join(authors[:MAX_AUTHORS])
    if len(authors) > MAX_AUTHORS:
        shown += " et al."
    return shown


def format_entry(entry: dict) -> str:
    """Render one paper as a compact Markdown block."""
    title = entry["title"]
    link = entry["link"]
    heading = f"**[{title}]({link})**" if link else f"**{title}**"
    byline = f"_{format_authors(entry['authors'])} · {entry['published']}_"
    lines = [heading, byline]
    if entry["summary"]:
        lines.append(entry["summary"])
    return "  \n".join(lines)


def render_block(entries: list[dict], today: str | None = None) -> str:
    """Render the full feed block that goes between the README markers."""
    today = today or date.today().isoformat()
    parts = [format_entry(entry) for entry in entries]
    if not parts:
        parts = ["_No recent papers found._"]
    footer = f"_Updated: {today} · source: arXiv {CATEGORY}_"
    return "\n\n".join(parts + [footer])


def splice_readme(readme_text: str, block: str) -> str:
    """Replace the content between the feed markers with `block`.

    Raises ValueError if either marker is missing or they are out of order.
    """
    start = readme_text.find(START_MARKER)
    end = readme_text.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        raise ValueError(
            f"README is missing feed markers '{START_MARKER}' / '{END_MARKER}' "
            "(or they are out of order)."
        )
    head = readme_text[: start + len(START_MARKER)]
    tail = readme_text[end:]
    return f"{head}\n{block}\n{tail}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Update README arXiv medical-physics feed block."
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to the README file to update (default: README.md).",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=6,
        help="Number of papers to include (default: 6).",
    )
    args = parser.parse_args(argv)

    try:
        with open(args.readme, encoding="utf-8") as fh:
            original = fh.read()
    except OSError as exc:
        print(f"ERROR: cannot read {args.readme}: {exc}", file=sys.stderr)
        return 1

    # Fail fast on missing markers before touching the network.
    if START_MARKER not in original or END_MARKER not in original:
        print(
            f"ERROR: {args.readme} does not contain both markers "
            f"'{START_MARKER}' and '{END_MARKER}'.",
            file=sys.stderr,
        )
        return 1

    try:
        entries = fetch_entries(args.count)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print("README left unchanged.", file=sys.stderr)
        return 1

    block = render_block(entries)
    try:
        updated = splice_readme(original, block)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if updated == original:
        print("Feed already up to date; nothing to write.")
        return 0

    with open(args.readme, "w", encoding="utf-8") as fh:
        fh.write(updated)
    print(f"Wrote {len(entries)} entries to {args.readme}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
