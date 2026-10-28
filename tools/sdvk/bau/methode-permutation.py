exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
import random
D = 'methode-permutation'

intro(D, 'Permutation', 'Methode // Variieren')

SCHWARZ, GRAU, HELL, LILA = '#231f20', '#888888', '#d9d9d9', '#9313ce'

# ---------------------------------------------------------------- Bausteine
# Modul aus der Übung: Quadrat mit einem Viertelring in der linken oberen Ecke (außen Schwarz, innen Lila)
def ring(r0, r1, farbe):
    return (f'<path d="M {r1},0 A {r1} {r1} 0 0 1 0,{r1} L 0,{r0} A {r0} {r0} 0 0 0 {r0},0 Z" fill="{farbe}" />')

def modul(T):
    return (f'<rect x="0" y="0" width="{T}" height="{T}" fill="{HELL}" />'
            + ring(T * 0.5, T * 0.68, SCHWARZ) + ring(T * 0.32, T * 0.5, LILA))

def kachel(i, x, y, T, rot):
    return (f'<g data-id="k{i}" transform="translate({x + T / 2:.1f},{y + T / 2:.1f}) rotate({rot}) translate({-T / 2:.1f},{-T / 2:.1f})">'
            + modul(T) + '</g>')

def feld(regel, n=6, T=80, w=600):
    off = (w - n * T) / 2
    out = []
    for r in range(n):
        for c in range(n):
            out.append(kachel(r * n + c, off + c * T, off + r * T, T, regel(r, c)))
    return '\n'.join(out)

KREISE = [[180, 270], [90, 0]]
REGELN = {
    'gleich':    lambda r, c: 0,
    'kreise':    lambda r, c: KREISE[r % 2][c % 2],
    'schach':    lambda r, c: [0, 180][(r + c) % 2],
    'wellen':    lambda r, c: (c % 2) * 90 + (r % 2) * 180,
}
random.seed(7)
ZUFALL = [[random.choice([0, 90, 180, 270]) for c in range(6)] for r in range(6)]
REGELN['zufall'] = lambda r, c: ZUFALL[r][c]

# Viertelkreis für die Superformen (wie im Beispiel der Aufgabe)
def viertel(x, y, T, rot, farbe=SCHWARZ, did=None):
    d = f' data-id="{did}"' if did else ''
    return (f'<g{d} transform="translate({x + T / 2},{y + T / 2}) rotate({rot}) translate({-T / 2},{-T / 2})">'
            f'<path d="M 0,{T} L 0,0 A {T} {T} 0 0 1 {T},{T} Z" fill="{farbe}" /></g>')

def frame(inner, bu, w=600, h=600):
    # Kein Auto-Animate: Reveal kann gedrehte SVG-Gruppen nicht überblenden, übrig bliebe eine einzige Kachel
    return "{% frame '{\"stage\":\"#ffffff\", \"animate\":false, \"w\":" + str(w) + ", \"h\":" + str(h) + ", \"bu\":\"" + bu + "\"}' %}\n" + inner + "\n{% endframe %}"

# ---------------------------------------------------------------- Problem
W(D, '005-problem.md', '''
---
title: "Das Problem"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Ein einziges Modul: ein Quadrat mit einem Viertelring in der Ecke. Frage ans Publikum: Wie viele verschiedene Formen stecken darin?

  Die meisten denken zuerst an eine Handvoll. Tatsächlich reicht schon ein Feld aus 2 × 2 Kacheln mit vier möglichen Drehungen pro Kachel für 4 hoch 4, also 256 Kombinationen. Bei einem Feld aus 6 × 6 Kacheln sind es mehr, als man je ausprobieren könnte.

  Das Problem ist also nicht, dass es zu wenige Möglichkeiten gibt, sondern zu viele. Wer ohne Regel probiert, landet beim Zufall oder bei der ersten Variante, die halbwegs gefällt. Permutation ist das Verfahren, mit dem man diesen Raum systematisch durchquert.
---

''' + frame(kachel(0, 200, 200, 200, 0), 'Ein Modul') + '''

{% statement "Ein Modul, unendlich viele Formen.", "Das Problem ist nicht, dass es zu wenige Möglichkeiten gibt, sondern zu viele. Permutation bringt eine Regel ins Spiel." %}
''')

# ---------------------------------------------------------------- Ergebnis zuerst
W(D, '010-ergebnis.md', '''
---
title: "Ergebnis zuerst"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Viermal dasselbe Modul, 36 Kacheln, keine einzige neue Form. Es ändert sich nur die Regel, nach der die Kacheln gedreht werden:

  1. **Alle gleich:** Jede Kachel liegt gleich. Es entsteht ein ruhiges, diagonales Muster.
  2. **Je vier um einen Punkt:** Vier Kacheln drehen sich um eine gemeinsame Ecke. Es entstehen geschlossene Ringe. Hier wirkt das Gesetz der Geschlossenheit.
  3. **Schachbrett:** 0° und 180° im Wechsel wie auf einem Schachbrett. Aus den Ringstücken werden durchgehende diagonale Linien. Hier wirkt die gute Fortsetzung.
  4. **Wellen:** Jede zweite Spalte um 90° gedreht, jede zweite Zeile um 180°. Es entstehen Wellen, also Bewegung und Rhythmus.

  Das ist das Ergebnis der Methode: eine Reihe von Varianten, jede mit einer benennbaren Regel. Daraus wählt man aus, und zwar begründet.
---

''' + frame(feld(REGELN['gleich']), '1. Alle gleich') + '''

''' + frame(feld(REGELN['kreise']), '2. Je vier um einen Punkt') + '''

''' + frame(feld(REGELN['schach']), '3. Schachbrett: 0° und 180° im Wechsel') + '''

''' + frame(feld(REGELN['wellen']), '4. Wellen: jede zweite Spalte 90°, jede zweite Zeile 180°') + '''
''')

# ---------------------------------------------------------------- Schritte
lagen = '\n'.join(viertel(60 + i * 130, 220, 100, i * 90, did=f'v{i}') for i in range(4))
superformen = '\n'.join([
    # Kreis
    viertel(60, 60, 80, 270), viertel(140, 60, 80, 0), viertel(60, 140, 80, 180), viertel(140, 140, 80, 90),
    # Blatt
    viertel(330, 60, 80, 270), viertel(410, 140, 80, 90),
    # Sanduhr
    viertel(60, 330, 80, 90), viertel(140, 330, 80, 180), viertel(60, 410, 80, 0), viertel(140, 410, 80, 270),
    # Halbkreis
    viertel(330, 370, 80, 270), viertel(410, 370, 80, 0),
])

W(D, '020-schritte.md', '''
---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **1. Modul festlegen:** eine Form, wenige Farben. Je einfacher das Modul, desto deutlicher sieht man, was die Regel bewirkt.

  **2. Operationen wählen:** Was darf sich ändern? Drehen (meist in 90°-Schritten), spiegeln, verschieben, Farbe tauschen. Alles andere bleibt fest. Die Zahl der Elemente bleibt gleich, es kommt nichts Neues dazu.

  **3. Regel formulieren:** in einem Satz, den man laut sagen kann. »0° und 180° im Wechsel wie auf einem Schachbrett.« »Vier Kacheln drehen sich um eine gemeinsame Ecke.«

  **4. Durchspielen:** Die Regel konsequent anwenden und mehrere Regeln nebeneinanderstellen. Nicht bei der ersten Variante stehen bleiben, die halbwegs gefällt.

  **5. Auswählen und brechen:** Die stärkste Variante auswählen und begründen. Wer will, bricht die Regel an einer Stelle bewusst. Das ist dann eine Störung, siehe Pop-out.

  **Superform:** Die Form, die aus mehreren Modulen zusammen entsteht. Aus einem Viertelkreis werden durch Drehen Kreis, Blatt, Sanduhr und Halbkreis.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Permutation in fünf Schritten</h1>
    {% fragment '<p class="list"><strong>1. Modul festlegen:</strong> eine Form, wenige Farben</p>' %}
    {% fragment '<p class="list"><strong>2. Operationen wählen:</strong> drehen, spiegeln, verschieben, Farbe tauschen</p>' %}
    {% fragment '<p class="list"><strong>3. Regel formulieren:</strong> in einem Satz, den man laut sagen kann</p>' %}
    {% fragment '<p class="list"><strong>4. Durchspielen:</strong> mehrere Regeln nebeneinander, nicht die erste nehmen</p>' %}
    {% fragment '<p class="list"><strong>5. Auswählen und brechen:</strong> begründet wählen, die Regel bewusst an einer Stelle brechen</p>' %}
  </div>
</section>

''' + frame(lagen, 'Ein Viertelkreis in vier Lagen: 0°, 90°, 180°, 270°') + '''

''' + frame(superformen, 'Superformen: Aus einem Modul entstehen durch Drehen neue Formen') + '''
''')

# ---------------------------------------------------------------- Mini-Übung
W(D, '030-uebung.md', '''
---
title: "Mini-Übung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Mini-Übung (ca. 5 Minuten), auf Papier**

  Ein Raster aus 2 × 2 Kästchen zeichnen, das Modul vom Anfang hineinsetzen, jede Kachel darf gedreht werden. Wie viele verschiedene Superformen finden Sie in fünf Minuten? Zu zweit, eine Person zeichnet, die andere formuliert die Regel.

  Danach drei Paare zeigen lassen und jeweils die Regel in einem Satz sagen lassen. Auflösung: 256 Kombinationen sind möglich (4 hoch 4), durch Symmetrie sehen viele davon gleich aus.

  Überleitung zur Übung »Permutation mit Flächenausschnitten«: Dort machen Sie dasselbe in Figma, mit der Vorlage und auf einer großen Fläche.
---

{% question "Wie viele Superformen finden Sie?", "Raster aus 2 × 2 Kästchen, ein Modul, nur drehen. Zu zweit, fünf Minuten. Und zu jeder Form: Wie heißt die Regel?" %}
''')

# ---------------------------------------------------------------- Typische Fehler
W(D, '040-fehler.md', '''
---
title: "Typische Fehler"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Der häufigste Fehler: Zufall statt Regel. Ein zufällig gedrehtes Feld sieht auf den ersten Blick lebendig aus, aber man kann es nicht begründen, nicht wiederholen und nicht gezielt verbessern. Die Folie zeigt dasselbe Modul, zufällig gedreht. Vergleich mit den Regeln vom Anfang: Wo entsteht eine Gestalt, wo nur Rauschen?

  Ebenfalls häufig: die erste Variante nehmen, die halbwegs gefällt. Oder zu viel auf einmal ändern: Drehen, Farbe und Position gleichzeitig. Dann sieht man nicht mehr, welche Operation welche Wirkung hat.
---

''' + frame(feld(REGELN['zufall']), 'Zufällig gedreht: lebendig, aber ohne Gestalt') + '''

<section class="simple" data-transition="fade">
  <div>
    <h1>Typische Fehler</h1>
    {% fragment '<p class="list">Zufall statt Regel: nicht begründbar, nicht wiederholbar</p>' %}
    {% fragment '<p class="list">Die erste Variante nehmen, die halbwegs gefällt</p>' %}
    {% fragment '<p class="list">Zu viel auf einmal ändern: Man sieht nicht mehr, was wirkt</p>' %}
    {% fragment '<p class="list">Neue Elemente dazunehmen: Dann ist es keine Permutation mehr</p>' %}
    {% fragment '<p class="list">Am Detail hängen statt auf die Gesamtform zu schauen</p>' %}
  </div>
</section>
''')

# ---------------------------------------------------------------- Einsatz
W(D, '050-einsatz.md', '''
---
title: "Einsatz"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Permutation hilft überall dort, wo aus wenigen Elementen viele Varianten entstehen sollen: Muster und Hintergründe, Icons und Bildzeichen aus einem gemeinsamen Baukasten, Layoutvarianten aus denselben Bausteinen. Sie ist die einfachste Form des systematischen Variierens. Der Morphologische Kasten treibt dasselbe Prinzip weiter, mit mehreren Eigenschaften gleichzeitig.

  **Hintergrund**

  Der französische Dominikanermönch Sébastien Truchet untersuchte 1704 in »Mémoire sur les combinaisons«, welche Muster sich aus einer einzigen, diagonal geteilten Fliese durch Drehen ergeben. Solche Kacheln heißen bis heute Truchet-Kacheln. Die Variante mit Viertelkreisen geht auf Cyril Stanley Smith zurück, »The Tiling Patterns of Sébastien Truchet and the Topology of Structural Hierarchy« (Leonardo, 1987).

  In der Gestaltung hat Karl Gerstner das regelbasierte Entwerfen geprägt: »Programme entwerfen« (1964). Statt einer Lösung entwirft man ein Programm, aus dem viele Lösungen hervorgehen. Heute lebt der Gedanke in der generativen Gestaltung weiter.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wo die Methode wiederkommt</h1>
    {% fragment '<p class="list">Muster und Flächen aus einem Modul</p>' %}
    {% fragment '<p class="list">Icons und Bildzeichen aus einem gemeinsamen Baukasten</p>' %}
    {% fragment '<p class="list">Layoutvarianten aus denselben Bausteinen</p>' %}
    {% fragment '<p class="list">Weiter mit dem Morphologischen Kasten: mehrere Eigenschaften gleichzeitig variieren</p>' %}
  </div>
</section>

{% statement "Merksatz", "Wenige Elemente, eine Regel, viele Varianten. Und dann begründet auswählen." %}
''')

done(D, 'Aus wenigen Elementen nach einer Regel systematisch viele Varianten erzeugen', 'Permutation, Modul, Superform, Regel, Truchet-Kachel')
p = f'{NEW}/{D}/index.md'; s = open(p).read()
s = s.replace('''inhalt:
  - "Drehen, spiegeln, umstellen nach Regel"''', '''inhalt:
  - "Ein Modul, viele Formen"
  - "Ergebnis zuerst: vier Regeln"
  - "Fünf Schritte, Superformen"
  - "Mini-Übung"
  - "Typische Fehler"''').replace('einsatz: ""', 'einsatz: "Muster, Bildzeichen und Layoutvarianten aus wenigen Bausteinen"')
open(p, 'w').write(s)
print('fertig')
