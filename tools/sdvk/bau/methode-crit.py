# Bauskript methode-crit. Aufruf: python3 tools/sdvk/bau/methode-crit.py
import glob, os
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'methode-crit'
os.makedirs(f'{NEW}/{D}', exist_ok=True)
for f in glob.glob(f'{NEW}/{D}/[0-9]*.md'): os.remove(f)
intro(D, 'Crit', 'Methode // Entscheiden und Kritik')

K = '#231f20'; HL = '#888888'; G2 = '#d9d9d9'; FL = '#e4e4e4'; BI = '#c4c4c4'; TX = '#aaaaaa'; L = '#9313ce'

# ---------------------------------------------------------------- Gemeinsames Beispiel: Startseite als Grayscale-Wireframe, 900 x 500
def wireframe(markiert=False):
    o = ''
    o += f'<rect data-id="nav" x="60" y="34" width="110" height="14" fill="{HL}" />\n'
    for i in range(4):
        o += f'<rect data-id="n{i}" x="{560 + i * 75}" y="37" width="55" height="8" fill="{G2}" />\n'
    o += f'<rect data-id="bild" x="60" y="80" width="430" height="230" fill="{BI}" />\n'
    o += f'<rect data-id="h1" x="520" y="96" width="300" height="24" fill="{HL}" />\n'
    o += f'<rect data-id="h1b" x="520" y="130" width="220" height="24" fill="{HL}" />\n'
    for i, w in enumerate([320, 320, 300, 240]):
        o += f'<rect data-id="t{i}" x="520" y="{180 + i * 20}" width="{w}" height="10" fill="{G2}" />\n'
    # Der Button ist so grau wie der Text: Er geht unter. Das ist der Gegenstand der Kritik.
    o += f'<rect data-id="btn" x="520" y="272" width="120" height="34" rx="17" fill="{G2}" />\n'
    for i in range(3):
        x = 60 + i * 285
        o += f'<rect data-id="k{i}" x="{x}" y="340" width="265" height="96" fill="{FL}" />\n'
        o += f'<rect data-id="kb{i}" x="{x + 16}" y="356" width="70" height="64" fill="{BI}" />\n'
        o += f'<rect data-id="kt{i}" x="{x + 102}" y="362" width="140" height="10" fill="{TX}" />\n'
        o += f'<rect data-id="ku{i}" x="{x + 102}" y="382" width="110" height="8" fill="{TX}" />\n'
    if markiert:
        o += f'<rect data-id="ring" x="508" y="262" width="144" height="54" rx="27" fill="none" stroke="{L}" stroke-width="4" />\n'
    return o

def fr(bu, inner, animate=True):
    a = '' if animate else ', "animate":false'
    return "{% frame '{\"stage\":\"#ffffff\", \"w\":900, \"h\":500" + a + ", \"bu\":\"" + bu + "\"}' %}\n" + inner + "{% endframe %}"

def html(titel, inhalt, transition='fade'):
    return f'<section class="simple" data-transition="{transition}">\n<div>\n\n# {titel}\n\n{inhalt}\n\n</div>\n</section>'

# ---------------------------------------------------------------- 005 Problem, Einstieg als Zuordnungsfrage
W(D, '005-problem.md', kopf('Drei Rückmeldungen', '''
**Einstieg als Zuordnungsfrage (ca. 3 Minuten).** Ein Entwurf, eine Startseite als Wireframe. Gedacht ist sie, damit sich Besucherinnen und Besucher für eine Veranstaltung anmelden. Dann drei Rückmeldungen zum selben Entwurf, nacheinander eingeblendet. Fragen: Welche hilft dem Entwurf weiter? Und was unterscheidet die drei?

Auflösung:

- **A** ist eine **Reaktion**. Sie sagt etwas über die Person, die sie gibt, nichts über den Entwurf. Man weiß danach nicht, was zu tun ist.
- **B** ist eine **Anweisung**. Sie schreibt eine Lösung vor, ohne das Problem zu nennen. Vielleicht ist die Lösung gut, vielleicht nicht, prüfen kann man es nicht. Und Rot bringt neue Probleme mit.
- **C** ist **Kritik**. Sie nennt das Ziel, beobachtet ein Element und erklärt, warum es dem Ziel im Weg steht. Die Lösung bleibt bei denen, die gestalten.

**Hintergrund**

Die Unterscheidung stammt von Adam Connor und Aaron Irizarry, »Discussing Design. Improving Communication and Collaboration through Critique« (O'Reilly, 2015). Sie unterscheiden reaktionsbasiertes Feedback (reaction-based), anweisungsbasiertes Feedback (direction-based) und Kritik (critique). Nur Kritik analysiert einen Entwurf gegen seine Ziele. Passt zur Haltung »Gefällt mir ist kein Argument« (siehe Beobachten und Begründen).
''', transition='none') + '''{% interlude "Welche Rückmeldung hilft?", "Ein Entwurf, drei Sätze" %}

''' + fr('Ein Entwurf: Die Startseite soll zur Anmeldung führen', wireframe(), animate=False) + '''

<section class="simple" data-transition="fade">
  <div>
    <h1>Drei Rückmeldungen zum selben Entwurf</h1>
    {% fragment '<p class="list"><strong>A:</strong> »Irgendwie gefällt mir das nicht so.«</p>' %}
    {% fragment '<p class="list"><strong>B:</strong> »Mach den Button größer und rot.«</p>' %}
    {% fragment '<p class="list"><strong>C:</strong> »Die Seite soll zur Anmeldung führen. Der Button ist aber so grau wie der Fließtext, er geht unter.«</p>' %}
  </div>
</section>

{% statement "Reaktion, Anweisung, Kritik.", "A sagt etwas über die Person, B schreibt eine Lösung vor. Nur C misst den Entwurf an seinem Ziel. Das ist eine Crit: Kritik mit Ziel, Ablauf und gemeinsamem Vokabular." %}
''')

# ---------------------------------------------------------------- 010 Ergebnis zuerst
W(D, '010-ergebnis.md', kopf('So klingt Kritik', '''
So sieht das Ergebnis einer guten Rückmeldung aus: vier Teile, immer in dieser Reihenfolge. Erst das Ziel, dann was dem Ziel hilft, dann was ihm im Weg steht, jeweils mit Begründung. Zum Schluss eine Frage statt einer fertigen Lösung.

Das Lob am Anfang ist keine Höflichkeitsfloskel. Es sagt den Gestaltenden, was sie behalten sollen. Wer nur Fehler hört, wirft im Zweifel auch das Gelungene weg.

Am Beispiel: Die große Headline und die klare Aufteilung in Bild links, Text rechts unterstützen das Ziel. Der Button arbeitet dagegen, er hat denselben Grauwert wie der Fließtext und hebt sich nicht ab (siehe Kontrast und Hervorhebung).
''', transition='none') + '''{% interlude "So klingt Kritik", "Ziel, Stärke, Schwäche, Frage" %}

''' + html('Eine Rückmeldung in vier Teilen', '''{% fragment '<p class="list"><strong>Ziel:</strong> »Die Seite soll zur Anmeldung führen.«</p>' %}
{% fragment '<p class="list"><strong>Das hilft:</strong> »Die große Headline zieht den Blick sofort, Bild und Text sind klar getrennt.«</p>' %}
{% fragment '<p class="list"><strong>Das steht im Weg:</strong> »Der Button ist so grau wie der Fließtext und geht unter.«</p>' %}
{% fragment '<p class="list"><strong>Frage:</strong> »Was wäre, wenn der Button das einzige dunkle Element auf der Seite wäre?«</p>' %}''') + '''

''' + fr('Das steht im Weg: Der Button hat denselben Grauwert wie der Text', wireframe(markiert=True), animate=False) + '\n')

# ---------------------------------------------------------------- 020 Ablauf
W(D, '020-ablauf.md', kopf('Der Ablauf', '''
Sechs Schritte. Die ersten beiden gehören den Präsentierenden, die nächsten drei den Kritisierenden, der letzte wieder den Präsentierenden.

**1. Kontext und Ziel:** Was soll der Entwurf erreichen, für wen? In welcher Stufe ist er, Skizze oder fast fertig? Und welche Art Feedback wird gesucht? Wer das nicht sagt, bekommt Feedback zu Dingen, die gar nicht zur Diskussion stehen.

**2. Zeigen:** ohne lange Vorrede und ohne sich vorab zu rechtfertigen.

**3. Beobachten:** Erst beschreiben, was zu sehen ist, dann bewerten. Das Werkzeug dafür kennen Sie: das Beschreibungsraster.

**4. Bewerten:** gegen das Ziel, nicht gegen den eigenen Geschmack. Was funktioniert, was nicht, und warum? Mit dem Vokabular der Prinzipien.

**5. Fragen:** »Was wäre, wenn …?« statt »Mach mal …«. Die Lösung bleibt bei denen, die gestalten.

**6. Zusammenfassen:** Die Präsentierenden fassen in zwei Sätzen zusammen, was sie mitnehmen. Sie entscheiden, was sie übernehmen. Kritik ist ein Angebot, kein Auftrag.

**Moderation:** achtet auf Zeit und Reihenfolge und holt zurück, wer vom Ziel abschweift.

**Hintergrund**

Der Ablauf folgt in den Grundzügen Connor und Irizarry (2015), die einen festen Rahmen aus Ziel, Beobachtung, Bewertung und Gespräch empfehlen. Die Rollen sind an die Praxis in Designstudios und Agenturen angelehnt.
''') + '''{% interlude "Der Ablauf", "Sechs Schritte, drei Rollen" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>In sechs Schritten</h1>
    {% fragment '<p class="list"><strong>1. Kontext und Ziel:</strong> Was soll der Entwurf erreichen, für wen, in welcher Stufe?</p>' %}
    {% fragment '<p class="list"><strong>2. Zeigen:</strong> ohne Rechtfertigung</p>' %}
    {% fragment '<p class="list"><strong>3. Beobachten:</strong> erst beschreiben, was zu sehen ist</p>' %}
    {% fragment '<p class="list"><strong>4. Bewerten:</strong> gegen das Ziel, mit Begründung</p>' %}
    {% fragment '<p class="list"><strong>5. Fragen:</strong> »Was wäre, wenn …?« statt »Mach mal …«</p>' %}
    {% fragment '<p class="list"><strong>6. Zusammenfassen:</strong> Die Präsentierenden entscheiden, was sie übernehmen.</p>' %}
  </div>
</section>

<section class="simple" data-transition="fade">
<div>

# Drei Rollen

| Rolle | Aufgabe | Schritte |
|---|---|---|
| **Präsentierende** | Ziel nennen, zeigen, zuhören, zusammenfassen | 1, 2, 6 |
| **Kritisierende** | beobachten, gegen das Ziel bewerten, fragen | 3, 4, 5 |
| **Moderation** | Zeit und Reihenfolge halten, zum Ziel zurückholen | alle |

</div>
</section>
''')

# ---------------------------------------------------------------- 030 Vokabular
W(D, '030-vokabular.md', kopf('Ein gemeinsames Vokabular', '''
Die Leitfragen der Prinzipiengruppen sind eine Prüfliste für jede Crit. Nicht alle Fragen passen zu jedem Entwurf: Sie wählen die zwei oder drei, die zum Ziel passen. Die Begriffe dazu haben Sie in den Prinzipien gelernt, und genau die machen eine Rückmeldung präzise: Statt »wirkt irgendwie unruhig« heißt es dann »die Abstände zwischen den Karten sind so groß wie die innerhalb, die Gruppen zerfallen«.

Die Spalte rechts verweist auf Bausteine, in denen Sie die Begriffe nachschlagen können.
''') + '''{% interlude "Ein gemeinsames Vokabular", "Die Leitfragen als Prüfliste" %}

<section class="simple" data-transition="fade">
<div>

# Leitfragen für die Crit

| Leitfrage | Zum Nachschlagen |
|---|---|
| **Was kann weg?** | [Reduzieren](../prinzip-reduzieren/) |
| **Was gehört zusammen?** | [Nähe und Abstand](../prinzip-naehe-und-abstand/) |
| **Wie hängt alles zusammen?** | [Ausrichtung und Raster](../prinzip-ausrichtung-und-raster/) |
| **Was ist wichtig?** | [Hierarchie](../prinzip-hierarchie/) |
| **Wie viel wovon?** | [Kontrast und Hervorhebung](../prinzip-kontrast-und-hervorhebung/) |
| **Welcher Charakter?** | [Farbwirkung](../prinzip-farbwirkung/), [Wirkung von Schrift](../prinzip-schrift-wirkung/) |
| **Kommt es an?** | [Lesetext](../prinzip-lesetext/), [Farbe und Lesbarkeit](../prinzip-farbe-und-lesbarkeit/) |
| **Kann man damit umgehen?** | Bedienbarkeit, folgt im Projekt |

</div>
</section>
''')

# ---------------------------------------------------------------- 035 Verantwortung
W(D, '035-verantwortung.md', kopf('Wem nützt das?', '''
Eine feste Runde in jeder Crit, kurz, aber nie weggelassen. Vier Fragen, die nicht nach schön oder hässlich fragen, sondern danach, was ein Entwurf mit Menschen macht.

Oft lautet die Antwort »passt«. Dann ist die Runde nach einer Minute vorbei. Manchmal fällt dabei aber auf, dass ein Formular mehr Daten abfragt als nötig, dass ein Ablehnen-Button kaum zu sehen ist oder dass eine Bildwelt nur eine Sorte Mensch zeigt. Genau dafür ist die Runde da.

**Hintergrund**

Die vier Fragen sind die Prüffragen aus dem roten Faden Verantwortung dieses Moduls. Zum Weiterlesen: Harry Brignull, »Deceptive Patterns« (2023), und Sara Wachter-Boettcher, »Technically Wrong« (2017).
''') + '''{% interlude "Wem nützt das?", "Eine feste Runde in jeder Crit" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Vier Fragen an jeden Entwurf</h1>
    {% fragment '<p class="list"><strong>Wem nützt das?</strong> Den Nutzenden oder nur dem Anbieter?</p>' %}
    {% fragment '<p class="list"><strong>Wer ist ausgeschlossen?</strong> Wer kann es nicht lesen, nicht bedienen, findet sich nicht wieder?</p>' %}
    {% fragment '<p class="list"><strong>Was wird verschwiegen?</strong> Kosten, Bedingungen, der Weg zum Kündigen?</p>' %}
    {% fragment '<p class="list"><strong>Was passiert mit den Daten?</strong> Wird nur gefragt, was wirklich gebraucht wird?</p>' %}
  </div>
</section>
''')

# ---------------------------------------------------------------- 040 Haltung
W(D, '040-haltung.md', kopf('Kritik gilt der Arbeit', '''
Zwei Seiten derselben Haltung.

**Für Kritisierende:** Kritik gilt der Arbeit, nicht der Person. »Der Button geht unter« statt »Du hast den Button versteckt«. Und Feedback gilt dem Entwurf in seinem Kontext: Ändert sich das Ziel, ändert sich auch die Kritik. Das ist kein Widerspruch, sondern genau der Punkt.

**Für Präsentierende:** Begründen statt beschreiben, wenn Sie Ihren Entwurf zeigen. Danach zuhören statt verteidigen. Wer jede Anmerkung sofort erklärt, hört nicht mehr, was die anderen sehen. Notieren, nachfragen, am Ende entscheiden.

**Hintergrund**

»Kritik gilt der Arbeit, nicht der Person« ist eine Grundregel bei Connor und Irizarry (2015) und in vielen Designstudios. Sie gilt in beide Richtungen: Auch wer präsentiert, nimmt Kritik nicht als Urteil über sich.
''') + '''{% interlude "Kritik gilt der Arbeit, nicht der Person.", "Und das in beide Richtungen" %}

{% statement "Begründen statt beschreiben. Zuhören statt verteidigen.", "Wer kritisiert, spricht über den Entwurf und sein Ziel. Wer präsentiert, nennt das Ziel, hört zu und entscheidet am Ende selbst, was er oder sie übernimmt." %}
''')

# ---------------------------------------------------------------- 050 Übung
KARTEN = ['Das Ziel ist …', 'Mir fällt auf …', 'Das unterstützt das Ziel, weil …', 'Das arbeitet dagegen, weil …', 'Was wäre, wenn …?']
karten = ''.join(
    f'<div style="flex:1 1 30%;min-width:0;background:{FL if i != 4 else L};color:{K if i != 4 else "#ffffff"};padding:2.2vh 1.4vw 3.4vh;font-family:IBM;font-size:3vh;line-height:1.25;text-align:left;font-weight:500;">{t}</div>'
    for i, t in enumerate(KARTEN))
W(D, '050-uebung.md', kopf('Mini-Übung', '''
**Mini-Übung (ca. 10 Minuten)**

Dreiergruppen. Jede Person bringt einen Entwurf aus einer der letzten Übungen mit, auf dem Rechner oder ausgedruckt. Drei Runden à drei Minuten, die Rollen rotieren: Wer präsentiert, nennt in einem Satz das Ziel und zeigt. Wer kritisiert, nutzt die Satzanfänge. Wer moderiert, achtet auf die Zeit und darauf, dass niemand Lösungen diktiert.

Die Satzanfänge auf der Folie stehen lassen oder als Karten verteilen. Die lila Karte ist die wichtigste: Sie ersetzt »Mach mal …«.

Nachbesprechung (1 Minute): Was war schwer? Meist: das Ziel in einem Satz zu nennen und beim Kritisieren keine Lösung vorzuschlagen.
''') + '''{% interlude "Und jetzt Sie.", "Dreiergruppen, zehn Minuten" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>So geht es</h1>
    {% fragment '<p class="list">Dreiergruppen, jede Person hat einen Entwurf aus einer Übung dabei</p>' %}
    {% fragment '<p class="list">Drei Runden à drei Minuten: präsentieren, kritisieren, moderieren</p>' %}
    {% fragment '<p class="list">Nach jeder Runde wechseln die Rollen</p>' %}
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>Satzanfänge für die Kritik</h1>
    <div style="display:flex;flex-wrap:wrap;gap:1.2vw;width:100%;">''' + karten + '''</div>
  </div>
</section>
''')

# ---------------------------------------------------------------- 060 Fehler
W(D, '060-fehler.md', kopf('Typische Fehler', '''
Der häufigste Fehler im Studium: Es wird gar kein Ziel genannt, also wird nach Geschmack bewertet. Der zweithäufigste: Kritisierende schlagen sofort ihre eigene Lösung vor. Und auf der anderen Seite: Präsentierende erklären jede Entscheidung, bevor überhaupt jemand gefragt hat.

Nur Lob ist genauso wenig hilfreich wie nur Kritik. Beides sagt nicht, was bleiben und was sich ändern soll.
''', cls='simple') + '\n'.join("{% fragment '<p class=\"list\">" + p + "</p>' %}" for p in [
  'Kein Ziel genannt: Dann bleibt nur Geschmack',
  'Geschmack statt Ziel: »gefällt mir« ist keine Kritik',
  'Lösungen diktieren statt Fragen stellen',
  'Alles auf einmal: Zwei, drei Punkte reichen',
  'Verteidigen statt zuhören',
  'Nur Negatives oder nur Lob',
]) + '\n')

# ---------------------------------------------------------------- 070 Einsatz
W(D, '070-einsatz.md', kopf('Einsatz', '''
Crit ist eine Können-Methode. Sie kehrt immer wieder: bei jedem Zusammentragen in einem Workshop, bei Präsentationen von Portfolio und Zwischenständen und in den Crits im Projekt. Je öfter, desto selbstverständlicher.

Dahinter: Beobachten und Begründen. Werkzeug für Schritt 3: Beschreibungsraster. Hilfen für Schritt 4: Unschärfe- und Graustufentest, Kontrast prüfen.
''') + '''<section class="simple" data-transition="fade">
  <div>
    <h1>Wo die Methode wiederkommt</h1>
    {% fragment '<p class="list">Beim Zusammentragen in jedem Workshop</p>' %}
    {% fragment '<p class="list">Bei Präsentationen von Portfolio und Zwischenständen</p>' %}
    {% fragment '<p class="list">In den Crits im Projekt</p>' %}
  </div>
</section>

{% statement "Merksatz", "Erst das Ziel, dann beobachten, dann bewerten, dann fragen. Kritik gilt der Arbeit, und die Entscheidung bleibt bei denen, die gestalten." %}

{% statement "Verweise", "Dahinter: [Beobachten und Begründen](../haltung-beobachten-und-begruenden/). Für Schritt 3: [Beschreibungsraster](../methode-beschreibungsraster/). Für Schritt 4: [Unschärfe- und Graustufentest](../methode-unschaerfetest/) und [Kontrast prüfen](../methode-kontrast-pruefen/)." %}
''')

if os.path.exists(f'{NEW}/{D}/010-inhalt.md'): os.remove(f'{NEW}/{D}/010-inhalt.md')
open(f'{NEW}/{D}/index.md', 'w').write('''---
title: "Crit"
layout: presentation.11ty.js
slideClasses: outro
transition: convex
typ: "Methode"
gruppe: "Entscheiden und Kritik"
tiefe: "können"
einsatz: "Bei jeder Präsentation und jedem Zusammentragen von Entwürfen"
kurzsatz: "Designkritik mit festem Ablauf und gemeinsamem Vokabular: erst das Ziel, dann beobachten, dann gegen das Ziel bewerten, dann fragen"
begriffe: ["Crit", "Kritik", "Reaktion", "Anweisung", "Gestaltungsziel", "Leitfragen"]
herkunft: "N"
inhalt:
  - "Reaktion, Anweisung, Kritik"
  - "Eine Rückmeldung in vier Teilen"
  - "Ablauf in sechs Schritten, drei Rollen"
  - "Leitfragen der Prinzipien als Prüfliste"
  - "Verantwortungsfragen"
  - "Mini-Übung mit Satzanfängen"
status: ok
---
''')
print('fertig', D)
