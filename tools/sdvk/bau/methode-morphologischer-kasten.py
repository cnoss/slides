# Bauskript methode-morphologischer-kasten. Aufruf: python3 tools/sdvk/bau/methode-morphologischer-kasten.py
import glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'methode-morphologischer-kasten'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Morphologischer Kasten', 'Methode // Variieren')

K = '#231f20'; G1 = '#888888'; G2 = '#d9d9d9'; HG = '#e4e4e4'; BI = '#c4c4c4'; TX = '#aaaaaa'; L = '#9313ce'

W(D, '005-frage.md', kopf('Rechenfrage', '''
**Einstieg (ca. 1 Minute).** Kopfrechnen lassen, Zahlen reinrufen. Typisch sind 12 (drei mal vier) und 64. Richtig ist 64: Jede Ausprägung der ersten Variable lässt sich mit jeder der zweiten und jeder der dritten kombinieren, also 4 × 4 × 4.

Das ist auch die Zahl der Varianten in der Card-Übung. Die 64 sind kein willkürliches Pensum, sondern das Ergebnis eines Kastens mit drei Variablen.
''') + '''{% question "Drei Variablen, je vier Ausprägungen.", "Wie viele Varianten sind das?" %}

{% statement "4 × 4 × 4 = 64", "Jede Ausprägung lässt sich mit jeder anderen kombinieren. So viele Varianten bauen Sie in der Card-Übung." %}
''')

AUSP = [('Bildposition', ['oben', 'links', 'als Hintergrund', 'ohne Bild']),
        ('Titelgröße', ['S', 'M', 'L', 'XL']),
        ('Fläche', ['keine', 'hellgrau', 'Rahmen', 'dunkel'])]
PFAD = [0, 2, 1]  # oben, L, hellgrau
def tabelle(pfad=False):
    z = '| Variable | 1 | 2 | 3 | 4 |\n|---|---|---|---|---|\n'
    for i, (v, a) in enumerate(AUSP):
        zellen = [(f'<span style="background:{L};color:#ffffff;padding:.2em .6em;">{x}</span>' if pfad and j == PFAD[i] else x) for j, x in enumerate(a)]
        z += f'| **{v}** | ' + ' | '.join(zellen) + ' |\n'
    return z
W(D, '010-kasten.md', kopf('Der Kasten', '''
Der Kasten ist eine Tabelle: In den Zeilen stehen die Variablen, in den Spalten ihre Ausprägungen. Jede Variante ist ein Weg durch den Kasten, aus jeder Zeile genau eine Zelle.

Der lila Weg: Bild oben, Titel L, Fläche hellgrau. Das ist eine von 64 Karten.

Die Variablen kommen aus dem Variieren entlang einer Achse: Jede Achse, bei der man unsicher war, wird eine Zeile. Die Stufen der Achse werden die Ausprägungen.

**Hintergrund**

Die Methode geht auf Fritz Zwicky zurück (1898 bis 1974), Schweizer Astrophysiker am California Institute of Technology. Er hat sie in den 1940er-Jahren unter anderem für Raketenantriebe entwickelt, um alle denkbaren Lösungen eines Problems systematisch zu erfassen. Buch: »Entdecken, Erfinden, Forschen im morphologischen Weltbild« (1966). Daten aus dem Gedächtnis, bitte prüfen.
''') + '''{% interlude "Der Kasten", "Variablen in die Zeilen, Ausprägungen in die Spalten" %}

<section class="simple" data-transition="fade">
<div>

# Drei Variablen, je vier Ausprägungen

''' + tabelle() + '''
</div>
</section>

<section class="simple" data-transition="none">
<div>

# Eine Variante ist ein Weg durch den Kasten

''' + tabelle(pfad=True) + '''
</div>
</section>
''')

# ---------------------------------------------------------------- 64 Thumbnails
TITEL_H = [4, 7, 10, 14]
def thumb(x, y, bp, ti, fl, aus=False, mark=False):
    w, h = 84, 96
    o = f'<g opacity="{0.18 if aus else 1}">'
    dunkel = fl == 3
    tf = G2 if dunkel else G1; zf = '#6a6a6a' if dunkel else TX
    if fl == 1: o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{HG}" />'
    if fl == 2: o += f'<rect x="{x+1}" y="{y+1}" width="{w-2}" height="{h-2}" fill="none" stroke="{G1}" stroke-width="2" />'
    if fl == 3: o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{K}" />'
    i = 7; th = TITEL_H[ti]
    if bp == 0:
        o += f'<rect x="{x+i}" y="{y+i}" width="{w-2*i}" height="34" fill="{BI}" />'; ty = y + i + 42
        o += f'<rect x="{x+i}" y="{ty}" width="{w-2*i-10}" height="{th}" fill="{tf}" />'
        o += f'<rect x="{x+i}" y="{ty+th+6}" width="{w-2*i}" height="4" fill="{zf}" /><rect x="{x+i}" y="{ty+th+14}" width="{w-2*i-20}" height="4" fill="{zf}" />'
    elif bp == 1:
        o += f'<rect x="{x+i}" y="{y+i}" width="30" height="{h-2*i}" fill="{BI}" />'; tx = x + i + 36; tw = w - 2 * i - 36
        o += f'<rect x="{tx}" y="{y+i+4}" width="{tw}" height="{th}" fill="{tf}" />'
        o += f'<rect x="{tx}" y="{y+i+th+10}" width="{tw}" height="4" fill="{zf}" /><rect x="{tx}" y="{y+i+th+18}" width="{tw-10}" height="4" fill="{zf}" />'
    elif bp == 2:
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{BI}" />'
        o += f'<rect x="{x+i}" y="{y+h-i-th-12}" width="{w-2*i-10}" height="{th}" fill="#ffffff" />'
        o += f'<rect x="{x+i}" y="{y+h-i-6}" width="{w-2*i-20}" height="4" fill="#ffffff" />'
    else:
        o += f'<rect x="{x+i}" y="{y+i+4}" width="{w-2*i-10}" height="{th}" fill="{tf}" />'
        for n in range(3): o += f'<rect x="{x+i}" y="{y+i+th+12+n*9}" width="{w-2*i-(n*10)}" height="4" fill="{zf}" />'
    o += '</g>'
    if mark: o += f'<line x1="{x}" y1="{y+h+6}" x2="{x+w}" y2="{y+h+6}" stroke="{L}" stroke-width="4" stroke-linecap="round" />'
    return o

def raster(aussortieren=False):
    o = ''
    for r in range(8):
        for c in range(8):
            bp = r // 2; fl = (r % 2) * 2 + c // 4; ti = c % 4
            # Sinnlos: Bild als Hintergrund verdeckt jede Fläche, XL-Titel passt neben dem Bild nicht
            aus = aussortieren and ((bp == 2 and fl != 0) or (bp == 1 and ti == 3))
            mark = aussortieren and (bp, ti, fl) == (0, 2, 1)
            o += thumb(18 + c * 108, 14 + r * 110, bp, ti, fl, aus, mark)
    return o + '\n'
def fq(bu, svg):
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":900, \"h\":900, \"bu\":\"" + bu + "\"}' %}\n" + svg + "{% endframe %}"
W(D, '020-raster.md', kopf('64 auf einen Blick', '''
Alle 64 Wege durch den Kasten als Thumbnails. Je zwei Zeilen haben dieselbe Bildposition: oben, links, als Hintergrund, ohne Bild. In jeder Zeile wächst der Titel von S bis XL, links mit der einen Fläche, rechts mit der anderen.

Dann der wichtigste Schritt, den viele vergessen: aussortieren. Nicht jede Kombination ergibt Sinn.

- **Bild als Hintergrund:** Die Fläche liegt darunter und ist gar nicht zu sehen. Diese Varianten sind Dubletten.
- **Bild links mit Titel XL:** Der Titel hat neben dem Bild keinen Platz.

Übrig bleiben 48. Eine davon ist lila markiert: Sie kommt aus dem Weg durch den Kasten von eben und wird jetzt im Grid mit echten Inhalten geprüft (siehe Variieren entlang einer Achse, im Kontext prüfen).
''', transition='none') + fq('Alle 64 Kombinationen', raster()) + '''

{% interlude "Nicht jede Kombination ergibt Sinn.", "Aussortieren gehört zur Methode." %}

''' + fq('Aussortiert: Dubletten und was nicht passt. Eine Kandidatin geht in den Kontext', raster(True)) + '\n')

W(D, '030-schritte.md', kopf('Schritte', '''
**1. Variablen sammeln:** Was lässt sich an der Lösung verändern? Zwei bis vier Variablen reichen.

**2. Ausprägungen festlegen:** pro Variable drei bis fünf, deutlich unterschieden.

**3. Kombinieren:** alle Wege durch den Kasten, bei wenigen Variablen vollständig.

**4. Aussortieren:** Dubletten, Unmögliches, Widersprüche.

**5. Im Kontext prüfen:** die besten Kandidaten im Grid, mit echten Inhalten.
''') + liste('In fünf Schritten', [
  '<strong>1. Variablen sammeln:</strong> zwei bis vier',
  '<strong>2. Ausprägungen festlegen:</strong> drei bis fünf, deutlich unterschieden',
  '<strong>3. Kombinieren:</strong> alle Wege durch den Kasten',
  '<strong>4. Aussortieren:</strong> Dubletten und Unmögliches',
  '<strong>5. Im Kontext prüfen:</strong> die besten Kandidaten im Grid',
]) + '\n')

W(D, '040-grenzen.md', kopf('Grenzen und Fehler', '''
**Kombinatorische Explosion:** Fünf Variablen mit je fünf Ausprägungen ergeben 3125 Varianten. Die baut niemand. Deshalb wenige Variablen, oder nur ausgewählte Wege durch den Kasten bauen statt aller.

**Typische Fehler:** Kombinationen bauen, ohne sie anzuschauen. Sinnlose Varianten nicht aussortieren und dann zwischen Dubletten entscheiden. Und zu glauben, die beste Variante ergebe sich von selbst: Der Kasten liefert Möglichkeiten, die Entscheidung bleibt Ihre.
''') + '''{% interlude "Und bei fünf Variablen?", "5 × 5 × 5 × 5 × 5 = 3125" %}

''' + liste('Typische Fehler', [
  'Zu viele Variablen: Der Kasten explodiert',
  'Kombinieren, ohne hinzuschauen',
  'Sinnlose Varianten nicht aussortieren',
  'Glauben, der Kasten entscheidet: Er liefert Möglichkeiten, entscheiden müssen Sie',
]) + '\n')

W(D, '050-verweise.md', kopf('Verweise', '''
Der Kasten baut auf dem Variieren entlang einer Achse auf: erst einzelne Achsen verstehen, dann kombinieren. Haltung dahinter: Entwickeln Sie Alternativen, über das Naheliegende hinaus.
''') + '''{% statement "Verweise", "Dahinter: [Variieren entlang einer Achse](../methode-variieren-achse/) und [Alternativen](../haltung-alternativen/). Prüfen: im Kontext und mit dem [Unschärfe- und Graustufentest](../methode-unschaerfetest/)." %}
''')

done(D, 'Variablen und Ausprägungen in einer Tabelle systematisch kombinieren, Sinnloses aussortieren, Kandidaten im Kontext prüfen',
     'Morphologischer Kasten, Variable, Ausprägung, Kombination')
index(D, ['Rechenfrage: 4 × 4 × 4', 'Der Kasten und ein Weg hindurch', '64 Thumbnails, aussortieren', 'Schritte', 'Grenzen und Fehler'], 'Wenn mehrere Achsen zusammenkommen, etwa bei Varianten einer Komponente')
p = f'{NEW}/{D}/index.md'; s = open(p).read(); open(p, 'w').write(s.replace('tiefe: ""', 'tiefe: "kennen"'))
print('fertig', D)
