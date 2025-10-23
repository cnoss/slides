---
title: Decks
layout: documents.11ty.js
bodyClass: presentation-list
---

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