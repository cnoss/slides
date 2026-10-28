---
title: "Die dunkle Seite"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Hierarchie entscheidet, was gesehen wird. Und damit auch, was nicht gesehen wird.

  Eine Kontoseite als Wireframe. Erst fragen: Wo kündigen Sie hier? Niemand findet es, und das ist der Punkt. Dann die Auflösung: Der Link »Kündigen« steht klein und hellgrau im Footer, zwischen Impressum, Datenschutz und AGB. Drei Prinzipien arbeiten zusammen gegen die Nutzenden:

  - **Hierarchie:** Das Upgrade ist das größte und einzige farbige Element, das Kündigen das kleinste und blasseste.
  - **Nähe:** Der Link steht in der Gruppe der Pflichtlinks, die niemand liest. Er gehört scheinbar zum Kleingedruckten, nicht zum Vertrag.
  - **Figur und Grund:** Mit so wenig Kontrast wird er nicht zur Figur, er verschwindet im Grund.

  Die ehrliche Variante: Kündigen steht dort, wo der Vertrag steht, als sekundärer Button. Das Upgrade bleibt die Hauptaktion, aber das Kündigen ist sichtbar und auffindbar.

  Verwandt: Hierarchie hebt auch die teure Option hervor. Das steht im Deck Kontrast und Hervorhebung (Lockangebot, Economist-Beispiel).

  **Hintergrund**

  Harry Brignull nennt das Muster »Roach Motel« bzw. »Hard to Cancel«: leicht hinein, schwer hinaus (»Deceptive Patterns«, 2023). In Deutschland gilt seit dem 1. Juli 2022 der Kündigungsbutton nach § 312k BGB: Wer online Verträge mit Dauerschuldverhältnis abschließen lässt, muss eine gut lesbare, ständig verfügbare und unmittelbar zugängliche Schaltfläche anbieten, beschriftet etwa mit »Verträge hier kündigen« (aus dem Gedächtnis, bitte prüfen). Gestaltung, die das Kündigen versteckt, ist also nicht nur unfair, sondern kann rechtswidrig sein.

  Prüffrage für jeden Entwurf: Wem nützt das?
---

{% interlude "Die dunkle Seite", "Hierarchie entscheidet, was gesehen wird. Und was nicht." %}

{% frame '{"w":900,"h":500,"bu":"Eine Kontoseite. Wo kündigen Sie hier?"}' %}
  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />
  <rect data-id="n1" x="640" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="n2" x="720" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="kopf" x="60" y="96" width="260" height="26" fill="#888888" />
  <rect data-id="karte" x="60" y="150" width="780" height="214" fill="#e4e4e4" />
  <rect data-id="k1" x="90" y="180" width="220" height="14" fill="#888888" />
  <rect data-id="k2" x="90" y="210" width="360" height="10" fill="#aaaaaa" />
  <rect data-id="k3" x="90" y="232" width="300" height="10" fill="#aaaaaa" />
  <rect data-id="upgrade" x="90" y="276" width="240" height="48" rx="24" fill="#9313ce" />
  <line data-id="trenner" x1="60" y1="404" x2="840" y2="404" stroke="#d9d9d9" stroke-width="2" stroke-linecap="round" />
  <rect data-id="f1" x="60" y="428" width="70" height="8" fill="#d9d9d9" />
  <rect data-id="f2" x="150" y="428" width="84" height="8" fill="#d9d9d9" />
  <rect data-id="kuendigen" x="254" y="428" width="64" height="8" fill="#d9d9d9" />
  <rect data-id="f3" x="338" y="428" width="50" height="8" fill="#d9d9d9" />
  <rect data-id="f4" x="408" y="428" width="64" height="8" fill="#d9d9d9" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Hier: klein, blass, zwischen den Pflichtlinks im Footer"}' %}
  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />
  <rect data-id="n1" x="640" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="n2" x="720" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="kopf" x="60" y="96" width="260" height="26" fill="#888888" />
  <rect data-id="karte" x="60" y="150" width="780" height="214" fill="#e4e4e4" />
  <rect data-id="k1" x="90" y="180" width="220" height="14" fill="#888888" />
  <rect data-id="k2" x="90" y="210" width="360" height="10" fill="#aaaaaa" />
  <rect data-id="k3" x="90" y="232" width="300" height="10" fill="#aaaaaa" />
  <rect data-id="upgrade" x="90" y="276" width="240" height="48" rx="24" fill="#9313ce" />
  <line data-id="trenner" x1="60" y1="404" x2="840" y2="404" stroke="#d9d9d9" stroke-width="2" stroke-linecap="round" />
  <rect data-id="f1" x="60" y="428" width="70" height="8" fill="#d9d9d9" />
  <rect data-id="f2" x="150" y="428" width="84" height="8" fill="#d9d9d9" />
  <rect data-id="kuendigen" x="254" y="428" width="64" height="8" fill="#d9d9d9" />
  <rect data-id="f3" x="338" y="428" width="50" height="8" fill="#d9d9d9" />
  <rect data-id="f4" x="408" y="428" width="64" height="8" fill="#d9d9d9" />
  <ellipse data-id="ring" cx="286" cy="432" rx="58" ry="24" fill="none" stroke="#9313ce" stroke-width="4" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Ehrlich: Kündigen steht beim Vertrag, als zweite Aktion"}' %}
  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />
  <rect data-id="n1" x="640" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="n2" x="720" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="kopf" x="60" y="96" width="260" height="26" fill="#888888" />
  <rect data-id="karte" x="60" y="150" width="780" height="214" fill="#e4e4e4" />
  <rect data-id="k1" x="90" y="180" width="220" height="14" fill="#888888" />
  <rect data-id="k2" x="90" y="210" width="360" height="10" fill="#aaaaaa" />
  <rect data-id="k3" x="90" y="232" width="300" height="10" fill="#aaaaaa" />
  <rect data-id="upgrade" x="90" y="276" width="240" height="48" rx="24" fill="#9313ce" />
  <line data-id="trenner" x1="60" y1="404" x2="840" y2="404" stroke="#d9d9d9" stroke-width="2" stroke-linecap="round" />
  <rect data-id="f1" x="60" y="428" width="70" height="8" fill="#d9d9d9" />
  <rect data-id="f2" x="150" y="428" width="84" height="8" fill="#d9d9d9" />
  <rect data-id="kuendigen" x="350" y="276" width="200" height="48" rx="24" fill="#e4e4e4" stroke="#231f20" stroke-width="2" />
  <rect data-id="f3" x="254" y="428" width="50" height="8" fill="#d9d9d9" />
  <rect data-id="f4" x="324" y="428" width="64" height="8" fill="#d9d9d9" />
{% endframe %}

{% question "Wem nützt diese Hierarchie?", "Den Nutzenden, die kündigen wollen? Oder dem Anbieter, der sie halten will?" %}
