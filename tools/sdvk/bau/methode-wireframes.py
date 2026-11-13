# Bauskript methode-wireframes. Aufruf: python3 tools/sdvk/bau/methode-wireframes.py
import glob, random, os
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'methode-wireframes'
os.makedirs(f'{NEW}/{D}', exist_ok=True)
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Wireframes und Fidelity', 'Methode // Konstruieren')

K = '#231f20'; HL = '#888888'; G2 = '#d9d9d9'; FL = '#e4e4e4'; BI = '#c4c4c4'; TX = '#aaaaaa'; L = '#9313ce'
FONT = 'font-family="Helvetica Neue, Arial, sans-serif"'

# ---------------------------------------------------------------- Beispiel-Screen: Produktseite, 900 x 500
# Alle Stufen nutzen dieselben Positionen und data-ids, damit Auto-Animate die Verfeinerung zeigt.
POS = {
    'nav':   (0, 0, 900, 50),
    'logo':  (40, 18, 90, 14),
    'bc':    (40, 70, 180, 8),
    'bild':  (40, 96, 400, 264),
    'th0':   (40, 374, 88, 52), 'th1': (144, 374, 88, 52), 'th2': (248, 374, 88, 52), 'th3': (352, 374, 88, 52),
    'h1':    (480, 100, 300, 22), 'h2': (480, 130, 200, 22),
    'preis': (480, 196, 120, 26),
    'menge': (480, 300, 80, 44),
    'btn':   (576, 300, 284, 44),
    't0':    (480, 368, 380, 9), 't1': (480, 388, 380, 9), 't2': (480, 408, 260, 9),
}
NAVX = [560, 630, 700, 770]
STERNE = [486, 506, 526, 546, 566]
FARBEN = [494, 534, 574, 614]

def rect(did, f, rx=0, extra=''):
    x, y, w, h = POS[did]
    return f'<rect data-id="{did}" x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}" rx="{rx}"{extra} />\n'

def grau():
    """Grayscale-Wireframe nach dem Vokabular aus dem Rückgrat."""
    o = rect('nav', '#f2f2f2') + rect('logo', HL)
    o += ''.join(f'<rect data-id="n{i}" x="{x}" y="22" width="50" height="8" fill="{TX}" />\n' for i, x in enumerate(NAVX))
    o += f'<circle data-id="cart" cx="860" cy="26" r="11" fill="{HL}" />\n'
    o += rect('bc', TX) + rect('bild', BI) + ''.join(rect(f'th{i}', G2) for i in range(4))
    o += rect('h1', HL) + rect('h2', HL)
    o += ''.join(f'<circle data-id="s{i}" cx="{x}" cy="168" r="6" fill="{TX}" />\n' for i, x in enumerate(STERNE))
    o += rect('preis', K)
    o += ''.join(f'<circle data-id="f{i}" cx="{x}" cy="262" r="14" fill="{G2}" />\n' for i, x in enumerate(FARBEN))
    o += rect('menge', '#ffffff', 0, f' stroke="{HL}" stroke-width="2"') + rect('btn', K, 22)
    o += ''.join(rect(f't{i}', G2) for i in range(3))
    return o

random.seed(7)
def jitter(x, y, w, h, did, fill='none'):
    """Handgezeichnetes Rechteck: leicht schiefe Kanten, runde Enden."""
    j = lambda: random.uniform(-3, 3)
    pts = [(x + j(), y + j()), (x + w + j(), y + j()), (x + w + j(), y + h + j()), (x + j(), y + h + j())]
    d = 'M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts) + ' Z'
    return f'<path data-id="{did}" d="{d}" fill="{fill}" stroke="{K}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" />\n'

def welle(x, y, w, did):
    """Textzeile in der Skizze: Wellenlinie."""
    d = f'M{x},{y}' + ''.join(f' q6,{-4 if i % 2 else 4} 12,0' for i in range(int(w // 12)))
    return f'<path data-id="{did}" d="{d}" fill="none" stroke="{HL}" stroke-width="2.5" stroke-linecap="round" />\n'

def skizze():
    o = jitter(*POS['nav'][:2], 900, 50, 'nav') if False else ''
    x, y, w, h = POS['bild']
    o += jitter(x, y, w, h, 'bild')
    o += f'<path data-id="kreuz" d="M{x+8},{y+8} L{x+w-8},{y+h-8} M{x+w-8},{y+8} L{x+8},{y+h-8}" stroke="{TX}" stroke-width="2.5" stroke-linecap="round" />\n'
    o += ''.join(jitter(*POS[f'th{i}'], f'th{i}') for i in range(4))
    o += welle(40, 26, 90, 'logo') + welle(480, 112, 300, 'h1') + welle(480, 142, 200, 'h2')
    o += jitter(*POS['preis'], 'preis')
    o += jitter(*POS['btn'], 'btn')
    o += ''.join(welle(480, 372 + i * 20, 380 if i < 2 else 260, f't{i}') for i in range(3))
    return o

def txt(did, x, y, s, size, fill=K, weight=400):
    return f'<text data-id="{did}" x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{weight}" fill="{fill}">{s}</text>\n'

def midfi(farbe=False):
    """Echte Texte und Schrift. Mid-Fi bleibt grau, Hi-Fi bekommt Farbe und Bild."""
    akz = L if farbe else K
    o = rect('nav', '#ffffff' if farbe else '#f2f2f2')
    if farbe:
        o += f'<line data-id="navlinie" x1="0" y1="50" x2="900" y2="50" stroke="{FL}" stroke-width="2" />\n'
    o += txt('logo', 40, 32, 'Hocker &amp; Co.', 17, K, 700)
    o += ''.join(txt(f'n{i}', x, 31, n, 13, '#555555') for i, (x, n) in enumerate(zip(NAVX, ['Stühle', 'Tische', 'Lampen', 'Sale'])))
    o += f'<circle data-id="cart" cx="860" cy="26" r="11" fill="{akz if farbe else HL}" />\n'
    o += txt('bc', 40, 79, 'Möbel / Hocker / Kiel', 11, '#6a6a6a')
    if farbe:
        x, y, w, h = POS['bild']
        o += rect('bild', '#f3eaf8')
        # Hocker als flache Illustration
        o += (f'<g data-id="hocker"><rect x="{x+130}" y="{y+70}" width="140" height="22" rx="6" fill="#c8a27a" />'
              f'<line x1="{x+150}" y1="{y+92}" x2="{x+135}" y2="{y+210}" stroke="#8a6440" stroke-width="10" stroke-linecap="round" />'
              f'<line x1="{x+250}" y1="{y+92}" x2="{x+265}" y2="{y+210}" stroke="#8a6440" stroke-width="10" stroke-linecap="round" />'
              f'<line x1="{x+200}" y1="{y+92}" x2="{x+200}" y2="{y+214}" stroke="#8a6440" stroke-width="10" stroke-linecap="round" />'
              f'<line x1="{x+142}" y1="{y+160}" x2="{x+258}" y2="{y+160}" stroke="#8a6440" stroke-width="6" stroke-linecap="round" /></g>\n')
        o += ''.join(rect(f'th{i}', '#f3eaf8' if i else '#e4cff0') for i in range(4))
    else:
        o += rect('bild', BI) + ''.join(rect(f'th{i}', G2) for i in range(4))
    o += txt('h1', 480, 118, 'Hocker Kiel', 24, K, 700) + txt('h2', 480, 146, 'Eiche geölt, Sitzhöhe 46 cm', 16, '#555555')
    o += ''.join(f'<circle data-id="s{i}" cx="{x}" cy="168" r="6" fill="{(akz if farbe else HL) if i < 4 else G2}" />\n' for i, x in enumerate(STERNE))
    o += txt('preis', 480, 220, '249,00 €', 26, K, 700)
    swatch = ['#c8a27a', '#231f20', '#ffffff', '#8a8a8a'] if farbe else [BI, HL, '#f2f2f2', TX]
    o += ''.join(f'<circle data-id="f{i}" cx="{x}" cy="262" r="14" fill="{c}" stroke="{akz if i == 0 else G2}" stroke-width="{3 if i == 0 else 2}" />\n' for i, (x, c) in enumerate(zip(FARBEN, swatch)))
    o += rect('menge', '#ffffff', 0, f' stroke="{HL}" stroke-width="2"') + txt('mz', 512, 328, '1', 16, K)
    o += rect('btn', akz, 22) + txt('btnt', 652, 328, 'In den Warenkorb', 16, '#ffffff', 600)
    for i, s in enumerate(['Massivholz aus Europa, von Hand geölt.', 'Stapelbar, belastbar bis 120 kg.', 'Lieferung in 3 bis 5 Werktagen.']):
        o += txt(f't{i}', 480, 377 + i * 20, s, 13, '#555555')
    return o

def fq(bu, svg, animate=True):
    a = '' if animate else '"animate":false,'
    return "{% frame '{" + a + "\"w\":900, \"h\":500, \"bu\":\"" + bu + "\"}' %}\n" + svg + "{% endframe %}"

def mark(svg):
    """Lila Rahmen um die verräterischen Elemente: Bild, Preis, Button."""
    o = ''
    for did, k in (('bild', 'm1'), ('preis', 'm2'), ('btn', 'm3')):
        x, y, w, h = POS[did]
        o += f'<rect data-id="{k}" x="{x-8}" y="{y-8}" width="{w+16}" height="{h+16}" rx="10" fill="none" stroke="{L}" stroke-width="4" />\n'
    return svg + o

# ---------------------------------------------------------------- Rätsel
W(D, '010-raetsel.md', '''
---
title: "Was für eine Seite ist das?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Rätsel (ca. 1 Minute):** Ein Screen ganz ohne Text, ohne Bild, ohne Farbe. Frage: Was für eine Seite ist das? Fast alle erkennen sofort eine Produktseite in einem Onlineshop. Nachfragen: Woran? Erwartbare Antworten: großes Bild links mit kleinen Vorschaubildern darunter, eine dicke dunkle Zahl (der Preis), runde Auswahlfelder (Farben oder Varianten), ein breiter Button neben einem kleinen Feld (Menge und »In den Warenkorb«).

  Die Pointe: Die Struktur allein verrät schon die Seite und ihre Rangfolge. Genau das ist ein Wireframe. Und genau deshalb lohnt es sich, über die Struktur zu entscheiden, bevor Farbe, Bilder und Schrift dazukommen.
---

{% interlude "Was für eine Seite ist das?", "Ohne Text, ohne Bild, ohne Farbe" %}

''' + fq('Was für eine Seite ist das? Und woran erkennen Sie es?', grau()) + '''
''' + fq('Großes Bild, eine dicke Zahl, ein breiter Button: ein Produkt im Shop', mark(grau())) + '''

{% statement "Die Struktur verrät die Seite.", "Noch bevor ein Wort dasteht, wissen Sie, was das ist und was am wichtigsten ist." %}
''')

# ---------------------------------------------------------------- Was ist ein Wireframe
W(D, '020-wireframe.md', '''
---
title: "Was ist ein Wireframe?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Ein Wireframe ist der Bauplan eines Screens: Struktur ohne Oberfläche. Er beantwortet zwei Fragen: Was steht wo? Und was ist wie wichtig? Texte sind graue Balken, Bilder graue Flächen, der wichtigste Button ist dunkel.

  **Warum grau?** Farbe, Bilder und Schrift sind stark. Sie ziehen die Aufmerksamkeit auf sich, beim Gestalten genauso wie im Gespräch. Wer ein buntes Layout zeigt, bekommt Feedback zur Farbe, nicht zur Anordnung. In Grau bleibt nur, worum es gerade geht: Anordnung, Gruppen, Hierarchie. Und die Diskussion über Geschmack fällt weg.

  Ein Nebeneffekt: Grau ist schnell. Ein Wireframe ist in Minuten verändert. Darum ist die Stufe ideal zum Variieren.

  Begriffe: Wireframe, Fidelity, Skizze, Mid-Fi, Hi-Fi.
---

{% interlude "Struktur ohne Oberfläche", "Was steht wo, und was ist wie wichtig?" %}

{% statement "Ein Wireframe ist der Bauplan eines Screens.", "Text als Balken, Bild als Fläche, der wichtigste Button dunkel. Mehr braucht es nicht, um über Anordnung und Hierarchie zu entscheiden." %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Warum grau?</h1>
    {% fragment '<p class="list">Farbe und Bild ziehen den Blick auf sich. In Grau bleibt die Anordnung sichtbar.</p>' %}
    {% fragment '<p class="list">Feedback gilt der Struktur, nicht dem Geschmack.</p>' %}
    {% fragment '<p class="list">Grau ist schnell: ideal, um viele Varianten zu bauen.</p>' %}
  </div>
</section>
''')

# ---------------------------------------------------------------- Fidelity-Leiter
W(D, '030-fidelity.md', '''
---
title: "Vier Stufen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Derselbe Screen in vier Stufen. Fidelity heißt Wiedergabetreue: wie nah ein Entwurf am fertigen Produkt ist.

  **Skizze:** von Hand auf Punktpapier, schnell, aber präzise. Ein Kreuz steht für ein Bild, Linien für Text, ein dicker Strich für eine Zwischenüberschrift. Frage: Was gehört auf die Seite, und wie verteilt es sich grob? Die Skizze zeigt zwei andere Seiten als die folgenden Stufen, sie steht für die Art zu zeichnen.

  **Grayscale-Wireframe:** dasselbe auf dem Raster, mit echten Proportionen und Abständen. Frage: Was steht wo, was ist wie wichtig?

  **Mid-Fi:** echte Texte und Schrift, aber noch grau. Frage: Passt das Layout zu den echten Inhalten? Ein langer Produktname, ein Preis mit Cent, drei Zeilen Beschreibung.

  **Hi-Fi:** Farbe, Bild, Akzent. Frage: Wie wirkt es? Ist es fertig für einen Test oder für die Umsetzung?

  Die Positionen bleiben von Stufe zu Stufe gleich. Was sich ändert, ist die Detailtiefe. Die Texte in der Grafik sind hier eine bewusste Ausnahme, sie sind der Inhalt der Mid-Fi-Stufe.

  **Hintergrund**

  Die Unterscheidung von Low und High Fidelity stammt aus der Literatur zum Prototyping der 1990er-Jahre (Rudd, Stern & Isensee, »Low vs. high-fidelity prototyping debate«, 1996, aus dem Gedächtnis, bitte prüfen). Bill Buxton unterscheidet in »Sketching User Experiences« (2007) Skizze und Prototyp: Eine Skizze ist billig, schnell und wegwerfbar und dient dazu, Ideen zu finden. Ein Prototyp dient dazu, eine Idee zu prüfen. Je grober, desto offener die Diskussion.
---

{% interlude "Vier Stufen", "Von der Skizze zum fertigen Entwurf" %}

{% screenshot "./images/wireframe-skizzen.webp", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"1. Skizze: Was gehört auf die Seite? Von Hand, schnell, aber präzise"}' %}
''' + fq('2. Grayscale-Wireframe: Was steht wo, was ist wie wichtig?', grau()) + '''
''' + fq('3. Mid-Fi: Passt es zu den echten Inhalten?', midfi()) + '''
''' + fq('4. Hi-Fi: Wie wirkt es?', midfi(True)) + '''
''')

# ---------------------------------------------------------------- Haltung
W(D, '040-so-grob-wie-moeglich.md', '''
---
title: "So grob wie möglich"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Haltung dahinter: Die Detailtiefe folgt der Frage, die ein Entwurf beantworten soll. Wer noch nicht weiß, ob das Bild links oder oben stehen soll, braucht keine Schrift und keine Farbe. Und wer erst in Hi-Fi merkt, dass die Anordnung nicht trägt, hat Stunden verloren.

  Die Zeiten sind Richtwerte pro Variante. Sie zeigen, warum man auf den frühen Stufen viele Varianten baut und auf den späten wenige.
---

{% interlude "So grob wie möglich, so fein wie nötig.", "Die Detailtiefe folgt der Frage" %}

<section class="simple" data-transition="fade">
<div>

# Welche Stufe beantwortet was?

| Stufe | beantwortet die Frage | Zeit pro Variante |
|---|---|---|
| **Skizze** | Was gehört auf die Seite, und wie verteilt es sich grob? | 1 bis 3 Minuten |
| **Grayscale-Wireframe** | Was steht wo, was ist wie wichtig? | 10 bis 20 Minuten |
| **Mid-Fi** | Passt es zu den echten Inhalten und zur Schrift? | 30 bis 60 Minuten |
| **Hi-Fi** | Wie wirkt es, ist es fertig für Test oder Umsetzung? | Stunden |

</div>
</section>
''')

# ---------------------------------------------------------------- Fehler und Einsatz
# ---------------------------------------------------------------- Nur zeigen, worüber Sie sprechen wollen
def nur_titel():
    """Wireframe, in dem nur der Produktname echt ist."""
    o = grau()
    o = o.replace(rect('h1', HL), txt('h1', 480, 118, 'Hocker Kiel', 24, K, 700))
    o = o.replace(rect('h2', HL), txt('h2', 480, 146, 'Eiche geölt, Sitzhöhe 46 cm', 16, '#555555'))
    return o

W(D, '045-nur-was-zur-sprache-kommt.md', """
---
title: "Nur zeigen, worüber Sie sprechen wollen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Die Unterzeile ist Watzlawicks erstes Axiom (siehe Prinzip Kommunikation): Auch was nur als Platzhalter gedacht war, sendet eine Botschaft.

  Die wichtigste Regel für jeden Prototyp, egal auf welcher Stufe: Alles, was im Entwurf zu sehen ist, wird auch besprochen. Wer ein Foto zeigt, bekommt Feedback zum Foto. Wer einen Werbetext zeigt, diskutiert den Werbetext. Wer Farbe zeigt, redet über Farbe.

  Daraus folgt: In einen Prototyp gehört nur, worüber Sie gerade sprechen wollen. Alles andere bleibt Platzhalter. Wollen Sie nicht über den Bildinhalt sprechen, zeigen Sie kein Bild, sondern eine graue Fläche. Wollen Sie nicht über den Wortlaut sprechen, zeigen Sie Balken. Wollen Sie nicht über Farbe sprechen, bleibt alles grau.

  Das gilt auch umgekehrt: Wollen Sie wissen, ob der lange Produktname in die Zeile passt, dann gehört genau dieser eine Text echt hinein, der Rest bleibt grau. Die Fidelity muss nicht überall gleich sein.

  Der Fehler passiert oft: Ein Wireframe mit einem schönen Stockfoto, und die ganze Runde redet über das Foto statt über die Anordnung.

  Vorführung: erst der Hi-Fi-Screen mit der Frage »Worüber würden Sie hier sprechen?« (Antworten: Hocker, Holz, Lila, Preis). Dann derselbe Screen als Wireframe: Jetzt bleibt nur die Anordnung. Zum Schluss der Wireframe, in dem nur der Produktname echt ist.
---

{% interlude "Nur zeigen, worüber Sie sprechen wollen.", "Man kann nicht nicht kommunizieren." %}

""" + fq('Worüber würden Sie hier sprechen?', midfi(True)) + """
""" + fq('Als Wireframe: Jetzt bleibt nur die Anordnung', grau()) + """
""" + fq('Nur der Produktname ist echt: Jetzt geht es um genau diesen Text', nur_titel()) + """

<section class="simple" data-transition="fade">
  <div>
    <h1>Was nicht besprochen werden soll, bleibt Platzhalter</h1>
    {% fragment '<p class="list"><strong>Bild:</strong> Kein Gespräch über den Bildinhalt? Dann eine graue Fläche statt eines Fotos.</p>' %}
    {% fragment '<p class="list"><strong>Text:</strong> Kein Gespräch über den Wortlaut? Dann Balken statt Text.</p>' %}
    {% fragment '<p class="list"><strong>Farbe:</strong> Kein Gespräch über Farbe? Dann bleibt alles grau.</p>' %}
    {% fragment '<p class="list"><strong>Umgekehrt:</strong> Was Sie besprechen wollen, zeigen Sie echt. Auch wenn der Rest grau bleibt.</p>' %}
  </div>
</section>
""")

W(D, '050-fehler.md', '''
---
title: "Typische Fehler"
layout: presentation.11ty.js
slideClasses: simple
status: ok
speaker: |
  Der häufigste Fehler: zu früh zu fein. Wer gleich in Farbe und mit Schatten anfängt, verliebt sich in die erste Lösung und baut keine Alternativen mehr.

  Der zweite: Lorem ipsum bis zum Schluss. Dann zeigt sich erst in der Umsetzung, dass der echte Produktname zweizeilig ist (siehe Inhalt bestimmt Form).

  Der dritte: Graustufen als Gestaltung missverstehen. Das Grau im Wireframe ist ein Platzhalter, keine Entscheidung für eine graue Seite.
---

{% fragment '<p class="list">Zu früh zu fein: Farbe und Schatten, bevor die Anordnung steht</p>' %}
{% fragment '<p class="list">Schon im Wireframe Farbe: Dann geht es im Feedback nur noch um die Farbe</p>' %}
{% fragment '<p class="list">Dinge zeigen, über die man nicht sprechen will: Stockfotos, Werbetexte, Logos</p>' %}
{% fragment '<p class="list">Lorem ipsum bis zum Schluss: Die echten Inhalte passen dann nicht hinein</p>' %}
{% fragment '<p class="list">Graustufen als Gestaltung missverstehen: Das Grau ist ein Platzhalter</p>' %}
{% fragment '<p class="list">Nur eine Variante pro Stufe: Gerade die groben Stufen sind zum Variieren da</p>' %}
''')

W(D, '060-einsatz.md', '''
---
title: "Einsatz"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Wireframes sind eine Können-Methode. Sie kommen im Layout-Workshop, im Projekt und vor jeder Abstimmung mit anderen zum Einsatz: mit Auftraggebenden, im Team, mit der Entwicklung. In Figma entstehen sie mit Rechtecken, Auto Layout und einem Raster. Viele Teams nutzen dafür eigene Wireframe-Komponenten.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wo Sie Wireframes brauchen</h1>
    {% fragment '<p class="list">Beim Variieren: viele Anordnungen in kurzer Zeit</p>' %}
    {% fragment '<p class="list">In der Abstimmung: Struktur besprechen, bevor über Farbe gestritten wird</p>' %}
    {% fragment '<p class="list">Im Projekt: als Bauplan für die Entwicklung</p>' %}
  </div>
</section>

{% statement "Verweise", "Davor: [Alternativen](../haltung-alternativen/). Damit: [Gestaltungsraster](../methode-gestaltungsraster/), [Spacing-System](../methode-spacing-system/) und [Variieren entlang einer Achse](../methode-variieren-achse/). Danach: [Inhalt bestimmt Form](../prinzip-inhalt-bestimmt-form/)." %}
''')

open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Wireframes und Fidelity"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Methode"
gruppe: "Konstruieren"
tiefe: "können"
einsatz: "Zum Variieren und Abstimmen, bevor Farbe, Bild und Schrift dazukommen"
kurzsatz: "Ein Wireframe zeigt, was wo steht und wie wichtig es ist. So grob wie möglich, so fein wie nötig"
begriffe: ["Wireframe", "Fidelity", "Skizze", "Mid-Fi", "Hi-Fi"]
herkunft: "N"
inhalt:
  - "Rätsel: Was für eine Seite ist das?"
  - "Struktur ohne Oberfläche, warum grau"
  - "Vier Stufen: Skizze, Grayscale-Wireframe, Mid-Fi, Hi-Fi"
  - "So grob wie möglich, so fein wie nötig"
  - "Typische Fehler, Einsatz"
status: ok
---
''')
print('fertig', D)
