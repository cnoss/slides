# Bauskript methode-variieren-achse. Aufruf: python3 tools/sdvk/bau/methode-variieren-achse.py
import glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'methode-variieren-achse'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Variieren entlang einer Achse', 'Methode // Variieren')

K = '#231f20'; G1 = '#888888'; G2 = '#d9d9d9'; HG = '#e4e4e4'; BI = '#c4c4c4'; TX = '#aaaaaa'; L = '#9313ce'

# ---------------------------------------------------------------- Card als Wireframe
def card(p, x, y, w=140, h=230, bild=0.34, titel=14, abstand=10, zeilen=(1.0, 0.8), mark=False):
    """Karte: hellgraue Fläche, Bild, Titelbalken, zwei Textzeilen, Link. bild = Anteil der Innenhöhe."""
    i = 10; iw = w - 2 * i
    bh = round((h - 2 * i) * bild)
    o = f'<rect data-id="{p}-k" x="{x}" y="{y}" width="{w}" height="{h}" fill="{HG}" />'
    yy = y + i
    if bh > 0:
        o += f'<rect data-id="{p}-b" x="{x+i}" y="{yy}" width="{iw}" height="{bh}" fill="{BI}" />'
        yy += bh + abstand
    else:
        o += f'<rect data-id="{p}-b" x="{x+i}" y="{yy}" width="{iw}" height="0" fill="{BI}" />'
    o += f'<rect data-id="{p}-t" x="{x+i}" y="{yy}" width="{round(iw*0.85)}" height="{titel}" fill="{G1}" />'
    yy += titel + abstand
    for n, z in enumerate(zeilen):
        o += f'<rect data-id="{p}-z{n}" x="{x+i}" y="{yy}" width="{round(iw*z)}" height="6" fill="{TX}" />'
        yy += 13
    o += f'<rect data-id="{p}-l" x="{x+i}" y="{yy+6}" width="40" height="10" rx="5" fill="{K}" />'
    if mark:
        o += f'<line data-id="{p}-m" x1="{x}" y1="{y+h+18}" x2="{x+w}" y2="{y+h+18}" stroke="{L}" stroke-width="6" stroke-linecap="round" />'
    return o + '\n'

def fr(bu, svg, w=900, h=500):
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":" + str(w) + ", \"h\":" + str(h) + ", \"bu\":\"" + bu + "\"}' %}\n" + svg + "{% endframe %}"

XS = [40, 210, 380, 550, 720]
BILD = [0.1, 0.22, 0.34, 0.46, 0.58]  # Stufe 5 passt mit Fundament noch in die Karte
TITEL = [8, 12, 16, 22, 30]
def reihe_bild(mark=None):
    return ''.join(card(f'c{n}', XS[n], 120, bild=BILD[n], mark=(mark == n)) for n in range(5))
def reihe_titel(mark=None):
    return ''.join(card(f'c{n}', XS[n], 120, bild=BILD[2], titel=TITEL[n], mark=(mark == n)) for n in range(5))

W(D, '005-problem.md', kopf('Das Problem', '''
Wer frei drauflos variiert, ändert meist mehrere Dinge auf einmal: Bild größer, Titel fetter, Abstände enger. Die neue Fassung ist anders, aber niemand weiß, woran es liegt, dass sie besser oder schlechter wirkt.

Die Methode macht aus dem Probieren einen Versuch: Eine Variable ändert sich, alles andere bleibt. Dann sieht man, was genau eine Entscheidung bewirkt. Und man kann sie begründen.
''') + '''{% interlude "Welche Card ist besser?", "Sie haben erst eine." %}

{% statement "Eine Variable ändert sich, alles andere bleibt.", "Dann sehen Sie, was genau eine Entscheidung bewirkt. Und Sie können sie begründen." %}
''')

W(D, '010-ergebnis.md', kopf('Ergebnis zuerst', '''
So sieht das Ergebnis aus: eine Reihe, fünf Stufen, eine einzige Variable. Hier die Höhe des Bildes. Titel, Text, Abstände und Link sind in allen fünf Karten gleich.

Frage: Welche Stufe würden Sie nehmen, und warum? Die Antworten unterscheiden sich, und das ist gut. Jetzt lässt sich über einen konkreten Unterschied sprechen statt über »irgendwie besser«.
''', transition='none') + fr('Ergebnis: eine Achse, fünf Stufen. Nur die Bildhöhe ändert sich', reihe_bild()) + '\n')

W(D, '020-aufbau.md', kopf('Schritt für Schritt', '''
Der Aufbau Schritt für Schritt, mit Auto-Animate:

1. Eine Ausgangskarte.
2. Sie wird fünfmal kopiert, alle gleich.
3. Eine Achse: die Bildhöhe in fünf deutlich unterschiedenen Stufen, inklusive der Extreme.
4. Eine Stufe wird gewählt (lila Linie) und eingefroren.
5. Nächste Achse auf Basis der gewählten Stufe: die Größe des Titels.

Wichtig ist Schritt 4: Erst wenn eine Achse entschieden ist, kommt die nächste. Sonst vermischen sich die Variablen wieder.

**Hintergrund**

Martin Lorenz beschreibt in »Flexible Visual Systems« (2016, bitte prüfen) visuelle Systeme über Parameter, die man einzeln verändert. Dieselbe Logik steckt in jedem Experiment: eine unabhängige Variable, alles andere konstant. Und in Figma, in Komponenten mit Varianten und Properties.
''', transition='none') + '''{% interlude "Schritt für Schritt", "Eine Achse nach der anderen" %}

''' + '\n'.join([
  fr('Eine Ausgangskarte', card('c2', 380, 120)),
  fr('Fünfmal kopiert, alle gleich', ''.join(card(f'c{n}', XS[n], 120) for n in range(5))),
  fr('Achse 1: die Bildhöhe in fünf Stufen', reihe_bild()),
  fr('Eine Stufe gewinnt und wird eingefroren', reihe_bild(mark=2)),
  fr('Achse 2: die Titelgröße, auf Basis der gewählten Stufe', reihe_titel()),
]) + '\n')

AXEN = ['Abstände', 'Bildgröße', 'Bildposition', 'Flächen als Regionen', 'Ähnlichkeit', 'Hierarchie', 'Schriftgröße', 'Schriftschnitt', 'Zeilenabstand', 'Satzart', 'Farbe der Fläche', 'Gewicht des Links']
pillen = ''.join(f'<span style="display:inline-block;background:#e4e4e4;padding:1vh 1.6vw;margin:0 1vw 1.6vh 0;font-size:2.6vh;">{a}</span>' for a in AXEN)
W(D, '030-achsen.md', kopf('Welche Achsen?', '''
Die Achsen kennen Sie schon, aus den letzten Wochen: Abstände (Nähe), Ähnlichkeit, Flächen als Regionen (gemeinsame Region), Hierarchie, Schriftgröße, Schriftschnitt, Zeilenabstand, Satzart. Dazu für die Card: Bildgröße und Bildposition.

Jede visuelle Variable ist eine mögliche Achse. Gute Achsen sind die, bei denen Sie unsicher sind. Was schon klar ist, muss man nicht variieren.
''') + '''{% interlude "Welche Achsen gibt es?", "Sie kennen fast alle schon." %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Jede visuelle Variable ist eine Achse</h1>
    <div style="text-align:left;width:100%;">''' + pillen + '''</div>
  </div>
</section>
''')

W(D, '040-schritte.md', kopf('Schritte', '''
**1. Ausgangsvariante festlegen:** eine solide Karte, nicht die perfekte. Sie ist der Nullpunkt.

**2. Eine Achse wählen:** eine Variable, bei der Sie unsicher sind.

**3. Stufen festlegen:** drei bis fünf, deutlich voneinander unterschieden. Die Extreme gehören dazu, oft lernt man an ihnen am meisten.

**4. Nebeneinanderlegen und vergleichen:** in einer Reihe, gleich groß, mit gleichem Inhalt.

**5. Entscheiden und einfrieren:** Die beste Stufe wird die neue Ausgangsvariante. Dann die nächste Achse.
''') + liste('In fünf Schritten', [
  '<strong>1. Ausgangsvariante:</strong> solide, nicht perfekt',
  '<strong>2. Eine Achse:</strong> wo Sie unsicher sind',
  '<strong>3. Stufen:</strong> drei bis fünf, deutlich unterschieden, mit Extremen',
  '<strong>4. Vergleichen:</strong> in einer Reihe, gleicher Inhalt',
  '<strong>5. Einfrieren:</strong> Die beste Stufe ist die neue Ausgangsvariante',
]) + '\n')

W(D, '050-uebung.md', kopf('Mini-Übung', '''
**Mini-Übung (ca. 10 Minuten)**, passt als Einstieg in eine längere Übung mit Varianten.

Eine Card aus der Vorlage der Übung nehmen. Eine Achse wählen, fünf Stufen bauen, nebeneinanderlegen. Dann zu zweit: Welche Stufe gewinnt? Warum? Ein Satz.

Danach kann es weitergehen: Aus mehreren Achsen werden mit dem Morphologischen Kasten viele Varianten.
''') + '''{% interlude "Und jetzt Sie.", "Eine Achse, fünf Stufen, zehn Minuten" %}

''' + liste('Ihre erste Achse', [
  'Nehmen Sie die Card aus der Vorlage.',
  'Wählen Sie eine Achse und bauen Sie fünf Stufen.',
  'Zu zweit: Welche Stufe gewinnt? Warum? Ein Satz.',
]) + '\n')

# ---------------------------------------------------------------- Im Kontext prüfen
TITEL_ZEILEN = [1, 3, 1, 2, 1, 2]
def grid():
    o = ''; cw, ch = 250, 200
    for n in range(6):
        cx = 60 + (n % 3) * 280; cy = 30 + (n // 3) * 230
        o += f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" fill="{HG}" />'
        bild = n != 4
        yy = cy + 10
        if bild:
            o += f'<rect x="{cx+10}" y="{yy}" width="{cw-20}" height="80" fill="{BI}" />'; yy += 90
        for z in range(TITEL_ZEILEN[n]):
            o += f'<rect x="{cx+10}" y="{yy}" width="{cw-20 if z < TITEL_ZEILEN[n]-1 else 120}" height="12" fill="{G1}" />'; yy += 18
        o += f'<rect x="{cx+10}" y="{yy+4}" width="{cw-40}" height="6" fill="{TX}" />'
    return o + '\n'
W(D, '060-kontext.md', kopf('Im Kontext prüfen', '''
Eine einzelne Karte auf weißer Fläche sieht fast immer gut aus. Ob sie trägt, zeigt sich erst im Grid, mit echten Inhalten: lange und kurze Titel, ein fehlendes Bild, sechs Karten nebeneinander. Darum gehört zu jeder Variantenreihe ein Grid mit echten Inhalten.

**Begründet auswählen:**

- **Kriterien vorher festlegen,** aus dem Gestaltungsziel. Etwa: Der Titel muss zuerst gelesen werden. Das Grid soll ruhig wirken, auch wenn Bilder fehlen.
- **Unschärfetest:** Grid unscharf und grau. Ist die Rangfolge noch die gewünschte?
- **Eine Zeile Entscheidungslog:** welche Variante, warum, was verworfen wurde und warum.

Siehe Inhalt bestimmt Form (Stresstest) und Unschärfe- und Graustufentest.
''', transition='none') + '''{% interlude "Allein sieht jede Card gut aus.", "Erst im Kontext zeigt sich, welche trägt." %}

''' + fr('Allein: Die Card wirkt fertig', card('k', 380, 120, w=140, h=230)) + '''
''' + fr('Im Grid mit echten Inhalten: lange Titel, ein Bild fehlt', grid()) + '''

<section class="simple" data-transition="fade">
<div>

# Begründet auswählen

| Schritt | Was Sie tun |
|---|---|
| **Kriterien** | vorher festlegen, aus dem Gestaltungsziel |
| **Unschärfetest** | Grid unscharf und grau: Stimmt die Rangfolge noch? |
| **Entscheidungslog** | eine Zeile: gewählt, weil … verworfen, weil … |

</div>
</section>

{% statement "Eine Zeile Entscheidungslog", "»Gewählt: Bildhöhe Stufe 3, weil der Titel im Grid zuerst gelesen wird. Verworfen: Stufe 5, weil das Bild den Titel verdrängt.«" %}
''')

W(D, '070-fehler.md', kopf('Typische Fehler', '''
Der häufigste Fehler: zwei Variablen auf einmal ändern. Der zweithäufigste: Stufen, die sich kaum unterscheiden. Wer zwischen 16 und 17 Pixeln variiert, sieht keinen Unterschied und lernt nichts (siehe Eindeutigkeit: gleich oder deutlich anders).
''', cls='simple') + '\n'.join("{% fragment '<p class=\"list\">" + p + "</p>' %}" for p in [
  'Zwei Variablen auf einmal ändern: Dann weiß niemand, was gewirkt hat',
  'Zu kleine Unterschiede: 16 gegen 17 Pixel sieht niemand',
  'Die Extreme weglassen: Gerade dort lernt man am meisten',
  'Nur die Einzelkarte bewerten, nie das Grid',
  'Nach Gefühl entscheiden, ohne Kriterien',
]) + '\n')

W(D, '080-einsatz.md', kopf('Einsatz', '''
Variieren entlang einer Achse ist eine Können-Methode. Sie kehrt wieder: in jeder Übung mit Varianten, beim Layout, im Projekt bei jeder Komponente. Haltung dahinter: Entwickeln Sie Alternativen.
''') + liste('Wo die Methode wiederkommt', [
  'In der Übung: Achse für Achse zur Card',
  'Beim Layout: Spaltenzahl, Bildgröße, Abstände',
  'Im Projekt: bei jeder Komponente, bevor sie ins System geht',
]) + '''

{% statement "Verweise", "Dahinter: [Alternativen](../haltung-alternativen/). Weiter: [Morphologischer Kasten](../methode-morphologischer-kasten/), [Inhalt bestimmt Form](../prinzip-inhalt-bestimmt-form/). Prüfen: [Unschärfe- und Graustufentest](../methode-unschaerfetest/), festhalten: [Entscheidungslog](../methode-entscheidungslog/)." %}
''')

done(D, 'Eine Variable ändert sich, alles andere bleibt: in Stufen variieren, im Kontext prüfen, begründet auswählen',
     'Achse, Stufe, Ausgangsvariante, Variable, Entscheidungslog')
index(D, ['Ergebnis zuerst: eine Achse, fünf Stufen', 'Aufbau Schritt für Schritt', 'Achsen', 'Fünf Schritte', 'Mini-Übung', 'Im Kontext prüfen und begründet auswählen', 'Typische Fehler'], 'In jeder Übung mit Varianten, im Layout und im Projekt')
print('fertig', D)
