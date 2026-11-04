exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'methode-typografische-skala'
intro(D, 'Typografische Skala', 'Methode // Konstruieren')
def stufen(ratio, n=5, basis=16):
    return [round(basis * ratio ** i) for i in range(n)]
def probe(ratio, n=5, faktor=0.2, label=True):
    # Darstellung proportional zur Foliengröße: 16 px der Skala entsprechen faktor * 16 vh
    o = []
    for px in reversed(stufen(ratio, n)):
        o.append(f'<div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">{px}</span><span style="font-family:PTsans;font-size:{px * faktor:.2f}vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div>')
    return '<div style="display:flex;flex-direction:column;gap:.6vh;">' + ''.join(o) + '</div>'

W(D, '005-problem.md', kopf('Das Problem', '''
Ohne System sammeln sich die Größen an: 13, 14, 15, 17, 19, 22, 23, 28. Der Unterschied zwischen 22 und 23 ist unsichtbar, und trotzdem muss jemand ihn pflegen. Die Hierarchie wird nicht klarer, sondern unruhiger.

Eine Skala begrenzt die Auswahl. Dann ist die Frage nicht mehr »Wie groß?«, sondern »Welche Stufe?«.
''') + '''{% interlude "13, 14, 15, 17, 19, 22, 23, 28", "Sehen Sie den Unterschied zwischen 22 und 23?" %}

{% statement "Wenige Größen, festes Verhältnis.", "Dann ist die Frage nicht mehr: Wie groß? Sondern: Welche Stufe?" %}
''')

W(D, '010-ergebnis.md', kopf('Ergebnis zuerst', '''
So sieht eine Skala aus: Grundgröße 16, jede Stufe das 1,25-Fache der vorigen, gerundet. Fünf Stufen reichen für die meisten Screens.

Die Zahlen links sind Pixel. Auf der Folie ist alles proportional vergrößert.
''') + beispiel('Grundgröße 16, Faktor 1,25', probe(1.25)) + '\n')

W(D, '020-schritte.md', kopf('Schritte', '''
**1. Grundgröße festlegen:** Das ist die Größe des Fließtexts, im Web meist 16 px (1 rem).

**2. Faktor wählen:** Kleine Faktoren (1,125 bis 1,2) für dichte Oberflächen, in denen viel auf den Screen muss. Größere (1,25 bis 1,5) für Inhaltsseiten mit deutlicher Hierarchie.

**3. Stufen berechnen und runden:** Grundgröße mal Faktor, immer wieder. Auf ganze Zahlen runden.

**4. Stufen zuweisen:** Jede Lesestufe bekommt eine Größe, nicht jede Größe muss vorkommen.

**In Figma** als Text Styles anlegen, **im Code** als Variablen. Dann gibt es nur noch diese Größen.

**Hintergrund**

Die Idee stammt aus der Buchtypografie: Die klassische Skala der Bleisatz-Schriftgrade (6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 21, 24, 36, 48, 60, 72) beschreibt Robert Bringhurst in »The Elements of Typographic Style« (1992). Fürs Web hat Tim Brown den Begriff der modularen Skala bekannt gemacht (»More Meaningful Typography«, A List Apart, 2011). Wathan und Schoger raten in »Refactoring UI« (2018) dagegen zu einer handverlesenen Skala, weil mathematisch berechnete Stufen zu krummen Werten führen. Beides funktioniert. Wichtig ist nur, dass es eine feste Auswahl gibt.
''') + liste('Eine Skala in vier Schritten', [
  '<strong>1. Grundgröße festlegen:</strong> die Größe des Fließtexts, im Web meist 16 px',
  '<strong>2. Faktor wählen:</strong> kleiner für dichte Oberflächen, größer für Inhaltsseiten',
  '<strong>3. Berechnen und runden:</strong> Grundgröße mal Faktor, immer wieder',
  '<strong>4. Zuweisen:</strong> Jede Lesestufe bekommt eine Größe',
]) + '\n\n' + beispiel('Drei Faktoren<br><small>Von links: 1,125 (dicht), 1,25 (ausgewogen), 1,5 (deutlich)</small>', '<div style="display:flex;gap:4vw;align-items:flex-end;">' + ''.join(f'<div>{probe(r, 5, 0.11)}</div>' for r in [1.125, 1.25, 1.5]) + '</div>') + '\n')

CODE = ''':root {
  --text-base: 1rem;     /* 16 px, Fließtext */
  --text-m:    1.25rem;  /* 20 px, Lead */
  --text-l:    1.5625rem; /* 25 px, Zwischentitel */
  --text-xl:   1.9375rem; /* 31 px, Headline klein */
  --text-2xl:  2.4375rem; /* 39 px, Headline groß */
}'''
W(D, '030-im-code.md', kopf('Im Code', '''
Die Skala als Variablen. Dann steht im Code keine Größe mehr, sondern eine Stufe. In Figma entspricht das den Text Styles.

**Für alle:** Größen in `rem` statt `px` angeben. So greift die im Browser eingestellte Schriftgröße, und Menschen, die größere Schrift brauchen, bekommen sie. WCAG 1.4.4 verlangt, dass sich Text ohne Hilfsmittel auf 200 % vergrößern lässt, ohne dass Inhalte oder Funktionen verloren gehen.
''') + code('Dieselbe Skala im Code', CODE, 2.8) + '''

{% statement "rem statt px.", "So greift die im Browser eingestellte Schriftgröße. Wer größere Schrift braucht, bekommt sie." %}
''')

W(D, '040-fehler.md', kopf('Typische Fehler', '''
Der häufigste Fehler: zu viele Stufen und zu kleine Abstände zwischen ihnen. Wenn zwei Stufen nicht sofort unterscheidbar sind, ist eine zu viel.

Tiefe: kennen. Eine Skala brauchen Sie spätestens im Projekt, wenn mehr als ein Screen entsteht.
''', cls='simple') + '''{% fragment '<p class="list">Zu viele Stufen: Zwei, die man nicht unterscheiden kann, sind eine zu viel</p>' %}
{% fragment '<p class="list">Krumme Werte stehen lassen: 15,63 px braucht niemand</p>' %}
{% fragment '<p class="list">Skala definieren und dann doch frei Größen eintippen</p>' %}
{% fragment '<p class="list">Nur am Desktop testen: Auf dem Handy ist 39 px schnell zu groß</p>' %}
''')

W(D, '050-einsatz.md', kopf('Einsatz', '''
Die Skala entsteht, wenn die Schrift gewählt ist und mehr als ein Screen gestaltet wird. Sie ist das Gegenstück zum Spacing-System bei den Abständen. Im Projekt gehört sie in die Text Styles.
''') + liste('Wo die Methode wiederkommt', [
  'Im Projekt: als Text Styles in Figma',
  'In der Übergabe an die Entwicklung: als Variablen',
  'Zusammen mit dem Spacing-System: dieselbe Idee für Abstände',
]) + '''

{% statement "Merksatz", "Wenige Größen, festes Verhältnis. Wer zwei Stufen nicht unterscheiden kann, braucht nur eine." %}
''')
done(D, 'Schriftgrößen in festem Verhältnis festlegen, statt sie einzeln zu wählen', 'Typografische Skala, Grundgröße, Faktor, Text Style, rem')
index(D, ['Ergebnis zuerst: fünf Stufen', 'Vier Schritte', 'Drei Faktoren', 'Skala im Code', 'Typische Fehler'], 'Sobald mehr als ein Screen entsteht')
print('fertig', D)
