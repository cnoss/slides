exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'prinzip-satz'
intro(D, 'Satz', 'Prinzip // Lesbar machen')
def block(st, ch=32, gr=3.1):
    return f'<p lang="de" style="font-family:PTserif;font-size:{gr}vh;line-height:1.45;max-width:{ch}ch;width:100%;margin:0;{st}">{KURZ}</p>'
def zwei(a, b, la, lb):
    k = lambda x, l: f'<div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">{l}</p>{x}</div>'
    return f'<div style="display:flex;gap:4vw;align-items:flex-start;width:100%;">{k(a, la)}{k(b, lb)}</div>'

W(D, '010-regel.md', kopf('Satz', '''
Die Regel: Die Satzart folgt der Textmenge. Lange Texte brauchen einen festen Zeilenanfang, damit die Augen zurückfinden. Kurze Texte dürfen freier gesetzt werden.

**Hintergrund**

Satz ist das alte Wort für das Anordnen von Text, aus der Zeit, als Text tatsächlich aus Bleilettern gesetzt wurde. Die Regeln dazu: Lupton, »Thinking with Type« (2. Auflage 2010), Kapitel »Text«; Willberg und Forssman, »Lesetypografie« (1997).

Die Beispiele auf den folgenden Folien sind echter Text, gesetzt vom Browser. Was Sie sehen, ist das, was auch auf Ihrer Website passiert.
''') + '''{% interlude "Die Satzart folgt der Textmenge.", "Langer Text braucht einen festen Zeilenanfang." %}
''')

W(D, '020-satzarten.md', kopf('Satzarten', '''
**Linksbündig (Flattersatz):** Der Standard am Screen. Fester Zeilenanfang, gleichmäßige Wortabstände. Der rechte Rand darf unruhig sein.

**Blocksatz ohne Silbentrennung:** Damit beide Ränder bündig werden, verteilt der Browser den Platz auf die Wortabstände. Es entstehen Löcher und »Gassen«, der Grauwert leidet. Vor allem in schmalen Spalten und auf dem Handy.

**Blocksatz mit Silbentrennung:** `hyphens: auto` mit gesetzter Sprache im Attribut `lang` hilft viel, braucht aber genug Breite. Am Screen weiß man nie genau, wie breit die Spalte wird, deshalb bleibt es riskant.

**Zentriert:** Jede Zeile beginnt woanders, die Augen müssen den Anfang jedes Mal suchen. Nur für Kurzes: eine Überschrift, ein Zitat, zwei bis drei Zeilen.

**Rechtsbündig:** Nur für Ausnahmen, etwa Zahlen in Tabellen oder eine kurze Bildunterschrift.
''') + live('Linksbündig gegen Blocksatz', zwei(block('text-align:left;hyphens:none;'), block('text-align:justify;hyphens:none;'), 'Linksbündig: gleichmäßige Wortabstände', 'Blocksatz ohne Trennung: Löcher')) + '\n\n' + live('Silbentrennung hilft', zwei(block('text-align:justify;hyphens:none;'), block('text-align:justify;hyphens:auto;'), 'Blocksatz ohne Trennung', 'Blocksatz mit <code>hyphens: auto</code>'), 'none') + '\n\n' + live('Zentriert: nur für Kurzes', zwei(block('text-align:center;hyphens:none;'), f'<p style="font-family:PTserif;font-size:5vh;line-height:1.3;margin:0;text-align:center;hyphens:none;">Typografie ist Auswählen, Gliedern, Anordnen und Lesbarmachen.</p>', 'Langer Text: Der Zeilenanfang fehlt', 'Kurzer Text: kein Problem'), 'none') + '''

{% statement "Am Screen: linksbündig.", "Blocksatz braucht Silbentrennung und viel Breite. Zentriert nur für Kurzes." %}
''')

P = 'font-family:PTserif;font-size:3.1vh;line-height:1.45;margin:0;text-align:left;max-width:34ch;hyphens:none;'
TA = 'Am Zeilenende springen die Augen zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie ihn schlecht wieder.'
TB = 'Ist sie zu kurz, reißt der Lesefluss ständig ab. Steht die nächste Zeile zu dicht darunter, rutschen die Augen ab.'
W(D, '030-absaetze.md', kopf('Absätze', '''
Absätze gliedern den Text in Sinnschritte. Zwei Mittel stehen zur Wahl: Abstand oder Einzug. Beides zugleich ist doppelt gemoppelt.

Am Screen ist der Abstand üblich: etwa eine halbe bis eine ganze Zeile. Der Einzug kommt aus dem Buch, wo Platz gespart werden musste.

Im CSS: `p + p { margin-top: 1em; }`, keine leeren Absätze.

Überschriften gehören zu dem, was folgt: Der Abstand nach oben ist größer als der nach unten. Das ist Nähe.
''') + live('Abstand oder Einzug', zwei(f'<p style="{P}margin-bottom:1em;">{TA}</p><p style="{P}">{TB}</p>', f'<p style="{P}">{TA}</p><p style="{P}text-indent:1.5em;">{TB}</p>', 'Abstand: üblich am Screen', 'Einzug: üblich im Buch')) + '\n')

H = 'font-family:PTsans;font-weight:700;font-size:5.4vh;line-height:1.15;margin:0;text-align:left;max-width:20ch;hyphens:none;'
W(D, '040-umbrueche.md', kopf('Umbrüche', '''
**Hurenkind:** die letzte Zeile eines Absatzes allein oben auf einer neuen Seite oder Spalte. **Schusterjunge:** die erste Zeile eines Absatzes allein unten. Merksatz aus dem Bleisatz: Ein Hurenkind weiß nicht, wo es herkommt, ein Schusterjunge nicht, wo er hingeht. Die Begriffe sind alt und nicht besonders schön, Sie werden ihnen trotzdem begegnen. Auf Englisch: widow und orphan.

Am Screen gibt es selten Seiten, das Problem verschiebt sich: Spalten und Karten haben Umbrüche, und im Fließtext steht gern ein einzelnes Wort in der letzten Zeile.

In CSS gibt es dafür Werkzeuge: `orphans` und `widows` für Umbrüche in Spalten und beim Druck, `text-wrap: balance` für Überschriften (die Zeilen werden gleich lang) und `text-wrap: pretty` für Fließtext (kein einsames letztes Wort). Früher hat man das von Hand mit festen Umbrüchen gelöst, die dann auf dem nächsten Gerät falsch saßen.
''') + live('Überschriften ausbalancieren', zwei(f'<p style="{H}">Die Bibliothek zieht im Frühjahr in den alten Bahnhof um</p>', f'<p style="{H}text-wrap:balance;">Die Bibliothek zieht im Frühjahr in den alten Bahnhof um</p>', 'Automatisch', '<code>text-wrap: balance</code>')) + '''

{% statement "Einsame Zeilen stören.", "Im Druck heißen sie Hurenkind und Schusterjunge. Am Screen hilft CSS: text-wrap, widows, orphans." %}
''')

W(D, '050-im-screen.md', kopf('Frage', '''
Frage ans Publikum, am eigenen Handy: Suchen Sie eine Seite mit Blocksatz oder zentriertem Fließtext. Beides findet sich schnell, etwa auf den Seiten von Vereinen, Praxen und Restaurants. Was fällt beim Lesen auf?
''') + '''{% question "Finden Sie Blocksatz auf dem Handy?", "Eine Vereinsseite, eine Praxis, ein Restaurant. Wie liest sich das?" %}
''')

W(D, '060-grenzen.md', kopf('Grenzen', '''
**Blocksatz kann gut sein:** Im Buch und in Zeitungen funktioniert er, weil Menschen dort jede Zeile von Hand oder mit starken Satzprogrammen ausgleichen. Browser können das bisher schlechter, auch wenn sie aufholen.

**Zentriert kann richtig sein:** Eine Startseite mit wenig Text, eine Einladung, ein Dialog mit einem Satz. Die Frage ist immer die Länge.

**Sprachen:** Rechts-nach-links-Schriften wie Arabisch und Hebräisch setzen rechtsbündig, und das ist dort der Standard. »Linksbündig« heißt eigentlich: bündig an der Seite, an der die Zeile beginnt. In CSS deshalb `text-align: start` statt `left`.
''') + liste('Wann bricht die Regel?', [
  'Im Buch und in der Zeitung: Blocksatz funktioniert mit viel Breite und gutem Ausgleich.',
  'Bei wenig Text: Eine Einladung darf zentriert sein.',
  'In anderen Schreibrichtungen: Bündig ist die Seite, an der die Zeile beginnt.',
]) + '\n')

W(D, '070-verweise.md', kopf('Verweise', '''
Dahinter: Phänomen Wortbilder. Weiter: Lesetext, Nähe und Abstand, Typografische Hierarchie.
''') + '''{% statement "Verweise", "Dahinter: [Wortbilder](../phaenomen-wortbilder/). Weiter: [Lesetext](../prinzip-lesetext/), [Typografische Hierarchie](../prinzip-typografische-hierarchie/), [Nähe und Abstand](../prinzip-naehe-und-abstand/)." %}
''')
done(D, 'Die Satzart folgt der Textmenge: am Screen linksbündig, Blocksatz nur mit Trennung und Breite, zentriert nur für Kurzes. Absätze gliedern, Umbrüche kontrollieren', 'Flattersatz, Blocksatz, Silbentrennung, Absatz, Hurenkind, Schusterjunge')
index(D, ['Satzart folgt Textmenge', 'Absätze', 'Hurenkind, Schusterjunge und text-wrap'])
print('fertig', D)
