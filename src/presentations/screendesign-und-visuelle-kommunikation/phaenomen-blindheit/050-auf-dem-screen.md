---
title: Auf dem Screen
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Formular als Wireframe. Der gestrichelte Kreis ist der Blick: Wer gerade auf »Absenden« geklickt hat, schaut auf den Button. Erscheint die Fehlermeldung oben, wird sie leicht übersehen, besonders wenn die Seite dabei neu lädt (Unterbrechung wie beim Flimmern). Typische Folge: Menschen klicken mehrfach auf Absenden und denken, das Formular sei kaputt.

  Besser: Die Rückmeldung erscheint dort, wo der Blick ist, und markiert das betroffene Feld. Im Kleinen genauso: Ein Warenkorb-Zähler, der sich beim Seitenwechsel still um eins erhöht, wird oft nicht bemerkt.
---

{% frame '{"bu":"Ein Formular. Der Blick ist beim Button."}' %}
<rect data-id="l0" x="150" y="120" width="110" height="12" fill="#888888" />
<rect data-id="f0" x="150" y="142" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="l1" x="150" y="220" width="110" height="12" fill="#888888" />
<rect data-id="f1" x="150" y="242" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="l2" x="150" y="320" width="110" height="12" fill="#888888" />
<rect data-id="f2" x="150" y="342" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="btn" x="150" y="440" width="140" height="44" rx="22" fill="#231f20" />
<circle data-id="blick" cx="220" cy="462" r="70" fill="none" stroke="#888888" stroke-width="2" stroke-dasharray="6 6" />
{% endframe %}
{% frame '{"bu":"Die Fehlermeldung erscheint oben. Wer schaut da hin?"}' %}
<rect data-id="err" x="60" y="40" width="480" height="36" fill="#9313ce" />
<rect data-id="l0" x="150" y="120" width="110" height="12" fill="#888888" />
<rect data-id="f0" x="150" y="142" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="l1" x="150" y="220" width="110" height="12" fill="#888888" />
<rect data-id="f1" x="150" y="242" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="l2" x="150" y="320" width="110" height="12" fill="#888888" />
<rect data-id="f2" x="150" y="342" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="btn" x="150" y="440" width="140" height="44" rx="22" fill="#231f20" />
<circle data-id="blick" cx="220" cy="462" r="70" fill="none" stroke="#888888" stroke-width="2" stroke-dasharray="6 6" />
{% endframe %}
{% frame '{"bu":"Besser: Die Rückmeldung erscheint auch dort, wo das Problem ist."}' %}
<rect data-id="err" x="60" y="40" width="480" height="36" fill="#9313ce" />
<rect data-id="l0" x="150" y="120" width="110" height="12" fill="#888888" />
<rect data-id="f0" x="150" y="142" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="l1" x="150" y="220" width="110" height="12" fill="#888888" />
<rect data-id="f1" x="150" y="242" width="300" height="44" fill="#ffffff" stroke="#9313ce" stroke-width="4" />
<rect data-id="l2" x="150" y="320" width="110" height="12" fill="#888888" />
<rect data-id="f2" x="150" y="342" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="hint" x="150" y="294" width="200" height="10" fill="#9313ce" />
<rect data-id="btn" x="150" y="440" width="140" height="44" rx="22" fill="#231f20" />
<circle data-id="blick" cx="220" cy="462" r="70" fill="none" stroke="#888888" stroke-width="2" stroke-dasharray="6 6" />
{% endframe %}
