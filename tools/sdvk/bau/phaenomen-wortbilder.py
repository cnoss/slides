exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/deckbau.py').read())
exec(open('/Users/cnoss/git/privat/slides/tools/sdvk/typo.py').read())
D = 'phaenomen-wortbilder'
intro(D, 'Wortbilder', 'Phänomen // Lesen')
GROSS = 'font-family:PTserif;font-size:5vh;line-height:1.4;text-align:left;margin:0;hyphens:none;'

W(D, '010-test.md', kopf('Der Test', '''
**Live-Test (ca. 1 Minute):** Text einblenden und laut mitlesen lassen. Fast alle schaffen das, und zwar ziemlich flüssig, obwohl kaum ein Wort richtig geschrieben ist.

Danach die zweite Fassung: dieselben Wörter, aber auch der erste und der letzte Buchstabe sind vertauscht. Plötzlich geht es kaum noch. Dann die Auflösung im Klartext.
''') + '''{% interlude "Können Sie das lesen?", "Laut mitlesen, bitte." %}

''' + beispiel('Erster Versuch', f'<p style="{GROSS}">Biem Leesn ekrenenn wir gnaze Wröter. Es ist nchit so whictig, in wlehcer Rienhnelfoge die Bcuhstbaen sethen, solnage der estre und der ltzete an der rhictgien Stlele snid.</p>') + '\n\n'
+ beispiel('Zweiter Versuch', f'<p style="{GROSS}">Ibem Eesnl enneerkn riw negza Erwtör. Se ist thicn os iwhgtic, ni echlewr Ehneifloneg ied Thabcsueb eehnst, gnaloes red esert dnu red zettel na red itgichren Elelts dins.</p>', 'none') + '\n\n'
+ beispiel('Im Klartext', f'<p style="{GROSS}">Beim Lesen erkennen wir ganze Wörter. Es ist nicht so wichtig, in welcher Reihenfolge die Buchstaben stehen, solange der erste und der letzte an der richtigen Stelle sind.</p>', 'none') + '\n')

W(D, '020-mechanismus.md', kopf('Was ist passiert?', '''
Geübte Leserinnen und Leser gehen nicht Buchstabe für Buchstabe vor. Sie erfassen Wörter und Wortgruppen als Einheit und ergänzen aus dem Zusammenhang. Deshalb stört ein Dreher im Wortinneren kaum, und deshalb überliest man Tippfehler im eigenen Text.

**Hintergrund, und eine Warnung**

Der Text aus dem ersten Versuch geht auf eine Kettenmail von 2003 zurück, die sich auf eine angebliche Studie der Universität Cambridge beruft. Diese Studie gibt es nicht. Der Effekt ist trotzdem echt, aber kleiner als behauptet: Rayner, White, Johnson und Liversedge (»Raeding Wrods With Jubmled Lettres«, Psychological Science, 2006) messen, dass vertauschte Buchstaben das Lesen deutlich verlangsamen, im Wortinneren am wenigsten, am Wortanfang am stärksten. Frühe Arbeiten dazu stammen von Graham Rawlinson (Dissertation, 1976).

Auch das Wort »Wortbild« ist eine Vereinfachung. Die alte Annahme, wir erkennten Wörter an ihrer Umrissform, gilt in der Leseforschung als überholt. Heute geht man davon aus, dass die Buchstaben eines Wortes parallel erkannt werden (Überblick: Kevin Larson, »The Science of Word Recognition«, 2004). Für die Gestaltung ändert sich wenig: Vertraute Wortformen und gemischte Schreibung lesen sich schneller.
''') + '''{% statement "Wir lesen in Wörtern, nicht in Buchstaben.", "Geübte erfassen Wörter und Wortgruppen als Einheit und ergänzen den Rest aus dem Zusammenhang." %}
''')

CAPS = 'BITTE BEACHTEN SIE, DASS IHRE BESTELLUNG ERST NACH EINGANG DER ZAHLUNG BEARBEITET WIRD. ÄNDERUNGEN SIND DANACH NUR NOCH ÜBER DEN KUNDENDIENST MÖGLICH.'
NORM = 'Bitte beachten Sie, dass Ihre Bestellung erst nach Eingang der Zahlung bearbeitet wird. Änderungen sind danach nur noch über den Kundendienst möglich.'
ST = 'font-family:PTsans;font-size:3.4vh;line-height:1.45;hyphens:none;margin:0;text-align:left;'
W(D, '030-versalien.md', kopf('Auf dem Screen', '''
Die wichtigste Folge fürs Screendesign: Versalien, also durchgehende Großbuchstaben, lesen sich schlechter. Alle Wörter haben dieselbe rechteckige Form, Ober- und Unterlängen fehlen, und wir sind diese Form nicht gewohnt. Versalsatz kostet messbar Zeit und auch Platz.

Für ein, zwei Wörter ist das kein Problem: ein Label, ein kurzer Button, eine Dachzeile. Für einen Satz oder einen Absatz schon. Und Versalien wirken laut.

Im Code: Text normal schreiben und über CSS umstellen (`text-transform: uppercase`), nicht in Großbuchstaben tippen. Screenreader lesen getippte Versalien teils Buchstabe für Buchstabe vor.

**Hintergrund**

Miles Tinker und Donald Paterson haben schon 1928 gemessen, dass Versalsatz langsamer gelesen wird als gemischte Schreibung. Tinker fasst das in »Legibility of Print« (1963) zusammen. Ein Teil des Effekts ist Übung: Wer viel Versalsatz liest, wird schneller.
''') + beispiel('Welchen lesen Sie lieber?', f'<div style="display:flex;gap:6vw;align-items:flex-start;width:100%;"><p style="{ST}flex:1;">{CAPS}</p><p style="{ST}flex:1;">{NORM}</p></div>') + '\n\n'
+ '''{% statement "Versalien nur für Kurzes.", "Ein Label, ein Button, eine Dachzeile: gut. Ein ganzer Satz: schlecht." %}
''')

W(D, '040-fuehrt-zu.md', kopf('Führt zu', '''
Weil Wörter und Zeilen als Ganzes wahrgenommen werden, entscheiden Abstände darüber, ob Lesen leicht fällt. Das ist Thema von Lesetext und Satz. Text, der ohne Anstrengung aussieht, ist auch das Ziel von Prinzip Wahrnehmungsarbeit.
''') + '''{% statement "Führt zu", "[Lesetext](../prinzip-lesetext/) und [Satz](../prinzip-satz/). Dahinter: [Wahrnehmungsarbeit](../prinzip-wahrnehmungsarbeit/)." %}
''')
done(D, 'Wir lesen in Wörtern und Wortgruppen, nicht Buchstabe für Buchstabe. Deshalb lesen sich Versalien schlechter', 'Wortbild, Versalien, Lesen')
index(D, ['Buchstabendreher-Test', 'Lesen in Wörtern', 'Versalien'], 'Einstieg in Lesetext und Satz')
print('fertig', D)
