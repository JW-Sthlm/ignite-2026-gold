"""Build index.html from ignite-2026-digest.md and prompt.md.

The digest file and the prompt file are the single sources of truth. Run this after
editing either of them:

    python scripts/build_site.py
"""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DIGEST = ROOT / "ignite-2026-digest.md"
PROMPT = ROOT / "prompt.md"
TEMPLATE = ROOT / "scripts" / "template.html"
OUT = ROOT / "index.html"

BOOK_OF_NEWS = "https://news.microsoft.com/events/ignite/2026/book-of-news/"

GROUPS = {
    1: {"short": "People", "color": "gold"},
    2: {"short": "Know-how", "color": "green"},
    3: {"short": "Systems", "color": "teal"},
    4: {"short": "Operations", "color": "sky"},
    5: {"short": "Building AI", "color": "orange"},
    6: {"short": "Trust and cost", "color": "pink"},
}

# The lens section on the page already carries the group 3 quote and survey numbers.
GROUP_SITE_INTRO = {
    3: "Where agents meet the applications and data you already have.",
}

AUDIENCES = [
    ("everyone", "Every employee"),
    ("leaders", "Leaders"),
    ("it", "IT and operations"),
    ("dev", "Developers"),
    ("data", "Data and finance"),
    ("security", "Security"),
    ("business", "Business teams"),
]

# Hand-curated from each item's "For" line.
ITEM_AUDIENCE = {
    "1.1": "everyone", "1.2": "everyone", "1.3": "business it", "1.4": "everyone it",
    "1.5": "everyone", "1.6": "everyone", "1.7": "business",
    "2.1": "leaders it", "2.2": "leaders it", "2.3": "data business",
    "3.1": "leaders it dev", "3.2": "dev", "3.3": "it data", "3.4": "leaders business it",
    "3.5": "it business", "3.6": "it",
    "4.1": "it", "4.2": "data it", "4.3": "it", "4.4": "it dev",
    "5.1": "dev", "5.2": "business data", "5.3": "dev",
    "6.1": "leaders", "6.2": "it security", "6.3": "security", "6.4": "security it", "6.5": "security it",
}

# Hand-curated from each item's "Status" line. The full status sentence is always shown too.
ITEM_CHIPS = {
    "1.1": ["Rolling out", "GA"], "1.2": ["GA"], "1.3": ["Frontier", "GA in December"],
    "1.4": ["Frontier", "Rolling out"], "1.5": ["Frontier"], "1.6": ["Private preview", "Frontier"],
    "1.7": ["GA", "Preview"],
    "2.1": ["GA"], "2.2": ["Frontier"], "2.3": ["GA", "Preview"],
    "3.1": ["GA", "Preview"], "3.2": ["GA", "Preview"], "3.3": ["GA", "Preview"],
    "3.4": ["Rolling out", "GA"], "3.5": ["Available", "Preview"], "3.6": ["Preview", "Early access"],
    "4.1": ["GA", "Preview", "Private preview"], "4.2": ["GA", "Preview"], "4.3": ["GA"], "4.4": ["Preview"],
    "5.1": ["GA", "Preview"], "5.2": ["GA", "Preview"], "5.3": ["GA"],
    "6.1": ["Preview", "Frontier"], "6.2": ["GA", "Preview", "Private preview"], "6.3": ["GA"],
    "6.4": ["GA", "Preview"], "6.5": ["Preview in Jan 2027"],
}

CHIP_CLASS = {
    "GA": "chip-ga",
    "Available": "chip-ga",
    "GA in December": "chip-soon",
    "Preview in Jan 2027": "chip-soon",
}

URL_RE = re.compile(r"https?://[^\s,)]+")


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def link_label(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.removeprefix("www.")
    if host == "aka.ms":
        return f"aka.ms{parsed.path}"
    if url.rstrip("/") == BOOK_OF_NEWS.rstrip("/"):
        return "Book of News"
    if host == "techcommunity.microsoft.com":
        return "Tech Community"
    return host


def linkify(text: str) -> str:
    """Escape text and turn bare URLs into links."""
    out, pos = [], 0
    for match in URL_RE.finditer(text):
        out.append(esc(text[pos:match.start()]))
        url = match.group(0).rstrip(".")
        out.append(f'<a href="{esc(url)}">{esc(link_label(url))}</a>')
        pos = match.start() + len(url)
    out.append(esc(text[pos:]))
    return "".join(out)


def parse_prompt() -> dict[str, str]:
    text = PROMPT.read_text(encoding="utf-8")
    prompts = {}
    for heading, key in (("## English", "en"), ("## Svenska", "sv")):
        start = text.index(heading)
        block = re.search(r"```text\n(.*?)\n```", text[start:], re.S)
        prompts[key] = block.group(1)
    return prompts


def parse_digest() -> list[dict]:
    groups: list[dict] = []
    group = item = None
    for raw in DIGEST.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        group_match = re.match(r"^## (\d)\. (.+)$", line)
        item_match = re.match(r"^### (\d\.\d) (.+)$", line)
        field_match = re.match(r"^- \*\*(.+?):\*\* (.+)$", line)
        if group_match:
            group = {"n": int(group_match.group(1)), "title": group_match.group(2), "intro": [], "items": []}
            groups.append(group)
            item = None
        elif line.startswith("## "):
            group = item = None
        elif item_match and group:
            item = {"id": item_match.group(1), "title": item_match.group(2), "fields": {}}
            group["items"].append(item)
        elif field_match and item:
            item["fields"][field_match.group(1)] = field_match.group(2)
        elif group and not item and line and not line.startswith("---"):
            group["intro"].append(line)
    return groups


def render_prompt(text: str) -> str:
    lines = []
    for i, line in enumerate(text.split("\n")):
        if i == 0:
            lines.append(f'<span class="p-title">{esc(line)}</span>')
        elif re.fullmatch(r"[A-ZÅÄÖ ]{3,}", line):
            lines.append(f'<span class="p-head">{esc(line)}</span>')
        else:
            lines.append(esc(line))
    return "\n".join(lines)


def render_sources(value: str) -> str:
    urls = [u.rstrip(".") for u in URL_RE.findall(value)]
    if "Book of News" in value and not any(BOOK_OF_NEWS.rstrip("/") in u for u in urls):
        urls.append(BOOK_OF_NEWS)
    return "".join(
        f'<a class="src" href="{esc(u)}">{esc(link_label(u))}<span aria-hidden="true"> \u2197</span></a>'
        for u in urls
    )


def render_item(item: dict) -> str:
    f = item["fields"]
    iid = item["id"]
    chips = "".join(
        f'<li class="chip {CHIP_CLASS.get(c, "")}">{esc(c)}</li>' for c in ITEM_CHIPS[iid]
    )
    deeper = (
        f'<p class="deeper"><span class="k">Go deeper</span> {linkify(f["Go deeper"])}</p>'
        if "Go deeper" in f else ""
    )
    return f"""
      <article class="item" id="i{iid.replace('.', '-')}" data-aud="{ITEM_AUDIENCE[iid]}">
        <div class="item-top">
          <span class="item-id">{iid}</span>
          <h4>{esc(item['title'])}</h4>
          <ul class="chips" aria-label="Status">{chips}</ul>
        </div>
        <p class="what">{linkify(f['What it is'])}</p>
        <p class="why"><span class="k">Why it matters</span> {linkify(f['Why it matters'])}</p>
        {deeper}
        <dl class="meta">
          <div><dt>Status</dt><dd>{linkify(f['Status'])}</dd></div>
          <div><dt>For</dt><dd>{esc(f['For'])}</dd></div>
        </dl>
        <p class="sources">{render_sources(f['Source'])}</p>
      </article>"""


def render_groups(groups: list[dict]) -> str:
    parts = []
    for g in groups:
        meta = GROUPS[g["n"]]
        intro = GROUP_SITE_INTRO.get(g["n"], " ".join(g["intro"]).strip())
        intro_html = f'<p class="group-intro">{linkify(intro)}</p>' if intro else ""
        items = "".join(render_item(i) for i in g["items"])
        parts.append(f"""
    <section class="group" id="g{g['n']}" style="--c: var(--{meta['color']})" aria-labelledby="g{g['n']}-title">
      <header class="group-head">
        <span class="group-lane" aria-hidden="true"></span>
        <h3 id="g{g['n']}-title"><span class="group-n">{g['n']}</span>{esc(g['title'])}</h3>
        {intro_html}
      </header>
      <div class="items">{items}
      </div>
    </section>""")
    return "".join(parts)


def render_jump(groups: list[dict]) -> str:
    return "".join(
        f'<a href="#g{g["n"]}" style="--c: var(--{GROUPS[g["n"]]["color"]})">'
        f'<span class="dot" aria-hidden="true"></span>{esc(GROUPS[g["n"]]["short"])}</a>'
        for g in groups
    )


def render_filters() -> str:
    buttons = ['<button type="button" data-f="all" aria-pressed="true">Everything</button>']
    buttons += [
        f'<button type="button" data-f="{key}" aria-pressed="false">{esc(label)}</button>'
        for key, label in AUDIENCES
    ]
    return "".join(buttons)


def main() -> None:
    groups = parse_digest()
    count = sum(len(g["items"]) for g in groups)
    missing = [i["id"] for g in groups for i in g["items"] if i["id"] not in ITEM_CHIPS or i["id"] not in ITEM_AUDIENCE]
    if missing:
        raise SystemExit(f"Add chips and audience for: {', '.join(missing)}")
    prompts = parse_prompt()
    page = TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "{{PROMPT_EN}}": render_prompt(prompts["en"]),
        "{{PROMPT_SV}}": render_prompt(prompts["sv"]),
        "{{NEWS_GROUPS}}": render_groups(groups),
        "{{JUMP}}": render_jump(groups),
        "{{FILTERS}}": render_filters(),
        "{{ITEM_COUNT}}": str(count),
    }
    for token, value in replacements.items():
        page = page.replace(token, value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", page)
    if leftover:
        raise SystemExit(f"Unreplaced tokens: {leftover}")
    if "\u2014" in page:
        raise SystemExit("Em dash found in the generated page.")
    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT.name}: {count} items in {len(groups)} groups, {len(page):,} characters.")


if __name__ == "__main__":
    main()
