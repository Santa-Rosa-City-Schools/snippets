#!/usr/bin/env python3
"""
Normalize and split tags in app/snippets.json.

Usage:
  python3 scripts/normalize_tags.py --file app/snippets.json

This script edits the file in place. It will:
 - Split tags on delimiters (-,/,&,;,:)
 - Split parts into words and treat each word as a tag (removing small stop words)
 - Normalize capitalization (Title Case for words, preserve acronyms)
 - Deduplicate tags per snippet
 - Print a short summary of changes
"""
import argparse
import json
import re
from collections import Counter

STOP_WORDS = set(['and','or','the','a','an','of','to','for','in','on','by','with','from'])

# Canonical map: lowercase -> canonical
CANONICAL_MAP = {
    'students': 'Student',
    'student': 'Student',
    'teachers': 'Teacher',
    'teacher': 'Teacher',
    'courses': 'Course',
    'course': 'Course',
    'parents': 'Parent',
    'parent portal': 'Parent Portal',
    'aeries': 'AERIES',
    'aeries query': 'AERIES',
    'testing': 'Testing',
    'tests': 'Testing',
    'programs': 'Program',
    'program': 'Program',
    'contacts': 'Contact',
    'contact': 'Contact',
    'enrollment': 'Enrollment',
    'attendance': 'Attendance',
    'special education': 'Special Education',
    'special': 'Special Education',
    'imports': 'Import',
    'import': 'Import',
    'exports': 'Export',
    'export': 'Export',
    'logs': 'Logs',
    'log': 'Logs',
    'discipline': 'Discipline',
    'assertive': 'Assertive',
}

def normalize_word(w):
    w = w.strip()
    if not w:
        return None
    # keep acronyms as uppercase
    if w.isupper() and len(w) > 1:
        return w
    # normalize capitalization
    return w.capitalize()

def split_tag_string(tag):
    # replace common delimiters with pipe
    if not isinstance(tag, str):
        return []
    s = tag.replace('\u2013','-').replace('\u2014','-')
    s = re.sub(r'[\-/,&;:]+', '|', s)
    parts = [p.strip() for p in s.split('|') if p.strip()]
    tags = []
    for p in parts:
        # split into words
        words = re.split(r'\s+', p)
        for w in words:
            w = w.strip()
            if not w:
                continue
            lw = w.lower()
            if lw in STOP_WORDS:
                continue
            nw = normalize_word(w)
            if nw:
                tags.append(nw)
    return tags

def normalize_snippet_tags(snippet):
    original = snippet.get('tags', []) or []
    new_tags = []
    for t in original:
        new_tags.extend(split_tag_string(t))

    # If no tags produced, try to add a tag from language or title words
    if not new_tags:
        lang = snippet.get('language')
        if lang:
            new_tags.append(normalize_word(lang))

    # dedupe while preserving order
    seen = set()
    final = []
    for t in new_tags:
        key = t.lower()
        # map canonical
        if key in CANONICAL_MAP:
            t = CANONICAL_MAP[key]
            key = t.lower()
        if key not in seen:
            seen.add(key)
            final.append(t)

    return original, final

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()

    path = args.file
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    snippets = data.get('snippets', [])
    changed = 0
    add_counts = Counter()
    remove_counts = Counter()
    for s in snippets:
        orig, final = normalize_snippet_tags(s)
        if orig != final:
            changed += 1
            for o in orig:
                remove_counts[o] += 1
            for n in final:
                add_counts[n] += 1
            s['tags'] = final

    if changed == 0:
        print('No tag changes needed.')
        return

    # backup
    import shutil
    backup_path = path + '.bak_merge'
    shutil.copyfile(path, backup_path)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'Updated tags for {changed} snippets. Backup written to {backup_path}')
    print('Top added tags:')
    for tag, cnt in add_counts.most_common(20):
        print(f'  {tag}: {cnt}')

if __name__ == '__main__':
    main()
