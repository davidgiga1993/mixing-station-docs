"""
Exports the rendered html pages as JSON so they
can be used in other SPA

Relative links in the page html are rewritten to absolute urls:
- Links to other pages: MS_SPA_PAGE_BASE + page url
- Everything else: MS_SPA_ASSET_BASE + file path
"""

import json
import os
import posixpath
import re
from typing import Dict, List, Optional
from urllib.parse import urlsplit

from properdocs.structure.nav import Link, Section
from properdocs.structure.pages import Page

PAGE_BASE = os.environ.get("MS_SPA_PAGE_BASE", "/docs/")
ASSET_BASE = os.environ.get("MS_SPA_ASSET_BASE", "/docs-content/")
OUT_DIR = "_spa"

URL_ATTR_PATTERN = re.compile(r'(\s(?:href|src|poster)=")([^"]*)"') # Poor man href parser (insert stackoverflow parse html with regex meme here)
EXTERNAL_PATTERN = re.compile(r"^([a-z][a-z0-9+.-]*:|//|#)", re.I) # Matches a url scheme

_pages: Dict[str, dict] = {}
_nav = None
_page_urls = set()


def on_nav(nav, config, files, **kwargs):
    global _nav
    _nav = nav
    _page_urls.clear()
    _pages.clear()
    for file in files.documentation_pages():
        _page_urls.add(file.url)
    for source in _get_redirects(config, files):
        _page_urls.add(source)
    return nav


def on_page_context(context, page: Page, config, nav, **kwargs):
    if page.url.startswith("print_page"):
        return context

    content = _render_puml(page.content or "", config)
    content = _rewrite_urls(content, page.url)
    _pages[page.url] = {
        "url": page.url,
        "title": page.title,
        "description": page.meta.get("description"),
        "toc": [_toc_item(item) for item in page.toc],
        "html": content,
    }
    return context


def _render_puml(html: str, config) -> str:
    # mkdocs_puml only replaces its placeholders after our hook,
    # but the svgs are already built in on_env, so we can substitute them here
    plugin = config["plugins"].get("plantuml")
    if plugin is None:
        return html
    for key in plugin.uuid_regex.findall(html):
        html = plugin._replace(key, html)
    return html


def on_post_build(config, **kwargs):
    out_dir = os.path.join(config["site_dir"], OUT_DIR)
    pages_dir = os.path.join(out_dir, "pages")
    os.makedirs(pages_dir, exist_ok=True)

    for url, data in _pages.items():
        path = os.path.join(pages_dir, page_json_name(url))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    manifest = {
        "nav": [item for item in (_nav_item(i) for i in _nav.items) if item is not None],
        "redirects": _redirects,
        "pages": {url: page["title"] for url, page in _pages.items()},
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False)


def page_json_name(url: str) -> str:
    """ "mixers/ah/dlive/" -> "mixers/ah/dlive.json", "" -> "index.json" """
    url = url.strip("/")
    return (url or "index") + ".json"


_redirects: Dict[str, str] = {}


def _get_redirects(config, files) -> List[str]:
    _redirects.clear()
    plugin = config["plugins"].get("redirects")
    if plugin is None:
        return []
    for source, target in plugin.config["redirect_maps"].items():
        target_file = files.get_file_from_path(target)
        if target_file is None:
            continue
        source_url = re.sub(r"(index)?\.md$", "", source)
        if not source_url.endswith("/") and source_url:
            source_url += "/"
        _redirects[source_url] = target_file.url
    return list(_redirects.keys())


def _toc_item(item) -> dict:
    return {
        "title": item.title,
        "id": item.id,
        "level": item.level,
        "children": [_toc_item(child) for child in item.children],
    }


def _nav_item(item) -> Optional[dict]:
    if isinstance(item, Section):
        return {"title": item.title, "children": [c for c in (_nav_item(i) for i in item.children) if c]}
    if isinstance(item, Page):
        return {"title": item.title, "url": item.url}
    if isinstance(item, Link):
        return {"title": item.title, "href": item.url}
    return None


def _rewrite_urls(html: str, page_url: str) -> str:
    page_dir = page_url if page_url.endswith("/") or page_url == "" else posixpath.dirname(page_url) + "/"

    def replace(match: re.Match) -> str:
        prefix, url = match.group(1), match.group(2)
        if url == "" or url.startswith("/") or EXTERNAL_PATTERN.match(url):
            return match.group(0)
        return prefix + _to_page_or_asset(posixpath.join(page_dir, url)) + '"'

    return URL_ATTR_PATTERN.sub(replace, html)


def _to_page_or_asset(path: str) -> str:
    """
    Maps a path relative to the site root to the final absolute url
    """
    parts = urlsplit(path)
    clean = posixpath.normpath(parts.path) if parts.path else ""
    if clean == ".":
        clean = ""
    if parts.path.endswith("/") and clean:
        clean += "/"
    suffix = ("?" + parts.query if parts.query else "") + ("#" + parts.fragment if parts.fragment else "")

    page = clean
    if page.endswith("index.html"):
        page = page[:-len("index.html")]
    elif page and not page.endswith("/") and page + "/" in _page_urls:
        page += "/"
    if page in _page_urls:
        return PAGE_BASE + page + suffix
    return ASSET_BASE + clean + suffix
