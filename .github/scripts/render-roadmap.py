#!/usr/bin/env python3
"""Render an academy roadmap image (SVG) from its roadmap.json.

Usage:
    python .github/scripts/render-roadmap.py engineering-academy/08-forward-deployed-engineering/roadmap.json

The JSON lists stages and their topics. Each topic label must match a "## " heading in the stage's page, so the
image and the topic guides stay in step. The script exits with status 1 if a heading is missing.
"""

import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

# Techversant palette
NAVY = "#0B334C"
CYAN = "#00BAE0"
CYAN_LIGHT = "#E5F6FC"
CYAN_SOFT = "#9EDFEE"
INK = "#1F2A37"
MUTED = "#5B6B79"
BORDER = "#DCEAF1"
OPTIONAL_BORDER = "#9FB3C2"
FONT = "'DM Sans', Inter, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"

WIDTH = 1120
CENTER = WIDTH // 2
STAGE_W, STAGE_H = 300, 52
STAGE_W_MAX = 360
TOPIC_W, TOPIC_H = 284, 38
SIDE_MARGIN = 48
ROW = 48
STAGE_PAD = 26
STAGE_GAP = 30
HEADER_H = 190
FOOTER_H = 90


def check_headings(base: Path, stages: list) -> list:
    """Return the topics whose label has no matching '## ' heading in the stage page."""
    missing = []
    for stage in stages:
        page = base / stage["page"]
        headings = set()
        if page.exists():
            headings = {line[3:].strip() for line in page.read_text(encoding="utf-8").splitlines()
                        if line.startswith("## ")}
        for topic in stage["topics"]:
            if topic["label"] not in headings:
                missing.append(f"{stage['page']}: no heading '## {topic['label']}'")
    return missing


def check_mark(cx: float, cy: float) -> str:
    """A small navy badge with a white tick: Techversant guidance exists for the topic."""
    return (f'<circle cx="{cx}" cy="{cy}" r="8" fill="{NAVY}"/>'
            f'<path d="M{cx - 3.6} {cy + 0.2} l2.5 2.6 l4.8 -5" fill="none" stroke="#FFFFFF" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')


def topic_node(x: float, y: float, topic: dict) -> str:
    label = escape(topic["label"])
    size = 13 if len(topic["label"]) > 32 else 13.5
    if topic["core"]:
        box = (f'<rect x="{x}" y="{y}" width="{TOPIC_W}" height="{TOPIC_H}" rx="10" fill="{CYAN_LIGHT}" '
               f'stroke="{CYAN}" stroke-width="1.5"/>')
    else:
        box = (f'<rect x="{x}" y="{y}" width="{TOPIC_W}" height="{TOPIC_H}" rx="10" fill="#FFFFFF" '
               f'stroke="{OPTIONAL_BORDER}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    text = (f'<text x="{x + 14}" y="{y + TOPIC_H / 2 + 4.6}" font-size="{size}" font-weight="500" '
            f'fill="{INK}">{label}</text>')
    badge = check_mark(x + TOPIC_W - 20, y + TOPIC_H / 2) if topic["techversant"] else ""
    return box + text + badge


def connector(x1: float, y1: float, x2: float, y2: float, core: bool) -> str:
    mid = (x1 + x2) / 2
    dash = "" if core else ' stroke-dasharray="4 4"'
    return (f'<path d="M{x1} {y1} C{mid} {y1}, {mid} {y2}, {x2} {y2}" fill="none" stroke="{CYAN_SOFT}" '
            f'stroke-width="2"{dash}/>')


def stage_size(stages: list) -> tuple:
    """Return one pill width and title font size that fit the longest stage title."""
    longest = max(len(stage["title"]) for stage in stages)
    for size in (17, 16, 15):
        # About 9 px per character at 17 px bold, plus the number badge and the end padding.
        width = 60 + longest * 9 * size / 17 + 28
        if width <= STAGE_W_MAX:
            return max(STAGE_W, round(width)), size
    return STAGE_W_MAX, 15


def stage_node(y: float, stage: dict, width: float, size: float) -> str:
    x = CENTER - width / 2
    cy = y + STAGE_H / 2
    return (f'<rect x="{x}" y="{y}" width="{width}" height="{STAGE_H}" rx="{STAGE_H / 2}" fill="{NAVY}"/>'
            f'<circle cx="{x + 30}" cy="{cy}" r="17" fill="{CYAN}"/>'
            f'<text x="{x + 30}" y="{cy + 5}" font-size="14" font-weight="700" fill="{NAVY}" '
            f'text-anchor="middle">{escape(stage["number"])}</text>'
            f'<text x="{x + 60}" y="{cy + 6}" font-size="{size}" font-weight="700" fill="#FFFFFF">'
            f'{escape(stage["title"])}</text>')


def legend(x: float, y: float) -> str:
    items = [
        (f'<rect x="{x + 18}" y="{y + 40}" width="34" height="18" rx="9" fill="{NAVY}"/>', "Stage"),
        (f'<rect x="{x + 18}" y="{y + 68}" width="34" height="18" rx="5" fill="{CYAN_LIGHT}" stroke="{CYAN}" '
         f'stroke-width="1.5"/>', "Core topic"),
        (f'<rect x="{x + 168}" y="{y + 40}" width="34" height="18" rx="5" fill="#FFFFFF" '
         f'stroke="{OPTIONAL_BORDER}" stroke-width="1.5" stroke-dasharray="5 4"/>', "Optional topic"),
        (check_mark(x + 185, y + 77), "Techversant guide"),
    ]
    out = [f'<rect x="{x}" y="{y}" width="340" height="104" rx="12" fill="#F7FBFD" stroke="{BORDER}"/>',
           f'<text x="{x + 18}" y="{y + 26}" font-size="12" font-weight="700" fill="{MUTED}" '
           f'letter-spacing="1.2">LEGEND</text>']
    positions = [(x + 62, y + 54), (x + 62, y + 82), (x + 212, y + 54), (x + 212, y + 82)]
    for (shape, text), (tx, ty) in zip(items, positions):
        out.append(shape)
        out.append(f'<text x="{tx}" y="{ty}" font-size="13" fill="{INK}">{text}</text>')
    return "".join(out)


def render(data: dict) -> str:
    parts = []
    y = HEADER_H
    spine_top = spine_bottom = None
    stage_w, stage_font = stage_size(data["stages"])
    for stage in data["stages"]:
        topics = stage["topics"]
        left = topics[: (len(topics) + 1) // 2]
        right = topics[(len(topics) + 1) // 2:]
        rows = max(len(left), len(right), 1)
        block_h = rows * ROW - (ROW - TOPIC_H) + 2 * STAGE_PAD
        cy = y + block_h / 2
        stage_y = cy - STAGE_H / 2
        spine_top = cy if spine_top is None else spine_top
        spine_bottom = cy

        for column, x_topic, x_from, x_to in (
            (left, SIDE_MARGIN, CENTER - stage_w / 2, SIDE_MARGIN + TOPIC_W),
            (right, WIDTH - SIDE_MARGIN - TOPIC_W, CENTER + stage_w / 2, WIDTH - SIDE_MARGIN - TOPIC_W),
        ):
            first_y = cy - (len(column) * ROW - (ROW - TOPIC_H)) / 2
            for i, topic in enumerate(column):
                ty = first_y + i * ROW
                parts.append(connector(x_from, cy, x_to, ty + TOPIC_H / 2, topic["core"]))
                parts.append(topic_node(x_topic, ty, topic))
        parts.append(stage_node(stage_y, stage, stage_w, stage_font))
        y += block_h + STAGE_GAP

    height = y - STAGE_GAP + FOOTER_H
    spine = (f'<line x1="{CENTER}" y1="{spine_top - 70}" x2="{CENTER}" y2="{spine_bottom + 50}" stroke="{CYAN}" '
             f'stroke-width="4" stroke-linecap="round"/>'
             f'<circle cx="{CENTER}" cy="{spine_top - 70}" r="7" fill="{CYAN}"/>'
             f'<circle cx="{CENTER}" cy="{spine_bottom + 50}" r="7" fill="{NAVY}" stroke="{CYAN}" '
             f'stroke-width="3"/>')
    header = (f'<text x="{SIDE_MARGIN + 6}" y="62" font-size="13" font-weight="700" fill="{CYAN}" '
              f'letter-spacing="1.6">{escape(data["subtitle"].upper())}</text>'
              f'<text x="{SIDE_MARGIN + 4}" y="104" font-size="36" font-weight="700" fill="{NAVY}">'
              f'{escape(data["title"])}</text>'
              f'<rect x="{SIDE_MARGIN + 6}" y="122" width="72" height="5" rx="2.5" fill="{CYAN}"/>'
              + legend(WIDTH - SIDE_MARGIN - 340, 40))
    footer_y = height - 44
    footer = (f'<line x1="{SIDE_MARGIN}" y1="{footer_y - 22}" x2="{WIDTH - SIDE_MARGIN}" y2="{footer_y - 22}" '
              f'stroke="{BORDER}"/>'
              f'<text x="{SIDE_MARGIN}" y="{footer_y + 4}" font-size="13" fill="{MUTED}">Every topic has a guide '
              f'in the stage pages next to this image.</text>'
              f'<text x="{WIDTH - SIDE_MARGIN}" y="{footer_y + 4}" font-size="13" font-weight="700" fill="{NAVY}" '
              f'text-anchor="end">Techversant Center of Excellence</text>')
    title = escape(f'{data["title"]} roadmap')
    desc = escape("; ".join(f'{s["number"]} {s["title"]}: ' + ", ".join(t["label"] for t in s["topics"])
                            for s in data["stages"]))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
            f'viewBox="0 0 {WIDTH} {height}" font-family="{FONT}" role="img" aria-labelledby="t d">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc>'
            f'<rect x="1" y="1" width="{WIDTH - 2}" height="{height - 2}" rx="18" fill="#FFFFFF" '
            f'stroke="{BORDER}" stroke-width="2"/>'
            + header + spine + "".join(parts) + footer + "</svg>\n")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    source = Path(sys.argv[1])
    data = json.loads(source.read_text(encoding="utf-8"))
    missing = check_headings(source.parent, data["stages"])
    out = source.parent / data["output"]
    out.write_text(render(data), encoding="utf-8", newline="\n")
    print(f"Wrote {out}")
    for line in missing:
        print(f"Missing topic heading: {line}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
