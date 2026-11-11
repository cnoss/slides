# Bauskript prinzip-inhalt-bestimmt-form. Aufruf: python3 tools/sdvk/bau/prinzip-inhalt-bestimmt-form.py
import glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'prinzip-inhalt-bestimmt-form'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Inhalt bestimmt Form', 'Prinzip // Ordnen')

K = '#231f20'; L = '#9313ce'

# ---------------------------------------------------------------- Karten als HTML mit echtem Text
# Feste Höhe wie in vielen Card-Grids: Was nicht passt, läuft sichtbar über die Karte hinaus.
def karte(kat, titel, text, bild=True, link='Mehr lesen', breite=22):
    b = '<div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div>' if bild else ''
    return (f'<div style="width:{breite}vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;">'
            f'{b}<p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">{kat}</p>'
            f'<p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:{K};">{titel}</p>'
            f'<p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">{text}</p>'
            f'<p style="font-size:1.9vh;font-weight:700;margin:0;color:{L};">{link} ›</p></div>')

def reihe(titel, karten, unter=''):
    u = f'<p style="margin-top:3vh;font-size:2.2vh;">{unter}</p>' if unter else ''
    return (f'<section class="simple" data-transition="none">\n  <div>\n    <h1>{titel}</h1>\n'
            f'    <div style="display:flex;gap:2vw;align-items:flex-start;justify-content:flex-start;width:100%;">{"".join(karten)}</div>{u}\n  </div>\n</section>')

LOREM_T = 'Lorem ipsum dolor sit amet'
LOREM = 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt.'
W(D, '010-stresstest.md', kopf('Stresstest', '''
**Live (ca. 2 Minuten).** Ein Card-Grid, wie es in jedem Entwurf steht: drei Karten, Platzhaltertext, schöne Bilder, feste Höhe. Sieht fertig aus.

Dann kommen nacheinander echte Inhalte. Bei jeder Folie fragen: Hält die Karte das aus?

1. **Echte Titel:** Einer ist sehr lang. Er läuft über die Karte hinaus, die Karten werden ungleich.
2. **Ein Bild fehlt, die Kategorie ist zweizeilig:** Die Karte sieht plötzlich kaputt aus, obwohl inhaltlich alles stimmt.
3. **Übersetzung:** Deutsche Texte sind oft deutlich länger als englische. »Events« wird zu »Veranstaltungen«, »Read more« zu »Weiterlesen«.

Pointe: Kaputt ist nicht der Inhalt. Kaputt ist ein Entwurf, der nur für Lorem ipsum gemacht wurde.

Die Inhalte sind ausgedacht, angelehnt an Meldungen einer Hochschul-Website.
''', transition='none') + '''{% interlude "Hält Ihre Card das aus?", "Ein Stresstest mit echten Inhalten" %}

''' + '\n\n'.join([
  reihe('Mit Platzhaltertext', [karte('Lorem', LOREM_T, LOREM)] * 3, 'Sieht fertig aus.'),
  reihe('Mit echten Titeln', [
    karte('Studium', 'Projektwoche startet', 'Vom 18. bis 22. November ruhen die Vorlesungen.'),
    karte('Forschung', 'Studierende entwickeln mit der Stadt eine barrierefreie Navigations-App für den Campus Gummersbach und alle angrenzenden Haltestellen', 'Das Projekt läuft zwei Semester.'),
    karte('Studium', 'Neue Leitlinien für KI im Studium', 'Was erlaubt ist und was nicht.')]),
  reihe('Ein Bild fehlt, die Kategorie ist länger', [
    karte('Studium', 'Projektwoche startet', 'Vom 18. bis 22. November ruhen die Vorlesungen.'),
    karte('Forschung und Transfer, Institut für Informatik', 'Medieninformatik gewinnt Förderpreis', 'Ausgezeichnet wurde ein Projekt zu Gestensteuerung.'),
    karte('Studium', 'Neue Leitlinien für KI im Studium', 'Was erlaubt ist und was nicht.', bild=False)]),
  reihe('Dieselbe Karte, zwei Sprachen', [
    karte('Events', 'Game Jam winners', 'Three teams, 48 hours, one theme.', link='Read more'),
    karte('Veranstaltungen', 'Gewinnerinnen und Gewinner des Game Jams stehen fest', 'Drei Teams, 48 Stunden, ein Thema.', link='Weiterlesen')]),
]) + '\n')

W(D, '020-regel.md', kopf('Inhalt bestimmt Form', '''
Die Regel: Das Layout folgt dem Inhalt und seiner Priorität, nicht umgekehrt. Wer zuerst die Form festlegt und dann den Inhalt hineinpresst, gestaltet für Lorem ipsum.

Praktisch heißt das: so früh wie möglich mit echten oder realistischen Inhalten arbeiten. Und bewusst die Extremfälle testen: der längste Titel, gar kein Bild, die längste Übersetzung, die größte Schrifteinstellung.

[Für alle] Wer die Schrift im Browser oder Betriebssystem vergrößert, macht genau diesen Stresstest jeden Tag. Text muss sich ohne Verlust auf 200 % vergrößern lassen (WCAG 2.2, Kriterium 1.4.4). Ein Layout, das nur bei einer Schriftgröße funktioniert, schließt Menschen aus.

**Hintergrund**

Wathan & Schoger, Refactoring UI (Starting from Scratch): erst Funktion und Inhalt, dann Details. »Lorem ipsum statt echter Inhalte« steht im Rückgrat des Moduls auf der Liste der typischen Fehler. Faustregel aus der Lokalisierung: Deutsche Texte sind gegenüber dem Englischen oft rund ein Drittel länger, kurze Wörter und Labels auch deutlich mehr (aus dem Gedächtnis, bitte prüfen).
''') + '''{% interlude "Das Layout folgt dem Inhalt.", "Nicht der Inhalt dem Layout." %}

{% statement "Kaputt ist nicht der Inhalt.", "Kaputt ist ein Entwurf, der nur für Lorem ipsum gemacht wurde. Testen Sie den längsten Titel, das fehlende Bild, die längste Übersetzung." %}
''')

# ---------------------------------------------------------------- Priorität und Mobile first
G1 = '#888888'; G2 = '#d9d9d9'; HG = '#e4e4e4'
def handy(reihenfolge):
    # Smartphone 450 x 900, Elemente in der gegebenen Reihenfolge untereinander
    els = {'titel': (G1, 40), 'datum': (G2, 14), 'bild': ('#c4c4c4', 200), 'text': (G2, 70), 'link': (L, 40)}
    y = 60; o = ''
    for k in reihenfolge:
        f, h = els[k]
        rx = ' rx="20"' if k == 'link' else ''
        w = 160 if k == 'link' else (180 if k == 'datum' else 370)
        o += f'  <rect data-id="{k}" x="40" y="{y}" width="{w}" height="{h}" fill="{f}"{rx} />\n'
        y += h + (36 if k in ('bild', 'text') else 22)
    return o
W(D, '030-prioritaet.md', kopf('Erst die Reihenfolge', '''
Bevor es eine Form gibt, gibt es eine Rangfolge. Was ist das Wichtigste auf dieser Karte, was kommt danach?

Auf dem Smartphone wird das zur harten Entscheidung: Es gibt nur eine Spalte, alles steht untereinander. Die Reihenfolge auf dem kleinen Screen ist die ehrlichste Antwort auf die Frage nach der Priorität. Deshalb Mobile first: erst den kleinsten Screen gestalten, dann den Platz auf großen Screens nutzen.

Die erste Fassung folgt der Gewohnheit: Bild oben, dann Titel. Die zweite folgt der Priorität einer Nachrichtenkarte: Titel und Datum zuerst, das Bild darf warten. Beides kann richtig sein. Entscheidend ist, dass die Reihenfolge eine Entscheidung ist.

**Hintergrund**

Mobile first geht auf Luke Wroblewski zurück (Buch »Mobile First«, 2011). Im Code steckt dieselbe Idee: Die Reihenfolge im HTML ist die Reihenfolge, in der Screenreader vorlesen und in der das Layout auf dem kleinsten Screen erscheint. Mit CSS Grid lässt sich die Anordnung auf großen Screens ändern, die Lesereihenfolge sollte trotzdem sinnvoll bleiben.
''', transition='none') + '''{% interlude "Erst die Reihenfolge, dann die Form.", "Was ist das Wichtigste?" %}

''' + liste('Rangfolge einer Nachrichtenkarte', ['<strong>1.</strong> Titel', '<strong>2.</strong> Datum', '<strong>3.</strong> Teaser', '<strong>4.</strong> Bild', '<strong>5.</strong> Weiterlesen']) + '''

{% frame '{"w":450,"h":900,"bu":"Aus Gewohnheit: Bild zuerst"}' %}
''' + handy(['bild', 'datum', 'titel', 'text', 'link']) + '''{% endframe %}
{% frame '{"w":450,"h":900,"bu":"Nach Priorität: Titel und Datum zuerst"}' %}
''' + handy(['titel', 'datum', 'text', 'bild', 'link']) + '''{% endframe %}
''')

W(D, '040-noxa.md', kopf('Erinnern Sie sich an NOXA?', '''
Brücke zur Textsatzaufgabe NOXA Analytik: ein Ratgeber-Artikel, drei Formate. Wer dort den Text gesetzt hat, hat genau das erlebt: Der Inhalt hat vorgegeben, wie breit die Spalte sein darf, wie groß die Headline auf dem Smartphone sein kann, wo die Zwischenüberschriften stehen.

Kurz zwei, drei Stimmen einsammeln.
''') + '''{% question "Ein Text, drei Formate.", "Welche Entscheidung hat bei der NOXA-Aufgabe der Inhalt für Sie getroffen?" %}
''')

W(D, '050-grenzen.md', kopf('Grenzen', '''
**Kein Inhalt da:** Oft gibt es den echten Text noch nicht. Dann realistische Platzhalter: echte Längen, echte Wortarten, die Extremfälle bewusst dazu. Lorem ipsum verschleiert genau das, was man prüfen müsste.

**Die Form ist gesetzt:** Ein Designsystem oder eine Marke gibt Karten mit fester Höhe vor, weil Ruhe im Grid wichtig ist. Dann bestimmt der Inhalt die Regeln: Titel höchstens drei Zeilen, danach kürzen, Bild immer im gleichen Format, Ersatzbild, wenn eines fehlt. Auch das ist Inhalt bestimmt Form, nur eine Ebene höher.

**Ausdruck vor Funktion:** Auf einem Plakat oder in einer Kampagne darf die Form führen und der Text sich ihr anpassen. Im Interface mit wechselnden Inhalten kaum.
''') + liste('Wann darf die Form führen?', [
  'Wenn es den Inhalt noch nicht gibt: dann realistische Platzhalter statt Lorem ipsum',
  'Wenn ein System die Form vorgibt: dann bestimmt der Inhalt die Regeln, etwa höchstens drei Zeilen',
  'Wenn Ausdruck wichtiger ist als Funktion: auf dem Plakat ja, im Interface kaum',
]) + '\n')

W(D, '060-verweise.md', kopf('Verweise', '''
Dahinter: Hierarchie (Priorität). Weiter: Ausrichtung und Raster, Lesetext. Prüfen: Variieren entlang einer Achse und im Kontext prüfen, dort mit echten Inhalten.
''') + '''{% statement "Verweise", "Dahinter: [Hierarchie](../prinzip-hierarchie/). Weiter: [Ausrichtung und Raster](../prinzip-ausrichtung-und-raster/) und [Lesetext](../prinzip-lesetext/). Prüfen: [Variieren entlang einer Achse](../methode-variieren-achse/), dort mit echten Inhalten im Kontext." %}
''')

done(D, 'Das Layout folgt dem Inhalt und seiner Priorität. Testen Sie mit echten Inhalten und Extremfällen statt mit Lorem ipsum',
     'Inhalt bestimmt Form, Priorität, Mobile first, Extremfall, Lorem ipsum')
index(D, ['Stresstest mit echten Inhalten', 'Priorität und Mobile first', 'Brücke zur NOXA-Aufgabe', 'Grenzen'], 'Vor dem ersten Entwurf und bei jedem Test mit echten Inhalten')
print('fertig', D)
