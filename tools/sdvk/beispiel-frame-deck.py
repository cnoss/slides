exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
d='prinzip-naehe-und-abstand'
B='#231f20'
def dots(xs, ys):
    out=[]; i=0
    for y in ys:
        for x in xs:
            out.append(f'  <circle data-id="p{i}" cx="{x}" cy="{y}" r="16" fill="{B}" />'); i+=1
    return '\n'.join(out)
def frame(content, bu, extra=''):
    return "{% frame '{\"bu\":\""+bu+"\""+extra+"}' %}\n"+content+"\n{% endframe %}\n"
W(d,'010-regel.md','''
---
title: Nähe
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Gesetz der Nähe, Max Wertheimer 1923. Eines der stärksten Gruppierungsprinzipien. Quellen: Lidwell, Universal Principles of Design (Proximity); Yablonski, Laws of UX (Law of Proximity).
---

{% statement "Was nah beieinander steht, gehört zusammen.", "Gesetz der Nähe" %}
''')
even=[180,260,340,420]
W(d,'020-abstrakt.md','''
---
title: Nähe abstrakt
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Dieselben 16 Punkte, nur die Abstände ändern sich. Erst gleichmäßig: ein Feld. Dann Spalten, dann Zeilen. Fragen: Was sehen Sie jetzt? Wie viele Gruppen?
---

'''+frame(dots(even,even),'Gleiche Abstände: ein Feld')
   +frame(dots([150,210,390,450],even),'Spalten rücken zusammen: zwei Gruppen')
   +frame(dots(even,[150,210,390,450]),'Zeilen rücken zusammen: wieder zwei Gruppen, ganz andere'))
W(d,'030-abstand.md','''
---
title: Abstand zeigt Beziehung
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Anwendung im Interface: Abstände sind keine Restgröße, sie tragen Bedeutung. Was zusammengehört, steht näher zusammen als das, was trennt. Quelle: Wathan & Schoger, Refactoring UI (Avoid ambiguous spacing).
---

{% statement "Innen enger als außen.", "Was zusammengehört, steht näher beieinander als das, was trennt." %}
''')
def form(lab, fld):
    out=[]
    for i,(ly,fy) in enumerate(zip(lab,fld)):
        out.append(f'  <rect data-id="l{i}" x="150" y="{ly}" width="110" height="12" fill="#888888" />')
        out.append(f'  <rect data-id="f{i}" x="150" y="{fy}" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />')
    out.append(f'  <rect data-id="btn" x="150" y="{fld[-1]+90}" width="120" height="40" rx="20" fill="#9313ce" />')
    return '\n'.join(out)
W(d,'040-formular.md','''
---
title: Formular
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Ein Formular als Wireframe. Grau: Beschriftung, Rahmen: Eingabefeld, Lila: Absenden. Links sind alle Abstände gleich: Gehört die Beschriftung zum Feld darüber oder darunter? Rechts ist nur der Abstand verändert, sonst nichts.
---

'''+frame(form([90,214,338],[138,262,386]),'Gleiche Abstände: Gehört die Beschriftung zum Feld darüber oder darunter?')
   +frame(form([90,224,358],[110,244,378]),'Innen enger als außen: Beschriftung und Feld bilden eine Gruppe'))
W(d,'050-im-screen.md','''
---
title: Im Screen
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Mini-Übung, 3 Minuten zu zweit. Erwartbar: Karten in Feeds, Einstellungen in Gruppen, Formulare, Navigation. Und Gegenbeispiele, wo Abstände nichts sagen.
---

{% question "Öffnen Sie eine App Ihrer Wahl.", "Wo zeigt der Abstand, was zusammengehört? Und wo nicht?" %}
''')
W(d,'060-grenzen.md','''
---
title: Grenzen
layout: presentation.11ty.js
slideClasses: wrap
status: ok
---

{% statement "Wann gilt das nicht?", "Ein gemeinsamer Rahmen oder eine Verbindungslinie schlägt Nähe. Und wenn alles nah ist, gibt es keine Gruppen: Ohne Weißraum keine Nähe." %}
''')
W(d,'070-verweise.md','''
---
title: Verweise
layout: presentation.11ty.js
slideClasses: simple
status: ok
---

{% fragment '<p class="list"><strong>Prinzipien:</strong> Ähnlichkeit, Geschlossenheit und Region, Weißraum</p>' %}
{% fragment '<p class="list"><strong>Methoden:</strong> Spacing-System, Unschärfetest</p>' %}
''')
done(d,'Was nah beieinander steht, gehört zusammen. Innen enger als außen','Gesetz der Nähe, Gruppierung, Weißraum')
