---
title: Bertin und CSS
layout: presentation.11ty.js
slideClasses: wrap
status: ok
---

<section class="image screenshot" data-transition="fade" data-background-color="#666">
  <figure>
    <svg viewBox="0 0 1400 300" width="1400" height="300" style="max-width:100%; height:auto;">
      <defs>
        <pattern id="bertin-stripes" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="4" height="8" fill="#231f20"/></pattern>
        <pattern id="bertin-dots" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="1.8" fill="#231f20"/></pattern>
      </defs>
      <g font-family="sans-serif" font-size="30" fill="#fff" text-anchor="middle">
        <text x="90" y="270">Position</text>
        <text x="290" y="270">Größe</text>
        <text x="490" y="270">Form</text>
        <text x="690" y="270">Helligkeit</text>
        <text x="890" y="270">Farbe</text>
        <text x="1090" y="270">Richtung</text>
        <text x="1290" y="270">Textur</text>
      </g>
      <g fill="#fff">
        <rect x="0" y="40" width="180" height="180"/><rect x="200" y="40" width="180" height="180"/><rect x="400" y="40" width="180" height="180"/><rect x="600" y="40" width="180" height="180"/><rect x="800" y="40" width="180" height="180"/><rect x="1000" y="40" width="180" height="180"/><rect x="1200" y="40" width="180" height="180"/>
      </g>
      <g fill="#231f20">
        <circle cx="40" cy="75" r="14"/><circle cx="95" cy="140" r="14"/><circle cx="145" cy="190" r="14"/>
        <circle cx="235" cy="130" r="8"/><circle cx="280" cy="130" r="16"/><circle cx="342" cy="130" r="28"/>
        <circle cx="440" cy="130" r="20"/><rect x="472" y="110" width="40" height="40"/><polygon points="550,110 572,150 528,150"/>
        <circle cx="640" cy="130" r="20" fill="#231f20"/><circle cx="690" cy="130" r="20" fill="#888"/><circle cx="740" cy="130" r="20" fill="#d4d4d4"/>
        <circle cx="840" cy="130" r="20" fill="#4952e1"/><circle cx="890" cy="130" r="20" fill="#dd1166"/><circle cx="940" cy="130" r="20" fill="#00ad2f"/>
        <rect x="1028" y="124" width="36" height="12" rx="6"/><rect x="1072" y="124" width="36" height="12" rx="6" transform="rotate(45 1090 130)"/><rect x="1116" y="124" width="36" height="12" rx="6" transform="rotate(90 1134 130)"/>
        <circle cx="1240" cy="130" r="20"/><circle cx="1290" cy="130" r="20" fill="url(#bertin-stripes)" stroke="#231f20" stroke-width="2"/><circle cx="1340" cy="130" r="20" fill="url(#bertin-dots)" stroke="#231f20" stroke-width="2"/>
      </g>
    </svg>
    <figcaption class="bu is-dark"><p>Visuelle Variablen nach Jacques Bertin (1967)</p></figcaption>
  </figure>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>Kennen Sie schon: aus CSS</h1>
    <table style="font-size:0.8em; width:100%;">
      <tr><td><strong>Position</strong></td><td><code>grid-area</code>, <code>margin</code>, <code>inset</code></td></tr>
      <tr><td><strong>Größe</strong></td><td><code>width</code>, <code>height</code>, <code>font-size</code></td></tr>
      <tr><td><strong>Form</strong></td><td><code>border-radius</code>, <code>clip-path</code></td></tr>
      <tr><td><strong>Helligkeit</strong></td><td><code>oklch(L …)</code>, <code>opacity</code></td></tr>
      <tr><td><strong>Farbe</strong></td><td><code>color</code>, <code>background-color</code></td></tr>
      <tr><td><strong>Richtung</strong></td><td><code>transform: rotate()</code>, <code>writing-mode</code></td></tr>
      <tr><td><strong>Textur</strong></td><td><code>background-image</code>, <code>mask</code>, <code>filter</code></td></tr>
    </table>
  </div>
</section>
