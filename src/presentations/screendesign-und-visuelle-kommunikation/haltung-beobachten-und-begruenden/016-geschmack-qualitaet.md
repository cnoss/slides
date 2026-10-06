---
title: Geschmack oder Qualität?
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Diskussion (ca. 5 Minuten)**

  Erst fragen: Gefällt Ihnen das? Meist großes Nein. Dann: Funktioniert es? Für wen? Ling's Cars nennt sich selbst Großbritanniens größte unabhängige Verkäuferin von Neuwagen (Zitat The Guardian, 2017, auf der Seite). Die Seite ist bewusst laut, persönlich und unverwechselbar.

  Der Netto-Prospekt: Für viele unattraktiv, für seine Zielgruppe hoch funktional. Preise springen ins Auge, Rabatte sind sofort erkennbar.

  Pointe: Ob uns etwas gefällt, sagt nichts darüber, ob es funktioniert. Qualität misst sich an Ziel, Zielgruppe und Kontext.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Geschmack oder Qualität?</h1>
    <div style="display:flex; gap:4rem; text-align:left;">
      <div style="flex:1;">
        {% fragment '<p><strong>Geschmack</strong></p><p class="list">persönlich</p><p class="list">nicht begründbar</p><p class="list">nicht verhandelbar</p>' %}
      </div>
      <div style="flex:1;">
        {% fragment '<p><strong>Qualität</strong></p><p class="list">an Ziel, Zielgruppe und Kontext messbar</p><p class="list">begründbar</p><p class="list">diskutierbar</p>' %}
      </div>
    </div>
  </div>
</section>

{% screenshot "./images/lingscars.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Gefällt Ihnen das? Funktioniert es? Für wen?<br><small>lingscars.com, Screenshot ca. 2017</small>"}' %}

{% screenshot "./images/zielgruppe-netto.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Und hier? Woran sehen Sie, für wen das gemacht ist?<br><small>Netto Marken-Discount, Prospekt Oktober 2024</small>"}' %}

{% statement "Ob uns etwas gefällt, sagt nichts darüber, ob es funktioniert.", "Qualität misst sich an Ziel, Zielgruppe und Kontext. Nicht an unserem Geschmack." %}

{% statement "Woran merken Sie, dass Sie nicht nach Geschmack urteilen?", "Sie sagen nicht »schön«, sondern was ein Gestaltungsmittel bewirkt: »Die große Headline zieht den Blick zuerst nach oben, der Button ist das einzige farbige Element.«" %}
