---
title: Tools zum Testen
layout: presentation.11ty.js
slideClasses: wrap

textAutomatischeTests: |
  - **WAVE** Web Accessibility Evaluator
  - **Lighthouse** (in Chrome DevTools integriert)

textManualTests: |
  - **Maus weglegen** - nur Tastatur verwenden
  - **Zoom auf 200%** - ist alles lesbar?
  - **Bilder deaktivieren** - fehlen Alt-Texte?
  - sind alle Bereiche mit **Tab** erreichbar?
  - **Fokus** immer sichtbar?
  - **Escape** schließt Dialoge?
  - **Screenreader** nutzen

---


{% simpleText "Manuelle Tests", textManualTests, '{"backgroundTransition":"slide"}' %}
{% simpleText "Tools zum Testen", textAutomatischeTests, '{"backgroundTransition":"slide"}' %}
