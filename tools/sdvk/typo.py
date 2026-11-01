# Gemeinsame Helfer für die Typografie-Decks. Nach deckbau.py einbinden.
import json, subprocess
MUSTER = '/tmp/shots/schriftmuster.js'  # Einrichtung siehe README, Quelle tools/sdvk/schriftmuster.js

LESETEXT = ('Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt, erfassen bei jedem Halt '
  'einige Buchstaben und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. '
  'Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab, weil die Augen mehr '
  'springen als lesen. Steht die nächste Zeile zu dicht darunter, rutschen sie ab. Steht sie zu weit weg, zerfällt der Text in einzelne Streifen.')

KURZ = ('Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. '
  'Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.')

def muster(deck, name, html, w=1600, h=900):
    """Schriftmuster als PNG mit Systemschriften rendern, liegt danach im Deck."""
    os.makedirs(f'{NEW}/{deck}/images', exist_ok=True)
    out = f'{NEW}/{deck}/images/{name}.png'
    subprocess.run(['node', MUSTER, json.dumps([{'out': out, 'w': w, 'h': h, 'html': html}])], check=True, capture_output=True, cwd='/tmp/shots')

def bild(img, bu, transition='fade', schatten=False):
    c = 'shadow' if schatten else 'no-shadow'
    return "{% screenshot \"./images/" + img + "\", '{\"transition\":\"" + transition + "\", \"classes\":\"" + c + "\", \"width\":\"auto\", \"bu\":\"" + bu + "\"}' %}"

def live(titel, inhalt, transition='fade'):
    """Folie mit echtem, im Browser gesetztem Text."""
    return f'<section class="simple" data-transition="{transition}">\n  <div>\n    <h1>{titel}</h1>\n    {inhalt}\n  </div>\n</section>'

def liste(titel, punkte):
    zeilen = '\n'.join("    {% fragment '<p class=\"list\">" + p + "</p>' %}" for p in punkte)
    return f'<section class="simple" data-transition="fade">\n  <div>\n    <h1>{titel}</h1>\n{zeilen}\n  </div>\n</section>'

def code(titel, css, gr=3):
    return live(titel, f'<pre style="font-size:{gr}vh;line-height:1.5;text-align:left;width:100%;box-shadow:none;"><code class="language-css">{css}</code></pre>')

def kopf(titel, speaker, cls='wrap', transition=None):
    tr = f'transition: {transition}\n' if transition else ''
    s = '\n'.join('  ' + z if z else '' for z in speaker.strip().split('\n'))
    return f'---\ntitle: "{titel}"\nlayout: presentation.11ty.js\nslideClasses: {cls}\n{tr}status: ok\nspeaker: |\n{s}\n---\n\n'

def index(deck, inhalt, einsatz=''):
    p = f'{NEW}/{deck}/index.md'; s = open(p).read()
    a = s.index('inhalt:'); b = s.index('status:')
    s = s[:a] + 'inhalt:\n' + ''.join(f'  - "{i}"\n' for i in inhalt) + s[b:]
    if einsatz: s = s.replace('einsatz: ""', f'einsatz: "{einsatz}"')
    open(p, 'w').write(s)
