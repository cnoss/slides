---
title: Prüfung Grundlagen des Web
layout: documents.11ty.js
---

{% set blockCount = 1 %}
{% for name, item in gdwFragen %}
  <h2>{{ name }}<span class="count">{{blockCount}}</span></h2>
  <ol>
  {% set questionCount = 1 %}
  {% for item in gdwFragen[name] %}
  <li><a class="is-black" href="/gdw-frage?block={{blockCount}}&question={{questionCount}}">{{ item }}</a></li>
  {% set questionCount = questionCount + 1 %}
  {% endfor %}
  </ol>
    {% set blockCount = blockCount + 1 %}
{% endfor %}
