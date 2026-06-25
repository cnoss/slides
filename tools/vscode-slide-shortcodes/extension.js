// Lokale VS-Code-Extension: Autovervollständigung der Eleventy-Shortcodes.
//
// Sobald in einer Markdown-Datei "{%" getippt wird, erscheint die Liste aller
// Folien-Shortcodes; bei Auswahl wird der komplette {% ... %}-Block mit
// Platzhaltern (Tab-Sprünge) und Transition-Dropdowns eingefügt.
//
// Reines JavaScript, kein Build-Schritt nötig.

const vscode = require('vscode');

// Die Shortcode-Definitionen spiegeln .vscode/markdown.code-snippets wider.
// body = vollständiger {% ... %}-Block als VS-Code-Snippet (inkl. ${1:...} und
// ${n|a,b,c|}-Auswahllisten).
const SHORTCODES = [
  {
    name: 'interlude',
    detail: 'Zwischentitel (zufällige Hintergrundfarbe)',
    body: '{% interlude "${1:Titel}", "${2:Untertitel}", \'{"transition":"${3|slide,zoom,fade,none,concave,convex|}"}\' %}',
  },
  {
    name: 'simpleText',
    detail: 'Einfache Text-Folie (Titel + Text)',
    body: '{% simpleText "${1:Titel}", "${2:Text}", \'{"transition":"${3|slide,zoom,fade,none,concave,convex|}"}\' %}',
  },
  {
    name: 'simpleInterlude',
    detail: 'Einfaches Interlude (zentriert)',
    body: '{% simpleInterlude "${1:Titel}", "${2:Text}", \'{"transition":"${3|slide,zoom,fade,none|}"}\' %}',
  },
  {
    name: 'question',
    detail: 'Frage-Folie',
    body: '{% question "${1:Frage}", "${2:Tagline}", \'{"classes":"${3:}"}\' %}',
  },
  {
    name: 'statement',
    detail: 'Statement (Aussage als Fragment)',
    body: '{% statement "${1:Titel}", "${2:Aussage (Fragment)}", \'{"backgroundTransition":"${3|fade,slide,zoom,none|}"}\' %}',
  },
  {
    name: 'shout',
    detail: 'Großes Zitat (Autor/Quelle/Info)',
    body: '{% shout "${1:Zitat}", "${2:Autor}", "${3:Quelle}", "${4:Info}", \'{"transition":"${5|slide,zoom,fade,none|}"}\' %}',
  },
  {
    name: 'cite',
    detail: 'Zitat-Folie (Blockquote)',
    body: '{% cite "${1:Zitat-Text}" %}',
  },
  {
    name: 'qa',
    detail: 'Frage-Antwort-Folie',
    body: '{% qa "${1:Frage}", "${2:Antwort}", \'{"transition":"${3|slide,zoom,fade,none|}"}\' %}',
  },
  {
    name: 'splitView',
    detail: 'Geteilte Ansicht (Titel + Inhalt)',
    body: '{% splitView "${1:Titel}", "${2:Inhalt}" %}',
  },
  {
    name: 'image',
    detail: 'Bild-Folie',
    body: '{% image "${1:images/datei.png}", \'{"transition":"${2|fade,slide,zoom,none|}", "classes":"${3:}", "bu":"${4:}"}\' %}',
  },
  {
    name: 'screenshot',
    detail: 'Screenshot-Folie',
    body: '{% screenshot "${1:images/datei.png}", \'{"transition":"${2|fade,slide,zoom,none|}", "classes":"${3:}", "bu":"${4:}", "badge":"${5:}"}\' %}',
  },
  {
    name: 'screenshotFs',
    detail: 'Vollbild-Screenshot (Hintergrund)',
    body: '{% screenshotFs "${1:images/datei.png}", \'{"transition":"${2|fade,slide,zoom,none|}", "bu":"${3:}", "badge":"${4:}"}\' %}',
  },
  {
    name: 'codeSmall',
    detail: 'Code-Folie (klein) mit Highlighting',
    body: '{% codeSmall "${1:Titel}", "${2:Beschreibung}", "${3:Code}", "${4|js,html,css,scss,bash,json,md|}", \'{"transition":"${5|slide,fade,zoom,none|}"}\' %}',
  },
  {
    name: 'fragment',
    detail: 'Fragment (erscheint per Klick)',
    body: '{% fragment "${1:Inhalt}" %}',
  },
  {
    name: 'important',
    detail: 'Hervorgehobener Hinweis',
    body: '{% important "${1:Inhalt}" %}',
  },
  {
    name: 'niceToKnow',
    detail: 'Zusatz-Info (nice to know)',
    body: '{% niceToKnow "${1:Inhalt}" %}',
  },
  {
    name: 'text',
    detail: 'Einfacher Text-Block',
    body: '{% text "${1:Inhalt}" %}',
  },
  {
    name: 'meta',
    detail: 'Meta-Tags (robots/viewport/charset)',
    body: '{% meta %}',
  },
];

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
  const provider = vscode.languages.registerCompletionItemProvider(
    { language: 'markdown', scheme: 'file' },
    {
      provideCompletionItems(document, position) {
        const linePrefix = document.lineAt(position).text.slice(0, position.character);

        // Nur reagieren, wenn der Cursor hinter einem (noch offenen) "{%" steht:
        //   {%            -> Liste zeigen
        //   {% sim        -> nach Namen filtern
        // Ein bereits geschlossenes "%}" auf der linken Seite schließt den Kontext.
        const match = linePrefix.match(/\{%\s*([\w]*)$/);
        if (!match) {
          return undefined;
        }

        // Bereich von "{%" bis zum Cursor — wird durch den Snippet ersetzt,
        // damit kein doppeltes "{%" entsteht.
        const startChar = position.character - match[0].length;
        const range = new vscode.Range(position.line, startChar, position.line, position.character);

        return SHORTCODES.map((sc, index) => {
          const item = new vscode.CompletionItem(sc.name, vscode.CompletionItemKind.Snippet);
          item.detail = sc.detail;
          item.insertText = new vscode.SnippetString(sc.body);
          item.range = range;
          // Damit das getippte "{% sim" gegen den Namen gefiltert wird.
          item.filterText = '{% ' + sc.name;
          item.sortText = String(index).padStart(3, '0');
          item.documentation = new vscode.MarkdownString('`' + sc.body.replace(/\$\{\d+(\|[^}]*\||:[^}]*)?\}/g, '…') + '`');
          return item;
        });
      },
    },
    '%', // Trigger direkt nach "{%"
    ' ', // Trigger nach "{% "
  );

  context.subscriptions.push(provider);
}

function deactivate() {}

module.exports = { activate, deactivate };
