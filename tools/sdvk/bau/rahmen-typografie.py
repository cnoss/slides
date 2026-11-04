exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
# Achtung: Das Deck wurde danach von Hand überarbeitet (Commit 959cff5bc). Nicht mehr ausführen, sonst gehen die Änderungen verloren.
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
import glob
D = 'rahmen-typografie'
os.makedirs(f'{NEW}/{D}/images', exist_ok=True)
# Alte Folien entfernen, damit keine verwaisten Nummern stehen bleiben (index.md und images bleiben)
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)

# Bilder aus dem Bestand. images/trajan-inschrift.jpg (Wikimedia Commons, 2026) liegt im Deck, das Skript bindet es nur ein.
imgs(D, 'typographie', ['historie-03.png', 'historie-05.png', 'historie-07.png', 'historie-08.png', 'historie-09.png', 'historie-10.png',
                        'historie-11.png', 'historie-13.png', 'mazarine-bibel-01.png', 'anatomie-01.png'])
# Der alte Bleibuchstabe steht neben einem Text: nur den Buchstaben nehmen
subprocess.run(['magick', f'{OLD}/typographie/images/historie-16.png', '-crop', '45%x100%+0+0', '+repage', '-trim', '+repage',
                f'{NEW}/{D}/images/bleibuchstabe.png'], check=True)

intro(D, 'Typografie', 'Rahmen')
W(D, '010-zitat.md', '''
---
title: "Was ist Typografie?"
layout: presentation.11ty.js
slideClasses: cite
transition: zoom
author: Kurt Weidemann
status: ok
speaker: |
  Weidemann (1922 bis 2011) war Typograf und Gestalter, unter anderem der Schriften Biblica, Corporate A-S-E für Daimler-Benz. Der Satz ist die kürzeste brauchbare Definition, die wir kennen. Er sortiert auch alles Weitere.
---

<div class="is-full-width">

Typografie ist: Auswählen, Gliedern, Anordnen und logisch Lesbarmachen von Schrift.

</div>
''')

# ---------------------------------------------------------------- Geschichte
W(D, '020-geschichte.md', kopf('Woher kommt unsere Schrift?', '''
**Die kurze Geschichte (ca. 5 Minuten).** Es geht nicht um Jahreszahlen, sondern um eine Frage: Warum haben wir zwei Sorten Buchstaben? Und woher kommen Ober- und Unterlängen?

**Hieroglyphen:** Schrift beginnt mit Bildern. Ein Zeichen zeigt eine Sache. Die ägyptischen Hieroglyphen kennen auch Lautzeichen, aber man braucht Hunderte Zeichen. Schreiben ist ein Beruf.

**Griechen:** Die Phönizier reduzieren um 1000 v. Chr. auf gut 20 Zeichen für Konsonanten. Die Griechen ergänzen um 800 v. Chr. die Vokale. Seitdem steht ein Zeichen für einen Laut. Das ist eine enorme Vereinfachung: Lesen und Schreiben lassen sich viel schneller lernen. Über die Etrusker kommt das Alphabet nach Rom.

**Capitalis Monumentalis:** die römische Inschriftenschrift. Das berühmteste Beispiel steht am Sockel der Trajanssäule in Rom, 113 n. Chr. Nur Großbuchstaben. Die Proportionen gelten bis heute als Maßstab, und die Großbuchstaben, die wir heute benutzen, gehen direkt darauf zurück. Die Folie danach zeigt das Alphabet in einer heutigen Rekonstruktion: Die Römer kannten J, U und W noch nicht.

**Capitalis Quadrata und Rustica:** Dieselben Buchstaben, aber mit der Feder geschrieben. Die Quadrata ist aufwendig und teuer, die Rustica schmaler und schneller. Beide bleiben zwischen zwei Linien.

**Aus A wird a:** Wer schnell schreibt, setzt die Feder seltener ab. Die Formen werden rund, Striche verbinden sich, einzelne Striche ragen nach oben oder unten heraus. So entstehen über Jahrhunderte Ober- und Unterlängen und aus der Großschrift eine Kleinschrift.

**Karolingische Minuskel:** Um 800 lässt Karl der Große die Schrift im ganzen Reich vereinheitlichen, ein Teil seiner Bildungsreform. Der Gelehrte Alkuin von York gilt als treibende Kraft. Eine klare, runde, gut lesbare Kleinschrift, das erste Schriftsystem, das in ganz Europa verstanden wird.

**Gutenberg:** Um 1450 entwickelt Johannes Gutenberg in Mainz den Druck mit beweglichen Lettern, die Bibel erscheint um 1454. Seine Schrift ist die Textura, eine gotische Schrift. Er ahmt die Handschrift der Zeit nach.

**Renaissance:** Um 1400 suchen italienische Humanisten die Antike und finden karolingische Handschriften, die sie irrtümlich für antik halten. Sie schreiben sie nach und kombinieren sie mit den römischen Großbuchstaben. In Venedig gießt Nicolas Jenson um 1470 daraus eine Druckschrift. Das ist bis heute das Grundmuster unserer Schrift: zwei Schriften aus zwei Epochen, die erst nachträglich zusammengefügt wurden.

**Hintergrund**

Typografie kommt aus dem Griechischen: týpos (Schlag, Gepräge, Form) und gráphein (schreiben, ritzen).

Woher die Serifen kommen, ist umstritten. Edward Catich vertritt in »The Origin of the Serif« (1968) die These, dass die Buchstaben erst mit dem Pinsel auf den Stein vorgeschrieben und dann gemeißelt wurden. Die Schrift »Trajan« von Carol Twombly (Adobe, 1989) greift die Inschrift auf und ist heute auf vielen Filmplakaten zu sehen.

Zum Weiterlesen: Lupton, Thinking with Type (Letter), und Hans Peter Willberg, Wegweiser Schrift.

Bilder aus dem bisherigen Foliensatz Typographie, Foto der Inschrift: MumblerJamie, Wikimedia Commons, CC BY-SA 2.0.
''', transition='none') + '''{% interlude "Woher kommt unsere Schrift?", "Warum gibt es zwei Sorten Buchstaben?" %}

''' + '\n'.join([
  bild('historie-03.png', 'Erst Bilder: Ein Zeichen zeigt eine Sache<br><small>Ägyptische Hieroglyphen, ab ca. 3200 v. Chr.</small>', schatten=True),
  bild('historie-05.png', 'Dann Laute: Ein Zeichen steht für einen Laut<br><small>Griechisches Alphabet, ab ca. 800 v. Chr.</small>').replace('"width":"auto"', '"width":"80%"'),
  "{% screenshot \"./images/trajan-inschrift.jpg\", '{\"transition\":\"fade\", \"classes\":\"shadow\", \"width\":\"auto\", \"bu\":\"Capitalis Monumentalis: in Stein, nur Großbuchstaben<br><small>Trajanssäule, Rom, 113 n. Chr. Foto: MumblerJamie, Wikimedia Commons, CC BY-SA 2.0</small>\"}' %}",
  bild('historie-07.png', 'Capitalis Monumentalis: Hier kommen unsere Großbuchstaben her<br><small>Heutige Rekonstruktion</small>'),
  bild('historie-08.png', 'Mit der Feder: Capitalis Quadrata und Capitalis Rustica<br><small>Ab ca. 100 n. Chr.</small>'),
  bild('historie-09.png', 'Wer schnell schreibt, rundet: Aus A wird a, es entstehen Ober- und Unterlängen'),
  bild('historie-10.png', 'Karolingische Minuskel: Hier kommen unsere Kleinbuchstaben her<br><small>Um 800 n. Chr.</small>'),
  bild('mazarine-bibel-01.png', 'Gutenberg druckt mit beweglichen Lettern, in gotischer Textura<br><small>Gutenberg-Bibel, um 1454</small>'),
  bild('anatomie-01.png', 'Die Renaissance fügt beides zusammen: römische Großbuchstaben, karolingische Kleinbuchstaben<br><small>Renaissance-Antiqua, ab ca. 1470</small>').replace('"width":"auto"', '"width":"80%"'),
  bild('historie-11.png', 'Ein Buchstabe, 5000 Jahre: vom Rinderkopf zum a'),
]) + '''

{% statement "Unsere Schrift sind zwei Schriften.", "Die Großbuchstaben kommen aus Rom, die Kleinbuchstaben vom Hof Karls des Großen. Die Renaissance hat sie zusammengebracht." %}
''')

W(D, '030-gross-und-klein.md', kopf('Groß und klein', '''
Für dieselbe Sache gibt es mehrere Wörter. Alle drei Paare sollten Sie einmal gehört haben.

**Versalien** kommt vom Vers: In Handschriften wurde der erste Buchstabe eines Verses groß und oft farbig gesetzt. **Gemeine** sind die gewöhnlichen Buchstaben, aus denen der Text besteht.

**Majuskel und Minuskel** kommen aus dem Lateinischen: etwas größer, etwas kleiner.

**Upper case und lower case:** In englischen Druckereien lagen die Großbuchstaben im oberen Setzkasten, die Kleinbuchstaben im unteren. Daher kommt der Begriff bis in jede CSS-Datei: text-transform: uppercase.

Noch ein Begriff, den Sie brauchen: Kapitälchen sind Großbuchstaben in der Höhe der Kleinbuchstaben.

Bild aus dem bisherigen Foliensatz Typographie.
''') + bild('historie-13.png', 'Versalien: der große, oft farbige Anfangsbuchstabe eines Verses<br><small>Buchseite, 16. Jahrhundert</small>') + '''

<section class="simple" data-transition="fade">
<div>

# Drei Wörter für dasselbe

| | Großbuchstaben | Kleinbuchstaben |
|---|---|---|
| **In der Typografie** | Versalien | Gemeine |
| **In der Schriftgeschichte** | Majuskeln | Minuskeln |
| **Aus dem Setzkasten, bis ins CSS** | upper case | lower case |

</div>
</section>
''')

# ---------------------------------------------------------------- Begriffe: Umrisse aus rahmen-typografie-pfade.json
P = json.load(open('/Users/cnoss/git/privat/slides/tools/sdvk/bau/rahmen-typografie-pfade.json'))
K = '#231f20'; G = '#888888'; L = '#9313ce'; H = '#e4e4e4'
LABEL = 'font-family="sans-serif" font-size="20"'
GRAD = 150; X0 = 40; BASIS = 320  # Schriftgrad, Start und Grundlinie der großen Wortbilder
SK = GRAD / 1000

def wort(key, x, y, gr, fill=K, did=None):
    p = P[key]; s = gr / p['upm']
    # Kein data-id: Auto-Animate würde sonst das transform-Attribut überschreiben
    return f'<g transform="translate({x},{y}) scale({s:.4f})"><path d="{p["d"]}" fill="{fill}" /></g>\n'

def linie(did, y, farbe, label='', unten=False, x1=20, x2=880):
    t = ''
    if label:
        ty = y + 26 if unten else y - 10
        t = f'<text data-id="{did}-t" x="{x2}" y="{ty}" text-anchor="end" {LABEL} fill="{farbe}">{label}</text>\n'
    return f'<line data-id="{did}" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{farbe}" stroke-width="3" stroke-linecap="round" />\n' + t

m = P['typografie']
Y = {'basis': BASIS, 'xh': BASIS - m['xh'] * SK, 'cap': BASIS - m['cap'] * SK, 'ober': BASIS - m['ober'] * SK, 'unter': BASIS - m['unter'] * SK}
NAME = {'basis': 'Grundlinie', 'xh': 'x-Höhe', 'ober': 'Oberlänge', 'unter': 'Unterlänge', 'cap': 'Versalhöhe'}

def anatomie(aktiv, sichtbar):
    out = ''
    for k in sichtbar:
        out += linie(k, Y[k], L if k == aktiv else G, NAME[k], unten=(k in ('unter', 'cap', 'xh')))
    return out + wort('typografie', X0, BASIS, GRAD)

def fq(bu, svg):
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":900, \"h\":500, \"bu\":\"" + bu + "\"}' %}\n" + svg + "{% endframe %}"

# Punzen und Serifen
punzen = (wort('typografie', X0, BASIS, GRAD) +
          f'<g transform="translate({X0},{BASIS}) scale({SK:.4f})"><path d="{m["innen"]}" fill="{L}" /></g>\n')
ringe = ''.join(f'<circle data-id="ring{c}" cx="{X0 + x * SK:.1f}" cy="{BASIS - 4}" r="34" fill="none" stroke="{L}" stroke-width="3" />\n' for c, x in m['fuesse'].items())

v = P['versal']; SV = 900 * 0 + 118 / 1000  # Versalwort etwas kleiner, damit es ins Format passt
YV = 300; capv = YV - v['cap'] * SV
zwei = (linie('v-o', capv, L, x1=20, x2=880) + linie('v-u', YV, L, x1=20, x2=880) + wort('versal', 90, YV, 118))
vier = (linie('v-o', Y['ober'], G, x1=20, x2=880) + linie('v-x', Y['xh'], G, x1=20, x2=880) + linie('v-u', BASIS, G, x1=20, x2=880) +
        linie('v-d', Y['unter'], G, x1=20, x2=880) + wort('typografie', X0, BASIS, GRAD))

W(D, '040-anatomie.md', kopf('Die Linien der Schrift', '''
Jetzt die Wörter, die Sie brauchen, um über Schrift zu sprechen. Sie stecken in der Geschichte von eben.

Großbuchstaben stehen zwischen zwei Linien, wie in Rom (Zweilinienschrift). Kleinbuchstaben brauchen vier (Vierlinienschrift). Das ist auch der Grund, warum Text in Kleinbuchstaben lebendige Wortbilder hat und Text in Versalien nicht.

- **Grundlinie:** Darauf stehen die Buchstaben. Rundungen ragen minimal darunter (optische Korrektur).
- **x-Höhe, auch Mittellänge:** die Höhe der Kleinbuchstaben ohne Ober- und Unterlängen. Sie bestimmt am stärksten, wie groß eine Schrift wirkt.
- **Oberlänge:** was über die x-Höhe hinausragt: b, d, f, h, k, l, t.
- **Unterlänge:** was unter die Grundlinie reicht: g, j, p, q, y.
- **Versalhöhe:** die Höhe der Großbuchstaben. Oft etwas niedriger als die Oberlänge, damit Versalien im Text nicht zu laut werden. Das sieht man hier am f und am T.
- **Serife:** die kleinen Abschlussstriche an den Enden. Schriften ohne heißen serifenlos oder Grotesk.
- **Punze:** der Innenraum eines Buchstabens, geschlossen wie beim o oder offen wie beim n. Der Name kommt vom Stempel, mit dem der Innenraum in die Bleiletter geschlagen wurde. Zu kleine Punzen laufen bei kleiner Schrift zu.

Die Beschriftung in der Grafik ist hier eine bewusste Ausnahme: Die Wörter sind der Inhalt der Folie. Schrift: PT Serif, als Umrisse.

**Hintergrund**

Mehr zur Anatomie: Lupton, Thinking with Type (Letter). Die Einteilung von Schriften steht in den Bausteinen Schriftauswahl (fünf Gruppen für den Alltag) und Schriftklassifikation (DIN 16518 und Matrix Beinert).
''', transition='none') + '''{% interlude "Wie heißt das?", "Wer über Schrift reden will, braucht die Wörter" %}

''' + '\n'.join([
  fq('Großbuchstaben: alles zwischen zwei Linien, wie in Rom', zwei),
  fq('Kleinbuchstaben: vier Linien', vier),
  fq('Die Grundlinie: Darauf stehen die Buchstaben', anatomie('basis', ['basis']) ),
  fq('Die x-Höhe: so hoch wie das x, ohne Ober- und Unterlängen', anatomie('xh', ['basis', 'xh'])),
  fq('Die Oberlänge: was über die x-Höhe hinausragt', anatomie('ober', ['basis', 'xh', 'ober'])),
  fq('Die Unterlänge: was unter die Grundlinie reicht', anatomie('unter', ['basis', 'xh', 'ober', 'unter'])),
  fq('Die Versalhöhe: oft etwas niedriger als die Oberlänge', anatomie('cap', ['basis', 'xh', 'ober', 'unter', 'cap'])),
  fq('Serifen: die kleinen Abschlussstriche', wort('typografie', X0, BASIS, GRAD) + ringe),
  fq('Punzen: die Innenräume', punzen),
]) + '\n')

# ---------------------------------------------------------------- Durchschuss
GZ = 76; XZ = 40; KX2 = 720; OBEN = 90; DS = 44
BW = int(GZ * 0.78)  # Grundlinie liegt bei 78 % des Kegels
def zeilen(durch, schriftgrad=False, durchschuss=False, abstand=False):
    y1 = OBEN; y2 = OBEN + GZ + durch
    b1 = y1 + BW; b2 = y2 + BW; XM = KX2 + 18
    o = f'<rect data-id="k1" x="{XZ-10}" y="{y1}" width="{KX2-XZ+10}" height="{GZ}" fill="{H}" />\n'
    o += f'<rect data-id="k2" x="{XZ-10}" y="{y2}" width="{KX2-XZ+10}" height="{GZ}" fill="{H}" />\n'
    if durchschuss:
        o += f'<rect data-id="ds" x="{XZ-10}" y="{y1+GZ}" width="{KX2-XZ+10}" height="{durch}" fill="{L}" />\n'
    o += wort('zeile1', XZ, b1, GZ) + wort('zeile2', XZ, b2, GZ)
    def klammer(a, b, text, did):
        return (f'<line data-id="{did}" x1="{XM}" y1="{a}" x2="{XM}" y2="{b}" stroke="{L}" stroke-width="3" stroke-linecap="round" />\n'
                f'<text data-id="{did}-t" x="{XM+12}" y="{(a+b)/2+7:.0f}" {LABEL} fill="{L}">{text}</text>\n')
    if schriftgrad: o += klammer(y1, y1 + GZ, 'Schriftgrad', 'sg')
    if durchschuss: o += klammer(y1 + GZ, y2, 'Durchschuss', 'dk')
    if abstand:
        o += linie('b1', b1, L, x1=XZ-10, x2=KX2+18) + linie('b2', b2, L, x1=XZ-10, x2=KX2+18)
        o += klammer(b1, b2, 'Zeilenabstand', 'za')
    return o

W(D, '050-durchschuss.md', kopf('Schriftgrad, Zeilenabstand, Durchschuss', '''
Die letzten drei Wörter kommen direkt aus dem Bleisatz. Jeder Buchstabe war ein Stück Metall, der Klotz darunter heißt Kegel.

- **Schriftgrad:** die Höhe des Kegels, nicht die Höhe des Buchstabens. Deshalb wirken zwei Schriften im selben Schriftgrad unterschiedlich groß. Das ist bis heute so: font-size misst nicht die sichtbaren Buchstaben.
- **Kompress:** Die Kegel liegen direkt aufeinander, kein Metall dazwischen.
- **Durchschuss:** der zusätzliche Raum zwischen den Zeilen. Im Bleisatz wörtlich ein Metallstreifen, den man zwischen die Zeilen schob. Im Englischen heißt das leading, von lead, Blei.
- **Zeilenabstand:** von Grundlinie zu Grundlinie. Also Schriftgrad plus Durchschuss.

Im Browser: font-size 16 px und line-height 1.5 ergeben 24 px Zeilenabstand, also 8 px Durchschuss. CSS verteilt ihn je zur Hälfte über und unter die Zeile. Figma macht das genauso. Wie viel Zeilenabstand Lesetext braucht, steht im Baustein Lesetext.

x-Höhe im Vergleich: Times New Roman und Verdana im selben Schriftgrad. Die Verdana wirkt deutlich größer, weil ihre x-Höhe höher ist. Darum lässt sich die Größe einer Schrift nicht von einer Schrift auf die andere übertragen. Eine Schrift tauschen heißt: Größe und Zeilenabstand neu prüfen. In CSS gibt es dafür die Einheiten ex (x-Höhe) und cap (Versalhöhe) sowie font-size-adjust.

Bleibuchstabe aus dem bisherigen Foliensatz Typographie.
''', transition='none') + bild('bleibuchstabe.png', 'Ein Buchstabe aus Blei: Der Klotz heißt Kegel') + '''

''' + '\n'.join([
  fq('Schriftgrad: die Höhe des Kegels, nicht die des Buchstabens', zeilen(0, schriftgrad=True)),
  fq('Durchschuss: im Bleisatz ein Metallstreifen zwischen den Zeilen', zeilen(DS, schriftgrad=True, durchschuss=True)),
  fq('Zeilenabstand: von Grundlinie zu Grundlinie', zeilen(DS, abstand=True)),
]) + '''

{% statement "Zeilenabstand = Schriftgrad + Durchschuss", "font-size: 16 px, line-height: 1.5. Das ergibt 24 px Zeilenabstand, also 8 px Durchschuss." %}

''' + (lambda t, ve: fq('Gleicher Schriftgrad, andere x-Höhe: Die rechte Schrift wirkt größer',
      f'<line data-id="gl" x1="20" y1="320" x2="880" y2="320" stroke="{G}" stroke-width="3" stroke-linecap="round" />\n' +
      f'<line data-id="xt" x1="20" y1="{320 - t["xh"] / t["upm"] * 130:.1f}" x2="405" y2="{320 - t["xh"] / t["upm"] * 130:.1f}" stroke="{L}" stroke-width="3" stroke-linecap="round" />\n' +
      f'<line data-id="xv" x1="430" y1="{320 - ve["xh"] / ve["upm"] * 130:.1f}" x2="880" y2="{320 - ve["xh"] / ve["upm"] * 130:.1f}" stroke="{L}" stroke-width="3" stroke-linecap="round" />\n' +
      wort('times', 40, 320, 130) + wort('verdana', 450, 320, 130)))(P['times'], P['verdana']) + '''

<section class="simple" data-transition="fade">
<div>

# Dieselben Wörter im Werkzeug

| Begriff | CSS | Figma |
|---|---|---|
| **Schriftgrad** | font-size | Size |
| **Zeilenabstand** | line-height | Line height |
| **Versalien** | text-transform: uppercase | Case: Uppercase |
| **Grundlinie** | align-items: baseline | Auto Layout: Text baseline |
| **x-Höhe, Versalhöhe** | Einheiten ex und cap | |

</div>
</section>
''')

# ---------------------------------------------------------------- Überleitung
W(D, '060-drei-schritte.md', kopf('Drei Fragen', '''
Die drei Fragen, an denen sich die Bausteine zu Schrift entlanghangeln.

**Auswählen:** Wirkung von Schrift, Methode Schriftauswahl.

**Gliedern und Anordnen:** Typografische Hierarchie, Methode Typografische Skala.

**Lesbar machen:** Lesetext, Satz.

Vorab ein kurzer Test, warum das alles überhaupt funktioniert: Wortbilder.
''') + liste('Drei Fragen an jede Schrift', [
  '<strong>Auswählen:</strong> Welche Schrift passt zu Zweck und Wirkung?',
  '<strong>Gliedern und Anordnen:</strong> Was ist wichtig, was gehört zusammen?',
  '<strong>Lesbar machen:</strong> Kommt der Text bequem an?',
]) + '\n')
open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Typografie"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Rahmen"
gruppe: ""
tiefe: ""
einsatz: "Einstieg in die Bausteine zu Schrift"
kurzsatz: "Typografie ist Auswählen, Gliedern, Anordnen und logisch Lesbarmachen von Schrift. Unsere Schrift verbindet römische Großbuchstaben mit karolingischen Kleinbuchstaben"
begriffe: ["Typografie", "Capitalis Monumentalis", "Karolingische Minuskel", "Versalien", "Gemeine", "Grundlinie", "x-Höhe", "Oberlänge", "Unterlänge", "Versalhöhe", "Serife", "Punze", "Schriftgrad", "Zeilenabstand", "Durchschuss"]
herkunft: "U: textsatz/005, typographie/030, 040, 050"
inhalt:
  - "Definition nach Weidemann"
  - "Kurze Geschichte der Schrift"
  - "Großbuchstaben und Kleinbuchstaben"
  - "Anatomie: Grundlinie, x-Höhe, Ober- und Unterlänge, Serife, Punze"
  - "Schriftgrad, Zeilenabstand, Durchschuss"
  - "Drei Fragen an jede Schrift"
status: ok
---
''')
print('fertig', D)
