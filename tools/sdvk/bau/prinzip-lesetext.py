exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'prinzip-lesetext'
intro(D, 'Lesetext', 'Prinzip // Lesbar machen')
def satz(ch, lh=1.5, gr=3.2, extra=''):
    return f'<p style="font-family:PTserif;font-size:{gr}vh;line-height:{lh};max-width:{ch}ch;width:100%;margin:0;text-align:left;hyphens:none;{extra}">{KURZ}</p>'
UNRUHIG = ('Beim <span style="font-weight:700;">Lesen</span> gleiten die Augen nicht <span style="letter-spacing:.25em;">gleichmäßig</span> über die Zeile. Sie <span style="font-weight:700;">springen von Punkt zu Punkt</span> und ergänzen den Rest aus dem Zusammenhang. '
  'Am <span style="letter-spacing:.25em;">Zeilenende</span> müssen sie zurück an den <span style="font-weight:700;">Anfang</span> der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang <span style="letter-spacing:.25em;">schlecht</span> wieder.')
RUHIG = ('Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. '
  'Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder.')
def grau(unscharf=False):
    b = 'filter:blur(0.35vw);' if unscharf else ''
    k = lambda t, st: f'<p lang="de" style="flex:1;font-family:PTserif;font-size:3vh;line-height:1.45;margin:0;hyphens:none;{st}{b}">{t}</p>'
    return f'<div style="display:flex;gap:5vw;align-items:flex-start;width:100%;">{k(UNRUHIG, "text-align:justify;")}{k(RUHIG, "text-align:left;")}</div>'

W(D, '010-regel.md', kopf('Lesetext', '''
Die Regel: Lesetext ist bequem, wenn drei Dinge stimmen: Zeilenlänge, Zeilenabstand und ein gleichmäßiger Grauwert. Sie merken es nicht, wenn es stimmt. Sie merken nur, wenn es nicht stimmt, und hören dann auf zu lesen.

**Für alle:** Davon profitieren alle, besonders aber Menschen mit Leseschwäche oder eingeschränktem Sehen.

**Hintergrund**

Robert Bringhurst, »The Elements of Typographic Style« (1992): 45 bis 75 Zeichen pro Zeile, 66 gelten als ideal. Matthew Butterick, »Practical Typography« (online): 45 bis 90 Zeichen, Zeilenabstand 120 bis 145 %. Wathan und Schoger, »Refactoring UI« (2018), Kapitel »Designing Text«. Lupton, »Thinking with Type«, Kapitel »Text«.
''') + '''{% interlude "Guter Lesetext fällt nicht auf.", "Schlechter schon." %}
''')

W(D, '020-zeilenlaenge.md', kopf('Zeilenlänge', '''
Derselbe Text in drei Breiten. Beim Lesen springen die Augen am Zeilenende zurück an den Anfang der nächsten Zeile.

**Zu lang:** Der Rücksprung ist weit, man landet leicht in der falschen Zeile. **Zu kurz:** Die Augen springen ständig, der Lesefluss reißt ab, die Wörter verteilen sich unruhig. **Richtig:** 45 bis 75 Zeichen, auf dem Handy dürfen es 35 bis 50 sein.

Die Breite ist unabhängig von der Bildschirmbreite. Genau das ist der häufigste Fehler am Screen: Der Text läuft einfach über die ganze Breite.

Im CSS gibt es dafür eine eigene Einheit: `ch`, die Breite der Ziffer Null. Die drei Fassungen hier sind so gesetzt: `max-width: 120ch`, `25ch` und `65ch`.
''') + beispiel('Zu lang: etwa 120 Zeichen', satz(120, gr=2.4)) + '\n\n' + beispiel('Zu kurz: etwa 25 Zeichen', satz(25, gr=2.6, lh=1.4), 'none') + '\n\n' + beispiel('Gut: etwa 65 Zeichen', satz(65), 'none') + '\n')

W(D, '030-zeilenabstand.md', kopf('Zeilenabstand', '''
**Zu eng:** Die Zeilen kleben zusammen, die Augen rutschen ab. **Zu weit:** Der Text zerfällt in Streifen, weil die Zeilen weiter voneinander entfernt sind als die Wörter voneinander. Das ist Nähe: Was nah ist, gehört zusammen.

**Gut:** Für Lesetext 120 bis 150 %. Je länger die Zeile, desto mehr Zeilenabstand braucht sie. Große Überschriften brauchen weniger, oft reichen 110 %. Im CSS ohne Einheit angeben (`line-height: 1.5`), dann wächst der Abstand mit der Schrift mit.
''') + beispiel('Zu eng: 100 %', satz(65, 1.0), 'none') + '\n\n' + beispiel('Zu weit: 220 %', satz(65, 2.2), 'none') + '\n\n' + beispiel('Gut: 150 %', satz(65, 1.5), 'none') + '\n')

W(D, '040-grauwert.md', kopf('Grauwert', '''
Kneifen Sie die Augen zusammen: Ein guter Textblock wirkt wie eine gleichmäßig graue Fläche. Das ist der Grauwert. Löcher, dunkle Flecken und helle Streifen stören den Lesefluss, auch wenn man sie beim Lesen nicht bewusst wahrnimmt.

Links und rechts: derselbe Text. Links mit Blocksatz ohne Trennung, gesperrten und fetten Wörtern, rechts ruhig gesetzt. Unscharf sieht man den Unterschied sofort. Das ist derselbe Trick wie beim Unschärfetest.

Was den Grauwert stört: gesperrter Text, zu viele Auszeichnungen im Absatz, erzwungener Blocksatz ohne Silbentrennung. Dazu mehr bei Satz.

Die Reihenfolge der Abstände: Buchstabenabstand kleiner als Wortabstand, kleiner als Zeilenabstand, kleiner als Absatzabstand. Wird diese Reihenfolge verletzt, zerfällt der Text.
''', transition='none') + beispiel('Zweimal derselbe Text', grau()) + '\n\n' + beispiel('Unscharf sieht man es', grau(True), 'none') + '''

{% statement "Abstände haben eine Reihenfolge.", "Buchstaben sind enger als Wörter. Wörter enger als Zeilen. Zeilen enger als Absätze." %}
''')

CODE = '''article p {
  font-size: 1rem;      /* mindestens 16 px */
  line-height: 1.5;     /* ohne Einheit */
  max-width: 65ch;      /* Zeilenlänge */
  text-wrap: pretty;    /* keine einsamen Wörter am Ende */
}'''
W(D, '050-im-screen.md', kopf('Im Screen', '''
Auf einer echten Seite: Die deutsche Wikipedia begrenzt die Textbreite in der Standarddarstellung, gibt aber die Wahl, ob der Text schmal oder breit läuft. Das Menü rechts stellt Textgröße und Breite ein. Eine gute Lösung, weil Lesevorlieben verschieden sind.

Dann die vier Zeilen CSS, mit denen das meiste erledigt ist. `text-wrap: pretty` ist noch nicht überall verfügbar, schadet aber auch nicht: Browser, die es nicht kennen, ignorieren es.

**Für alle:** WCAG 1.4.12 (Textabstände) verlangt, dass ein Layout nicht bricht, wenn Nutzende den Zeilenabstand auf das 1,5-Fache, den Absatzabstand auf das 2-Fache, den Buchstabenabstand auf das 0,12-Fache und den Wortabstand auf das 0,16-Fache der Schriftgröße stellen. Also keine festen Höhen für Textcontainer.

Screenshot: de.wikipedia.org, 2026, ausgeschnitten. Der Spendenaufruf über der Seite ist weggelassen.
''') + bild('lesetext-wikipedia.jpg', 'Begrenzte Breite, und die Lesenden dürfen sie ändern<br><small>de.wikipedia.org, Screenshot 2026, Ausschnitt</small>', schatten=True) + '\n\n' + code('Vier Zeilen CSS', CODE) + '''

{% question "Wie lang sind die Zeilen auf Ihrer Lieblingsseite?", "Zählen Sie nach: Wie viele Zeichen hat eine Zeile? Und wie viele auf dem Handy?" %}
''')

W(D, '060-grenzen.md', kopf('Grenzen', '''
**Kurze Texte:** Die Regeln gelten für Lesetext. Ein Label, ein Button oder eine Tabellenzeile folgen anderen Regeln. Eine Tabelle darf breit sein, weil sie nicht zeilenweise gelesen wird.

**Überschriften:** Große Schrift braucht weniger Zeilenabstand und oft etwas engere Laufweite. Die 150 % würden sie zerfallen lassen.

**Helle Schrift auf dunklem Grund:** Sie wirkt dünner und braucht oft etwas mehr Zeilenabstand und einen kräftigeren Schnitt. Kontrast prüfen.
''') + liste('Wann gilt das nicht?', [
  'Kurze Texte: Label, Buttons und Tabellen folgen eigenen Regeln.',
  'Überschriften: Große Schrift braucht weniger Zeilenabstand.',
  'Helle Schrift auf dunklem Grund: oft etwas mehr Abstand, kräftigerer Schnitt.',
]) + '\n')

W(D, '070-verweise.md', kopf('Verweise', '''
Dahinter: Phänomen Wortbilder. Weiter: Satz, Nähe und Abstand. Prüfen: Unschärfe- und Graustufentest, Kontrast prüfen.
''') + '''{% statement "Verweise", "Dahinter: [Wortbilder](../phaenomen-wortbilder/). Weiter: [Satz](../prinzip-satz/), [Nähe und Abstand](../prinzip-naehe-und-abstand/). Prüfen: [Unschärfe- und Graustufentest](../methode-unschaerfetest/), [Kontrast prüfen](../methode-kontrast-pruefen/)." %}
''')
done(D, 'Lesetext ist bequem, wenn Zeilenlänge (45 bis 75 Zeichen), Zeilenabstand (120 bis 150 %) und Grauwert stimmen', 'Zeilenlänge, Zeilenabstand, Grauwert, ch, line-height')
index(D, ['Zeilenlänge (Für alle)', 'Zeilenabstand (Für alle)', 'Grauwert', 'Lesetext in CSS'])
print('fertig', D)
