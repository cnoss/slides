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

# Geräte-Reihe: übliche Ausrichtung schwarz, gedrehte grau
GERAETE = [('desk', 1440, 900, False), ('tab-h', 834, 1194, False), ('tab-q', 1194, 834, True), ('ph-h', 390, 844, False), ('ph-q', 844, 390, True)]
def geraete():
    sk = 0.165; gap = 20; base = 345
    breite = sum(w * sk for _, w, h, q in GERAETE) + gap * (len(GERAETE) - 1)
    x = (900 - breite) / 2
    pos = []
    for gid, w, h, quer in GERAETE:
        W_, H_ = w * sk, h * sk
        pos.append((gid, x, base - H_, W_, H_, quer)); x += W_ + gap
    def umriss(gid, x, y, w, h, quer):
        farbe = '#888888' if quer else '#231f20'
        return f'<rect data-id="{gid}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" fill="#ffffff" stroke="{farbe}" stroke-width="3" />\n'
    def inhalt(gid, x, y, w, h, quer):
        # Kopfzeile, dann Karten in so vielen Spalten, wie die Breite hergibt
        spalten = {'desk': 3, 'tab-h': 2, 'tab-q': 3, 'ph-h': 1, 'ph-q': 2}[gid]
        p = max(w * 0.07, 5); g = max(w * 0.04, 3)
        o = f'<rect data-id="{gid}-kopf" x="{x + p:.1f}" y="{y + p:.1f}" width="{w - 2 * p:.1f}" height="{max(h * 0.06, 4):.1f}" fill="#888888" />\n'
        top = y + p + max(h * 0.06, 4) + g
        kw = (w - 2 * p - g * (spalten - 1)) / spalten
        kh = min(kw * 0.9, (y + h - p - top))
        reihen = max(1, int((y + h - p - top + g) // (kh + g)))
        n = 0
        for r in range(reihen):
            for c_ in range(spalten):
                if n >= 6: break
                kx = x + p + c_ * (kw + g); ky = top + r * (kh + g)
                o += f'<rect data-id="{gid}-k{n}" x="{kx:.1f}" y="{ky:.1f}" width="{kw:.1f}" height="{kh:.1f}" fill="#e4e4e4" />\n'
                o += f'<rect data-id="{gid}-b{n}" x="{kx:.1f}" y="{ky:.1f}" width="{kw:.1f}" height="{kh * 0.55:.1f}" fill="#c4c4c4" />\n'
                n += 1
        return o
    leer = ''.join(umriss(*q) for q in pos)
    voll = ''.join(umriss(*q) + inhalt(*q) for q in pos)
    f1 = "{% frame '{\"stage\":\"#ffffff\", \"w\":900, \"h\":500, \"bu\":\"Ein Inhalt, viele Formate: Desktop, Tablet und Smartphone, die übliche Ausrichtung schwarz, die gedrehte grau\"}' %}\n" + leer + "{% endframe %}"
    f2 = "{% frame '{\"stage\":\"#ffffff\", \"w\":900, \"h\":500, \"bu\":\"Das Layout passt sich an: Die Reihenfolge bleibt, die Zahl der Spalten ändert sich\"}' %}\n" + voll + "{% endframe %}"
    return f1 + '\n' + f2

W(D, '020-was-ist-ein-layout.md', '''
---
title: "Was ist ein Layout?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Die Definition, die wir heute brauchen: Ein Layout ordnet Text, Bild und Fläche auf einem Format. Es entscheidet, was zuerst gelesen wird, was zusammengehört und was zurücktritt.

  Das Wort kommt aus dem Englischen: to lay out, auslegen, ausbreiten. In Druckereien und Agenturen hieß so der Entwurf, auf dem die Teile einer Seite ausgelegt wurden, bevor sie gesetzt wurden.

  Für jedes Layout stellen sich dieselben Fragen. Im bisherigen Foliensatz standen sie als fünf W-Fragen: Was (Inhalt), Warum (Ziel), Für wen (Zielgruppe), Wo (Medium) und Wie (stilistische Festlegungen). Die ersten vier kommen vor dem Wie. Ausführlich in der Methode Layoutanalyse.

  Danach die Geräte-Reihe: Desktop, Tablet und Smartphone im richtigen Seitenverhältnis, die übliche Ausrichtung mit schwarzer Kontur, die gedrehte mit grauer. Beim Weiterschalten füllen sich die Umrisse mit demselben Inhalt: drei Spalten auf dem Desktop, zwei auf dem Tablet hoch, eine auf dem Smartphone hoch. Frage: Wer entscheidet, was auf dem Smartphone quer passiert? Antwort: das Layout, also Sie.

  Zum Schluss das Foto von Brad Frost, das er in seinen Vorträgen zu Responsive Design und Atomic Design immer wieder zeigt: Geräte aus seinem eigenen Bestand, 2012. Seitdem ist die Vielfalt nur größer geworden: Uhren, faltbare Smartphones, Autos, Fernseher. Foto: Brad Frost, »Devices«, Flickr, CC BY 2.0, https://www.flickr.com/photos/brad_frost/7387824246

  Die Abgrenzung: Raster, Wireframe, Layout und Screendesign werden oft durcheinander verwendet. Das Raster ist das Gerüst, der Wireframe das Layout ohne Oberfläche, das Screendesign kommt mit Oberfläche, Zuständen und Interaktion dazu. Auf dem Screen ist ein Layout außerdem nie ein einzelnes Bild, sondern ein System aus Regeln für viele Formate (siehe Inhalt bestimmt Form).

  **Hintergrund**

  Der Begriff Makrotypografie meint dasselbe aus Sicht der Typografie: die Anordnung von Text und Bild auf der Seite, im Unterschied zur Mikrotypografie, die sich um Buchstaben, Wörter und Zeilen kümmert. Zum Weiterlesen: Lupton, Thinking with Type (Grid).
---

{% interlude "Was ist ein Layout?", "Und warum reicht es nicht, alles irgendwie unterzubringen?" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Layout</h1>
    <p><em>von englisch »to lay out«: auslegen, ausbreiten</em></p>
    <p>Die Anordnung aller Elemente auf einem Format, also Text, Bild, Fläche und Bedienelemente, nach einer erkennbaren Ordnung.</p>
    {% fragment '<p class="list"><strong>Reihenfolge:</strong> Was wird zuerst gelesen, was danach?</p>' %}
    {% fragment '<p class="list"><strong>Zusammenhang:</strong> Was gehört zusammen, was ist getrennt?</p>' %}
    {% fragment '<p class="list"><strong>Gewicht:</strong> Was ist wichtig, was tritt zurück?</p>' %}
    {% fragment '<p class="list"><strong>Raum:</strong> Was bleibt frei?</p>' %}
  </div>
</section>

{% statement "Ein Layout ordnet Text, Bild und Fläche auf einem Format.", "Es entscheidet, was zuerst gelesen wird, was zusammengehört und was zurücktritt." %}

<section class="simple" data-transition="fade">
<div>

# Nicht dasselbe

| Begriff | Was es ist |
|---|---|
| **Raster** | das unsichtbare Gerüst unter dem Layout |
| **Wireframe** | das Layout ohne Oberfläche: Struktur, Gewicht, Reihenfolge |
| **Layout** | die Anordnung der Elemente auf dem Format |
| **Screendesign** | Layout plus Oberfläche, Zustände und Interaktion |

</div>
</section>

{% statement "Auf dem Screen ist ein Layout kein Bild, sondern ein System.", "Dieselben Inhalte müssen auf vielen Formaten funktionieren. Das Layout legt fest, was sich anpasst und was bleibt." %}

''' + geraete() + '''

{% screenshot "./images/geraete-brad-frost.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"So sah das schon 2012 aus: Ein Layout muss auf all dem funktionieren<br><small>Foto: Brad Frost, »Devices«, 2012, Flickr, CC BY 2.0</small>"}' %}
''')

W(D, '025-beispiele.md', '''
---
title: "Layouts im Alltag"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Echte Layouts (ca. 5 Minuten).** Bei jedem Beispiel dieselben zwei Fragen an den Raum: Was lesen Sie zuerst? Welche Ordnung erkennen Sie? Die Bildunterschrift nennt danach das Muster. Die Namen sind keine Norm, sie helfen nur, über Layouts zu sprechen.

  **Apple, iPhone:** eine Bühne pro Produkt. Viel Weißraum, ein Bild, ein Titel, zwei Links. Die Navigationsleiste mit den Modellen darüber ist eine Reihe gleichartiger Elemente, Ähnlichkeit und Ausrichtung tragen sie.

  **tagesschau.de:** ein Aufmacher, dann ein Raster aus kleineren Meldungen. Größe ordnet die Nachrichten nach Wichtigkeit, klassisch wie in der Zeitung.

  **tagesschau.de mobil:** derselbe Inhalt in einer Spalte. Die Reihenfolge bleibt, die Anordnung ändert sich. Genau das meint »Layout als System«.

  **Wikipedia:** drei Spalten mit klaren Rollen. Links Inhaltsverzeichnis, in der Mitte der Lesetext, rechts Einstellungen. Der Lesetext hat die breiteste Spalte, weil er die Hauptsache ist. Nebenbei passt der Artikel: Er erklärt den Begriff Layout.

  **IKEA, Produkte:** ein Kachelraster. Alle Kategorien sind gleich wichtig, also gleich groß, mit Bild oben und Liste darunter. Ordnung durch Wiederholung.

  **Stripe:** geteiltes Layout. Große Aussage links, Bildfläche rechts, darunter eine Reihe mit Kundenlogos als Beleg. Typisch für Startseiten, die etwas verkaufen.

  Alle Screenshots von 2026.
---

{% interlude "Layouts im Alltag", "Was lesen Sie zuerst? Welche Ordnung erkennen Sie?" %}

{% screenshot "./images/layout-apple.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Eine Bühne pro Produkt, viel Weißraum<br><small>apple.com, Screenshot 2026</small>"}' %}
{% screenshot "./images/layout-tagesschau.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Ein Aufmacher, darunter ein Raster aus kleineren Meldungen<br><small>tagesschau.de, Screenshot 2026</small>"}' %}
{% screenshot "./images/layout-tagesschau-mobil.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Derselbe Inhalt in einer Spalte: Die Reihenfolge bleibt, die Anordnung ändert sich<br><small>tagesschau.de, Smartphone, Screenshot 2026</small>"}' %}
{% screenshot "./images/layout-wikipedia.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Drei Spalten mit klaren Rollen, der Lesetext bekommt die breiteste<br><small>de.wikipedia.org, Artikel »Layout«, Screenshot 2026</small>"}' %}
{% screenshot "./images/layout-ikea.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Ein Kachelraster: Gleich wichtig heißt gleich groß<br><small>ikea.com, Screenshot 2026</small>"}' %}
{% screenshot "./images/layout-stripe.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Geteilt: große Aussage links, Bildfläche rechts, darunter die Belege<br><small>stripe.com, Screenshot 2026</small>"}' %}

{% question "Welches Muster hat Ihre meistgenutzte App?", "Bühne, Aufmacher mit Raster, Spalten, Kacheln oder geteilt?" %}
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
begriffe: ["Layout", "Leserichtung", "Makrotypografie", "Raster", "Wireframe", "Layoutmuster"]
herkunft: "U: layout/010"
inhalt:
  - "Schätzfrage: dieselben Teile, drei Anordnungen"
  - "Was ist ein Layout? Definition und Abgrenzung"
  - "Layouts im Alltag: sechs Beispiele, Layoutmuster"
  - "Was Sie schon haben"
  - "Lernziele des Tages"
status: ok
---
''')
print('fertig', D)
