---
title: Competencies
layout: presentation.11ty.js
slideClasses: images
status: hidden


kompetenz: |
  Wissen<span class="fragment"> + Können</span><span class="fragment"> + Wollen</span><span class="fragment"> + Kontextsensibilität</span>

kompetenzSatz: |
  Eine Kompetenz beschreibt die Fähigkeit, Wissen, Fertigkeiten und Haltung in konkreten Situationen selbstorganisiert und verantwortungsvoll anzuwenden.

dbTeam: ./images/digital-product-team.png

---


{% statement "Kompetenz", kompetenz %}

{% question kompetenzSatz, false, '{"classes":"align-left"}' %}

{% image dbTeam, '{"transition":"fade", "classes":"no-shadow", "bu": "Ideales Team, DB Reisendeninformation 2016"}' %}

{% question "Welche Kompetenzen brauchen wir <del>an der Schnittstelle</del><br>am Übergang zu anderen Disziplinen?", false, '{"classes":"align-left fit-text"}' %}
