---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **1. Modul festlegen:** eine Form, wenige Farben. Je einfacher das Modul, desto deutlicher sieht man, was die Regel bewirkt.

  **2. Operationen wählen:** Was darf sich ändern? Drehen (meist in 90°-Schritten), spiegeln, verschieben, Farbe tauschen. Alles andere bleibt fest. Die Zahl der Elemente bleibt gleich, es kommt nichts Neues dazu.

  **3. Regel formulieren:** in einem Satz, den man laut sagen kann. »0° und 180° im Wechsel wie auf einem Schachbrett.« »Vier Kacheln drehen sich um eine gemeinsame Ecke.«

  **4. Durchspielen:** Die Regel konsequent anwenden und mehrere Regeln nebeneinanderstellen. Nicht bei der ersten Variante stehen bleiben, die halbwegs gefällt.

  **5. Auswählen und brechen:** Die stärkste Variante auswählen und begründen. Wer will, bricht die Regel an einer Stelle bewusst. Das ist dann eine Störung, siehe Pop-out.

  **Superform:** Die Form, die aus mehreren Modulen zusammen entsteht. Aus einem Viertelkreis werden durch Drehen Kreis, Blatt, Sanduhr und Halbkreis.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Permutation in fünf Schritten</h1>
    {% fragment '<p class="list"><strong>1. Modul festlegen:</strong> eine Form, wenige Farben</p>' %}
    {% fragment '<p class="list"><strong>2. Operationen wählen:</strong> drehen, spiegeln, verschieben, Farbe tauschen</p>' %}
    {% fragment '<p class="list"><strong>3. Regel formulieren:</strong> in einem Satz, den man laut sagen kann</p>' %}
    {% fragment '<p class="list"><strong>4. Durchspielen:</strong> mehrere Regeln nebeneinander, nicht die erste nehmen</p>' %}
    {% fragment '<p class="list"><strong>5. Auswählen und brechen:</strong> begründet wählen, die Regel bewusst an einer Stelle brechen</p>' %}
  </div>
</section>

{% frame '{"stage":"#ffffff", "animate":false, "w":600, "h":600, "bu":"Ein Viertelkreis in vier Lagen: 0°, 90°, 180°, 270°"}' %}
<g data-id="v0" transform="translate(110.0,270.0) rotate(0) translate(-50.0,-50.0)"><path d="M 0,100 L 0,0 A 100 100 0 0 1 100,100 Z" fill="#231f20" /></g>
<g data-id="v1" transform="translate(240.0,270.0) rotate(90) translate(-50.0,-50.0)"><path d="M 0,100 L 0,0 A 100 100 0 0 1 100,100 Z" fill="#231f20" /></g>
<g data-id="v2" transform="translate(370.0,270.0) rotate(180) translate(-50.0,-50.0)"><path d="M 0,100 L 0,0 A 100 100 0 0 1 100,100 Z" fill="#231f20" /></g>
<g data-id="v3" transform="translate(500.0,270.0) rotate(270) translate(-50.0,-50.0)"><path d="M 0,100 L 0,0 A 100 100 0 0 1 100,100 Z" fill="#231f20" /></g>
{% endframe %}

{% frame '{"stage":"#ffffff", "animate":false, "w":600, "h":600, "bu":"Superformen: Aus einem Modul entstehen durch Drehen neue Formen"}' %}
<g transform="translate(100.0,100.0) rotate(270) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(180.0,100.0) rotate(0) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(100.0,180.0) rotate(180) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(180.0,180.0) rotate(90) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(370.0,100.0) rotate(270) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(450.0,180.0) rotate(90) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(100.0,370.0) rotate(90) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(180.0,370.0) rotate(180) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(100.0,450.0) rotate(0) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(180.0,450.0) rotate(270) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(370.0,410.0) rotate(270) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
<g transform="translate(450.0,410.0) rotate(0) translate(-40.0,-40.0)"><path d="M 0,80 L 0,0 A 80 80 0 0 1 80,80 Z" fill="#231f20" /></g>
{% endframe %}
