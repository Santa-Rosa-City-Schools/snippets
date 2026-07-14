#!/usr/bin/env python3
"""
Build app/snippets.json from the markdown files under snippet/.

Usage:
  python3 scripts/build_snippets_json.py --src snippet --out app/snippets.json

Runs as a build step before deploy (see .github/workflows/deploy.yml) and can
also be run locally to preview changes to snippet/ before pushing.
"""
import argparse
import json
import sys
import time
from pathlib import Path

from snippet_md import insert_id_field, iter_snippet_files, parse_snippet_md


def generate_unique_id(ids_seen):
    candidate = int(time.time() * 1000)
    while str(candidate) in ids_seen:
        candidate += 1
    return str(candidate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', default='snippet')
    parser.add_argument('--out', default='app/snippets.json')
    args = parser.parse_args()

    files = iter_snippet_files(args.src)
    if not files:
        print(f'No snippet files found under {args.src}/', file=sys.stderr)
        sys.exit(1)

    snippets = []
    ids_seen = {}
    errors = []

    for path in files:
        try:
            snippet = parse_snippet_md(path)
        except ValueError as e:
            errors.append(str(e))
            continue

        if not snippet['id']:
            new_id = generate_unique_id(ids_seen)
            insert_id_field(path, new_id)
            snippet['id'] = new_id
            print(f'Assigned id {new_id} to {path}')

        if snippet['id'] in ids_seen:
            errors.append(f'{path}: duplicate id {snippet["id"]!r} (also used by {ids_seen[snippet["id"]]})')
            continue
        ids_seen[snippet['id']] = path

        snippets.append(snippet)

    if errors:
        for e in errors:
            print(f'ERROR: {e}', file=sys.stderr)
        sys.exit(1)

    snippets.sort(key=lambda s: s['createdAt'])

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({'snippets': snippets}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    print(f'Wrote {len(snippets)} snippets to {out_path}')


if __name__ == '__main__':
    main()
