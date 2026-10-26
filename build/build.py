#!/usr/bin/env python3
"""Generate index.html (English) and he/index.html (Hebrew) from build/content.py.

Run from anywhere:  python3 build/build.py
"""
from __future__ import annotations

import html
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from content import SITE  # noqa: E402

import math


def hero_art(ring: dict) -> str:
    """Ring of five research symbols with the Ψ mark at the centre."""
    labels, bubble = ring["labels"], ring["bubble"]
    cx, cy, R, NR = 260, 224, 140, 36
    angles = [-90, -18, 54, 126, 198]
    nodes = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in angles]
    icons = [
        # touch: open hand
        '<path d="M11 21 V11 a2.2 2.2 0 0 1 4.4 0 V18 V7 a2.2 2.2 0 0 1 4.4 0 V18 V9 a2.2 2.2 0 0 1 4.4 0 V18 V12 a2.2 2.2 0 0 1 4.4 0 V24 a8 8 0 0 1 -8 8 H18.5 a8 8 0 0 1 -6.4 -3.2 L7.6 22.7 a2.2 2.2 0 0 1 3.4 -2.8 Z"/>',
        # social synchrony: two people joined by a wave
        '<circle cx="10.5" cy="10" r="4"/><circle cx="25.5" cy="10" r="4"/><path d="M3 20 a7.5 7.5 0 0 1 15 0"/><path d="M18 20 a7.5 7.5 0 0 1 15 0"/><path d="M4 29 q3.5 -6 7 0 t7 0 t7 0 t7 0"/>',
        # reinforcement learning: loop arrow with a reward star
        '<path d="M29 15 a11.5 11.5 0 1 0 -1.5 12"/><path d="M29 8 v7 h-7"/><path d="M18 13.5 l1.7 3.6 3.9 .5 -2.8 2.7 .7 3.9 -3.5 -1.9 -3.5 1.9 .7 -3.9 -2.8 -2.7 3.9 -.5 Z" fill="#004128" stroke="none"/>',
        # language development: speech bubble with letters
        '<path d="M7 6 h22 a3.5 3.5 0 0 1 3.5 3.5 v13 a3.5 3.5 0 0 1 -3.5 3.5 H17 l-7 6 v-6 H7 a3.5 3.5 0 0 1 -3.5 -3.5 v-13 A3.5 3.5 0 0 1 7 6 Z"/><text x="18" y="20" text-anchor="middle" font-size="11.5" font-weight="700" fill="#004128" stroke="none" font-family="Heebo, Rubik, sans-serif">' + bubble + '</text>',
        # MEG: head with a crown of sensors and a signal trace
        '<circle cx="18" cy="21" r="7.5"/><circle cx="18" cy="7.5" r="1.6" fill="#004128" stroke="none"/><circle cx="8.5" cy="11.5" r="1.6" fill="#004128" stroke="none"/><circle cx="27.5" cy="11.5" r="1.6" fill="#004128" stroke="none"/><circle cx="4.5" cy="20" r="1.6" fill="#004128" stroke="none"/><circle cx="31.5" cy="20" r="1.6" fill="#004128" stroke="none"/><path d="M4 33 h6 l2 -4 l3 7 l3 -6 l2 3 h12"/>',
    ]
    spokes = "".join(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>' for x, y in nodes)
    out = [f'<svg viewBox="0 0 520 440" role="img" aria-label="{esc(", ".join(labels))}" xmlns="http://www.w3.org/2000/svg">']
    out.append('<defs><radialGradient id="ringGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#87cd7d" stop-opacity=".35"/><stop offset="1" stop-color="#87cd7d" stop-opacity="0"/></radialGradient></defs>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R + 60}" fill="url(#ringGlow)"/>')
    out.append(f'<g stroke="#c3dc87" stroke-width="1.5" stroke-dasharray="3 5">{spokes}</g>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#006937" stroke-width="2.5"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="#e7f2d3" stroke="#87cd7d" stroke-width="1.5"/>')
    out.append(f'<text x="{cx}" y="{cy + 21}" text-anchor="middle" font-family="Frank Ruhl Libre, Rubik, serif" font-weight="700" font-size="60" fill="#004128">Ψ</text>')
    for i, ((x, y), icon, label) in enumerate(zip(nodes, icons, labels)):
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NR}" fill="#fff" stroke="#006937" stroke-width="2.5"/>')
        out.append(f'<g transform="translate({x - 18:.1f},{y - 18:.1f})" fill="none" stroke="#004128" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon}</g>')
        words = label.split(" ")
        if i == 0:      # top
            tx, ty, anchor = cx, y - NR - 14, "middle"; lines = [label]
        elif i == 1:    # right
            tx, ty, anchor = x + NR + 10, y + (5 if len(words) == 1 else -3), "start"; lines = words if len(words) == 2 else [label]
        elif i == 4:    # left
            tx, ty, anchor = x - NR - 10, y + (5 if len(words) == 1 else -3), "end"; lines = words if len(words) == 2 else [label]
        else:           # bottom pair
            tx, ty, anchor = x, y + NR + 18, "middle"; lines = words if len(words) == 2 else [label]
        tspans = "".join(f'<tspan x="{tx:.1f}" dy="{0 if k == 0 else 16}">{esc(w)}</tspan>' for k, w in enumerate(lines))
        out.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}" font-size="13.5" font-weight="600" fill="#2f3b47" font-family="Heebo, Rubik, system-ui, sans-serif">{tspans}</text>')
    out.append("</svg>")
    return "".join(out)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def render_list(items: list[str], cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def render_faculty(members: list[dict], labels: dict) -> str:
    out = []
    for m in members:
        kw_i = m.get("key_work", 0)
        key_work = m["works"][kw_i]
        rest_works = [w for i, w in enumerate(m["works"]) if i != kw_i]
        if m["awards"]:
            ka_i = m.get("key_award", 0)
            ka_label, key_award = labels["award"], m["awards"][ka_i]
            rest_awards = [a for i, a in enumerate(m["awards"]) if i != ka_i]
        else:
            ka_label, key_award, rest_awards = labels["highlight"], m.get("highlight", ""), []
        key = f'<dl class="key"><dt>{esc(labels["key_work"])}</dt><dd class="pubs">{key_work}</dd>'
        if key_award:
            key += f'<dt>{esc(ka_label)}</dt><dd>{key_award}</dd>'
        key += "</dl>"
        more = ""
        if rest_works:
            more += f'<h4>{esc(labels["more_works"])}</h4>{render_list(rest_works, "pubs")}'
        if rest_awards:
            more += f'<h4>{esc(labels["more_awards"])}</h4>{render_list(rest_awards)}'
        details = (
            f'<details><summary><span class="more">{esc(labels["read_more"])}</span>'
            f'<span class="less">{esc(labels["show_less"])}</span></summary><div>{more}</div></details>'
            if more else ""
        )
        links = "".join(
            f'<a href="{esc(l["url"])}" target="_blank" rel="noopener"{" class=\"primary\"" if l.get("primary") else ""}>{esc(l["label"])}</a>'
            for l in m["links"]
        )
        out.append(
            f"""<article class="card prof" id="{esc(m["id"])}">
  <div class="avatar" aria-hidden="true">{esc(m["initials"])}</div>
  <div>
    <h3>{esc(m["name"])}</h3>
    <div class="role">{esc(m["role"])}</div>
    <p class="summary">{m["summary"]}</p>
    {key}
    {details}
    <div class="links">{links}</div>
  </div>
</article>"""
        )
    return "\n".join(out)


def render_page(lang: str) -> str:
    c = SITE[lang]
    other = "he" if lang == "en" else "en"
    base = "" if lang == "en" else "../"
    other_href = "he/" if lang == "en" else "../"
    dir_attr = "rtl" if lang == "he" else "ltr"
    fonts_url = (
        "https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700;800&family=Assistant:wght@400;500;600;700&display=swap"
        if lang == "he"
        else "https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;600;700&family=Heebo:wght@400;500;600;700&display=swap"
    )
    nav_links = "".join(f'<a href="#{esc(h)}">{esc(t)}</a>' for h, t in c["nav"])
    facts = "".join(f'<div class="fact"><b>{esc(n)}</b><span>{t}</span></div>' for n, t in c["hero"]["facts"])
    def award_box(a):
        big = f'<a href="{esc(a["url"])}" target="_blank" rel="noopener">{esc(a["big"])}</a>' if a.get("url") else esc(a["big"])
        cls = "fact fact-wide" if a.get("wide") else "fact"
        return f'<div class="{cls}"><b>{big}</b><span>{a["label"]}</span></div>'
    awards = "".join(award_box(a) for a in c["hero"]["awards"])
    pills = "".join(f"<li>{esc(p)}</li>" for p in c["about"]["pills"])

    def paras(ps):
        return "".join(f"<p>{p}</p>" for p in ps)

    mu = c["multi"]
    pw = c["pathways"]
    dr = c["directions"]
    ea = c["emotion_ai"]
    fa = c["faculty"]
    pa = c["path"]
    ap = c["apply"]
    ft = c["footer"]

    pillars = "".join(f'<div class="pillar"><h3>{esc(pl["title"])}</h3><p>{pl["text"]}</p></div>' for pl in mu["pillars"])
    steps = "".join(f'<div class="step"><h3>{esc(s["title"])}</h3><p>{s["text"]}</p></div>' for s in pa["steps"])
    directions = "".join(f'<article class="direction"><span class="who">{esc(d["who"])}</span><h3>{esc(d["title"])}</h3><p>{d["text"]}</p></article>' for d in dr["items"])
    reqs = render_list(ap["reqs"])
    contact_rows = "".join(f"<dt>{esc(k)}</dt><dd>{v}</dd>" for k, v in ap["contact"])
    footer_links = "".join(f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a>' for t, u in ft["links"])

    return f"""<!doctype html>
<html lang="{lang}" dir="{dir_attr}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(c["meta"]["title"])}</title>
<meta name="description" content="{esc(c["meta"]["description"])}">
<meta property="og:title" content="{esc(c["meta"]["title"])}">
<meta property="og:description" content="{esc(c["meta"]["description"])}">
<meta property="og:type" content="website">
<link rel="alternate" hreflang="en" href="{base}./">
<link rel="alternate" hreflang="he" href="{base}he/">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts_url}" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<a class="sr-only" href="#main">{esc(c["skip"])}</a>
<header class="site-header">
  <div class="wrap">
    <div class="header-row">
      <a class="brand" href="{base}{'' if lang == 'en' else 'he/'}">
        <span class="brand-mark" aria-hidden="true">{esc(c["brand"]["mark"])}</span>
        <span class="brand-text">{esc(c["brand"]["name"])}<small>{esc(c["brand"]["sub"])}</small></span>
      </a>
      <nav class="nav" aria-label="{esc(c["nav_label"])}">{nav_links}</nav>
      <div class="lang-tabs" role="tablist" aria-label="{esc(c["lang_label"])}">
        <a href="{'' if lang == 'en' else '../'}" hreflang="en" lang="en" aria-current="{'true' if lang == 'en' else 'false'}">English</a>
        <a href="{'he/' if lang == 'en' else ''}" hreflang="he" lang="he" aria-current="{'true' if lang == 'he' else 'false'}">עברית</a>
      </div>
      <button class="menu-btn" aria-expanded="false" aria-controls="mobile-nav" aria-label="{esc(c["menu_label"])}">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
    <nav class="mobile-nav" id="mobile-nav" aria-label="{esc(c["nav_label"])}">{nav_links}</nav>
  </div>
</header>

<main id="main">
<section class="hero" id="top">
  <div class="wrap">
    <div>
      <span class="kicker">{esc(c["hero"]["kicker"])}</span>
      <h1>{c["hero"]["title"]}</h1>
      <p class="lede">{c["hero"]["lede"]}</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#about">{esc(c["hero"]["cta_primary"])}</a>
        <a class="btn btn-secondary" href="#apply">{esc(c["hero"]["cta_secondary"])}</a>
      </div>
    </div>
    <div class="hero-art">{hero_art(c["hero"]["ring"])}</div>
  </div>
</section>
<div class="wrap facts-wrap">
  <div class="facts">{facts}</div>
  <h2 class="sr-only">{esc(c["hero"]["awards_label"])}</h2>
  <div class="facts facts-awards">{awards}</div>
</div>

<section class="block" id="about">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(c["about"]["kicker"])}</span>
      <h2>{esc(c["about"]["title"])}</h2>
    </div>
    <div class="prose">{paras(c["about"]["paras"])}</div>
    <ul class="pill-list" aria-label="{esc(c["about"]["pills_label"])}">{pills}</ul>
  </div>
</section>

<section class="block alt" id="multidisciplinary">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(mu["kicker"])}</span>
      <h2>{esc(mu["title"])}</h2>
    </div>
    <div class="prose">{paras(mu["paras"])}</div>
    <div class="pillars">{pillars}</div>
  </div>
</section>

<section class="block" id="pathways">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(pw["kicker"])}</span>
      <h2>{esc(pw["title"])}</h2>
      <p class="lede">{pw["lede"]}</p>
    </div>
    <div class="grid-2">
      <div class="card">
        <span class="tag tag-industry">{esc(pw["industry"]["tag"])}</span>
        <h3>{esc(pw["industry"]["title"])}</h3>
        <p>{pw["industry"]["intro"]}</p>
        {render_list(pw["industry"]["bullets"])}
        <p style="margin-top:1em;color:var(--ink-3)">{pw["industry"]["outro"]}</p>
      </div>
      <div class="card">
        <span class="tag tag-academia">{esc(pw["academia"]["tag"])}</span>
        <h3>{esc(pw["academia"]["title"])}</h3>
        <p>{pw["academia"]["intro"]}</p>
        {render_list(pw["academia"]["bullets"])}
        <p style="margin-top:1em;color:var(--ink-3)">{pw["academia"]["outro"]}</p>
      </div>
    </div>
  </div>
</section>

<section class="block alt" id="directions">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(dr["kicker"])}</span>
      <h2>{esc(dr["title"])}</h2>
      <p class="lede">{dr["lede"]}</p>
    </div>
    <div class="directions">{directions}</div>
  </div>
</section>

<section class="block" id="emotion-ai">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(ea["kicker"])}</span>
      <h2>{esc(ea["title"])}</h2>
    </div>
    <div class="prose">{paras(ea["paras"])}</div>
  </div>
</section>

<section class="block alt" id="faculty">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(fa["kicker"])}</span>
      <h2>{esc(fa["title"])}</h2>
      <p class="lede">{fa["lede"]}</p>
    </div>
    <div class="faculty-grid">{render_faculty(fa["members"], fa["labels"])}</div>
  </div>
</section>

<section class="block" id="your-path">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(pa["kicker"])}</span>
      <h2>{esc(pa["title"])}</h2>
      <p class="lede">{pa["lede"]}</p>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="block alt" id="apply">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{esc(ap["kicker"])}</span>
      <h2>{esc(ap["title"])}</h2>
      <p class="lede">{ap["intro"]}</p>
    </div>
    <div class="apply-grid">
      <div class="card">
        <h3>{esc(ap["reqs_title"])}</h3>
        {reqs}
        <p style="margin-top:1em">{ap["registration"]}</p>
        <a class="btn btn-primary" href="{esc(ap["official_url"])}" target="_blank" rel="noopener">{esc(ap["official_label"])}</a>
      </div>
      <div class="card contact">
        <h3>{esc(ap["contact_title"])}</h3>
        <dl>{contact_rows}</dl>
      </div>
    </div>
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <div>
      <div>{esc(ft["line1"])}</div>
      <div>{ft["line2"]}</div>
      <div style="margin-top:8px">{ft["disclaimer"]}</div>
    </div>
    <div class="footer-links">{footer_links}</div>
  </div>
</footer>
<script src="{base}assets/site.js" defer></script>
</body>
</html>
"""


def main() -> None:
    targets = {"en": os.path.join(ROOT, "index.html"), "he": os.path.join(ROOT, "he", "index.html")}
    for lang, path in targets.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_page(lang))
        print(f"wrote {os.path.relpath(path, ROOT)} ({os.path.getsize(path)} bytes)")


if __name__ == "__main__":
    main()
