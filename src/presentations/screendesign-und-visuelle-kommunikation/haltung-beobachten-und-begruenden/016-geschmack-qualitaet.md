---
title: Geschmack oder Qualität?
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Diskussion (ca. 5 Minuten)**

  Erst fragen: Gefällt Ihnen das? Meist großes Nein. Dann: Funktioniert es? Für wen? Ling's Cars nennt sich selbst Großbritanniens größte unabhängige Verkäuferin von Neuwagen (Zitat The Guardian, 2017, auf der Seite). Die Seite ist bewusst laut, persönlich und unverwechselbar.

  Der Netto-Prospekt: Für viele unattraktiv, für seine Zielgruppe hoch funktional. Preise springen ins Auge, Rabatte sind sofort erkennbar.

  **Und anderswo? (ca. 5 Minuten)**

  Vier Seiten, die aus europäischer Sicht oft als "zu voll" gelten und in ihrem Kontext sehr erfolgreich sind. Die Studierenden aus diesen Designkulturen als Expert:innen einbinden: Was ist dort normal, was gilt als vertrauenswürdig, was als billig?

  Häufig genannte Erklärungsansätze, ausdrücklich keine Gesetze: Chinesische und japanische Schriftzeichen tragen mehr Information pro Zeichen, dichte Seiten wirken für Lesende dieser Schriften weniger voll. Viel Information auf einen Blick kann als Zeichen von Vollständigkeit und Vertrauen gelesen werden. In Sprachen, die von rechts nach links geschrieben werden, spiegelt sich das ganze Layout, inklusive Navigation und Leserichtung. In vielen Märkten wird zuerst und vor allem mobil gelesen.

  Pointe: Ob uns etwas gefällt, sagt nichts darüber, ob es funktioniert. Qualität misst sich an Ziel, Zielgruppe und Kontext. Und was als schön gilt, ist kulturell gelernt.
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

{% interlude "Und anderswo?", "Gestaltung aus anderen Designkulturen" %}

{% screenshot "./images/kontext-rakuten.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Rakuten Ichiba, einer der großen Online-Marktplätze Japans<br><small>rakuten.co.jp, Screenshot 2026</small>"}' %}

{% screenshot "./images/kontext-sina.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Sina, eines der großen Nachrichtenportale Chinas<br><small>sina.com.cn, Screenshot 2026</small>"}' %}

{% screenshot "./images/kontext-haraj.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Haraj, Kleinanzeigenportal aus Saudi-Arabien. Gelesen wird von rechts nach links<br><small>haraj.com.sa, Screenshot 2026</small>"}' %}

{% screenshot "./images/kontext-nairaland.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Nairaland, eines der bekanntesten Online-Foren Nigerias<br><small>nairaland.com, Screenshot 2026</small>"}' %}

{% question "Was gilt dort als gut gemacht?", "Wer von Ihnen kennt Websites und Apps aus einem anderen Designkontext? Was ist dort anders?" %}

{% statement "Was als »zu voll« oder »zu leer« gilt, ist gelernt.", "Wir sehen Gestaltung immer durch unsere eigene Sehgewohnheit. Gute Gestaltung fragt, was ihre Zielgruppe gewohnt ist." %}

{% statement "Ob uns etwas gefällt, sagt nichts darüber, ob es funktioniert.", "Qualität misst sich an Ziel, Zielgruppe und Kontext. Nicht an unserem Geschmack." %}

{% statement "Woran merken Sie, dass Sie nicht nach Geschmack urteilen?", "Sie sagen nicht »schön«, sondern was ein Gestaltungsmittel bewirkt: »Die große Headline zieht den Blick zuerst nach oben, der Button ist das einzige farbige Element.«" %}
