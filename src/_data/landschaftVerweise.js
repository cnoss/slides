// Querverweise zwischen den Decks von "Screendesign und visuelle Kommunikation"
// für den Export src/screendesign-landschaft.json.njk.
// Liest alle Markdown-Dateien eines Decks und sammelt relative Links auf andere Decks.
// Ergebnis: { "deck-id": ["ziel-id", ...] }. Links auf unbekannte Decks werden gemeldet und entfallen.

const fs = require('fs');
const path = require('path');

const WURZEL = path.join(__dirname, '..', 'presentations', 'screendesign-und-visuelle-kommunikation');
const LINK = /(?:\]\(|href=["'])\.\.\/([a-z0-9-]+)/g;

module.exports = () => {
  const decks = fs.readdirSync(WURZEL, { withFileTypes: true })
    .filter((eintrag) => eintrag.isDirectory())
    .map((eintrag) => eintrag.name);
  const bekannt = new Set(decks);
  const verweise = {};

  decks.forEach((deck) => {
    const ordner = path.join(WURZEL, deck);
    const ziele = new Set();

    fs.readdirSync(ordner)
      .filter((datei) => datei.endsWith('.md'))
      .forEach((datei) => {
        const inhalt = fs.readFileSync(path.join(ordner, datei), 'utf-8');
        Array.from(inhalt.matchAll(LINK)).forEach((treffer) => {
          const ziel = treffer[1];
          if (ziel === deck) return;
          if (bekannt.has(ziel)) ziele.add(ziel);
          else console.warn(`[landschaft] ${deck}/${datei} verweist auf unbekanntes Deck: ${ziel}`);
        });
      });

    verweise[deck] = Array.from(ziele).sort();
  });

  return verweise;
};
