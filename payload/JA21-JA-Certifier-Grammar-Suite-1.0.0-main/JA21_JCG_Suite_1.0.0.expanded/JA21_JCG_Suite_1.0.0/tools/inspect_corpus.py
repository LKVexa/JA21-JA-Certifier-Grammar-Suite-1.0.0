#!/usr/bin/env python3
import argparse, gzip, json
from collections import Counter

p=argparse.ArgumentParser(description='Inspect the JA21 JCG technical corpus')
p.add_argument('corpus')
p.add_argument('--topic')
p.add_argument('--tier',type=int)
p.add_argument('--class-name',dest='class_name')
p.add_argument('--limit',type=int,default=10)
a=p.parse_args()
rows=[]
with gzip.open(a.corpus,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line)
        ped=r['pedagogy']
        if a.topic and ped['topic']!=a.topic: continue
        if a.tier and ped['tier']!=a.tier: continue
        if a.class_name and ped['example_class']!=a.class_name: continue
        rows.append(r)
print(json.dumps({'matches':len(rows),'topics':Counter(r['pedagogy']['topic'] for r in rows),'tiers':Counter(r['pedagogy']['tier'] for r in rows),'classes':Counter(r['pedagogy']['example_class'] for r in rows)},default=dict,indent=2))
for r in rows[:a.limit]:
    print('\n',r['identity']['record_id'],r['pedagogy']['topic'],r['pedagogy']['example_class'])
    print(r['source']['program'])
