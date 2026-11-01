---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **1. Grundgröße festlegen:** Das ist die Größe des Fließtexts, im Web meist 16 px (1 rem).

  **2. Faktor wählen:** Kleine Faktoren (1,125 bis 1,2) für dichte Oberflächen, in denen viel auf den Screen muss. Größere (1,25 bis 1,5) für Inhaltsseiten mit deutlicher Hierarchie.

  **3. Stufen berechnen und runden:** Grundgröße mal Faktor, immer wieder. Auf ganze Zahlen runden.

  **4. Stufen zuweisen:** Jede Lesestufe bekommt eine Größe, nicht jede Größe muss vorkommen.

  **In Figma** als Text Styles anlegen, **im Code** als Variablen. Dann gibt es nur noch diese Größen.

  **Hintergrund**

  Die Idee stammt aus der Buchtypografie: Die klassische Skala der Bleisatz-Schriftgrade (6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 21, 24, 36, 48, 60, 72) beschreibt Robert Bringhurst in »The Elements of Typographic Style« (1992). Fürs Web hat Tim Brown den Begriff der modularen Skala bekannt gemacht (»More Meaningful Typography«, A List Apart, 2011). Wathan und Schoger raten in »Refactoring UI« (2018) dagegen zu einer handverlesenen Skala, weil mathematisch berechnete Stufen zu krummen Werten führen. Beides funktioniert. Wichtig ist nur, dass es eine feste Auswahl gibt.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Eine Skala in vier Schritten</h1>
    {% fragment '<p class="list"><strong>1. Grundgröße festlegen:</strong> die Größe des Fließtexts, im Web meist 16 px</p>' %}
    {% fragment '<p class="list"><strong>2. Faktor wählen:</strong> kleiner für dichte Oberflächen, größer für Inhaltsseiten</p>' %}
    {% fragment '<p class="list"><strong>3. Berechnen und runden:</strong> Grundgröße mal Faktor, immer wieder</p>' %}
    {% fragment '<p class="list"><strong>4. Zuweisen:</strong> Jede Lesestufe bekommt eine Größe</p>' %}
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>Drei Faktoren</h1>
    <div style="display:flex;gap:4vw;align-items:flex-end;"><div><p style="font-family:PTsans;font-size:2.6vh;margin:0 0 1vh;text-align:left;color:#9313ce;">1,125: dicht</p><div style="display:flex;flex-direction:column;gap:.6vh;"><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">26</span><span style="font-family:PTsans;font-size:2.86vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">23</span><span style="font-family:PTsans;font-size:2.53vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">20</span><span style="font-family:PTsans;font-size:2.20vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">18</span><span style="font-family:PTsans;font-size:1.98vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">16</span><span style="font-family:PTsans;font-size:1.76vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div></div></div><div><p style="font-family:PTsans;font-size:2.6vh;margin:0 0 1vh;text-align:left;color:#9313ce;">1,25: ausgewogen</p><div style="display:flex;flex-direction:column;gap:.6vh;"><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">39</span><span style="font-family:PTsans;font-size:4.29vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">31</span><span style="font-family:PTsans;font-size:3.41vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">25</span><span style="font-family:PTsans;font-size:2.75vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">20</span><span style="font-family:PTsans;font-size:2.20vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">16</span><span style="font-family:PTsans;font-size:1.76vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div></div></div><div><p style="font-family:PTsans;font-size:2.6vh;margin:0 0 1vh;text-align:left;color:#9313ce;">1,5: deutlich</p><div style="display:flex;flex-direction:column;gap:.6vh;"><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">81</span><span style="font-family:PTsans;font-size:8.91vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">54</span><span style="font-family:PTsans;font-size:5.94vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">36</span><span style="font-family:PTsans;font-size:3.96vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">24</span><span style="font-family:PTsans;font-size:2.64vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div><div style="display:flex;align-items:baseline;gap:1.5vw;"><span style="font-family:PTsans;font-size:2vh;color:#888888;width:3em;flex:none;">16</span><span style="font-family:PTsans;font-size:1.76vh;line-height:1.1;white-space:nowrap;">Lesestufe</span></div></div></div></div>
  </div>
</section>
