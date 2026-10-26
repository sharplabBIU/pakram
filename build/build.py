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

HERO_ART = """
<svg viewBox="0 0 520 420" role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#004128"/><stop offset="1" stop-color="#006937"/>
    </linearGradient>
    <linearGradient id="g2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#006937"/><stop offset="1" stop-color="#87cd7d"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#87cd7d" stop-opacity=".45"/><stop offset="1" stop-color="#87cd7d" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="260" cy="210" r="190" fill="url(#glow)"/>
  <g fill="none" stroke="url(#g1)" stroke-width="1.5" opacity=".55">
    <path d="M110 300 C 140 160, 220 110, 300 120 S 440 200, 410 310"/>
    <path d="M130 120 C 200 180, 260 180, 330 130 S 420 100, 440 160"/>
    <path d="M90 210 C 160 240, 230 240, 300 300 S 400 330, 450 260"/>
    <path d="M160 360 C 200 300, 280 280, 350 350"/>
    <path d="M70 160 L 150 230 L 230 170 L 300 230 L 380 160 L 450 230"/>
    <path d="M120 60 L 200 120 L 270 70 L 340 120 L 430 60"/>
  </g>
  <g fill="url(#g1)">
    <circle cx="110" cy="300" r="7"/><circle cx="300" cy="120" r="9"/><circle cx="410" cy="310" r="7"/>
    <circle cx="130" cy="120" r="6"/><circle cx="330" cy="130" r="6"/><circle cx="440" cy="160" r="6"/>
    <circle cx="90" cy="210" r="6"/><circle cx="300" cy="300" r="8"/><circle cx="450" cy="260" r="6"/>
    <circle cx="160" cy="360" r="6"/><circle cx="350" cy="350" r="6"/>
    <circle cx="150" cy="230" r="5"/><circle cx="230" cy="170" r="5"/><circle cx="380" cy="160" r="5"/>
    <circle cx="200" cy="120" r="5"/><circle cx="270" cy="70" r="5"/><circle cx="340" cy="120" r="5"/><circle cx="430" cy="60" r="5"/>
  </g>
  <g fill="url(#g2)">
    <circle cx="260" cy="210" r="16"/><circle cx="70" cy="160" r="8"/><circle cx="450" cy="230" r="8"/><circle cx="120" cy="60" r="7"/>
  </g>
  <g fill="none" stroke="url(#g2)" stroke-width="2.2" stroke-linecap="round">
    <path d="M30 400 h40 l12 -22 l14 44 l14 -60 l14 70 l14 -42 l12 10 h60"/>
    <path d="M300 400 h40 l10 -14 l12 28 l12 -40 l12 46 l12 -28 l10 8 h60" opacity=".7"/>
  </g>
</svg>
"""


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
    nav_links = "".join(f'<a href="#{esc(h)}">{esc(t)}</a>' for h, t in c["nav"])
    facts = "".join(f'<div class="fact"><b>{esc(n)}</b><span>{t}</span></div>' for n, t in c["hero"]["facts"])
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
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;600;700&family=Heebo:wght@400;500;600;700&display=swap" rel="stylesheet">
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
<section class="hero">
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
    <div class="hero-art">{HERO_ART}</div>
  </div>
</section>
<div class="wrap facts-wrap">
  <div class="facts">{facts}</div>
  <div class="distinctions"><span class="label">{esc(c["hero"]["distinctions"]["label"])}</span><p>{c["hero"]["distinctions"]["text"]}</p></div>
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
