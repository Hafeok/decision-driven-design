"""Predict the pin advance's firing WITHOUT touching graph/upstream.yaml.

Reads the pin list at the CURRENT pin, and computes, for each pinned id, the status and
content digest at both refs, using validate-core-order.py's own hashing so the prediction is
made with the instrument's arithmetic rather than an approximation of it.
"""
import hashlib, subprocess, sys, yaml

REPO='/home/user/actor-indexed-determination'
OLD, NEW = 'v5.9.0', 'v5.12.0'

def show(ref, p):
    r = subprocess.run(['git','-C',REPO,'show',f'{ref}:{p}'], capture_output=True, text=True)
    return None if r.returncode else r.stdout

def digest(o):
    parts=[o.get('statement',''), o.get('region',''), o.get('canonical_md','')]
    return 'sha256:'+hashlib.sha256('\x00'.join(parts).encode()).hexdigest()

def graph(ref):
    objs={}
    for d in ('core/claims/','core/decisions/'):
        for f in subprocess.run(['git','-C',REPO,'ls-tree','-r','--name-only',ref,d],
                                capture_output=True,text=True).stdout.split():
            if f.endswith('.yaml'):
                y=yaml.safe_load(show(ref,f))
                objs[y['id']]={'status':str(y.get('status','')),
                               'canonical_md':(y.get('canonical_md') or '').strip(),
                               'statement':(y.get('statement') or '').strip(),
                               'region':(y.get('region') or '').strip()}
    for t in yaml.safe_load(show(ref,'core/graph/terms.yaml'))['terms']:
        objs[t['id']]={'status':str(t.get('status','')),
                       'canonical_md':(t.get('canonical_md') or '').strip(),
                       'statement':(t.get('statement') or '').strip(),
                       'region':(t.get('region') or '').strip()}
    return objs

g_old, g_new = graph(OLD), graph(NEW)
pins = yaml.safe_load(open('graph/upstream.yaml'))['upstream']['pins']
print(f'{len(pins)} pins in graph/upstream.yaml at ref {OLD}\n')

e12=[]; w5=[]; w6=[]; ok=0
for p in pins:
    i=p['id']
    if i not in g_new: e12.append(i); continue
    if p.get('status_at_pin') != g_new[i]['status']:
        w5.append((i, p.get('status_at_pin'), g_new[i]['status']))
    d_new = digest(g_new[i])
    if p.get('content_hash') != d_new:
        w6.append((i, p.get('content_hash'), d_new,
                   'statement' if g_old.get(i,{}).get('statement')!=g_new[i]['statement'] else '',
                   'region' if g_old.get(i,{}).get('region')!=g_new[i]['region'] else '',
                   'canonical_md' if g_old.get(i,{}).get('canonical_md')!=g_new[i]['canonical_md'] else ''))
    else: ok+=1

print(f'E12 (pinned id gone at {NEW}): {len(e12)}', e12 or '')
print(f'\nW5 (status moved since the pin): {len(w5)}')
for i,a,b in w5: print(f'   {i}: {a} -> {b}')
print(f'\nW6 (content moved since the pin): {len(w6)}')
for i,a,b,*f in w6:
    print(f'   {i}: {a[:23]}... -> {b[:23]}...   fields: {", ".join(x for x in f if x)}')
print(f'\nunchanged pins: {ok}')

# W7: local terms shadowing upstream
import pathlib
local=set()
lt = pathlib.Path('core/graph/terms.yaml')
if lt.exists():
    for t in (yaml.safe_load(lt.read_text()) or {}).get('terms',[]) or []:
        local.add((t['id'], t.get('shadows_upstream')))
sh=[(i,s) for i,s in local if i in g_new]
print(f'\nW7 (local term ids shadowing the upstream registry at {NEW}): {len(sh)}')
for i,s in sh: print(f'   {i}  shadows_upstream: {s or "NOT DECLARED"}')
