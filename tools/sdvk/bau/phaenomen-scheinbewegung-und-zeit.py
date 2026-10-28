# Bauskript für das Deck phaenomen-scheinbewegung-und-zeit
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
d='phaenomen-scheinbewegung-und-zeit'
B='#231f20'; L='#9313ce'

def frame(content, bu, w=900, h=500, animate=True):
    extra = '' if animate else ', \"animate\":false'
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":"+str(w)+", \"h\":"+str(h)+", \"bu\":\""+bu+"\""+extra+"}' %}\n"+content+"\n{% endframe %}\n"

intro(d,'Scheinbewegung und Zeit','Phänomen')

W(d,'010-frage.md','''
---
title: "Bewegt sich da etwas?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Einstieg ohne Erklärung. Auf den nächsten drei Folien passiert jedes Mal dasselbe, nur in einem anderen Tempo. Bei jeder Folie fragen: Was sehen Sie? Erst beschreiben lassen, dann weiterschalten.
---

{% interlude "Bewegt sich da etwas?", "Schauen Sie genau hin. Und beschreiben Sie, was Sie sehen." %}
''')

# Zwei Punkte, die abwechselnd aufleuchten. Gleiche Keyframes, drei Periodendauern.
# A an 0 bis 30 %, Pause, B an 50 bis 80 %, Pause. Bei 300 ms: 90 ms an, 60 ms Pause.
def phi(nr, periode):
    css = ('<style>'
      f'@keyframes phi-a-{nr}{{0%,29.9%{{opacity:1}}30%,100%{{opacity:0}}}}'
      f'@keyframes phi-b-{nr}{{0%,49.9%{{opacity:0}}50%,79.9%{{opacity:1}}80%,100%{{opacity:0}}}}'
      f'.phi-a-{nr}{{animation:phi-a-{nr} {periode} linear infinite}}'
      f'.phi-b-{nr}{{animation:phi-b-{nr} {periode} linear infinite}}'
      f'@media (prefers-reduced-motion: reduce){{.phi-a-{nr},.phi-b-{nr}{{animation:none}}}}'
      '</style>')
    return css+f'''
<circle data-id="pa" class="phi-a-{nr}" cx="330" cy="250" r="36" fill="{B}" />
<circle data-id="pb" class="phi-b-{nr}" cx="570" cy="250" r="36" fill="{B}" />'''

W(d,'020-erleben.md','''
---
title: "Zwei Punkte"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Live-Test (ca. 3 Minuten)**

  Dreimal dieselben zwei Punkte. Sie leuchten abwechselnd auf, nur das Tempo ändert sich.

  1. **Langsam** (Takt 2 Sekunden): zwei Punkte, die nacheinander blinken. Niemand sieht Bewegung.
  2. **Mittel** (jeder Punkt ca. 90 ms an, ca. 60 ms Pause): Ein Punkt springt hin und her. Fast alle sehen Bewegung, manche sogar die Strecke dazwischen.
  3. **Sehr schnell** (Takt 40 ms): beide Punkte gleichzeitig, leicht flimmernd. Keine Bewegung mehr.

  Bei jeder Folie fragen: Was sehen Sie? Auf dem Beamer kann das Tempo je nach Bildwiederholrate etwas abweichen. Die mittlere Folie ist die wichtige.

  Die Animation ist reines CSS. Ist im Betriebssystem »Bewegung reduzieren« aktiviert, stehen beide Punkte still. Für die Vorlesung die Einstellung am Präsentationsrechner ausschalten.
---

'''+frame(phi(1,'2s'),'Langsam: Was sehen Sie?')
   +frame(phi(2,'300ms'),'Schneller: Und jetzt?')
   +frame(phi(3,'40ms'),'Sehr schnell: Und jetzt?'))

W(d,'030-aufloesung.md','''
---
title: "Auflösung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Auf dem Bildschirm hat sich nichts bewegt. Zwei Punkte gehen an und aus, sonst nichts. Die Bewegung dazwischen, die lila Bahn, gibt es nur im Kopf.

  Jeder Film funktioniert so: 24 Einzelbilder pro Sekunde, und wir sehen Bewegung. Jede Animation im Interface auch. Ein Display zeigt nie Bewegung, immer nur eine Folge stehender Bilder.
---

'''+frame(f'''
<circle data-id="pa" cx="330" cy="250" r="36" fill="{B}" />
<circle data-id="pb" cx="570" cy="250" r="36" fill="{B}" />''','Auf dem Bildschirm: zwei Punkte, die an- und ausgehen')
   +frame(f'''
<path d="M 330 250 Q 450 150 570 250" fill="none" stroke="{L}" stroke-width="6" stroke-linecap="round" stroke-dasharray="1 18" />
<circle data-id="pa" cx="330" cy="250" r="36" fill="{B}" />
<circle data-id="pb" cx="570" cy="250" r="36" fill="{B}" />''','Im Kopf: eine Bewegung, die es nicht gibt')+'''
{% statement "Da bewegt sich nichts.", "Jeder Film, jede Animation, jedes Scrollen: eine Folge stehender Bilder. Die Bewegung macht das Gehirn." %}
''')

W(d,'040-mechanismus.md','''
---
title: "Mechanismus"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Das Gehirn bekommt zwei Reize an zwei Orten kurz nacheinander. Die einfachste Erklärung dafür ist: ein Gegenstand, der sich bewegt hat. Also sehen wir genau das. Ist die Pause zu lang, passt die Erklärung nicht mehr, wir sehen zwei Punkte. Ist sie zu kurz, sehen wir beide gleichzeitig.

  Das ist mehr als eine Kuriosität. Es zeigt: Wahrnehmung ist nicht die Summe einzelner Reize. Das Gehirn baut aus ihnen ein Ganzes, hier eine Bewegung, die in keinem der beiden Reize steckt.

  **Hintergrund**

  Max Wertheimer, »Experimentelle Studien über das Sehen von Bewegung«, Zeitschrift für Psychologie 61, 1912. Die Versuche fanden in Frankfurt statt, Versuchspersonen waren unter anderem Wolfgang Köhler und Kurt Koffka. Die Arbeit gilt als Gründungsdokument der Gestaltpsychologie (Berliner Schule).

  Wertheimer hat die Pause systematisch verändert. Ungefähre Werte aus seinen Versuchen: unter ca. 30 ms Gleichzeitigkeit, um ca. 60 ms optimale Bewegung, über ca. 200 ms Nacheinander (aus dem Gedächtnis, bitte prüfen).

  **Phi und Beta:** Streng genommen ist das, was die meisten hier sehen, die sogenannte Beta-Bewegung: Ein Gegenstand wandert sichtbar von A nach B. Wertheimers »reines Phi« ist eine objektlose Bewegung: Man sieht, dass sich etwas bewegt, aber keinen Gegenstand dazwischen. Die beiden werden im Alltag oft verwechselt, auch in Lehrbüchern (Steinman, Pizlo & Pizlo, Phi is not beta, 2000).

  Begriffe: Scheinbewegung, Phi-Phänomen, Gestaltpsychologie.
---

{% statement "Das Gehirn verbindet.", "Zwei Reize an zwei Orten, kurz nacheinander: Die einfachste Erklärung ist eine Bewegung. Also sehen wir eine." %}

{% statement "Der Beginn der Gestaltpsychologie", "Max Wertheimer, 1912: Die Bewegung steckt in keinem der beiden Reize. Das Ganze ist etwas anderes als seine Teile." %}
''')

W(d,'050-zeit.md','''
---
title: "Und wie lange dauert das?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Zweiter Teil: Auch Zeit wird nicht gemessen, sondern wahrgenommen. Gleich kommen zwei Ladevorgänge. Bitte nicht zählen, nur schauen.
---

{% interlude "Und wie lange dauert das?", "Zweimal laden. Bitte nicht zählen, nur schauen." %}
''')

# Karte als Wireframe, Inhalt erscheint nach 4 s. Animation startet, wenn die Folie aktiv wird (.present)
INHALT=f'''<rect x="320" y="60" width="260" height="140" fill="#c4c4c4" />
<rect x="320" y="222" width="180" height="16" fill="#888888" />
<rect x="320" y="254" width="260" height="10" fill="#aaaaaa" />
<rect x="320" y="274" width="240" height="10" fill="#aaaaaa" />
<rect x="320" y="294" width="170" height="10" fill="#aaaaaa" />
<rect x="320" y="330" width="110" height="36" rx="18" fill="{B}" />'''
SKELETT='''<rect x="320" y="60" width="260" height="140" fill="#d9d9d9" />
<rect x="320" y="222" width="180" height="16" fill="#d9d9d9" />
<rect x="320" y="254" width="260" height="10" fill="#d9d9d9" />
<rect x="320" y="274" width="240" height="10" fill="#d9d9d9" />
<rect x="320" y="294" width="170" height="10" fill="#d9d9d9" />
<rect x="320" y="330" width="110" height="36" rx="18" fill="#d9d9d9" />'''
CSS=('<style>'
  '@keyframes wz-da{0%{opacity:0}100%{opacity:1}}'
  '@keyframes wz-weg{0%{opacity:1}100%{opacity:0}}'
  '@keyframes wz-dreh{to{transform:rotate(360deg)}}'
  '@keyframes wz-puls{0%,100%{opacity:1}50%{opacity:.45}}'
  '.wz-inhalt{opacity:1}.wz-warten{opacity:0}'
  'section>section.present .wz-inhalt{animation:wz-da 4s step-end both}'
  'section>section.present .wz-warten{animation:wz-weg 4s step-end both}'
  'section>section.present .wz-dreh{transform-origin:450px 230px;animation:wz-dreh .9s linear infinite}'
  'section>section.present .wz-puls{animation:wz-puls 1.2s ease-in-out infinite}'
  '@media (prefers-reduced-motion: reduce){section>section.present .wz-dreh,section>section.present .wz-puls{animation:none}}'
  '</style>')
KARTE='<rect x="300" y="40" width="300" height="400" fill="#e4e4e4" />'
spinner=f'''<g class="wz-warten"><g class="wz-dreh"><circle cx="450" cy="230" r="34" fill="none" stroke="#d9d9d9" stroke-width="8" /><path d="M 450 196 A 34 34 0 0 1 484 230" fill="none" stroke="#888888" stroke-width="8" stroke-linecap="round" /></g></g>'''
skelett=f'<g class="wz-warten"><g class="wz-puls">{SKELETT}</g></g>'

W(d,'060-laden.md','''
---
title: "Zweimal laden"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Live-Test (ca. 2 Minuten)**

  Erst die Karte mit dem drehenden Kreis, dann die Karte mit den grauen Platzhaltern. Beide Male erscheint der Inhalt nach genau vier Sekunden. Die Animation startet, sobald die Folie erscheint (Auto-Animate ist auf diesen beiden Folien abgeschaltet, sonst bleibt der Inhalt unsichtbar). Wer sie noch einmal sehen will: eine Folie zurück und wieder vor.

  Danach fragen: Welcher Ladevorgang hat sich kürzer angefühlt? Meist sagt die Mehrheit: der zweite. Manche finden den Spinner kürzer, weil er vertraut ist. Beides ist ein Gesprächsanlass.

  Bei »Bewegung reduzieren« drehen und pulsieren die Platzhalter nicht, der Inhalt erscheint trotzdem nach vier Sekunden.
---

'''+frame(CSS+KARTE+spinner+f'<g class="wz-inhalt">{INHALT}</g>','Laden, Variante 1', animate=False)
   +frame(CSS+KARTE+skelett+f'<g class="wz-inhalt">{INHALT}</g>','Laden, Variante 2', animate=False)+'''
{% question "Was ging schneller?", "Beide dauerten genau vier Sekunden." %}
''')

W(d,'070-mechanismus-zeit.md','''
---
title: "Gefühlte Zeit"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Gefühlte Wartezeit hängt davon ab, was in der Zeit passiert. Leere Zeit dehnt sich, gefüllte Zeit vergeht schneller. Der Skeleton Screen zeigt sofort, wie das Ergebnis aussehen wird: Es passiert schon etwas, und man kann sich orientieren. Der Spinner sagt nur: warten.

  Die drei Grenzen sind seit Jahrzehnten stabil, weil sie an der menschlichen Wahrnehmung hängen, nicht an der Technik:

  - **0,1 Sekunden:** fühlt sich unmittelbar an, wie eine direkte Reaktion auf die eigene Handlung.
  - **1 Sekunde:** Der Gedankenfluss bleibt erhalten, man merkt die Verzögerung aber.
  - **10 Sekunden:** Grenze der Aufmerksamkeit. Danach braucht es eine Fortschrittsanzeige, sonst wird abgebrochen.

  **Hintergrund**

  Robert B. Miller, »Response time in man-computer conversational transactions«, 1968. Jakob Nielsen hat die drei Grenzen in »Usability Engineering« (1993) zusammengefasst. Walter J. Doherty und Ahrvind J. Thadani, »The Economic Value of Rapid Response Time« (IBM, 1982): Unter ca. 400 ms Antwortzeit arbeiten Menschen deutlich produktiver, Yablonski nennt das die Doherty-Schwelle (Laws of UX).

  Dass gefüllte Wartezeit kürzer wirkt als leere, beschreibt David Maister, »The Psychology of Waiting Lines« (1985), am Beispiel von Warteschlangen (aus dem Gedächtnis, bitte prüfen).

  Begriffe: gefühlte Wartezeit, Antwortzeit, Doherty-Schwelle, Skeleton Screen.
---

{% statement "Zeit wird nicht gemessen, sondern erlebt.", "Leere Wartezeit dehnt sich. Wartezeit, in der etwas passiert, vergeht schneller." %}

<section class="simple" data-transition="fade">
<div>

# Wie schnell ist schnell genug?

| Antwortzeit | Wirkung |
|---|---|
| bis 0,1 Sekunden | unmittelbar, wie eine direkte Reaktion |
| bis 0,4 Sekunden | flüssig, man bleibt im Arbeitsfluss |
| bis 1 Sekunde | spürbar, der Gedankenfluss bleibt |
| bis 10 Sekunden | Grenze der Aufmerksamkeit, danach braucht es eine Fortschrittsanzeige |

</div>
</section>
''')

# Auf dem Screen: Fortschritt und optimistische Oberfläche
HERZ='M 450 300 C 430 280 380 250 380 205 C 380 175 405 155 430 160 C 440 162 447 168 450 176 C 453 168 460 162 470 160 C 495 155 520 175 520 205 C 520 250 470 280 450 300 Z'
W(d,'080-auf-dem-screen.md','''
---
title: "Auf dem Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Drei Mittel gegen gefühlte Wartezeit, alle aus dem Alltag:

  **Skeleton Screens:** Platzhalter in der Form des Inhalts, wie eben gesehen. Verbreitet in Feeds, Shops und Videoplattformen.

  **Fortschrittsanzeige:** Bei längeren Vorgängen (Upload, Installation, Bezahlung) zeigt sie, dass etwas passiert und wie lange es noch dauert. Ein Balken, der am Anfang schneller läuft und am Ende langsamer, wirkt länger als einer, der sich am Ende beschleunigt (Harrison u. a., 2007, aus dem Gedächtnis, bitte prüfen).

  **Optimistische Oberfläche:** Das Herz wird sofort gefüllt, wenn man tippt. Der Server antwortet erst später. Geht etwas schief, wird die Änderung zurückgenommen und erklärt. Die Reaktion fühlt sich unmittelbar an, weil sie unter 0,1 Sekunden liegt.

  Frage zum Schluss: Wo warten Sie in Ihrer meistgenutzten App? Und was sehen Sie dabei?
---

'''+frame(f'''
<rect data-id="bar-bg" x="250" y="236" width="400" height="28" rx="14" fill="#e4e4e4" />
<rect data-id="bar" x="250" y="236" width="120" height="28" rx="14" fill="{B}" />''','Fortschritt zeigen: Es passiert etwas, und es dauert noch so lange')
   +frame(f'''
<rect data-id="bar-bg" x="250" y="236" width="400" height="28" rx="14" fill="#e4e4e4" />
<rect data-id="bar" x="250" y="236" width="300" height="28" rx="14" fill="{B}" />''','Fortschritt zeigen: Es passiert etwas, und es dauert noch so lange')
   +frame(f'''
<path data-id="herz" d="{HERZ}" fill="#ffffff" stroke="{B}" stroke-width="8" stroke-linejoin="round" />''','Optimistisch reagieren: Vor dem Tippen')
   +frame(f'''
<path data-id="herz" d="{HERZ}" fill="{L}" stroke="{L}" stroke-width="8" stroke-linejoin="round" />''','Sofort gefüllt. Der Server antwortet später.')+'''
{% question "Wo warten Sie in Ihrer meistgenutzten App?", "Und was sehen Sie, während Sie warten?" %}
''')

W(d,'090-fuehrt-zu.md','''
---
title: "Führt zu"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Scheinbewegung führt zur Gestaltpsychologie und zum Gesetz des gemeinsamen Schicksals: Was sich gemeinsam bewegt, gehört zusammen. Die gefühlte Wartezeit führt zu Feedback und Zuständen (laden, Fehler, Erfolg) und zur Frage, wofür Animation im Interface da ist.
---

{% statement "Führt zu", "[Gestaltpsychologie](../prinzip-gestaltpsychologie/), [Fortsetzung und Schicksal](../prinzip-fortsetzung-und-schicksal/), [Feedback und Zustände](../prinzip-feedback-und-zustaende/) und [Bewegung](../prinzip-bewegung/): Animation hat einen Zweck." %}
''')

done(d,'Zwei Reize kurz nacheinander werden als Bewegung gesehen, und Wartezeit wird nicht gemessen, sondern erlebt',
     'Scheinbewegung, Phi-Phänomen, Gefühlte Wartezeit, Doherty-Schwelle, Skeleton Screen')
