---
title: Decks
layout: documents.11ty.js
bodyClass: presentation-list
---

## Screendesign und visuelle Kommunikation

### Rahmen
<ul>
{%- for post in collections.screendesignUndVisuelleKommunikation -%}
  {%- if post.data.typ == "Rahmen" -%}
    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a>{% if post.data.gruppe %} <small>{{ post.data.gruppe }}</small>{% endif %}{% if post.data.tiefe %} <small>({{ post.data.tiefe }})</small>{% endif %}</li>
  {%- endif -%}
{%- endfor -%}
</ul>

### Haltungen
<ul>
{%- for post in collections.screendesignUndVisuelleKommunikation -%}
  {%- if post.data.typ == "Haltung" -%}
    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a>{% if post.data.gruppe %} <small>{{ post.data.gruppe }}</small>{% endif %}{% if post.data.tiefe %} <small>({{ post.data.tiefe }})</small>{% endif %}</li>
  {%- endif -%}
{%- endfor -%}
</ul>

### Phänomene
<ul>
{%- for post in collections.screendesignUndVisuelleKommunikation -%}
  {%- if post.data.typ == "Phänomen" -%}
    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a>{% if post.data.gruppe %} <small>{{ post.data.gruppe }}</small>{% endif %}{% if post.data.tiefe %} <small>({{ post.data.tiefe }})</small>{% endif %}</li>
  {%- endif -%}
{%- endfor -%}
</ul>

### Prinzipien
<ul>
{%- for post in collections.screendesignUndVisuelleKommunikation -%}
  {%- if post.data.typ == "Prinzip" -%}
    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a>{% if post.data.gruppe %} <small>{{ post.data.gruppe }}</small>{% endif %}{% if post.data.tiefe %} <small>({{ post.data.tiefe }})</small>{% endif %}</li>
  {%- endif -%}
{%- endfor -%}
</ul>

### Methoden
<ul>
{%- for post in collections.screendesignUndVisuelleKommunikation -%}
  {%- if post.data.typ == "Methode" -%}
    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a>{% if post.data.gruppe %} <small>{{ post.data.gruppe }}</small>{% endif %}{% if post.data.tiefe %} <small>({{ post.data.tiefe }})</small>{% endif %}</li>
  {%- endif -%}
{%- endfor -%}
</ul>

## Screendesign
<ul>
{%- for post in collections.screendesign -%}
  
    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a></li>
  
{%- endfor -%}
</ul>

## Master
<ul>
{%- for post in collections.master -%}

    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a></li>

{%- endfor -%}
</ul>

## Bachelor
<ul>
{%- for post in collections.bachelor -%}

    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a></li>

{%- endfor -%}
</ul>

## Others
<ul>
{%- for post in collections.misc -%}

    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a></li>

{%- endfor -%}
</ul>