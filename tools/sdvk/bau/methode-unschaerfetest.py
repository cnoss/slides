exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
D = 'methode-unschaerfetest'

intro(D, 'Unschärfe- und Graustufentest', 'Methode // Testen und Prüfen')

# Unscharf und grau per CSS. Die Unschärfe hängt an der Viewport-Breite, damit sie auf jedem Beamer gleich stark wirkt.
# Beim kleinen Bild auf der Ergebnisfolie halb so stark (0.35vw), sonst ist es zu verwaschen.
UNSCHARF = 'filter:blur(0.7vw) grayscale(1);'

def unscharf(img, bu, transition='fade'):
    return f'''<section class="image screenshot shadow" data-transition="{transition}" data-background-transition="fade"><figure><img src="{img}" alt="Screenshot, unscharf und in Graustufen" style="{UNSCHARF}"><figcaption class="bu"><p>{bu}</p></figcaption></figure></section>'''

# ---------------------------------------------------------------- Problem
W(D, '005-problem.md', '''
---
title: "Das Problem"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Wer einen Entwurf gebaut hat, kennt jedes Element. Man liest die Headline, weil man weiß, dass sie da ist, und findet den Button, weil man ihn selbst gesetzt hat. Was ein fremder Blick zuerst sieht, kann man am eigenen Entwurf kaum noch beurteilen.

  Der Test nimmt dem Auge die Details: Ohne lesbaren Text und ohne Farbe bleibt nur, was wirklich Gewicht hat. Größe, Helligkeit, Fläche, Position. Genau das bestimmt die Hierarchie.

  Die Methode verbindet zwei Prüfungen: unscharf (Was hat Gewicht, wenn man nichts lesen kann?) und grau (Trägt die Hierarchie auch ohne Farbe? Farben gleicher Helligkeit verschmelzen in Grau, siehe Farbe und Lesbarkeit).

  **Hintergrund**

  Der Unschärfetest ist eine alte Praxis aus Grafikdesign und Malerei: Augen zusammenkneifen (»squint test«) oder ein paar Schritte zurücktreten. Wathan und Schoger empfehlen in »Refactoring UI« (2018, Kapitel »Starting from Scratch«), zuerst in Graustufen zu gestalten: Wer Hierarchie ohne Farbe hinbekommt, braucht Farbe nur noch als Ergänzung. Der Graustufenschritt ist derselbe wie in der Methode Kontrast prüfen.
---

{% interlude "Sie kennen Ihren Entwurf zu gut.", "Was sieht jemand, der ihn zum ersten Mal sieht?" %}

{% statement "Unscharf und grau bleibt nur, was Gewicht hat.", "Ohne lesbaren Text und ohne Farbe zählen Größe, Helligkeit, Fläche und Position. Das ist Ihre Hierarchie." %}
''')

# ---------------------------------------------------------------- Ergebnis zuerst
W(D, '010-ergebnis.md', f'''
---
title: "Ergebnis zuerst"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Startseite von Duolingo (2026), erst scharf, dann unscharf und grau. Das Ergebnis des Tests ist eine Rangfolge: Was sehe ich zuerst, was als Zweites, was als Drittes? Und der Abgleich mit dem Ziel der Seite.

  Ziel der Seite: Menschen sollen anfangen. Ergebnis: Die bunte Illustration hat das meiste Gewicht, dann folgt der Button, dann die Headline. In Farbe springt der grüne Button stärker heraus. In Grau verliert er, weil sein Grün kaum dunkler ist als ein mittleres Grau. Die Hierarchie trägt hier also zu einem guten Teil über Farbe. Für die meisten passt das, für Menschen mit Farbsehschwäche oder auf einem schlechten Display weniger.

  Das ist kein Urteil über Duolingo, sondern zeigt, was der Test sichtbar macht.
---

{{% screenshot "./images/test-duolingo.jpg", '{{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Scharf und farbig<br><small>de.duolingo.com, Screenshot 2026</small>"}}' %}}

<section class="simple" data-transition="none">
  <div>
    <h1>Unscharf und grau</h1>
    <div style="display:flex; gap:3vw; align-items:center; width:100%;">
      <figure style="flex:3; margin:0;"><img src="./images/test-duolingo.jpg" alt="Startseite von Duolingo, unscharf und in Graustufen" style="width:100%; height:auto; box-shadow:0 0 1.5rem rgba(0,0,0,.2); filter:blur(0.35vw) grayscale(1);"></figure>
      <div style="flex:2;">
        <p class="list"><strong>1.</strong> Illustration</p>
        <p class="list"><strong>2.</strong> Button »Anfangen«</p>
        <p class="list"><strong>3.</strong> Headline</p>
        {{% fragment '<p><strong>Ziel:</strong> anfangen. Der Button trägt, aber vor allem über Farbe.</p>' %}}
      </div>
    </div>
  </div>
</section>
''')

# ---------------------------------------------------------------- Schritte
W(D, '020-schritte.md', '''
---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **1. Screenshot:** der ganze Screen in Originalgröße, mit echten Inhalten, nicht mit Lorem ipsum. Bilder gehören dazu, sie verändern die Hierarchie oft am stärksten.

  **2. Unscharf machen:** so stark, dass man keinen Text mehr lesen kann. In Figma: Screenshot oder Frame kopieren, Effekt »Layer Blur«, Wert etwa 8 bis 16. Ohne Werkzeug: Augen zusammenkneifen oder zwei, drei Meter zurücktreten.

  **3. Grau stellen:** In Figma ein schwarzes Rechteck mit dem Ebenenmodus »Color« über den Frame legen (wie bei Kontrast prüfen). Am Mac für den ganzen Bildschirm: Systemeinstellungen, Bedienungshilfen, Anzeige, Farbfilter, Graustufen.

  **4. Reihenfolge notieren:** 1, 2, 3. Was sehen Sie zuerst? Besser noch: jemand anderen fragen, der den Entwurf nicht kennt.

  **5. Abgleichen und korrigieren:** Passt die Reihenfolge zum Gestaltungsziel? Wenn nicht, mit Größe, Helligkeit, Weißraum und Position nachsteuern. Oft reicht es, das Konkurrierende zurückzunehmen (Betonen durch Zurücknehmen). Danach erneut testen.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>In fünf Schritten</h1>
    {% fragment '<p class="list"><strong>1. Screenshot:</strong> ganzer Screen, echte Inhalte</p>' %}
    {% fragment '<p class="list"><strong>2. Unscharf machen:</strong> bis kein Text mehr lesbar ist</p>' %}
    {% fragment '<p class="list"><strong>3. Grau stellen:</strong> Farbe weg, Helligkeit bleibt</p>' %}
    {% fragment '<p class="list"><strong>4. Reihenfolge notieren:</strong> Was sehen Sie zuerst, als Zweites, als Drittes?</p>' %}
    {% fragment '<p class="list"><strong>5. Abgleichen und korrigieren:</strong> Passt das zum Ziel? Dann erneut testen.</p>' %}
  </div>
</section>

<section class="simple" data-transition="fade">
<div>

# Werkzeuge

| Schritt | In Figma | Ohne Werkzeug |
|---|---|---|
| **Unscharf** | Effekt »Layer Blur«, etwa 8 bis 16 | Augen zusammenkneifen, zurücktreten |
| **Grau** | schwarze Fläche, Ebenenmodus »Color« | Mac: Bedienungshilfen, Farbfilter, Graustufen |

</div>
</section>
''')

# ---------------------------------------------------------------- Mini-Übung
uebung = [('uebung-netflix.jpg', 'A', 'netflix.com/de, Screenshot 2026'),
          ('uebung-ikea.jpg', 'B', 'ikea.com/de, Screenshot 2026'),
          ('uebung-thkoeln.jpg', 'C', 'th-koeln.de, Screenshot 2026')]
blind = '\n\n'.join(unscharf(f'./images/{f}', f'Screen {k}: Was sehen Sie zuerst, als Zweites, als Drittes?') for f, k, q in uebung)
scharf = '\n\n'.join(
    f'''{{% screenshot "./images/{f}", '{{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Screen {k}: Stimmt Ihre Reihenfolge? Und passt sie zum Ziel der Seite?<br><small>{q}</small>"}}' %}}'''
    for f, k, q in uebung)

W(D, '030-uebung.md', f'''
---
title: "Mini-Übung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Mini-Übung (ca. 10 Minuten)**

  Drei Screens, erst unscharf und grau. Zu zweit für jeden Screen die Rangfolge 1, 2, 3 notieren, je etwa eine Minute. Danach die Auflösung scharf und in Farbe. Diskussion: Was ist das Ziel der Seite? Passt die Rangfolge dazu?

  Erwartbar (aus dem eigenen Test, bitte live gegenprüfen):

  - **A, Netflix:** 1. Headline, 2. Eingabe und Button, 3. Login oben rechts. Das dunkle Plakatraster tritt zurück. Ziel ist die Anmeldung, das passt. Der rote Button verliert in Grau deutlich, hier trägt die Headline.
  - **B, IKEA:** 1. das große Foto links, 2. die dunklen Teaser rechts, 3. die Headline »Willkommen«. Die Fotos dominieren. Gewollt? Für einen Shop, der inspirieren will, vielleicht ja.
  - **C, TH Köln:** 1. das dunkle Foto im Slider, 2. die Kästen darunter, 3. Logo und Navigation. Die farbigen Kästen (Rot, Pink) verlieren in Grau ihre Kraft und konkurrieren miteinander. Gute Diskussion: Was soll man auf der Hochschulseite zuerst sehen?

  **Alternative:** Statt der drei Screens das eigene Ergebnis aus dem letzten Workshop testen und mit der Nachbarin oder dem Nachbarn tauschen.
---

{{% interlude "Und jetzt Sie.", "Drei Screens, zu zweit, zehn Minuten" %}}

{blind}

{{% statement "Auflösung", "Jetzt scharf und in Farbe. Stimmt Ihre Reihenfolge? Was will die Seite, und kommt das an?" %}}

{scharf}

{{% question "Und Ihr eigener Entwurf?", "Testen Sie Ihr Ergebnis aus dem Workshop. Am besten mit jemandem, der es noch nicht kennt." %}}
''')

# ---------------------------------------------------------------- Typische Fehler
W(D, '040-fehler.md', '''
---
title: "Typische Fehler"
layout: presentation.11ty.js
slideClasses: simple
status: ok
speaker: |
  Der häufigste Fehler: zu wenig Unschärfe. Solange man noch Wörter erkennt, liest man, statt zu sehen, und der Test misst nichts.

  Der zweithäufigste: Fotos. Ein großes Bild mit viel Kontrast schlägt fast jede Headline, das merkt man scharf oft nicht, weil man den Text liest. Unscharf ist es sofort sichtbar.

  Und: Farbe für Hierarchie halten. Zwei Farben, die nebeneinander laut wirken, können gleich hell sein und verschmelzen in Grau. Wer nur unscharf, aber nicht grau testet, übersieht das.
---

{% fragment '<p class="list">Zu wenig Unschärfe: Wer noch lesen kann, sieht nicht</p>' %}
{% fragment '<p class="list">Den eigenen Entwurf im Kopf mitlesen, statt jemand anderen zu fragen</p>' %}
{% fragment '<p class="list">Fotos übersehen: Große Bilder schlagen fast jede Headline</p>' %}
{% fragment '<p class="list">Nur unscharf, nicht grau: Hierarchie, die nur über Farbe läuft, bleibt unentdeckt</p>' %}
{% fragment '<p class="list">Reihenfolge notieren, aber nicht mit dem Ziel abgleichen</p>' %}
{% fragment '<p class="list">Nur einmal testen, ganz am Ende</p>' %}
''')

# ---------------------------------------------------------------- Einsatz
W(D, '050-einsatz.md', '''
---
title: "Einsatz"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Der Unschärfe- und Graustufentest ist eine Können-Methode. Er dauert eine Minute und kehrt immer wieder: in jedem Workshop vor dem Upload, im Crit als erste Frage (»Was sehen Sie unscharf zuerst?«), im Projekt für jeden Screen, besonders für Startseiten und Formulare. In der Typografie prüft er Lesestufen und Grauwert, im Layout das Gleichgewicht.

  Verwandt: Kontrast prüfen (Graustufenschritt), 5-Sekunden-Test (was bleibt hängen?), Prinzip Hierarchie.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wo die Methode wiederkommt</h1>
    {% fragment '<p class="list">Im Workshop: jedes Ergebnis vor dem Upload</p>' %}
    {% fragment '<p class="list">Im Crit: »Was sehen Sie unscharf zuerst?«</p>' %}
    {% fragment '<p class="list">Im Projekt: jeder Screen, vor allem Startseite und Formulare</p>' %}
    {% fragment '<p class="list">In Typografie und Layout: Lesestufen, Grauwert, Gleichgewicht</p>' %}
  </div>
</section>

{% statement "Merksatz", "Unscharf und grau: Was dann noch zuerst auffällt, ist Ihre Hierarchie. Passt sie zum Ziel? Siehe [Hierarchie](../prinzip-hierarchie/) und [Kontrast prüfen](../methode-kontrast-pruefen/)." %}
''')

done(D, 'Unscharf und grau bleibt nur, was Gewicht hat: Hierarchie ohne Details und ohne Farbe prüfen und mit dem Ziel abgleichen',
     ['Unschärfetest', 'Graustufentest', 'Squint-Test', 'Rangfolge'])
