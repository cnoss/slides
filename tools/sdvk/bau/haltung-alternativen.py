# Bauskript für das Deck haltung-alternativen
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
d='haltung-alternativen'

intro(d,'Alternativen','Haltung')

W(d,'010-satz.md','''
---
title: "Entwickeln Sie Alternativen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Haltung des Tages. Wer nur eine Lösung zeigt, kann auf die Frage »Warum so?« nur mit Geschmack antworten. Wer Alternativen hat, kann vergleichen und begründen: »Variante B, weil der Button hier zuerst gesehen wird.«

  Typischer Fehler im Studium: Die erste Idee wird ausgearbeitet, poliert und verteidigt. Die erste Idee ist aber meistens die naheliegende, also die, die alle anderen auch haben.

  **Hintergrund**

  Der Satz stammt aus dem Leitfaden dieses Moduls (»Gestaltungslösungen sind nie binär«). Verwandte Haltungen, die hier mitschwingen: »Erst ausprobieren, dann schärfen«, »Über das Naheliegende hinaus«, »Wer nie danebenliegt, hat nicht genug ausprobiert« (John Maeda, The Laws of Simplicity, 2006, Law 9: Failure) und »Verlieben Sie sich nicht in Ihren Prototyp«.
---

{% interlude "Entwickeln Sie Alternativen.", "Wer nur eine Lösung hat, hat keine Argumente." %}
''')

# Wireframe-Varianten, Koordinaten im Kartensystem 260 x 340
V = [
  dict(img=(20,20,220,120), h=(20,160,150,14), t1=(20,188,220,8), t2=(20,204,200,8), t3=(20,220,150,8), btn=(20,252,90,28)),
  dict(h=(20,20,180,14), t1=(20,44,220,8), t2=(20,58,200,8), t3=(20,72,150,8), img=(20,96,220,140), btn=(20,256,90,28)),
  dict(img=(0,0,260,170), h=(20,190,180,14), t1=(20,218,220,8), t2=(20,234,200,8), t3=(20,250,150,8), btn=(20,276,90,28)),
  dict(img=(70,20,120,120), h=(55,160,150,14), t1=(20,188,220,8), t2=(30,204,200,8), t3=(55,220,150,8), btn=(85,252,90,28)),
  dict(img=(20,20,100,100), h=(136,20,104,14), t1=(136,44,104,8), t2=(136,58,90,8), t3=(136,72,70,8), btn=(20,140,220,28)),
  dict(h=(20,20,220,30), t1=(20,62,220,8), t2=(20,78,200,8), t3=(20,94,150,8), img=(20,120,220,110), btn=(20,250,220,28)),
]
COL = dict(img='#c4c4c4', h='#888888', t1='#aaaaaa', t2='#aaaaaa', t3='#aaaaaa')

def card(i, ox, oy, s, op=1, btn='#231f20'):
    v=V[i]; out=[]
    f=lambda n: round(n*s,1)
    o=f' opacity="{op}"' if op!=1 else ''
    out.append(f'<rect data-id="v{i}-card" x="{ox}" y="{oy}" width="{f(260)}" height="{f(340)}" fill="#e4e4e4"{o} />')
    for k in ['img','h','t1','t2','t3','btn']:
        x,y,w,h=v[k]
        fill = btn if k=='btn' else COL[k]
        rx = f' rx="{f(14)}"' if k=='btn' else ''
        out.append(f'<rect data-id="v{i}-{k}" x="{round(ox+x*s,1)}" y="{round(oy+y*s,1)}" width="{f(w)}" height="{f(h)}"{rx} fill="{fill}"{o} />')
    return '\n'.join(out)

def frame(content, bu):
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":900, \"h\":500, \"bu\":\""+bu+"\"}' %}\n"+content+"\n{% endframe %}\n"

def raster(chosen=None):
    s=0.62; cw=260*s; ch=340*s; gx=40; gy=40
    x0=(900-(3*cw+2*gx))/2; y0=(500-(2*ch+gy))/2
    out=[]
    for i in range(6):
        r,c=divmod(i,3)
        op = 1 if chosen is None or chosen==i else 0.25
        btn = '#9313ce' if chosen==i else '#231f20'
        out.append(card(i, round(x0+c*(cw+gx),1), round(y0+r*(ch+gy),1), s, op, btn))
    return '\n'.join(out)

single = card(0, round((900-260*1.25)/2,1), round((500-340*1.25)/2,1), 1.25)

W(d,'020-varianten.md','''
---
title: "Eine Lösung, viele Lösungen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Erst ein einzelner Entwurf: Bild, Überschrift, Text, Button. Sieht ordentlich aus. Frage: Ist das gut? Ohne Vergleich lässt sich das kaum sagen.

  Dann dieselben Inhalte in sechs Anordnungen. Keine ist falsch. Erst jetzt kann man fragen: Welche passt am besten zu Ziel, Zielgruppe und Kontext? Und warum?

  Zum Schluss wird eine ausgewählt. Die anderen waren nicht umsonst: Sie sind die Begründung für die eine.
---

'''+frame(single,'Ein Entwurf. Ist er gut?')
   +frame(raster(),'Dieselben Inhalte, sechs Anordnungen')
   +frame(raster(4),'Viele gute Lösungen. Und gute Gründe für eine.'))

W(d,'030-nicht-binaer.md','''
---
title: "Nicht binär"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  In der Informatik gibt es oft richtig und falsch: Der Test läuft durch oder nicht. In der Gestaltung gibt es schlechte, gute und sehr gute Lösungen, und zu einem Problem oft mehrere sehr gute. Die zentrale Frage lautet deshalb: Was sind die Alternativen, und warum ist der gewählte Ansatz besser?

  Wer darauf keine Antwort hat, weil er keine Alternativen entwickelt hat, hat keine Argumente und einen schlechten Stand. Im Crit, gegenüber Auftraggeber:innen und in der Prüfung.

  **Hintergrund**

  Aus dem Leitfaden des Moduls (»Warum ändert sich mein Feedback so oft?«). Gestaltungsprobleme gelten in der Designforschung als »wicked problems« (Horst Rittel und Melvin Webber, 1973): Es gibt keine eindeutig richtige Lösung, nur bessere und schlechtere.
---

{% statement "Gestaltungslösungen sind nicht binär.", "Es gibt nicht die eine richtige Lösung. Es gibt viele gute. Und gute Gründe für eine davon." %}
''')

W(d,'040-erst-viele.md','''
---
title: "Erst viele, dann gute"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Anekdote (ca. 2 Minuten)**

  Ein Keramiklehrer teilt seine Klasse in zwei Gruppen. Die eine wird nur nach Menge bewertet: 25 Kilo Töpfe ergeben die Bestnote. Die andere nur nach Qualität: Sie muss einen einzigen, perfekten Topf abgeben. Am Ende stammen die besten Töpfe aus der Mengengruppe. Sie hat getöpfert, Fehler gemacht und daraus gelernt. Die Qualitätsgruppe hat vor allem über den perfekten Topf nachgedacht.

  Das ist eine Anekdote, kein Experiment. Die Botschaft trägt trotzdem: In der offenen Phase zählt Menge. Bewerten kommt später.

  **Hintergrund**

  David Bayles und Ted Orland, Art & Fear (1993). Orland hat später erzählt, dass die Geschichte auf einen Fotografie-Kurs von Jerry Uelsmann an der University of Florida zurückgeht, die Töpferei ist eine literarische Umdeutung (aus dem Gedächtnis, bitte prüfen).

  Verwandt: »Wer nie danebenliegt, hat nicht genug ausprobiert«. Fehler gehören dazu, sie sind der Preis für das Unerwartete.
---

{% statement "Erst viele, dann gute.", "In der offenen Phase zählt Menge. Bewerten und Aussortieren kommt danach." %}
''')

W(d,'050-woran.md','''
---
title: "Woran merken Sie es?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Prüffrage für die eigene Arbeit und für jedes Crit. Wer keine verworfenen Varianten zeigen kann, hat vermutlich die erste Idee genommen.

  Methodischer Partner: Variieren entlang einer Achse. Dort wird aus »viele Varianten« ein Verfahren: Eine visuelle Variable ändert sich, alles andere bleibt.
---

{% statement "Woran merken Sie, dass Sie es tun?", "Sie können zu jedem Entwurf zeigen, welche Varianten Sie verworfen haben. Und warum." %}

{% statement "So geht es", "Methode: [Variieren entlang einer Achse](../methode-variieren-achse/)" %}
''')

done(d,'Wer nur eine Lösung hat, hat keine Argumente: erst viele Varianten, dann begründet eine wählen',
     'Alternative, Variante, Exploration')
