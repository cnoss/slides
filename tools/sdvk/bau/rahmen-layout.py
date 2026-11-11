# Bauskript rahmen-layout. Aufruf: python3 tools/sdvk/bau/rahmen-layout.py
import glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'rahmen-layout'
os.makedirs(f'{NEW}/{D}', exist_ok=True)
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Layout', 'Rahmen')

L = '#9313ce'; FL = '#e4e4e4'; BI = '#c4c4c4'; TX = '#aaaaaa'; HL = '#888888'

def teile(pos, karte=None):
    """Elemente einer Card. pos: dict id -> (x, y). karte: (x, y, w, h) oder None."""
    o = ''
    if karte:
        x, y, w, h = karte
        o += f'<rect data-id="karte" x="{x}" y="{y}" width="{w}" height="{h}" fill="{FL}" />\n'
    else:
        o += f'<rect data-id="karte" x="450" y="250" width="0" height="0" fill="{FL}" />\n'
    m = {'bild': (pos['bild'][2], pos['bild'][3], BI, 0),
         'kat': (70, 10, HL, 0), 'titel': (pos['titel'][2], 20, HL, 0),
         't1': (pos['t1'][2], 10, TX, 0), 't2': (pos['t2'][2], 10, TX, 0), 't3': (pos['t3'][2] * 0.7, 10, TX, 0),
         'link': (100, 30, L, 15)}
    for k, (w, h, f, r) in m.items():
        x, y = pos[k][0], pos[k][1]
        o += f'<rect data-id="{k}" x="{x}" y="{y}" width="{w:g}" height="{h}" fill="{f}" rx="{r}" />\n'
    return o

# Lose Teile
LOSE = {'bild': (560, 70, 220, 140), 'kat': (130, 380, 0, 0), 'titel': (90, 90, 230, 0),
        't1': (420, 300, 230, 0), 't2': (120, 210, 230, 0), 't3': (560, 420, 230, 0), 'link': (360, 150, 0, 0)}
# A: Bild oben, dann Text
A = {'bild': (320, 50, 260, 150), 'kat': (320, 222, 0, 0), 'titel': (320, 246, 220, 0),
     't1': (320, 282, 260, 0), 't2': (320, 300, 260, 0), 't3': (320, 318, 260, 0), 'link': (320, 352, 0, 0)}
KA = (300, 30, 300, 380)
# B: Text oben, Bild unten
B = {'kat': (320, 50, 0, 0), 'titel': (320, 74, 220, 0), 't1': (320, 110, 260, 0), 't2': (320, 128, 260, 0),
     't3': (320, 146, 260, 0), 'bild': (320, 176, 260, 150), 'link': (320, 342, 0, 0)}
KB = (300, 30, 300, 380)
# C: Bild links, Text rechts
C = {'bild': (170, 130, 240, 200), 'kat': (440, 140, 0, 0), 'titel': (440, 164, 270, 0), 't1': (440, 200, 290, 0),
     't2': (440, 218, 290, 0), 't3': (440, 236, 290, 0), 'link': (440, 280, 0, 0)}
KC = (150, 110, 600, 260)

def fr(bu, svg, animate=True):
    a = '' if animate else '"animate":false,'
    return "{% frame '{" + a + "\"stage\":\"#ffffff\", \"w\":900, \"h\":500, \"bu\":\"" + bu + "\"}' %}\n" + svg + "{% endframe %}"

def mitte(p, k):
    return {'bild': (p['bild'][0] + p['bild'][2] / 2, p['bild'][1] + p['bild'][3] / 2),
            'titel': (p['titel'][0] + 40, p['titel'][1] + 10), 'text': (p['t1'][0] + 40, p['t2'][1] + 5),
            'link': (p['link'][0] + 50, p['link'][1] + 15)}[k]

def pfad(p, reihe):
    pts = ' '.join(f'{x:.0f},{y:.0f}' for x, y in (mitte(p, k) for k in reihe))
    return f'<polyline points="{pts}" fill="none" stroke="{L}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />\n'

W(D, '010-sortieren.md', '''
---
title: "Was lesen Sie zuerst?"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **Einstieg (ca. 3 Minuten), Schätzfrage.** Erst die losen Teile einer Card: ein Bild, eine Kategorie, ein Titel, drei Zeilen Teaser, ein Link. Fragen: Was davon lesen Sie zuerst? Die Antwort ist: Es kommt darauf an, wie die Teile angeordnet sind. Lose gibt es keine Reihenfolge.

  Dann drei Anordnungen derselben Teile. Bei jeder kurz zeigen lassen, was zuerst gesehen wird und in welcher Reihenfolge es weitergeht. Zum Schluss alle drei nebeneinander mit der Leserichtung in Lila.

  Pointe: Die Teile sind immer dieselben, kein Element ist größer, keine Farbe anders. Nur die Anordnung ändert sich, und damit die Reihenfolge, in der gelesen wird. Genau das ist ein Layout.
---

{% interlude "Was lesen Sie zuerst?", "Dieselben Teile, drei Anordnungen" %}

''' + '\n'.join([
    fr('Die Teile einer Card: Was lesen Sie zuerst?', teile(LOSE)),
    fr('Anordnung A', teile(A, KA)),
    fr('Anordnung B', teile(B, KB)),
    fr('Anordnung C', teile(C, KC)),
]) + '''

{% question "Welche Anordnung liest sich am klarsten?", "Und in welcher Reihenfolge lesen Sie jeweils?" %}

''' + fr('Dieselben Teile, drei Leserichtungen', (
    '<g transform="translate(-95,60) scale(0.6)">' + teile(A, KA).replace('data-id="', 'data-x="') + pfad(A, ['bild', 'titel', 'text', 'link']) + '</g>\n'
    '<g transform="translate(125,60) scale(0.6)">' + teile(B, KB).replace('data-id="', 'data-x="') + pfad(B, ['titel', 'text', 'bild', 'link']) + '</g>\n'
    '<g transform="translate(477,130) scale(0.45)">' + teile(C, KC).replace('data-id="', 'data-x="') + pfad(C, ['bild', 'titel', 'text', 'link']) + '</g>\n'
), animate=False) + '\n')

W(D, '020-was-ist-ein-layout.md', '''
---
title: "Was ist ein Layout?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Definition, die wir heute brauchen: Ein Layout ordnet Text, Bild und Fläche auf einem Format. Es entscheidet, was zuerst gelesen wird, was zusammengehört und was zurücktritt.

  Das Wort kommt aus dem Englischen: to lay out, auslegen, ausbreiten. In Druckereien und Agenturen hieß so der Entwurf, auf dem die Teile einer Seite ausgelegt wurden, bevor sie gesetzt wurden.

  Für jedes Layout stellen sich dieselben Fragen. Im bisherigen Foliensatz standen sie als fünf W-Fragen: Was (Inhalt), Warum (Ziel), Für wen (Zielgruppe), Wo (Medium) und Wie (stilistische Festlegungen). Die ersten vier kommen vor dem Wie. Ausführlich in der Methode Layoutanalyse.

  **Hintergrund**

  Der Begriff Makrotypografie meint dasselbe aus Sicht der Typografie: die Anordnung von Text und Bild auf der Seite, im Unterschied zur Mikrotypografie, die sich um Buchstaben, Wörter und Zeilen kümmert. Zum Weiterlesen: Lupton, Thinking with Type (Grid).
---

{% interlude "Was ist ein Layout?", "Und warum reicht es nicht, alles irgendwie unterzubringen?" %}

{% statement "Ein Layout ordnet Text, Bild und Fläche auf einem Format.", "Es entscheidet, was zuerst gelesen wird, was zusammengehört und was zurücktritt." %}
''')

W(D, '030-werkzeuge.md', '''
---
title: "Was Sie schon haben"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Neuen Stoff gibt es heute wenig. Die Werkzeuge für ein Layout haben Sie in den letzten Wochen schon gesammelt. Kurz durchgehen, bei jedem eine Frage an den Raum: Wer erinnert sich, was die Regel war?

  - Ausrichtung und Raster: Jedes Element richtet sich an etwas aus.
  - Nähe und Abstand: innen enger als außen.
  - Hierarchie: Nicht alles ist gleich wichtig, und das muss man sehen.
  - Typografische Skala: Schriftgrößen in festem Verhältnis.
  - Lesetext: Zeilenlänge, Zeilenabstand, Grauwert.

  Heute kommt das zusammen. Neu sind nur die Werkzeuge, die das Ganze systematisch machen: Gestaltungsraster und Spacing-System.
---

{% interlude "Was Sie schon haben", "Die Werkzeuge liegen bereit" %}

{% statement "Ihr Werkzeugkasten", "[Ausrichtung und Raster](../prinzip-ausrichtung-und-raster/), [Nähe und Abstand](../prinzip-naehe-und-abstand/), [Hierarchie](../prinzip-hierarchie/), [Typografische Skala](../methode-typografische-skala/) und [Lesetext](../prinzip-lesetext/). Neu heute: [Gestaltungsraster](../methode-gestaltungsraster/) und [Spacing-System](../methode-spacing-system/)." %}
''')

W(D, '040-heute.md', '''
---
title: "Heute"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Lernziele für heute. Sie stehen auch auf der Seite zur Veranstaltung.

  Der Input kommt heute in kleinen Portionen, jeweils direkt vor dem Arbeitsschritt, in dem Sie ihn brauchen: erst Skizzen, dann Grayscale-Wireframes, dann echte Inhalte, zum Schluss Farbe und Bild.
---

{% interlude "Heute", "Was Sie am Ende des Tages können" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Am Ende des Tages können Sie</h1>
    {% fragment '<p class="list">ein Layout aus Text, Bild und Fläche auf einem Raster bauen,</p>' %}
    {% fragment '<p class="list">vom Skizzieren über Wireframes bis zum fertigen Entwurf arbeiten,</p>' %}
    {% fragment '<p class="list">ein Layout systematisch variieren, eine Variable nach der anderen,</p>' %}
    {% fragment '<p class="list">Varianten begründet auswählen.</p>' %}
  </div>
</section>
''')

open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Layout"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Rahmen"
gruppe: ""
tiefe: ""
einsatz: "Einstieg in die Bausteine zu Layout und Variantenbildung"
kurzsatz: "Ein Layout ordnet Text, Bild und Fläche auf einem Format und legt fest, was zuerst gelesen wird"
begriffe: ["Layout", "Leserichtung", "Makrotypografie"]
herkunft: "U: layout/010"
inhalt:
  - "Schätzfrage: dieselben Teile, drei Anordnungen"
  - "Was ist ein Layout?"
  - "Was Sie schon haben"
  - "Lernziele des Tages"
status: ok
---
''')
print('fertig', D)
