# Bauskript prinzip-weissraum. Aufruf: python3 tools/sdvk/bau/prinzip-weissraum.py
import glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'prinzip-weissraum'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Weißraum', 'Prinzip // Dosieren')

K = '#231f20'; L = '#9313ce'; KARTE = '#e4e4e4'; BILD = '#d9d9d9'; TEXT = '#d9d9d9'; TITEL = '#888888'

def seite(m, g):
    """Startseite als Wireframe. m = Rand, g = Abstand. Die Elemente wachsen, wenn der Weißraum schrumpft."""
    W_, H_ = 900, 500
    o = []
    def r(i, x, y, w, h, f, rx=0):
        o.append(f'<rect data-id="{i}" x="{x:.1f}" y="{y:.1f}" width="{max(w,1):.1f}" height="{max(h,1):.1f}" fill="{f}"' + (f' rx="{rx:.1f}"' if rx else '') + ' />')
    unten = m * 1.3  # Fundament: unten mehr Luft als oben
    nav = 14
    r('logo', m, m, 90, nav, K)
    for i in range(4):
        r(f'nav{i}', W_ - m - (4 - i) * 62 + 12, m + 3, 50, 8, TITEL)
    A = H_ - m - unten - nav - 2 * g
    hero = A * 0.58; feat = A - hero
    y0 = m + nav + g
    sw = (W_ - 2 * m - g) / 2
    # Hero links: alles relativ zur Höhe des Hero-Bereichs
    hl = hero * 0.14
    r('h1', m, y0, sw * 0.95, hl, TITEL); r('h2', m, y0 + hero * 0.2, sw * 0.7, hl, TITEL)
    for i, f in enumerate((1, 0.95, 0.6)):
        r(f't{i}', m, y0 + hero * (0.47 + i * 0.1), sw * f, hero * 0.05, TEXT)
    bh = hero * 0.18
    r('btn', m, y0 + hero - bh, sw * 0.35, bh, L, bh / 2)
    r('bild', m + sw + g, y0, sw, hero, BILD)
    # Drei Karten
    fy = y0 + hero + g; fw = (W_ - 2 * m - 2 * g) / 3; p = max(g * 0.4, 4)
    for i in range(3):
        x = m + i * (fw + g)
        r(f'k{i}', x, fy, fw, feat, KARTE)
        cr = feat * 0.11; p = max(feat * 0.12, 4)
        o.append(f'<circle data-id="ki{i}" cx="{x + p + cr:.1f}" cy="{fy + feat * 0.22:.1f}" r="{cr:.1f}" fill="#c4c4c4" />')
        r(f'kh{i}', x + p, fy + feat * 0.44, fw * 0.55, feat * 0.1, TITEL)
        for j in range(2):
            r(f'kt{i}{j}', x + p, fy + feat * (0.62 + j * 0.13), (fw - 2 * p) * (1 if j == 0 else 0.7), feat * 0.06, '#aaaaaa')
    return '\n'.join(o) + '\n'

def fr(bu, inner, w=900, h=500, animate=True):
    a = '' if animate else ', "animate":false'
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":" + str(w) + ", \"h\":" + str(h) + a + ", \"bu\":\"" + bu + "\"}' %}\n" + inner + "{% endframe %}"

# ---------------------------------------------------------------- 010 Gedankenexperiment
W(D, '010-experiment.md', kopf('Gedankenexperiment', '''
**Mitmachen (ca. 2 Minuten).** Eine Startseite als Wireframe. Von Folie zu Folie wird der Weißraum kleiner. Die Elemente bleiben dieselben, sie wachsen nur in den Platz hinein, der frei wird. Das ist kein konstruiertes Beispiel: Genau so argumentieren Auftraggebende oft. »Da ist doch noch Platz, mach das Bild größer.«

Bei jeder Folie fragen: Was ist jetzt besser, was schlechter? Spätestens bei der dritten Fassung: Was ist verloren gegangen? Erwartbare Antworten: Man weiß nicht mehr, wo man anfangen soll. Alles ist gleich laut. Der Button geht unter, obwohl er größer ist. Die drei Karten kleben aneinander.

Dann zurück zur ersten Fassung. Erst der Vergleich zeigt, was der Weißraum geleistet hat: Er hat die Teile getrennt, die Reihenfolge vorgegeben und Ruhe geschaffen.
''', transition='none') + '''{% interlude "Was passiert, wenn der Weißraum verschwindet?", "Wir nehmen ihn Schritt für Schritt weg." %}

''' + '\n'.join([
  fr('Viel Weißraum', seite(80, 48)),
  fr('»Da ist doch noch Platz.«', seite(36, 22)),
  fr('Kein Platz mehr verschwendet. Was ist verloren gegangen?', seite(8, 6)),
  fr('Und zurück', seite(80, 48)),
]) + '\n')

# ---------------------------------------------------------------- 020 Regel
W(D, '020-regel.md', kopf('Weißraum', '''
Die Regel: Weißraum ist kein Rest, der übrig bleibt, wenn alles platziert ist. Er wird genauso gestaltet wie jedes Element. Weiß muss er übrigens nicht sein: Gemeint ist jede Fläche ohne Inhalt, auch eine farbige.

**Makro und Mikro:** Makro-Weißraum liegt zwischen den großen Blöcken: Rand, Abstände zwischen Abschnitten und Spalten. Er ordnet die Seite. Mikro-Weißraum liegt im Kleinen: Zeilenabstand, Abstand zwischen Absätzen, Innenabstand eines Buttons. Er macht Text lesbar und Elemente bedienbar.

**Hintergrund**

Im Englischen auch »negative space«. Wathan & Schoger (Refactoring UI, »Start with too much white space«) raten, mit zu viel Weißraum anzufangen und dann zu reduzieren: Wer mit zu wenig anfängt, gibt nur so viel dazu, bis es gerade nicht mehr stört. Das Zitat stammt von Armin Hofmann, Basler Grafiker und Lehrer, aus »Methodik der Form- und Bildgestaltung« (1965). Es stand schon im bisherigen Foliensatz. Die Interpunktion ist angepasst, Wortlaut und Seite bitte am Original prüfen.
''') + '''{% interlude "Leere ist gestalteter Raum.", "Nicht übrig gebliebener." %}
''')

W(D, '030-hofmann.md', '''
---
title: "Armin Hofmann"
layout: presentation.11ty.js
slideClasses: cite
author: Armin Hofmann, Grafiker
src: "Hofmann, A. (1965): Methodik der Form- und Bildgestaltung. Niggli, Teufen"
status: ok
speaker: |
  Hofmann (1920 bis 2020) hat an der Basler Schule für Gestaltung Generationen von Gestaltenden geprägt. Für ihn war der Zwischenraum kein Nebenprodukt, sondern gleichwertiger Teil der Gestaltung. Wortlaut und Seite bitte prüfen, die Interpunktion ist angepasst.
---

Die Beziehung positiv und negativ, eines der wichtigsten Gegensatzpaare bei allen Designs, entsteht automatisch. Ein Zwischenraum ist ebenso wichtig wie das Element, das ihn verursacht.
''')

# ---------------------------------------------------------------- 040 Gruppieren ohne Rahmen
def liste_wf(art):
    """Sechs Einträge in zwei Gruppen. art: 'linien' (jede Zeile mit Rahmen und Trennlinie) oder 'luft' (nur Weißraum)."""
    o = []; x = 270; w = 360
    y = 50
    for gi in range(2):
        if art == 'luft':
            o.append(f'<rect data-id="gh{gi}" x="{x}" y="{y}" width="140" height="16" fill="{TITEL}" />')
            y += 34
        else:
            o.append(f'<rect data-id="gh{gi}" x="{x}" y="{y}" width="140" height="16" fill="{TITEL}" />')
            y += 26
        for i in range(3):
            if art == 'linien':
                o.append(f'<rect x="{x - 12}" y="{y - 10}" width="{w + 24}" height="44" fill="none" stroke="#888888" stroke-width="2" />')
            o.append(f'<rect data-id="z{gi}{i}" x="{x}" y="{y}" width="{w * (0.9 if i != 1 else 0.7)}" height="10" fill="#aaaaaa" />')
            o.append(f'<rect data-id="zz{gi}{i}" x="{x}" y="{y + 16}" width="{w * 0.5}" height="8" fill="{TEXT}" />')
            y += 44 if art == 'linien' else 40
        y += 10 if art == 'linien' else 44
    return '\n'.join(o) + '\n'

W(D, '040-gruppieren.md', kopf('Weißraum gruppiert', '''
Zwei Gruppen mit je drei Einträgen, zum Beispiel Einstellungen in einer App. Links bekommt jede Zeile einen Rahmen. Das trennt alles von allem, die beiden Gruppen sind kaum noch zu erkennen. Rechts ist jeder Rahmen weg. Der Abstand zwischen den Gruppen ist größer als innerhalb, und schon sind die Gruppen klar.

Weißraum ist das leiseste Mittel, um zu gruppieren. Rahmen und Linien sind dann nur noch nötig, wenn der Platz fehlt (siehe Geschlossenheit und Region, Grenzen).
''', transition='none') + '''{% interlude "Weißraum gruppiert.", "Ohne einen einzigen Rahmen" %}

''' + fr('Jede Zeile gerahmt: Alles ist getrennt, nichts gehört zusammen', liste_wf('linien'), animate=False) + '\n' + fr('Nur Weißraum: zwei Gruppen, sofort erkennbar', liste_wf('luft'), animate=False) + '\n')

# ---------------------------------------------------------------- 050 Grenzen
W(D, '050-grenzen.md', kopf('Grenzen', '''
**Wertigkeit:** Viel Weißraum wird oft als hochwertig gelesen, wenig Weißraum als günstig und dringlich. Ein Prospekt vom Discounter und die Website einer Uhrenmarke zeigen den Unterschied sofort. Das ist eine gelernte Konvention, kein Naturgesetz, und sie kann gewollt sein: Ein Discounter, der aussieht wie eine Boutique, verunsichert seine Kundschaft (siehe Haltung Beobachten und Begründen, Netto-Prospekt).

**Zu viel:** Wenn alles weit auseinandersteht, zerfallen Zusammenhänge. Eine Beschriftung, die zu weit von ihrem Feld steht, gehört zu nichts mehr.

**Klein:** Auf dem Smartphone ist Weißraum teuer. Hier wird er nicht gestrichen, sondern umverteilt: weniger Rand, aber die Abstände zwischen den Gruppen bleiben deutlich größer als die innerhalb.
''') + liste('Wann trägt Weißraum nicht?', [
  'Wenn er zu groß wird: Dann gehört nichts mehr zusammen.',
  'Wenn er nicht zum Kontext passt: Viel Leere wirkt teuer, auch wo es günstig sein soll.',
  'Wenn er auf kleinen Screens überall gleich schrumpft: lieber umverteilen.',
]) + '''

{% statement "Verweise", "Dahinter: [Nähe und Abstand](../prinzip-naehe-und-abstand/) und [Geschlossenheit und Region](../prinzip-geschlossenheit-und-region/). Weiter: [Reduzieren](../prinzip-reduzieren/) und [Proportion](../prinzip-proportion/). Konstruieren: [Spacing-System](../methode-spacing-system/)." %}
''')

open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Weißraum"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Prinzip"
gruppe: "Dosieren"
tiefe: ""
einsatz: ""
kurzsatz: "Leere ist gestalteter Raum, nicht übrig gebliebener. Weißraum trennt, gruppiert und gibt die Reihenfolge vor"
begriffe: ["Weißraum", "Negativraum", "Makro-Weißraum", "Mikro-Weißraum"]
herkunft: "B: proportionen-und-abstaende/050"
inhalt:
  - "Gedankenexperiment: Weißraum wegnehmen"
  - "Leere ist gestalteter Raum (Hofmann)"
  - "Weißraum gruppiert ohne Rahmen"
  - "Grenzen: Wertigkeit, zu viel, kleine Screens"
status: ok
---
''')
print('fertig', D)
