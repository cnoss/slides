---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Wenn ein Rahmen gruppiert, warum nicht überall einen? Die erste Fassung zeigt das Ergebnis: Kiste in Kiste in Kiste. Jede Linie ist ein Signal, und viele Signale sind Rauschen. Die zweite Fassung zeigt dieselben Gruppen nur mit zwei Flächen und Abstand. Ruhiger, und die Gruppen sind trotzdem eindeutig.

  Faustregel aus Refactoring UI (Wathan & Schoger, »Use fewer borders«): Bevor Sie einen Rahmen ziehen, probieren Sie Abstand, eine Hintergrundfläche oder einen leichten Helligkeitsunterschied.

  Zweite Grenze: Eine hellgraue Fläche auf Weiß ist leise. Auf schlechten Bildschirmen oder für Menschen mit Sehschwäche kann sie verschwinden. Wenn die Gruppe wichtig ist, darf sie nicht nur an der Fläche hängen.
---

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Rahmen um alles: Kiste in Kiste in Kiste"}' %}
  <rect data-id="k0" x="60" y="50" width="480" height="470" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="k1" x="80" y="70" width="440" height="50" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="kh" x="100" y="86" width="180" height="18" fill="#888888" />
  <rect data-id="kc0" x="80" y="140" width="210" height="360" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="kb0" x="95" y="155" width="180" height="120" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="ki0" x="95" y="155" width="180" height="120" fill="#c4c4c4" />
  <rect data-id="kt0" x="95" y="290" width="180" height="110" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="kx0a" x="108" y="304" width="150" height="14" fill="#888888" />
  <rect data-id="kx0b" x="108" y="334" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="kx0c" x="108" y="356" width="110" height="10" fill="#aaaaaa" />
  <rect data-id="kbb0" x="95" y="415" width="180" height="60" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="kbt0" x="108" y="425" width="120" height="40" rx="20" fill="#9313ce" />
  <rect data-id="kc1" x="310" y="140" width="210" height="360" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="kb1" x="325" y="155" width="180" height="120" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="ki1" x="325" y="155" width="180" height="120" fill="#c4c4c4" />
  <rect data-id="kt1" x="325" y="290" width="180" height="110" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="kx1a" x="338" y="304" width="150" height="14" fill="#888888" />
  <rect data-id="kx1b" x="338" y="334" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="kx1c" x="338" y="356" width="110" height="10" fill="#aaaaaa" />
  <rect data-id="kbb1" x="325" y="415" width="180" height="60" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="kbt1" x="338" y="425" width="120" height="40" rx="20" fill="#9313ce" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Dieselben Gruppen: nur Flächen und Abstand"}' %}
  <rect data-id="kh" x="100" y="86" width="180" height="18" fill="#888888" />
  <rect data-id="kc0" x="80" y="140" width="210" height="360" fill="#e4e4e4" />
  <rect data-id="ki0" x="95" y="155" width="180" height="120" fill="#c4c4c4" />
  <rect data-id="kx0a" x="108" y="304" width="150" height="14" fill="#888888" />
  <rect data-id="kx0b" x="108" y="334" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="kx0c" x="108" y="356" width="110" height="10" fill="#aaaaaa" />
  <rect data-id="kbt0" x="108" y="425" width="120" height="40" rx="20" fill="#9313ce" />
  <rect data-id="kc1" x="310" y="140" width="210" height="360" fill="#e4e4e4" />
  <rect data-id="ki1" x="325" y="155" width="180" height="120" fill="#c4c4c4" />
  <rect data-id="kx1a" x="338" y="304" width="150" height="14" fill="#888888" />
  <rect data-id="kx1b" x="338" y="334" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="kx1c" x="338" y="356" width="110" height="10" fill="#aaaaaa" />
  <rect data-id="kbt1" x="338" y="425" width="120" height="40" rx="20" fill="#9313ce" />
{% endframe %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann schadet ein Rahmen?</h1>
    {% fragment '<p class="list">Wenn Rahmen in Rahmen in Rahmen stecken: Rauschen.</p>' %}
    {% fragment '<p class="list">Wenn Abstand genügt: Weißraum ist leiser als eine Linie.</p>' %}
    {% fragment '<p class="list">Wenn die Fläche zu schwach ist: Dann sehen nicht alle die Gruppe.</p>' %}
  </div>
</section>
