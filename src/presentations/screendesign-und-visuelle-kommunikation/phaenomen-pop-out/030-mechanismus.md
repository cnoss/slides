---
title: "Mechanismus"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Ein Teil der Verarbeitung läuft parallel über das ganze Gesichtsfeld, bevor die Aufmerksamkeit irgendwohin gelenkt wird: präattentiv. Einfache Merkmale wie Farbe, Größe, Ausrichtung und Bewegung werden dort schon erfasst. Weicht ein Element in genau einem solchen Merkmal ab, springt es heraus, egal wie viele andere Elemente da sind.

  Eine Kombination von Merkmalen erkennt erst die Aufmerksamkeit, und die arbeitet nacheinander. Deshalb wächst die Suchzeit mit jedem zusätzlichen Element.

  Welche Merkmale das sind, zeigt das Prinzip Kontrast und Hervorhebung Folie für Folie.

  **Hintergrund**

  Anne Treisman und Garry Gelade, »A feature-integration theory of attention«, Cognitive Psychology 12, 1980. Merkmalsintegrationstheorie: Merkmale werden parallel registriert, ihre Verknüpfung zu einem Objekt braucht serielle Aufmerksamkeit. In ihren Versuchen blieb die Suchzeit bei Merkmalssuche fast gleich, bei Konjunktionssuche stieg sie mit der Zahl der Elemente linear an.

  Colin Ware, »Visual Thinking for Information Design« (2. Auflage 2021), nennt als präattentiv u. a. Farbe, Größe, Ausrichtung, Bewegung, Krümmung und Hinzufügungen (z. B. ein Rahmen). Form wirkt nur teilweise: Ein Kreis zwischen Quadraten springt weniger stark heraus als eine abweichende Farbe.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Was sofort ins Auge springt</h1>
    {% fragment '<p class="list"><strong>Farbe</strong></p>' %}
    {% fragment '<p class="list"><strong>Größe</strong></p>' %}
    {% fragment '<p class="list"><strong>Ausrichtung</strong></p>' %}
    {% fragment '<p class="list"><strong>Bewegung</strong></p>' %}
    {% fragment '<p class="list"><strong>Form</strong>, aber schwächer</p>' %}
  </div>
</section>

{% statement "Ein Merkmal: sofort, egal wie viele.", "Eine Kombination: Element für Element. Je mehr Elemente, desto länger dauert es." %}
