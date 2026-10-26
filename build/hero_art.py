"""Hero illustration: a ring of five illustrated medallions around the Ψ mark.

Each scene is drawn in a 128x128 local box and clipped to a circle. No text.
"""
import math

BG = "#f3f8f1"
FLOOR = "#dfe7dc"
SKIN = "#f1c9a5"
SKIN2 = "#e3b58e"
HAIR = "#4a3426"
INK = "#2f3b47"
GREY = "#6b7784"
LIGHT = "#c9d3d9"
GREEN = "#006937"
DEEP = "#004128"
APPLE = "#87cd7d"
BLUE = "#2b5c8a"
GOLD = "#c9962b"


def scene_meg() -> str:
    return f"""
<rect width="128" height="128" fill="{BG}"/>
<rect y="110" width="128" height="18" fill="{FLOOR}"/>
<rect x="28" y="72" width="72" height="44" rx="8" fill="#b8c2c9"/>
<rect x="34" y="86" width="60" height="30" rx="6" fill="#9aa5ae"/>
<path d="M36 128 V102 a28 28 0 0 1 56 0 V128 Z" fill="{GREEN}"/>
<rect x="57" y="78" width="14" height="12" fill="{SKIN}"/>
<circle cx="64" cy="70" r="15" fill="{SKIN}"/>
<circle cx="58.5" cy="71" r="1.7" fill="{INK}"/><circle cx="69.5" cy="71" r="1.7" fill="{INK}"/>
<path d="M58 78 q6 4.5 12 0" stroke="{INK}" stroke-width="1.6" fill="none" stroke-linecap="round"/>
<path d="M30 4 h68 a7 7 0 0 1 7 7 v36 H23 V11 a7 7 0 0 1 7 -7 z" fill="#ffffff" stroke="{GREY}" stroke-width="2.2"/>
<rect x="30" y="12" width="68" height="4" rx="2" fill="#e4e9ec"/>
<rect x="30" y="22" width="68" height="4" rx="2" fill="#e4e9ec"/>
<path d="M23 47 h82 v4 a41 17 0 0 1 -82 0 z" fill="#f6f8f9" stroke="{GREY}" stroke-width="2.2"/>
<path d="M40 60 q24 10 48 0" stroke="{LIGHT}" stroke-width="1.5" fill="none"/>
<circle cx="44" cy="58" r="2" fill="{GREEN}"/><circle cx="54" cy="63" r="2" fill="{GREEN}"/><circle cx="64" cy="65" r="2" fill="{GREEN}"/><circle cx="74" cy="63" r="2" fill="{GREEN}"/><circle cx="84" cy="58" r="2" fill="{GREEN}"/>
<path d="M105 18 h8 q8 0 8 8 v40" stroke="{GREY}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M4 96 h6 l2 -5 l3 9 l3 -7 l2 3 h6" stroke="{GREEN}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
"""


def scene_touch_fmri() -> str:
    return f"""
<rect width="128" height="128" fill="{BG}"/>
<rect y="104" width="128" height="24" fill="{FLOOR}"/>
<rect x="0" y="18" width="66" height="86" rx="16" fill="#e9eef0" stroke="{GREY}" stroke-width="2.2"/>
<rect x="8" y="28" width="50" height="6" rx="3" fill="#d4dbe0"/>
<rect x="40" y="42" width="26" height="44" rx="13" fill="{INK}"/>
<rect x="46" y="48" width="14" height="32" rx="7" fill="#43515f"/>
<rect x="44" y="84" width="84" height="7" rx="3" fill="{LIGHT}" stroke="{GREY}" stroke-width="1.5"/>
<rect x="104" y="91" width="7" height="13" fill="#9aa5ae"/>
<circle cx="56" cy="72" r="8" fill="{SKIN}"/>
<path d="M48 70 a8 8 0 0 1 14 -4 l-2 2 a6 6 0 0 0 -10 3 z" fill="{HAIR}"/>
<circle cx="60" cy="72" r="1.2" fill="{INK}"/>
<rect x="62" y="70" width="42" height="14" rx="7" fill="{APPLE}"/>
<rect x="98" y="73" width="30" height="10" rx="5" fill="{APPLE}"/>
<rect x="70" y="77" width="28" height="6.5" rx="3.2" fill="{SKIN}"/>
<circle cx="99" cy="80" r="4.2" fill="{SKIN}"/>
<path d="M128 34 l-20 16" stroke="{BLUE}" stroke-width="10" stroke-linecap="round"/>
<path d="M110 48 l-13 15" stroke="{SKIN2}" stroke-width="7.5" stroke-linecap="round"/>
<ellipse cx="92" cy="69" rx="7.5" ry="5" fill="{SKIN2}" transform="rotate(-40 92 69)"/>
<path d="M88 72 l-3 3 M91 74 l-3 3 M94 76 l-3 3" stroke="{SKIN2}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M84 64 a9 9 0 0 0 -4 12" stroke="{GREEN}" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M80 60 a15 15 0 0 0 -6 19" stroke="{GREEN}" stroke-width="1.5" fill="none" opacity=".55" stroke-linecap="round"/>
<path d="M102 60 a9 9 0 0 1 4 12" stroke="{GREEN}" stroke-width="1.5" fill="none" stroke-linecap="round"/>
"""


def scene_drumming() -> str:
    wave = "q4 -11 8 0 t8 0 t8 0 t8 0"
    return f"""
<rect width="128" height="128" fill="{BG}"/>
<rect y="106" width="128" height="22" fill="{FLOOR}"/>
<path d="M10 24 {wave}" stroke="{GREEN}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M86 24 {wave}" stroke="{BLUE}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M48 24 h32" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 3" stroke-linecap="round"/>
<circle cx="30" cy="50" r="11" fill="{SKIN}"/>
<path d="M19 48 a11 11 0 0 1 22 0 v-3 a11 7 0 0 0 -22 0 z" fill="{HAIR}"/>
<circle cx="27" cy="51" r="1.4" fill="{INK}"/><circle cx="34" cy="51" r="1.4" fill="{INK}"/>
<path d="M27 56 q3 2.5 6 0" stroke="{INK}" stroke-width="1.3" fill="none" stroke-linecap="round"/>
<path d="M12 106 V80 a18 18 0 0 1 36 0 v26 z" fill="{GREEN}"/>
<path d="M40 78 l12 12" stroke="{SKIN}" stroke-width="5.5" stroke-linecap="round"/>
<path d="M44 94 h22 l-3 20 h-16 z" fill="#b5651d"/>
<path d="M47 102 h16" stroke="#8a4b12" stroke-width="1.2"/>
<ellipse cx="55" cy="94" rx="11" ry="4.2" fill="#f3e9d2" stroke="#8a4b12" stroke-width="1.2"/>
<circle cx="98" cy="50" r="11" fill="{SKIN2}"/>
<path d="M87 48 a11 11 0 0 1 22 0 v-3 a11 7 0 0 0 -22 0 z" fill="#2a1d14"/>
<circle cx="95" cy="51" r="1.4" fill="{INK}"/><circle cx="102" cy="51" r="1.4" fill="{INK}"/>
<path d="M95 56 q3 2.5 6 0" stroke="{INK}" stroke-width="1.3" fill="none" stroke-linecap="round"/>
<path d="M80 106 V80 a18 18 0 0 1 36 0 v26 z" fill="{BLUE}"/>
<path d="M88 78 l-12 12" stroke="{SKIN2}" stroke-width="5.5" stroke-linecap="round"/>
<path d="M62 94 h22 l-3 20 h-16 z" fill="#b5651d"/>
<path d="M65 102 h16" stroke="#8a4b12" stroke-width="1.2"/>
<ellipse cx="73" cy="94" rx="11" ry="4.2" fill="#f3e9d2" stroke="#8a4b12" stroke-width="1.2"/>
"""


def scene_rl() -> str:
    return f"""
<rect width="128" height="128" fill="{BG}"/>
<rect x="8" y="30" width="112" height="76" rx="6" fill="#edf2ee" stroke="{GREY}" stroke-width="3"/>
<path d="M44 30 v30 M44 78 v28 M80 30 v22 M80 70 v36 M8 68 h18" stroke="{GREY}" stroke-width="3" stroke-linecap="round"/>
<path d="M26 92 q12 -24 36 -24 t36 -22" stroke="{GREEN}" stroke-width="2.2" fill="none" stroke-dasharray="4 3" stroke-linecap="round"/>
<path d="M92 50 l6 -3 -1 7" stroke="{GREEN}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<ellipse cx="26" cy="92" rx="12" ry="8" fill="#9aa5ae"/>
<circle cx="37" cy="89" r="6" fill="#9aa5ae"/>
<circle cx="35" cy="82.5" r="3.2" fill="#f1b8c2" stroke="#9aa5ae" stroke-width="1"/>
<circle cx="40" cy="88" r="1.3" fill="{INK}"/>
<circle cx="43.5" cy="90.5" r="1.4" fill="#f1b8c2"/>
<path d="M14 94 q-9 4 -6 12" stroke="#9aa5ae" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M100 32 l4.4 9.2 10 1.4 -7.3 7 1.8 10 -8.9 -4.8 -8.9 4.8 1.8 -10 -7.3 -7 10 -1.4 z" fill="{GOLD}" stroke="#a67a1a" stroke-width="1"/>
<path d="M106 86 a12 12 0 1 1 -3 -9" stroke="{BLUE}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M104 73 l-1 6 -6 -1" stroke="{BLUE}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
"""


def scene_language() -> str:
    l1 = [(16, 36), (16, 58), (16, 80)]
    l2 = [(34, 28), (34, 48), (34, 68), (34, 88)]
    l3 = [(52, 44), (52, 72)]
    edges = []
    for a in l1:
        for b in l2:
            edges.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}"/>')
    for a in l2:
        for b in l3:
            edges.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}"/>')
    nodes = "".join(f'<circle cx="{x}" cy="{y}" r="3.8" fill="{BLUE}"/>' for x, y in l1 + l2 + l3)
    return f"""
<rect width="128" height="128" fill="{BG}"/>
<rect x="0" width="64" height="128" fill="#eef3f7"/>
<rect x="63" y="10" width="2" height="108" fill="{LIGHT}"/>
<g stroke="#9bb3cc" stroke-width="1.1">{''.join(edges)}</g>
{nodes}
<path d="M30 96 h22 a3 3 0 0 1 3 3 v10 a3 3 0 0 1 -3 3 h-11 l-5 5 v-5 h-6 a3 3 0 0 1 -3 -3 v-10 a3 3 0 0 1 3 -3 z" fill="#fff" stroke="{GREY}" stroke-width="1.3"/>
<path d="M41 99.5 l4.5 8 h-9 z" fill="{BLUE}"/>
<rect y="110" x="64" width="64" height="18" fill="{FLOOR}"/>
<circle cx="96" cy="54" r="16" fill="{SKIN}"/>
<path d="M95 38 q3 -9 9 -3" stroke="{HAIR}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<circle cx="90" cy="54" r="2.1" fill="{INK}"/><circle cx="102" cy="54" r="2.1" fill="{INK}"/>
<path d="M91 61 q5 4 10 0" stroke="{INK}" stroke-width="1.6" fill="none" stroke-linecap="round"/>
<circle cx="85" cy="59" r="2.6" fill="#f4a3a3" opacity=".7"/><circle cx="107" cy="59" r="2.6" fill="#f4a3a3" opacity=".7"/>
<path d="M80 110 V88 a16 14 0 0 1 32 0 v22 z" fill="{APPLE}"/>
<path d="M82 92 l-10 10 M110 92 l10 10" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>
<rect x="68" y="104" width="14" height="14" rx="2" fill="#fff" stroke="{GREY}" stroke-width="1.4"/><circle cx="75" cy="111" r="3.6" fill="{GREEN}"/>
<rect x="88" y="104" width="14" height="14" rx="2" fill="#fff" stroke="{GREY}" stroke-width="1.4"/><path d="M95 106.5 l4.6 8 h-9.2 z" fill="{BLUE}"/>
<rect x="108" y="104" width="14" height="14" rx="2" fill="#fff" stroke="{GREY}" stroke-width="1.4"/><rect x="111.5" y="107.5" width="7" height="7" fill="{GOLD}"/>
<path d="M104 22 h18 a3 3 0 0 1 3 3 v11 a3 3 0 0 1 -3 3 h-9 l-4 4 v-4 h-5 a3 3 0 0 1 -3 -3 v-11 a3 3 0 0 1 3 -3 z" fill="#fff" stroke="{GREY}" stroke-width="1.3"/>
<path d="M113 25.5 l4.5 8 h-9 z" fill="{BLUE}"/>
"""


def hero_art(aria_label: str) -> str:
    cx, cy, R, NR = 300, 300, 196, 70
    angles = [-90, -18, 54, 126, 198]
    scenes = [scene_meg(), scene_drumming(), scene_rl(), scene_language(), scene_touch_fmri()]
    nodes = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in angles]
    k = (2 * NR) / 128  # scale a 128px scene to the medallion diameter
    out = [f'<svg viewBox="0 0 600 600" role="img" aria-label="{aria_label}" xmlns="http://www.w3.org/2000/svg">']
    out.append(
        '<defs><radialGradient id="ringGlow" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0" stop-color="{APPLE}" stop-opacity=".32"/><stop offset="1" stop-color="{APPLE}" stop-opacity="0"/>'
        '</radialGradient><clipPath id="medal"><circle cx="64" cy="64" r="63"/></clipPath></defs>'
    )
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R + 80}" fill="url(#ringGlow)"/>')
    spokes = "".join(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>' for x, y in nodes)
    out.append(f'<g stroke="#c3dc87" stroke-width="2" stroke-dasharray="3 6">{spokes}</g>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{GREEN}" stroke-width="3"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="54" fill="#e7f2d3" stroke="{APPLE}" stroke-width="2"/>')
    out.append(f'<text x="{cx}" y="{cy + 24}" text-anchor="middle" font-family="Frank Ruhl Libre, Rubik, serif" font-weight="700" font-size="68" fill="{DEEP}">Ψ</text>')
    for (x, y), scene in zip(nodes, scenes):
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NR + 3}" fill="#fff" stroke="{GREEN}" stroke-width="3"/>')
        out.append(f'<g transform="translate({x - NR:.1f},{y - NR:.1f}) scale({k:.4f})" clip-path="url(#medal)">{scene}</g>')
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NR}" fill="none" stroke="{GREEN}" stroke-width="2"/>')
    out.append("</svg>")
    return "".join(out)
