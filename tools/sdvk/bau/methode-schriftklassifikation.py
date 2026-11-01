# Bauskript methode-schriftklassifikation. Aufruf: python3 tools/sdvk/bau/methode-schriftklassifikation.py
# Schriftmuster entstehen mit Systemschriften (macOS) über typo.py. Vorher tools/sdvk/*.js nach /tmp/shots kopieren.
# Fraktur: tools/sdvk/bau/schriften/UnifrakturMaguntia-Book.ttf (Google Fonts, SIL Open Font License).
import base64, glob
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'methode-schriftklassifikation'
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Schriftklassifikation', 'Methode // Konstruieren')
imgs(D, 'typographie', [f'schriftgruppe-0{i}.png' for i in range(1, 5)])

FRAKTUR = base64.b64encode(open('/Users/cnoss/git/privat/slides/tools/sdvk/bau/schriften/UnifrakturMaguntia-Book.ttf', 'rb').read()).decode()
FACE = f'<style>@font-face{{font-family:Fraktur;src:url(data:font/ttf;base64,{FRAKTUR})}}</style>'
WORT = 'Hamburgefonts'
FREMD = '<span style="font-family:\'Times New Roman\'">Ελληνικά</span> &nbsp; <span style="font-family:\'Geeza Pro\'">العربية</span> &nbsp; <span style="font-family:\'Hiragino Sans GB\'">汉字</span>'

def tafel(name, zeilen, gr=56, breite=660):
    """Tafel mit Schriftmustern: links die Bezeichnung, rechts das Muster. Zeile: (Bezeichnung, Schrift, Gewicht, Inhalt)"""
    z = ''
    for label, schrift, gewicht, inhalt in zeilen:
        z += (f'<div style="display:flex;align-items:center;gap:40px;flex:1;">'
              f'<div style="width:{breite}px;font-family:\'Helvetica Neue\';font-size:30px;color:#6a6a6a;line-height:1.15;">{label}</div>'
              f'<div style="font-family:\'{schrift}\';font-weight:{gewicht};font-size:{gr}px;line-height:1;white-space:nowrap;">{inhalt}</div></div>')
    muster(D, name, f'{FACE}<div style="display:flex;flex-direction:column;width:1600px;height:900px;padding:30px 70px;box-sizing:border-box;">{z}</div>')

tafel('din-gruppen', [
  ('1 Venezianische Renaissance-Antiqua', 'Iowan Old Style', 400, WORT),
  ('2 Französische Renaissance-Antiqua', 'Palatino', 400, WORT),
  ('3 Barock-Antiqua', 'Baskerville', 400, WORT),
  ('4 Klassizistische Antiqua', 'Didot', 400, WORT),
  ('5 Serifenbetonte Linear-Antiqua', 'Rockwell', 400, WORT),
  ('6 Serifenlose Linear-Antiqua', 'Helvetica Neue', 400, WORT),
  ('7 Antiqua-Varianten', 'Herculanum', 400, WORT),
  ('8 Schreibschriften', 'Snell Roundhand', 700, WORT),
  ('9 Handschriftliche Antiqua', 'Bradley Hand', 400, WORT),
  ('10 Gebrochene Schriften', 'Fraktur', 400, WORT),
  ('11 Fremde Schriften', 'Times New Roman', 400, FREMD),
])
tafel('beinert-gruppen', [
  ('1 Antiqua', 'Baskerville', 400, WORT),
  ('2 Egyptienne', 'Rockwell', 400, WORT),
  ('3 Grotesk', 'Helvetica Neue', 400, WORT),
  ('4 Zierschriften', 'Phosphate', 400, WORT),
  ('5 Screen Fonts', 'Verdana', 400, WORT),
  ('6 Corporate Fonts', 'IBM Plex Sans', 400, WORT),
  ('7 Gebrochene Schriften', 'Fraktur', 400, WORT),
  ('8 Nichtrömische Schriften', 'Times New Roman', 400, FREMD),
  ('9 Bildzeichen', 'Zapf Dingbats', 400, '✂ ✈ ✉ ☞ ★ ✓'),
], gr=66, breite=480)
tafel('ergebnis', [
  ('Baskerville<br>DIN 3, Beinert 1', 'Baskerville', 400, WORT),
  ('Rockwell<br>DIN 5, Beinert 2', 'Rockwell', 400, WORT),
  ('Futura<br>DIN 6, Beinert 3', 'Futura', 400, WORT),
  ('Verdana<br>DIN 6, Beinert 5', 'Verdana', 400, WORT),
], gr=104, breite=380)
tafel('eine-gruppe', [
  ('Helvetica Neue', 'Helvetica Neue', 400, WORT),
  ('Futura', 'Futura', 400, WORT),
  ('Gill Sans', 'Gill Sans', 400, WORT),
  ('Verdana', 'Verdana', 400, WORT),
], gr=104, breite=380)
tafel('uebung', [
  ('A', 'Palatino', 400, WORT),
  ('B', 'Didot', 400, WORT),
  ('C', 'Rockwell', 400, WORT),
  ('D', 'Futura', 400, WORT),
], gr=120, breite=90)

W(D, '005-problem.md', kopf('Das Problem', '''
Wer keine Wörter für Schriften hat, sagt »die mit den Füßchen« oder »so wie Apple, nur wärmer«. Das hilft weder im Gespräch noch bei der Suche.

Eine Klassifikation ist ein Wörterbuch. Sie ordnet Schriften nach sichtbaren Merkmalen und oft auch nach ihrer Geschichte. Damit können Sie über eine Schrift sprechen, nach Alternativen suchen und Ihre Schriften sortieren. Sie sagt nichts darüber, ob eine Schrift gut ist oder zur Aufgabe passt.

Tiefe: kennen. Sie müssen die Gruppen nicht auswendig können. Sie sollen wissen, dass es sie gibt, wie man eine Schrift grob einordnet und wo man nachschlägt.
''') + '''{% interlude "»Die mit den Füßchen.«", "Wie sprechen Sie über eine Schrift?" %}

{% statement "Eine Klassifikation ist ein Wörterbuch.", "Sie macht Schriften beschreibbar und auffindbar. Sie sagt nicht, welche Schrift gut ist." %}
''')

W(D, '010-ergebnis.md', kopf('Ergebnis zuerst', '''
So sieht das Ergebnis aus: Jede Schrift bekommt eine Gruppe. Hier nach zwei Modellen, der DIN 16518 und der Matrix Beinert.

Bei den ersten drei Schriften sind sich die Modelle einig, sie benennen und zählen nur anders. Bei Verdana nicht: Für die DIN von 1964 ist sie eine serifenlose Schrift wie jede andere. Beinert führt sie als Screen Font, weil sie für den Bildschirm gezeichnet wurde. Das ist der Unterschied der beiden Modelle auf einer Folie.

Die Zuordnungen sind unsere Einordnung nach den Merkmalen. Klassifikationen sind nicht immer eindeutig, Fachleute ordnen einzelne Schriften auch mal anders ein.
''') + bild('ergebnis.png', 'Jede Schrift bekommt eine Gruppe. Verdana zeigt, wo sich die Modelle unterscheiden') + '\n')

W(D, '020-schritte.md', kopf('Schritte', '''
Das reicht für eine grobe Einordnung:

**1. Grundform:** Gedruckt oder geschrieben? Gebrochen wie eine Fraktur? Lateinisch oder nicht? Damit sind schon einige Gruppen geklärt.

**2. Serifen:** keine (Grotesk), normal (Antiqua) oder kräftig und betont (Egyptienne, im Englischen Slab Serif).

**3. Achse und Kontrast, wenn es Serifen gibt:** Schauen Sie auf das o oder das e. Ist die Achse der Rundung schräg und der Strich gleichmäßig, ist die Schrift eher alt. Ist die Achse senkrecht und sind die Haarstriche hauchdünn, ist sie klassizistisch.

**4. Nachschlagen:** Kurz prüfen, wie der Schriftanbieter oder das Typolexikon die Schrift einordnet. Google Fonts filtert nach Serif, Sans Serif, Display, Handwriting und Monospace, nicht nach DIN.
''') + liste('In vier Schritten einordnen', [
  '<strong>1. Grundform:</strong> gedruckt oder geschrieben, gebrochen, lateinisch?',
  '<strong>2. Serifen:</strong> keine, normal oder betont?',
  '<strong>3. Achse und Kontrast:</strong> Schauen Sie auf das o und das e.',
  '<strong>4. Nachschlagen:</strong> beim Schriftanbieter oder im Typolexikon',
]) + '\n')

W(D, '030-din.md', kopf('DIN 16518', '''
Das klassische Modell im deutschsprachigen Raum. Elf Gruppen, geordnet vor allem nach Stil und Entstehungszeit. Die ersten vier Gruppen sind eine kleine Schriftgeschichte der Antiqua, die nächsten Folien zeigen sie im Vergleich: Die Achse richtet sich auf, der Unterschied zwischen dicken und dünnen Strichen wächst, die Serifen werden feiner.

Die Tafel zeigt Beispiele aus den Systemschriften. Die Beispiele sind unsere Einordnung, die Norm selbst nennt keine digitalen Schriften.

Die Vergleichsbilder stammen aus dem bisherigen Foliensatz Typographie.

**Grenzen:** Die Norm stammt aus dem Bleisatz. Für alles ohne Serifen hat sie genau eine Gruppe: Helvetica, Futura, Gill Sans und Verdana stehen zusammen, obwohl sie sehr verschieden wirken. Screen Fonts und Webfonts kennt sie gar nicht.

**Hintergrund**

Die DIN 16518 erschien im August 1964 und baut auf der Klassifikation von Maximilien Vox (1954) auf. Der Normenkatalog führt die Ausgabe von 1964 bis heute. Sie gilt fast nur im deutschsprachigen Raum.

Den Begriff »Barock-Antiqua« gibt es international nicht, im Englischen heißt die Gruppe »Transitional«. »Fremde Schriften« ist die Wortwahl von 1964. Heute sagt man nicht lateinische Schriften. Aus deren Sicht ist die lateinische Schrift die fremde.

Scharfe Kritik kommt von Wolfgang Beinert, der die Norm als »Bleisatz-DIN« bezeichnet und von ihrer Anwendung abrät. Er hat allerdings auch das Gegenmodell entwickelt. Quelle: typolexikon.de, Stichwort DIN 16518.
''') + '''{% interlude "DIN 16518", "Elf Gruppen, von 1964" %}

''' + '\n'.join([
  bild('din-gruppen.png', 'Die elf Gruppen der DIN 16518'),
  bild('schriftgruppe-01.png', 'Gruppe 1, Venezianische Renaissance-Antiqua: Die Achse steht schräg, der Strich ist fast gleichmäßig'),
  bild('schriftgruppe-02.png', 'Gruppe 2, Französische Renaissance-Antiqua: etwas feiner, die Achse noch schräg'),
  bild('schriftgruppe-03.png', 'Gruppe 3, Barock-Antiqua: Die Achse richtet sich auf, der Kontrast wächst'),
  bild('schriftgruppe-04.png', 'Gruppe 4, Klassizistische Antiqua: Die Achse steht senkrecht, die Haarstriche sind hauchdünn'),
  bild('eine-gruppe.png', 'Alle in Gruppe 6: Für alles ohne Serifen hat die DIN nur eine Gruppe'),
]) + '\n')

W(D, '040-beinert.md', kopf('Matrix Beinert', '''
Wolfgang Beinert hat die Matrix 2001 für die digitale Arbeit entwickelt und aktualisiert sie bis heute, zuletzt im Dezember 2025. Sie ordnet Druckschriften, Screen Fonts, Webfonts und Bildzeichen in neun Hauptgruppen.

Der Unterschied zur DIN: Die Matrix fragt auch, wofür eine Schrift da ist. Screen Fonts, Corporate Fonts und Bildzeichen stehen schon auf der obersten Ebene. Darunter wird weiter unterteilt, die Grotesk etwa in Ältere Grotesk (Akzidenz Grotesk), Amerikanische Grotesk (Trade Gothic), Konstruierte Grotesk (Futura) und Jüngere Grotesk (Frutiger). Damit bekommt die Vielfalt der serifenlosen Schriften, die in der DIN in einer Gruppe steckt, eigene Namen.

**Ganz praktisch:** Beinert denkt die Hauptgruppen als Ordner für die eigene Schriftensammlung, Unter- und Nebengruppen als Unterordner. Das geht auch in einer Software zur Schriftverwaltung.

Die Tafel zeigt Beispiele aus den Systemschriften. Die Beispiele sind unsere Einordnung. Maßgeblich ist typolexikon.de, Stichwort Matrix Beinert.

**Hintergrund**

Die Reihenfolge der Hauptgruppen hat sich geändert: In älteren Fassungen, auch in unserem früheren Foliensatz, standen die Corporate Fonts an vierter Stelle. Hier steht der Stand von Dezember 2025.

Die Matrix ist keine Norm, sondern das Modell einer Person, verbreitet über sein Typolexikon. International üblich sind die Gruppen, die Schriftanbieter nutzen: Serif, Sans Serif, Slab Serif, Script, Display, Monospace.
''') + '''{% interlude "Matrix Beinert", "Neun Hauptgruppen, für die digitale Arbeit" %}

''' + bild('beinert-gruppen.png', 'Die neun Hauptgruppen der Matrix Beinert') + '''

{% statement "Die Matrix fragt auch: Wofür ist die Schrift da?", "Screen Fonts, Corporate Fonts und Bildzeichen haben eigene Hauptgruppen. Die Grotesk wird weiter unterteilt, zum Beispiel in Konstruierte Grotesk wie die Futura." %}

<section class="simple" data-transition="fade">
<div>

# DIN 16518 und Matrix Beinert

| | DIN 16518 | Matrix Beinert |
|---|---|---|
| **Stand** | 1964 | 2001, laufend aktualisiert |
| **Gedacht für** | Bleisatz | digitale Arbeit |
| **Gruppen** | 11 | 9 Hauptgruppen mit Untergruppen |
| **Ohne Serifen** | eine Gruppe | Grotesk mit Untergruppen, dazu Screen Fonts |
| **Status** | Norm | Modell von Wolfgang Beinert |

</div>
</section>
''')

W(D, '050-uebung.md', kopf('Kurz ausprobieren', '''
**Optional, ca. 3 Minuten.** Bei einer Kennen-Methode keine Pflicht, aber es macht die Merkmale greifbar. Zu zweit: Serifen? Achse? Welche Gruppe?

**Auflösung:** A ist Palatino, B Didot, C Rockwell, D Futura. Es muss nicht jede Nummer sitzen. Serifen, betonte Serifen, keine Serifen und der Unterschied zwischen A und B reichen schon.

Bei A sind Einordnungen im Netz nicht ganz einheitlich, das ist ein guter Anlass, über die Grenzen von Klassifikationen zu sprechen.
''') + bild('uebung.png', 'Welche Gruppe? Achten Sie auf Serifen, Achse und Kontrast') + '''

<section class="simple" data-transition="fade">
<div>

# Auflösung

| | Schrift | Merkmal | DIN 16518 | Matrix Beinert |
|---|---|---|---|---|
| **A** | Palatino | Achse schräg, wenig Kontrast | 2 | 1 Antiqua |
| **B** | Didot | Achse senkrecht, Haarstriche | 4 | 1 Antiqua |
| **C** | Rockwell | betonte Serifen | 5 | 2 Egyptienne |
| **D** | Futura | keine Serifen, geometrisch | 6 | 3 Grotesk |

</div>
</section>
''')

W(D, '060-fehler.md', kopf('Typische Fehler', '''
Der häufigste Fehler ist, die Einordnung für eine Auswahl zu halten. Aus »Grotesk« folgt noch nicht, dass die Schrift zur Aufgabe passt. Dafür gibt es die Methode Schriftauswahl.

Der zweite: Gruppen auswendig lernen, ohne auf die Buchstaben zu schauen. Wer ein o und ein e vergleichen kann, braucht die Nummer nicht.
''', cls='simple') + '\n'.join("{% fragment '<p class=\"list\">" + p + "</p>' %}" for p in [
  'Einordnen statt auswählen: Die Gruppe sagt nicht, ob die Schrift passt',
  'Nummern lernen statt auf die Buchstaben schauen',
  'Für eine Gruppe eine feste Wirkung annehmen: Serifen sind nicht automatisch seriös',
  'Klassifikation für Wahrheit halten: Es sind Modelle, und sie widersprechen sich',
]) + '\n')

W(D, '070-einsatz.md', kopf('Einsatz', '''
Die Methode ist eine Kennen-Methode. Sie taucht wieder auf, wenn es um die Schriftauswahl und Schriftmischung geht, und im Crit, wenn jemand begründen will, warum eine Schrift passt.

Dahinter: Rahmen Typografie mit der Geschichte und den Begriffen. Weiter: Schriftauswahl mit den fünf Gruppen für den Alltag, Wirkung von Schrift.

Zum Nachschlagen: typolexikon.de (Wolfgang Beinert), Lupton, Thinking with Type (Letter).
''') + liste('Wo Sie das brauchen', [
  'Bei der Suche: Alternativen zu einer Schrift finden',
  'Im Gespräch: sagen können, was man meint',
  'In der Schriftensammlung: Ordnung halten',
]) + '''

{% statement "Verweise", "Dahinter: [Typografie](../rahmen-typografie/). Weiter: [Schriftauswahl](../methode-schriftauswahl/) und [Wirkung von Schrift](../prinzip-schrift-wirkung/). Zum Nachschlagen: [Typolexikon](https://www.typolexikon.de/schriftklassifikation/)." %}
''')

open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Schriftklassifikation"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Methode"
gruppe: "Konstruieren"
tiefe: "kennen"
einsatz: "Zum Beschreiben, Suchen und Ordnen von Schriften"
kurzsatz: "Schriften nach Merkmalen und Geschichte einordnen: DIN 16518 für den Bleisatz, Matrix Beinert für die digitale Arbeit"
begriffe: ["Schriftklassifikation", "DIN 16518", "Matrix Beinert", "Antiqua", "Egyptienne", "Grotesk", "Achse"]
herkunft: "U: typographie/060, 070"
inhalt:
  - "DIN 16518"
  - "Matrix Beinert"
  - "Schriften einordnen"
status: ok
---
''')
print('fertig', D)
