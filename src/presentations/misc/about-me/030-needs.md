---
title: Needs
layout: presentation.11ty.js
slideClasses: images
status: ok

tShape: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxUiEgFykaIrMx1KEFPe9HqtRf-VYsODxjNeMRL-jh5EMOmkTtvQYwICwg0_Tlqxn6-eIg6qgvvdbzxZiZLkxWq_74bYSBJ71CbDM_R8lFysyUfGtfXxHQXyipGBgG6nTZ6UXH/s400/tshaped.png



bitkommPhiWs: ./images/bitkomm-phi-black.jpg

bitkommPhi: ./images/bitkomm-phi.png

anspruch: |
  Wir wollen sicher­stellen, dass unsere Studie­renden<br>ein <mark><strong>Höchstmaß an Profes­sio­na­lität</strong></mark> errei­chen und eine aktive Rolle im Sinne der Nutzer:innen von Gestal­tungs­dienst­leis­tungen einnehmen.

kompetenz: |
  Wissen<span class="fragment"> + Können</span><span class="fragment"> + Wollen</span><span class="fragment"> + Kontextsensibilität</span>

kompetenzSatz: |
  Eine Kompetenz beschreibt die Fähigkeit, Wissen, Fertigkeiten und Haltung in konkreten Situationen selbstorganisiert und verantwortungsvoll anzuwenden.

dbTeam: ./images/digital-product-team.png
tShapeTeam: ./images/digital-product-t-shaped-team.png



---
{% image "./images/hfg-triade.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"https://www.hfg-gmuend.de/hochschule/geschichte"}' %}

{% statement anspruch %}

{% image tShape, '{"transition":"fade", "classes":"no-shadow", "bu":"Introduced by David Guest in 1991, coined by Tim Brown 15 years later."}' %}
{% image tShapeTeam, '{"transition":"fade", "classes":"no-shadow", "bu":"Tim Brown, CEO of the IDEO design consultancy, endorsed this approach to résumé assessment as a method to build interdisciplinary work teams for creative processes."}' %}

{% image dbTeam, '{"transition":"fade", "classes":"no-shadow", "bu": "Ideales Team, DB Reisendeninformation 2016"}' %}
{% image tShapeTeam, '{"transition":"fade", "classes":"no-shadow", "bu": "Ideales Team, DB Reisendeninformation 2016"}' %}

{% image bitkommPhi, '{"transition":"fade", "classes":"no-shadow", "bu": "<a href=\'https://www.bitkom.org/sites/main/files/file/import/20171013-Rollenideal-Digital-Design.pdf\'>Rollenideal «Digital Design»</a>, Bitkom 2017"}' %}

{% statement "Kompetenz", kompetenz %}

{% question kompetenzSatz, false, '{"classes":"align-left"}' %}

{% question "Welche Kompetenzen brauchen wir <del>an der Schnittstelle</del> am Übergang zu anderen Disziplinen?", false, '{"classes":"align-left fit-text"}' %}