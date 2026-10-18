---
title: Die dunkle Seite
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Dieselben Kontraste lassen sich gegen die Nutzenden einsetzen. Beim Cookie-Banner: Zustimmen bekommt Farbe, Fläche und Helligkeitskontrast (Bunt-Unbunt, Quantität, Hell-Dunkel), Ablehnen wird grau, klein und kontrastarm. Beide Wege sind formal da, aber nur einer wird gesehen.

  Die Wireframes zeigen das Prinzip, der Screenshot ein echtes Beispiel: Bei Otto steht »Einwilligung ablehnen« auf der ersten Ebene, aber grau und flach neben einem roten »OK«.

  Die deutschen Aufsichtsbehörden (DSK) erwarten, dass Ablehnen auf der ersten Ebene gleichwertig möglich ist. Faire Lösung: beide Buttons in derselben Gestaltung.

  Quellen: Brignull, Deceptive Patterns (2023), Kapitel »Visual interference«.
---

{% interlude "Die dunkle Seite", "Kontraste lenken. Auch weg von dem, was Nutzende wollen." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Zustimmen: bunt, groß, kontrastreich. Ablehnen: grau, klein, kaum sichtbar"}' %}
<rect data-id="bg" x="50" y="40" width="800" height="420" fill="#f2f2f2" />
<rect data-id="box" x="250" y="90" width="400" height="320" fill="#ffffff" />
<rect data-id="t" x="290" y="130" width="220" height="20" fill="#231f20" />
<rect data-id="z0" x="290" y="175" width="320" height="10" fill="#d9d9d9" />
<rect data-id="z1" x="290" y="199" width="290" height="10" fill="#d9d9d9" />
<rect data-id="z2" x="290" y="223" width="260" height="10" fill="#d9d9d9" />
<rect data-id="z3" x="290" y="247" width="230" height="10" fill="#d9d9d9" />
<rect data-id="b1" x="290" y="320" width="320" height="48" rx="24" fill="#9313ce" />
<rect data-id="b2" x="410" y="380" width="80" height="8" fill="#d9d9d9" />
{% endframe %}
{% screenshot "./images/banner-otto.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Ablehnen grau und flach, OK in kräftigem Rot<br><small>otto.de, Screenshot 2026</small>"}' %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Fair: beide Wege mit derselben Gestaltung"}' %}
<rect data-id="bg" x="50" y="40" width="800" height="420" fill="#f2f2f2" />
<rect data-id="box" x="250" y="90" width="400" height="320" fill="#ffffff" />
<rect data-id="t" x="290" y="130" width="220" height="20" fill="#231f20" />
<rect data-id="z0" x="290" y="175" width="320" height="10" fill="#d9d9d9" />
<rect data-id="z1" x="290" y="199" width="290" height="10" fill="#d9d9d9" />
<rect data-id="z2" x="290" y="223" width="260" height="10" fill="#d9d9d9" />
<rect data-id="z3" x="290" y="247" width="230" height="10" fill="#d9d9d9" />
<rect data-id="b1" x="290" y="320" width="150" height="48" rx="24" fill="#9313ce" />
<rect data-id="b2" x="460" y="320" width="150" height="48" rx="24" fill="#9313ce" />
{% endframe %}

{% question "Wem nützt dieser Kontrast?", "Die Frage für jeden Akzent, den Sie setzen." %}
