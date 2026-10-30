exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
import math
D = 'methode-semantisches-differential'
ALT = 'semantisches-diff-axis-maps-moodboards'

intro(D, 'Semantisches Differenzial', 'Methode // Wirkung und Ziel')

# Bilder: Finanzseiten (Screenshots 2024) und Schriftmuster aus dem Altbestand, Krume-Screen aus dem Moodboard-Deck
imgs(D, ALT, ['deka.jpg', 'flossbach.jpg', 'black-rock.jpg', 'font-01.png', 'font-02.png', 'font-03.png'])
shutil.copy(f'{NEW}/methode-moodboard-und-farbklima/images/baeckerei-app.jpg', f'{NEW}/{D}/images/baeckerei-app.jpg')

# ---------------------------------------------------------------- Profil als SVG
SCHWARZ, GRAU, HELL, LILA = '#231f20', '#888888', '#d9d9d9', '#9313ce'
# (linker Pol, rechter Pol, Soll, Ist). Pole bewusst gemischt, damit die Wunschbegriffe nicht alle auf einer Seite stehen.
PAARE = [
    ('handwerklich', 'effizient',    1, 1.4),
    ('modern',       'traditionell', 4, 2.6),
    ('warm',         'klar',         2, 2.2),
    ('ruhig',        'lebendig',     3, 3.3),
    ('verspielt',    'seriös',       3, 3.4),
    ('exklusiv',     'bodenständig', 5, 3.2),
    ('nahbar',       'zurückhaltend',1, 1.6),
    ('natürlich',    'raffiniert',   2, 2.3),
]
LUECKEN = {1, 5}  # modern/traditionell, exklusiv/bodenständig
def X(v): return 330 + (v - 1) * 70
def Y(i): return 50 + i * 52

def profil(soll=False, ist=False, fokus=False):
    out = []
    for i, (l, r, s, t) in enumerate(PAARE):
        op = '0.25' if fokus and i not in LUECKEN else '1'
        y = Y(i)
        out.append(f'<g data-id="zeile{i}" opacity="{op}">')
        out.append(f'<text x="290" y="{y + 8}" text-anchor="end" font-family="sans-serif" font-size="22" fill="{SCHWARZ}">{l}</text>')
        out.append(f'<text x="650" y="{y + 8}" text-anchor="start" font-family="sans-serif" font-size="22" fill="{SCHWARZ}">{r}</text>')
        out.append(f'<line x1="{X(1)}" y1="{y}" x2="{X(5)}" y2="{y}" stroke="{HELL}" stroke-width="2" stroke-linecap="round" />')
        for v in range(1, 6):
            out.append(f'<circle cx="{X(v)}" cy="{y}" r="6" fill="#ffffff" stroke="{GRAU}" stroke-width="2" />')
        out.append('</g>')
    if soll:
        pts = ' '.join(f'{X(s)},{Y(i)}' for i, (l, r, s, t) in enumerate(PAARE))
        out.append(f'<polyline data-id="soll" points="{pts}" fill="none" stroke="{SCHWARZ}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" />')
        for i, (l, r, s, t) in enumerate(PAARE):
            out.append(f'<circle data-id="soll{i}" cx="{X(s)}" cy="{Y(i)}" r="10" fill="{SCHWARZ}" />')
    if ist:
        pts = ' '.join(f'{X(t):.0f},{Y(i)}' for i, (l, r, s, t) in enumerate(PAARE))
        out.append(f'<polyline data-id="ist" points="{pts}" fill="none" stroke="{LILA}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" />')
        for i, (l, r, s, t) in enumerate(PAARE):
            out.append(f'<circle data-id="ist{i}" cx="{X(t):.0f}" cy="{Y(i)}" r="10" fill="{LILA}" />')
    return '\n'.join(out)

# Entwurf links, Profil rechts: Das Bild steht fest, nur die Linien bauen sich auf
BILD_W = round(460 * 780 / 1688)
def mit_entwurf(inner):
    return (f'<image data-id="entwurf" href="./images/baeckerei-app.jpg" x="60" y="20" width="{BILD_W}" height="460" />'
            f'<rect data-id="entwurf-rand" x="60" y="20" width="{BILD_W}" height="460" fill="none" stroke="{HELL}" stroke-width="2" />'
            f'<g transform="translate(250,0)">\n{inner}\n</g>')

def frame(inner, bu, w=900, h=500):
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":" + str(w) + ", \"h\":" + str(h) + ", \"bu\":\"" + bu + "\"}' %}\n" + inner + "\n{% endframe %}"

# ---------------------------------------------------------------- Problem
W(D, '005-problem.md', '''
---
title: "Das Problem"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 5 Minuten):** Erst die Aufgabe zeigen, noch ohne Screenshot: Zettel und Stift raus. Dann drei Startseiten von Finanzanbietern nacheinander zeigen, je ca. eine Minute. Jede Person notiert pro Seite still für sich fünf bis zehn Adjektive. Nicht reinrufen: Sonst lehnen sich alle an die ersten Aussagen an, und die Unterschiede verschwinden. Erst danach einsammeln: Einige lesen ihre Wörter zu einer Seite vor, die Wörter an der Tafel sammeln.

  Was dabei passiert: Für dieselbe Seite fallen sehr unterschiedliche Wörter. »Seriös«, »langweilig«, »vertrauenswürdig«, »kalt«. Teils meinen sie dasselbe, teils das Gegenteil, und vergleichen kann man sie nicht. Genau dieses Problem löst das semantische Differenzial: Es gibt die Begriffe vor und macht aus Eindrücken Werte auf einer Skala.

  **Vergleich:** BlackRock und Flossbach von Storch nebeneinander. Beide verkaufen dasselbe, Geldanlage, und wirken trotzdem verschieden. Inwieweit? Die Adjektive von eben helfen, reichen aber nicht: Man merkt, dass man für den Vergleich gemeinsame Begriffe braucht. Das ist die Überleitung zum nächsten Schritt.

  Screenshots: deka.de, flossbachvonstorch.de, blackrock.com, jeweils 2024.
---

{% interlude "Wie wirkt was?", "Notieren Sie fünf bis zehn Adjektive." %}

{% screenshot "./images/deka.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Wie wirkt diese Seite?<br><small>deka.de, Screenshot 2024</small>"}' %}
{% screenshot "./images/flossbach.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und diese?<br><small>flossbachvonstorch.de, Screenshot 2024</small>"}' %}
{% screenshot "./images/black-rock.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und diese?<br><small>blackrock.com, Screenshot 2024</small>"}' %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Inwieweit wirken sie unterschiedlich?</h1>
    <div style="display:flex; gap:3vw; align-items:flex-start; width:100%;">
      <figure style="flex:1; margin:0;"><img src="./images/black-rock.jpg" alt="Startseite von BlackRock" style="width:100%; height:auto; box-shadow:0 0 1.5rem rgba(0,0,0,.2);"><figcaption><small>blackrock.com, Screenshot 2024</small></figcaption></figure>
      <figure style="flex:1; margin:0;"><img src="./images/flossbach.jpg" alt="Startseite von Flossbach von Storch" style="width:100%; height:auto; box-shadow:0 0 1.5rem rgba(0,0,0,.2);"><figcaption><small>flossbachvonstorch.de, Screenshot 2024</small></figcaption></figure>
    </div>
  </div>
</section>

{% statement "Zehn Personen, zehn Wörter.", "Eindrücke lassen sich so nicht vergleichen. Das semantische Differenzial gibt die Begriffe vor und macht aus Eindrücken Werte." %}
''')

# ---------------------------------------------------------------- Ergebnis zuerst
W(D, '010-ergebnis.md', '''
---
title: "Ergebnis zuerst"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  So sieht das Ergebnis aus, am Beispiel der erfundenen Bäckerei »Krume«, die Sie aus dem Moodboard kennen. Links steht der Entwurf, rechts baut sich das Profil auf. So hat man beim Bewerten den Entwurf vor Augen.

  **Das Profil:** acht Gegensatzpaare, dazwischen eine Skala mit fünf Stufen. Die schwarze Linie ist das Soll: So soll die Marke wirken. Es wird festgelegt, bevor gestaltet wird.

  **Der Test:** Zehn Personen, die das Soll nicht kennen, bewerten den Entwurf mit denselben Paaren. Die lila Linie ist der Mittelwert, das Ist.

  **Die Lücken:** Wo Soll und Ist auseinanderliegen, wirkt der Entwurf anders als geplant. Hier wirkt »Krume« moderner und exklusiver, als sie soll. Das ist ein konkreter Auftrag für die Überarbeitung, viel genauer als »gefällt mir nicht so«. Mögliche Ursachen: die serifenlose, sehr gleichmäßige Schrift, der viele Weißraum, die zurückhaltende Bildsprache.

  Die Daten sind ausgedacht, das Vorgehen ist echt.

  Die Pole stehen bewusst gemischt: Die Wunschbegriffe liegen mal links, mal rechts. Sonst kreuzen Bewertende aus Gewohnheit immer auf derselben Seite an.
---

''' + frame(mit_entwurf(profil()), 'Der Entwurf für die Bäckerei »Krume« und acht Gegensatzpaare mit fünf Stufen<br><small>Fiktives Beispiel</small>', 1160) + '''

''' + frame(mit_entwurf(profil(soll=True)), 'Das Soll: So soll »Krume« wirken', 1160) + '''

''' + frame(mit_entwurf(profil(soll=True, ist=True)), 'Das Ist: So wirkt der Entwurf auf zehn Testpersonen (Mittelwert)', 1160) + '''

''' + frame(mit_entwurf(profil(soll=True, ist=True, fokus=True)), 'Die Lücken: moderner und exklusiver als gewollt. Das ist der Auftrag für die Überarbeitung.', 1160) + '''
''')

# ---------------------------------------------------------------- Schritte
# Karte: Kern in der Mitte, Begriffe als Punkte, Nähe = Wichtigkeit
PUNKTE = [(95, 20), (110, 140), (125, 255), (135, 75), (150, 200), (160, 320), (170, 110), (175, 280),
          (215, 45), (230, 165), (240, 235), (255, 345), (265, 120)]
def karte(auswahl=False):
    out = [f'<circle data-id="kern" cx="300" cy="300" r="48" fill="{LILA}" />']
    if auswahl:
        out.append(f'<circle data-id="ring" cx="300" cy="300" r="193" fill="none" stroke="{HELL}" stroke-width="2" />')
    for k, (d, a) in enumerate(PUNKTE):
        x = 300 + d * math.cos(math.radians(a)); y = 300 + d * math.sin(math.radians(a))
        nah = k < 8
        farbe = SCHWARZ if nah else (HELL if auswahl else GRAU)
        out.append(f'<circle data-id="p{k}" cx="{x:.0f}" cy="{y:.0f}" r="13" fill="{farbe}" />')
    return '\n'.join(out)

W(D, '020-schritte.md', '''
---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **1. Sammeln:** Welche Eigenschaften soll die Marke haben? Adjektive, frei und ohne Bewertung. Hilfreich: Was sagen Kundinnen und Kunden? Was soll man nach dem ersten Besuch erzählen? Wodurch unterscheidet sich die Marke von der Konkurrenz?

  **2. Gewichten:** Die Begriffe um den Markenkern anordnen. Je wichtiger, desto näher dran. Die acht nächsten bleiben. Mehr Paare machen das Profil unlesbar und die Bewertung zäh. Wer einen neunten Begriff braucht, schiebt einen anderen nach außen.

  **3. Gegenpole finden:** Zu jedem Begriff ein Gegenbegriff. Beide Pole müssen positiv sein, siehe nächste Folien.

  **4. Soll festlegen:** Auf jeder Skala markieren, wo die Marke landen soll. Nicht überall die Mitte: Eine Marke, die sich nirgends festlegt, hat kein Profil.

  **5. Prüfen:** Andere bewerten den Entwurf mit denselben Paaren, ohne das Soll zu kennen. Dann Soll und Ist übereinanderlegen. Die Lücken sind der Auftrag.

  **Skala:** Wir arbeiten mit fünf Stufen. Osgood hat sieben verwendet. Fünf reichen, um Richtung und Stärke zu zeigen, und sind schneller ausgefüllt.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Semantisches Differenzial in fünf Schritten</h1>
    {% fragment '<p class="list"><strong>1. Sammeln:</strong> Wofür soll die Marke stehen? Adjektive, frei und ohne Bewertung</p>' %}
    {% fragment '<p class="list"><strong>2. Gewichten:</strong> je wichtiger, desto näher am Kern. Die acht nächsten bleiben.</p>' %}
    {% fragment '<p class="list"><strong>3. Gegenpole finden:</strong> beide Pole positiv</p>' %}
    {% fragment '<p class="list"><strong>4. Soll festlegen:</strong> auf einer Skala mit fünf Stufen</p>' %}
    {% fragment '<p class="list"><strong>5. Prüfen:</strong> Andere bewerten, ohne das Soll zu kennen. Soll und Ist vergleichen.</p>' %}
  </div>
</section>

''' + frame(karte(), 'Gewichten: je wichtiger der Begriff, desto näher am Kern', 600, 600) + '''

''' + frame(karte(True), 'Die acht nächsten bleiben, der Rest fällt raus', 600, 600) + '''
''')

# ---------------------------------------------------------------- Gegenpole
W(D, '030-gegenpole.md', '''
---
title: "Gegenpole finden"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Der schwierigste Schritt. Ein Pol, der wie ein Fehler klingt, zieht jede Bewertung auf die andere Seite. Niemand will »altmodisch« ankreuzen, also landen alle bei »modern«, und das Profil sagt nichts mehr.

  Ein guter Gegenpol ist eine echte Alternative: eine Eigenschaft, die eine andere Marke mit Stolz für sich beanspruchen würde. »Beständig« ist für eine Privatbank ein Versprechen, »altmodisch« nie.

  Prüffrage: Gibt es eine erfolgreiche Marke, die genau diesen Pol für sich wählen würde? Wenn nein, ist der Pol negativ.

  Ebenfalls kein Gegenpol: Synonyme oder Begriffe auf einer anderen Ebene, etwa »warm« gegen »herzlich« oder »modern« gegen »günstig«.

  KI-Werkzeuge helfen, Kandidaten zu finden. Die Prüffrage stellen Sie trotzdem selbst.
---

{% interlude "Beide Pole müssen positiv sein.", "Sonst kreuzt niemand die andere Seite an." %}

<section class="simple" data-transition="fade">
<div>

# Statt … besser

| Begriff | Negativer Gegenpol | Positiver Gegenpol |
|---|---|---|
| modern | altmodisch | beständig |
| lebendig | langweilig | ruhig |
| seriös | unseriös | verspielt |
| nahbar | distanziert | exklusiv |
| präzise | ungenau | intuitiv |

</div>
</section>

{% statement "Die Prüffrage", "Gibt es eine erfolgreiche Marke, die genau diesen Pol für sich wählen würde? Wenn nein, ist der Pol negativ." %}
''')

# Mini-Übung (040-uebung.md) entfernt am 28.10.2026: Die Wirkung der drei Seiten wird schon im Problem-Teil notiert.

# ---------------------------------------------------------------- Typische Fehler
W(D, '050-fehler.md', '''
---
title: Typische Fehler
layout: presentation.11ty.js
slideClasses: simple
status: ok
speaker: |
  Der häufigste Fehler ist der negative Gegenpol. Der zweithäufigste: nur selbst bewerten. Wer den Entwurf gebaut hat, sieht darin, was er wollte, nicht was er zeigt. Wirkung entsteht beim Gegenüber.

  Überall die Mitte: Wer auf jeder Skala die Mitte ankreuzt, hat keine Entscheidung getroffen. Ein Profil entsteht erst durch klare Ausschläge. Die Mitte ist oft eine Flucht vor der Entscheidung, beim Festlegen des Solls genauso wie beim Bewerten.

  Pole immer auf derselben Seite: Menschen kreuzen aus Gewohnheit gern auf einer Seite an (Antworttendenz). Gemischte Pole halten die Aufmerksamkeit wach.
---

{% fragment '<p class="list">Negativer Gegenpol: Die Bewertung kippt auf die andere Seite</p>' %}
{% fragment '<p class="list">Synonyme statt Gegensätze: warm gegen herzlich misst nichts</p>' %}
{% fragment '<p class="list">Zu viele Paare: Das Profil wird zur Zickzacklinie</p>' %}
{% fragment '<p class="list">Überall die Mitte: Wer sich nicht festlegt, hat kein Profil</p>' %}
{% fragment '<p class="list">Pole immer auf derselben Seite: Man kreuzt aus Gewohnheit an</p>' %}
{% fragment '<p class="list">Nur selbst bewerten: Wirkung entsteht beim Gegenüber</p>' %}
''')

# ---------------------------------------------------------------- Einsatz
W(D, '060-einsatz.md', '''
---
title: "Einsatz"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Das semantische Differenzial steht am Anfang: Es macht das Gestaltungsziel prüfbar. Danach folgen Moodboard und Farbklima. Und es kommt am Ende wieder, wenn geprüft wird, ob der Entwurf so wirkt wie geplant.

  Tiefe: können. Die Methode kommt bei Farbe, bei Schrift und im Projekt wieder.

  **Hintergrund**

  Das semantische Differenzial geht auf den Psychologen Charles E. Osgood zurück: Osgood, Suci und Tannenbaum, »The Measurement of Meaning« (1957). Osgood wollte die Bedeutung von Begriffen messbar machen und fand, dass sich die meisten Gegensatzpaare auf drei Grunddimensionen zurückführen lassen: Bewertung (gut gegen schlecht), Stärke (stark gegen schwach) und Aktivität (aktiv gegen passiv). Im deutschen Sprachraum hat Peter R. Hofstätter die Methode in den 1950er Jahren als Polaritätsprofil eingeführt.

  Die Skala mit Abstufungen geht auf Rensis Likert zurück, »A Technique for the Measurement of Attitudes« (1932).

  Für Marken hat Jennifer Aaker die Idee weitergeführt: »Dimensions of Brand Personality« (Journal of Marketing Research, 1997) beschreibt fünf Dimensionen der Markenpersönlichkeit: Aufrichtigkeit, Begeisterung, Kompetenz, Kultiviertheit und Robustheit.

  Am Ende hängt als Backup ein Beispiel zur Wirkung von Schrift: derselbe Satz in drei Schriften.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wo die Methode wiederkommt</h1>
    {% fragment '<p class="list">Am Anfang: Das Gestaltungsziel wird prüfbar</p>' %}
    {% fragment '<p class="list">Danach: Moodboard und Farbklima, Schriftauswahl</p>' %}
    {% fragment '<p class="list">Am Ende: Wirkt der Entwurf so wie geplant?</p>' %}
    {% fragment '<p class="list">Im Crit: »Wirkt exklusiver als geplant« statt »gefällt mir nicht«</p>' %}
  </div>
</section>

{% statement "Merksatz", "Erst das Soll festlegen, dann gestalten, dann andere prüfen lassen. Die Lücken sind der Auftrag." %}
''')

# ---------------------------------------------------------------- Backup
W(D, '900-backup.md', '''
---
title: "Backup: Wirkung von Schrift"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Backup, im normalen Ablauf überspringen. Derselbe Satz in drei Schriften: Frutiger, Georgia, Max. Gut geeignet, um das Differenzial live an Schrift auszuprobieren: Wie wirken die drei auf den Paaren sachlich gegen verspielt und modern gegen traditionell?
---

{% interlude "Backup", "Wirkung von Schrift" %}

{% screenshot "./images/font-01.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Frutiger"}' %}
{% screenshot "./images/font-02.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Georgia"}' %}
{% screenshot "./images/font-03.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Max"}' %}
''')

done(D, 'Wirkung über Gegensatzpaare festlegen, messen und vergleichen', 'Semantisches Differenzial, Polaritätsprofil, Gegensatzpaar, Soll und Ist, Likert-Skala')
p = f'{NEW}/{D}/index.md'; s = open(p).read()
s = s.replace('''inhalt:
  - "Gegensatzpaare finden"
  - "Bewerten"
  - "Auswerten und vergleichen"''', '''inhalt:
  - "Ergebnis zuerst: Soll und Ist"
  - "Fünf Schritte"
  - "Gegenpole finden"
  - "Typische Fehler"''').replace('einsatz: ""', 'einsatz: "Am Anfang zum Festlegen der Wirkung, am Ende zum Prüfen"')
open(p, 'w').write(s)
print('fertig')
