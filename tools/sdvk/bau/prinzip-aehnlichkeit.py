# Bauskript für das Deck prinzip-aehnlichkeit
# Aufruf: python3 tools/sdvk/bau/prinzip-aehnlichkeit.py
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'prinzip-aehnlichkeit'
K = '#231f20'; G1 = '#888888'; G2 = '#d9d9d9'; L = '#9313ce'

intro(D, 'Ähnlichkeit', 'Prinzip // Gruppieren')

W(D, '010-regel.md', '''
---
title: "Ähnlichkeit"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Regel: Was gleich aussieht, gehört zusammen. Gleich heißt: gleiche Farbe, gleiche Form, gleiche Größe, gleiche Richtung, gleiche Textur. Jede visuelle Variable kann Ähnlichkeit stiften. Neben der Nähe das stärkste Gruppierungsprinzip.

  **Hintergrund**

  Das Gesetz der Ähnlichkeit gehört zu den Gestaltgesetzen, die Max Wertheimer 1923 in »Untersuchungen zur Lehre von der Gestalt II« (Psychologische Forschung 4) formuliert hat. Quellen: Lidwell, Holden & Butler, Universal Principles of Design (Similarity); Yablonski, Laws of UX (Law of Similarity).

  Im Interface ist Ähnlichkeit die Grundlage von Konsistenz: Was gleich aussieht, wird als gleich verstanden, also auch als gleich bedienbar. Darum sehen alle Links gleich aus und alle Buttons einer Sorte auch.
---

{% statement "Was gleich aussieht, gehört zusammen.", "Gesetz der Ähnlichkeit" %}
''')

# Abstrakt: 5 x 5 Raster, je eine Variable
xs = [120, 210, 300, 390, 480]
def raster(fill_fn, shape_fn, size_fn):
    out = []
    for r, y in enumerate(xs):
        for c, x in enumerate(xs):
            i = r * 5 + c
            s = size_fn(r)
            if shape_fn(r) == 'q':
                out.append(f'  <rect data-id="e{i}" x="{x-s}" y="{y-s}" width="{2*s}" height="{2*s}" fill="{fill_fn(r)}" />')
            else:
                out.append(f'  <circle data-id="e{i}" cx="{x}" cy="{y}" r="{s}" fill="{fill_fn(r)}" />')
    return '\n'.join(out)

def frame(bu, inner, w=600, h=600, stage='#ffffff'):
    return f"{{% frame '{{\"stage\":\"{stage}\", \"w\":{w}, \"h\":{h}, \"bu\":\"{bu}\"}}' %}}\n{inner}\n{{% endframe %}}\n"

alle = lambda r: K
kreis = lambda r: 'k'
gleich = lambda r: 18
f_basis = frame('Gleiche Elemente: ein Feld', raster(alle, kreis, gleich))
f_farbe = frame('Farbe: Sie sehen Zeilen', raster(lambda r: L if r % 2 else K, kreis, gleich))
f_form = frame('Form: wieder Zeilen', raster(alle, lambda r: 'q' if r % 2 else 'k', lambda r: 16 if r % 2 else 18))
f_groesse = frame('Größe: wieder Zeilen', raster(alle, kreis, lambda r: 10 if r % 2 else 24))

W(D, '020-abstrakt.md', f'''
---
title: "Ähnlichkeit abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Dieselben 25 Punkte, die Abstände bleiben immer gleich. Erst ein gleichmäßiges Feld. Dann ändert sich jedes Mal eine einzige visuelle Variable in jeder zweiten Zeile: Farbe, Form, Größe. Fragen: Was sehen Sie jetzt? Zeilen oder Spalten? Fast alle sehen sofort Zeilen, obwohl sich am Abstand nichts geändert hat.

  Farbe wirkt dabei am stärksten. Darum sollte sie nie das einzige Merkmal sein: Wer Farben schlecht unterscheidet, sieht bei der Farbvariante nur ein Feld (siehe Farbe codieren).
---

{f_basis}{f_farbe}{f_form}{f_groesse}''')

# Konflikt Nähe gegen Ähnlichkeit, 900 x 500
cx = [155, 205, 335, 385, 515, 565, 695, 745]
cy = [130, 210, 290, 370]
def konflikt(fill_fn):
    out = []
    for r, y in enumerate(cy):
        for c, x in enumerate(cx):
            out.append(f'  <circle data-id="k{r}{c}" cx="{x}" cy="{y}" r="16" fill="{fill_fn(r, c)}" />')
    return '\n'.join(out)
k1 = frame('Abstand: Paare von Spalten', konflikt(lambda r, c: K), 900, 500)
k2 = frame('Abstand sagt Spalten, Farbe sagt Zeilen. Was gewinnt?', konflikt(lambda r, c: L if r % 2 else K), 900, 500)
k3 = frame('Abstand und Farbe sagen dasselbe: eindeutig', konflikt(lambda r, c: L if (c // 2) % 2 else K), 900, 500)

W(D, '030-konflikt.md', f'''
---
title: "Nähe gegen Ähnlichkeit"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Erst nur Abstand: Die Spalten rücken paarweise zusammen, man sieht vier Doppelspalten. Dann wird jede zweite Zeile lila. Fragen: Was sehen Sie jetzt, Spalten oder Zeilen? Erfahrungsgemäß ist der Raum gespalten, und viele springen hin und her. Das ist das Problem: Zwei Prinzipien sagen Verschiedenes, das Bild wird mehrdeutig.

  Welches Prinzip gewinnt, hängt von der Stärke ab: wie groß der Abstandsunterschied ist, wie stark der Farbunterschied. Eine feste Rangfolge gibt es nicht. Die Lehre für die Gestaltung ist einfacher: Lassen Sie die Prinzipien dasselbe sagen. Die letzte Fassung färbt die Spaltenpaare ein, Abstand und Farbe verstärken sich.

  **Hintergrund**

  Versuche zur Konkurrenz von Nähe und Ähnlichkeit gibt es seit Wertheimer. Quinlan und Wilton (1998) zeigten zum Beispiel, dass das Ergebnis vom Verhältnis der Unterschiede abhängt (aus dem Gedächtnis, bitte prüfen).
---

{k1}{k2}{k3}''')

# Im Screen: Links und Buttons, 600 x 600 Format auf grauer Bühne
def text_zeilen(y0, breiten, links):
    """links: dict zeilenindex -> (x, w, stil)"""
    out = []
    for i, w in enumerate(breiten):
        y = y0 + i * 26
        out.append(f'  <rect x="90" y="{y}" width="{w}" height="12" fill="{G2}" />')
        if i in links:
            x, lw, stil, did = links[i]
            farbe = {'link': L, 'schwarz': K, 'grau': G1, 'betont': L}[stil]
            out.append(f'  <rect data-id="{did}" x="{x}" y="{y}" width="{lw}" height="12" fill="{farbe}" />')
            if stil in ('link', 'grau'):
                out.append(f'  <line data-id="{did}u" x1="{x}" y1="{y+18}" x2="{x+lw}" y2="{y+18}" stroke="{farbe}" stroke-width="3" stroke-linecap="round" />')
    return '\n'.join(out)

def screen(stile, buttons_einheitlich, badge):
    out = [f'  <rect x="90" y="90" width="300" height="22" fill="{G1}" />']
    if badge:
        out.append(f'  <rect data-id="badge" x="410" y="88" width="90" height="26" rx="13" fill="{L}" />')
    out.append(text_zeilen(140, [420, 400, 420, 260], {0: (190, 90, stile[0], 'a'), 2: (300, 80, stile[1], 'b')}))
    out.append(text_zeilen(270, [420, 380, 420, 300], {1: (150, 110, stile[2], 'c'), 3: (90, 70, stile[3], 'd')}))
    out.append(f'  <rect data-id="btn1" x="90" y="430" width="150" height="44" rx="22" fill="{L}" />')
    if buttons_einheitlich:
        out.append(f'  <rect data-id="btn2" x="260" y="431" width="150" height="42" rx="21" fill="#ffffff" stroke="{L}" stroke-width="2" />')
    else:
        out.append(f'  <rect data-id="btn2" x="260" y="430" width="150" height="44" fill="{K}" />')
    return '\n'.join(out)

s1 = frame('Was ist hier klickbar?', screen(['link', 'schwarz', 'betont', 'grau'], False, True), stage='#666666')
s2 = frame('Gleiches gleich: Links lila und unterstrichen, Buttons als Pille', screen(['link', 'link', 'link', 'link'], True, False), stage='#666666')

W(D, '040-im-screen.md', f'''
---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Artikel als Wireframe. In der ersten Fassung gibt es vier Hervorhebungen im Text, jede sieht anders aus: lila und unterstrichen, schwarz, lila ohne Linie, grau und unterstrichen. Dazu ein lila Etikett neben der Überschrift und zwei Buttons, die nichts miteinander zu tun haben. Fragen: Was davon ist klickbar? Die ehrliche Antwort: Man kann es nicht wissen, man muss es ausprobieren.

  Die zweite Fassung: Alle Links sehen gleich aus, lila und unterstrichen. Beide Buttons sind Pillen, einmal gefüllt, einmal mit Rahmen. Das Etikett ist weg, weil es wie ein Button aussah. Ähnlichkeit macht das Interface lernbar: Wer einen Link erkannt hat, erkennt alle.

  Mini-Übung danach, 3 Minuten zu zweit.
---

{s1}{s2}
{{% question "Woran erkennen Sie in Ihrer meistgenutzten App, was klickbar ist?", "Und wo sieht etwas klickbar aus, ohne es zu sein?" %}}
''')

W(D, '050-grenzen.md', '''
---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Ähnlichkeit ist ein Versprechen: Was gleich aussieht, funktioniert gleich. Wer es bricht, erzeugt Verwechslungen. Klassiker: Überschriften in derselben Farbe wie Links, ein Etikett, das wie ein Button aussieht, ein deaktivierter Button, der genauso aussieht wie ein aktiver.

  Die Gegenregel gehört dazu: Unterschiedliches unterschiedlich gestalten (Prinzip Konsistenz und Konventionen). Und wenn alles gleich aussieht, gibt es keine Gruppen mehr und keine Hierarchie: Monotonie. Bewusst bricht man Ähnlichkeit, um etwas hervorzuheben (siehe Kontrast und Hervorhebung).
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann wird Ähnlichkeit zum Problem?</h1>
    {% fragment '<p class="list">Wenn Verschiedenes gleich aussieht: Verwechslung.</p>' %}
    {% fragment '<p class="list">Wenn alles gleich aussieht: keine Gruppen, keine Hierarchie.</p>' %}
    {% fragment '<p class="list">Wenn die Ähnlichkeit nur über Farbe läuft: Nicht alle sehen sie.</p>' %}
  </div>
</section>
''')

# Die dunkle Seite: getarnte Anzeige, falsche Download-Buttons
def treffer(i, y, anzeige, markiert):
    out = []
    out.append(f'  <rect data-id="u{i}" x="90" y="{y}" width="140" height="10" fill="{G2}" />')
    if anzeige:
        farbe = L if markiert else G1
        out.append(f'  <rect data-id="ad" x="240" y="{y+1}" width="22" height="8" fill="{farbe}" />')
        if markiert:
            out.append(f'  <circle data-id="ring" cx="251" cy="{y+5}" r="22" fill="none" stroke="{L}" stroke-width="3" />')
    out.append(f'  <rect data-id="t{i}" x="90" y="{y+20}" width="300" height="16" fill="{G1}" />')
    out.append(f'  <rect data-id="a{i}" x="90" y="{y+46}" width="420" height="10" fill="{G2}" />')
    out.append(f'  <rect data-id="b{i}" x="90" y="{y+64}" width="340" height="10" fill="{G2}" />')
    return '\n'.join(out)

def suche(markiert):
    out = [f'  <rect data-id="feld" x="90" y="70" width="420" height="40" rx="20" fill="#ffffff" stroke="{G1}" stroke-width="2" />']
    for i, y in enumerate([150, 255, 360]):
        out.append(treffer(i, y, i == 0, markiert))
    return '\n'.join(out)

def pfeil(cx, cy, farbe='#ffffff'):
    return f'  <polyline points="{cx-10},{cy-2} {cx},{cy+8} {cx+10},{cy-2}" fill="none" stroke="{farbe}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" /><line x1="{cx}" y1="{cy-12}" x2="{cx}" y2="{cy+8}" stroke="{farbe}" stroke-width="4" stroke-linecap="round" />'

def download(markiert):
    out = [f'  <rect x="90" y="80" width="260" height="22" fill="{G1}" />',
           f'  <rect x="90" y="130" width="420" height="12" fill="{G2}" />',
           f'  <rect x="90" y="156" width="360" height="12" fill="{G2}" />',
           f'  <rect data-id="fake1" x="90" y="186" width="420" height="66" rx="33" fill="{K}" />',
           pfeil(300, 217)]
    farbe = L if markiert else G1
    out.append(f'  <rect data-id="echt" x="90" y="310" width="70" height="10" fill="{farbe}" />')
    out.append(f'  <line data-id="echtu" x1="90" y1="326" x2="160" y2="326" stroke="{farbe}" stroke-width="2" stroke-linecap="round" />')
    if markiert:
        out.append(f'  <circle data-id="ring2" cx="125" cy="318" r="44" fill="none" stroke="{L}" stroke-width="3" />')
    out.append(f'  <rect x="90" y="376" width="420" height="12" fill="{G2}" />')
    out.append(f'  <rect data-id="fake2" x="160" y="408" width="280" height="56" rx="28" fill="{K}" />')
    out.append(pfeil(300, 434))
    return '\n'.join(out)

d1 = frame('Drei Suchergebnisse?', suche(False), stage='#666666')
d2 = frame('Das erste ist eine Anzeige. Erkennbar nur an einer winzigen Markierung', suche(True), stage='#666666')
d3 = frame('Drei Downloads?', download(False), stage='#666666')
d4 = frame('Der echte Download ist der unscheinbarste. Die großen Buttons sind Werbung', download(True), stage='#666666')

W(D, '060-dunkle-seite.md', f'''
---
title: "Die dunkle Seite"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ähnlichkeit lässt sich gegen die Nutzenden einsetzen: Was wie ein Suchergebnis aussieht, wird angeklickt wie eines. Was wie ein Download-Button aussieht, auch.

  **Getarnte Anzeigen:** Anzeigen in Suchergebnissen, Feeds und Nachrichtenseiten übernehmen Aufbau, Schrift und Farben der echten Inhalte. Unterscheidbar sind sie oft nur durch ein kleines Wort wie »Gesponsert« oder »Anzeige«. Je ähnlicher die Anzeige, desto mehr Klicks, und genau das ist der Zweck. Suchmaschinen haben ihre Kennzeichnung über die Jahre immer unauffälliger gemacht, von einer farbigen Fläche hinter den Anzeigen bis zu einem kleinen Wort (aus dem Gedächtnis, bitte prüfen).

  **Falsche Download-Buttons:** Auf Download-Portalen stehen große Werbeflächen, die wie der eigentliche Download aussehen. Der echte Link ist klein und unscheinbar. Wer den falschen erwischt, landet bei Werbung oder installiert etwas, das er nicht wollte.

  Prüffrage für den eigenen Entwurf: Wem nützt diese Ähnlichkeit? Hilft sie den Nutzenden, etwas wiederzuerkennen, oder soll sie sie täuschen?

  **Hintergrund**

  Harry Brignull nennt das Muster »Disguised Ads« (Deceptive Patterns, 2023, und deceptive.design). Werbung muss in Deutschland und der EU als solche erkennbar sein (Trennungsgebot, Gesetz gegen den unlauteren Wettbewerb, für Plattformen auch der Digital Services Act). Die Wireframes sind erfunden, das Muster ist es nicht.
---

{{% interlude "Die dunkle Seite", "Was wie ein Suchergebnis aussieht, wird angeklickt wie eines." %}}

{d1}{d2}{d3}{d4}
{{% question "Wem nützt diese Ähnlichkeit?", "Den Nutzenden, die etwas wiedererkennen sollen? Oder dem, der für den Klick bezahlt wird?" %}}
''')

W(D, '070-verweise.md', '''
---
title: "Verweise"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dahinter: Gestaltpsychologie. Weiter: Nähe und Abstand, Konsistenz und Konventionen, Kontrast und Hervorhebung, Farbe codieren. Prüfen: Unschärfetest.
---

{% statement "Verweise", "Dahinter: [Gestaltpsychologie](../prinzip-gestaltpsychologie/). Weiter: [Nähe und Abstand](../prinzip-naehe-und-abstand/), [Konsistenz und Konventionen](../prinzip-konsistenz-und-konventionen/), [Kontrast und Hervorhebung](../prinzip-kontrast-und-hervorhebung/) und [Farbe codieren](../prinzip-farbe-codieren/). Prüfen: [Unschärfetest](../methode-unschaerfetest/)." %}
''')

done(D, 'Was gleich aussieht, gehört zusammen, und wird als gleich bedienbar verstanden',
     'Gesetz der Ähnlichkeit, Gruppierung, Konsistenz, Getarnte Anzeige')
p = f'{NEW}/{D}/index.md'; s = open(p).read()
s = s.replace('  - "Gesetz der Ähnlichkeit"\n', '  - "Gesetz der Ähnlichkeit"\n  - "Nähe gegen Ähnlichkeit"\n  - "Die dunkle Seite: getarnte Anzeigen"\n')
open(p, 'w').write(s)
print('ok', D)
