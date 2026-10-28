# Bauskript phaenomen-pop-out. Aufruf: python3 tools/sdvk/bau/phaenomen-pop-out.py
# Erzeugt auch die Testbilder (SVG) in images/.
import random
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/blitz.py').read())
D='phaenomen-pop-out'
os.makedirs(f'{NEW}/{D}/images', exist_ok=True)
L='#9313ce'; G='#888888'

def suchbild(name, seite, konjunktion, seed):
    rnd=random.Random(seed)
    cols, rows = 12, 6
    cells=[(c,r) for c in range(cols) for r in range(rows)]
    rnd.shuffle(cells)
    cells=cells[:44]
    half=[x for x in cells if (x[0]<cols//2)==(seite=='links')]
    ziel=half[0]
    out=[]
    for (c,r) in cells:
        cx=110+c*125+rnd.randint(-28,28); cy=110+r*136+rnd.randint(-26,26)
        if (c,r)==ziel:
            out.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="{L}"/>')
        elif konjunktion and rnd.random()<0.5:
            out.append(f'<rect x="{cx-22}" y="{cy-22}" width="44" height="44" fill="{L}"/>')
        else:
            out.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="{G}"/>')
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900"><rect width="1600" height="900" fill="#ffffff"/>'+''.join(out)+'</svg>'
    open(f'{NEW}/{D}/images/{name}.svg','w').write(svg)

suchbild('suche-a1','rechts',False,11)
suchbild('suche-a2','links',False,12)
suchbild('suche-b1','links',True,21)
suchbild('suche-b2','rechts',True,22)

intro(D,'Pop-out','Phänomen')

frage='Links oder rechts? Zeigen Sie sofort in die Richtung.'
W(D,'010-aufgabe.md',f'''
---
title: "Finden Sie den lila Kreis"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 4 Minuten)**

  Vier Suchbilder, jedes blitzt beim Weiterschalten nur 250 Millisekunden auf. Vorher ansagen: Es geht sehr schnell, und gleich danach zeigen alle mit dem Arm, auf welcher Seite der lila Kreis war.

  Durchgang 1 und 2: Der lila Kreis ist der einzige lila Gegenstand zwischen grauen Kreisen. Fast alle zeigen richtig, obwohl die Zeit kaum zum Hinschauen reicht. Lösung: 1 rechts, 2 links.

  Durchgang 3 und 4: Jetzt gibt es auch lila Quadrate. Der lila Kreis unterscheidet sich von den grauen Kreisen nur durch die Farbe und von den lila Quadraten nur durch die Form. Die Arme zeigen in alle Richtungen, viele zögern. Lösung: 3 links, 4 rechts.

  Danach beide Fassungen in Ruhe zeigen. Im zweiten Bild muss man auch mit Zeit suchen.

  Technik: Der Blitz ist ein Fragment. Zurück und wieder vor wiederholt ihn. Die Suchbilder erzeugt das Bauskript (zufällig, aber fest).
---

{{% statement "Finden Sie den lila Kreis.", "Er blitzt nur einen Augenblick auf. Zeigen Sie danach sofort: links oder rechts?" %}}

{blitz('./images/suche-a1.svg','Durchgang 1',frage,'250ms','Suchbild mit Kreisen',css=True)}
{blitz('./images/suche-a2.svg','Durchgang 2',frage,'250ms','Suchbild mit Kreisen')}
{{% statement "Noch einmal.", "Gleiche Aufgabe: Finden Sie den lila Kreis." %}}

{blitz('./images/suche-b1.svg','Durchgang 3',frage,'250ms','Suchbild mit Kreisen und Quadraten')}
{blitz('./images/suche-b2.svg','Durchgang 4',frage,'250ms','Suchbild mit Kreisen und Quadraten')}
{{% screenshot "./images/suche-a1.svg", '{{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Und jetzt in Ruhe: Durchgang 1"}}' %}}
{{% screenshot "./images/suche-b1.svg", '{{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Durchgang 3: Sie müssen suchen, auch mit Zeit"}}' %}}
''')

W(D,'020-aufloesung.md','''
---
title: "Auflösung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Im ersten Bild war der Kreis da, bevor Sie gesucht haben. Er unterscheidet sich in einem einzigen Merkmal, der Farbe, von allem anderen. Im zweiten Bild unterscheidet er sich nur in der Kombination aus Farbe und Form. Dafür muss man Element für Element prüfen.

  Begriffe: Pop-out, präattentive Wahrnehmung, Merkmalssuche, Konjunktionssuche.
---

{% interlude "Ein Merkmal springt ins Auge.", "Eine Kombination muss man suchen." %}
''')

W(D,'030-mechanismus.md','''
---
title: "Mechanismus"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Ein Teil der Verarbeitung läuft parallel über das ganze Gesichtsfeld, bevor die Aufmerksamkeit irgendwohin gelenkt wird: präattentiv. Einfache Merkmale wie Farbe, Größe, Ausrichtung und Bewegung werden dort schon erfasst. Weicht ein Element in genau einem solchen Merkmal ab, springt es heraus, egal wie viele andere Elemente da sind.

  Eine Kombination von Merkmalen erkennt erst die Aufmerksamkeit, und die arbeitet nacheinander. Deshalb wächst die Suchzeit mit jedem zusätzlichen Element.

  Welche Merkmale das sind, zeigt das Prinzip Kontrast und Hervorhebung Folie für Folie.

  **Hintergrund**

  Anne Treisman und Garry Gelade, »A feature-integration theory of attention«, Cognitive Psychology 12, 1980. Merkmalsintegrationstheorie: Merkmale werden parallel registriert, ihre Verknüpfung zu einem Objekt braucht serielle Aufmerksamkeit. In ihren Versuchen blieb die Suchzeit bei Merkmalssuche fast gleich, bei Konjunktionssuche stieg sie mit der Zahl der Elemente linear an.

  Colin Ware, »Visual Thinking for Information Design« (2. Auflage 2021), nennt als präattentiv u. a. Farbe, Größe, Ausrichtung, Bewegung, Krümmung und Hinzufügungen (z. B. ein Rahmen). Form wirkt nur teilweise: Ein Kreis zwischen Quadraten springt weniger stark heraus als eine abweichende Farbe.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Was sofort ins Auge springt</h1>
    {% fragment '<p class="list"><strong>Farbe</strong></p>' %}
    {% fragment '<p class="list"><strong>Größe</strong></p>' %}
    {% fragment '<p class="list"><strong>Ausrichtung</strong></p>' %}
    {% fragment '<p class="list"><strong>Bewegung</strong></p>' %}
    {% fragment '<p class="list"><strong>Form</strong>, aber schwächer</p>' %}
  </div>
</section>

{% statement "Ein Merkmal: sofort, egal wie viele.", "Eine Kombination: Element für Element. Je mehr Elemente, desto länger dauert es." %}
''')

worte=['Tisch','Lampe','Fenster','Teppich','Regal','Kissen','Spiegel','Sessel','Vorhang','Schrank']
def liste(akzent=True):
    return ''.join(f'<div style="margin:0;padding:0.15em 0;{"color:"+L+";font-weight:700;" if (w=="Spiegel" and akzent) else ""}">{w}</div>' for w in worte)
W(D,'040-von-restorff.md',f'''
---
title: "Das Andere bleibt hängen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 3 Minuten)**

  Die Liste erscheint beim Weiterschalten für fünf Sekunden und verschwindet von selbst. Danach 30 Sekunden: Alle schreiben auf, welche Wörter sie noch wissen. Dann per Handzeichen abfragen, Wort für Wort. Meist nennen die meisten das lila Wort »Spiegel«, obwohl es mitten in der Liste steht. Häufig sind auch das erste und das letzte Wort dabei (Serial-Position-Effekt).

  Eine Demo im Hörsaal ist kein Experiment: kleine Gruppe, alle sehen die Pointe kommen. Aber der Effekt ist robust und gut belegt.

  **Hintergrund**

  Hedwig von Restorff, »Über die Wirkung von Bereichsbildungen im Spurenfeld«, Psychologische Forschung 18, 1933, entstanden am Berliner Psychologischen Institut im Umfeld von Wolfgang Köhler, also mitten in der Gestaltpsychologie. Ein Element, das sich von den anderen abhebt, wird besser erinnert (Isolationseffekt). Yablonski, Laws of UX: »Von Restorff Effect«.
---

<section class="simple" data-transition="none">
  <div>
    <h1>Merken Sie sich so viele Wörter wie möglich.</h1>
    <p>Sie haben fünf Sekunden.</p>
    <div class="fragment wortliste" style="--dauer:5s;"><div style="display:block;width:8em !important;hyphens:none;white-space:nowrap;margin:0;padding:0;font-size:4vh;line-height:1.25;text-align:left;">{liste()}</div></div>
    <style>
.reveal .slides section .fragment.wortliste{{opacity:0;visibility:inherit;transition:none;transform:none;position:fixed;inset:0;width:100% !important;max-width:none !important;margin:0;padding:0;display:flex;align-items:center;justify-content:center;background:#ffffff;pointer-events:none;}}
.reveal .slides section .fragment.wortliste.visible{{opacity:0;animation:wortliste-zeigen var(--dauer,5s) linear 1;}}
@keyframes wortliste-zeigen{{from{{opacity:1}}to{{opacity:1}}}}
    </style>
  </div>
</section>

{{% question "Welche Wörter wissen Sie noch?", "Schreiben Sie sie auf. 30 Sekunden." %}}

<section class="simple" data-transition="fade">
  <div>
    <h1>Die Liste</h1>
    <div style="margin:0;padding:0;font-size:3.2vh;line-height:1.2;text-align:left;columns:2;">{liste()}</div>
  </div>
</section>

{{% statement "Das Andere bleibt hängen.", "Was sich abhebt, wird nicht nur schneller gefunden, sondern auch besser erinnert." %}}
''')

# Wireframes
def icons(badges=()):
    out=[]
    for r in range(5):
        for c in range(4):
            i=r*4+c; x=25+c*110; y=80+r*110
            out.append(f'  <rect data-id="i{i}" x="{x}" y="{y}" width="70" height="70" rx="18" fill="#d9d9d9" />')
    for i in badges:
        r,c=divmod(i,4); x=25+c*110; y=80+r*110
        out.append(f'  <circle data-id="b{i}" cx="{x+66}" cy="{y+4}" r="16" fill="{L}" stroke="#ffffff" stroke-width="4" />')
    return '\n'.join(out)+'\n'
viele=(1,3,4,6,9,10,13,15,16,18)
form='''  <rect data-id="l0" x="75" y="90" width="110" height="12" fill="#888888" />
  <rect data-id="f0" x="75" y="110" width="300" height="48" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="l1" x="75" y="210" width="110" height="12" fill="#888888" />
  <rect data-id="f1" x="75" y="230" width="300" height="48" fill="#ffffff" stroke="{s1}" stroke-width="{w1}" />
  {err}
  <rect data-id="l2" x="75" y="350" width="110" height="12" fill="#888888" />
  <rect data-id="f2" x="75" y="370" width="300" height="48" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="l3" x="75" y="470" width="110" height="12" fill="#888888" />
  <rect data-id="f3" x="75" y="490" width="300" height="48" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="btn" x="75" y="590" width="140" height="48" rx="24" fill="#231f20" />
'''
err=f'<circle data-id="ei" cx="350" cy="254" r="11" fill="{L}" /><rect data-id="em" x="75" y="292" width="180" height="10" fill="{L}" />'
W(D,'050-auf-dem-screen.md',f'''
---
title: "Auf dem Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Homescreen als Wireframe. Zwanzig gleiche Icons. Dann ein einziger Punkt an einem Icon: Sie sehen ihn sofort, ohne zu suchen. Genau dafür ist er gebaut. Dann viele Punkte: Jetzt springt keiner mehr heraus, und trotzdem zieht jeder ein bisschen.

  Ein Formular mit einem fehlerhaften Feld. Der Fehler wird gefunden, weil er sich in mehreren Merkmalen gleichzeitig unterscheidet: Farbe, dickerer Rahmen, ein Symbol, eine Meldung darunter. So erkennen ihn auch Menschen, die die Farbe nicht unterscheiden können. In echten Interfaces ist die Fehlerfarbe meist Rot, hier steht die Akzentfarbe dafür.
---

{{% frame '{{"w":450,"h":900,"bu":"Zwanzig gleiche Icons"}}' %}}
{icons()}{{% endframe %}}
{{% frame '{{"w":450,"h":900,"bu":"Ein Punkt: sofort gesehen"}}' %}}
{icons((6,))}{{% endframe %}}
{{% frame '{{"w":450,"h":900,"bu":"Viele Punkte: Keiner springt mehr heraus, jeder zieht"}}' %}}
{icons(viele)}{{% endframe %}}
{{% frame '{{"stage":"#ffffff","w":450,"h":740,"bu":"Ein Formular"}}' %}}
{form.format(s1="#888888",w1="2",err="")}{{% endframe %}}
{{% frame '{{"stage":"#ffffff","w":450,"h":740,"bu":"Ein Fehler: Farbe, Rahmen, Symbol und Meldung zugleich"}}' %}}
{form.format(s1=L,w1="4",err=err)}{{% endframe %}}
''')

W(D,'060-aufmerksamkeit.md','''
---
title: "Aufmerksamkeit"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Der rote Punkt am App-Icon ist Pop-out auf Bestellung. Er nutzt genau den Mechanismus, den Sie gerade erlebt haben: Er wird gesehen, bevor man sich entscheiden kann, ihn nicht zu sehen. Und er bleibt hängen (Von Restorff).

  Das ist nützlich, wenn wirklich etwas wartet: eine Nachricht von einem Menschen, ein Fehler, ein Termin. Es wird zum Problem, wenn der Punkt vor allem dazu da ist, die App wieder zu öffnen: Badges für Empfehlungen, »Neuigkeiten«, Angebote.

  Diskussion (ca. 3 Minuten): Wie viele Punkte hat Ihr Homescreen gerade? Welche davon haben Ihnen etwas gebracht?

  **Hintergrund**

  Jon Yablonski, Laws of UX (2. Auflage 2024), Kapitel zur Ethik: Wer weiß, wie Wahrnehmung funktioniert, kann damit Aufmerksamkeit lenken, auch gegen die Interessen der Nutzenden. Im Rückgrat des Moduls: Verantwortung, Bereich Aufmerksamkeit (»Wem gehört die Zeit der Nutzenden?«), Prinzip Aufmerksamkeit respektieren.
---

{% interlude "Pop-out auf Bestellung.", "Ein Punkt am Icon wird gesehen, bevor Sie entscheiden können, ihn nicht zu sehen." %}

{% question "Wer verbraucht hier Ihre Aufmerksamkeit?", "Wie viele Punkte hat Ihr Homescreen gerade? Und welche davon haben Ihnen etwas gebracht?" %}
''')

W(D,'070-fuehrt-zu.md','''
---
title: "Führt zu"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Führt zu den Prinzipien Kontrast und Hervorhebung (welche Merkmale, wie sparsam) und Hierarchie (was zuerst gesehen wird).
---

{% statement "Führt zu", "[Kontrast und Hervorhebung](../prinzip-kontrast-und-hervorhebung/) und [Hierarchie](../prinzip-hierarchie/): Was sich in einem Merkmal unterscheidet, wird zuerst gesehen und am besten erinnert." %}
''')

done(D,'Was sich in einem einzigen Merkmal unterscheidet, springt sofort ins Auge und bleibt hängen. Kombinationen muss man suchen','Pop-out, präattentive Wahrnehmung, Merkmalssuche, Konjunktionssuche, Von-Restorff-Effekt')
