exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'prinzip-typografische-hierarchie'
intro(D, 'Typografische Hierarchie', 'Prinzip // Gewichten')

T = {'dach': 'Stadtentwicklung', 'head': 'Die Bibliothek zieht in den alten Bahnhof', 'lead': 'Nach drei Jahren Umbau öffnet das Haus im Frühjahr. Es gibt mehr Platz, längere Öffnungszeiten und erstmals ein Café.',
     'text': 'Wo früher Fahrkarten verkauft wurden, stehen bald Regale. Im Erdgeschoss liegen die Zeitungen, darüber die Lernplätze. Für die Ausleihe braucht es weiterhin nur einen Ausweis.', 'bu': 'Die Bahnhofshalle während des Umbaus im Sommer'}
def art(st, sp=None, labels=False):
    # st: Stil je Lesestufe. sp: Abstand nach der Stufe in em. Schrift PTsans, Größen in vh.
    sp = sp or {}
    o = []
    for k in ['dach', 'head', 'lead', 'text', 'bu']:
        lab = f'<span style="position:absolute;left:0;width:9em;color:#9313ce;font-size:2.4vh;line-height:1.3;font-weight:400;font-family:PTsans;top:.2em;">{ {"dach":"Dachzeile","head":"Headline","lead":"Lead","text":"Fließtext","bu":"Bildunterschrift"}[k]}</span>' if labels else ''
        o.append(f'<div style="position:relative;padding-left:{"14vw" if labels else "0"};margin:0 0 {sp.get(k, 0.5)}vh;font-family:PTsans;text-align:left;hyphens:none;{st[k]}">{lab}{T[k]}</div>')
    return '<div style="max-width:74vw;">' + ''.join(o) + '</div>'
B = 'font-size:3.2vh;line-height:1.4;'
GLEICH = {k: B for k in T}
GROESSE = {'dach': B, 'head': 'font-size:7.5vh;line-height:1.1;', 'lead': 'font-size:4vh;line-height:1.35;', 'text': B, 'bu': B}
SCHNITT = dict(GROESSE); SCHNITT['head'] += 'font-weight:700;'; SCHNITT['dach'] = B + 'font-weight:700;'
FARBE = dict(SCHNITT); FARBE['bu'] = 'font-size:2.6vh;line-height:1.4;color:#888888;'; FARBE['dach'] = 'font-size:2.6vh;line-height:1.4;font-weight:700;color:#888888;'
ABST = {'dach': 0.6, 'head': 2.4, 'lead': 2.4, 'text': 2.0, 'bu': 0}

W(D, '010-regel.md', kopf('Typografische Hierarchie', '''
Die Regel: Ein Text hat mehrere Einstiege. Wer überfliegt, muss in der Überschrift verstehen, worum es geht. Wer liest, findet über den Vorspann hinein. Wer nachschlägt, findet die Stelle. Das leisten die Lesestufen: Dachzeile, Headline, Lead, Fließtext, Bildunterschrift.

Es ist dasselbe Prinzip wie Hierarchie, nur mit Text als Material.

**Hintergrund**

Ellen Lupton, »Thinking with Type« (2. Auflage 2010), Kapitel »Text«, beschreibt Hierarchie als Ausdruck der Gliederung eines Inhalts. Adam Wathan und Steve Schoger, »Refactoring UI« (2018), Kapitel »Hierarchy is Everything« und »Designing Text«: Schriftgröße ist nicht das einzige Mittel. Oft reichen Schnitt und Farbe.
''') + '''{% interlude "Ein Text hat mehrere Einstiege.", "Wer überfliegt, wer liest und wer sucht, muss sich zurechtfinden." %}
''')

W(D, '020-aufbau.md', kopf('Schritt für Schritt', '''
Derselbe Text, jede Folie ändert genau ein Mittel.

1. **Alles gleich:** Kein Einstieg. Man muss alles lesen, um zu wissen, worum es geht.
2. **Größe:** Die Headline springt heraus, der Lead setzt sich ab.
3. **Schnitt:** Bold für die Headline und die Dachzeile. Das Gewicht steigt, ohne dass mehr Platz gebraucht wird.
4. **Farbe:** Grau nimmt Dachzeile und Bildunterschrift zurück. Betonen durch Zurücknehmen.
5. **Abstand:** Nähe zeigt, was zusammengehört. Die Dachzeile rückt an die Headline, die Bildunterschrift bekommt ihren eigenen Platz.
6. **Die Namen:** Fünf Lesestufen. Mehr braucht fast kein Screen.

Der Text ist erfunden.
''') + beispiel('Alles gleich', art(GLEICH), 'none') + '\n\n' + beispiel('Größe', art(GROESSE), 'none') + '\n\n' + beispiel('Schnitt', art(SCHNITT), 'none') + '\n\n' + beispiel('Farbe', art(FARBE), 'none') + '\n\n' + beispiel('Abstand', art(FARBE, ABST), 'none') + '\n\n' + beispiel('Die Lesestufen', art(FARBE, ABST, True), 'none') + '\n')

W(D, '030-im-screen.md', kopf('Im Screen', '''
Die Lesestufen auf einer echten Seite: Dachzeile »Fehlender Wohnraum«, Headline, Lead, darunter die Autorenzeile. Die Dachzeile ist klein, die Headline trägt Größe und Farbe, und der Lead steht direkt darunter. Wer nur die Überschrift liest, hat die Nachricht verstanden.

**Für alle:** Die optische Hierarchie muss auch im Code stehen. Überschriften gehören in `h1` bis `h6`, in der richtigen Reihenfolge. Screenreader-Nutzende springen über diese Struktur durch die Seite wie andere mit den Augen. Eine Überschrift, die nur groß und fett aussieht, gibt es für sie nicht.

Screenshot: tagesschau.de, 2026.
''') + bild('lesestufen-tagesschau.jpg', 'Dachzeile, Headline, Lead, Autorenzeile<br><small>tagesschau.de, Screenshot 2026</small>', schatten=True) + '''

{% statement "Sie muss auch im Code stehen.", "Überschriften gehören in h1 bis h6. Screenreader springen über diese Struktur durch die Seite wie andere mit den Augen." %}

{% question "Wie viele Lesestufen hat Ihre meistgenutzte App?", "Welche Mittel nutzt sie dafür: Größe, Schnitt, Farbe oder Abstand?" %}
''')

W(D, '040-grenzen.md', kopf('Grenzen', '''
**Zu viele Stufen:** Wenn sich jede Stufe nur minimal von der nächsten unterscheidet, sieht man keine Rangfolge mehr. Lieber wenige Stufen mit deutlichem Abstand.

**Zu viele Mittel auf einmal:** Größer, fetter, bunter und unterstrichen ist kein Mehr an Hierarchie, es ist Lärm. Meist reichen zwei Mittel pro Stufe.

**Interface ist nicht Artikel:** In dichten Oberflächen gibt es oft keine Headline im klassischen Sinn. Dort sind die Daten das Wichtigste, nicht ihre Beschriftung. Label dürfen zurücktreten.
''') + liste('Wann bricht die Regel?', [
  'Zu viele Stufen: Minimale Unterschiede zeigen keine Rangfolge.',
  'Zu viele Mittel: Größer, fetter und bunter zugleich ist Lärm.',
  'Interface ist nicht Artikel: Oft sind die Daten wichtiger als ihre Beschriftung.',
]) + '\n')

W(D, '050-verweise.md', kopf('Verweise', '''
Dahinter: Prinzip Hierarchie. Konstruieren: Typografische Skala. Prüfen: Unschärfe- und Graustufentest.
''') + '''{% statement "Verweise", "Dahinter: [Hierarchie](../prinzip-hierarchie/). Konstruieren: [Typografische Skala](../methode-typografische-skala/). Prüfen: [Unschärfe- und Graustufentest](../methode-unschaerfetest/)." %}
''')
done(D, 'Lesestufen geben einem Text mehrere Einstiege. Größe, Schnitt, Farbe und Abstand bauen die Rangfolge auf', 'Lesestufe, Dachzeile, Headline, Lead, Fließtext, Bildunterschrift')
index(D, ['Mehrere Einstiege', 'Schritt für Schritt: Größe, Schnitt, Farbe, Abstand', 'Lesestufen im Screen', 'Hierarchie im Code'])
print('fertig', D)
