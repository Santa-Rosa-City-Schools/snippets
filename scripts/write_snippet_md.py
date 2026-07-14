#!/usr/bin/env python3
"""
Write a single new snippet markdown file from a JSON descriptor.

Used by .github/workflows/snippet-from-issue.yml after parsing a
"Suggest a Snippet" issue into {title, description, code, category, tags,
author}. Not meant for interactive use, but safe to run by hand too.

Usage:
  python3 scripts/write_snippet_md.py --input new-snippet.json --out snippet
"""
import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from snippet_md import slugify, write_snippet_md


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--out', default='snippet')
    args = parser.parse_args()

    fields = json.loads(Path(args.input).read_text(encoding='utf-8'))

    snippet = {
        'id': str(int(time.time() * 1000)),
        'title': fields['title'],
        'description': fields['description'],
        'code': fields['code'],
        'language': fields.get('category', ''),
        'tags': fields.get('tags', []),
        'createdAt': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    }
    if fields.get('author'):
        snippet['author'] = fields['author']

    out_dir = Path(args.out)
    category_slug = slugify(snippet['language']) if snippet['language'] else 'uncategorized'
    title_slug = slugify(snippet['title'])

    target = out_dir / category_slug / f'{title_slug}.md'
    n = 2
    while target.exists():
        target = out_dir / category_slug / f'{title_slug}-{n}.md'
        n += 1

    write_snippet_md(target, snippet)
    print(f'Wrote {target}')


if __name__ == '__main__':
    main()
