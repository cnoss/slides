exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'methode-schriftauswahl'
ALT = 'auswahl-von-schriften'
intro(D, 'Schriftauswahl', 'Methode // Konstruieren')
imgs(D, ALT, ['lineares-lesen-01.png.jpg', 'informierendes-lesen-01.png.jpg', 'konsultierendes-lesen-01.png.jpg', 'inszenierende-typo-02.png.jpg'])

GR = [('Serifenlos', 'Helvetica Neue', '400'), ('Serifen', 'Georgia', '400'), ('Serifenbetont', 'Rockwell', '400'), ('Monospace', 'Menlo', '400'), ('Schreibschrift', 'Snell Roundhand', '700')]
z = ''.join(f'<div style="display:flex;align-items:baseline;gap:50px;"><div style="width:330px;font-family:Helvetica Neue;font-size:32px;color:#888888;">{n}</div><div style="font-family:\'{f}\';font-weight:{w};font-size:96px;line-height:1.2;">Hamburgefonts</div></div>' for n, f, w in GR)
muster(D, 'schriftgruppen', f'<div style="display:flex;flex-direction:column;justify-content:center;gap:16px;width:1600px;height:900px;padding:0 120px;box-sizing:border-box;">{z}</div>')

W(D, '005-problem.md', kopf('Das Problem', '''
Allein Google Fonts bietet weit über tausend Schriftfamilien an, und dazu kommen die kommerziellen Anbieter. Wer sich dort durchscrollt, landet bei dem, was gerade gefällt oder gerade überall zu sehen ist.

Die Methode dreht das um: erst klären, was die Schrift leisten muss. Dann bleiben von tausend Schriften ein paar Kandidaten übrig, zwischen denen sich begründet entscheiden lässt. Die Begründung ist das eigentliche Ergebnis: Wer sie sagen kann, kann auch mit Auftraggebenden darüber sprechen.
''') + '''{% interlude "Über tausend Schriften.", "Welche nehmen Sie?" %}

{% statement "Erst der Zweck, dann die Schrift.", "Wer weiß, was die Schrift leisten muss, sucht nicht mehr nach Geschmack." %}
''')

F = 'font-family:IBM;'
W(D, '010-ergebnis.md', kopf('Ergebnis zuerst', '''
Das Ergebnis ist kein Schriftmuster, sondern eine Entscheidung mit Begründung. In den Übungen heißt das Typo-Fähnchen: der Name der Schrift und zwei bis drei Sätze, warum.

Das Beispiel ist das Labor NOXA Analytik mit seinem Kundenportal. Die Art des Lesens gibt die Anforderung vor (konsultierend: nachschlagen, vergleichen), die Wirkung kommt aus dem semantischen Differenzial (präzise, sachlich, aber nicht kalt). Die Praxis gibt den Rest: viele Schnitte, frei lizenziert.

Die Folie ist in IBM Plex Sans gesetzt. Die Schrift stammt von Mike Abbink und Bold Monday für IBM (2017) und steht unter der SIL Open Font License.
''') + live('IBM Plex Sans', f'<div style="{F}"><p style="{F}font-size:11vh;line-height:1.15;margin:0 0 .25em;text-align:left;">Il1 O0 · 0,03 mg/l</p><p style="{F}font-size:3.6vh;line-height:1.5;margin:0;text-align:left;max-width:62ch;hyphens:none;">Für das Kundenportal von NOXA Analytik: Hier wird nachgeschlagen und verglichen, also muss die Schrift auch klein und in Tabellen gut lesbar sein. I, l und 1 sind klar unterscheidbar. Die Anmutung ist technisch und präzise, die offenen Formen halten sie zugänglich. Viele Schnitte, frei lizenziert.</p></div>') + '\n')

W(D, '020-schritte.md', kopf('Schritte', '''
**1. Vorgaben klären:** Gibt es einen Styleguide? Dann ist die Frage oft schon beantwortet, und das ist in Ordnung. Sie gestalten nicht für sich.

**2. Art des Lesens bestimmen:** Wird fortlaufend gelesen, überflogen, nachgeschlagen, oder soll der Text vor allem wirken? Siehe nächste Folien.

**3. Wirkung festlegen:** am besten mit dem semantischen Differenzial.

**4. Kandidaten testen:** drei bis fünf Schriften, im echten Text, in den echten Größen, auf dem echten Gerät. Nicht mit dem Satz aus dem Schriftmuster, sondern mit Ihrem längsten Wort und Ihren Ziffern.

**5. Praxis prüfen und begründen:** Reichen die Schnitte? Gibt es alle Zeichen und Sprachen, die Sie brauchen? Was kostet die Lizenz, darf sie ins Web? Wie groß ist die Datei? Dann entscheiden und die Entscheidung aufschreiben.

**Hintergrund**

Die Arten des Lesens stammen aus Hans Peter Willberg und Friedrich Forssman, »Lesetypografie« (1997). Dort stehen acht Arten, wir verdichten sie hier auf vier: lineares, informierendes, konsultierendes Lesen und die inszenierende Typografie.
''') + liste('Schriftauswahl in fünf Schritten', [
  '<strong>1. Vorgaben klären:</strong> Gibt es einen Styleguide?',
  '<strong>2. Art des Lesens bestimmen:</strong> Wie wird der Text gelesen?',
  '<strong>3. Wirkung festlegen:</strong> mit dem semantischen Differenzial',
  '<strong>4. Kandidaten testen:</strong> im echten Text, in echter Größe, auf dem echten Gerät',
  '<strong>5. Praxis prüfen und begründen:</strong> Schnitte, Zeichen, Lizenz, Dateigröße',
]) + '\n')

W(D, '030-arten-des-lesens.md', kopf('Arten des Lesens', '''
Vier Arten des Lesens, jede mit einer eigenen Anforderung an die Schrift.

**Linear:** Man liest von vorn nach hinten, lange und ohne Sprünge, etwa einen Roman oder einen langen Artikel. Die Schrift soll nicht auffallen, Serifen oder ruhige serifenlose Schriften, nichts Extravagantes.

**Informierend:** Man überfliegt und steigt dort ein, wo es interessant wird: Zeitung, Nachrichtenseite, Ratgeber. Die Schrift braucht gut unterscheidbare Schnitte, damit Hierarchien entstehen.

**Konsultierend:** Man sucht etwas und liest nur das: Lexikon, Tabelle, Einstellungen, Dashboard. Die Schrift muss auch klein funktionieren, Ziffern und ähnliche Zeichen müssen sich klar unterscheiden.

**Inszenierend:** Der Text soll vor allem wirken: Plakat, Startseite, Kampagne. Hier darf die Schrift laut sein, weil sie wenig Text tragen muss.

Die meisten Screens mischen mehrere Arten. Deshalb arbeiten viele mit einer Schrift für die Inszenierung und einer für alles andere.

Bilder aus dem Bestand. Die Beispiele sind Printbeispiele, die Frage lässt sich aber auf jeden Screen übertragen.
''', transition='none') + bild('lineares-lesen-01.png.jpg', 'Linear: von vorn nach hinten. Die Schrift soll nicht auffallen') + '\n\n' + bild('informierendes-lesen-01.png.jpg', 'Informierend: überfliegen und einsteigen. Die Schrift braucht Schnitte für Hierarchien') + '\n\n' + bild('konsultierendes-lesen-01.png.jpg', 'Konsultierend: suchen und finden. Die Schrift muss auch klein funktionieren') + '\n\n' + bild('inszenierende-typo-02.png.jpg', 'Inszenierend: Der Text soll wirken. Die Schrift darf laut sein') + '\n')

W(D, '040-schriftgruppen.md', kopf('Schriftgruppen', '''
Fünf Gruppen reichen fürs Gespräch und für die Suche. In Google Fonts lässt sich genau danach filtern.

**Serifenlos** (Grotesk): sachlich, modern, der Standard im Interface. **Serifen** (Antiqua): traditionell, ruhig, gut für lange Texte. Dass Serifen die Lesbarkeit verbessern, ist übrigens nicht belegt, gewohnte Schriften lesen sich einfach besser. **Serifenbetont** (Slab Serif): kräftig, robust. **Monospace:** Jedes Zeichen ist gleich breit, gut für Code und Zahlen. **Schreibschrift:** persönlich, nur für große, kurze Texte.

**Hintergrund**

Es gibt ausführlichere Klassifikationen: die DIN 16518 (1964) mit elf Gruppen, die in den 1990er-Jahren überarbeitet werden sollte und nie ersetzt wurde, und die Matrix von Wolfgang Beinert. Beides brauchen Sie zum Nachschlagen, nicht für die tägliche Arbeit.
''') + bild('schriftgruppen.png', 'Fünf Gruppen reichen fürs Gespräch und für die Suche') + '\n')

W(D, '050-uebung.md', kopf('Mini-Übung', '''
**Mini-Übung (ca. 8 Minuten)**

Zu zweit, im Browser auf Google Fonts: Eine Schrift für einen der drei Fälle wählen. Erst Art des Lesens und zwei Adjektive für die Wirkung festlegen, dann suchen. Am Ende ein Satz Begründung. Zwei bis drei Paare stellen vor.

Die Fälle sind bewusst verschieden: Die Fahrplan-App ist konsultierend, das Festival inszenierend, das Magazin linear.
''') + '''{% question "Welche Schrift nehmen Sie?", "Eine Fahrplan-App, ein Musikfestival oder ein Online-Magazin für lange Texte. Zu zweit, acht Minuten, mit einem Satz Begründung." %}
''')

W(D, '060-fehler.md', kopf('Typische Fehler', '''
Der häufigste Fehler: Die Schrift wird am Überschriftenmuster ausgesucht und dann im Fließtext und in der Tabelle nie getestet. Der zweithäufigste: Es gibt nur Regular und Bold, und die Hierarchie braucht mehr.
''', cls='simple') + '''{% fragment '<p class="list">Nach Geschmack wählen und die Begründung nachreichen</p>' %}
{% fragment '<p class="list">Nur die Überschrift testen, nie den Fließtext und die Tabelle</p>' %}
{% fragment '<p class="list">Zu wenig Schnitte oder fehlende Zeichen erst am Ende bemerken</p>' %}
{% fragment '<p class="list">Die Lizenz vergessen: Darf die Schrift überhaupt ins Web?</p>' %}
{% fragment '<p class="list">Drei Schriften, wo eine gereicht hätte</p>' %}
''')

W(D, '070-einsatz.md', kopf('Einsatz', '''
Die Schriftauswahl steht am Anfang der visuellen Sprache, zusammen mit Moodboard und Farbklima. Tiefe: können. Sie kommt in den Übungen und im Projekt wieder, dort auch als Typo-Fähnchen oder im Entscheidungslog.

Schriftquellen: Google Fonts, Open Foundry, Fontshare, Adobe Fonts. Prüfhilfe für Paare: fontpair.co.
''') + liste('Wo die Methode wiederkommt', [
  'Am Anfang der visuellen Sprache, zusammen mit Moodboard und Farbklima',
  'In der Übung: als Typo-Fähnchen mit Begründung',
  'Im Projekt: im Entscheidungslog',
]) + '''

{% statement "Merksatz", "Erst der Zweck, dann die Wirkung, dann die Schrift. Und immer im echten Text testen." %}
''')
done(D, 'Schrift nach Zweck, Art des Lesens und Wirkung wählen, im echten Text testen und die Wahl begründen', 'Schriftauswahl, Arten des Lesens, Schriftgruppe, Schnitt, Typo-Fähnchen')
index(D, ['Ergebnis zuerst: Typo-Fähnchen', 'Fünf Schritte', 'Arten des Lesens', 'Schriftgruppen', 'Mini-Übung', 'Typische Fehler'], 'Am Anfang der visuellen Sprache')
print('fertig', D)
