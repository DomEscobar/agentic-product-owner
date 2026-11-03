#!/usr/bin/env python3
"""Validate this knowledge repository; does not evaluate a PO agent."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    errors = []
    docs = list(root.rglob('*.md'))
    source_text = (root / 'research/sources.md').read_text()
    source_ids = set(re.findall(r'^## (S\d+):', source_text, re.M))
    requirements = set(re.findall(r'\| (R\d+) \|', (root / 'docs/requirements.md').read_text()))
    for doc in docs:
        text = doc.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith('#'):
                continue
            if not (doc.parent / target.split('#')[0]).exists():
                errors.append(f'{doc.name}: broken link {target}')
        for source in re.findall(r'\bS\d{2}\b', text):
            if source not in source_ids:
                errors.append(f'{doc.name}: unknown source {source}')
        for marker in ['/root/', 'ghp_', 'gho_', 'sk-proj-', 'BEGIN PRIVATE KEY']:
            if marker in text:
                errors.append(f'{doc.name}: publication-sensitive marker')
    scenarios = json.loads((root / 'evals/scenarios.json').read_text())
    ids = [s['id'] for s in scenarios]
    if len(ids) != len(set(ids)):
        errors.append('duplicate scenario IDs')
    edge_text = (root / 'docs/edge-cases.md').read_text()
    for s in scenarios:
        if s['requirement'] not in requirements:
            errors.append(f"{s['id']}: unknown requirement")
        if not all(s.get(k) for k in ['trigger', 'expected_behavior', 'acceptance']):
            errors.append(f"{s['id']}: missing scenario fields")
        if s['status'] != 'specified-not-executed':
            errors.append(f"{s['id']}: unverified execution claim")
        if f"| {s['id']} |" not in edge_text:
            errors.append(f"{s['id']}: missing from edge-case document")
    return errors, {'documents': len(docs), 'sources': len(source_ids), 'requirements': len(requirements), 'scenarios': len(scenarios)}


if __name__ == '__main__':
    errors, counts = check()
    print(json.dumps({'status': 'FAIL' if errors else 'PASS', **counts, 'errors': errors}, ensure_ascii=False))
    raise SystemExit(bool(errors))
