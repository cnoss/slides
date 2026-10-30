# Bauskript prinzip-raeumlichkeit (zusammengeführt mit dem früheren Phänomen Tiefenstaffelung, 23.10.2026).
# Aufruf: python3 tools/sdvk/bau/prinzip-raeumlichkeit.py
# Die Screenshots images/ebenen-airbnb.jpg und images/ebenen-booking.jpg liegen im Deck (screenshots.js, 2026), das Skript bindet sie nur ein.
import glob, os
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D='prinzip-raeumlichkeit'
# Alte Folien des Decks entfernen, damit keine verwaisten Nummern stehen bleiben (index.md und images bleiben)
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
imgs(D,'raeumlichkeit',[f'playmobil-edit-0{i}.png' for i in range(1,6)]+['malaga-3619271_1920.jpg'])
intro(D,'Räumlichkeit','Prinzip // Gewichten')


W(D,'010-frage.md','''
---
title: "Was ist weiter weg?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Einstieg ohne Erklärung. Gleich kommen zwei Figuren. Bei jeder Folie fragen: Welche steht weiter hinten? Und wie weit? Mit der Hand zeigen lassen.
---

{% interlude "Was ist weiter weg?", "Zeigen Sie es mit der Hand." %}
''')

W(D,'020-playmobil.md','''
---
title: "Zwei Figuren"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Live (ca. 3 Minuten)**

  Bei jeder Folie fragen: Welche Figur steht weiter hinten? Wie weit? Von Folie zu Folie kommt genau ein Hinweis dazu:

  1. Zwei Figuren, gleich groß: Sie stehen nebeneinander.
  2. Die linke ist kleiner: Sie rückt nach hinten. Oder ist sie einfach ein Kind?
  3. Weniger Kontrast: Jetzt wirkt sie deutlich weiter weg.
  4. Weniger Sättigung: noch weiter.
  5. Überdeckung: Sie steht eindeutig hinter der rechten Figur.

  Die Pointe kommt erst bei der Auflösung: Keine der Figuren hat sich bewegt. Es sind Bildbearbeitungen derselben Aufnahme.

  Fotos: eigene Aufnahmen aus dem bisherigen Foliensatz Räumlichkeit.
---

{% screenshot "./images/playmobil-edit-01.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Welche Figur steht weiter hinten?"}' %}
{% screenshot "./images/playmobil-edit-02.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Und jetzt?"}' %}
{% screenshot "./images/playmobil-edit-03.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Und jetzt?"}' %}
{% screenshot "./images/playmobil-edit-04.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Und jetzt?"}' %}
{% screenshot "./images/playmobil-edit-05.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Und jetzt?"}' %}
''')

W(D,'030-malaga.md','''
---
title: "Málaga"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Blick über Málaga. Fragen: Was ist nah, was ist fern? Woran sehen Sie das? Erwartbare Antworten: Die Häuser hinten sind kleiner, blasser, bläulicher, sie liegen höher im Bild, sie werden von den vorderen verdeckt, und die Dächer werden zum Horizont hin immer dichter.

  Die Berge im Hintergrund sind fast nur noch eine graublaue Fläche: Luftperspektive.

  Foto: Barbara Iandolo, Pixabay (Pixabay-Lizenz), aus dem bisherigen Foliensatz Räumlichkeit.
---

{% screenshotFs "./images/malaga-3619271_1920.jpg", '{"transition":"fade", "bu":"Was ist nah, was ist fern? Woran sehen Sie das?", "credit":"Foto: Barbara Iandolo, Pixabay"}' %}
''')

W(D,'040-aufloesung.md','''
---
title: "Auflösung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Figuren haben sich nicht bewegt. Es ist dieselbe Aufnahme, nur bearbeitet: verkleinert, Kontrast und Sättigung zurückgenommen, hinter die andere Figur geschoben. Und auch Málaga ist eine flache Fläche aus Pixeln. Tiefe steht nicht im Bild, wir lesen sie hinein.

  Das funktioniert so zuverlässig, dass wir es kaum abschalten können. Gestaltung nutzt genau das, auf jedem Screen.

  **Mechanismus:** Die Netzhaut ist eine Fläche. Räumliches Sehen ist eine Leistung des Gehirns, und es nutzt dafür viele Hinweise gleichzeitig. Ein Teil braucht zwei Augen (Querdisparation), ein großer Teil funktioniert mit einem Auge und auf jedem flachen Bild: die monokularen oder bildhaften Tiefenhinweise. Genau die stehen uns auf dem Screen zur Verfügung.

  **Hintergrund**

  - **Relative Größe:** Von zwei gleichen Dingen wirkt das kleinere weiter weg.
  - **Luftperspektive:** Die Luft streut Licht. Ferne Dinge werden heller, kontrastärmer, weniger gesättigt und bläulich. Leonardo da Vinci hat das in seinen Notizen zur Malerei beschrieben (»prospettiva aerea«, um 1500, später zusammengestellt im »Trattato della pittura«) und in seinen Bildhintergründen eingesetzt.
  - **Verdeckung:** Was etwas anderes verdeckt, liegt davor. Der stärkste und eindeutigste Hinweis.
  - **Höhe im Bild:** Was näher am Horizont liegt, wirkt weiter weg.
  - **Texturgradient:** Gleichmäßige Strukturen werden mit der Entfernung feiner und dichter. Beschrieben von James J. Gibson, »The Perception of the Visual World« (1950).

  Zum Nachlesen: E. Bruce Goldstein, Wahrnehmungspsychologie (Kapitel Tiefenwahrnehmung).
---

{% statement "Keine Figur hat sich bewegt.", "Das Bild ist flach. Die Tiefe lesen wir aus Hinweisen hinein." %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Was weiter weg ist, wirkt</h1>
    {% fragment '<p class="list"><strong>kleiner</strong></p>' %}
    {% fragment '<p class="list"><strong>kontrastärmer</strong> und <strong>blasser</strong></p>' %}
    {% fragment '<p class="list"><strong>verdeckt</strong> von dem, was davor liegt</p>' %}
    {% fragment '<p class="list"><strong>höher im Bild</strong>, näher am Horizont</p>' %}
    {% fragment '<p class="list"><strong>dichter</strong> in seiner Struktur</p>' %}
  </div>
</section>
''')

W(D,'050-regel.md','''
---
title: "Räumlichkeit"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Regel: Wir lesen Tiefe als Rangfolge. Was näher wirkt, wird zuerst gesehen und für wichtiger gehalten. Die Mittel kennen Sie aus der Playmobil-Sequenz: Größe, Kontrast, Sättigung, Überdeckung. Dazu kommen auf dem Screen Licht und Schatten.

  **Hintergrund**

  Die Tiefenhinweise stammen aus der Wahrnehmungspsychologie (monokulare Tiefenhinweise, siehe Auflösung am Anfang des Decks). Dass Nähe Bedeutung trägt, ist alt: In der mittelalterlichen Malerei wurden wichtige Figuren größer dargestellt als unwichtige (Bedeutungsperspektive). Im Interface sprechen Wathan und Schoger in »Refactoring UI« von »Creating Depth«, Material Design von »Elevation«.
---

{% interlude "Was näher wirkt, wirkt wichtiger.", "Wir lesen Tiefe als Rangfolge." %}
''')

def sq(a, b, order='ab'):
    A=f'  <rect data-id="a" x="{a[0]}" y="{a[1]}" width="{a[2]}" height="{a[2]}" fill="{a[3]}" />\n'
    B=f'  <rect data-id="b" x="{b[0]}" y="{b[1]}" width="{b[2]}" height="{b[2]}" fill="{b[3]}" />\n'
    return A+B if order=='ab' else B+A
K='#231f20'
steps=[
 ('Zwei gleiche Quadrate: gleich weit weg, gleich wichtig', sq((110,220,160,K),(330,220,160,K))),
 ('Größe: Das kleinere rückt nach hinten', sq((110,220,160,K),(355,245,110,K))),
 ('Kontrast: noch weiter', sq((110,220,160,K),(355,245,110,'#d9d9d9'))),
 ('Sättigung: Das gesättigte kommt nach vorn', sq((110,220,160,'#9313ce'),(355,245,110,'#d9d9d9'))),
 ('Überdeckung: Jetzt ist eindeutig, was vorn liegt', sq((150,240,160,'#9313ce'),(255,180,110,'#d9d9d9'),order='ba')),
]
frames='\n'.join(f'{{% frame \'{{"stage":"#ffffff","bu":"{bu}"}}\' %}}\n{svg}{{% endframe %}}' for bu,svg in steps)
W(D,'060-abstrakt.md',f'''
---
title: "Tiefe abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Zwei gleiche Quadrate. Von Folie zu Folie kommt genau ein Tiefenhinweis dazu, das rechte rückt Schritt für Schritt nach hinten, das linke nach vorn. Fragen bei jedem Schritt: Welches ist wichtiger? Welches sehen Sie zuerst?

  Die Reihenfolge entspricht der Playmobil-Sequenz vom Anfang: Größe, Kontrast, Sättigung, Überdeckung. Die Hinweise addieren sich. Je mehr in dieselbe Richtung zeigen, desto eindeutiger die Rangfolge.

  Sättigung: Gesättigte, warme Farben wirken näher als ungesättigte, kühle. Deshalb trägt hier die Akzentfarbe.
---

{frames}
''')

# Elevation abstrakt
DEFS='<defs><filter id="ev1" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#231f20" flood-opacity="0.22"/></filter><filter id="ev2" x="-40%" y="-40%" width="180%" height="200%"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#231f20" flood-opacity="0.28"/></filter></defs>'
def cards(e1=False, e2=False):
    f1=' filter="url(#ev1)"' if e1 else ''
    f2=' filter="url(#ev2)"' if e2 else ''
    y2=200 if e2 else 220
    return f'''  {DEFS}
  <rect data-id="c0" x="90" y="160" width="200" height="200" fill="#0f6b75" />
  <rect data-id="c1" x="350" y="160" width="200" height="200" fill="#0f6b75"{f1} />
  <rect data-id="c2" x="610" y="{y2-60}" width="200" height="200" fill="#0f6b75"{f2} />
'''
W(D,'070-licht-und-schatten.md',f'''
---
title: "Licht und Schatten"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Auf dem Screen kommt ein Mittel dazu, das in der Natur selbstverständlich ist: Was über einer Fläche schwebt, wirft einen Schatten. Ein kleiner, scharfer Schatten heißt »liegt knapp darüber«, ein großer, weicher Schatten heißt »schwebt weit darüber«. Der Schatten fällt nach unten, weil wir Licht von oben erwarten.

  In allen anderen Grafiken dieses Moduls gibt es keine Schatten. Hier ist es die Ausnahme, weil das Prinzip selbst davon handelt.

  **Hintergrund**

  Wathan & Schoger, Refactoring UI, Kapitel »Creating Depth«: Licht kommt von oben, Schatten zeigen die Höhe eines Elements, wenige feste Stufen statt beliebiger Werte. Material Design nennt das Elevation und arbeitet mit einer festen Skala von Höhenstufen. Dass wir Licht von oben annehmen, zeigen Studien zur Wahrnehmung von Form aus Schattierung (Ramachandran, 1988, aus dem Gedächtnis, bitte prüfen).
---

{{% statement "Schatten zeigen Höhe.", "Ein kleiner Schatten: liegt knapp darüber. Ein großer: schwebt weit darüber." %}}

{{% frame '{{"stage":"#ffffff","w":900,"h":500,"bu":"Drei Flächen auf einer Ebene"}}' %}}
{cards()}{{% endframe %}}
{{% frame '{{"stage":"#ffffff","w":900,"h":500,"bu":"Ein kleiner Schatten: Die mittlere hebt sich ab"}}' %}}
{cards(True)}{{% endframe %}}
{{% frame '{{"stage":"#ffffff","w":900,"h":500,"bu":"Ein großer Schatten: Die rechte schwebt darüber"}}' %}}
{cards(True,True)}{{% endframe %}}
''')

# Wireframe: Seite, dann Dialog, dann Dialog mit abgedunkeltem Hintergrund
page_d='''
  <rect data-id="bild" x="40" y="60" width="370" height="200" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="292" width="250" height="22" fill="#888888" />
  <rect data-id="t1" x="40" y="336" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="40" y="360" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="40" y="384" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="k1" x="40" y="430" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="450" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k1t1" x="190" y="460" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="190" y="490" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="600" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="620" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k2t1" x="190" y="630" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="190" y="660" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="btn" x="40" y="780" width="160" height="44" rx="22" fill="#231f20" />
'''
dialog='''
  <rect data-id="dlg" x="45" y="310" width="360" height="290" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="dh" x="75" y="345" width="200" height="20" fill="#888888" />
  <rect data-id="dt1" x="75" y="387" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="dt2" x="75" y="411" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="dt3" x="75" y="435" width="200" height="12" fill="#d9d9d9" />
  <rect data-id="db1" x="75" y="490" width="140" height="44" rx="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="db2" x="235" y="490" width="140" height="44" rx="22" fill="#9313ce" />
'''
scrim='  <rect data-id="scrim" x="0" y="0" width="450" height="900" fill="#231f20" fill-opacity="0.55" />\n'
# Wireframe: Seite, Button schwebt, Bottom Sheet
page='''  <rect data-id="bild" x="40" y="60" width="370" height="180" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="272" width="250" height="22" fill="#888888" />
  <rect data-id="k1" x="40" y="320" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="340" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k1t1" x="180" y="350" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="180" y="378" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="480" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="500" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k2t1" x="180" y="510" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="180" y="538" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k3" x="40" y="640" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k3b" x="60" y="660" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k3t1" x="180" y="670" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k3t2" x="180" y="698" width="150" height="10" fill="#aaaaaa" />
'''
fab='  <circle data-id="fab" cx="360" cy="810" r="32" fill="#9313ce" filter="url(#ev1)" />\n'
sheet='''  <path data-id="sheet" d="M0 920 L0 560 Q0 540 20 540 L430 540 Q450 540 450 560 L450 920 Z" fill="#ffffff" filter="url(#ev2s)" />
  <line data-id="griff" x1="200" y1="562" x2="250" y2="562" stroke="#d9d9d9" stroke-width="6" stroke-linecap="round" />
  <rect data-id="sh" x="40" y="600" width="220" height="22" fill="#888888" />
  <rect data-id="st1" x="40" y="644" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="st2" x="40" y="668" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="sbtn" x="40" y="712" width="370" height="48" rx="24" fill="#231f20" />
'''
DEFS2='<defs><filter id="ev1" x="-40%" y="-40%" width="180%" height="190%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#231f20" flood-opacity="0.3"/></filter><filter id="ev2s" x="-10%" y="-20%" width="120%" height="140%"><feDropShadow dx="0" dy="-6" stdDeviation="14" flood-color="#231f20" flood-opacity="0.3"/></filter></defs>'
W(D,'080-im-screen.md',f'''
---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Dialog:** Ein Screen als Wireframe. Grau: Bild und Text, hellgraue Flächen: Karten, Schwarz: ein Button. Lila: die Hauptaktion im Dialog. Dann öffnet sich ein Dialog. Ohne weitere Hinweise liegt er auf derselben Ebene wie die Seite, man muss erst sortieren, was dazugehört. Mit abgedunkeltem Hintergrund ist sofort klar, was vorn ist: Die Seite verliert Kontrast und rückt optisch nach hinten, der Dialog wird zur einzigen Figur. Luftperspektive auf dem Screen. Frage: Was hat sich zwischen der zweiten und der dritten Folie geändert? Nur der Hintergrund. Im Interface heißt die abdunkelnde Fläche »Scrim« (Material Design) oder Backdrop (CSS: ::backdrop beim Element dialog).

  **Ebenen:** Ein Screen mit drei Ebenen. Ganz hinten die Seite mit ihren Karten. Darüber ein schwebender Button (in Material Design: Floating Action Button) mit kleinem Schatten: Er bleibt beim Scrollen stehen und gehört nicht zum Inhalt. Ganz vorn ein Bottom Sheet mit großem Schatten nach oben: Es verdeckt die Seite und verlangt Aufmerksamkeit. Die Höhe sagt, wie wichtig und wie vorübergehend etwas ist. Je höher, desto eher erwartet man, dass es wieder verschwindet.

  **Echte Beispiele:** Airbnb (2026): Das Suchfeld schwebt mit Schatten über der Seite, die Karten liegen flach. Booking.com (2026): Seite abgedunkelt, Suchleiste, darüber der Dialog. Fragen: Welche Ebenen erkennen Sie? Woran?
---

{{% frame '{{"w":450,"h":900,"bu":"Eine Seite"}}' %}}{page_d}{{% endframe %}}
{{% frame '{{"w":450,"h":900,"bu":"Ein Dialog öffnet sich. Was liegt vorn?"}}' %}}{page_d}{dialog}{{% endframe %}}
{{% frame '{{"w":450,"h":900,"bu":"Hintergrund abgedunkelt: Die Seite rückt nach hinten"}}' %}}{page_d}{scrim}{dialog}{{% endframe %}}

{{% frame '{{"w":450,"h":900,"animate":false,"bu":"Ebene 0: die Seite"}}' %}}
  {DEFS2}
{page}{{% endframe %}}
{{% frame '{{"w":450,"h":900,"bu":"Ebene 1: Ein Button schwebt darüber"}}' %}}
  {DEFS2}
{page}{fab}{{% endframe %}}
{{% frame '{{"w":450,"h":900,"bu":"Ebene 2: Ein Bottom Sheet schiebt sich nach vorn"}}' %}}
  {DEFS2}
{page}{fab}{sheet}{{% endframe %}}

{{% screenshot "./images/ebenen-airbnb.jpg", '{{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Das Suchfeld schwebt, die Karten liegen flach<br><small>airbnb.de, Screenshot 2026</small>"}}' %}}
{{% screenshot "./images/ebenen-booking.jpg", '{{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Wie viele Ebenen sehen Sie? Woran erkennen Sie sie?<br><small>booking.com, Screenshot 2026</small>"}}' %}}

{{% question "Welche Ebenen hat Ihre meistgenutzte App?", "Was liegt ganz hinten, was ganz vorn? Und woran erkennen Sie das?" %}}
''')

W(D,'090-grenzen.md','''
---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Zu viele Ebenen:** Wenn jede Karte, jeder Button und jede Leiste einen eigenen Schatten hat, gibt es keine Rangfolge mehr, nur Unruhe. Wenige feste Stufen, die meisten Elemente flach.

  **Flat Design:** Mit iOS 7 (2013) und Microsofts Metro-Stil wurden Schatten und Glanz fast vollständig entfernt. Das Ergebnis war ruhiger, aber es gingen Hinweise verloren, was man anklicken kann und was davor liegt. Die Nielsen Norman Group hat das später als Problem der Bedienbarkeit beschrieben (»Flat UI Elements Attract Less Attention and Cause Uncertainty«, 2017, aus dem Gedächtnis, bitte prüfen). Heute sind die meisten Systeme wieder »fast flach«: wenig Schatten, aber gezielt.

  **Schatten allein trägt nicht:** Auf dunklem Grund oder bei schwachem Kontrast sind Schatten kaum zu sehen. Im Dark Mode arbeitet Material Design deshalb mit helleren Flächen statt mit Schatten: Was höher liegt, ist heller (tonal elevation, Material 3). Und wer schlecht sieht, sieht den Schatten nicht. Die Fläche selbst muss sich ausreichend abheben.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt Räumlichkeit nicht?</h1>
    {% fragment '<p class="list">Wenn alles schwebt: Dann gibt es keine Rangfolge mehr, nur Unruhe.</p>' %}
    {% fragment '<p class="list">Wenn alles flach ist: Dann fehlt der Hinweis, was vorn liegt und was man bedienen kann.</p>' %}
    {% fragment '<p class="list">Wenn nur der Schatten trennt: Auf dunklem Grund und bei schwachem Kontrast verschwindet er.</p>' %}
  </div>
</section>
''')

W(D,'100-verweise.md','''
---
title: "Verweise"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dahinter: Kippfiguren (Figur und Grund). Weiter: Hierarchie, Figur und Grund. Prüfen: Unschärfe- und Graustufentest. Im Graustufentest sieht man sofort, ob die Ebenen auch ohne Farbe getrennt sind.
---

{% statement "Verweise", "Dahinter: [Kippfiguren](../phaenomen-kippfiguren/). Weiter: [Hierarchie](../prinzip-hierarchie/) und [Figur und Grund](../prinzip-figur-und-grund/). Prüfen mit dem [Unschärfe- und Graustufentest](../methode-unschaerfetest/)." %}
''')

W(D,'index.md','''
---
title: "Räumlichkeit"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Prinzip"
gruppe: "Gewichten"
tiefe: ""
einsatz: ""
kurzsatz: "Was näher wirkt, wirkt wichtiger. Tiefe lesen wir aus flachen Hinweisen: Größe, Kontrast, Sättigung, Überdeckung und Schatten"
begriffe: ["Räumlichkeit", "Tiefenhinweis", "Luftperspektive", "Überdeckung", "Elevation"]
herkunft: "U: raeumlichkeit (mit dem früheren Phänomen Tiefenstaffelung, raeumlichkeit/010, 020)"
inhalt:
  - "Tiefenstaffelung, Luftperspektive (Playmobil, Málaga)"
  - "Räumlichkeit als Hierarchie"
  - "Tiefe durch Licht und Schatten"
status: ok
---
''')
