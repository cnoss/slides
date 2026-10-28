exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'prinzip-hierarchie'

intro(D, 'Hierarchie', 'Prinzip // Gewichten')

# ---------------------------------------------------------------- Regel
W(D, '010-regel.md', '''
---
title: "Hierarchie"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Regel: Nicht alles ist gleich wichtig, und das muss man sehen. Eine Gestaltung ohne Hierarchie zwingt die Betrachtenden, selbst zu sortieren. Das kostet Wahrnehmungsarbeit und führt oft zum falschen Einstieg.

  Hierarchie ist das dritte Werkzeug aus der Wahrnehmungsarbeit: reduzieren, strukturieren, hierarchisieren. Erst wenn klar ist, was da ist und was zusammengehört, kann man entscheiden, in welcher Reihenfolge es gesehen werden soll.

  **Hintergrund**

  Adam Wathan und Steve Schoger überschreiben das Kapitel in »Refactoring UI« (2018) mit »Hierarchy is Everything«: Visuelle Hierarchie bestimmt, wie wichtig ein Element im Vergleich zu den anderen wirkt. Steve Krug fordert in »Don't Make Me Think« (3. Auflage 2014) eine klare visuelle Hierarchie, weil Menschen Seiten nicht lesen, sondern überfliegen. Abraham Moles beschreibt Hierarchisieren als einen Weg, die Kosten der Wahrnehmung zu senken.

  Mittel der Hierarchie sind die visuellen Variablen: Größe, Helligkeit und Kontrast, Farbe, Position, Weißraum. Siehe auch Räumlichkeit: Was größer, kontrastreicher und vorn ist, wirkt wichtiger.
---

{% interlude "Nicht alles ist gleich wichtig.", "Und das muss man sehen." %}
''')

# ---------------------------------------------------------------- Abstrakt
def kreise(spec):
    """spec: Liste von (cx, cy, r, fill)"""
    return '\n'.join(f'  <circle data-id="k{i}" cx="{cx}" cy="{cy}" r="{r}" fill="{f}" />' for i, (cx, cy, r, f) in enumerate(spec))

S, G1, G2, L = '#231f20', '#888888', '#d9d9d9', '#9313ce'
raster = [(150 + 100 * (i % 4), 150 + 100 * (i // 4)) for i in range(16)]

f1 = kreise([(300, 300, 40, S)])
f2 = kreise([(200, 300, 40, S), (400, 300, 40, S)])
f3 = kreise([(200, 300, 40, S), (400, 300, 40, G2)])
f4 = kreise([(x, y, 36, S) for x, y in raster])
f5 = kreise([(x, y, 36, S if i == 0 else G2) for i, (x, y) in enumerate(raster)])
f6 = kreise([(x, y, 56 if i == 0 else 36, S if i == 0 else (G1 if i in (1, 2, 3) else G2)) for i, (x, y) in enumerate(raster)])

W(D, '020-abstrakt.md', f'''
---
title: "Hierarchie abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Nach den Grafiken aus dem bisherigen Foliensatz (Wahrnehmungsarbeit). Bei jeder Folie fragen: Wo schauen Sie zuerst hin?

  Ein Element: keine Frage der Reihenfolge. Zwei gleiche: Der Blick pendelt, meist beginnt er links (Leserichtung). Tritt eins zurück, gibt es eine Reihenfolge. Sechzehn gleiche Elemente bieten keinen Einstieg, der Blick wandert. Wird eins betont und alle anderen treten zurück, ist der Einstieg klar. Mit drei Stufen entsteht eine Lesereihenfolge: erst das Große, dann die mittlere Stufe, dann der Rest.

  Wichtig: In der fünften Folie wurde kein Element lauter gemacht. Alle anderen wurden leiser.
---

{{% frame '{{"stage":"#ffffff","bu":"Ein Element"}}' %}}
{f1}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","bu":"Zwei gleiche: Wo fangen Sie an?"}}' %}}
{f2}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","bu":"Eins tritt zurück: Jetzt gibt es eine Reihenfolge"}}' %}}
{f3}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","bu":"Sechzehn gleiche: kein Einstieg"}}' %}}
{f4}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","bu":"Alle anderen treten zurück: ein Einstieg"}}' %}}
{f5}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","bu":"Drei Stufen: eine Lesereihenfolge"}}' %}}
{f6}
{{% endframe %}}
''')

# ---------------------------------------------------------------- Variiert: Headline und Copy
def textblock(h_h, h_fill, h_w, t_fill, t_y0, btn):
    out = [f'  <rect data-id="h0" x="150" y="100" width="{h_w}" height="{h_h}" fill="{h_fill}" />']
    for i in range(4):
        w = [600, 600, 600, 420][i]
        out.append(f'  <rect data-id="t{i}" x="150" y="{t_y0 + 30 * i}" width="{w}" height="14" fill="{t_fill}" />')
    out.append(btn)
    return '\n'.join(out)

btn_grau = '  <rect data-id="btn" x="150" y="300" width="160" height="14" rx="0" fill="#888888" />'
btn_lila = '  <rect data-id="btn" x="150" y="290" width="180" height="48" rx="24" fill="#9313ce" />'
v1 = textblock(14, G1, 600, G1, 130, btn_grau)
v2 = textblock(40, S, 480, G1, 170, btn_grau)
v3 = textblock(40, S, 480, G2, 170, btn_grau)
v4 = textblock(40, S, 480, G2, 170, btn_lila)

W(D, '030-variiert.md', f'''
---
title: "Headline und Text"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Nach der Headline-Copy-Demo aus dem bisherigen Foliensatz (Räumlichkeit), jetzt als Wireframe. Pro Folie ändert sich genau eine Sache.

  1. Alle Zeilen gleich: Headline, Text und Button sind nicht zu unterscheiden.
  2. Die Headline wird größer, dunkler und bekommt Abstand: Jetzt gibt es einen Einstieg.
  3. Der Text wird heller. Die Headline hat sich nicht verändert, wirkt aber noch stärker. Das ist Betonen durch Zurücknehmen.
  4. Der Button bekommt Form und Akzentfarbe: Die Handlung ist das Ziel der Seite.

  **Hintergrund**

  »Emphasize by de-emphasizing«: Wathan und Schoger raten in »Refactoring UI« (2018), Konkurrenz nicht durch immer lautere Hauptelemente zu lösen, sondern die Nebenelemente leiser zu machen. Wer alles lauter macht, landet wieder bei Folie 1, nur in groß.
---

{{% frame '{{"stage":"#ffffff","w":900,"h":500,"bu":"Alles gleich: Wo fangen Sie an?"}}' %}}
{v1}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","w":900,"h":500,"bu":"Die Headline wird größer"}}' %}}
{v2}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","w":900,"h":500,"bu":"Der Text tritt zurück"}}' %}}
{v3}
{{% endframe %}}
{{% frame '{{"stage":"#ffffff","w":900,"h":500,"bu":"Die Handlung bekommt die Akzentfarbe"}}' %}}
{v4}
{{% endframe %}}

{{% statement "Betonen durch Zurücknehmen.", "Oft ist es leichter, das Unwichtige leiser zu machen, als das Wichtige lauter." %}}
''')

# ---------------------------------------------------------------- Scanmuster
# F-Muster: textlastige Seite (Screen als Wireframe, darum graue Bühne mit Format)
f_seite = ['  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />',
           '  <rect data-id="h" x="60" y="90" width="520" height="28" fill="#888888" />']
for i in range(9):
    w = [780, 760, 780, 540, 780, 720, 780, 760, 480][i]
    y = 150 + 26 * i + (18 if i >= 4 else 0)
    f_seite.append(f'  <rect data-id="z{i}" x="60" y="{y}" width="{w}" height="10" fill="#d9d9d9" />')
f_seite = '\n'.join(f_seite)
f_pfad = ('  <path data-id="pfad" d="M 70 104 L 560 104 M 70 104 L 70 277 L 420 277 M 70 277 L 70 386" '
          'fill="none" stroke="#9313ce" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.85" />')

# Z-Muster: Einstiegsseite mit wenig Text
z_seite = '\n'.join([
    '  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />',
    '  <rect data-id="n1" x="560" y="42" width="60" height="8" fill="#d9d9d9" />',
    '  <rect data-id="n2" x="640" y="42" width="60" height="8" fill="#d9d9d9" />',
    '  <rect data-id="n3" x="720" y="42" width="60" height="8" fill="#d9d9d9" />',
    '  <rect data-id="bild" x="60" y="96" width="780" height="200" fill="#e4e4e4" />',
    '  <rect data-id="t1" x="60" y="330" width="420" height="12" fill="#d9d9d9" />',
    '  <rect data-id="t2" x="60" y="356" width="360" height="12" fill="#d9d9d9" />',
    '  <rect data-id="btn" x="660" y="330" width="180" height="48" rx="24" fill="#231f20" />',
])
z_pfad = ('  <path data-id="pfad" d="M 105 46 L 780 46 L 110 336 L 750 354" '
          'fill="none" stroke="#9313ce" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.85" />')

W(D, '040-scanmuster.md', f'''
---
title: "Scanmuster"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Menschen lesen Screens nicht, sie überfliegen sie. Dabei entstehen typische Blickmuster.

  **F-Muster:** bei textlastigen Seiten ohne klare Hierarchie. Erst eine Zeile ganz, dann eine kürzere, dann nur noch den linken Rand hinunter. Was rechts unten steht, sieht kaum jemand.

  **Z-Muster:** bei Seiten mit wenig Text, etwa Einstiegsseiten. Der Blick geht von links oben nach rechts oben, quer nach links unten und wieder nach rechts. Wichtige Punkte liegen auf dem Z: Logo, Navigation, Handlung rechts unten.

  Die Pointe: Das F-Muster ist kein Ziel, sondern ein Symptom. Es entsteht, wenn Hierarchie fehlt. Gute Hierarchie gibt dem Blick einen besseren Weg.

  **Hintergrund**

  Jakob Nielsen beschrieb das F-Muster 2006 nach Eyetracking-Studien der Nielsen Norman Group (»F-Shaped Pattern For Reading Web Content«). Kara Pernice hat die Studien 2017 aktualisiert: Das Muster gibt es weiterhin, vor allem wenn Text nicht gegliedert ist, Zwischenüberschriften, Hervorhebungen und kurze Absätze machen es schwächer. Das Z-Muster geht auf Leserichtung und das Gutenberg-Diagramm aus dem Zeitungsdesign zurück. Steve Krug, »Don't Make Me Think« (2014): »We don't read pages. We scan them.« (Jahreszahlen aus dem Gedächtnis, bitte prüfen.)
---

{{% statement "Wir lesen nicht, wir scannen.", "Der Blick springt über einen Screen und sucht nach Einstiegen. Hierarchie bestimmt, wo er landet." %}}

{{% frame '{{"w":900,"h":500,"bu":"Viel Text, wenig Hierarchie"}}' %}}
{f_seite}
{{% endframe %}}
{{% frame '{{"w":900,"h":500,"bu":"F-Muster: zwei Zeilen, dann nur noch der linke Rand"}}' %}}
{f_seite}
{f_pfad}
{{% endframe %}}
{{% frame '{{"w":900,"h":500,"bu":"Wenig Text, ein Bild, eine Handlung"}}' %}}
{z_seite}
{{% endframe %}}
{{% frame '{{"w":900,"h":500,"bu":"Z-Muster: oben quer, diagonal zurück, unten zur Handlung"}}' %}}
{z_seite}
{z_pfad}
{{% endframe %}}
''')

# ---------------------------------------------------------------- Im Screen
W(D, '050-im-screen.md', '''
---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **tagesschau.de (2026):** klare Hierarchie. Das große Bild zieht den Blick zuerst, dann die blaue Headline, dann der Teaser. Die Navigation ist klein und grau, sie ist da, drängt sich aber nicht vor. Das Logo oben links ist der Anker.

  **Wikipedia (2026):** sehr flache Hierarchie. Viele Kästen mit gleich gewichteten Überschriften, viel blauer Linktext in einer Größe. Das ist nicht falsch: Wikipedia ist ein Nachschlagewerk, die meisten kommen über die Suche oder direkt auf einen Artikel. Gute Diskussionsfrage: Für wen ist diese Startseite, und braucht sie mehr Hierarchie?

  Frage danach: Ihre meistgenutzte App öffnen. Was sehen Sie zuerst, was als Zweites, was als Drittes? Und war das so gemeint?
---

{% screenshot "./images/hierarchie-tagesschau.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Wie ist die Hierarchie der Elemente?<br><small>tagesschau.de, Screenshot 2026</small>"}' %}

{% screenshot "./images/hierarchie-wikipedia.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und hier? Für wen ist diese Seite gemacht?<br><small>de.wikipedia.org, Screenshot 2026</small>"}' %}

{% question "Öffnen Sie Ihre meistgenutzte App.", "Was sehen Sie zuerst, was als Zweites, was als Drittes? Und war das so gemeint?" %}
''')

# ---------------------------------------------------------------- Grenzen
W(D, '060-grenzen.md', '''
---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Hierarchie ist kein Selbstzweck. Sie muss dem folgen, was die Nutzenden an dieser Stelle wollen. Eine Startseite, die das Angebot des Monats groß macht, während fast alle nur den Login suchen, hat eine Hierarchie, aber die falsche.

  Zu viele Stufen ebnen ein: Mehr als drei oder vier Stufen kann kaum jemand auseinanderhalten. Und wenn alles groß ist, ist nichts groß (siehe Sparsam hervorheben).

  Manchmal ist flach richtig: Gleichwertiges soll gleich aussehen. Suchergebnisse, Tabellen, Produktlisten, Werkzeugleisten. Hier wäre eine künstliche Hierarchie eine Behauptung, die nicht stimmt.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt Hierarchie nicht?</h1>
    {% fragment '<p class="list">Wenn sie am Ziel der Nutzenden vorbeigeht: Sie ist da, aber falsch.</p>' %}
    {% fragment '<p class="list">Wenn es zu viele Stufen gibt: Mehr als drei oder vier sieht niemand.</p>' %}
    {% fragment '<p class="list">Wenn alles groß ist: Dann ist nichts groß.</p>' %}
    {% fragment '<p class="list">Und manchmal ist flach richtig: Gleichwertiges soll gleich aussehen.</p>' %}
  </div>
</section>
''')

# ---------------------------------------------------------------- Die dunkle Seite
def konto(kuendigen_ehrlich=False, ring=False):
    out = [
        '  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />',
        '  <rect data-id="n1" x="640" y="42" width="60" height="8" fill="#d9d9d9" />',
        '  <rect data-id="n2" x="720" y="42" width="60" height="8" fill="#d9d9d9" />',
        '  <rect data-id="kopf" x="60" y="96" width="260" height="26" fill="#888888" />',
        '  <rect data-id="karte" x="60" y="150" width="780" height="214" fill="#e4e4e4" />',
        '  <rect data-id="k1" x="90" y="180" width="220" height="14" fill="#888888" />',
        '  <rect data-id="k2" x="90" y="210" width="360" height="10" fill="#aaaaaa" />',
        '  <rect data-id="k3" x="90" y="232" width="300" height="10" fill="#aaaaaa" />',
        '  <rect data-id="upgrade" x="90" y="276" width="240" height="48" rx="24" fill="#9313ce" />',
        '  <line data-id="trenner" x1="60" y1="404" x2="840" y2="404" stroke="#d9d9d9" stroke-width="2" stroke-linecap="round" />',
        '  <rect data-id="f1" x="60" y="428" width="70" height="8" fill="#d9d9d9" />',
        '  <rect data-id="f2" x="150" y="428" width="84" height="8" fill="#d9d9d9" />',
    ]
    if kuendigen_ehrlich:
        out += [
            '  <rect data-id="kuendigen" x="350" y="276" width="200" height="48" rx="24" fill="#e4e4e4" stroke="#231f20" stroke-width="2" />',
            '  <rect data-id="f3" x="254" y="428" width="50" height="8" fill="#d9d9d9" />',
            '  <rect data-id="f4" x="324" y="428" width="64" height="8" fill="#d9d9d9" />',
        ]
    else:
        out += [
            '  <rect data-id="kuendigen" x="254" y="428" width="64" height="8" fill="#d9d9d9" />',
            '  <rect data-id="f3" x="338" y="428" width="50" height="8" fill="#d9d9d9" />',
            '  <rect data-id="f4" x="408" y="428" width="64" height="8" fill="#d9d9d9" />',
        ]
    if ring:
        out.append('  <ellipse data-id="ring" cx="286" cy="432" rx="58" ry="24" fill="none" stroke="#9313ce" stroke-width="4" />')
    return '\n'.join(out)

W(D, '070-dunkle-seite.md', f'''
---
title: "Die dunkle Seite"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Hierarchie entscheidet, was gesehen wird. Und damit auch, was nicht gesehen wird.

  Eine Kontoseite als Wireframe. Erst fragen: Wo kündigen Sie hier? Niemand findet es, und das ist der Punkt. Dann die Auflösung: Der Link »Kündigen« steht klein und hellgrau im Footer, zwischen Impressum, Datenschutz und AGB. Drei Prinzipien arbeiten zusammen gegen die Nutzenden:

  - **Hierarchie:** Das Upgrade ist das größte und einzige farbige Element, das Kündigen das kleinste und blasseste.
  - **Nähe:** Der Link steht in der Gruppe der Pflichtlinks, die niemand liest. Er gehört scheinbar zum Kleingedruckten, nicht zum Vertrag.
  - **Figur und Grund:** Mit so wenig Kontrast wird er nicht zur Figur, er verschwindet im Grund.

  Die ehrliche Variante: Kündigen steht dort, wo der Vertrag steht, als sekundärer Button. Das Upgrade bleibt die Hauptaktion, aber das Kündigen ist sichtbar und auffindbar.

  Verwandt: Hierarchie hebt auch die teure Option hervor. Das steht im Deck Kontrast und Hervorhebung (Lockangebot, Economist-Beispiel).

  **Hintergrund**

  Harry Brignull nennt das Muster »Roach Motel« bzw. »Hard to Cancel«: leicht hinein, schwer hinaus (»Deceptive Patterns«, 2023). In Deutschland gilt seit dem 1. Juli 2022 der Kündigungsbutton nach § 312k BGB: Wer online Verträge mit Dauerschuldverhältnis abschließen lässt, muss eine gut lesbare, ständig verfügbare und unmittelbar zugängliche Schaltfläche anbieten, beschriftet etwa mit »Verträge hier kündigen« (aus dem Gedächtnis, bitte prüfen). Gestaltung, die das Kündigen versteckt, ist also nicht nur unfair, sondern kann rechtswidrig sein.

  Prüffrage für jeden Entwurf: Wem nützt das?
---

{{% interlude "Die dunkle Seite", "Hierarchie entscheidet, was gesehen wird. Und was nicht." %}}

{{% frame '{{"w":900,"h":500,"bu":"Eine Kontoseite. Wo kündigen Sie hier?"}}' %}}
{konto()}
{{% endframe %}}
{{% frame '{{"w":900,"h":500,"bu":"Hier: klein, blass, zwischen den Pflichtlinks im Footer"}}' %}}
{konto(ring=True)}
{{% endframe %}}
{{% frame '{{"w":900,"h":500,"bu":"Ehrlich: Kündigen steht beim Vertrag, als zweite Aktion"}}' %}}
{konto(kuendigen_ehrlich=True)}
{{% endframe %}}

{{% question "Wem nützt diese Hierarchie?", "Den Nutzenden, die kündigen wollen? Oder dem Anbieter, der sie halten will?" %}}
''')

# ---------------------------------------------------------------- Verweise
W(D, '080-verweise.md', '''
---
title: "Verweise"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dahinter: Phänomen Pop-out. Weiter: Räumlichkeit, Kontrast und Hervorhebung, Nähe und Abstand, Figur und Grund. Prüfen mit der Methode Unschärfe- und Graustufentest.
---

{% statement "Verweise", "Dahinter: [Pop-out](../phaenomen-pop-out/). Weiter: [Räumlichkeit](../prinzip-raeumlichkeit/), [Kontrast und Hervorhebung](../prinzip-kontrast-und-hervorhebung/), [Nähe und Abstand](../prinzip-naehe-und-abstand/) und [Figur und Grund](../prinzip-figur-und-grund/). Prüfen: [Unschärfe- und Graustufentest](../methode-unschaerfetest/)." %}
''')

done(D, 'Nicht alles ist gleich wichtig, und das muss man sehen. Oft betont man am besten, indem man das Unwichtige zurücknimmt',
     ['Visuelle Hierarchie', 'Betonen durch Zurücknehmen', 'Scanmuster', 'F-Muster', 'Z-Muster'])
