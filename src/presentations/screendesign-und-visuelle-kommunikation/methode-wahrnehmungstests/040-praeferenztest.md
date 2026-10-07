---
title: Präferenztest
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Der Präferenztest (Tiefe: kennen) vergleicht zwei oder mehr Varianten: Welche bevorzugen Sie, und warum? Das Warum ist der eigentliche Ertrag. Die Mehrheit allein sagt wenig, die Begründungen zeigen, worauf es ankommt.

  Beispiel: zwei Varianten einer Produktkarte. A betont die Handlung, B den Preis. Kurz abstimmen lassen, dann nach Gründen fragen. Gut kombinierbar mit dem Semantischen Differential, wenn es um Wirkung geht (»Welche wirkt vertrauenswürdiger?«).

  Online-Werkzeuge wie Lyssna (früher UsabilityHub) bieten 5-Sekunden-Tests und Präferenztests mit externen Testpersonen an.
---

{% statement "Präferenztest", "Zwei Varianten, eine Frage: Welche bevorzugen Sie, und warum?" %}

{% frame '{"bu":"Variante A"}' %}
<rect data-id="bild" x="150" y="90" width="300" height="200" fill="#d9d9d9" />\n<rect data-id="h" x="150" y="320" width="220" height="24" fill="#231f20" />\n<rect data-id="t0" x="150" y="364" width="300" height="12" fill="#d9d9d9" />\n<rect data-id="t1" x="150" y="390" width="240" height="12" fill="#d9d9d9" />\n<rect data-id="btn" x="150" y="440" width="300" height="56" rx="28" fill="#9313ce" />
{% endframe %}
{% frame '{"bu":"Variante B"}' %}
<rect data-id="bild" x="150" y="90" width="300" height="200" fill="#d9d9d9" />\n<rect data-id="h" x="150" y="320" width="220" height="24" fill="#231f20" />\n<rect data-id="t0" x="150" y="364" width="300" height="12" fill="#d9d9d9" />\n<rect data-id="t1" x="150" y="390" width="240" height="12" fill="#d9d9d9" />\n<rect data-id="btn" x="150" y="450" width="140" height="40" rx="20" fill="#ffffff" stroke="#888888" stroke-width="2" />\n<rect data-id="preis" x="330" y="456" width="120" height="28" fill="#231f20" />
{% endframe %}

{% question "Welche würden Sie nutzen? Und warum?", "Das Warum ist wichtiger als die Mehrheit." %}
