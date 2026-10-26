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
    sans = "Heebo, Rubik, system-ui, sans-serif"
    return f"""
<rect width="128" height="128" fill="{BG}"/>
<rect x="18" y="8" width="92" height="30" rx="7" fill="#fff" stroke="{GREEN}" stroke-width="2"/>
<text x="30" y="28" font-size="12.5" font-weight="700" fill="{DEEP}" font-family="{sans}">Agent</text>
<text x="92" y="32" text-anchor="middle" font-size="24" font-weight="700" fill="{DEEP}" font-family="Frank Ruhl Libre, serif">Ψ</text>
<path d="M85 31 c8 -2 8 -6 0 -8 c-8 -2 -8 -6 1 -8" stroke="{GOLD}" stroke-width="1.9" fill="none" stroke-linecap="round"/>
<circle cx="87" cy="14.5" r="1.5" fill="{GOLD}"/>
<rect x="14" y="90" width="100" height="30" rx="7" fill="#fff" stroke="{GREEN}" stroke-width="2"/>
<text x="64" y="110" text-anchor="middle" font-size="12" font-weight="700" fill="{DEEP}" font-family="{sans}">Environment</text>
<path d="M104 38 V84" stroke="{BLUE}" stroke-width="2.2" fill="none"/>
<path d="M99 79 l5 6 5 -6" stroke="{BLUE}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M24 90 V44" stroke="{GREEN}" stroke-width="2.2" fill="none"/>
<path d="M19 49 l5 -6 5 6" stroke="{GREEN}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="97" y="52" text-anchor="end" font-size="10.5" font-style="italic" fill="{BLUE}" font-family="{sans}">a</text>
<text x="31" y="52" font-size="10.5" font-style="italic" fill="{GREEN}" font-family="{sans}">s, r</text>
<text x="64" y="68" text-anchor="middle" font-size="10.5" font-style="italic" fill="{INK}" font-family="{sans}">δ = r + γV(s′) − V(s)</text>
<text x="64" y="81" text-anchor="middle" font-size="9.5" font-style="italic" fill="{INK}" font-family="{sans}">V(s) ← V(s) + αδ</text>
"""


def scene_language(word: str) -> str:
    sans = "Heebo, Rubik, system-ui, sans-serif"
    return f"""
<rect width="128" height="128" fill="{BG}"/>
<rect y="106" width="128" height="22" fill="{FLOOR}"/>
<ellipse cx="92" cy="78" rx="33" ry="30" fill="#fff" stroke="{GREEN}" stroke-width="1.6" stroke-dasharray="4 3"/>
<circle cx="28" cy="58" r="13" fill="{SKIN}"/>
<path d="M15 56 a13 13 0 0 1 26 0 v-4 a13 8 0 0 0 -26 0 z" fill="{HAIR}"/>
<circle cx="23.5" cy="59" r="1.7" fill="{INK}"/><circle cx="32.5" cy="59" r="1.7" fill="{INK}"/>
<path d="M24 65 q4 3 8 0" stroke="{INK}" stroke-width="1.4" fill="none" stroke-linecap="round"/>
<path d="M12 106 V84 a16 16 0 0 1 32 0 v22 z" fill="{APPLE}"/>
<path d="M40 84 l20 -12" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>
<circle cx="61" cy="71" r="3" fill="{SKIN}"/>
<path d="M28 12 h34 a4 4 0 0 1 4 4 v13 a4 4 0 0 1 -4 4 h-18 l-6 6 v-6 h-10 a4 4 0 0 1 -4 -4 v-13 a4 4 0 0 1 4 -4 z" fill="#fff" stroke="{GREY}" stroke-width="1.4"/>
<text x="45" y="26" text-anchor="middle" font-size="11.5" font-weight="700" fill="{DEEP}" font-family="{sans}">{word}</text>
<path d="M66 22 q24 4 26 28" stroke="{BLUE}" stroke-width="1.3" fill="none" stroke-dasharray="3 2"/>
<path d="M66 24 q10 30 6 56" stroke="{BLUE}" stroke-width="1.3" fill="none" stroke-dasharray="3 2"/>
<path d="M66 22 q40 10 40 60" stroke="{BLUE}" stroke-width="1.3" fill="none" stroke-dasharray="3 2"/>
<rect x="78" y="54" width="26" height="13" rx="6.5" fill="#a0683a"/>
<circle cx="106" cy="56" r="6.5" fill="#a0683a"/>
<ellipse cx="102.5" cy="51" rx="2.3" ry="3.8" fill="#7a4a24"/>
<circle cx="108.5" cy="55" r="1.1" fill="{INK}"/>
<circle cx="111" cy="58" r="1.3" fill="{INK}"/>
<path d="M78 58 l-6 -5" stroke="#a0683a" stroke-width="2.6" stroke-linecap="round"/>
<rect x="81" y="66" width="3.2" height="7" fill="#a0683a"/><rect x="97" y="66" width="3.2" height="7" fill="#a0683a"/>
<rect x="64" y="86" width="20" height="10" rx="5" fill="#fff" stroke="{INK}" stroke-width="1.1"/>
<circle cx="85" cy="87" r="5" fill="#fff" stroke="{INK}" stroke-width="1.1"/>
<ellipse cx="82" cy="84" rx="1.6" ry="3" fill="{INK}"/>
<circle cx="72" cy="90" r="2.2" fill="{INK}"/><circle cx="79" cy="92" r="1.6" fill="{INK}"/>
<circle cx="87" cy="86" r=".9" fill="{INK}"/>
<rect x="66" y="95" width="2.6" height="6" fill="{INK}"/><rect x="78" y="95" width="2.6" height="6" fill="{INK}"/>
<rect x="96" y="88" width="17" height="9" rx="4.5" fill="{INK}"/>
<circle cx="114" cy="88" r="4.5" fill="{INK}"/>
<ellipse cx="111" cy="84.5" rx="1.5" ry="2.6" fill="{INK}"/>
<circle cx="115.8" cy="87" r=".9" fill="#fff"/>
<path d="M96 91 l-5 -3" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
<rect x="98" y="96" width="2.6" height="6" fill="{INK}"/><rect x="108" y="96" width="2.6" height="6" fill="{INK}"/>
"""


def hero_art(lang: str, aria_label: str) -> str:
    cx, cy, R, NR = 300, 300, 196, 70
    angles = [-90, -18, 54, 126, 198]
    word = "כלב" if lang == "he" else "dog"
    centre = "פק״רם" if lang == "he" else "PAKRAM"
    centre_font = "Rubik, Heebo, sans-serif" if lang == "he" else "Frank Ruhl Libre, serif"
    scenes = [scene_meg(), scene_drumming(), scene_rl(), scene_language(word), scene_touch_fmri()]
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
    out.append(f'<circle cx="{cx}" cy="{cy}" r="62" fill="#e7f2d3" stroke="{APPLE}" stroke-width="2"/>')
    spacing = "" if lang == "he" else ' letter-spacing="1"'
    out.append(f'<text x="{cx}" y="{cy + 9}" text-anchor="middle" direction="{"rtl" if lang == "he" else "ltr"}" font-family="{centre_font}" font-weight="700" font-size="{30 if lang == "he" else 27}"{spacing} fill="{DEEP}">{centre}</text>')
    for (x, y), scene in zip(nodes, scenes):
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NR + 3}" fill="#fff" stroke="{GREEN}" stroke-width="3"/>')
        out.append(f'<g transform="translate({x - NR:.1f},{y - NR:.1f}) scale({k:.4f})" clip-path="url(#medal)">{scene}</g>')
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NR}" fill="none" stroke="{GREEN}" stroke-width="2"/>')
    out.append("</svg>")
    return "".join(out)
