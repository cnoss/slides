exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'methode-isotype'
os.makedirs(f'{NEW}/{D}/images', exist_ok=True)

# Beispielgrafiken aus der Übung »Zahlen zeigen« (Website-Repo), Daten ausgedacht
SRC = '/Users/cnoss/git/mi/mi-bachelor/screendesign/_assignments/images'
for n in ['1a', '1b', '2', '3']:
    shutil.copy(f'{SRC}/zahlen-zeigen-{n}.svg', f'{NEW}/{D}/images/zahlen-zeigen-{n}.svg')

intro(D, 'Isotype', 'Methode // Konstruieren')

W(D, 'index.md', '''
---
title: "Isotype"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Methode"
gruppe: "Konstruieren"
tiefe: "kennen"
einsatz: "Mengen und Anteile mit gleichen Zeichen zeigen, Übung »Zahlen zeigen«"
kurzsatz: "Mengen mit vielen gleichen Zeichen zeigen und die Aussage über Gruppieren, Ordnen und Gewichten herausarbeiten"
begriffe: ["Isotype", "Bildstatistik", "Mengenzeichen", "Pointe"]
herkunft: "N"
inhalt:
  - "Erhebung im Raum"
  - "Dieselben 100 Zeichen"
  - "Regeln"
  - "Die drei Aufgaben"
status: ok
---
''')

# ---------------------------------------------------------------- Erhebung
W(D, '005-erhebung.md', '''
---
title: "Erhebung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Am Anfang des Blocks zeigen (ca. 3 Minuten).** Per Handzeichen abfragen, nacheinander: Auto, Bahn, Bus, Rad oder zu Fuß. Wer kombiniert, nennt das längste Stück. Zahlen an die Tafel schreiben und auf 100 hochrechnen.

  Die Zahlen sind die Grundlage für Aufgabe 1 der Übung »Zahlen zeigen«. Sie kommen danach auf die Website, damit auch alle sie haben, die heute nicht da sind.
---

{% question "Wie sind Sie heute nach Gummersbach gekommen?", "Auto, Bahn, Bus, Rad oder zu Fuß. Wer kombiniert, nennt das längste Stück." %}
''')

# ---------------------------------------------------------------- Problem
W(D, '010-problem.md', '''
---
title: "Dieselben 100 Zeichen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Zweimal dieselben 100 Zeichen, dieselben Zahlen. Links ungeordnet: Man sieht, dass es vier Sorten gibt, aber nicht, wie viele von jeder. Rechts gruppiert: Man sieht in einer Sekunde, welche Gruppe die größte ist. Und weil die kleinste lila ist, sieht man auch, worauf es ankommt.

  Nichts ist neu dazugekommen. Es hat sich nur die Anordnung geändert. Genau das leisten die Gestaltgesetze: Nähe macht aus Zeichen Gruppen, Ähnlichkeit macht Gruppen unterscheidbar, Ausrichtung macht sie vergleichbar, Hierarchie zeigt die Pointe.

  Die Zahlen sind ausgedacht.
---

{% interlude "Dieselben 100 Zeichen", "Wie trinken 100 Personen ihren Kaffee?" %}

{% screenshot "./images/zahlen-zeigen-1a.svg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Ungeordnet: vier Sorten, aber wie viele?<br><small>Ausgedachte Zahlen</small>"}' %}
{% screenshot "./images/zahlen-zeigen-1b.svg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Gruppiert: Die Aussage steht in einer Sekunde<br><small>Ausgedachte Zahlen</small>"}' %}

{% statement "Ein Zeichen steht für eine Menge.", "Mehr Menge heißt mehr Zeichen, nicht größere Zeichen. Die Aussage entsteht durch die Anordnung." %}
''')

# ---------------------------------------------------------------- Regeln
W(D, '020-regeln.md', '''
---
title: "Regeln"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Ein Zeichen, eine Menge:** Das Zeichen steht immer für dieselbe Menge, etwa eine Person oder ein Prozent. Wer mehr zeigen will, setzt mehr Zeichen, statt eines zu vergrößern. Größe lässt sich schlecht vergleichen: Ein doppelt so großes Quadrat hat die vierfache Fläche.

  **Zählen ohne Zählen:** Zeichen in Fünfer- oder Zehnerblöcken anordnen. Dann erfasst man die Menge, ohne zu zählen.

  **Gruppieren statt beschriften:** Je klarer die Gruppen, desto weniger Legende braucht es.

  **Eine Pointe:** Jede Grafik hat eine Aussage. Die bekommt den Akzent, alles andere tritt zurück.

  **Hintergrund**

  Isotype geht auf den Wiener Philosophen und Volksbildner Otto Neurath zurück. Ab 1925 entwickelte er am Gesellschafts- und Wirtschaftsmuseum in Wien die »Wiener Methode der Bildstatistik«: Statistiken sollten auch für Menschen ohne Vorbildung verständlich sein. Die Zeichen gestaltete ab 1928 der Grafiker Gerd Arntz, die Übersetzung von Daten in Bilder verantwortete Marie Neurath (geb. Reidemeister) als »Transformatorin«. Im niederländischen Exil bekam die Methode 1935 den Namen Isotype, »International System of Typographic Picture Education«.

  Arntz' Zeichen sind urheberrechtlich geschützt und deshalb nicht auf den Folien. Viele Beispiele zeigt das Gerd Arntz Web Archive (gerdarntz.org). Otl Aicher hat mit seinen Piktogrammen für die Olympischen Spiele 1972 an diese Tradition angeknüpft.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Regeln</h1>
    {% fragment '<p class="list"><strong>Ein Zeichen, eine Menge:</strong> mehr Zeichen statt größerer Zeichen</p>' %}
    {% fragment '<p class="list"><strong>Zählen ohne Zählen:</strong> in Fünfer- oder Zehnerblöcken anordnen</p>' %}
    {% fragment '<p class="list"><strong>Gruppieren statt beschriften:</strong> je klarer die Gruppen, desto kürzer die Legende</p>' %}
    {% fragment '<p class="list"><strong>Eine Pointe:</strong> Die Aussage bekommt den Akzent, alles andere tritt zurück</p>' %}
  </div>
</section>
''')

# ---------------------------------------------------------------- Aufgaben
W(D, '030-aufgaben.md', '''
---
title: "Die drei Aufgaben"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Übung »Zahlen zeigen« besteht aus drei Aufgaben, in derselben Reihenfolge wie die Folien heute: Gruppieren, Ordnen, Gewichten. Die Beispiele haben bewusst andere Themen. Bitte nicht abmalen, sondern das Prinzip übertragen.

  1. **Wie kommen wir nach Gummersbach?** 100 Zeichen, die Zahlen von heute. Beispiel: Kaffee.
  2. **Mein Tag in 96 Kästchen:** ein eigener Tag in Viertelstunden, 24 Spalten für 24 Stunden. Beispiel: ein Tag im Leben einer Katze.
  3. **Studienfortschritt als Widget:** 180 ECTS als Kachel für ein Studierendenportal, 390 px breit. Beispiel: ein Lauftraining.

  Vorlage in Figma, Abgabe bis 05.11. im ILU. Alles Weitere steht in der Aufgabe auf der Website.
---

{% interlude "Zahlen zeigen", "Drei Aufgaben: Gruppieren, Ordnen, Gewichten" %}

{% screenshot "./images/zahlen-zeigen-1b.svg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"1. Gruppieren: Wie kommen wir nach Gummersbach?<br><small>Beispiel mit ausgedachten Zahlen</small>"}' %}
{% screenshot "./images/zahlen-zeigen-2.svg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"2. Ordnen: Mein Tag in 96 Kästchen<br><small>Beispiel: ein Tag im Leben einer Katze</small>"}' %}
{% screenshot "./images/zahlen-zeigen-3.svg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"3. Gewichten: Studienfortschritt als Widget<br><small>Beispiel: ein Lauftraining mit 36 Einheiten</small>"}' %}
''')

print('fertig')
