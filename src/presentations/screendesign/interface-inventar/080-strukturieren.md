---
title: Wahrnehmungsarbeit
layout: presentation.11ty.js
slideClasses: images
transition: zoom
---

{% interlude "Wie <strong>strukturieren</strong> wir die Dokumentation?"%}

{% screenshot "./images/struktur/struktur-01.png", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/struktur/struktur-02.png", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/struktur/struktur-03.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/struktur/struktur-04.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/struktur/struktur-05.png", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/struktur/struktur-06.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/struktur/struktur-07.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/struktur/struktur-08.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":""}' %}

{% interlude "Praxisbeispiel"%}


<section class="image is-fullscreen" data-transition="fade"  data-background-transition="fade" data-background="./images/map-cologne.jpg">
  <div class="is-centered">
    <div>
      <h1>Pattern Library </h1>
      {% fragment '<p class="list"><strong>Base</strong> Unwichtiges weglassen</p>' %}
      {% fragment '<p class="list"><strong>Atoms</strong> Muster bilden</p>' %}
      {% fragment '<p class="list"><strong>Molecules</strong> Bezüge herstellen</p>' %}
      {% fragment '<p class="list"><strong>Organisms</strong> Kombinationen aus Molekülen und Atomen</p>' %}
      {% fragment '<p class="list"><strong>Composition</strong> Raster, Layout</p>' %}
      {% fragment '<p class="list"><strong>Behavior</strong> Flow, Transition, Microinteraction, Reaktion auf Viewports</p>' %}
    </div>
  </div>
</section>