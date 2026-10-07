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
| `beispiel-frame-deck.py` | Beispiel: Deck mit eigenen SVG-Visualisierungen (`frame`, Auto-Animate) | `python3 beispiel-frame-deck.py` |
| `render.js` | Rendert alle Folien eines oder mehrerer Decks nach `/tmp/shots/r/<deck>/` (1920 × 1080). Braucht den laufenden Dev-Server auf Port 8080 (`npm run dev`) | `node render.js <deck> [<deck> …]` |
| `navigation.js` | Simuliert Pfeil rechts durch ein Deck und listet die Folienfolge | `node navigation.js` (Deck-URL im Skript) |
| `screenshots.js` | Zieht Website-Screenshots (1440 × 900), klickt Cookie-Banner weg, Ausgabe `/tmp/shots/k-<name>.png` | `node screenshots.js '[{"name":"x","url":"https://…"}]'` |

Kontaktbogen aus gerenderten Folien: `montage` (ImageMagick) über Python `subprocess`, nicht über zsh-Globbing mit `[0]`.

## Hinweise

- Der Dev-Server lädt Änderungen an `.eleventy.js` erst nach Neustart.
- Bei Frame-Folien kein Übergang (`transition: none`), sonst blendet die Bühne mit.
- Reveal: Pfeil rechts springt von Stapel zu Stapel, Pfeil runter oder Leertaste geht durch alle Folien.
