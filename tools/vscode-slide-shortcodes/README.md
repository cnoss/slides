# Slide Shortcodes — lokale VS-Code-Extension

Autovervollständigung der Eleventy-Shortcodes (`{% … %}`) für die Folien in
diesem Repo. Sobald in einer Markdown-Datei `{%` getippt wird, erscheint die
Liste aller Shortcodes; bei Auswahl wird der komplette Block mit Platzhaltern
(Tab-Sprünge) und Transition-Dropdowns eingefügt.

Reines JavaScript, **kein Build-Schritt**.

## Installation

Per Symlink ins VS-Code-Extensions-Verzeichnis (Quellcode bleibt im Repo):

```bash
ln -sfn "$(pwd)/tools/vscode-slide-shortcodes" \
  ~/.vscode/extensions/cnoss.slide-shortcodes-0.1.0
```

Danach VS Code neu laden: `Cmd+Shift+P` → **Reload Window**.

## Deinstallation

```bash
rm ~/.vscode/extensions/cnoss.slide-shortcodes-0.1.0
```

## Shortcodes pflegen

Die Definitionen stehen in [`extension.js`](extension.js) im Array `SHORTCODES`
und spiegeln `.vscode/markdown.code-snippets` wider. Neuen Shortcode in
`.eleventy.js` ergänzt? Dann hier (und im Snippet-File) einen Eintrag
hinzufügen und VS Code neu laden.

## Verhältnis zu den Snippets

`.vscode/markdown.code-snippets` ist die zero-install-Variante (Präfix + Tab)
und funktioniert auch ohne diese Extension. Die Extension ergänzt das
Auslösen direkt nach `{%`.
