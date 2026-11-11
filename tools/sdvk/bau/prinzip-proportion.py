# Bauskript prinzip-proportion. Aufruf: python3 tools/sdvk/bau/prinzip-proportion.py
import glob, math
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'prinzip-proportion'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Proportion', 'Prinzip // Dosieren')

K = '#231f20'; L = '#9313ce'; G1 = '#888888'; G2 = '#d9d9d9'; KARTE = '#e4e4e4'; BILD = '#c4c4c4'
PHI = (1 + 5 ** 0.5) / 2

def fr(bu, inner, w=900, h=500, animate=True):
    a = '' if animate else ', "animate":false'
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":" + str(w) + ", \"h\":" + str(h) + a + ", \"bu\":\"" + bu + "\"}' %}\n" + inner + "{% endframe %}"

# ---------------------------------------------------------------- 010 Schätzfrage
VERH = [2 ** 0.5, 2.0, PHI, 1.0, 1.25]  # A bis E, gemischt
def rechtecke(golden=False):
    h = 130; gap = 36
    ws = [h * v for v in VERH]
    x = (1100 - sum(ws) - gap * 4) / 2; o = ''
    for i, (w, v) in enumerate(zip(ws, VERH)):
        f = L if (golden and abs(v - PHI) < 0.01) else G2
        o += f'<rect data-id="r{i}" x="{x:.1f}" y="{185}" width="{w:.1f}" height="{h}" fill="{f}" />\n'
        x += w + gap
    return o
W(D, '010-schaetzfrage.md', kopf('Schätzfrage', '''
**Abstimmung (ca. 2 Minuten).** Fünf Rechtecke, gleich hoch, verschieden breit. Von links nach rechts A bis E. Frage: Welches gefällt Ihnen am besten? Per Handzeichen abstimmen, die Stimmen grob an die Tafel.

**Auflösung:** A ist 1 : 1,414 (das Format von DIN A4), B ist 1 : 2, C ist 1 : 1,618, der Goldene Schnitt, D ist ein Quadrat, E ist 1 : 1,25.

Was meistens passiert: C bekommt viele Stimmen, aber nicht alle, und A liegt oft dicht dahinter. Das ist genau der Stand der Forschung.

**Hintergrund**

Gustav Theodor Fechner hat 1876 in der »Vorschule der Ästhetik« Versuchspersonen zehn Rechtecke vorgelegt. Das goldene Rechteck bekam die meisten Stimmen, aber bei Weitem nicht alle. Spätere Versuche konnten das nur schwach oder gar nicht bestätigen (u. a. McManus, 1980): Die Vorliebe hängt stark von Anordnung, Kontext und Person ab. Zahlen aus dem Gedächtnis, bitte prüfen.
''', transition='none') + '''{% interlude "Welches Rechteck ist das schönste?", "Stimmen Sie ab. Von links nach rechts: A bis E." %}

''' + fr('A, B, C, D oder E?', rechtecke(), w=1100) + '\n' + fr('C ist das goldene Rechteck, 1 : 1,618. Hat es gewonnen?', rechtecke(True), w=1100) + '\n')

# ---------------------------------------------------------------- 020 Regel
def karten(fest):
    ws = [170, 250, 330]; x = 60; o = ''
    for i, w in enumerate(ws):
        bh = 140 if fest else w / 1.5
        y = 60
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{bh + 84:.1f}" fill="{KARTE}" />\n'
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{bh:.1f}" fill="{BILD}" />\n'
        o += f'<rect x="{x + 16}" y="{y + bh + 18:.1f}" width="{w * 0.6:.1f}" height="14" fill="{G1}" />\n'
        o += f'<rect x="{x + 16}" y="{y + bh + 44:.1f}" width="{w - 32}" height="9" fill="#aaaaaa" />\n'
        x += w + 40
    return o
W(D, '020-regel.md', kopf('Verhältnis statt Einzelmaß', '''
Die Regel: Proportionen entstehen aus Verhältnissen, nicht aus festen Pixelwerten. Bei responsiven Layouts gibt es den einen Pixelwert ohnehin nicht. Eine Card ist mal 170, mal 330 Pixel breit.

Erste Fassung: Das Bild jeder Card hat dasselbe Seitenverhältnis, 3 : 2. Die drei Cards wirken wie eine Familie, nur verschieden groß. Zweite Fassung: Das Bild hat überall dieselbe Höhe, 140 Pixel. Die schmale Card wirkt fast quadratisch, die breite wie ein Streifen. Jede Card hat plötzlich einen anderen Charakter.

Im CSS ist genau das eine Zeile: aspect-ratio: 3 / 2. In Figma lässt sich das Seitenverhältnis eines Rahmens sperren.
''', transition='none') + '''{% interlude "Verhältnis statt Einzelmaß.", "Gute Proportionen entstehen aus Beziehungen, nicht aus Pixeln." %}

''' + fr('Gleiches Verhältnis, 3 : 2: drei Größen, eine Familie', karten(False), animate=False) + '\n' + fr('Gleiche Höhe, 140 Pixel: drei Cards, drei Charaktere', karten(True), animate=False) + '\n')

# ---------------------------------------------------------------- 030 Goldener Schnitt
def golden(spirale=False):
    x, y, w, h = 190, 60, 380 * PHI, 380
    o = f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" fill="none" stroke="{K}" stroke-width="3" />\n'
    # Quadrate abtrennen: links, oben, rechts, unten, …
    rx, ry, rw, rh = x, y, w, h; arcs = ''
    for i in range(7):
        s = min(rw, rh); seite = i % 4
        if seite == 0:   sq = (rx, ry); rx += s; rw -= s; lin = (rx, ry, rx, ry + rh); a = (sq[0] + s, sq[1] + s, sq[0], sq[1] + s, sq[0] + s, sq[1])
        elif seite == 1: sq = (rx, ry); ry += s; rh -= s; lin = (rx, ry, rx + rw, ry); a = (sq[0], sq[1] + s, sq[0], sq[1], sq[0] + s, sq[1])
        elif seite == 2: sq = (rx + rw - s, ry); rw -= s; lin = (rx + rw, ry, rx + rw, ry + rh); a = (sq[0], sq[1], sq[0] + s, sq[1], sq[0] + s, sq[1] + s)
        else:            sq = (rx, ry + rh - s); rh -= s; lin = (rx, ry + rh, rx + rw, ry + rh); a = (sq[0] + s, sq[1], sq[0] + s, sq[1] + s, sq[0], sq[1] + s)
        if i == 0:
            o += f'<rect x="{sq[0]:.1f}" y="{sq[1]:.1f}" width="{s:.1f}" height="{s:.1f}" fill="{L}" fill-opacity="0.25" />\n'
        o += f'<line x1="{lin[0]:.1f}" y1="{lin[1]:.1f}" x2="{lin[2]:.1f}" y2="{lin[3]:.1f}" stroke="{K}" stroke-width="2" stroke-linecap="round" />\n'
        arcs += f'<path d="M{a[0]:.1f} {a[1]:.1f} A{s:.1f} {s:.1f} 0 0 1 {a[4]:.1f} {a[5]:.1f}" fill="none" stroke="{L}" stroke-width="3" stroke-linecap="round" />\n' if False else ''
    return o

def teilung():
    x0, x1, y = 120, 780, 250
    a = (x1 - x0) / PHI
    return (f'<line x1="{x0}" y1="{y}" x2="{x0 + a:.1f}" y2="{y}" stroke="{L}" stroke-width="10" stroke-linecap="round" />\n'
            f'<line x1="{x0 + a + 14:.1f}" y1="{y}" x2="{x1}" y2="{y}" stroke="{K}" stroke-width="10" stroke-linecap="round" />\n')

W(D, '030-goldener-schnitt.md', kopf('Der Goldene Schnitt', '''
Der Goldene Schnitt teilt eine Strecke so, dass sich der kleine Teil zum großen verhält wie der große zum Ganzen. Das ergibt etwa 1 : 1,618. Das goldene Rechteck hat dieses Seitenverhältnis. Trennt man ein Quadrat ab, bleibt wieder ein goldenes Rechteck übrig, und das immer weiter.

Als Konstruktionshilfe ist er brauchbar: für die Teilung eines Formats, für das Verhältnis von Inhalt und Seitenleiste, für eine Schriftgrößen-Skala. Als Beweis für Schönheit taugt er nicht.

**Der Mythos-Anteil:** Behauptet wird der Goldene Schnitt im Parthenon, in der Mona Lisa, im Apple-Logo, im Nautilus-Gehäuse. Für die meisten Fälle gibt es keinen Beleg. Die Spiralen werden nachträglich darübergelegt, und weil man Anfangs- und Endpunkte frei wählt, passt fast immer irgendetwas. Der Nautilus wächst nachweislich in einem anderen Verhältnis.

**Hintergrund**

Euklid beschreibt die Teilung um 300 v. Chr. als »Teilung im äußeren und mittleren Verhältnis«. Der Name »Goldener Schnitt« taucht erst im 19. Jahrhundert auf (Martin Ohm, 1835) und wurde durch Adolf Zeising (1854) populär, der ihn zum Naturgesetz der Schönheit erklärte. Zum Weiterlesen: Mario Livio, »The Golden Ratio« (2002). Angaben aus dem Gedächtnis, bitte prüfen.
''', transition='none') + '''{% interlude "Der Goldene Schnitt", "1 : 1,618, und ein bisschen Mythos" %}

''' + fr('Der kleine Teil verhält sich zum großen wie der große zum Ganzen', teilung(), animate=False) + '\n' + fr('Quadrat ab, übrig bleibt wieder ein goldenes Rechteck', golden(), animate=False) + '''

{% statement "Eine Hilfe, kein Beweis.", "Der Goldene Schnitt kann beim Teilen helfen. Dass etwas schön ist, weil es golden ist, lässt sich nicht belegen." %}
''')

# ---------------------------------------------------------------- 040 Rechnen mit Verhältnissen
def drittel():
    x, y, w, h = 150, 50, 600, 400
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{KARTE}" />\n'
    o += f'<rect x="{x}" y="{y + h * 2 / 3:.1f}" width="{w}" height="{h / 3:.1f}" fill="{BILD}" />\n'
    o += f'<circle cx="{x + w * 2 / 3:.1f}" cy="{y + h / 3:.1f}" r="38" fill="{K}" />\n'
    for i in (1, 2):
        o += f'<line x1="{x + w * i / 3:.1f}" y1="{y}" x2="{x + w * i / 3:.1f}" y2="{y + h}" stroke="{L}" stroke-width="3" stroke-linecap="round" />\n'
        o += f'<line x1="{x}" y1="{y + h * i / 3:.1f}" x2="{x + w}" y2="{y + h * i / 3:.1f}" stroke="{L}" stroke-width="3" stroke-linecap="round" />\n'
    return o

def a_reihe():
    x, y, w, h = 150, 40, 420 * 2 ** 0.5, 420
    o = f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" fill="{G2}" />\n'
    rx, ry, rw, rh = x, y, w, h
    for i in range(6):
        if rw >= rh:
            rw /= 2; o += f'<line x1="{rx + rw:.1f}" y1="{ry:.1f}" x2="{rx + rw:.1f}" y2="{ry + rh:.1f}" stroke="{K}" stroke-width="3" stroke-linecap="round" />\n'
            rx += rw
        else:
            rh /= 2; o += f'<line x1="{rx:.1f}" y1="{ry + rh:.1f}" x2="{rx + rw:.1f}" y2="{ry + rh:.1f}" stroke="{K}" stroke-width="3" stroke-linecap="round" />\n'
            ry += rh
    o += f'<rect x="{rx:.1f}" y="{ry:.1f}" width="{rw:.1f}" height="{rh:.1f}" fill="{L}" />\n'
    return o

def fibo():
    zahlen = [5, 8, 13, 21, 34, 55]; o = ''; y = 80
    for z in zahlen:
        o += f'<rect x="150" y="{y}" width="{z * 10}" height="34" fill="{L if z == 21 else G1}" />\n'; y += 56
    return o

W(D, '040-rechnen.md', kopf('Mit Verhältnissen rechnen', '''
Zwei Verhältnisse, mit denen sich im Alltag arbeiten lässt.

**Drittel:** Format in drei mal drei Felder teilen, Wichtiges auf eine Linie oder einen Schnittpunkt legen. Das ist eine vereinfachte Annäherung an den Goldenen Schnitt und aus der Fotografie bekannt. Ein Horizont genau in der Mitte wirkt oft starr, auf dem unteren Drittel ruhiger.

**DIN A:** Die Formate der A-Reihe haben das Verhältnis 1 : √2, etwa 1 : 1,414. Halbiert man ein A-Blatt, hat die Hälfte wieder dasselbe Verhältnis. Darum wird aus A4 durch Falten A5. Festgelegt in DIN 476 (1922), international ISO 216.

Die Zahlenreihen (Fibonacci, Renard) kommen im nächsten Abschnitt.

Bildmaterial dazu im bisherigen Foliensatz Proportionen und Abstände. Angaben aus dem Gedächtnis, bitte prüfen.
''', transition='none') + '''{% interlude "Mit Verhältnissen rechnen", "Drittel und DIN A" %}

''' + '\n'.join([
  fr('Drittel: Wichtiges auf eine Linie oder einen Schnittpunkt', drittel(), animate=False),
  fr('DIN A: Halbiert bleibt das Verhältnis gleich, 1 : 1,414', a_reihe(), animate=False),
]) + '\n')

# ---------------------------------------------------------------- 045 Zahlenreihen
FIB = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
R5 = [10, 16, 25, 40, 63, 100]
def reihe(zahlen, mark=(), skala=4.6, h=26, gap=12, x0=150):
    o = ''; y = (500 - len(zahlen) * (h + gap) + gap) / 2
    for i, z in enumerate(zahlen):
        o += f'<rect data-id="b{i}" x="{x0}" y="{y:.1f}" width="{max(z * skala, 4):.1f}" height="{h}" fill="{L if z in mark else G1}" />\n'
        y += h + gap
    return o

def skala_live(titel, stufen, quelle):
    # stufen: (Zahl, Rolle, Text, Schnitt). Größen proportional in vh, damit die Verhältnisse auf jedem Beamer stimmen
    f = 0.16
    zeilen = ''.join(
        f'<div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;">'
        f'<div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">{z}</div>'
        f'<div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">{rolle}</div>'
        f'<div style="font-family:IBM;font-weight:{w};font-size:{z * f:.2f}vh;line-height:1.1;white-space:nowrap;color:#231f20;">{text}</div></div>'
        for z, rolle, text, w in stufen)
    return (f'<section class="simple" data-transition="fade">\n  <div>\n    <h1>{titel}</h1>\n'
            f'    <div style="width:100%;text-align:left;">{zeilen}</div>\n    <p style="font-size:1.8vh;color:#6a6a6a;margin-top:2vh;">{quelle}</p>\n  </div>\n</section>')

def seite_live(titel, marken, quelle):
    # Seitenaufbau wie im bisherigen Foliensatz: Positionen von oben und Schriftgrade aus derselben Reihe
    u = 0.55; h = max(m[0] for m in marken) * u + 14
    inhalt = ''
    for pos, label, text, gr, w in marken:
        top = pos * u
        inhalt += (f'<div style="position:absolute;left:0;top:{top:.1f}vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">{pos}</div>'
                   f'<div style="position:absolute;left:8vw;right:0;top:{top:.1f}vh;border-top:2px solid #9313ce;"></div>'
                   f'<div style="position:absolute;left:10vw;top:{top + 0.8:.1f}vh;font-family:IBM;font-weight:{w};font-size:{gr}vh;line-height:1.15;color:#231f20;max-width:48vw;">{text}</div>')
    return (f'<section class="simple" data-transition="fade">\n  <div>\n    <h1>{titel}</h1>\n'
            f'    <div style="position:relative;width:62vw;height:{h:.1f}vh;text-align:left;">{inhalt}</div>\n'
            f'    <p style="font-size:1.8vh;color:#6a6a6a;margin-top:1vh;">{quelle}</p>\n  </div>\n</section>')

LOREM = 'Gute Proportionen entstehen aus Beziehungen. Wer Größen und Abstände aus einer Reihe wählt, bekommt Verhältnisse, die zusammenpassen.'
W(D, '045-zahlenreihen.md', kopf('Zahlenreihen', '''
**Zahlenreihen** sind Proportion zum Mitnehmen: Statt jede Größe einzeln zu erfinden, wählt man aus einer Reihe, deren Werte in einem festen Verhältnis zueinander stehen. Dann passen Schriftgrade, Abstände und Flächen von selbst zusammen.

**Fibonacci-Folge:** Jede Zahl ist die Summe der beiden davor: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144. Das Verhältnis zweier Nachbarn nähert sich schnell dem Goldenen Schnitt (34 : 21 ≈ 1,619). Benannt nach Leonardo von Pisa, genannt Fibonacci, »Liber abaci« (1202), der damit das Wachstum einer Kaninchenpopulation durchrechnet. In der Typografie lässt sich die Reihe direkt als Schriftgrad-Skala nutzen: 13, 21, 34, 55.

**Renard-Reihen:** Charles Renard, französischer Militäringenieur, standardisierte um 1877 die Kabel für Fesselballone und reduzierte dabei die Zahl der Varianten drastisch (laut bisherigem Foliensatz von 425 auf 17). Seine Reihen teilen jede Zehnerpotenz in gleich große Stufen: R5 in fünf Stufen mit dem Faktor fünfte Wurzel aus 10, also ≈ 1,585, also 10, 16, 25, 40, 63, 100. R10 in zehn Stufen mit dem Faktor zehnte Wurzel aus 10, also ≈ 1,259: 10, 12,5, 16, 20, 25, 31,5, 40, 50, 63, 80, 100. Genormt als Normzahlen (DIN 323, ISO 3). Im Alltag stecken sie zum Beispiel in Leitungsquerschnitten (1,5, 2,5, 4, 6, 10, 16, 25 mm²), bitte prüfen.

**Die Pointe für den Screen:** R5 liegt nah am Goldenen Schnitt (1,585 gegen 1,618), R10 nah an der beliebten Typo-Skala 1,25 (große Terz). R5 beginnt bei 10 und enthält die 16: Mit 16 px als Grundschrift ergibt sich 10, 16, 25, 40, 63. Die klassische Schriftgradreihe des Bleisatzes (6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 21, 24, 36, 48, 60, 72 Punkt) ist dagegen keine geometrische Reihe, sondern eine über Jahrhunderte gewachsene Auswahl. Bringhurst druckt sie in »The Elements of Typographic Style« ab (bitte prüfen).

Die Beispiele sind mit IBM Plex Sans live gesetzt. Die Größen sind auf den Beamer skaliert, die Verhältnisse stimmen. Der Seitenaufbau greift das Beispiel aus dem bisherigen Foliensatz auf: Positionen und Schriftgrade aus derselben Reihe.

**Hintergrund**

Normzahlen: DIN 323, ISO 3 und ISO 17. Fibonacci: »Liber abaci«, 1202. Renard: um 1877. Angaben teils aus dem Gedächtnis, bitte prüfen.
''', transition='none') + '''{% interlude "Zahlenreihen", "Größen aus einer Reihe statt aus dem Bauch" %}

''' + '\n'.join([
  fr('Fibonacci: Jede Zahl ist die Summe der beiden davor', reihe(FIB, mark=(13, 21, 34, 55))),
  skala_live('Fibonacci als Schriftgrade', [(13, 'Text', LOREM[:60] + ' …', 400), (21, 'Zwischentitel', 'Verhältnis statt Einzelmaß', 500), (34, 'Titel', 'Zahlenreihen', 600), (55, 'Display', 'Proportion', 600)], 'Jede Stufe etwa 1,618-mal größer als die vorige'),
  seite_live('Fibonacci im Seitenaufbau', [(13, '', 'Kolumnentitel', 1.6, 600), (21, '', 'Headline in derselben Reihe', 3.4, 600), (34, '', LOREM, 2.1, 400), (55, '', LOREM, 2.1, 400), (89, '', '', 2, 400)], 'Abstand von oben, in Einheiten: 13, 21, 34, 55, 89'),
]) + '''

{% interlude "Renard-Reihen", "Zehn bis hundert in gleichen Schritten" %}

''' + '\n'.join([
  fr('Renard R5: 10, 16, 25, 40, 63, 100, jede Stufe etwa 1,585-mal größer', reihe(R5, mark=(16,), skala=7.2, h=40, gap=18)),
  skala_live('Renard R5 als Schriftgrade', [(10, 'Klein', 'Bildunterschrift und Quellenangabe', 400), (16, 'Text', LOREM[:60] + ' …', 400), (25, 'Zwischentitel', 'Verhältnis statt Einzelmaß', 500), (40, 'Titel', 'Zahlenreihen', 600), (63, 'Display', 'Proportion', 600)], 'Mit 16 px als Grundschrift: 10, 16, 25, 40, 63'),
  seite_live('Renard im Seitenaufbau', [(10, '', 'Kolumnentitel', 1.6, 600), (16, '', 'Headline in derselben Reihe', 3.4, 600), (25, '', LOREM, 2.1, 400), (40, '', LOREM, 2.1, 400), (63, '', LOREM, 2.1, 400), (100, '', '', 2, 400)], 'Abstand von oben, in Einheiten: 10, 16, 25, 40, 63, 100'),
]) + '''

<section class="simple" data-transition="fade">
<div>

# Reihen im Vergleich

| Reihe | Faktor | Beispiel | Nah an |
|---|---|---|---|
| **Fibonacci** | ≈ 1,618 | 13, 21, 34, 55 | Goldener Schnitt |
| **Renard R5** | ≈ 1,585 | 10, 16, 25, 40, 63 | Goldener Schnitt |
| **DIN A** | ≈ 1,414 | 210 × 297 mm | Quadratwurzel aus 2 |
| **Typografische Skala** | 1,25 | 16, 20, 25, 31, 39 | Renard R10 (≈ 1,259) |
| **Klassische Schriftgrade** | kein fester | 8, 9, 10, 12, 14, 18, 24, 36 | über Jahrhunderte gewachsen |

</div>
</section>

{% question "Welche Reihe steckt in Ihrer Typografischen Skala?", "Und aus welcher Reihe stammen Ihre Abstände?" %}

{% statement "Die Skala erledigt die Proportion.", "Typografische Skala und Spacing-System sind Proportion zum Mitnehmen: Wer aus einer Reihe wählt, muss nicht jedes Verhältnis neu erfinden." %}
''')

# ---------------------------------------------------------------- 050 Grenzen
W(D, '050-grenzen.md', kopf('Grenzen', '''
Proportionsregeln sind Werkzeuge für den Anfang und für Entscheidungen, die man begründen will. Sie ersetzen nicht das Hinschauen. Die optische Korrektur gilt auch hier: Was rechnerisch stimmt, kann optisch daneben liegen.

Und auf dem Screen bestimmt oft der Inhalt die Proportion, nicht die Mathematik. Ein Text, der nicht in ein goldenes Rechteck passt, wird nicht gekürzt, damit die Zahl stimmt.
''') + liste('Wann tragen Proportionsregeln nicht?', [
  'Wenn sie als Beweis dienen sollen: »Das ist golden, also schön.«',
  'Wenn die Rechnung stimmt, aber das Auge nicht: dann optisch korrigieren.',
  'Wenn der Inhalt nicht hineinpasst: Inhalt bestimmt Form.',
]) + '''

{% statement "Verweise", "Weiter: [Spacing-System](../methode-spacing-system/), [Typografische Skala](../methode-typografische-skala/), [Weißraum](../prinzip-weissraum/), [Gestaltungsraster](../methode-gestaltungsraster/) und [Inhalt bestimmt Form](../prinzip-inhalt-bestimmt-form/). Dahinter: [Optische Korrektur](../phaenomen-optische-korrektur/)." %}
''')

open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Proportion"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Prinzip"
gruppe: "Dosieren"
tiefe: ""
einsatz: ""
kurzsatz: "Gute Proportionen entstehen aus Verhältnissen, nicht aus Einzelmaßen. Goldener Schnitt, Drittel und Zahlenreihen helfen, beweisen aber nichts"
begriffe: ["Proportion", "Seitenverhältnis", "Goldener Schnitt", "Drittelregel", "Fibonacci-Folge", "Renard-Reihe", "Normzahlen"]
herkunft: "U: proportionen-und-abstaende/030, 040"
inhalt:
  - "Schätzfrage: Welches Rechteck?"
  - "Verhältnis statt Einzelmaß"
  - "Goldener Schnitt und sein Mythos"
  - "Drittel, DIN A"
  - "Zahlenreihen: Fibonacci und Renard als Schriftgrade und im Seitenaufbau"
status: ok
---
''')
print('fertig', D)
