import os, re, shutil
OLD='/Users/cnoss/git/privat/slides/src/presentations/screendesign'
NEW='/Users/cnoss/git/privat/slides/src/presentations/screendesign-und-visuelle-kommunikation'
def W(deck, name, text):
    open(f'{NEW}/{deck}/{name}','w').write(text.lstrip('\n'))
def imgs(deck, src_deck, names):
    os.makedirs(f'{NEW}/{deck}/images', exist_ok=True)
    for n in names: shutil.copy(f'{OLD}/{src_deck}/images/{n}', f'{NEW}/{deck}/images/{n}')
def cp(deck, src, name, fix=None):
    s=open(f'{OLD}/{src}').read()
    if fix: s=fix(s)
    W(deck, name, s)
    # Bilder automatisch mitnehmen
    srcdeck=src.split('/')[0]
    for n in set(re.findall(r'\./images/([^"\')\s]+)', s)):
        if os.path.exists(f'{OLD}/{srcdeck}/images/{n}'): imgs(deck, srcdeck, [n])
def done(deck, kurzsatz, begriffe):
    begriffe=[x.strip() for x in begriffe.split(",") if x.strip()] if isinstance(begriffe,str) else begriffe
    p=f'{NEW}/{deck}/index.md'; s=open(p).read()
    s=s.replace('kurzsatz: ""', f'kurzsatz: "{kurzsatz}"').replace('begriffe: []', 'begriffe: ['+', '.join(f'"{b}"' for b in begriffe)+']').replace('status: entwurf','status: ok')
    open(p,'w').write(s)
    if os.path.exists(f'{NEW}/{deck}/010-inhalt.md'): os.remove(f'{NEW}/{deck}/010-inhalt.md')
def intro(deck, title, sub):
    W(deck,'000-intro.md',f'''
---
title: "{title}"
layout: presentation.11ty.js
slideClasses: intro
transition: zoom
---

<div class="is-full-width">

# {title}

## {sub}

</div>
''')
