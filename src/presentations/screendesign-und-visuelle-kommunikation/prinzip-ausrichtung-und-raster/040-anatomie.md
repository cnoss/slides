---
title: "Anatomie eines Rasters"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Vier Begriffe, die man braucht, um über Raster zu sprechen, in Figma genauso wie in CSS.

  - **Spalte (Column):** die Fläche, auf der Inhalte stehen. Ein Element belegt eine oder mehrere Spalten.
  - **Rinne (Gutter):** der Abstand zwischen zwei Spalten. In CSS heißt sie gap.
  - **Rand (Margin):** der Abstand zwischen Raster und Formatkante.
  - **Modul (Module, Rasterzelle):** Teilt man die Spalten zusätzlich in Zeilen (Rows), entstehen Module. Ein Raster aus Spalten und Zeilen heißt Modulraster.

  Begriffe: Spalte (Column), Rinne (Gutter), Rand (Margin), Modul (Module), Modulraster (Modular Grid). Figma und viele Werkzeuge verwenden die englischen Begriffe, deshalb brauchen Sie beide.
---

{% frame '{"bu":"Spalte (Column)"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.9" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="rinne" x="290" y="40" width="20" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="rand" x="0" y="0" width="40" height="600" fill="#9313ce" fill-opacity="0" />
  <rect data-id="row1" x="40" y="128" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row2" x="40" y="236" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row3" x="40" y="344" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row4" x="40" y="452" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="modul" x="220" y="148" width="70" height="88" fill="#9313ce" fill-opacity="0" />
{% endframe %}
{% frame '{"bu":"Rinne (Gutter)"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="rinne" x="290" y="40" width="20" height="520" fill="#9313ce" fill-opacity="0.9" />
  <rect data-id="rand" x="0" y="0" width="40" height="600" fill="#9313ce" fill-opacity="0" />
  <rect data-id="row1" x="40" y="128" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row2" x="40" y="236" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row3" x="40" y="344" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row4" x="40" y="452" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="modul" x="220" y="148" width="70" height="88" fill="#9313ce" fill-opacity="0" />
{% endframe %}
{% frame '{"bu":"Rand (Margin)"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="rinne" x="290" y="40" width="20" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="rand" x="0" y="0" width="40" height="600" fill="#9313ce" fill-opacity="0.9" />
  <rect data-id="row1" x="40" y="128" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row2" x="40" y="236" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row3" x="40" y="344" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="row4" x="40" y="452" width="520" height="20" fill="#ffffff" fill-opacity="0" />
  <rect data-id="modul" x="220" y="148" width="70" height="88" fill="#9313ce" fill-opacity="0" />
{% endframe %}
{% frame '{"bu":"Modul (Module): Spalten (Columns) und Zeilen (Rows) ergeben Rasterzellen"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#d9d9d9" fill-opacity="0.6" />
  <rect data-id="rinne" x="290" y="40" width="20" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="rand" x="0" y="0" width="40" height="600" fill="#9313ce" fill-opacity="0" />
  <rect data-id="row1" x="40" y="128" width="520" height="20" fill="#ffffff" fill-opacity="1" />
  <rect data-id="row2" x="40" y="236" width="520" height="20" fill="#ffffff" fill-opacity="1" />
  <rect data-id="row3" x="40" y="344" width="520" height="20" fill="#ffffff" fill-opacity="1" />
  <rect data-id="row4" x="40" y="452" width="520" height="20" fill="#ffffff" fill-opacity="1" />
  <rect data-id="modul" x="220" y="148" width="70" height="88" fill="#9313ce" fill-opacity="0.9" />
{% endframe %}
