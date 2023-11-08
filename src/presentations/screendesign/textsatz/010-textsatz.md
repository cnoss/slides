---
title: Worum geht es?
layout: presentation.11ty.js
slideClasses: images
status: ok
---


{% screenshot "./images/textsatz-01.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":""}' %}

{% screenshot "./images/blocksatz-01-gut.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Blocksatz"}' %}
{% screenshot "./images/blocksatz-02-besser.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Blocksatz mit optischem Randausgleich"}' %}
{% screenshot "./images/blocksatz-03-erzwungen.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Erzwungener Blocksatz"}' %}
{% screenshot "./images/blocksatz-04-schmal.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Blocksatz"}' %}
{% screenshot "./images/blocksatz-05-schmal-ohne-st.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Blocksatz ohne Silbentrennung"}' %}
{% screenshot "./images/blocksatz-06-schlecht.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Microsoft Word Blocksatz"}' %}
{% screenshot "./images/blocksatz-07-html.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"HTML Blocksatz"}' %}

{% screenshot "./images/blocksatz-example-01.png", '{"transition":"fade", "classes": "shadow", "width":"auto", "bu":"Blocksatz"}' %}
{% screenshot "./images/blocksatz-example-02.png", '{"transition":"fade", "classes": "shadow", "width":"auto", "bu":"Blocksatz"}' %}


{% screenshot "./images/rauhsatz-01.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Linksbündiger Rauhsatz"}' %}
{% screenshot "./images/rauhsatz-02-ora.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Linksbündiger Rauhsatz mit optischem Randausgleich"}' %}

{% screenshot "./images/flattersatz-01.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Linksbündiger Flattersatz"}' %}
{% screenshot "./images/flattersatz-02-rechts.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Rechtsbündiger Flattersatz"}' %}
{% screenshot "./images/flattersatz-03-schmal.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Linksbündiger Flattersatz"}' %}
{% screenshot "./images/flattersatz-04-html.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Linksbündiger HTML Flattersatz"}' %}

{% screenshot "./images/mittelachs-01.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Symmetrischer Satz, auch Mittelachssatz oder axialer Satz"}' %}

{% screenshot "./images/formsatz-01.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Formsatz"}' %}
{% screenshot "./images/formsatz-02.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Formsatz"}' %}

{% screenshot "./images/strukturieren-01.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Texte strukturieren"}' %}
{% screenshot "./images/strukturieren-02.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Hurenkind"}' %}
{% screenshot "./images/strukturieren-03.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Ohne Hurenkind"}' %}
{% screenshot "./images/strukturieren-04.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"Schusterjunge"}' %}

<section class="simple">
  <div>
    <h1>Textsatz KnowHow</h1>
    <div>
      {% fragment "<p class=\"list\">Ziel bei Mengentexten ist die Wirkung als möglichst <strong>gleichmäßige Graufläche</strong></p>" %}
      {% fragment "<p class=\"list\">Buchstabenabstand <strong>&lt;
</strong> Wortabstand <strong>&lt;</strong> Zeilenabstand <strong>&lt;</strong> Spaltenabstand</p>" %}
      {% fragment "<p class=\"list\">Spatonierung sollte bei sehr <strong>großen</strong> und sehr<strong>kleinen</strong> Schriftgraden <strong>angepasst</strong> werden: kleine Schriften (&lt; 9pt) benötigen eine größere Spationierung, große Schriften &gt; 16pt eine kleinere Spatonierung. </p>" %}
    </div>
</section>

<section class="simple">
  <div>
    <h1>Textsatz KnowHow</h1>
    <div>
      {% fragment "<p class=\"list\">Der <strong>Zeilenabstand</strong> sollte zwischen <strong>120%</strong> und <strong>130%</strong> des Schriftgrades betragen. Kleine Schriften (&lt; 9pt) oder breite Spalten benötigen einen größeren Zeilenabstand, große Schriften (&gt; 16pt) oder schmale Spalten benötigen einen kleineren Zeilenabstand.</p>" %}
      {% fragment "<p class=\"list\">Die Spaltenbreite sollte so gewählt sein, dass <strong>Zeilenlängen</strong> zwischen <strong>9</strong> und <strong>13 Worten</strong> oder 60 und 80 Zeichen entstehen.</p>" %}
      {% fragment "<p class=\"list\">Der <strong>Spaltenabstand</strong> sollte etwa so groß wie der <strong>Schriftgrad</strong> sein.</p>" %}
    </div>
</section>
<section class="simple">
  <div>
    <h1>Textsatz KnowHow</h1>
    <div>
      {% fragment "<p class=\"list\">Längere Texte sollten in <strong>kurze Absätze</strong> gegliedert werden. </p>" %}
      {% fragment "<p class=\"list\">Falls Sie Silbentrennung verwenden, vermeiden Sie Endzeilen, die <strong>ausschließlich</strong> aus <strong>einem Wortteil</strong> bestehen.</p>" %}
      {% fragment "<p class=\"list\">Falls Mehrspaltsatz verwenden, vermeiden Sie <strong>Hurenkinder</strong> und <strong>Schusterjungen</strong>.</p>" %}
      {% fragment "<p class=\"list\">Verwenden Sie <strong>rechtsbündigen</strong> Flatter- oder Rauhsatz, <strong>symmetrischen</strong> oder <strong>Formsatz</strong> nur in Ausnahmefällen oder für <strong>kurze Texte</strong>.</p>" %}
    </div>
</section>
<section class="simple">
  <div>
    <h1>Textsatz KnowHow</h1>
    <div>
      {% fragment "<p class=\"list\">Achten Sie beim <strong>Blocksatz</strong> auf <strong>gleichmäßige Wortabstände</strong>. Diese ergeben sich nur, wenn die Zeilen lang genug sind, <strong>Silbentrennung</strong> möglich ist und das Satzprogramm (oder Sie!) den Randausgleich über Wortabstand UND Buchstabenabstand realisiert.</p>" %}
      {% fragment "<p class=\"list\">Verwenden Sie <strong>keine Silbentrennung</strong> in <strong>Überschriften</strong>.</p>" %}
    </div>
</section>

{% screenshot "./images/beispiel-01.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":""}' %}
{% screenshot "./images/beispiel-02.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"https://type.method.ac/"}' %}
{% screenshot "./images/beispiel-03.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"https://shape.method.ac/"}' %}
{% screenshot "./images/beispiel-04.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"https://typewar.com/"}' %}
{% screenshot "./images/beispiel-05.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"https://tothepoint.co.uk/"}' %}
{% screenshot "./images/beispiel-06.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"http://typeconnection.com/"}' %}
{% screenshot "./images/beispiel-07.png", '{"transition":"fade", "classes": "no-shadow", "width":"auto", "bu":"https://fathom.info/"}' %}