#!/usr/bin/env python3
import csv, gzip, hashlib, json, re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
errors=[]
master=ROOT/'corpus'/'technical'/'JA21_JCG_TECHNICAL_CORPUS_10000.jsonl.gz'
records=[]
with gzip.open(master,'rt',encoding='utf-8') as f:
    for line in f: records.append(json.loads(line))
if len(records)!=10000: errors.append(f'corpus count {len(records)}')
ids=[r['identity']['record_id'] for r in records]
if len(set(ids))!=10000: errors.append('duplicate record ids')
if [r['identity']['sequence'] for r in records]!=list(range(1,10001)): errors.append('sequence failure')
for r in records:
    actual=hashlib.sha256(r['source']['program'].encode()).hexdigest()
    expected=r['source']['sha256'].replace('sha256:','')
    if actual!=expected: errors.append('source hash '+r['identity']['record_id']); break
scripts=list((ROOT/'scripts').rglob('*.ebnf'))
if len(scripts)!=1000: errors.append(f'script count {len(scripts)}')
with (ROOT/'catalogs'/'SCRIPT_CATALOG.csv').open(encoding='utf-8') as f: rows=list(csv.DictReader(f))
if len(rows)!=1000: errors.append(f'catalog rows {len(rows)}')
classes=Counter(r['example_class'] for r in rows)
tiers=Counter(int(r['tier']) for r in rows)
if classes!=Counter({'positive':750,'negative':190,'certification':60}): errors.append('class composition '+str(classes))
if tiers!=Counter({1:100,2:150,3:250,4:250,5:150,6:100}): errors.append('tier composition '+str(tiers))
if len(set(r['topic'] for r in rows))!=47: errors.append('topic coverage')
for row in rows:
    p=ROOT/row['script_path']; text=p.read_text(encoding='utf-8')
    required=['ja certifier 0.3','module ','policy no_execute_unknown_code','policy no_network','grammar ']
    if any(x not in text for x in required): errors.append('required declaration '+row['record_id']); break
    structural=re.sub(r'"(?:\\.|[^"\\])*"','',text)
    if structural.count('{')!=structural.count('}'): errors.append('brace balance '+row['record_id']); break
    if hashlib.sha256(text.rstrip('\n').encode()).hexdigest()!=row['origin_sha256']: errors.append('script hash '+row['record_id']); break
book=(ROOT/'textbook'/'JA21_JA_CERTIFIER_GRAMMAR_TEXTBOOK.md').read_text(encoding='utf-8')
if len(re.findall(r'^# Chapter \d+:',book,flags=re.M))!=22: errors.append('textbook chapter count')
max_path=max(len(p.relative_to(ROOT).as_posix()) for p in ROOT.rglob('*'))
if max_path>120: errors.append('path length '+str(max_path))
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'records':len(records),'scripts':len(scripts),'catalog_rows':len(rows),'classes':dict(classes),'tiers':dict(tiers),'topics':len(set(r['topic'] for r in rows)),'max_relative_path':max_path}
print(json.dumps(result,indent=2))
raise SystemExit(0 if not errors else 1)
