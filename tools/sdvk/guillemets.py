import re,glob,sys
NEW='/Users/cnoss/git/privat/slides/src/presentations/screendesign-und-visuelle-kommunikation'
dry = len(sys.argv)>1 and sys.argv[1]=='dry'
tot=0; files=0
for p in sorted(glob.glob(NEW+'/*/*.md')):
    s=open(p).read()
    if not s.startswith('---'): continue
    end=s.index('\n---',3)
    fm=s[:end].split('\n'); body=s[end:]
    inblock=False; changed=0
    for i,l in enumerate(fm):
        if re.match(r'^speaker:\s*\|',l): inblock=True; continue
        if inblock and l and not l.startswith(' '): inblock=False
        if inblock:
            n=l
            n=re.sub(r'"([^"\n]+)"',r'»\1«',n)
            n=re.sub(r'„([^“”\n]+)[“”]',r'»\1«',n)
            n=re.sub(r'“([^”\n]+)”',r'»\1«',n)
            if n.count('"') or '„' in n or '“' in n: print('PRÜFEN',p.split('/')[-2:],n.strip()[:100])
            if n!=l: changed+=1; tot+=l.count('"')//2+l.count('„'); fm[i]=n
    if changed:
        files+=1
        if dry: print(p.split('/')[-2]+'/'+p.split('/')[-1],changed)
        else: open(p,'w').write('\n'.join(fm)+body)
print('Dateien',files,'Paare ca.',tot)
