#!/usr/bin/env python3
"""
One-time migration: convert app/snippets.json into snippet/<category>/<title>.md
files. Run once when moving to the markdown-based storage format; not part of
the regular build.

Usage:
  python3 scripts/migrate_to_markdown.py --json app/snippets.json --out snippet
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from snippet_md import slugify, write_snippet_md


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', default='app/snippets.json')
    parser.add_argument('--out', default='snippet')
    args = parser.parse_args()

    data = json.loads(Path(args.json).read_text(encoding='utf-8'))
    snippets = data.get('snippets', [])

    out_dir = Path(args.out)
    used_paths = Counter()
    written = 0

    for snippet in snippets:
        category = snippet.get('language') or ''
        category_slug = slugify(category) if category else 'uncategorized'
        title_slug = slugify(snippet['title'])

        used_paths[(category_slug, title_slug)] += 1
        n = used_paths[(category_slug, title_slug)]
        filename = f'{title_slug}.md' if n == 1 else f'{title_slug}-{snippet["id"]}.md'

        write_snippet_md(out_dir / category_slug / filename, snippet)
        written += 1

    print(f'Wrote {written} snippet files under {out_dir}/')


if __name__ == '__main__':
    main()
