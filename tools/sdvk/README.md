# Werkzeuge für "Screendesign und visuelle Kommunikation"

Hilfsskripte, mit denen Claude die Decks baut und prüft. Referenz für Inhalte und Regeln: Obsidian, "Screendesign Rückgrat".

## Einrichtung (einmalig, außerhalb des Repos)

```
mkdir -p /tmp/shots && cd /tmp/shots && npm init -y && npm i puppeteer-core@22
cp /Users/cnoss/git/privat/slides/tools/sdvk/*.js /tmp/shots/
```

Die JS-Skripte erwarten `puppeteer-core` in `/tmp/shots` und Chrome unter `/Applications/Google Chrome.app`.

## Skripte

| Datei | Zweck | Aufruf |
|---|---|---|
| `deckbau.py` | Helfer für Python-Bauskripte: `W()` Datei schreiben, `cp()` Bestandsfolie samt Bildern übernehmen, `imgs()` Bilder kopieren, `intro()` Titelfolie, `done()` Metadaten setzen, Status ok, Platzhalter löschen | `exec(open('…/deckbau.py').read())` |
| `blitz.py` | Helfer `blitz(img, titel, frage, dauer)`: Screen blitzt beim Weiterschalten für eine feste Zeit auf und verschwindet von selbst (Fragment mit CSS-Animation). Für Ersteindruck (50 ms) und 5-Sekunden-Test. `css=True` beim ersten Aufruf pro Datei | `exec(open('…/blitz.py').read())` |
| `beispiel-frame-deck.py` | Beispiel: Deck mit eigenen SVG-Visualisierungen (`frame`, Auto-Animate) | `python3 beispiel-frame-deck.py` |
| `render.js` | Rendert alle Folien eines oder mehrerer Decks nach `/tmp/shots/r/<deck>/` (1920 × 1080). Braucht den laufenden Dev-Server auf Port 8080 (`npm run dev`). Eigenes Chrome-Profil pro Lauf, Live-Reload abgeschaltet, wartet, bis Reveal bereit ist. Darf parallel laufen | `node render.js <deck> [<deck> …]` |
| `one.js` | Rendert eine einzelne Folie, wenn `render.js` im Stapel die falsche erwischt hat | `node one.js <deck> <h> <v> <ausgabe.png> [wartezeit-ms]` |
| `navigation.js` | Simuliert Pfeil rechts durch ein Deck und listet die Folienfolge | `node navigation.js` (Deck-URL im Skript) |
| `screenshots.js` | Zieht Website-Screenshots (1440 × 900), klickt Cookie-Banner weg, Ausgabe `/tmp/shots/k-<name>.png` | `node screenshots.js '[{"name":"x","url":"https://…"}]'` |

Kontaktbogen aus gerenderten Folien: `montage` (ImageMagick) über Python `subprocess`, nicht über zsh-Globbing mit `[0]`.

## Hinweise

- `render.js` rendert in Stapeln mit vielen vertikalen Folien manchmal die falsche Folie (Timing). Dann einzelne Folie gezielt per `Reveal.slide(h, v)` prüfen.
- Animationen (Blitz, Flimmern) laufen nur auf der aktiven Folie. Prüfen über `element.getAnimations()` nach `Reveal.slide()`.
- `render.js` zeigt direkt nach einem `interlude` manchmal noch das verblasste Interlude. Einzeln mit `one.js` gerendert stimmt die Folie.
- Schreibt man Dateien, während `render.js` läuft, baut der Dev-Server neu. `render.js` lädt dann nach, ein zweiter Lauf ist meist nicht mehr nötig.
- **CSS-Animationen in Frame-Folien:** Mit Auto-Animate starten Animationen schon beim Betreten des Stapels. Für Folien, deren Animation beim Erreichen starten soll (z. B. Ladezustände), im Frame `"animate":false` setzen und im Selektor `section>section.present` statt `section.present` verwenden. Beispiel: `phaenomen-scheinbewegung-und-zeit/060-laden.md`.
- **Zeitgesteuert einblenden statt blitzen:** Ein Fragment, das per CSS-Animation für eine feste Zeit sichtbar ist und dann verschwindet (z. B. Wortliste 5 s), siehe `phaenomen-pop-out/040-von-restorff.md`. `blitz.py` funktioniert auch mit SVG-Dateien als Bild (`phaenomen-pop-out/images/suche-*.svg`).
- **Screenshots mit `screenshots.js`:** Gut gingen 2026 tagesschau.de, de.wikipedia.org, booking.com, airbnb.de, duolingo.com, netflix.com, ikea.com, th-koeln.de. Unbrauchbar: zeit.de (Bot-Sperre), bahn.de, dm.de, spiegel.de, chefkoch.de (Cookie-Banner bleibt), kleinanzeigen.de (Login-Popup, Werbung).

- Der Dev-Server lädt Änderungen an `.eleventy.js` erst nach Neustart.
- Bei Frame-Folien kein Übergang (`transition: none`), sonst blendet die Bühne mit.
- **Auto-Animate und gedrehte SVG-Gruppen:** Ändert sich zwischen zwei Frame-Folien das `transform`-Attribut einer `<g>` mit `data-id` (z. B. `rotate`), zerlegt Reveal die Folie beim Weiterschalten, übrig bleibt ein einzelnes Element. Dann im Frame `"animate":false` setzen. Beispiel: `methode-permutation`.
- Speaker Notes mit Guillemets (»…«). `python3 tools/sdvk/guillemets.py dry` listet gerade Anführungszeichen in den Speaker Notes, ohne `dry` werden sie ersetzt.
- Reveal: Pfeil rechts springt von Stapel zu Stapel, Pfeil runter oder Leertaste geht durch alle Folien.
