"""Check relative links and structure rules across the repository's markdown files.

Usage:
    python scripts/check-links.py            # report problems, exit 1 if any
    python scripts/check-links.py --orphans  # also list markdown files nothing links to

Checks:
  - Relative links and images point to files or folders that exist.
  - A #fragment on a link to another markdown file names a heading in that file.
    Same-file fragments are checked by markdownlint (MD051).
  - No file references the removed `learning-paths/` folder (docs/maintainers/ is exempt).
Skips code blocks, inline code, archive/ and .claude/templates/ (templates use placeholder links).
External URLs are checked by the Lychee job in CI, not here.
"""
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_PREFIXES = ("archive/", ".claude/templates/")
# redirect stubs at old paths are meant to have no inbound links
REDIRECT_STUB_MARKER = "<!-- redirect-stub"
# maintainer records describe the old layout on purpose, so only their links are checked
LEGACY_EXEMPT_PREFIXES = ("docs/maintainers/",)

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
LEGACY_RE = re.compile(r"learning-paths/")


def tracked_files():
    out = subprocess.check_output(
        ["git", "-C", ROOT, "ls-files", "-co", "--exclude-standard"], text=True, encoding="utf-8"
    )
    return [f.strip('"') for f in out.splitlines()]


def read_markdown(path):
    with open(os.path.join(ROOT, path), encoding="utf-8-sig") as handle:
        return handle.read()


def github_slug(heading):
    """Anchor GitHub generates for a heading: lower case, punctuation and symbols dropped, spaces to hyphens."""
    heading = re.sub(r"`([^`]*)`", r"\1", heading)
    heading = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    kept = [
        ch for ch in heading.strip().lower()
        if ch in " -_" or unicodedata.category(ch)[0] in "LN" or unicodedata.category(ch) == "Mn"
    ]
    return "".join(kept).replace(" ", "-")


def heading_anchors(path):
    anchors, seen = set(), Counter()
    for line in FENCE_RE.sub("", read_markdown(path)).splitlines():
        match = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if match:
            slug = github_slug(match.group(1))
            anchors.add(slug if seen[slug] == 0 else f"{slug}-{seen[slug]}")
            seen[slug] += 1
    return anchors


def main():
    show_orphans = "--orphans" in sys.argv
    files = [f for f in tracked_files() if os.path.exists(os.path.join(ROOT, f))]
    markdown = [f for f in files if f.lower().endswith(".md") and not f.startswith(SKIP_PREFIXES)]

    broken, legacy, bad_anchors = [], [], []
    inbound = Counter()
    anchor_cache = {}

    for source in markdown:
        text = read_markdown(source)
        prose = INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))
        for match in LINK_RE.finditer(prose):
            target = match.group(1)
            if re.match(r"^(https?:|mailto:|tel:|#)", target):
                continue
            path_part = urllib.parse.unquote(target.split("#")[0])
            if not path_part:
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(source), path_part)).replace("\\", "/")
            full = os.path.join(ROOT, resolved)
            if os.path.exists(full):
                inbound[resolved] += 1
                if os.path.isdir(full):
                    inbound[resolved.rstrip("/") + "/README.md"] += 1
                fragment = urllib.parse.unquote(target.partition("#")[2])
                if fragment and resolved.lower().endswith(".md") and resolved != source:
                    if resolved not in anchor_cache:
                        anchor_cache[resolved] = heading_anchors(resolved)
                    if fragment not in anchor_cache[resolved]:
                        bad_anchors.append((source, target))
            else:
                broken.append((source, target))
        if source.startswith(LEGACY_EXEMPT_PREFIXES):
            continue
        for number, line in enumerate(text.splitlines(), 1):
            if LEGACY_RE.search(line):
                legacy.append((source, number, line.strip()[:100]))

    print(f"Checked {len(markdown)} markdown files")
    print(f"\nBroken relative links: {len(broken)}")
    for source, target in broken:
        print(f"  {source} -> {target}")
    print(f"\nLinks to a heading that does not exist in the target file: {len(bad_anchors)}")
    for source, target in bad_anchors:
        print(f"  {source} -> {target}")
    print(f"\nReferences to removed learning-paths/ folder: {len(legacy)}")
    for source, number, line in legacy:
        print(f"  {source}:{number}: {line}")

    if show_orphans:
        index_names = {"README.md", "CLAUDE.md", "AGENTS.md"}
        # tool configuration is loaded by Claude Code and GitHub, not reached through links
        tooling_prefixes = (".claude/", ".github/")
        orphans = [
            f for f in markdown
            if inbound[f] == 0
            and os.path.basename(f) not in index_names
            and not f.startswith(tooling_prefixes)
            and not read_markdown(f).lstrip().startswith(REDIRECT_STUB_MARKER)
        ]
        print(f"\nMarkdown files with no inbound links: {len(orphans)}")
        for path in sorted(orphans):
            print(f"  {path}")

    return 1 if broken or legacy or bad_anchors else 0


if __name__ == "__main__":
    sys.exit(main())
