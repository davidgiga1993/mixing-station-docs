"""
Exports the rendered html pages as JSON

Relative links are rewritten to absolute:
- Links to other pages: MS_SPA_PAGE_BASE + page url
- Everything else: MS_SPA_ASSET_BASE + file path

All pages are also merged in a print.json file
"""

import json
import os
import posixpath
import re
from html import escape
from typing import Dict, List, Optional
from urllib.parse import urlsplit

from properdocs.structure.nav import Link, Section
from properdocs.structure.pages import Page

PAGE_BASE = os.environ.get("MS_SPA_PAGE_BASE", "/docs/")
ASSET_BASE = os.environ.get("MS_SPA_ASSET_BASE", "/docs-content/")
OUT_DIR = "_spa"

# Poor man href "parser" (insert stackoverflow parse html with regex meme here)
URL_ATTR_PATTERN = re.compile(r'(\s(?:href|src|poster)=")([^"]*)"')
EXTERNAL_PATTERN = re.compile(r"^([a-z][a-z0-9+.-]*:|//|#)", re.I)  # Matches a url scheme
ID_ATTR_PATTERN = re.compile(r'(\s(?:id|for)=")([^"]*)"')
HREF_ATTR_PATTERN = re.compile(r'(\shref=")([^"]*)"')

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
    # mkdocs_puml only replaces its placeholders after this hook,
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
        path = os.path.join(pages_dir, tp_page_json_name(url))
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

    with open(os.path.join(out_dir, "print.json"), "w", encoding="utf-8") as f:
        json.dump(_print_page(config), f, ensure_ascii=False)


def _print_page(config) -> dict:
    """
    Combines all pages into a single page.
    Ids are prefixed with the page anchor to make them unique and links
    to other pages are rewritten to point to the page inside the print page
    """
    html: List[str] = []
    toc: List[dict] = []
    added = set()

    def add_page(url: str, level: int) -> Optional[dict]:
        if url in added or url not in _pages:
            return None
        added.add(url)
        page = _pages[url]
        anchor = _to_print_anchor(url)
        html.append(
            '<section class="print-page" id="%s">%s</section>' % (anchor, _rewrite_print_html(page["html"], url)))
        return {
            "title": page["title"],
            "id": anchor,
            "level": level,
            "children": [_print_toc_item(item, url) for item in page["toc"]],
        }

    def add_nav(items, level: int) -> List[dict]:
        result = []
        for item in items:
            if isinstance(item, Section):
                anchor = "section-" + str(len(html))
                html.append('<h1 class="print-section-title" id="%s">%s</h1>' % (anchor, escape(item.title)))
                result.append(
                    {"title": item.title, "id": anchor, "level": level, "children": add_nav(item.children, level + 1)})
            elif isinstance(item, Page):
                entry = add_page(item.url, level)
                if entry is not None:
                    result.append(entry)
        return result

    toc.extend(add_nav(_nav.items, 1))
    # Pages which are not part of the nav
    for url in sorted(_pages.keys()):
        entry = add_page(url, 1)
        if entry is not None:
            toc.append(entry)

    return {
        "url": "print/",
        "title": config["site_name"],
        "description": None,
        "toc": toc,
        "html": "\n".join(html),
    }


def _to_print_anchor(url: str) -> str:
    """ "mixers/ah/dlive/" -> "mixers-ah-dlive", "" -> "index" """
    return url.strip("/").replace("/", "-") or "index"


def _print_toc_item(item: dict, page_url: str) -> dict:
    return {
        "title": item["title"],
        "id": _to_print_anchor(page_url) + "--" + item["id"],
        "level": item["level"],
        "children": [_print_toc_item(child, page_url) for child in item["children"]],
    }


def _rewrite_print_html(html: str, page_url: str) -> str:
    prefix = _to_print_anchor(page_url) + "--"

    def replace_id(match: re.Match) -> str:
        return match.group(1) + prefix + match.group(2) + '"'

    def replace_href(match: re.Match) -> str:
        attr, url = match.group(1), match.group(2)
        if url.startswith("#") and len(url) > 1:
            return attr + "#" + prefix + url[1:] + '"'
        if url.startswith(PAGE_BASE):
            parts = urlsplit(url[len(PAGE_BASE):])
            if parts.path in _pages and not parts.query:
                anchor = _to_print_anchor(parts.path)
                if parts.fragment:
                    anchor += "--" + parts.fragment
                return attr + "#" + anchor + '"'
        return match.group(0)

    html = ID_ATTR_PATTERN.sub(replace_id, html)
    return HREF_ATTR_PATTERN.sub(replace_href, html)


def tp_page_json_name(url: str) -> str:
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
