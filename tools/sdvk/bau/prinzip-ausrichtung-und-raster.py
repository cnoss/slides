# Bauskript prinzip-ausrichtung-und-raster. Aufruf: python3 tools/sdvk/bau/prinzip-ausrichtung-und-raster.py
import glob, os
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D='prinzip-ausrichtung-und-raster'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D,'Ausrichtung und Raster','Prinzip // Ordnen')

K='#231f20'; G1='#888888'; G2='#d9d9d9'; L='#9313ce'

W(D,'010-regel.md','''
---
title: "Ausrichtung und Raster"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Regel in zwei Teilen. Ausrichtung: Kein Element steht für sich, jedes bezieht sich auf eine Kante, eine Achse oder eine Linie, an der auch andere stehen. Raster: Viele solcher Bezüge zusammen ergeben ein System. Was auf demselben Raster steht, gehört sichtbar zu einem Ganzen, auch wenn das Raster selbst unsichtbar bleibt.

  Warum wir unsichtbare Linien überhaupt sehen, erklärt das Gesetz der guten Fortsetzung: Elemente, die auf einer Linie liegen, werden als Verlauf gelesen.

  **Hintergrund**

  Lidwell, Holden & Butler, Universal Principles of Design (Alignment): Ausgerichtete Elemente wirken geordneter, zusammengehöriger und leichter zu erfassen. Das Gestaltungsraster hat seine Wurzeln im Buchdruck (Satzspiegel) und wurde in der Schweizer Typografie der 1950er und 1960er Jahre zum System ausgebaut, u. a. von Josef Müller-Brockmann (»Rastersysteme für die visuelle Gestaltung«, 1981), Emil Ruder und Karl Gerstner. Im Web ist es mit CSS Grid seit 2017 in allen großen Browsern direkt im Code verfügbar.
---

{% interlude "Jedes Element richtet sich an etwas aus.", "Und ein gemeinsames Raster verbindet alles, was darauf steht." %}
''')

W(D,'015-mueller-brockmann.md','''
---
title: "Josef Müller-Brockmann"
layout: presentation.11ty.js
slideClasses: cite
author: Josef Müller-Brockmann, Grafiker
src: "Müller-Brockmann, J. (1981): Rastersysteme für die visuelle Gestaltung. Niggli, Teufen"
status: ok
speaker: |
  Zitat aus dem bisherigen Foliensatz Proportionen und Abstände. Wortlaut und Seite bitte am Original prüfen (deutsche Ausgabe, Niggli).

  Müller-Brockmann (1914 bis 1996) war einer der prägenden Gestalter der Schweizer Typografie. Seine Konzertplakate für die Tonhalle Zürich sind Lehrbeispiele für Gestaltung im Raster: wenige Elemente, strenge Ordnung, große Wirkung.

  Diskussion: Stimmt das mit dem Vertrauen? Ein Formular, eine Rechnung, ein Fahrplan: Ordnung wirkt verlässlich. Unordnung wirkt schnell unseriös, auch wenn der Inhalt stimmt.
---

Reduziert man die Zahl der visuellen Elemente und integriert sie in ein Rastersystem, entstehen klare Designs, die sich durch eine spezifische Ordnung auszeichnen. Diese Ordnung verleiht den Informationen Glaubwürdigkeit und schafft Vertrauen.
''')

# Ausrichtung abstrakt: fünf verschiedene Formen, je ein Ausrichtungsprinzip pro Folie
# Form: (id, typ, breite, höhe)
shapes=[('s0','rect',120,70),('s1','circle',80,80),('s2','rect',60,60),('s3','rect',200,40),('s4','circle',50,50)]
def shape(id_,typ,w,h,x,y,fill=K):
    if typ=='circle':
        return f'  <circle data-id="{id_}" cx="{x+w/2:g}" cy="{y+h/2:g}" r="{w/2:g}" fill="{fill}" />\n'
    return f'  <rect data-id="{id_}" x="{x:g}" y="{y:g}" width="{w}" height="{h}" fill="{fill}" />\n'
def layout(kind):
    out=''
    if kind=='frei':
        pos=[(330,70),(120,170),(420,250),(200,330),(90,470)]
        for (i,t,w,h),(x,y) in zip(shapes,pos): out+=shape(i,t,w,h,x,y)
        return out
    if kind in ('links','mitte','rechts'):
        y=70
        for i,t,w,h in shapes:
            x={'links':150,'mitte':300-w/2,'rechts':450-w}[kind]
            out+=shape(i,t,w,h,x,y); y+=h+40
        return out
    if kind=='grundlinie':
        x=60
        for i,t,w,h in shapes:
            out+=shape(i,t,w,h,x,400-h); x+=w+20
        return out
def achse(kind):
    x1,y1,x2,y2={'links':(150,40,150,560),'mitte':(300,40,300,560),'grundlinie':(30,400,570,400)}[kind]
    return f'  <line data-id="achse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{L}" stroke-width="3" stroke-linecap="round" />\n'
fr=lambda bu,svg: f"{{% frame '{{\"stage\":\"#ffffff\",\"bu\":\"{bu}\"}}' %}}\n{svg}{{% endframe %}}"
W(D,'020-ausrichtung.md',f'''
---
title: "Ausrichtung abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Fünf Formen, verschieden groß, verschieden in der Form. Erst frei verteilt: Jede steht für sich, das Ganze wirkt zufällig. Dann richten sie sich an einer Kante aus, und plötzlich ist es eine Gruppe. Die lila Linie zeigt die Kante einmal, danach verschwindet sie wieder. Gesehen wird sie trotzdem.

  Dann die anderen Möglichkeiten: Mittelachse und Grundlinie (Baseline). Fragen: Welche Fassung wirkt am ruhigsten? Welche am festesten? Meist: die linke Kante am ruhigsten (sie ist am leichtesten zu verfolgen, weil sie gerade ist), die Grundlinie am festesten (alles steht, siehe Kräfte). Die Mittelachse erzeugt einen unruhigen, gezackten Rand auf beiden Seiten.

  Kreise und Quadrate an derselben Kante wirken nicht ganz bündig. Das ist ein Fall für die optische Korrektur (siehe Phänomen Optische Korrektur).
---

{fr("Frei verteilt: Jede Form steht für sich", layout('frei'))}
{fr("An einer Kante ausgerichtet: eine Gruppe", layout('links'))}
{fr("Die Kante, die man sieht, obwohl sie nicht da ist", layout('links')+achse('links'))}
{fr("An der Mittelachse", layout('mitte'))}
{fr("Auf einer Grundlinie (Baseline)", layout('grundlinie'))}
''')

# Raster abstrakt: Format 600 x 600, 6 Spalten, Rand 40, Rinne 20 -> Spalte (600-80-100)/6 = 70
M=40; GU=20; CW=70
cx=lambda c: M+c*(CW+GU)
cols=''.join(f'  <rect data-id="col{c}" x="{cx(c)}" y="{M}" width="{CW}" height="{600-2*M}" fill="{L}" fill-opacity="0.12" />\n' for c in range(6))
cols0=''.join(f'  <rect data-id="col{c}" x="{cx(c)}" y="{M}" width="{CW}" height="{600-2*M}" fill="{L}" fill-opacity="0" />\n' for c in range(6))
# Elemente: Bild, Headline, Textzeilen, zwei Bildchen, Button
def els(snap):
    if snap:
        e=[('bild',cx(0),M,cx(3)+CW-cx(0),180,G2),('h',cx(4),M,cx(5)+CW-cx(4),22,G1),
           ('t1',cx(4),M+40,cx(5)+CW-cx(4),12,G2),('t2',cx(4),M+62,cx(5)+CW-cx(4),12,G2),('t3',cx(4),M+84,CW+40,12,G2),
           ('b1',cx(0),260,cx(1)+CW-cx(0),120,G2),('b2',cx(2),260,cx(3)+CW-cx(2),120,G2),('b3',cx(4),260,cx(5)+CW-cx(4),120,G2),
           ('u1',cx(0),400,cx(1)+CW-cx(0),12,G2),('u2',cx(2),400,cx(3)+CW-cx(2),12,G2),('u3',cx(4),400,cx(5)+CW-cx(4),12,G2),
           ('btn',cx(0),470,cx(1)+CW-cx(0),40,K)]
    else:
        e=[('bild',55,48,300,170,G2),('h',385,70,150,22,G1),
           ('t1',372,112,170,12,G2),('t2',380,134,175,12,G2),('t3',368,156,100,12,G2),
           ('b1',35,262,150,130,G2),('b2',215,250,170,110,G2),('b3',410,275,140,125,G2),
           ('u1',50,412,140,12,G2),('u2',230,380,150,12,G2),('u3',415,420,130,12,G2),
           ('btn',70,480,150,40,K)]
    return ''.join(f'  <rect data-id="{i}" x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}"{" rx=\"20\"" if i=="btn" else ""} />\n' for i,x,y,w,h,f in e)
frg=lambda bu,svg: f"{{% frame '{{\"bu\":\"{bu}\"}}' %}}\n{svg}{{% endframe %}}"
W(D,'030-raster.md',f'''
---
title: "Raster abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Format mit zwölf Elementen: ein großes Bild, eine Überschrift mit Text, drei Bilder mit Unterzeilen, ein Button. Erst nach Augenmaß platziert. Nichts ist falsch, aber nichts passt zusammen.

  Dann wird ein Raster sichtbar: sechs Spalten (Columns) mit Rinnen (Gutter) dazwischen und einem Rand (Margin). Die Elemente rasten ein, jedes beginnt und endet an einer Spaltenkante. Zum Schluss verschwindet das Raster wieder. Die Ordnung bleibt.

  Fragen: Was hat sich verändert? Nur die Positionen und Breiten. Kein Element ist neu, keine Farbe anders.

  Hier ist die graue Bühne mit weißem Format bewusst gewählt: Beim Raster bedeutet das Format etwas, die Spalten beziehen sich auf seine Kanten.
---

{frg("Nach Augenmaß", cols0+els(False))}
{frg("Ein Raster (Grid) aus sechs Spalten (Columns)", cols+els(False))}
{frg("Die Elemente rasten ein", cols+els(True))}
{frg("Das Raster verschwindet. Die Ordnung bleibt", cols0+els(True))}
''')

# Anatomie: je eine Größe hervorgehoben
def anat(mark):
    out=''
    for c in range(6):
        hl = (mark=='spalte' and c==2)
        out+=f'  <rect data-id="col{c}" x="{cx(c)}" y="{M}" width="{CW}" height="{600-2*M}" fill="{L if hl else G2}" fill-opacity="{0.9 if hl else 0.6}" />\n'
    # Rinne
    out+=f'  <rect data-id="rinne" x="{cx(2)+CW}" y="{M}" width="{GU}" height="{600-2*M}" fill="{L}" fill-opacity="{0.9 if mark=="rinne" else 0}" />\n'
    # Rand
    op=0.9 if mark=='rand' else 0
    out+=f'  <rect data-id="rand" x="0" y="0" width="{M}" height="600" fill="{L}" fill-opacity="{op}" />\n'
    # Modul: horizontale Teilung in Zeilen, ein Modul markiert
    rows=5; RH=(600-2*M-(rows-1)*GU)/rows
    for r in range(1,rows):
        y=M+r*RH+(r-1)*GU
        out+=f'  <rect data-id="row{r}" x="{M}" y="{y:g}" width="{600-2*M}" height="{GU}" fill="#ffffff" fill-opacity="{1 if mark=="modul" else 0}" />\n'
    out+=f'  <rect data-id="modul" x="{cx(2)}" y="{M+RH+GU:g}" width="{CW}" height="{RH:g}" fill="{L}" fill-opacity="{0.9 if mark=="modul" else 0}" />\n'
    return out
W(D,'040-anatomie.md',f'''
---
title: "Anatomie eines Rasters"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Vier Begriffe, die man braucht, um über Raster zu sprechen, in Figma genauso wie in CSS.

  - **Spalte (Column):** die Fläche, auf der Inhalte stehen. Ein Element belegt eine oder mehrere Spalten.
  - **Rinne (Gutter):** der Abstand zwischen zwei Spalten. In CSS heißt sie gap.
  - **Rand (Margin):** der Abstand zwischen Raster und Formatkante.
  - **Modul (Module, Rasterzelle):** Teilt man die Spalten zusätzlich in Zeilen (Rows), entstehen Module. Ein Raster aus Spalten und Zeilen heißt Modulraster.

  Begriffe: Spalte (Column), Rinne (Gutter), Rand (Margin), Modul (Module), Modulraster (Modular Grid). Figma und viele Werkzeuge verwenden die englischen Begriffe, deshalb brauchen Sie beide.
---

{frg("Spalte (Column)", anat('spalte'))}
{frg("Rinne (Gutter)", anat('rinne'))}
{frg("Rand (Margin)", anat('rand'))}
{frg("Modul (Module): Spalten (Columns) und Zeilen (Rows) ergeben Rasterzellen", anat('modul'))}
''')

# Beispiel Modulraster 24 x 32, Format 990 x 1310 halbiert (495 x 655): Rand 10, Rinne 5, Zelle 15
def modulraster(n_el):
    m=10; g=5; c=15
    out=''
    for i in range(24):
        for j in range(32):
            out+=f'<rect x="{m+i*(c+g)}" y="{m+j*(c+g)}" width="{c}" height="{c}" fill="{G2}" fill-opacity="0.55" />'
    return out
def gruppe():
    m=10; g=5; c=15; p=lambda i: m+i*(c+g)
    out=''
    # Gruppe aus Kreisen links oben (Nähe), Quadrate rechts (Ähnlichkeit), ein lila Ausreißer
    for i in range(2,8):
        for j in range(3,9): out+=f'<circle cx="{p(i)+7.5}" cy="{p(j)+7.5}" r="7.5" fill="{K}" />'
    for i in range(13,22,2):
        for j in range(3,15,2): out+=f'<rect x="{p(i)}" y="{p(j)}" width="15" height="15" fill="{K}" />'
    for i in range(2,22):
        out+=f'<rect x="{p(i)}" y="{p(20)}" width="15" height="15" fill="{G1}" />'
    out+=f'<rect x="{p(11)}" y="{p(20)}" width="15" height="15" fill="{L}" />'
    return out
W(D,'050-modulraster.md',f'''
---
title: "Ein Modulraster"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein strenges Modulraster für ein Tablet im Hochformat: 990 × 1310 Pixel, 24 Spalten (Columns) und 32 Zeilen (Rows), Rand (Margin) 20, Rinne (Gutter) 10. Daraus ergeben sich quadratische Zellen von 30 × 30 Pixeln: (990 − 2 × 20 − 23 × 10) ÷ 24 = 30 und (1310 − 2 × 20 − 31 × 10) ÷ 32 = 30.

  Auf so einem Raster lässt sich jedes Gestaltgesetz durchspielen: Nähe, Ähnlichkeit, gemeinsame Ausrichtung, Störung. Auf der zweiten Folie: eine Gruppe durch Nähe, eine durch Ähnlichkeit, eine Reihe mit einem Ausreißer.

  **In Figma:** Frame auswählen, unter »Layout guide« (früher »Layout grid«) zwei Raster anlegen: Columns mit Count 24, Margin 20, Gutter 10 und Rows mit Count 32, Margin 20, Gutter 10. Mit Shift und Pfeiltaste springt eine Form 10 Pixel weit. Stellt man den großen Schritt in den Einstellungen (Nudge amount) auf 40, springt sie genau von Zelle zu Zelle.
---

{{% frame '{{"w":495,"h":655,"bu":"24 Spalten (Columns), 32 Zeilen (Rows), quadratische Zellen"}}' %}}
{modulraster(0)}{{% endframe %}}
{{% frame '{{"w":495,"h":655,"bu":"Darauf gruppieren: Nähe, Ähnlichkeit, ein Ausreißer"}}' %}}
{modulraster(0)}{gruppe()}{{% endframe %}}
''')

# Im Screen: Desktop-Wireframe 900 x 500 mit 12 Spalten, Rand 60, Rinne 20 -> Spalte (900-120-220)/12 = 46.67
SM=60; SG=20; SC=(900-2*SM-11*SG)/12
sx=lambda c: SM+c*(SC+SG)
span=lambda a,b: sx(b)+SC-sx(a)
cols12=lambda op: ''.join(f'  <rect data-id="sc{c}" x="{sx(c):g}" y="0" width="{SC:g}" height="500" fill="{L}" fill-opacity="{op}" />\n' for c in range(12))
def seite(bruch=False):
    e=[('nav',sx(0),30,span(0,1),16,G1),('n1',sx(8),33,SC,10,G2),('n2',sx(9),33,SC,10,G2),('n3',sx(10),33,SC,10,G2),('n4',sx(11),33,SC,10,G2),
       ('h',sx(0),100,span(0,5),26,G1),('t1',sx(0),146,span(0,5),12,G2),('t2',sx(0),168,span(0,4),12,G2),('btn',sx(0),206,span(0,1),36,K),
       ('k1',sx(0),290,span(0,3),130,'#e4e4e4'),('k2',sx(4),290,span(4,7),130,'#e4e4e4'),('k3',sx(8),290,span(8,11),130,'#e4e4e4')]
    if bruch: e.insert(9,('bild',sx(7),70,900-sx(7),190,G2))
    else: e.insert(9,('bild',sx(7),70,span(7,11),190,G2))
    return ''.join(f'  <rect data-id="{i}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{f}"{" rx=\"18\"" if i=="btn" else ""} />\n' for i,x,y,w,h,f in e)
fq=lambda bu,svg: f"{{% frame '{{\"w\":900,\"h\":500,\"bu\":\"{bu}\"}}' %}}\n{svg}{{% endframe %}}"
W(D,'060-im-screen.md',f'''
---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Startseite als Wireframe. Navigation, Überschrift mit Text und Button, ein Bild, drei Karten. Dann das Raster dahinter: zwölf Spalten. Jedes Element beginnt und endet an einer Spaltenkante. Die Karten belegen je vier Spalten, der Text sechs, das Bild fünf.

  Zwölf Spalten sind im Web so verbreitet, weil sich zwölf durch zwei, drei, vier und sechs teilen lässt. Auf dem Handy sind vier Spalten üblich, auf dem Tablet acht (so etwa im Raster von Material Design, aus dem Gedächtnis, bitte prüfen).

  Die dritte Fassung bricht das Raster bewusst: Das Bild läuft rechts aus dem Format. Ein Rasterbruch wirkt nur, weil alles andere im Raster steht.

  Danach dasselbe im Code. CSS Grid beschreibt genau diese Struktur: Spalten (Columns), Rinne (Gutter, in CSS: gap), Spannweite eines Elements. Wer in Figma mit einem Raster entwirft, kann es eins zu eins übergeben.
---

{fq("Eine Startseite", cols12(0)+seite())}
{fq("Zwölf Spalten (Columns) dahinter", cols12(0.1)+seite())}
{fq("Bewusst gebrochen: Das Bild läuft aus dem Format", cols12(0.1)+seite(True))}

<section class="simple" data-transition="fade">
  <div>
    <h1>Dasselbe Raster im Code</h1>
<pre style="font-size:2.6vh; line-height:1.5; text-align:left; width:100%; box-shadow:none;"><code class="language-css">.seite {{
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px; /* Rinne, Gutter */
  padding: 0 60px; /* Rand, Margin */
}}
.karte {{ grid-column: span 4; }}
.text {{ grid-column: 1 / 7; }}</code></pre>
  </div>
</section>

{{% question "Wie viele Spalten hat Ihre meistgenutzte App?", "Legen Sie gedanklich ein Raster darüber. Woran richten sich die Elemente aus?" %}}
''')

W(D,'070-grenzen.md','''
---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Das Raster ist ein Werkzeug, kein Käfig.** Wathan und Schoger (Refactoring UI) schreiben ausdrücklich »Grids are overrated«: Nicht alles muss sich in Prozentspalten auflösen. Eine Seitenleiste mit fester Breite oder ein Formular mit fester Maximalbreite ist oft besser als eine Breite, die sich aus Spalten ergibt.

  **Optik schlägt Mathematik:** Kreise, Dreiecke und Icons wirken an einer exakten Kante eingerückt. Dann wird optisch korrigiert, nicht nach dem Raster (siehe Optische Korrektur).

  **Bruch braucht Ordnung:** Ein Rasterbruch wirkt nur vor einem Raster. Wer nie ein Raster hatte, kann es auch nicht brechen, es sieht dann einfach unordentlich aus.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt das Raster nicht?</h1>
    {% fragment '<p class="list">Wenn es zum Käfig wird: Manche Elemente brauchen eine feste Breite statt einer Spaltenbreite.</p>' %}
    {% fragment '<p class="list">Wenn die Rechnung stimmt, aber das Auge nicht: Dann optisch korrigieren.</p>' %}
    {% fragment '<p class="list">Wenn alles gebrochen wird: Ein Bruch wirkt nur vor einer Ordnung.</p>' %}
  </div>
</section>
''')

W(D,'080-verweise.md','''
---
title: "Verweise"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dahinter: Fortsetzung (warum wir unsichtbare Linien sehen) und Eindeutigkeit (fast bündig ist schlechter als bündig). Weiter: Nähe und Abstand, Weißraum, Optische Korrektur. Konstruieren: Gestaltungsraster und Spacing-System als Methoden. Ausprobieren: Permutation.
---

{% statement "Verweise", "Dahinter: [Fortsetzung und Schicksal](../prinzip-fortsetzung-und-schicksal/) und [Eindeutigkeit](../prinzip-eindeutigkeit/). Weiter: [Nähe und Abstand](../prinzip-naehe-und-abstand/), [Weißraum](../prinzip-weissraum/) und [Optische Korrektur](../phaenomen-optische-korrektur/). Konstruieren: [Gestaltungsraster](../methode-gestaltungsraster/) und [Spacing-System](../methode-spacing-system/). Ausprobieren: [Permutation](../methode-permutation/)." %}
''')

done(D,'Jedes Element richtet sich an etwas aus. Ein gemeinsames Raster verbindet alles, was darauf steht','Ausrichtung, Achse, Gestaltungsraster, Spalte (Column), Rinne (Gutter), Rand (Margin), Modul (Module)')

# Herkunft: Zitat aus dem Bestand
p=f'{NEW}/{D}/index.md'; s=open(p).read()
open(p,'w').write(s.replace('herkunft: "N"','herkunft: "N, Zitat aus proportionen-und-abstaende/020"'))
