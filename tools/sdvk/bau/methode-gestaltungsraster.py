# Bauskript methode-gestaltungsraster. Aufruf: python3 tools/sdvk/bau/methode-gestaltungsraster.py
import glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'methode-gestaltungsraster'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Gestaltungsraster', 'Methode // Konstruieren')
imgs(D, 'typographie', ['historie-15.png'])
imgs(D, 'layout', ['layout-10.png', 'layout-11.png'])

L = '#9313ce'; FL = '#e4e4e4'; BI = '#c4c4c4'; TX = '#aaaaaa'; HL = '#888888'; K = '#231f20'
# Desktop 1440 x 800 im Maßstab 0,625: Rand 80 -> 50, Spaltenabstand 24 -> 15
S = 0.625; W0 = 900; H0 = 500; M = 50; G = 15; N = 12
CW = (W0 - 2 * M - (N - 1) * G) / N
cx = lambda c: M + c * (CW + G)
span = lambda a, b: cx(b) + CW - cx(a)

def spalten(op, did='col'):
    return ''.join(f'<rect data-id="{did}{c}" x="{cx(c):.1f}" y="0" width="{CW:.1f}" height="{H0}" fill="{L}" fill-opacity="{op}" />\n' for c in range(N))

def rand(op):
    return (f'<rect data-id="rand-l" x="0" y="0" width="{M}" height="{H0}" fill="{L}" fill-opacity="{op}" />\n'
            f'<rect data-id="rand-r" x="{W0 - M}" y="0" width="{M}" height="{H0}" fill="{L}" fill-opacity="{op}" />\n')

def r(did, x, y, w, h, f, rx=0):
    return f'<rect data-id="{did}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{f}" rx="{rx}" />\n'

def text(raster=True):
    if raster:
        x, w = cx(0), span(0, 5)
    else:
        x, w = 70, 300
    o = r('h1', x, 50, w * 0.8, 24, HL)
    for i in range(4):
        o += r(f'tx{i}', x, 92 + i * 18, w if i < 3 else w * 0.6, 9, TX)
    return o

def karten(raster=True):
    o = ''
    if raster:
        rects = [(cx(0), span(0, 3)), (cx(4), span(4, 7)), (cx(8), span(8, 11))]
        ys = [200, 200, 200]; hs = [240, 240, 240]
    else:
        rects = [(60, 245), (330, 270), (625, 225)]
        ys = [190, 210, 200]; hs = [240, 220, 250]
    for i, ((x, w), y, h) in enumerate(zip(rects, ys, hs)):
        o += r(f'k{i}', x, y, w, h, FL)
        o += r(f'kb{i}', x + 12, y + 12, w - 24, h * 0.5, BI)
        o += r(f'kt{i}', x + 12, y + h * 0.5 + 26, (w - 24) * 0.8, 12, HL)
        o += r(f'kx{i}', x + 12, y + h * 0.5 + 50, w - 24, 8, TX)
        o += r(f'kl{i}', x + 12, y + h * 0.5 + 72, 60, 16, L, 8)
    return o

def fq(bu, svg, animate=True):
    a = '' if animate else '"animate":false,'
    return "{% frame '{" + a + "\"w\":900, \"h\":500, \"bu\":\"" + bu + "\"}' %}\n" + svg + "{% endframe %}"

# ---------------------------------------------------------------- Problem
W(D, '005-problem.md', '''
---
title: "Das Problem"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Wie ein Raster aufgebaut ist, wissen Sie seit dem Workshop Raum und Anordnungen: Spalten, Spaltenabstände, Rand, Module. Heute geht es um die Frage danach: Woher kommen die Zahlen? Warum zwölf Spalten und nicht neun? Warum 24 Pixel Spaltenabstand?

  Die Antwort ist unbequem: Es gibt kein Standardraster, das immer passt. Frameworks bringen eines mit, aber das kennt Ihren Inhalt nicht. Ein gutes Raster wird aus dem Inhalt abgeleitet: Wie breit muss der Lesetext sein? Wie viele Cards sollen nebeneinander stehen? Wie groß ist das kleinste Element?
---

{% interlude "Woher kommen die Zahlen?", "Warum zwölf Spalten? Warum 24 Pixel Spaltenabstand?" %}

{% statement "Das Raster folgt dem Inhalt.", "Nicht umgekehrt. Ein Raster von der Stange kennt Ihren Text, Ihre Bilder und Ihre Cards nicht." %}
''')

# ---------------------------------------------------------------- Ergebnis zuerst: vorher, nachher
W(D, '010-ergebnis.md', '''
---
title: "Ergebnis zuerst"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Vorher und nachher. Eine Startseite mit Überschrift, Text und drei Cards, erst nach Augenmaß gesetzt. Nichts ist falsch, aber nichts passt zusammen: Die Cards sind unterschiedlich breit, die Abstände zufällig, der Text endet irgendwo.

  Dann dasselbe auf einem Raster mit zwölf Spalten. Der Text belegt sechs Spalten, jede Card vier. Zum Schluss verschwindet das Raster wieder. Gesehen wird es nicht, gespürt schon.

  Das ist das Ergebnis der Methode: ein Raster, in dem jedes Element einen begründeten Platz hat.
---

{% interlude "Vorher, nachher", "Dieselbe Seite, einmal ohne und einmal mit Raster" %}

''' + '\n'.join([
    fq('Vorher: nach Augenmaß', spalten(0) + text(False) + karten(False)),
    fq('Nachher: auf zwölf Spalten', spalten(0.12) + text() + karten()),
    fq('Das Raster verschwindet, die Ordnung bleibt', spalten(0) + text() + karten()),
]) + '\n')

# ---------------------------------------------------------------- Schritte: Aufbau
lines8 = lambda op: ''.join(f'<line data-id="g{i}" x1="0" y1="{y:.1f}" x2="{W0}" y2="{y:.1f}" stroke="{L}" stroke-opacity="{op}" stroke-width="1" />\n'
                             for i, y in enumerate([j * 24 * S for j in range(1, int(H0 / (24 * S)) + 1)]))
def module(op, mark):
    RH = 3 * 24 * S * 2  # 6 Grundlinien je Modul
    o = ''
    for c in range(N):
        for row in range(4):
            y = 20 + row * (RH + G)
            if y + RH > H0 - 20: continue
            f = L if (mark and c in (4, 5) and row == 1) else L
            op2 = 0.85 if (mark and c in (4, 5) and row == 1) else op
            o += f'<rect data-id="m{c}-{row}" x="{cx(c):.1f}" y="{y:.1f}" width="{CW:.1f}" height="{RH:.1f}" fill="{f}" fill-opacity="{op2}" />\n'
    return o

lese = r('h1', cx(0), 50, span(0, 5) * 0.8, 24, HL) + ''.join(r(f'tx{i}', cx(0), 92 + i * 18, span(0, 5) if i < 3 else span(0, 5) * 0.6, 9, TX) for i in range(4))
W(D, '020-schritte.md', '''
---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Ein Raster entsteht Schritt für Schritt, und jeder Schritt hat einen Grund.

  **1. Format:** Für welche Breite? Desktop 1440, Tablet 834, Smartphone 390 Pixel sind gute Ausgangspunkte. Ein Raster pro Format.

  **2. Rand:** Wie viel Luft braucht der Inhalt zur Kante? Auf großen Formaten mehr, auf kleinen weniger.

  **3. Inhalt messen:** Der Lesetext gibt die wichtigste Breite vor: 45 bis 75 Zeichen pro Zeile (siehe Lesetext). Bei 18 Pixel Schrift sind das etwa 600 Pixel. Und: Wie viele Cards sollen nebeneinander stehen?

  **4. Spalten und Spaltenabstand:** So viele Spalten, dass sich beides sauber abbilden lässt. Zwölf sind beliebt, weil sich zwölf durch zwei, drei, vier und sechs teilen lässt. Der Text belegt sechs Spalten, eine Card vier. Der Spaltenabstand ist so breit wie der Abstand, der zwischen zwei Cards stehen soll.

  **5. Grundlinie:** Für die Senkrechte ein feines Raster, meist in Schritten von 8 Pixeln (hier 24 Pixel für den Zeilenabstand). Höhen und Abstände rasten darauf ein.

  **6. Module:** Wer Bilder und Kacheln in festen Höhen braucht, fasst Spalten und Zeilen zu Modulen zusammen. Hier belegt ein Element zwei Module nebeneinander.

  Der Lila-Ton zeigt in jeder Folie nur, was neu ist. Die Pixelwerte sind im Maßstab 0,625 gezeichnet, die Rechnung steht auf der übernächsten Folie.
---

{% interlude "Schritt für Schritt", "Vom leeren Format zum Raster" %}

''' + '\n'.join([
    fq('1. Das Format', ''),
    fq('2. Der Rand: Luft zur Kante', rand(0.35)),
    fq('3. Den Inhalt messen: Der Lesetext braucht 45 bis 75 Zeichen', rand(0.12) + lese),
    fq('4. Spalten und Spaltenabstand: Der Text belegt sechs Spalten, eine Card vier', rand(0) + spalten(0.15) + lese + karten()),
    fq('5. Die Grundlinie: Höhen und Abstände rasten senkrecht ein', spalten(0.08) + lines8(0.45) + lese + karten()),
    fq('6. Module: Spalten und Zeilen ergeben Felder', module(0.12, True)),
]) + '''

<section class="simple" data-transition="fade">
  <div>
    <h1>Ein Raster in sechs Schritten</h1>
    {% fragment '<p class="list"><strong>1. Format:</strong> ein Raster pro Breite</p>' %}
    {% fragment '<p class="list"><strong>2. Rand:</strong> Luft zur Kante</p>' %}
    {% fragment '<p class="list"><strong>3. Inhalt messen:</strong> Lesetext, Cards, kleinstes Element</p>' %}
    {% fragment '<p class="list"><strong>4. Spalten und Spaltenabstand:</strong> so viele, dass der Inhalt aufgeht</p>' %}
    {% fragment '<p class="list"><strong>5. Grundlinie:</strong> ein feines Raster für die Senkrechte</p>' %}
    {% fragment '<p class="list"><strong>6. Module:</strong> nur wenn feste Höhen gebraucht werden</p>' %}
  </div>
</section>
''')

# ---------------------------------------------------------------- Satzspiegel
W(D, '030-satzspiegel.md', '''
---
title: "Satzspiegel"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Idee ist älter als jeder Bildschirm. Im Buch heißt die Fläche, auf der Text steht, Satzspiegel. Die Ränder heißen Stege: Bundsteg innen, Kopfsteg oben, Außensteg und Fußsteg. Der Fußsteg ist der größte. Dieselbe Regel kennen Sie aus unseren Wireframes als Fundament: unten mehr Luft als oben.

  Die Gutenberg-Bibel (um 1454) zeigt es schon: zwei Spalten, ein Spaltenabstand, Ränder in festen Verhältnissen. Die Diagonalen helfen beim Konstruieren: Ein klassisches Verfahren teilt die Seite über die Diagonalen der Doppelseite, sodass Satzspiegel und Seite dasselbe Seitenverhältnis haben (Villardsche Figur, für die Buchgestaltung bekannt gemacht von Jan Tschichold).

  Bilder aus den bisherigen Foliensätzen Typographie und Layout.

  **Hintergrund**

  Villard de Honnecourt war ein Baumeister des 13. Jahrhunderts, die Figur ist nach ihm benannt. Tschichold hat die Konstruktion Mitte des 20. Jahrhunderts für die Buchgestaltung beschrieben (bitte prüfen). Zum Weiterlesen: Lupton, Thinking with Type (Grid).
---

{% interlude "Älter als jeder Bildschirm", "Der Satzspiegel im Buch" %}

{% screenshot "./images/historie-15.png", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Zwei Spalten, ein Spaltenabstand, feste Ränder: der Satzspiegel der Gutenberg-Bibel<br><small>Um 1454, Bild aus dem bisherigen Foliensatz</small>"}' %}
{% screenshot "./images/layout-10.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Die Stege: Der Fußsteg ist der größte. Unten mehr Luft als oben"}' %}
{% screenshot "./images/layout-11.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Konstruiert über die Diagonalen der Doppelseite"}' %}
''')

# ---------------------------------------------------------------- Rechnen
W(D, '040-rechnen.md', '''
---
title: "Rechnen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Spaltenbreite ist keine Eingabe, sie ergibt sich: Breite minus beide Ränder minus alle Spaltenabstände, geteilt durch die Zahl der Spalten.

  Desktop: (1440 − 2 × 80 − 11 × 24) ÷ 12 = 1016 ÷ 12 = 84,67 px.
  Tablet: (834 − 2 × 40 − 7 × 24) ÷ 8 = 586 ÷ 8 = 73,25 px.
  Smartphone: (390 − 2 × 20 − 3 × 16) ÷ 4 = 302 ÷ 4 = 75,5 px.

  Krumme Werte sind normal. In Figma (Stretch) und in CSS (1fr) werden die Spalten ohnehin gestreckt. Was zählt, sind Rand und Spaltenabstand: Die bleiben fest und kommen aus Ihrem Spacing-System.

  Probe für den Lesetext: Sechs Spalten auf dem Desktop sind 6 × 84,67 + 5 × 24 = 628 px. Bei 18 px Schrift sind das grob 70 Zeichen. Passt.

  Dieselben Werte stehen in der Aufgabe »Textsatz für NOXA Analytik«.
---

{% interlude "Rechnen Sie mit", "Die Spaltenbreite ergibt sich" %}

<section class="simple" data-transition="fade">
<div>

# Spaltenbreite = (Breite − 2 × Rand − Spaltenabstände) ÷ Spalten

| Format | Breite | Spalten | Rand | Spaltenabstand | Spalte |
|---|---|---|---|---|---|
| **Desktop** | 1440 px | 12 | 80 px | 24 px | 84,67 px |
| **Tablet hoch** | 834 px | 8 | 40 px | 24 px | 73,25 px |
| **Smartphone** | 390 px | 4 | 20 px | 16 px | 75,5 px |

</div>
</section>

{% statement "Rand und Spaltenabstand legen Sie fest. Die Spalte ergibt sich.", "Krumme Spaltenbreiten sind normal, Figma und CSS strecken sie ohnehin. Probe: Sechs Spalten auf dem Desktop ergeben 628 px, gut 70 Zeichen Lesetext." %}
''')

# ---------------------------------------------------------------- Figma
W(D, '050-figma.md', '''
---
title: "In Figma"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  In Figma heißt das Raster Layout Guide (früher Layout Grid). Es hängt immer an einem Frame.

  - Frame auswählen, rechts bei Layout guide auf Plus.
  - Typ Columns: Count (Zahl der Spalten), Type Stretch, Margin (Rand), Gutter (Spaltenabstand).
  - Stretch streckt die Spalten über die Breite, Center hält sie in fester Breite in der Mitte, Left und Right richten sie an einer Kante aus.
  - Ein zweiter Layout Guide vom Typ Rows für die Zeilen, ein dritter vom Typ Grid (8 px) für die Grundlinie.
  - Ein- und ausblenden: auf dem Mac Ctrl + G (bitte am Rechner prüfen).
  - Das Raster als Style speichern, dann gilt es für alle Frames gleich.

  In CSS ist es dieselbe Struktur: grid-template-columns: repeat(12, 1fr), gap für den Spaltenabstand, padding für den Rand. Siehe Prinzip Ausrichtung und Raster.
---

{% interlude "In Figma", "Das Raster heißt dort Layout Guide" %}

<section class="simple" data-transition="fade">
<div>

# Layout Guide

| Einstellung | Bedeutung |
|---|---|
| **Columns, Count** | Zahl der Spalten |
| **Type: Stretch** | Spalten strecken sich über die Breite |
| **Type: Center** | Spalten in fester Breite, mittig |
| **Margin** | Rand |
| **Gutter** | Spaltenabstand |
| **Rows, Grid** | Zeilen und Grundlinie |

</div>
</section>
''')

# ---------------------------------------------------------------- Mini-Übung
W(D, '060-uebung.md', '''
---
title: "Mini-Übung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Mini-Übung (5 Minuten), direkt in der Vorlage für heute.**

  Jede Person legt auf dem Frame der Card-Übersicht ein Raster an: 12 Spalten, Stretch, Rand 80, Spaltenabstand 24. Dazu ein Grid mit 8 px für die Grundlinie. Dann prüfen: Passen drei Cards nebeneinander auf je vier Spalten? Oder vier Cards auf je drei Spalten? Wie breit wird eine Card dann?

  Auflösung: drei Cards je 4 Spalten = 4 × 84,67 + 3 × 24 = 410,67 px. Vier Cards je 3 Spalten = 3 × 84,67 + 2 × 24 = 302 px.

  Kurz zeigen lassen, wer was gewählt hat und warum. Das ist die erste Entscheidung für die Varianten danach.
---

{% interlude "Und jetzt Sie", "Fünf Minuten, in der Vorlage für heute" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Legen Sie das Raster für die Card-Übersicht an</h1>
    {% fragment '<p class="list"><strong>Columns:</strong> 12, Stretch, Margin 80, Gutter 24</p>' %}
    {% fragment '<p class="list"><strong>Grid:</strong> 8 px für die Grundlinie</p>' %}
    {% fragment '<p class="list"><strong>Entscheiden:</strong> drei Cards auf je vier Spalten oder vier Cards auf je drei?</p>' %}
  </div>
</section>
''')

# ---------------------------------------------------------------- Fehler
W(D, '070-fehler.md', '''
---
title: "Typische Fehler"
layout: presentation.11ty.js
slideClasses: simple
status: ok
speaker: |
  Der häufigste Fehler: das Raster anlegen und dann nicht benutzen. Elemente stehen »fast« auf der Kante. Der zweithäufigste: das Raster des Frameworks übernehmen, ohne zu prüfen, ob der Text darin gut lesbar ist.

  Und: Der Spaltenabstand ist nicht beliebig. Er ist der wichtigste Abstand auf der Seite und gehört ins Spacing-System.
---

{% fragment '<p class="list">Das Raster anlegen und nicht benutzen: Elemente stehen »fast« auf der Kante</p>' %}
{% fragment '<p class="list">Ein Raster von der Stange übernehmen, ohne den Inhalt zu messen</p>' %}
{% fragment '<p class="list">Spaltenabstand und Rand nach Gefühl statt aus dem Spacing-System</p>' %}
{% fragment '<p class="list">Ein Raster für alle Formate, statt eines pro Breite</p>' %}
{% fragment '<p class="list">Die Senkrechte vergessen: Höhen und Abstände ohne Grundlinie</p>' %}
''')

# ---------------------------------------------------------------- Einsatz
W(D, '080-einsatz.md', '''
---
title: "Einsatz"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Können-Methode. Sie kommt heute in der Übung zum Einsatz, im Dezember beim Thema Layout wieder und im Projekt für jeden Screen. Im Code wird das Raster eins zu eins mit CSS Grid umgesetzt.

  Dahinter: Prinzip Ausrichtung und Raster (Anatomie, Rasterbruch, CSS Grid). Daneben: Spacing-System für Rand und Spaltenabstand. Prüfen: Lesetext für die Zeilenlänge.
---

{% statement "Erst den Inhalt messen, dann das Raster bauen.", "Ein Raster pro Format. Rand und Spaltenabstand aus dem Spacing-System, die Spalte ergibt sich." %}

{% statement "Verweise", "Dahinter: [Ausrichtung und Raster](../prinzip-ausrichtung-und-raster/). Daneben: [Spacing-System](../methode-spacing-system/) und [Lesetext](../prinzip-lesetext/). Weiter: [Weißraum](../prinzip-weissraum/) und [Proportion](../prinzip-proportion/)." %}
''')

p = f'{NEW}/{D}/index.md'; s = open(p).read()
a = s.index('inhalt:'); b = s.index('status:')
s = s[:a] + 'inhalt:\n  - "Ergebnis zuerst: vorher, nachher"\n  - "Sechs Schritte zum Raster"\n  - "Satzspiegel"\n  - "Spaltenbreite berechnen"\n  - "Layout Guide in Figma"\n  - "Mini-Übung"\n' + s[b:]
open(p, 'w').write(s)
done(D, 'Ein Raster wird aus dem Inhalt abgeleitet: Format, Rand, Inhalt messen, Spalten und Spaltenabstand, Grundlinie, Module', 'Gestaltungsraster, Satzspiegel, Steg, Grundlinienraster, Layout Guide, Spaltenbreite')
print('fertig', D)
