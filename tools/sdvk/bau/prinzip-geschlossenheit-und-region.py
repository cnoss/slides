# Bauskript für das Deck prinzip-geschlossenheit-und-region
# Aufruf: python3 tools/sdvk/bau/prinzip-geschlossenheit-und-region.py
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'prinzip-geschlossenheit-und-region'
K = '#231f20'; G1 = '#888888'; G2 = '#d9d9d9'; L = '#9313ce'
KARTE = '#e4e4e4'; BILD = '#c4c4c4'; TEXT = '#aaaaaa'

def frame(bu, inner, w=600, h=600, stage='#ffffff'):
    return f"{{% frame '{{\"stage\":\"{stage}\", \"w\":{w}, \"h\":{h}, \"bu\":\"{bu}\"}}' %}}\n{inner}\n{{% endframe %}}\n"

intro(D, 'Geschlossenheit und Region', 'Prinzip // Gruppieren')

W(D, '010-regel.md', '''
---
title: "Geschlossenheit und Region"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Drei verwandte Regeln in einem Deck. Geschlossenheit: Wir ergänzen Lücken zu geschlossenen Formen. Gemeinsame Region: Was in einem gemeinsamen Rahmen oder auf einer gemeinsamen Fläche steht, gehört zusammen. Verbundenheit: Was durch eine Linie verbunden ist, gehört zusammen. Region und Verbundenheit sind stärker als Nähe und Ähnlichkeit. Im Interface sind das Karten, Flächen, Rahmen und Linien.

  **Hintergrund**

  Die Geschlossenheit gehört zu den klassischen Gestaltgesetzen der Berliner Schule (Max Wertheimer, Wolfgang Köhler, Kurt Koffka), ausführlich bei Koffka, Principles of Gestalt Psychology (1935). Die beiden anderen Regeln sind jünger: Stephen E. Palmer beschrieb die gemeinsame Region 1992 (»Common region: A new principle of perceptual grouping«, Cognitive Psychology 24), Palmer und Irvin Rock die Verbundenheit 1994 (»Rethinking perceptual organization: The role of uniform connectedness«, Psychonomic Bulletin & Review 1). Die Gestaltgesetze sind also keine abgeschlossene Liste von 1923, die Forschung geht weiter.

  Quellen: Lidwell, Holden & Butler, Universal Principles of Design (Closure, Uniform Connectedness); Yablonski, Laws of UX (Law of Common Region, Law of Uniform Connectedness).
---

{% statement "Was umschlossen ist, gehört zusammen.", "Und was fehlt, ergänzen wir." %}
''')

# Geschlossenheit: vier Winkel
def winkel(v, arm, did):
    (x, y), (dx, dy) = v
    return (f'  <polyline data-id="{did}" points="{x+dx*arm},{y} {x},{y} {x},{y+dy*arm}" fill="none" '
            f'stroke="{K}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />')

def ecken(a, b, arm):
    # a, b: obere linke und untere rechte Ecke
    vs = [((a, a), (1, 1)), ((b, a), (-1, 1)), ((a, b), (1, -1)), ((b, b), (-1, -1))]
    return '\n'.join(winkel(v, arm, f'w{i}') for i, v in enumerate(vs))

g1 = frame('Vier Winkel', ecken(110, 490, 70))
g2 = frame('Ein Quadrat. Obwohl alle Seiten Lücken haben', ecken(190, 410, 70))
g3 = frame('Auch ein Kreis mit Lücken bleibt ein Kreis',
           f'  <circle data-id="kreis" cx="300" cy="300" r="130" fill="none" stroke="{K}" stroke-width="8" stroke-linecap="round" stroke-dasharray="70 32" />')

imgs(D, 'gestaltgesetze', ['ibm-logo.png'])

W(D, '020-geschlossenheit.md', f'''
---
title: "Geschlossenheit"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Vier Winkel, weit auseinander: Man sieht vier Winkel. Rücken sie zusammen, sieht man ein Quadrat, obwohl jede Seite eine Lücke hat. Das Gehirn ergänzt die einfachste geschlossene Form. Dasselbe beim Kreis aus Bogenstücken.

  Wer im Phänomen Kippfiguren das Dreieck von Kanizsa gesehen hat, kennt den Effekt schon: Dort ergänzen wir sogar eine Kante, die gar nicht da ist.

  Das IBM-Logo: Die Streifen zerschneiden die Buchstaben, trotzdem lesen wir drei ganze Buchstaben. Entworfen von Paul Rand, in der heutigen Form mit acht Streifen seit 1972 (aus dem Gedächtnis, bitte prüfen). Viele Logos und Icons arbeiten mit Geschlossenheit: Sie lassen weg, was das Auge ohnehin ergänzt.

  **Hintergrund**

  Die Geschlossenheit hängt eng mit der Prägnanz zusammen (siehe Gestaltpsychologie): Wir sehen die einfachste und vollständigste Form, die zu den Reizen passt.
---

{g1}{g2}{g3}
{{% screenshot "./images/ibm-logo.png", '{{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Streifen statt Buchstaben, gelesen wird trotzdem IBM<br><small>IBM-Logo, Paul Rand, 1972</small>"}}' %}}
''')

# Gemeinsame Region und Verbundenheit, 900 x 500
gleich = [135 + 90 * i for i in range(8)]
paare = []
for k in range(4):
    paare += [180 + 180 * k - 25, 180 + 180 * k + 25]
Y = 250

def punkte(xs):
    return '\n'.join(f'  <circle data-id="p{i}" cx="{x}" cy="{Y}" r="12" fill="{K}" />' for i, x in enumerate(xs))

def regionen(xs, gruppen, pad=32):
    out = []
    for j, (a, b) in enumerate(gruppen):
        x0 = xs[a] - pad; x1 = xs[b] + pad
        out.append(f'  <rect data-id="r{j}" x="{x0}" y="{Y-40}" width="{x1-x0}" height="80" fill="{KARTE}" />')
    return '\n'.join(out)

def linien(xs, gruppen):
    return '\n'.join(f'  <line data-id="l{j}" x1="{xs[a]}" y1="{Y}" x2="{xs[b]}" y2="{Y}" stroke="{K}" stroke-width="6" stroke-linecap="round" />'
                     for j, (a, b) in enumerate(gruppen))

r1 = frame('Gleiche Abstände: eine Reihe', punkte(gleich), 900, 500)
r2 = frame('Gemeinsame Fläche: Paare', regionen(gleich, [(0, 1), (2, 3), (4, 5), (6, 7)]) + '\n' + punkte(gleich), 900, 500)
r3 = frame('Andere Flächen, andere Paare', regionen(gleich, [(1, 2), (3, 4), (5, 6)]) + '\n' + punkte(gleich), 900, 500)
r4 = frame('Nähe bildet Paare', punkte(paare), 900, 500)
r5 = frame('Die Fläche schlägt die Nähe', regionen(paare, [(1, 2), (3, 4), (5, 6)], 20) + '\n' + punkte(paare), 900, 500)
r6 = frame('Auch eine Verbindungslinie schlägt die Nähe', linien(paare, [(1, 2), (3, 4), (5, 6)]) + '\n' + punkte(paare), 900, 500)

W(D, '030-region.md', f'''
---
title: "Gemeinsame Region"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Acht Punkte in gleichen Abständen. Dann liegen jeweils zwei auf einer gemeinsamen hellgrauen Fläche: Paare. Verschieben sich die Flächen, entstehen andere Paare, die Punkte selbst haben sich nicht bewegt.

  Dann der Härtetest: Die Punkte rücken paarweise zusammen, Nähe bildet Paare. Legt man die Flächen quer dazu, gewinnt die Fläche. Dasselbe mit einer einfachen Verbindungslinie. Fragen nach jeder Folie: Welche Punkte gehören zusammen?

  **Hintergrund**

  Stephen E. Palmer (1992) zeigte, dass eine gemeinsame Region Nähe und Ähnlichkeit überstimmen kann. Palmer und Rock (1994) beschrieben die Verbundenheit (uniform connectedness) als eines der stärksten Gruppierungsprinzipien: Was verbunden ist, sehen wir als ein Objekt.
---

{r1}{r2}{r3}{r4}{r5}{r6}''')

# Im Screen: Liste ohne und mit Karten
def liste(karten):
    out = [f'  <rect x="80" y="70" width="220" height="20" fill="{G1}" />']
    for i, y in enumerate([120, 245, 370]):
        if karten:
            out.append(f'  <rect data-id="c{i}" x="70" y="{y-14}" width="460" height="118" fill="{KARTE}" />')
        bild = BILD if karten else G2
        text = TEXT if karten else G2
        out.append(f'  <rect data-id="i{i}" x="86" y="{y}" width="90" height="90" fill="{bild}" />')
        out.append(f'  <rect data-id="h{i}" x="196" y="{y+8}" width="200" height="14" fill="{G1}" />')
        out.append(f'  <rect data-id="t{i}a" x="196" y="{y+36}" width="300" height="10" fill="{text}" />')
        out.append(f'  <rect data-id="t{i}b" x="196" y="{y+56}" width="220" height="10" fill="{text}" />')
    return '\n'.join(out)

l1 = frame('Ohne Flächen: Gruppen nur durch Abstand', liste(False), stage='#666666')
l2 = frame('Mit Karten: Jede Fläche ist eine Gruppe', liste(True), stage='#666666')

def formular(regionen_an):
    out = [f'  <rect x="90" y="60" width="200" height="20" fill="{G1}" />']
    bloecke = [(110, [0, 1]), (300, [0, 1])]
    for b, (y0, felder) in enumerate(bloecke):
        if regionen_an:
            out.append(f'  <rect data-id="fr{b}" x="70" y="{y0-14}" width="460" height="168" fill="{KARTE}" />')
        out.append(f'  <rect data-id="fh{b}" x="90" y="{y0+4}" width="140" height="14" fill="{G1}" />')
        for f in felder:
            y = y0 + 40 + f * 56
            out.append(f'  <rect data-id="fl{b}{f}" x="90" y="{y}" width="90" height="10" fill="{TEXT if regionen_an else G2}" />')
            out.append(f'  <rect data-id="ff{b}{f}" x="90" y="{y+16}" width="420" height="28" fill="#ffffff" stroke="{G1}" stroke-width="2" />')
    out.append(f'  <rect data-id="fbtn" x="90" y="490" width="140" height="40" rx="20" fill="{L}" />')
    return '\n'.join(out)

f1 = frame('Ein Formular, zwei Abschnitte', formular(False), stage='#666666')
f2 = frame('Mit Flächen: Abschnitte auf einen Blick', formular(True), stage='#666666')

W(D, '040-im-screen.md', f'''
---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Liste als Wireframe. Ohne Flächen hält nur der Abstand die Einträge zusammen. Das funktioniert, solange die Abstände eindeutig sind. Mit Karten ist jede Fläche eine Gruppe, selbst wenn die Einträge eng stehen. Darum sind Karten im Interface so verbreitet: in Feeds, Shops, Dashboards.

  Dasselbe bei Formularen: Zwei Abschnitte, etwa Adresse und Zahlung. Mit hinterlegten Flächen sieht man auf einen Blick, welches Feld zu welchem Abschnitt gehört. Die Fläche ersetzt keine Überschrift, aber sie zeigt die Gruppe schneller.

  Mini-Übung danach, 3 Minuten zu zweit.
---

{l1}{l2}{f1}{f2}
{{% question "Wo arbeitet Ihre meistgenutzte App mit Karten, Flächen oder Linien?", "Und wäre es ohne sie auch eindeutig?" %}}
''')

# Grenzen: Kiste in Kiste
def kisten(rahmen):
    out = []
    def box(did, x, y, w, h):
        if rahmen:
            out.append(f'  <rect data-id="{did}" x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="{G1}" stroke-width="2" />')
    box('k0', 60, 50, 480, 470)
    box('k1', 80, 70, 440, 50)
    out.append(f'  <rect data-id="kh" x="100" y="86" width="180" height="18" fill="{G1}" />')
    for i, x in enumerate([80, 310]):
        if rahmen:
            box(f'kc{i}', x, 140, 210, 360)
        else:
            out.append(f'  <rect data-id="kc{i}" x="{x}" y="140" width="210" height="360" fill="{KARTE}" />')
        box(f'kb{i}', x + 15, 155, 180, 120)
        out.append(f'  <rect data-id="ki{i}" x="{x+15}" y="155" width="180" height="120" fill="{BILD}" />')
        box(f'kt{i}', x + 15, 290, 180, 110)
        out.append(f'  <rect data-id="kx{i}a" x="{x+28}" y="304" width="150" height="14" fill="{G1}" />')
        out.append(f'  <rect data-id="kx{i}b" x="{x+28}" y="334" width="150" height="10" fill="{TEXT}" />')
        out.append(f'  <rect data-id="kx{i}c" x="{x+28}" y="356" width="110" height="10" fill="{TEXT}" />')
        box(f'kbb{i}', x + 15, 415, 180, 60)
        out.append(f'  <rect data-id="kbt{i}" x="{x+28}" y="425" width="120" height="40" rx="20" fill="{L}" />')
    return '\n'.join(out)

k1 = frame('Rahmen um alles: Kiste in Kiste in Kiste', kisten(True), stage='#666666')
k2 = frame('Dieselben Gruppen: nur Flächen und Abstand', kisten(False), stage='#666666')

W(D, '050-grenzen.md', f'''
---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Wenn ein Rahmen gruppiert, warum nicht überall einen? Die erste Fassung zeigt das Ergebnis: Kiste in Kiste in Kiste. Jede Linie ist ein Signal, und viele Signale sind Rauschen. Die zweite Fassung zeigt dieselben Gruppen nur mit zwei Flächen und Abstand. Ruhiger, und die Gruppen sind trotzdem eindeutig.

  Faustregel aus Refactoring UI (Wathan & Schoger, »Use fewer borders«): Bevor Sie einen Rahmen ziehen, probieren Sie Abstand, eine Hintergrundfläche oder einen leichten Helligkeitsunterschied.

  Zweite Grenze: Eine hellgraue Fläche auf Weiß ist leise. Auf schlechten Bildschirmen oder für Menschen mit Sehschwäche kann sie verschwinden. Wenn die Gruppe wichtig ist, darf sie nicht nur an der Fläche hängen.
---

{k1}{k2}
<section class="simple" data-transition="fade">
  <div>
    <h1>Wann schadet ein Rahmen?</h1>
    {{% fragment '<p class="list">Wenn Rahmen in Rahmen in Rahmen stecken: Rauschen.</p>' %}}
    {{% fragment '<p class="list">Wenn Abstand genügt: Weißraum ist leiser als eine Linie.</p>' %}}
    {{% fragment '<p class="list">Wenn die Fläche zu schwach ist: Dann sehen nicht alle die Gruppe.</p>' %}}
  </div>
</section>
''')

W(D, '060-verweise.md', '''
---
title: "Verweise"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dahinter: Kippfiguren (Scheinkonturen), Gestaltpsychologie. Weiter: Nähe und Abstand, Ähnlichkeit, Figur und Grund, Weißraum. Prüfen: Unschärfetest.
---

{% statement "Verweise", "Dahinter: [Kippfiguren](../phaenomen-kippfiguren/) und [Gestaltpsychologie](../prinzip-gestaltpsychologie/). Weiter: [Nähe und Abstand](../prinzip-naehe-und-abstand/), [Ähnlichkeit](../prinzip-aehnlichkeit/), [Figur und Grund](../prinzip-figur-und-grund/) und [Weißraum](../prinzip-weissraum/). Prüfen: [Unschärfetest](../methode-unschaerfetest/)." %}
''')

done(D, 'Was umschlossen, auf einer Fläche oder verbunden ist, gehört zusammen. Lücken ergänzen wir',
     'Geschlossenheit, Gemeinsame Region, Verbundenheit, Karte')
print('ok', D)
