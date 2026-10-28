# Bauskript für das Deck prinzip-fortsetzung-und-schicksal
# Aufruf: python3 tools/sdvk/bau/prinzip-fortsetzung-und-schicksal.py
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'prinzip-fortsetzung-und-schicksal'
K = '#231f20'; G1 = '#888888'; G2 = '#d9d9d9'; L = '#9313ce'
KARTE = '#e4e4e4'; BILD = '#c4c4c4'; TEXT = '#aaaaaa'

def frame(bu, inner, w=600, h=600, stage='#ffffff', animate=True):
    extra = '' if animate else ', "animate":false'
    return f"{{% frame '{{\"stage\":\"{stage}\", \"w\":{w}, \"h\":{h}, \"bu\":\"{bu}\"{extra}}}' %}}\n{inner}\n{{% endframe %}}\n"

intro(D, 'Fortsetzung und Schicksal', 'Prinzip // Gruppieren')

W(D, '010-regel.md', '''
---
title: "Fortsetzung und Schicksal"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Zwei Regeln, die beide mit Verläufen zu tun haben. Gute Fortsetzung: Was auf einer Linie oder Kurve liegt, lesen wir als einen Verlauf, und wir folgen ihm mit dem Blick. Gemeinsames Schicksal: Was sich gemeinsam bewegt oder gemeinsam verändert, gehört zusammen, egal wo es steht.

  **Hintergrund**

  Beide gehören zu den Gestaltgesetzen, die Max Wertheimer 1923 in »Untersuchungen zur Lehre von der Gestalt II« (Psychologische Forschung 4) beschrieben hat. Wertheimer spricht von »Faktoren«, etwa dem Faktor des gemeinsamen Schicksals (Bezeichnungen aus dem Gedächtnis, bitte prüfen). Dass gerade Bewegung am Anfang steht, ist kein Zufall: Die Gestaltpsychologie beginnt mit Wertheimers Arbeit zur Scheinbewegung (Phi-Phänomen, 1912, siehe Phänomen Scheinbewegung und Zeit).

  Quellen: Lidwell, Holden & Butler, Universal Principles of Design (Good Continuation, Common Fate).
---

{% statement "Was auf einer Linie liegt, wird als Verlauf gelesen.", "Und was sich gemeinsam bewegt, gehört zusammen." %}
''')

# Gute Fortsetzung: zwei sich kreuzende Kurven, an der Kreuzung geteilt
def bez(p, t):
    u = 1 - t
    return (u**3*p[0][0] + 3*u*u*t*p[1][0] + 3*u*t*t*p[2][0] + t**3*p[3][0],
            u**3*p[0][1] + 3*u*u*t*p[1][1] + 3*u*t*t*p[2][1] + t**3*p[3][1])

def teile(p, t):
    lerp = lambda a, b: (a[0] + (b[0]-a[0])*t, a[1] + (b[1]-a[1])*t)
    a, b, c, d = p
    ab, bc, cd = lerp(a, b), lerp(b, c), lerp(c, d)
    abc, bcd = lerp(ab, bc), lerp(bc, cd)
    m = lerp(abc, bcd)
    return [a, ab, abc, m], [m, bcd, cd, d]

A = [(90, 520), (130, 280), (260, 140), (520, 130)]
B = [(80, 170), (260, 170), (340, 280), (420, 520)]
best = None
N = 600
pa = [bez(A, i/N) for i in range(N+1)]
pb = [bez(B, j/N) for j in range(N+1)]
for i, a in enumerate(pa):
    for j, b in enumerate(pb):
        d = (a[0]-b[0])**2 + (a[1]-b[1])**2
        if best is None or d < best[0]:
            best = (d, i/N, j/N)
A1, A2 = teile(A, best[1]); B1, B2 = teile(B, best[2])

def pfad(p, did, farbe):
    f = lambda q: f'{q[0]:.1f} {q[1]:.1f}'
    return (f'  <path data-id="{did}" d="M {f(p[0])} C {f(p[1])}, {f(p[2])}, {f(p[3])}" fill="none" '
            f'stroke="{farbe}" stroke-width="8" stroke-linecap="round" />')

k1 = frame('Was sehen Sie?', '\n'.join([pfad(A1, 'a1', K), pfad(A2, 'a2', K), pfad(B1, 'b1', K), pfad(B2, 'b2', K)]))
k2 = frame('Möglich wäre auch das: zwei Linien mit Knick. So sieht es kaum jemand', '\n'.join([pfad(A1, 'a1', L), pfad(B2, 'b2', L), pfad(A2, 'a2', K), pfad(B1, 'b1', K)]))

# Punkte auf einer Linie und auf einer Kurve
C = [(80, 160), (220, 560), (380, 560), (520, 300)]
punkte = []
for i in range(13):
    t = i / 12
    x, y = bez(C, t)
    punkte.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="{K}" />')
    x2, y2 = 80 + 440*t, 470 - 320*t
    punkte.append(f'  <circle cx="{x2:.1f}" cy="{y2:.1f}" r="10" fill="{K}" />')
k3 = frame('26 Punkte. Gesehen werden eine Gerade und eine Kurve', '\n'.join(punkte), animate=False)

W(D, '020-fortsetzung.md', f'''
---
title: "Gute Fortsetzung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Erst fragen: Was sehen Sie? Fast alle sagen: zwei Kurven, die sich kreuzen. Dann die Auflösung: Genauso gut könnten es zwei Linien sein, die sich an der Kreuzung berühren und jeweils einen Knick haben. So sieht es kaum jemand. Wir bevorzugen die Lesart, bei der die Linien ohne Knick weiterlaufen.

  Die dritte Grafik: 26 einzelne Punkte. Gesehen werden aber eine Gerade und eine Kurve, die sich kreuzen. Der Blick folgt dem Verlauf, auch über Lücken hinweg.

  **Hintergrund**

  Gute Fortsetzung ist der Grund, warum Diagramme mit Linien funktionieren, warum Ausrichtung an einer Kante wirkt und warum ein angeschnittenes Element »weiter« sagt. Das Auge ergänzt den Verlauf über die Lücke hinaus, verwandt mit der Geschlossenheit.
---

{k1}{k2}{k3}''')

# Im Screen: Karussell und Kante
def karussell(breit, kante):
    out = [f'  <rect data-id="h1" x="40" y="70" width="200" height="20" fill="{G1}" />']
    w = 220 if breit else 160
    for i in range(3):
        x = 40 + i * (w + 20)
        out.append(f'  <rect data-id="c{i}" x="{x}" y="110" width="{w}" height="190" fill="{KARTE}" />')
        out.append(f'  <rect data-id="ci{i}" x="{x+12}" y="122" width="{w-24}" height="110" fill="{BILD}" />')
        out.append(f'  <rect data-id="ct{i}a" x="{x+12}" y="248" width="{w-40}" height="12" fill="{G1}" />')
        out.append(f'  <rect data-id="ct{i}b" x="{x+12}" y="272" width="{int((w-24)*0.6)}" height="10" fill="{TEXT}" />')
    out.append(f'  <rect data-id="h2" x="40" y="340" width="160" height="20" fill="{G1}" />')
    for i in range(3):
        x = 40 + i * (w + 20)
        out.append(f'  <rect data-id="d{i}" x="{x}" y="380" width="{w}" height="110" fill="{KARTE}" />')
        out.append(f'  <rect data-id="dt{i}a" x="{x+14}" y="400" width="{int(w*0.6)}" height="12" fill="{G1}" />')
        out.append(f'  <rect data-id="dt{i}b" x="{x+14}" y="426" width="{w-28}" height="10" fill="{TEXT}" />')
        out.append(f'  <rect data-id="dt{i}c" x="{x+14}" y="446" width="{int((w-28)*0.5)}" height="10" fill="{TEXT}" />')
    if kante:
        out.append(f'  <line data-id="kante" x1="40" y1="40" x2="40" y2="540" stroke="{L}" stroke-width="4" stroke-linecap="round" stroke-dasharray="1 12" />')
    return '\n'.join(out)

s1 = frame('Drei Karten pro Reihe. Ist das alles?', karussell(False, False), stage='#666666')
s2 = frame('Angeschnitten: Da geht es weiter', karussell(True, False), stage='#666666')
s3 = frame('Die linke Kante: eine Linie, die gar nicht gezeichnet ist', karussell(True, True), stage='#666666')

W(D, '030-fortsetzung-im-screen.md', f'''
---
title: "Fortsetzung im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Startseite als Wireframe mit zwei Reihen. Erst passen drei Karten genau in die Breite: Das wirkt abgeschlossen. Niemand kommt auf die Idee, zu wischen. Dann werden die Karten breiter und die dritte ist angeschnitten. Der Verlauf läuft über den Rand hinaus, also geht es dort weiter. Streaming-Dienste, App Stores und Shops arbeiten genau so.

  Die dritte Fassung zeigt die zweite Fortsetzung im selben Screen: Alle Elemente beginnen an derselben linken Kante. Diese Linie ist nirgends gezeichnet, trotzdem sehen wir sie, und sie hält den Screen zusammen (siehe Ausrichtung und Raster).
---

{s1}{s2}{s3}''')

# Gemeinsames Schicksal abstrakt
cols = [135 + 70 * i for i in range(10)]
rows = [145 + 70 * r for r in range(4)]
mover = {(0, 2), (1, 6), (2, 1), (3, 4), (0, 8), (2, 7), (3, 9), (1, 3)}
def feld(modus):
    still, beweg = [], []
    for r, y in enumerate(rows):
        for c, x in enumerate(cols):
            if (r, c) in mover:
                farbe = L if modus == 'markiert' else K
                beweg.append(f'<circle cx="{x}" cy="{y}" r="14" fill="{farbe}" />')
            else:
                still.append(f'<circle cx="{x}" cy="{y}" r="14" fill="{K}" />')
    out = ['  ' + c for c in still]
    if modus == 'bewegt':
        out.insert(0, '<style>@keyframes gs-hub{from{transform:translateY(0)}to{transform:translateY(-26px)}}'
                      '.gs-hub{animation:gs-hub .9s ease-in-out infinite alternate}'
                      '@media (prefers-reduced-motion: reduce){.gs-hub{animation:none}}</style>')
        out.append('  <g class="gs-hub">' + ''.join(beweg) + '</g>')
    else:
        out += ['  ' + c for c in beweg]
    return '\n'.join(out)

m1 = frame('Ein Punktfeld', feld('still'), 900, 500, animate=False)
m2 = frame('Und jetzt?', feld('bewegt'), 900, 500, animate=False)
m3 = frame('Was sich gemeinsam bewegt, ist eine Gruppe. Quer durch das Feld', feld('markiert'), 900, 500, animate=False)

W(D, '040-schicksal.md', f'''
---
title: "Gemeinsames Schicksal"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Feld aus 40 gleichen Punkten in gleichen Abständen. Nach Nähe und Ähnlichkeit gibt es keine Gruppen. Dann bewegen sich acht Punkte im selben Takt auf und ab. Sofort sind sie eine Gruppe, obwohl sie über das ganze Feld verstreut sind und genauso aussehen wie alle anderen. Die letzte Folie hält die Gruppe fest.

  Die Animation ist reines CSS im SVG. Bei aktivierter Einstellung »Bewegung reduzieren« im Betriebssystem bleibt das Bild stehen. Dann direkt zur dritten Folie weiterschalten.

  **Hintergrund**

  Gemeinsames Schicksal ist eines der stärksten Gruppierungsprinzipien, stärker als Nähe und Ähnlichkeit. Gemeint ist nicht nur Bewegung, sondern jede gemeinsame Veränderung: gemeinsam aufleuchten, gemeinsam die Farbe wechseln, gemeinsam verschwinden. Das Auge reagiert besonders empfindlich auf Bewegung, gerade im Augenwinkel (siehe Phänomen Pop-out und Prinzip Bewegung).
---

{m1}{m2}{m3}''')

# Gemeinsames Schicksal im Screen: Auswahl verschieben
def liste(verschoben, haken):
    out = [f'  <rect x="80" y="60" width="180" height="20" fill="{G1}" />']
    for i in range(5):
        y = 120 + 64 * i
        dx = 60 if (verschoben and i in (0, 2, 3)) else 0
        an = haken and i in (0, 2, 3)
        x = 80 + dx
        if an:
            out.append(f'  <rect data-id="cb{i}" x="{x}" y="{y}" width="24" height="24" fill="{L}" />')
            out.append(f'  <polyline data-id="ck{i}" points="{x+6},{y+12} {x+11},{y+17} {x+19},{y+7}" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />')
        else:
            out.append(f'  <rect data-id="cb{i}" x="{x+1}" y="{y+1}" width="22" height="22" fill="#ffffff" stroke="{G1}" stroke-width="2" />')
        out.append(f'  <rect data-id="rh{i}" x="{x+44}" y="{y+2}" width="200" height="12" fill="{G1}" />')
        out.append(f'  <rect data-id="rt{i}" x="{x+44}" y="{y+24}" width="300" height="10" fill="{G2}" />')
    return '\n'.join(out)

l1 = frame('Fünf Einträge', liste(False, False), stage='#666666')
l2 = frame('Drei bewegen sich gemeinsam: eine Gruppe', liste(True, False), stage='#666666')
l3 = frame('Dazu ein Häkchen: Bewegung und Ähnlichkeit sagen dasselbe', liste(True, True), stage='#666666')

W(D, '050-schicksal-im-screen.md', f'''
---
title: "Schicksal im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Liste, etwa Mails oder Dateien. Beim Weiterschalten rücken drei Einträge gemeinsam nach rechts: Schon das macht sie zur Gruppe, ganz ohne Markierung. Im Interface passiert das beim Auswählen und Ziehen mehrerer Elemente, beim Wischen in Listen oder wenn Inhalte gemeinsam nachladen. Die dritte Fassung ergänzt die Markierung: Bewegung und Ähnlichkeit verstärken sich.

  Weitere Beispiele: Beim Hover über eine Karte reagieren Bild, Titel und Button gemeinsam, also gehören sie zu einer Karte. Beim Öffnen eines Menüs gleiten alle Einträge gemeinsam herein.

  Mini-Übung danach, 2 Minuten.
---

{l1}{l2}{l3}
{{% question "Wo bewegt sich in Ihrer meistgenutzten App etwas gemeinsam?", "Beim Auswählen, Ziehen, Wischen, Laden?" %}}
''')

# Grenzen: bündig gegen fast bündig
def buendig(versatz):
    o = versatz
    return '\n'.join([
        f'  <rect data-id="g0" x="{120+o[0]}" y="120" width="260" height="22" fill="{G1}" />',
        f'  <rect data-id="g1" x="{120+o[1]}" y="170" width="360" height="160" fill="{G2}" />',
        f'  <rect data-id="g2" x="{120+o[2]}" y="350" width="340" height="12" fill="{G2}" />',
        f'  <rect data-id="g3" x="{120+o[3]}" y="374" width="300" height="12" fill="{G2}" />',
        f'  <rect data-id="g4" x="{120+o[4]}" y="398" width="320" height="12" fill="{G2}" />',
        f'  <rect data-id="g5" x="{120+o[5]}" y="440" width="140" height="44" rx="22" fill="{L}" />',
    ])

b1 = frame('Bündig: eine gemeinsame Kante', buendig([0, 0, 0, 0, 0, 0]))
b2 = frame('Fast bündig: Fehler oder Absicht?', buendig([7, -5, 3, 0, -4, 9]))

W(D, '060-grenzen.md', f'''
---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Gute Fortsetzung ist empfindlich. Eine Kante, die nur fast stimmt, wirkt nicht wie eine Linie, sondern wie ein Versehen. Wenige Pixel genügen. Entweder bündig oder deutlich versetzt, alles dazwischen ist uneindeutig (siehe Prinzip Eindeutigkeit).

  Bewegung ist das stärkste Gruppierungsmittel und darum auch das lauteste. Wenn sich alles bewegt, gruppiert nichts mehr, und der Blick wird ständig abgelenkt. Bewegung braucht einen Zweck: Feedback, Zustandswechsel, Orientierung.

  Und Bewegung erreicht nicht alle. Manche Menschen reagieren auf Bewegung mit Schwindel oder Übelkeit und schalten sie im Betriebssystem ab (»Bewegung reduzieren«, in CSS abfragbar mit prefers-reduced-motion). Dann muss die Gruppe auch ohne Bewegung erkennbar sein, zum Beispiel über ein Häkchen.

  **Hintergrund**

  WCAG 2.2: Inhalte, die sich automatisch länger als fünf Sekunden bewegen, müssen sich anhalten lassen (2.2.2 Pause, Stop, Hide, Stufe A). Animationen, die durch Interaktion ausgelöst werden, sollen sich abschalten lassen (2.3.3 Animation from Interactions, Stufe AAA).
---

{b1}{b2}
<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt das nicht?</h1>
    {{% fragment '<p class="list">Wenn die Kante nur fast stimmt: Es wirkt wie ein Versehen.</p>' %}}
    {{% fragment '<p class="list">Wenn sich alles bewegt: Dann gruppiert nichts mehr.</p>' %}}
    {{% fragment '<p class="list">Wenn Bewegung die einzige Information ist: Mit »Bewegung reduzieren« fällt sie weg.</p>' %}}
  </div>
</section>
''')

W(D, '070-verweise.md', '''
---
title: "Verweise"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dahinter: Scheinbewegung und Zeit, Gestaltpsychologie. Weiter: Ausrichtung und Raster, Bewegung, Eindeutigkeit, Nähe und Abstand, Ähnlichkeit. Prüfen: Unschärfetest.
---

{% statement "Verweise", "Dahinter: [Scheinbewegung und Zeit](../phaenomen-scheinbewegung-und-zeit/) und [Gestaltpsychologie](../prinzip-gestaltpsychologie/). Weiter: [Ausrichtung und Raster](../prinzip-ausrichtung-und-raster/), [Bewegung](../prinzip-bewegung/), [Eindeutigkeit](../prinzip-eindeutigkeit/), [Nähe und Abstand](../prinzip-naehe-und-abstand/) und [Ähnlichkeit](../prinzip-aehnlichkeit/). Prüfen: [Unschärfetest](../methode-unschaerfetest/)." %}
''')

done(D, 'Was auf einer Linie liegt, wird als Verlauf gelesen. Was sich gemeinsam bewegt, gehört zusammen',
     'Gute Fortsetzung, Gemeinsames Schicksal, Ausrichtung, Anschnitt')
print('ok', D)
