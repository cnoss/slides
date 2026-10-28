---
title: "Hierarchie abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Nach den Grafiken aus dem bisherigen Foliensatz (Wahrnehmungsarbeit). Bei jeder Folie fragen: Wo schauen Sie zuerst hin?

  Ein Element: keine Frage der Reihenfolge. Zwei gleiche: Der Blick pendelt, meist beginnt er links (Leserichtung). Tritt eins zurück, gibt es eine Reihenfolge. Sechzehn gleiche Elemente bieten keinen Einstieg, der Blick wandert. Wird eins betont und alle anderen treten zurück, ist der Einstieg klar. Mit drei Stufen entsteht eine Lesereihenfolge: erst das Große, dann die mittlere Stufe, dann der Rest.

  Wichtig: In der fünften Folie wurde kein Element lauter gemacht. Alle anderen wurden leiser.
---

{% frame '{"stage":"#ffffff","bu":"Ein Element"}' %}
  <circle data-id="k0" cx="300" cy="300" r="40" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Zwei gleiche: Wo fangen Sie an?"}' %}
  <circle data-id="k0" cx="200" cy="300" r="40" fill="#231f20" />
  <circle data-id="k1" cx="400" cy="300" r="40" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Eins tritt zurück: Jetzt gibt es eine Reihenfolge"}' %}
  <circle data-id="k0" cx="200" cy="300" r="40" fill="#231f20" />
  <circle data-id="k1" cx="400" cy="300" r="40" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Sechzehn gleiche: kein Einstieg"}' %}
  <circle data-id="k0" cx="150" cy="150" r="36" fill="#231f20" />
  <circle data-id="k1" cx="250" cy="150" r="36" fill="#231f20" />
  <circle data-id="k2" cx="350" cy="150" r="36" fill="#231f20" />
  <circle data-id="k3" cx="450" cy="150" r="36" fill="#231f20" />
  <circle data-id="k4" cx="150" cy="250" r="36" fill="#231f20" />
  <circle data-id="k5" cx="250" cy="250" r="36" fill="#231f20" />
  <circle data-id="k6" cx="350" cy="250" r="36" fill="#231f20" />
  <circle data-id="k7" cx="450" cy="250" r="36" fill="#231f20" />
  <circle data-id="k8" cx="150" cy="350" r="36" fill="#231f20" />
  <circle data-id="k9" cx="250" cy="350" r="36" fill="#231f20" />
  <circle data-id="k10" cx="350" cy="350" r="36" fill="#231f20" />
  <circle data-id="k11" cx="450" cy="350" r="36" fill="#231f20" />
  <circle data-id="k12" cx="150" cy="450" r="36" fill="#231f20" />
  <circle data-id="k13" cx="250" cy="450" r="36" fill="#231f20" />
  <circle data-id="k14" cx="350" cy="450" r="36" fill="#231f20" />
  <circle data-id="k15" cx="450" cy="450" r="36" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Alle anderen treten zurück: ein Einstieg"}' %}
  <circle data-id="k0" cx="150" cy="150" r="36" fill="#231f20" />
  <circle data-id="k1" cx="250" cy="150" r="36" fill="#d9d9d9" />
  <circle data-id="k2" cx="350" cy="150" r="36" fill="#d9d9d9" />
  <circle data-id="k3" cx="450" cy="150" r="36" fill="#d9d9d9" />
  <circle data-id="k4" cx="150" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k5" cx="250" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k6" cx="350" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k7" cx="450" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k8" cx="150" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k9" cx="250" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k10" cx="350" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k11" cx="450" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k12" cx="150" cy="450" r="36" fill="#d9d9d9" />
  <circle data-id="k13" cx="250" cy="450" r="36" fill="#d9d9d9" />
  <circle data-id="k14" cx="350" cy="450" r="36" fill="#d9d9d9" />
  <circle data-id="k15" cx="450" cy="450" r="36" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Drei Stufen: eine Lesereihenfolge"}' %}
  <circle data-id="k0" cx="150" cy="150" r="56" fill="#231f20" />
  <circle data-id="k1" cx="250" cy="150" r="36" fill="#888888" />
  <circle data-id="k2" cx="350" cy="150" r="36" fill="#888888" />
  <circle data-id="k3" cx="450" cy="150" r="36" fill="#888888" />
  <circle data-id="k4" cx="150" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k5" cx="250" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k6" cx="350" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k7" cx="450" cy="250" r="36" fill="#d9d9d9" />
  <circle data-id="k8" cx="150" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k9" cx="250" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k10" cx="350" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k11" cx="450" cy="350" r="36" fill="#d9d9d9" />
  <circle data-id="k12" cx="150" cy="450" r="36" fill="#d9d9d9" />
  <circle data-id="k13" cx="250" cy="450" r="36" fill="#d9d9d9" />
  <circle data-id="k14" cx="350" cy="450" r="36" fill="#d9d9d9" />
  <circle data-id="k15" cx="450" cy="450" r="36" fill="#d9d9d9" />
{% endframe %}
