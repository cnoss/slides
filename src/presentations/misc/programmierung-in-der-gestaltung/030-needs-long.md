---
title: Needs
layout: presentation.11ty.js
slideClasses: images
status: hidden

tShape01: ./images/t-shaped-04.png
tShape02: ./images/t-shaped-03.png
tShape03: ./images/t-shaped-02.png
tShape04: ./images/t-shaped-01.png
tShape05: ./images/t-shaped-04a.png
tShape06: ./images/t-shaped-04b.png



bitkommPhiWs: ./images/bitkomm-phi-black.jpg

bitkommPhi: ./images/bitkomm-phi.png

anspruch: |
  Wir wollen sicher­stellen, dass unsere Studie­renden ein <mark><strong>Höchstmaß an Profes­sio­na­lität</strong></mark> errei­chen und eine aktive Rolle im Sinne der Nutzer:innen von Gestal­tungs­dienst­leis­tungen einnehmen.

kompetenz: |
  Wissen<span class="fragment"> + Können</span><span class="fragment"> + Wollen</span><span class="fragment"> + Kontextsensibilität</span>

kompetenzSatz: |
  Eine Kompetenz beschreibt die Fähigkeit, Wissen, Fertigkeiten und Haltung in konkreten Situationen selbstorganisiert und verantwortungsvoll anzuwenden.

dbTeam: ./images/digital-product-team.png
tShapeTeam: ./images/digital-product-t-shaped-team.png



---
{% image "./images/hfg-triade.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"https://www.hfg-gmuend.de/hochschule/geschichte"}' %}

{% statement anspruch %}

{% image tShape06, '{"transition":"fade", "classes":"no-shadow", "bu":"Generalist: jemand, der über breit gefächertes Wissen und vielseitige Fähigkeiten in verschiedenen Bereichen verfügt."}' %}
{% image tShape05, '{"transition":"fade", "classes":"no-shadow", "bu":"Spezialistin: jemand, der sich auf ein bestimmtes Fachgebiet konzentriert und darin über tiefgehendes Wissen und hohe Expertise verfügt."}' %}
{% image tShape01, '{"transition":"fade", "classes":"no-shadow", "bu":"Introduced by David Guest in 1991,<br>coined by Tim Brown 15 years later."}' %}
{% image tShape03, '{"transition":"fade", "classes":"no-shadow" }' %}
{% image tShape04, '{"transition":"fade", "classes":"no-shadow", "bu":"Vielleicht passend für die HFG – Gestaltung, Technologie & Wissenschaft"}' %}


{% image dbTeam, '{"transition":"fade", "classes":"no-shadow", "bu": "Ideales Team, DB Reisendeninformation 2016"}' %}
{% image tShapeTeam, '{"transition":"fade", "classes":"no-shadow", "bu": "Ideales Team, DB Reisendeninformation 2016"}' %}

{% image bitkommPhi, '{"transition":"fade", "classes":"no-shadow", "bu": "<a href=\'https://www.bitkom.org/sites/main/files/file/import/20171013-Rollenideal-Digital-Design.pdf\'>Rollenideal «Digital Design»</a>, Bitkom 2017"}' %}

{% statement "Kompetenz", kompetenz %}

{% question "Welche Kompetenzen brauchen wir <del>an der Schnittstelle</del> am Übergang zu anderen Disziplinen?", false, '{"classes":"align-left fit-text"}' %}