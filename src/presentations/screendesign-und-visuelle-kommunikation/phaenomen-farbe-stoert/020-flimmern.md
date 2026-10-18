---
title: Flimmern
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Erst nur schauen lassen: Was passiert an den Kanten? Viele sehen ein Flirren, die Kanten scheinen zu vibrieren oder vor- und zurückzuspringen. Manchen wird das schnell unangenehm, also nicht zu lange stehen lassen.

  Dann der Trick: Dieselbe Grafik in Graustufen. Rot und Blau haben fast dieselbe Leuchtdichte, das Muster verschwindet fast vollständig. Danach die Lösung: Blau gegen ein dunkles Blau getauscht, das Muster ist ruhig.

  Danach ein Text auf Orange: Blau flimmert, Grau verschwindet, Dunkelblau ist ruhig und lesbar.

  **Hintergrund**

  Kanten und Formen erkennt unser visuelles System vor allem über Helligkeitsunterschiede. Haben zwei Farben dieselbe Helligkeit (Isoluminanz), fehlt dieses Signal, die Kante wird unscharf und instabil. Margaret Livingstone beschreibt das in »Vision and Art: The Biology of Seeing« (2002). Dazu kommt, dass das Auge Rot und Blau unterschiedlich bricht (chromatische Aberration): Beide Farben liegen nicht in derselben Schärfeebene, die Kante scheint zu springen. Albers nennt das in »Interaction of Color« (1963) »vibrierende Grenzen«.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Was passiert an den Kanten?"}' %}
<rect data-id="f0" x="50" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f1" x="140" y="60" width="90" height="380" fill="#0082ff" />
<rect data-id="f2" x="230" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f3" x="320" y="60" width="90" height="380" fill="#0082ff" />
<rect data-id="f4" x="410" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f5" x="500" y="60" width="90" height="380" fill="#0082ff" />
<rect data-id="f6" x="590" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f7" x="680" y="60" width="90" height="380" fill="#0082ff" />
<rect data-id="f8" x="770" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="mq" x="300" y="170" width="300" height="160" fill="#0082ff" />
<rect data-id="mi" x="360" y="210" width="180" height="80" fill="#ff2a2a" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dieselbe Grafik in Graustufen: Rot und Blau sind fast gleich hell"}' %}
<rect data-id="f0" x="50" y="60" width="90" height="380" fill="#848484" />
<rect data-id="f1" x="140" y="60" width="90" height="380" fill="#828282" />
<rect data-id="f2" x="230" y="60" width="90" height="380" fill="#848484" />
<rect data-id="f3" x="320" y="60" width="90" height="380" fill="#828282" />
<rect data-id="f4" x="410" y="60" width="90" height="380" fill="#848484" />
<rect data-id="f5" x="500" y="60" width="90" height="380" fill="#828282" />
<rect data-id="f6" x="590" y="60" width="90" height="380" fill="#848484" />
<rect data-id="f7" x="680" y="60" width="90" height="380" fill="#828282" />
<rect data-id="f8" x="770" y="60" width="90" height="380" fill="#848484" />
<rect data-id="mq" x="300" y="170" width="300" height="160" fill="#828282" />
<rect data-id="mi" x="360" y="210" width="180" height="80" fill="#848484" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Mit Helligkeitsunterschied wird es ruhig"}' %}
<rect data-id="f0" x="50" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f1" x="140" y="60" width="90" height="380" fill="#0b1f6b" />
<rect data-id="f2" x="230" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f3" x="320" y="60" width="90" height="380" fill="#0b1f6b" />
<rect data-id="f4" x="410" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f5" x="500" y="60" width="90" height="380" fill="#0b1f6b" />
<rect data-id="f6" x="590" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="f7" x="680" y="60" width="90" height="380" fill="#0b1f6b" />
<rect data-id="f8" x="770" y="60" width="90" height="380" fill="#ff2a2a" />
<rect data-id="mq" x="300" y="170" width="300" height="160" fill="#0b1f6b" />
<rect data-id="mi" x="360" y="210" width="180" height="80" fill="#ff2a2a" />
{% endframe %}

{% screenshot "./images/flimmern-text.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Und mit Text"}' %}
