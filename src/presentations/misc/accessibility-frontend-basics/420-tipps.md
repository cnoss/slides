---
title: Sematisches HTML
layout: presentation.11ty.js
slideClasses: wrap
code: |
  <header><h1>Willkommen</h1></header>
  <main>
    <section>
      <h2>Unser Angebot</h2>
      <p>Individuelle Beratung und Support …</p>
    </section>
  </main>

alt: |
  <img src="katze.jpg" 
    alt="Graue Katze schläft auf rotem Sofa">

aria: |
  <div role="tablist">
    <button role="tab" aria-selected="true">Details</button>
    <button role="tab" aria-selected="false">Bewertungen</button>
  </div>

kontraste: |
  **Kontrast-Anforderungen (WCAG)**
  **Normaler Text:** Mindestens 4.5:1<br>
  **Großer Text:** Mindestens 3:1<br>
  **UI-Elemente:** Mindestens 3:1<br>

  *Häufige Fehler vermeiden*<br>
  **Nicht nur Farbe** für wichtige Informationen nutzen<br>
  **Graue Texte** auf weißem Hintergrund prüfen

textFocus: |
  **Tab-Taste:** Zwischen interaktiven Elementen wechseln<br>
  **Enter/Space:** Buttons und Links aktivieren<br>
  **Pfeiltasten:** In Listen und Menüs navigieren<br>
  **Escape:** Dialoge und Overlays schließen

codeFocus: |
  /* Fokus sichtbar machen */
  button:focus {
    outline: 2px solid #005fcc;
    outline-offset: 2px;
  }
---

{% interlude "Was können wir dafür tun?", "Awareness, Code, Testing"%}

{% codeSmall "Semantisches HTML", "Gut strukturiertes, valides, semantisches HTML bedeutet, dass der Aufbau der Seite mit den richtigen HTML-Tags ihre inhaltliche Bedeutung widerspiegelt – sodass Menschen, Maschinen und Hilfsmittel die Inhalte verstehen und sinnvoll nutzen können..", code , "html", "slide" %}

{% codeSmall "Textäquivalente", "Ein guter Alternativtext (Alt-Text) beschreibt den Inhalt und Zweck eines Bildes klar, prägnant und kontextbezogen – für Menschen, die das Bild nicht sehen können (z. B. durch Screenreader oder bei deaktivierten Bildern im Browser).", alt , "javascript", "slide" %}

{% codeSmall "ARIA - Wenn HTML nicht reich", "ARIA (Accessible Rich Internet Applications) macht Inhalte für Screenreader zugänglich – aber nur, wenn HTML es nicht schon kann. Nutze ARIA, um Rollen, Zustände oder Beschriftungen zu ergänzen, nicht um fehlende Semantik zu ersetzen.", aria, "html", "slide" %}

{% simpleText "Farben und Kontraste", kontraste, '{"backgroundTransition":"slide"}' %}


{% codeSmall "Fokus und Tastatur-Navigation", textFocus, codeFocus , "javascript", "slide" %}