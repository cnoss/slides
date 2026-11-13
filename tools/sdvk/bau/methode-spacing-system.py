# Bauskript methode-spacing-system. Aufruf: python3 tools/sdvk/bau/methode-spacing-system.py
import glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'methode-spacing-system'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Spacing-System', 'Methode // Konstruieren')

K = '#231f20'; L = '#9313ce'; KARTE = '#e4e4e4'; BILD = '#c4c4c4'; TEXT = '#aaaaaa'; TITEL = '#888888'
FONT = 'font-family="sans-serif" font-size="15" font-weight="600"'

# ---------------------------------------------------------------- Card als Wireframe
# Abstände: (Rand links, Rand rechts, Bild bis Kategorie, Kategorie bis Titel, Titel bis Teaser, Teaser bis Link, Rand unten)
AUGE  = dict(l=24, r=24, a=31, b=5, c=23, d=12, u=38)  # nach Augenmaß: nur die vertikalen Abstände sind unruhig
SKALA = dict(l=24, r=24, a=24, b=8, c=16, d=24, u=32)
CW = 300; BH = 150

def card(p, x, y, sp, s=1.0, mass=False, seite='rechts', mark=None):
    """Card aus Bild, Kategorie, zwei Titelzeilen, drei Teaserzeilen und Link mit Pfeil.
    mark: 'inset', 'stack' oder 'inline' hebt die jeweiligen Abstände hervor."""
    w = CW * s; o = []; m = []
    def r(id_, xx, yy, ww, hh, f, rx=0):
        o.append(f'<rect data-id="{p}-{id_}" x="{xx:.1f}" y="{yy:.1f}" width="{ww:.1f}" height="{hh:.1f}" fill="{f}"' + (f' rx="{rx}"' if rx else '') + ' />')
    tx = x + sp['l'] * s; tw = w - (sp['l'] + sp['r']) * s
    dx = {k: v * s for k, v in sp.get('dx', {}).items()}
    X = lambda k: tx + dx.get(k, 0)
    cy = y + BH * s
    ys = {}
    ys['bild'] = (y, cy)
    k0 = cy + sp['a'] * s; ys['kat'] = (k0, k0 + 8 * s)
    t0 = ys['kat'][1] + sp['b'] * s; ys['titel'] = (t0, t0 + 40 * s)
    e0 = ys['titel'][1] + sp['c'] * s; ys['teaser'] = (e0, e0 + 41 * s)
    l0 = ys['teaser'][1] + sp['d'] * s; ys['link'] = (l0, l0 + 10 * s)
    hoehe = ys['link'][1] + sp['u'] * s - y
    r('karte', x, y, w, hoehe, KARTE)
    r('bild', x, y, w, BH * s, BILD)
    r('kat', X('kat'), k0, 70 * s, 8 * s, TITEL)
    r('t1', X('t'), t0, tw, 16 * s, TITEL); r('t2', X('t'), t0 + 24 * s, tw * 0.62, 16 * s, TITEL)
    for i, f in enumerate((1, 1, 0.7)):
        r(f'e{i}', X('e'), e0 + i * 16 * s, tw * f - dx.get('e', 0), 9 * s, TEXT)
    r('link', X('link'), l0, 64 * s, 10 * s, K)
    px = X('link') + 72 * s; py = l0 + 5 * s
    o.append(f'<path data-id="{p}-pfeil" d="M{px:.1f} {py - 5*s:.1f} L{px + 5*s:.1f} {py:.1f} L{px:.1f} {py + 5*s:.1f}" fill="none" stroke="{K}" stroke-width="{2.5*s:.1f}" stroke-linecap="round" stroke-linejoin="round" />')
    lucken = [('a', cy, k0, sp['a']), ('b', ys['kat'][1], t0, sp['b']), ('c', ys['titel'][1], e0, sp['c']),
              ('d', ys['teaser'][1], l0, sp['d']), ('u', ys['link'][1], y + hoehe, sp['u'])]
    if mass:
        bx = x + w + 14 if seite == 'rechts' else x - 14
        tx2 = bx + 8 if seite == 'rechts' else bx - 8
        anker = 'start' if seite == 'rechts' else 'end'
        for k, y1, y2, v in lucken:
            m.append(f'<line data-id="{p}-m{k}" x1="{bx:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{y2:.1f}" stroke="{L}" stroke-width="3" stroke-linecap="round" />')
            m.append(f'<text data-id="{p}-mt{k}" x="{tx2:.1f}" y="{(y1 + y2) / 2 + 5:.1f}" text-anchor="{anker}" {FONT} fill="{L}">{v}</text>')
        # Rand links
        m.append(f'<line data-id="{p}-ml" x1="{x:.1f}" y1="{k0 - 6:.1f}" x2="{tx:.1f}" y2="{k0 - 6:.1f}" stroke="{L}" stroke-width="3" stroke-linecap="round" />')
        m.append(f'<text data-id="{p}-mtl" x="{x + 3:.1f}" y="{k0 - 12:.1f}" {FONT} fill="{L}">{sp["l"]}</text>')
    if mark == 'inset':
        op = 'fill-opacity="0.45"'
        m.append(f'<rect x="{x:.1f}" y="{cy:.1f}" width="{sp["l"]*s:.1f}" height="{hoehe - BH*s:.1f}" fill="{L}" {op} />')
        m.append(f'<rect x="{x + w - sp["r"]*s:.1f}" y="{cy:.1f}" width="{sp["r"]*s:.1f}" height="{hoehe - BH*s:.1f}" fill="{L}" {op} />')
        m.append(f'<rect x="{tx:.1f}" y="{cy:.1f}" width="{tw:.1f}" height="{sp["a"]*s:.1f}" fill="{L}" {op} />')
        m.append(f'<rect x="{tx:.1f}" y="{ys["link"][1]:.1f}" width="{tw:.1f}" height="{sp["u"]*s:.1f}" fill="{L}" {op} />')
    if mark == 'stack':
        for k, y1, y2, v in lucken[1:4]:
            m.append(f'<rect x="{tx:.1f}" y="{y1:.1f}" width="{tw:.1f}" height="{y2 - y1:.1f}" fill="{L}" fill-opacity="0.45" />')
    if mark == 'inline':
        m.append(f'<rect x="{tx + 64*s:.1f}" y="{l0 - 3*s:.1f}" width="{8*s:.1f}" height="{16*s:.1f}" fill="{L}" fill-opacity="0.6" />')
    return '\n'.join(o + m) + '\n', hoehe

def fr(bu, inner, w=900, h=500, stage='#ffffff', animate=True):
    a = '' if animate else ', "animate":false'
    return "{% frame '{\"stage\":\"" + stage + "\", \"w\":" + str(w) + ", \"h\":" + str(h) + a + ", \"bu\":\"" + bu + "\"}' %}\n" + inner + "{% endframe %}"

def paar(mass):
    a, _ = card('a', 110, 60, AUGE, mass=mass, seite='links')
    b, _ = card('b', 490, 60, SKALA, mass=mass, seite='rechts')
    return a + b

# ---------------------------------------------------------------- 005 Live-Test
W(D, '005-live-test.md', kopf('Live-Test', '''
**Live-Test (ca. 3 Minuten).** Zwei Cards mit denselben Elementen: Bild, Kategorie, Titel, Teaser, Link. Frage: Welche wirkt ruhiger, ordentlicher, »fertiger«? Handzeichen links oder rechts. Erfahrungsgemäß gewinnt rechts deutlich, aber kaum jemand kann sagen, warum.

Dann die Auflösung: Die Maße erscheinen. Links wurde nach Augenmaß gesetzt: 5, 12, 23, 31, 38 Pixel, jeder Abstand ist anders, und keiner hat einen Grund. Der Link klebt fast am Teaser, die Kategorie fast am Titel. Die Ränder links und rechts sind auf beiden Seiten gleich, unruhig sind nur die vertikalen Abstände. Rechts stammen alle Abstände aus einer Skala: 8, 16, 24, 32. Und sie folgen einer Regel: Was zusammengehört (Kategorie und Titel), steht enger als das, was trennt.

Das ist das Problem, das die Methode löst: Abstände nach Augenmaß sind fast nie falsch genug, dass es jemand bemerkt, aber zusammen ergeben sie Unruhe. Und spätestens im Team oder im Code weiß niemand mehr, welcher Wert gilt.
''', transition='none') + '''{% interlude "Welche Card wirkt ruhiger?", "Links oder rechts? Entscheiden Sie aus dem Bauch." %}

''' + fr('Links oder rechts?', paar(False)) + '\n' + fr('Links nach Augenmaß, rechts aus einer Skala', paar(True)) + '''

{% statement "Gleiche Elemente, andere Abstände.", "Abstände nach Augenmaß sind einzeln kaum falsch. Zusammen ergeben sie Unruhe, und niemand kann sie begründen." %}
''')

# ---------------------------------------------------------------- 010 Ergebnis
W(D, '010-ergebnis.md', kopf('Ergebnis zuerst', '''
So sieht das Ergebnis aus: eine kleine Skala mit Namen. Mehr nicht. Jeder Abstand im Entwurf stammt aus dieser Tabelle, und jeder hat einen Namen, den Gestaltung und Entwicklung gleich verwenden.

Die Werte wachsen nicht gleichmäßig. Kleine Schritte unten, wo feine Unterschiede zählen, große Schritte oben, wo ein Unterschied von 4 Pixeln niemandem auffällt. Die Basis ist hier 4 bzw. 8, weil sich damit gut rechnen lässt und viele Bildschirmgrößen durch 8 teilbar sind.

Die Spalte »In der Card« zeigt, wo die Werte in der Card vom Live-Test sitzen.
''') + '''{% interlude "Ergebnis zuerst", "Eine Skala, sieben Werte, jeder mit Namen" %}

<section class="simple" data-transition="fade">
<div>

# Eine Skala für alle Abstände

| Name | Wert | In der Card |
|---|---|---|
| **space-xs** | 4 px | Abstand im Icon, sehr feine Abstände |
| **space-s** | 8 px | Kategorie zu Titel, Link zu Pfeil |
| **space-m** | 16 px | Titel zu Teaser |
| **space-l** | 24 px | Innenabstand der Card, Teaser zu Link |
| **space-xl** | 32 px | zwischen zwei Cards |
| **space-2xl** | 48 px | zwischen zwei Abschnitten |
| **space-3xl** | 64 px | großer Seitenrand |

</div>
</section>
''')

# ---------------------------------------------------------------- 020 Schritte
gross = lambda mark, bu: fr(bu, card('g', 300, 25, SKALA, s=1.0, mark=mark)[0].replace('x="300.0"', 'x="300.0"'), animate=False)
W(D, '020-schritte.md', kopf('Schritte', '''
**1. Basis wählen:** 4 oder 8 Pixel. Für Interfaces hat sich 8 durchgesetzt, 4 für feine Abstände.

**2. Skala festlegen:** sechs bis acht Werte, unten fein, oben grob, etwa 4, 8, 16, 24, 32, 48, 64. Nicht jede Achtergröße aufnehmen (8, 16, 24, 32, 40, 48 …): Zwischen 40 und 48 sieht niemand einen Unterschied, aber alle müssen entscheiden.

**3. Benennen:** Werte bekommen Namen (space-s, space-m …). Dann reden alle über dasselbe.

**4. Als Token anlegen:** In Figma als Variables (Typ Number), im Code als CSS-Variablen. Ein Wert wird an einer Stelle geändert und gilt überall.

**5. Anwenden:** In Figma mit Auto Layout, das Padding (Inset) und Gap (Stack und Inline) direkt aus den Variablen nimmt. Ab jetzt wird nicht mehr geschoben, sondern gewählt.

**Inset, Stack, Inline:** Die drei Begriffe stammen von Nathan Curtis (»Space in Design Systems«, 2016). Inset ist der Innenabstand eines Containers, wie ein Passepartout. Stack ist der Abstand zwischen Elementen, die untereinander stehen. Inline ist der Abstand zwischen Elementen nebeneinander, hier zwischen Link und Pfeil. Im CSS entspricht das grob padding (Inset) und gap (Stack und Inline).

**Hintergrund**

Nathan Curtis, »Space in Design Systems«, EightShapes, Medium, 2016. Die 8-Punkt-Skala ist in Material Design und vielen anderen Design-Systemen üblich. Wathan & Schoger, Refactoring UI (»Establish a spacing and sizing system«): Nicht nach Augenmaß, sondern aus einer begrenzten Auswahl wählen, deren Stufen sich deutlich unterscheiden.
''', transition='none') + '''{% interlude "In fünf Schritten", "Von der Basis bis zum Token" %}

''' + liste('Eine Skala für alle Abstände', [
  '<strong>1. Basis wählen:</strong> 4 oder 8 Pixel',
  '<strong>2. Skala festlegen:</strong> sechs bis acht Werte, unten fein, oben grob',
  '<strong>3. Benennen:</strong> space-s, space-m, space-l …',
  '<strong>4. Als Token anlegen:</strong> Figma Variables, CSS-Variablen',
  '<strong>5. Anwenden:</strong> mit Auto Layout, nur noch Werte aus der Skala',
]) + '''

{% interlude "Inset, Stack, Inline", "Drei Sorten Abstand, drei Wörter" %}

''' + '\n'.join([
  gross(None, 'Die Card aus der Skala'),
  gross('inset', 'Inset: der Innenabstand, wie ein Passepartout'),
  gross('stack', 'Stack: Abstände zwischen Elementen untereinander'),
  gross('inline', 'Inline: Abstände zwischen Elementen nebeneinander'),
]) + '\n')

# ---------------------------------------------------------------- 025 Innen und außen, Code
def raster3():
    o = ''
    for i in range(3):
        c, h = card(f'k{i}', 60 + i * (230 + 40), 60, SKALA, s=230 / 300)
        o += c
    for i in range(2):
        x = 60 + 230 + i * 270
        o += f'<rect x="{x}" y="60" width="40" height="{h:.1f}" fill="{L}" fill-opacity="0.45" />\n'
    return o
W(D, '025-innen-aussen.md', kopf('Innen und außen', '''
Die Skala allein macht noch keine Ordnung. Die Regel aus dem Gesetz der Nähe gilt weiter: Was zusammengehört, steht enger. Innerhalb der Card liegen die Abstände bei 8 bis 24, zwischen den Cards bei 32 oder mehr. Wäre der Abstand zwischen den Cards kleiner als der Innenabstand, würden Titel und Bild der Nachbarcard optisch zusammenrücken.

Der Code zeigt, wie direkt sich das übergeben lässt: Die Skala steht einmal als CSS-Variablen da, jede Komponente nimmt sich ihre Werte. Figma Variables lassen sich genauso benennen. Wer so arbeitet, muss in der Übergabe keine Pixel mehr nachmessen.
''', transition='none') + '''{% interlude "Innen enger als außen", "Die Skala sagt, welche Werte. Die Nähe sagt, wo." %}

''' + fr('Innen 8 bis 24, außen 40: Jede Card bleibt eine Einheit', raster3(), animate=False) + '\n\n' + code('Dieselbe Skala im Code', ''':root {
  --space-s: 8px;
  --space-m: 16px;
  --space-l: 24px;
  --space-xl: 40px;
}
.card  { padding: var(--space-l); display: flex; flex-direction: column; gap: var(--space-m); }
.link  { display: flex; gap: var(--space-s); }
.cards { display: grid; gap: var(--space-xl); }''', gr=3) + '\n')

# ---------------------------------------------------------------- 030 Mini-Übung
W(D, '030-uebung.md', kopf('Mini-Übung', '''
**Mini-Übung (ca. 5 Minuten), direkt in der Vorlage des Tages.**

Jede Person legt für die Card eine Skala mit höchstens sechs Werten fest und schreibt sie als Liste neben die Card. Dann wird die Card mit Auto Layout so umgebaut, dass jeder Abstand aus dieser Liste stammt.

Danach tauschen: Die Nachbarin oder der Nachbar zeigt auf drei beliebige Abstände. Für jeden muss der Name aus der Skala kommen. Wer »ungefähr 20« sagt, hat noch einen Wert nach Augenmaß.

Die Skala bleibt für die Varianten des Tages stehen: Variiert wird ab jetzt entlang der Skala, nicht mehr beliebig.
''') + '''{% interlude "Und jetzt Sie.", "Fünf Minuten, an der Card aus der Vorlage" %}

''' + liste('Ihre Card, Ihre Skala', [
  'Legen Sie eine Skala mit höchstens sechs Werten fest.',
  'Bauen Sie die Card mit Auto Layout nur aus diesen Werten.',
  'Ihr Gegenüber zeigt auf drei Abstände. Sie nennen den Namen aus der Skala.',
]) + '\n')

# ---------------------------------------------------------------- 040 Fehler
W(D, '040-fehler.md', kopf('Typische Fehler', '''
Der häufigste Fehler im Studium: Die Skala steht, aber an einer Stelle fehlt »nur noch ein bisschen«. Ab dem ersten Wert außerhalb der Skala beginnt das Augenmaß von vorn.

Der zweite: Textrahmen in Figma. Der Zeilenabstand einer Schrift fügt über und unter der Zeile Raum hinzu. Wer zwischen zwei Textrahmen 16 einstellt, sieht optisch eher 22. Darum bei Texten auch einmal hinschauen, nicht nur messen.
''', cls='simple') + '\n'.join("{% fragment '<p class=\"list\">" + p + "</p>' %}" for p in [
  '»Nur 2 Pixel mehr«: der erste Wert außerhalb der Skala',
  'Zu feine Skala: 40 und 48 unterscheidet niemand',
  'Innen so groß wie außen: Die Cards zerfallen',
  'Abstände an jedes Element einzeln hängen statt an den Container',
  'Den Zeilenabstand vergessen: Text sieht weiter weg aus, als er ist',
]) + '\n')

# ---------------------------------------------------------------- 050 Einsatz
W(D, '050-einsatz.md', kopf('Einsatz', '''
Das Spacing-System ist eine Können-Methode. Es kommt heute in der Variantenbildung zum Einsatz, im Projekt bei den Design Tokens und im Crit (»Welcher Wert ist das?«). Es arbeitet eng mit der Typografischen Skala zusammen: Beide sind begrenzte Auswahlen statt freier Werte. Und mit dem Gestaltungsraster: Spaltenabstand und Rand sollten ebenfalls aus der Skala stammen.
''') + liste('Wo die Methode wiederkommt', [
  'Heute: Jede Variante der Card nutzt nur Werte aus Ihrer Skala',
  'Im Projekt: als Design Tokens, gemeinsam mit Farben und Schriftgrößen',
  'Im Crit: »Welcher Wert ist das?«',
]) + '''

{% statement "Merksatz", "Wählen statt schieben. Jeder Abstand kommt aus der Skala, und innen ist enger als außen." %}

{% statement "Verweise", "Dahinter: [Nähe und Abstand](../prinzip-naehe-und-abstand/). Weiter: [Typografische Skala](../methode-typografische-skala/), [Gestaltungsraster](../methode-gestaltungsraster/), [Proportion](../prinzip-proportion/) und [Weißraum](../prinzip-weissraum/)." %}
''')

open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Spacing-System"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Methode"
gruppe: "Konstruieren"
tiefe: "können"
einsatz: "Beim Konstruieren von Komponenten und Layouts, im Projekt als Design Tokens"
kurzsatz: "Abstände aus einer festen, benannten Skala wählen statt nach Augenmaß schieben"
begriffe: ["Spacing-System", "Skala", "Inset", "Stack", "Inline", "Design Token", "Auto Layout"]
herkunft: "B: proportionen-und-abstaende/060"
inhalt:
  - "Live-Test: Augenmaß gegen Skala"
  - "Ergebnis zuerst: benannte Skala"
  - "Fünf Schritte"
  - "Inset, Stack, Inline"
  - "Innen enger als außen, Skala im Code"
  - "Mini-Übung an der Card"
status: ok
---
''')
print('fertig', D)
