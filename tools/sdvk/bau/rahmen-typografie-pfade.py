# Erzeugt die Buchstaben-Umrisse für rahmen-typografie als Pfade (rahmen-typografie-pfade.json).
# Nur nötig, wenn sich Wörter oder Schriften ändern. Umrisse statt Text, damit die Hilfslinien auf jedem Gerät exakt sitzen.
# Braucht: python3 -m venv /tmp/shots/venv && /tmp/shots/venv/bin/pip install fonttools uharfbuzz
# Aufruf: /tmp/shots/venv/bin/python tools/sdvk/bau/rahmen-typografie-pfade.py
import json, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HIER = os.path.dirname(os.path.abspath(__file__))
PT = os.path.abspath(f'{HIER}/../../../src/assets/fonts/PT_Serif/PTSerif-Regular.ttf')
TIMES = '/System/Library/Fonts/Supplemental/Times New Roman.ttf'
VERDANA = '/System/Library/Fonts/Supplemental/Verdana.ttf'
WOERTER = {'typografie': ('Typografie', PT), 'versal': ('TYPOGRAFIE', PT), 'zeile1': ('Typografie braucht', PT),
           'zeile2': ('Luft zum Atmen', PT), 'times': ('Schrift', TIMES), 'verdana': ('Schrift', VERDANA)}

def formen(text, pfad):
    b = hb.Buffer(); b.add_str(text); b.guess_segment_properties()
    f = hb.Font(hb.Face(hb.Blob.from_file_path(pfad)))
    hb.shape(f, b, {'kern': True, 'liga': False})
    return b.glyph_infos, b.glyph_positions

def fmt(gs, name, x):
    rec = DecomposingRecordingPen(gs); gs[name].draw(rec)
    return rec.value

def umrisse(rec):
    """Teilt eine Glyphe in Konturen und berechnet den Umlaufsinn."""
    konturen, akt = [], []
    for op, args in rec:
        akt.append((op, args))
        if op in ('closePath', 'endPath'):
            konturen.append(akt); akt = []
    return konturen

def flaeche(k):
    p = [a[-1] for op, a in k if a and op != 'closePath' and a[-1] is not None]
    return sum(p[i][0]*p[(i+1) % len(p)][1] - p[(i+1) % len(p)][0]*p[i][1] for i in range(len(p))) / 2

def zeichne(gs, konturen, x):
    pen = SVGPathPen(gs, ntos=lambda v: f'{v:.1f}'.rstrip('0').rstrip('.'))
    t = TransformPen(pen, (1, 0, 0, -1, x, 0))
    for k in konturen:
        for op, a in k:
            getattr(t, op)(*a)
    return pen.getCommands()

aus = {}
for key, (text, pfad) in WOERTER.items():
    tt = TTFont(pfad); gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    infos, pos = formen(text, pfad)
    x = 0; d = []; innen = []; fuesse = {}
    for ch, i, p in zip(text, infos, pos):
        name = order[i.codepoint]
        ks = umrisse(fmt(gs, name, x))
        d.append(zeichne(gs, ks, x + p.x_offset))
        if ks:
            haupt = max(abs(flaeche(k)) for k in ks)
            vz = next(flaeche(k) for k in ks if abs(flaeche(k)) == haupt)
            innen += [zeichne(gs, [k], x + p.x_offset) for k in ks if flaeche(k) * vz < 0]
            basis = [a[-1][0] for k in ks for op, a in k if a and a[-1] is not None and abs(a[-1][1]) <= 1]
            if basis and ch in 'Trfi':
                fuesse[ch] = x + p.x_offset + (min(basis) + max(basis)) / 2
        x += p.x_advance
    os2 = tt['OS/2']
    from fontTools.pens.boundsPen import BoundsPen
    def grenze(n):
        bp = BoundsPen(gs); gs[n].draw(bp); return bp.bounds
    aus[key] = {'d': ' '.join(d), 'innen': ' '.join(innen), 'fuesse': fuesse, 'breite': x, 'upm': tt['head'].unitsPerEm,
                'xh': grenze('x')[3], 'cap': grenze('H')[3], 'ober': grenze('h')[3], 'unter': grenze('p')[1]}
json.dump(aus, open(f'{HIER}/rahmen-typografie-pfade.json', 'w'), ensure_ascii=False, indent=1)
for k, v in aus.items():
    print(k, v['upm'], v['breite'], v['xh'], v['cap'], v['ober'], v['unter'], list(v['fuesse']), len(v['innen']))
