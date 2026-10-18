---
title: Die dunkle Seite
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Farbe zum Emotionalisieren lässt sich gegen die Nutzenden einsetzen. Klassiker: falsche Dringlichkeit. Rote Hinweise wie »Nur noch 2 Zimmer frei!« oder ein roter Countdown erzeugen Stress, damit schneller gebucht wird. Rot aktiviert, das ist gewollt, aber hier verhindert es eine überlegte Entscheidung.

  Harry Brignull nennt das »False urgency« und »Fake scarcity«. Die EU-Verbraucherschutzbehörden sind mehrfach gegen Buchungsportale vorgegangen, unter anderem 2019 gegen irreführende Knappheitshinweise.

  Die Wireframes zeigen das Prinzip: dieselbe Hotelkarte, einmal ruhig, einmal mit roten Dringlichkeitshinweisen.
---

{% interlude "Die dunkle Seite", "Farbe macht Stimmung. Auch Druck." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eine Hotelkarte, ruhig"}' %}
<rect data-id="bg" x="200" y="40" width="500" height="420" rx="0" fill="#ffffff" />
<rect x="200" y="40" width="500" height="420" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="img" x="230" y="70" width="440" height="150" rx="0" fill="#d9d9d9" />
<rect data-id="h" x="230" y="245" width="260" height="24" rx="0" fill="#231f20" />
<rect data-id="t0" x="230" y="285" width="380" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t1" x="230" y="307" width="320" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="btn" x="540" y="395" width="130" height="40" rx="20" fill="#9313ce" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dieselbe Karte mit roten Hinweisen: »Nur noch 2 frei!«, Countdown"}' %}
<rect data-id="bg" x="200" y="40" width="500" height="420" rx="0" fill="#ffffff" />
<rect x="200" y="40" width="500" height="420" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="img" x="230" y="70" width="440" height="150" rx="0" fill="#d9d9d9" />
<rect data-id="h" x="230" y="245" width="260" height="24" rx="0" fill="#231f20" />
<rect data-id="t0" x="230" y="285" width="380" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t1" x="230" y="307" width="320" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="badge" x="230" y="340" width="240" height="32" rx="4" fill="#e8002a" />
<rect data-id="timer" x="490" y="340" width="180" height="32" rx="4" fill="#e8002a" />
<rect data-id="btn" x="540" y="395" width="130" height="40" rx="20" fill="#9313ce" />
{% endframe %}

{% question "Wem nützt dieses Rot?", "Den Nutzenden, die informiert sein wollen? Oder dem Anbieter, der schnell verkaufen will?" %}
