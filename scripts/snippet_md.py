#!/usr/bin/env python3
"""
Shared helpers for reading/writing snippet markdown files.

Each snippet lives at snippet/<category-slug>/<title-slug>.md:

    ---
    id: "1738287868625"
    title: "Chage ISP Attendance Class MST.AU 2nd Query"
    category: "aeries-query"
    tags: ["Scheduling", "Attendance"]
    createdAt: "2025-01-31T01:44:28Z"
    author: "Jane Doe"
    ---

    Description text (markdown).

    ```text
    CODE HERE
    ```

`category` is the canonical value (not derived from the folder name - the
folder is just for browsability, since category strings like
"scheduling - course request queries" don't round-trip losslessly through a
slug). `author` is omitted entirely when there is none.

This is a small hand-rolled subset of YAML (quoted scalars + inline lists of
quoted scalars) rather than a PyYAML dependency, since it's fully controlled
by the two scripts that read/write it.
"""
import re
from pathlib import Path

FRONTMATTER_RE = re.compile(r'\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z', re.S)
FIELD_RE = re.compile(r'^([A-Za-z]+):\s*(.*)$')
LIST_ITEM_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
CODE_FENCE_RE = re.compile(r'```[A-Za-z0-9]*\r?\n(.*?)\r?\n```\s*\Z', re.S)


def slugify(text, maxlen=60):
    slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    slug = re.sub(r'-{2,}', '-', slug)
    return (slug[:maxlen].rstrip('-')) or 'untitled'


def _escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')


def _unescape(s):
    return s.replace('\\"', '"').replace('\\\\', '\\')


def _quote(s):
    return f'"{_escape(str(s))}"'


def format_frontmatter(snippet):
    lines = ['---']
    lines.append(f'id: {_quote(snippet["id"])}')
    lines.append(f'title: {_quote(snippet["title"])}')
    lines.append(f'category: {_quote(snippet.get("language", ""))}')
    tags = snippet.get('tags') or []
    lines.append('tags: [' + ', '.join(_quote(t) for t in tags) + ']')
    lines.append(f'createdAt: {_quote(snippet["createdAt"])}')
    if snippet.get('author'):
        lines.append(f'author: {_quote(snippet["author"])}')
    lines.append('---')
    return '\n'.join(lines)


def write_snippet_md(path, snippet):
    frontmatter = format_frontmatter(snippet)
    body = f'{snippet.get("description", "").strip()}\n\n```text\n{snippet["code"]}\n```\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'{frontmatter}\n\n{body}', encoding='utf-8')


def insert_id_field(path, new_id):
    """Add an `id:` line to a snippet file's frontmatter without touching
    anything else in the file (field order, body formatting, etc)."""
    text = path.read_text(encoding='utf-8')
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError(f'{path}: missing --- frontmatter block')
    frontmatter_fields, rest = m.group(1), m.group(2)
    path.write_text(f'---\nid: {_quote(new_id)}\n{frontmatter_fields}\n---\n{rest}', encoding='utf-8')


def _parse_scalar(raw):
    raw = raw.strip()
    if raw.startswith('"') and raw.endswith('"'):
        return _unescape(raw[1:-1])
    return raw


def _parse_list(raw):
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        raw = raw[1:-1]
    return [_unescape(m) for m in LIST_ITEM_RE.findall(raw)]


def parse_snippet_md(path):
    text = path.read_text(encoding='utf-8')
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError(f'{path}: missing --- frontmatter block')

    fields = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        fm = FIELD_RE.match(line)
        if not fm:
            raise ValueError(f'{path}: could not parse frontmatter line: {line!r}')
        key, value = fm.group(1), fm.group(2)
        fields[key] = _parse_list(value) if value.strip().startswith('[') else _parse_scalar(value)

    body = m.group(2).strip('\n')
    code_match = CODE_FENCE_RE.search(body)
    if not code_match:
        raise ValueError(f'{path}: no fenced code block found in body')
    description = body[:code_match.start()].strip()
    code = code_match.group(1)

    snippet = {
        'id': fields.get('id', ''),
        'title': fields.get('title', ''),
        'description': description,
        'code': code,
        'language': fields.get('category', ''),
        'tags': fields.get('tags', []),
        'createdAt': fields.get('createdAt', ''),
    }
    if fields.get('author'):
        snippet['author'] = fields['author']
    return snippet


def iter_snippet_files(snippet_dir):
    return sorted(Path(snippet_dir).glob('*/*.md'))
