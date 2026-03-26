#!/usr/bin/env python3
"""
Scan snippets.json and add tags based on keywords in title/description.

Usage:
  python3 scripts/add_tags_from_text.py --file app/snippets.json

This edits the file in place and creates a backup at the same path + '.bak2'.
It preserves existing tags and only adds new ones.
"""
import argparse
import json
import re
import shutil
from collections import Counter

KEYWORD_TAG_MAP = [
    (r'ELPAC', ['ELPAC','Testing']),
    (r'ELPAC\b', ['ELPAC']),
    (r'CAASPP|SBAC|Smarter Balanced', ['CAASPP','Testing']),
    (r'PFT\b|Physical Fitness', ['PFT','Testing']),
    (r'Parent Portal|Parent Portal', ['Parent Portal','Contacts']),
    (r'Attendance|Attendance Ruleset|Attendance Class', ['Attendance']),
    (r'Health|Vision|Hearing', ['Health']),
    (r'Discipline|Assertive', ['Discipline','Assertive']),
    (r'Scheduling|Master schedule|master schedule|MST\.', ['Scheduling']),
    (r'Enrollment|Next Year Program|NSP\b', ['Enrollment']),
    (r'Teacher|TCH\.|Teachers', ['Teacher']),
    (r'Contact|Contacts|CON\.', ['Contacts']),
    (r'Programs|PGM\.|Student Programs', ['Programs','Student']),
    (r'Import|Export|Download|Upload', ['Import','Export']),
    (r'Student\b|STU\.', ['Students','Student']),
    (r'Course|CRS\.|Courses|CTE', ['Courses']),
    (r'Testing|Initial ELPAC|Interim|Summative', ['Testing']),
    (r'Special Education|Special', ['Special Education','Special']),
    (r'SSID', ['SSID','Student']),
    (r'Parent Portal', ['Parent Portal']),
    (r'Logs|Log', ['Logs','Admin']),
    (r'Aeries', ['Aeries','Aeries Query']),
]

def normalize_tag(t):
    if not isinstance(t, str):
        return None
    s = t.strip()
    if not s:
        return None
    # keep common acronyms uppercase
    if s.upper() in ('ELPAC','CAASPP','PFT','SSID','AERIES'):
        return s.upper()
    # Title case multi-word
    return ' '.join([w.capitalize() if not w.isupper() else w for w in s.split()])

def add_tags(data):
    snippets = data.get('snippets', [])
    added_counter = Counter()
    changed = 0
    for s in snippets:
        text = ' '.join(filter(None, [s.get('title',''), s.get('description','')]))
        if not text:
            continue
        text_l = text.lower()
        existing = s.get('tags') or []
        existing_norm = {t.lower() for t in existing}
        to_add = []
        for pattern, tags in KEYWORD_TAG_MAP:
            try:
                if re.search(pattern, text, re.IGNORECASE):
                    for tag in tags:
                        tn = normalize_tag(tag)
                        if tn and tn.lower() not in existing_norm:
                            to_add.append(tn)
                            existing_norm.add(tn.lower())
            except re.error:
                continue

        if to_add:
            changed += 1
            # append new tags preserving order
            new_tags = existing + [t for t in to_add if t not in existing]
            s['tags'] = new_tags
            for t in to_add:
                added_counter[t] += 1

    return changed, added_counter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()

    path = args.file
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changed, added = add_tags(data)
    if changed == 0:
        print('No tags added.')
        return

    shutil.copyfile(path, path + '.bak2')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'Added tags to {changed} snippets. Backup at {path}.bak2')
    print('Top added tags:')
    for tag, cnt in added.most_common(30):
        print(f'  {tag}: {cnt}')

if __name__ == '__main__':
    main()
