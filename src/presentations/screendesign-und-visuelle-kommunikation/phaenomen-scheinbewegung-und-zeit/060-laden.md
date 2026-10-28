---
title: "Zweimal laden"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Live-Test (ca. 2 Minuten)**

  Erst die Karte mit dem drehenden Kreis, dann die Karte mit den grauen Platzhaltern. Beide Male erscheint der Inhalt nach genau vier Sekunden. Die Animation startet, sobald die Folie erscheint (Auto-Animate ist auf diesen beiden Folien abgeschaltet, sonst bleibt der Inhalt unsichtbar). Wer sie noch einmal sehen will: eine Folie zurück und wieder vor.

  Danach fragen: Welcher Ladevorgang hat sich kürzer angefühlt? Meist sagt die Mehrheit: der zweite. Manche finden den Spinner kürzer, weil er vertraut ist. Beides ist ein Gesprächsanlass.

  Bei »Bewegung reduzieren« drehen und pulsieren die Platzhalter nicht, der Inhalt erscheint trotzdem nach vier Sekunden.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Laden, Variante 1", "animate":false}' %}
<style>@keyframes wz-da{0%{opacity:0}100%{opacity:1}}@keyframes wz-weg{0%{opacity:1}100%{opacity:0}}@keyframes wz-dreh{to{transform:rotate(360deg)}}@keyframes wz-puls{0%,100%{opacity:1}50%{opacity:.45}}.wz-inhalt{opacity:1}.wz-warten{opacity:0}section>section.present .wz-inhalt{animation:wz-da 4s step-end both}section>section.present .wz-warten{animation:wz-weg 4s step-end both}section>section.present .wz-dreh{transform-origin:450px 230px;animation:wz-dreh .9s linear infinite}section>section.present .wz-puls{animation:wz-puls 1.2s ease-in-out infinite}@media (prefers-reduced-motion: reduce){section>section.present .wz-dreh,section>section.present .wz-puls{animation:none}}</style><rect x="300" y="40" width="300" height="400" fill="#e4e4e4" /><g class="wz-warten"><g class="wz-dreh"><circle cx="450" cy="230" r="34" fill="none" stroke="#d9d9d9" stroke-width="8" /><path d="M 450 196 A 34 34 0 0 1 484 230" fill="none" stroke="#888888" stroke-width="8" stroke-linecap="round" /></g></g><g class="wz-inhalt"><rect x="320" y="60" width="260" height="140" fill="#c4c4c4" />
<rect x="320" y="222" width="180" height="16" fill="#888888" />
<rect x="320" y="254" width="260" height="10" fill="#aaaaaa" />
<rect x="320" y="274" width="240" height="10" fill="#aaaaaa" />
<rect x="320" y="294" width="170" height="10" fill="#aaaaaa" />
<rect x="320" y="330" width="110" height="36" rx="18" fill="#231f20" /></g>
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Laden, Variante 2", "animate":false}' %}
<style>@keyframes wz-da{0%{opacity:0}100%{opacity:1}}@keyframes wz-weg{0%{opacity:1}100%{opacity:0}}@keyframes wz-dreh{to{transform:rotate(360deg)}}@keyframes wz-puls{0%,100%{opacity:1}50%{opacity:.45}}.wz-inhalt{opacity:1}.wz-warten{opacity:0}section>section.present .wz-inhalt{animation:wz-da 4s step-end both}section>section.present .wz-warten{animation:wz-weg 4s step-end both}section>section.present .wz-dreh{transform-origin:450px 230px;animation:wz-dreh .9s linear infinite}section>section.present .wz-puls{animation:wz-puls 1.2s ease-in-out infinite}@media (prefers-reduced-motion: reduce){section>section.present .wz-dreh,section>section.present .wz-puls{animation:none}}</style><rect x="300" y="40" width="300" height="400" fill="#e4e4e4" /><g class="wz-warten"><g class="wz-puls"><rect x="320" y="60" width="260" height="140" fill="#d9d9d9" />
<rect x="320" y="222" width="180" height="16" fill="#d9d9d9" />
<rect x="320" y="254" width="260" height="10" fill="#d9d9d9" />
<rect x="320" y="274" width="240" height="10" fill="#d9d9d9" />
<rect x="320" y="294" width="170" height="10" fill="#d9d9d9" />
<rect x="320" y="330" width="110" height="36" rx="18" fill="#d9d9d9" /></g></g><g class="wz-inhalt"><rect x="320" y="60" width="260" height="140" fill="#c4c4c4" />
<rect x="320" y="222" width="180" height="16" fill="#888888" />
<rect x="320" y="254" width="260" height="10" fill="#aaaaaa" />
<rect x="320" y="274" width="240" height="10" fill="#aaaaaa" />
<rect x="320" y="294" width="170" height="10" fill="#aaaaaa" />
<rect x="320" y="330" width="110" height="36" rx="18" fill="#231f20" /></g>
{% endframe %}

{% question "Was ging schneller?", "Beide dauerten genau vier Sekunden." %}
