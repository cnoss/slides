---
title: "Innen und außen"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Die Skala allein macht noch keine Ordnung. Die Regel aus dem Gesetz der Nähe gilt weiter: Was zusammengehört, steht enger. Innerhalb der Card liegen die Abstände bei 8 bis 24, zwischen den Cards bei 32 oder mehr. Wäre der Abstand zwischen den Cards kleiner als der Innenabstand, würden Titel und Bild der Nachbarcard optisch zusammenrücken.

  Der Code zeigt, wie direkt sich das übergeben lässt: Die Skala steht einmal als CSS-Variablen da, jede Komponente nimmt sich ihre Werte. Figma Variables lassen sich genauso benennen. Wer so arbeitet, muss in der Übergabe keine Pixel mehr nachmessen.
---

{% interlude "Innen enger als außen", "Die Skala sagt, welche Werte. Die Nähe sagt, wo." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Innen 8 bis 24, außen 40: Jede Card bleibt eine Einheit"}' %}
<rect data-id="k0-karte" x="60.0" y="60.0" width="230.0" height="270.6" fill="#e4e4e4" />
<rect data-id="k0-bild" x="60.0" y="60.0" width="230.0" height="115.0" fill="#c4c4c4" />
<rect data-id="k0-kat" x="78.4" y="193.4" width="53.7" height="6.1" fill="#888888" />
<rect data-id="k0-t1" x="78.4" y="205.7" width="193.2" height="12.3" fill="#888888" />
<rect data-id="k0-t2" x="78.4" y="224.1" width="119.8" height="12.3" fill="#888888" />
<rect data-id="k0-e0" x="78.4" y="248.6" width="193.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k0-e1" x="78.4" y="260.9" width="193.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k0-e2" x="78.4" y="273.1" width="135.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k0-link" x="78.4" y="298.4" width="49.1" height="7.7" fill="#231f20" />
<path data-id="k0-pfeil" d="M133.6 298.4 L137.4 302.3 L133.6 306.1" fill="none" stroke="#231f20" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" />
<rect data-id="k1-karte" x="330.0" y="60.0" width="230.0" height="270.6" fill="#e4e4e4" />
<rect data-id="k1-bild" x="330.0" y="60.0" width="230.0" height="115.0" fill="#c4c4c4" />
<rect data-id="k1-kat" x="348.4" y="193.4" width="53.7" height="6.1" fill="#888888" />
<rect data-id="k1-t1" x="348.4" y="205.7" width="193.2" height="12.3" fill="#888888" />
<rect data-id="k1-t2" x="348.4" y="224.1" width="119.8" height="12.3" fill="#888888" />
<rect data-id="k1-e0" x="348.4" y="248.6" width="193.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k1-e1" x="348.4" y="260.9" width="193.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k1-e2" x="348.4" y="273.1" width="135.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k1-link" x="348.4" y="298.4" width="49.1" height="7.7" fill="#231f20" />
<path data-id="k1-pfeil" d="M403.6 298.4 L407.4 302.3 L403.6 306.1" fill="none" stroke="#231f20" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" />
<rect data-id="k2-karte" x="600.0" y="60.0" width="230.0" height="270.6" fill="#e4e4e4" />
<rect data-id="k2-bild" x="600.0" y="60.0" width="230.0" height="115.0" fill="#c4c4c4" />
<rect data-id="k2-kat" x="618.4" y="193.4" width="53.7" height="6.1" fill="#888888" />
<rect data-id="k2-t1" x="618.4" y="205.7" width="193.2" height="12.3" fill="#888888" />
<rect data-id="k2-t2" x="618.4" y="224.1" width="119.8" height="12.3" fill="#888888" />
<rect data-id="k2-e0" x="618.4" y="248.6" width="193.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k2-e1" x="618.4" y="260.9" width="193.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k2-e2" x="618.4" y="273.1" width="135.2" height="6.9" fill="#aaaaaa" />
<rect data-id="k2-link" x="618.4" y="298.4" width="49.1" height="7.7" fill="#231f20" />
<path data-id="k2-pfeil" d="M673.6 298.4 L677.4 302.3 L673.6 306.1" fill="none" stroke="#231f20" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" />
<rect x="290" y="60" width="40" height="270.6" fill="#9313ce" fill-opacity="0.45" />
<rect x="560" y="60" width="40" height="270.6" fill="#9313ce" fill-opacity="0.45" />
{% endframe %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Dieselbe Skala im Code</h1>
    <pre style="font-size:3vh;line-height:1.5;text-align:left;width:100%;box-shadow:none;"><code class="language-css">:root {
  --space-s: 8px;
  --space-m: 16px;
  --space-l: 24px;
  --space-xl: 40px;
}
.card  { padding: var(--space-l); display: flex; flex-direction: column; gap: var(--space-m); }
.link  { display: flex; gap: var(--space-s); }
.cards { display: grid; gap: var(--space-xl); }</code></pre>
  </div>
</section>
