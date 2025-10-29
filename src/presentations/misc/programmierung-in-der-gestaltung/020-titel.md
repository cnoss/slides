---
title: Titel der Ausschreibung
layout: presentation.11ty.js
slideClasses: images
status: ok

design: |
  <p>
  «**Hochschule für Gestaltung** meint dabei mehr als nur Design im heutigen Sinne – es geht um die Gestaltung der menschlichen Umwelt.  Denn letztlich geht es um die Frage, wie der Mensch mit seiner Umwelt interagiert – und wie er sie gestaltet.»<br><small>Prof. Dr. Dagmar Rinker</small></p>
  <!--
  **Gestaltung** umfasst Denkweise und Prozess, also Prinzip, Methode und Reflexion, **Design** manifestiert sich in der Anwendungsdisziplin (Praxis, Umsetzung, Artefakt).-->

coding: |
  <div class="fragment is-unbalanced"><strong>Coding</strong> als Schreiben von Code als handwerkliche, konkrete Tätigkeit, bei der eine Idee oder ein Algorithmus in eine Programmiersprache übersetzt wird.</div>
  <div class="fragment is-unbalanced"><strong>Programmierung</strong> als systematische, strukturierte Entwicklung funktionaler Software. // Das reflektierte und systematische Entwerfen von Verhalten, Prozessen und Strukturen.</div>

program: |
  <div class="fragment is-unbalanced"><strong>Programmierung</strong> Substantiv, ist statisch, benennt, fixiert</div>
  <div class="fragment is-unbalanced"><strong>programmieren</strong> Verb, bewegt sich, ist dynamisch, beschreibt eine Tätigkeit, ist ein Werden</div>

mission: |
  Es geht um das Gestalten mit und durch Programmieren und somit die Erweiterung des gestalterischen <del>Denkens</del> Repertoires um algorithmische und technologische Mittel.

---
{% interlude "Programmierung in der Gestaltung", false, '{"transition": "fade"}' %}
{% interlude "Programmierung *|* in der *|* Gestaltung", false, '{"transition": "fade"}' %}
{% simpleText "Design oder Gestaltung?", design %}

{% simpleText "Programmieren oder Programmierung?", program %}
{% simpleInterlude "Programmieren in der Gestaltung", mission %}



