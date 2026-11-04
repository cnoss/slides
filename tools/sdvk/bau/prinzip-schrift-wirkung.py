exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'prinzip-schrift-wirkung'
intro(D, 'Wirkung von Schrift', 'Prinzip // Wirken')

SCHRIFTEN = [('Helvetica Neue', '500'), ('Didot', '400'), ('Menlo', '400'), ('Futura', '700'), ('Chalkboard SE', '400'), ('Snell Roundhand', '700')]
def raster(text, gr=62):
    z = ''.join(f'<div style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;padding:0 40px;">'
                f'<div style="font-family:\'{f}\';font-weight:{w};font-size:{gr}px;line-height:1.15;white-space:nowrap;">{text}</div>'
                f'<div style="font-family:Helvetica Neue;font-size:22px;color:#888888;margin-top:16px;">{f}</div></div>' for f, w in SCHRIFTEN)
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr 1fr;width:1600px;height:860px;padding:20px 0;">{z}</div>'
muster(D, 'botschaft', raster('Wir sind für Sie da.'))
muster(D, 'noxa', raster('NOXA Analytik'))
def paar(a, fa, wa, b, fb, wb):
    bl = lambda t, f, w: f'<div style="flex:1;display:flex;align-items:center;justify-content:center;font-family:\'{f}\';font-weight:{w};font-size:92px;text-align:center;line-height:1.15;padding:0 30px;">{t}</div>'
    return f'<div style="display:flex;width:1600px;height:900px;">{bl(a, fa, wa)}{bl(b, fb, wb)}</div>'
muster(D, 'unpassend', paar('Ihre Diagnose', 'Comic Sans MS', '400', 'Kinder&shy;geburtstag', 'Didot', '400'))
def artikel(hf, hw, tf, tcol='#231f20'):
    t = 'Am Samstag öffnet die neue Stadtbibliothek ihre Türen. Auf drei Etagen warten Bücher, Lernplätze und ein Café. Der Eintritt ist frei, der Ausweis kostet nichts.'
    return (f'<div style="display:flex;flex-direction:column;justify-content:center;width:1600px;height:900px;padding:0 240px;box-sizing:border-box;">'
            f'<div style="font-family:\'{hf}\';font-weight:{hw};font-size:92px;line-height:1.1;margin-bottom:40px;">Lesen ohne Grenzen</div>'
            f'<div style="font-family:{tf};font-size:40px;line-height:1.45;color:{tcol};">{t}</div></div>')
muster(D, 'mischen-familie', artikel('Helvetica Neue', '700', "'Helvetica Neue'"))
muster(D, 'mischen-kontrast', artikel('Didot', '400', "'Helvetica Neue'"))
muster(D, 'mischen-aehnlich', artikel('Georgia', '400', "'Times New Roman'"))
muster(D, 'mischen-zufall', artikel('Snell Roundhand', '700', "'Chalkboard SE'"))

W(D, '010-regel.md', kopf('Wirkung von Schrift', '''
Die Regel: Schrift spricht mit. Noch bevor jemand ein Wort gelesen hat, hat die Schrift schon einen Ton gesetzt: sachlich oder verspielt, teuer oder billig, alt oder neu.

Das ist derselbe Mechanismus wie bei Farbe und Form: Wirkung lässt sich nicht vermeiden, nur gestalten. Es gibt keine neutrale Schrift. Auch Helvetica wirkt, nämlich sachlich.

**Hintergrund**

Ellen Lupton beschreibt in »Thinking with Type« (2. Auflage 2010), Kapitel »Letter«, wie Schriften ihre Herkunft und Haltung mittragen. Jan Tschichold, Max Bill, Otl Aicher: Der Streit darüber, welche Schrift welche Haltung ausdrückt, ist so alt wie die moderne Typografie.
''') + '''{% interlude "Schrift spricht mit.", "Noch bevor jemand ein Wort gelesen hat." %}
''')

W(D, '020-variiert.md', kopf('Dieselbe Botschaft', '''
Derselbe Satz, sechs Schriften. Fragen: Wer sagt das jeweils? Eine Bank, eine Kita, ein Bestattungsinstitut, eine Hotline? Die Antworten sind sich meist erstaunlich einig.

Dann ein Name, den Sie schon kennen: das Labor NOXA Analytik. Jetzt kommt das semantische Differenzial wieder ins Spiel: Per Handzeichen abstimmen (ein bis fünf Finger), welche Schrift auf den beiden Skalen wo liegt. Damit wird aus »passt irgendwie nicht« eine Aussage.

Kleiner Abstecher, wenn Zeit ist: Der Link in der Bildunterschrift öffnet das Kerning Lab mit »NOXA Analytik«. Dort lassen sich die Abstände zwischen den Buchstabenpaaren live einstellen, etwa zwischen A und n oder zwischen l und y.

Zum Schluss das Gegenteil: Schrift und Inhalt beißen sich. Das ist nicht falsch im Sinne von unlesbar, aber es sendet ein Signal, das niemand wollte.

Die Muster sind mit Systemschriften gesetzt. Comic Sans ist nicht grundsätzlich schlecht: Für Menschen mit Leseschwäche wird sie teils als gut lesbar beschrieben. Sie ist hier nur falsch am Platz.
''', transition='none') + bild('botschaft.png', 'Wer sagt das? Dieselbe Botschaft in sechs Schriften') + '\n\n' + bild('noxa.png', 'Welche passt zu einem Labor für Spurenanalytik?<br><small>Kerning selbst ausprobieren: [Kerning Lab mit »NOXA Analytik«](https://cnoss.github.io/kerning-lab/#t=NOXA%20Analytik)</small>') + '''

{% question "Wo liegen die sechs Schriften?", "Sachlich gegen verspielt, traditionell gegen modern. Ein bis fünf Finger." %}

''' + bild('unpassend.png', 'Schrift und Inhalt beißen sich') + '\n')

W(D, '030-mischen.md', kopf('Schriften mischen', '''
Wer zwei Schriften mischt, braucht einen Grund. Die Regel: Kontrast oder Verwandtschaft, aber kein Zufall.

1. **Eine Familie:** Die sicherste Lösung. Bold und Regular derselben Schrift reichen für die meisten Screens.
2. **Deutlicher Kontrast:** Zwei Familien, die sich klar unterscheiden, etwa eine Serifenschrift für die Überschrift und eine serifenlose für den Text. Der Unterschied muss wie Absicht aussehen.
3. **Zu ähnlich:** Zwei ähnliche Schriften wirken wie ein Versehen. Das ist der häufigste Fehler und fällt erst auf den zweiten Blick auf: Es stimmt etwas nicht, und man weiß nicht, was.
4. **Zufall:** Zwei Schriften, die jede für sich laut sind, streiten miteinander.

Faustregel: höchstens zwei Familien. Hilfe bei der Suche: fontpair.co, Google Fonts (Rubrik »Pairings« auf den Schriftseiten).
''', transition='none') + '''{% statement "Kontrast oder Verwandtschaft.", "Aber kein Zufall. Und höchstens zwei Familien." %}

''' + bild('mischen-familie.png', 'Eine Familie: Bold und Regular. Immer sicher') + '\n\n' + bild('mischen-kontrast.png', 'Zwei Familien mit deutlichem Kontrast: Absicht', 'none') + '\n\n' + bild('mischen-aehnlich.png', 'Zu ähnlich: wirkt wie ein Versehen', 'none') + '\n\n' + bild('mischen-zufall.png', 'Beide laut: Sie streiten miteinander', 'none') + '\n')

W(D, '040-im-screen.md', kopf('Im Screen', '''
Zwei Screens, zwei Tonlagen. Die Tagesschau setzt auf eine ruhige, gut lesbare Schrift, die Sachlichkeit und Verlässlichkeit ausstrahlt. Duolingo nutzt eine runde, freundliche Schrift mit kräftigen Schnitten: Lernen soll sich wie ein Spiel anfühlen.

Die Frage ans Publikum: Tauschen Sie gedanklich die Schriften. Was passiert? Eine Nachricht über ein Unglück in der runden Schrift wäre kaum auszuhalten.

Screenshots: tagesschau.de und de.duolingo.com, jeweils 2026.
''') + bild('wirkung-tagesschau.jpg', 'Sachlich und verlässlich<br><small>tagesschau.de, Screenshot 2026</small>', schatten=True) + '\n\n' + bild('wirkung-duolingo.jpg', 'Rund und freundlich<br><small>de.duolingo.com, Screenshot 2026</small>', schatten=True) + '''

{% question "Was passiert, wenn Sie die Schriften tauschen?", "Und wie wirkt die Schrift in Ihrer meistgenutzten App?" %}
''')

W(D, '050-grenzen.md', kopf('Grenzen', '''
**Wirkung schlägt Lesbarkeit nie:** Eine Schrift mit toller Ausstrahlung, die man nicht lesen kann, hilft niemandem. Für Fließtext gilt zuerst Lesbarkeit, Ausdruck darf vor allem in großen Größen stattfinden.

**Wirkung ist gelernt:** Sie hängt von Kultur, Generation und Kontext ab. Fraktur galt lange als deutsch und traditionell, ist heute auch Heavy-Metal-Schrift. Deshalb prüfen statt behaupten: mit dem semantischen Differenzial und mit Menschen aus der Zielgruppe.

**Systemschriften sind keine Niederlage:** In Werkzeugen und dichten Oberflächen ist die Schrift des Betriebssystems oft die richtige Wahl. Sie lädt sofort, ist vertraut und zieht keine Aufmerksamkeit auf sich.
''') + liste('Wann trägt die Wirkung nicht?', [
  'Wenn sie die Lesbarkeit kostet: Für Fließtext gilt zuerst Lesbarkeit.',
  'Wenn sie nur behauptet ist: Wirkung ist gelernt, also prüfen.',
  'Wenn Zurückhaltung das Ziel ist: Systemschriften sind keine Niederlage.',
]) + '\n')

W(D, '060-verweise.md', kopf('Verweise', '''
Auswählen mit der Methode Schriftauswahl. Prüfen mit dem semantischen Differenzial. Verwandt: Farbwirkung, Formsemantik.
''') + '''{% statement "Verweise", "Auswählen: [Schriftauswahl](../methode-schriftauswahl/). Prüfen: [Semantisches Differenzial](../methode-semantisches-differential/). Verwandt: [Farbwirkung](../prinzip-farbwirkung/), [Formsemantik](../prinzip-formsemantik/)." %}
''')
done(D, 'Schrift spricht mit: Dieselbe Botschaft wirkt in jeder Schrift anders. Beim Mischen gilt Kontrast oder Verwandtschaft, aber kein Zufall', 'Schriftwirkung, Schriftmischung, Schriftfamilie, Schnitt')
index(D, ['Schrift hat Ausstrahlung', 'Schriften mischen', 'Tonlagen im Screen'])
print('fertig', D)
