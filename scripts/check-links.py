"""Check relative links and structure rules across the repository's markdown files.

Usage:
    python scripts/check-links.py            # report problems, exit 1 if any
    python scripts/check-links.py --orphans  # also list markdown files nothing links to

Checks:
  - Relative links and images point to files or folders that exist.
  - No file references the removed `learning-paths/` folder.
Skips code blocks, inline code, archive/ and .claude/templates/ (templates use placeholder links).
External URLs are checked by the Lychee job in CI, not here.
"""
import os
import re
import subprocess
import sys
import urllib.parse
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_PREFIXES = ("archive/", ".claude/templates/")

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


def main():
    show_orphans = "--orphans" in sys.argv
    files = [f for f in tracked_files() if os.path.exists(os.path.join(ROOT, f))]
    markdown = [f for f in files if f.lower().endswith(".md") and not f.startswith(SKIP_PREFIXES)]

    broken, legacy = [], []
    inbound = Counter()

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
            else:
                broken.append((source, target))
        for number, line in enumerate(text.splitlines(), 1):
            if LEGACY_RE.search(line):
                legacy.append((source, number, line.strip()[:100]))

    print(f"Checked {len(markdown)} markdown files")
    print(f"\nBroken relative links: {len(broken)}")
    for source, target in broken:
        print(f"  {source} -> {target}")
    print(f"\nReferences to removed learning-paths/ folder: {len(legacy)}")
    for source, number, line in legacy:
        print(f"  {source}:{number}: {line}")

    if show_orphans:
        index_names = {"README.md", "CLAUDE.md", "AGENTS.md"}
        orphans = [
            f for f in markdown
            if inbound[f] == 0 and os.path.basename(f) not in index_names
        ]
        print(f"\nMarkdown files with no inbound links: {len(orphans)}")
        for path in sorted(orphans):
            print(f"  {path}")

    return 1 if broken or legacy else 0


if __name__ == "__main__":
    sys.exit(main())
