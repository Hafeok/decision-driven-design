import yaml,re,os,sys
UP='/home/user/actor-indexed-determination'
def corpus():
    c={}
    for dp,dn,fns in os.walk(f'{UP}/core'):
        for fn in sorted(fns):
            if fn.endswith(('.md','.yaml')):
                p=os.path.join(dp,fn)
                try: c[os.path.relpath(p,UP)]=open(p,encoding='utf-8').read()
                except: pass
    return c
C=corpus()
def show(name,pre=70,post=90,filt=None,limit=400):
    pat=re.compile(r'(?<![A-Za-z0-9_-])'+re.escape(name).replace(r'\-','[- ]')+r'(?![A-Za-z0-9_-])',re.I)
    n=0
    for rel in sorted(C):
        txt=re.sub(r'\s+',' ',C[rel])
        for m in pat.finditer(txt):
            s=txt[max(0,m.start()-pre):m.end()+post]
            if filt and not re.search(filt,s,re.I): continue
            n+=1
            if n<=limit: print(f"  {rel}\n     …{s}…")
    print(f"  [{n} shown/matched]")
if __name__=='__main__':
    show(sys.argv[1], filt=(sys.argv[2] if len(sys.argv)>2 else None))
