---
title: Slides
layout: documents.11ty.js
---

## Screendesign
<ul>
{%- for post in collections.screendesign -%}
  
    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a></li>
  
{%- endfor -%}
</ul>


## Others
<ul>
{%- for post in collections.misc -%}

    <li><a href="{{ post.url | url }}">{{ post.data.title }}</a></li>

{%- endfor -%}
</ul>