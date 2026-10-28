# Bauskript für das Deck prinzip-gestaltpsychologie
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
d='prinzip-gestaltpsychologie'
B='#231f20'; L='#9313ce'

def frame(content, bu, w=600, h=600):
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":"+str(w)+", \"h\":"+str(h)+", \"bu\":\""+bu+"\"}' %}\n"+content+"\n{% endframe %}\n"

intro(d,'Gestaltpsychologie','Prinzip // Fundament')

W(d,'010-regel.md','''
---
title: "Prägnanz"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Regel hinter allen Gestaltgesetzen: Aus allen möglichen Lesarten eines Bildes wählt die Wahrnehmung die einfachste, regelmäßigste, symmetrischste. Das heißt Prägnanz oder Gesetz der guten Gestalt. Die Gesetze der Nähe, Ähnlichkeit, Geschlossenheit und Fortsetzung sind Spezialfälle davon.

  Das Koffka-Zitat wird oft falsch als »Das Ganze ist mehr als die Summe seiner Teile« wiedergegeben. Koffka hat ausdrücklich widersprochen: nicht mehr, sondern etwas anderes. Das Ganze hat eigene Eigenschaften, die in keinem Teil stecken.

  **Hintergrund**

  Die Gestaltpsychologie entstand ab 1912 mit Max Wertheimers Arbeit zur Scheinbewegung (siehe Phänomen Scheinbewegung und Zeit). Mit Wolfgang Köhler und Kurt Koffka bildete Wertheimer den Kern der Berliner Schule. Wertheimer formulierte die Gestaltgesetze 1923 in »Untersuchungen zur Lehre von der Gestalt II« (Psychologische Forschung 4). Koffka fasste sie 1935 in »Principles of Gestalt Psychology« zusammen, dort steht auch das Zitat (sinngemäß: »The whole is other than the sum of its parts«, aus dem Gedächtnis, bitte prüfen).

  Quellen im Modul: Yablonski, Laws of UX (Law of Prägnanz); Lidwell, Universal Principles of Design.

  Begriffe: Gestalt, Prägnanz, Gesetz der guten Gestalt, Gestaltgesetze, Erfahrung.
---

{% interlude "Wir sehen die einfachste mögliche Ordnung.", "Prägnanz, das Grundgesetz der Gestaltpsychologie" %}

{% statement "Das Ganze ist etwas anderes als die Summe seiner Teile.", "Kurt Koffka" %}
''')

# Zwei überlappende Kreise, Mittelpunkte (240,300) und (360,300), r 110. Schnittpunkte (300, 207.8) und (300, 392.2)
R=110; T='300,207.8'; U='300,392.2'
links  = f'M {T} A {R} {R} 0 1 0 {U} A {R} {R} 0 0 1 {T} Z'
linse  = f'M {T} A {R} {R} 0 0 0 {U} A {R} {R} 0 0 0 {T} Z'
rechts = f'M {T} A {R} {R} 0 1 1 {U} A {R} {R} 0 0 0 {T} Z'
kreise = f'''
<circle data-id="k1" cx="240" cy="300" r="{R}" fill="none" stroke="{B}" stroke-width="5" />
<circle data-id="k2" cx="360" cy="300" r="{R}" fill="none" stroke="{B}" stroke-width="5" />'''
teile = f'''
<path data-id="t1" d="{links}" fill="{B}" transform="translate(-50 0)" />
<path data-id="t2" d="{linse}" fill="{L}" />
<path data-id="t3" d="{rechts}" fill="{B}" transform="translate(50 0)" />'''

# Quadrat und gedrehtes Quadrat, Seite 240, Mitte (300,300)
quadrate = f'''
<rect data-id="q1" x="180" y="180" width="240" height="240" fill="none" stroke="{B}" stroke-width="5" stroke-linejoin="round" />
<polygon data-id="q2" points="300,130.3 469.7,300 300,469.7 130.3,300" fill="none" stroke="{B}" stroke-width="5" stroke-linejoin="round" />'''
dreiecke = [
  '300,130.3 349.7,180 250.3,180', '469.7,300 420,349.7 420,250.3', '300,469.7 250.3,420 349.7,420', '130.3,300 180,250.3 180,349.7',
  '180,180 250.3,180 180,250.3', '420,180 420,250.3 349.7,180', '420,420 349.7,420 420,349.7', '180,420 180,349.7 250.3,420']
stern = '\n'.join(f'<polygon data-id="d{i}" points="{p}" fill="{B}" />' for i,p in enumerate(dreiecke))

W(d,'020-abstrakt.md','''
---
title: "Gute Gestalt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Zweimal dasselbe Spiel. Erst fragen: Was sehen Sie? Fast alle sagen: zwei Kreise, die sich überlagern. Genauso gut könnten es drei Flächen sein, zwei Monde und eine Linse, die zufällig aneinanderstoßen. Diese Lesart wählt kaum jemand, weil zwei Kreise die einfachere Erklärung sind.

  Bei den Quadraten genauso: Zwei Quadrate, eines davon gedreht. Man könnte auch ein Achteck mit acht Dreiecken sehen oder einen Stern. Die zweite Fassung zeigt nur die Dreiecke: Jetzt sehen viele einen Stern, aber kaum jemand kommt von selbst darauf, wenn die Quadrate komplett sind.

  **Hintergrund**

  Die Beispiele folgen klassischen Abbildungen zum Gesetz der guten Gestalt (Wertheimer 1923) und sind dem bisherigen Foliensatz nachempfunden.
---

'''+frame(kreise,'Was sehen Sie?')
   +frame(teile,'Genauso möglich: drei Flächen. Sieht aber kaum jemand.')
   +frame(quadrate,'Und hier?')
   +frame(stern,'Acht Dreiecke um ein Achteck: genauso möglich. Wir sehen zwei Quadrate.'))

# Erfahrung: A als Umriss aus 12 Strecken, Strecke für Strecke
P = dict(a=(180,480), b=(270,120), c=(330,120), e=(420,480), f=(360,480), g=(340,400), h=(260,400), i=(240,480),
         j=(280,330), k=(320,330), l=(308,230), m=(292,230))
S = [('j','k'),('e','f'),('b','c'),('k','l'),('a','b'),('h','i'),('c','e'),('l','m'),('i','a'),('m','j'),('f','g'),('g','h')]
def seg(n):
    out=[]
    for idx,(p,q) in enumerate(S[:n]):
        (x1,y1),(x2,y2)=P[p],P[q]
        out.append(f'<line data-id="s{idx}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{B}" stroke-width="6" stroke-linecap="round" />')
    return '\n'.join(out)
schritte=[(2,'Ab wann erkennen Sie es?'),(4,'Ab wann erkennen Sie es?'),(6,'Und jetzt?'),(8,'Und jetzt?'),(10,'Und jetzt?'),(12,'Erkannt, lange bevor es vollständig war')]

W(d,'030-erfahrung.md','''
---
title: "Erfahrung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Live-Test (ca. 2 Minuten)**

  Eine Form entsteht Strecke für Strecke. Wer erkennt, was es wird, hebt die Hand, verrät es aber noch nicht. Die meisten erkennen das A ab der Hälfte der Strecken, manche noch früher.

  Pointe: Wir erkennen das A so früh, weil wir es tausendfach gesehen haben. Wer das lateinische Alphabet nicht kennt, erkennt es erst viel später oder gar nicht. Was »einfach« und »prägnant« ist, hängt also auch davon ab, was man kennt. Im Interface heißt das: Bekannte Formen, Icons und Muster werden schneller erkannt (siehe Konsistenz und Konventionen).

  **Hintergrund**

  Wertheimer nennt das den Faktor der Erfahrung oder Gewohnheit (1923). Er ist der schwächste und zugleich der kulturell abhängigste der Gestaltfaktoren. Die Abfolge ist dem bisherigen Foliensatz nachempfunden (Gesetz der Erfahrung).
---

'''+''.join(frame(seg(n),bu) for n,bu in schritte)+'''
{% statement "Erfahrung ist gelernt.", "Wer das lateinische Alphabet nicht kennt, erkennt das A erst viel später. Was einfach ist, hängt davon ab, was man kennt." %}
''')

W(d,'040-gesetze.md','''
---
title: "Die Gestaltgesetze"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Überblick über die Gestaltgesetze, die für Screendesign am meisten tragen. Alle beantworten dieselbe Frage: Was gehört zusammen? Im Interface ist das die Grundlage für jede Gruppierung: Karten, Formulare, Navigation, Listen.

  Nähe und Ähnlichkeit tragen am meisten. Gemeinsame Region (Stephen Palmer, 1992) und Verbundenheit (Palmer & Rock, 1994) sind spätere Ergänzungen, die im Interface besonders wichtig sind, weil Karten und Rahmen überall vorkommen.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Was gehört zusammen?</h1>
    {% fragment '<p class="list"><a href="../prinzip-naehe-und-abstand/">Nähe</a>: was nah beieinander steht</p>' %}
    {% fragment '<p class="list"><a href="../prinzip-aehnlichkeit/">Ähnlichkeit</a>: was gleich aussieht</p>' %}
    {% fragment '<p class="list"><a href="../prinzip-geschlossenheit-und-region/">Geschlossenheit und Region</a>: was eingefasst oder verbunden ist</p>' %}
    {% fragment '<p class="list"><a href="../prinzip-fortsetzung-und-schicksal/">Fortsetzung und Schicksal</a>: was auf einer Linie liegt oder sich gemeinsam bewegt</p>' %}
  </div>
</section>
''')

# Icons aus Grundformen
icons = f'''
<g data-id="i-haus" fill="none" stroke="{B}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><polyline points="110,190 160,145 210,190" /><polyline points="125,178 125,235 195,235 195,178" /></g>
<g data-id="i-suche" fill="none" stroke="{B}" stroke-width="8" stroke-linecap="round"><circle cx="292" cy="182" r="32" /><line x1="315" y1="205" x2="345" y2="235" /></g>
<g data-id="i-plus" fill="none" stroke="{B}" stroke-width="8" stroke-linecap="round"><line x1="440" y1="140" x2="440" y2="240" /><line x1="390" y1="190" x2="490" y2="190" /></g>
<g data-id="i-menu" fill="none" stroke="{B}" stroke-width="8" stroke-linecap="round"><line x1="110" y1="370" x2="210" y2="370" /><line x1="110" y1="400" x2="210" y2="400" /><line x1="110" y1="430" x2="210" y2="430" /></g>
<g data-id="i-x" fill="none" stroke="{B}" stroke-width="8" stroke-linecap="round"><line x1="255" y1="355" x2="335" y2="445" /><line x1="335" y1="355" x2="255" y2="445" /></g>
<g data-id="i-pfeil" fill="none" stroke="{L}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><line x1="395" y1="400" x2="490" y2="400" /><polyline points="455,365 490,400 455,435" /></g>'''

W(d,'050-im-screen.md','''
---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Icons sind angewandte Prägnanz: Haus, Lupe, Plus, Menü, Schließen, Pfeil. Wenige Grundformen, gleiche Strichstärke, symmetrisch oder einfach gerichtet. Sie werden auch klein und aus dem Augenwinkel erkannt. Dazu kommt Erfahrung: Das Hamburger-Menü war anfangs umstritten, heute erkennen es fast alle, weil sie es gelernt haben.

  Mini-Übung (ca. 3 Minuten): Handy entsperren, kurz auf den Homescreen schauen, wegsehen. Welche App-Icons erkennen Sie schon aus dem Augenwinkel? Welche nicht, und was haben die gemeinsam? Erwartbar: einfache, prägnante Formen und kräftige Farben werden schneller erkannt als detailreiche Icons oder Schriftzüge.
---

'''+frame(icons,'Sechs Icons aus Grundformen: auch klein und im Vorbeisehen erkannt')+'''
{% question "Welche App-Icons erkennen Sie aus dem Augenwinkel?", "Schauen Sie kurz auf Ihren Homescreen. Welche erkennen Sie sofort, welche nicht? Was haben sie gemeinsam?" %}
''')

W(d,'060-grenzen.md','''
---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Gestaltgesetze sind Beschreibungen, keine Naturgesetze. Sie sagen, was wir sehen, aber nicht, warum. Die heutige Wahrnehmungsforschung erklärt viele davon über Statistik: Das Gehirn bevorzugt die Lesart, die in der Welt am wahrscheinlichsten ist.

  Sie konkurrieren: Ähnlichkeit kann Nähe schlagen und umgekehrt, ein Rahmen schlägt beide. Wer gestaltet, entscheidet, welches Gesetz gewinnen soll, und sorgt dafür, dass alle in dieselbe Richtung zeigen.

  Und Erfahrung ist kulturell. Was für die einen einfach ist, ist für andere fremd.

  **Hintergrund**

  Zur Kritik: Die Gestaltgesetze wurden lange als rein beschreibend kritisiert. Johan Wagemans u. a. geben in »A century of Gestalt psychology in visual perception« (Psychological Bulletin, 2012) einen Überblick über den heutigen Stand (aus dem Gedächtnis, bitte prüfen).
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt das nicht?</h1>
    {% fragment '<p class="list">Gestaltgesetze beschreiben, was wir sehen. Warum, erklären sie nicht.</p>' %}
    {% fragment '<p class="list">Sie konkurrieren: Ähnlichkeit kann Nähe schlagen. Sie müssen entscheiden, welches gewinnt.</p>' %}
    {% fragment '<p class="list">Erfahrung ist kulturell: Was einfach ist, hängt davon ab, was man kennt.</p>' %}
  </div>
</section>
''')

W(d,'070-verweise.md','''
---
title: "Verweise"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dahinter: die Phänomene Scheinbewegung (der Beginn der Gestaltpsychologie) und Kippfiguren (dort auch Scheinkonturen nach Kanizsa). Weiter mit den einzelnen Gestaltgesetzen.
---

{% statement "Verweise", "Dahinter: [Scheinbewegung und Zeit](../phaenomen-scheinbewegung-und-zeit/) und [Kippfiguren](../phaenomen-kippfiguren/). Weiter: [Nähe und Abstand](../prinzip-naehe-und-abstand/), [Ähnlichkeit](../prinzip-aehnlichkeit/), [Geschlossenheit und Region](../prinzip-geschlossenheit-und-region/), [Fortsetzung und Schicksal](../prinzip-fortsetzung-und-schicksal/)." %}
''')

done(d,'Wir sehen die einfachste mögliche Ordnung: Das Ganze ist etwas anderes als die Summe seiner Teile',
     'Gestalt, Prägnanz, Gesetz der guten Gestalt, Gestaltgesetze, Erfahrung')
