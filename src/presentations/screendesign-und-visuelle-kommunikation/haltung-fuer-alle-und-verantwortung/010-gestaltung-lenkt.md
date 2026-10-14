---
title: Gestaltung lenkt
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Einstieg in eine Veranstaltung über Wahrnehmung: Wer weiß, wie Wahrnehmung funktioniert, kann Blicke lenken, Entscheidungen erleichtern und Dinge verstecken. Dieses Wissen wirkt in beide Richtungen.

  Medieninformatiker:innen entwerfen und bauen. Wer baut, entscheidet mit, auch wenn der Entwurf von anderen kommt. Methodischer Partner: der Crit mit der Frage »Wem nützt das?«, später im Semester der Verantwortungs-Check.

  **Hintergrund**

  Den Begriff »Dark Patterns« hat der britische UX-Designer Harry Brignull 2010 geprägt. Seine Sammlung heißt heute »Deceptive Patterns« (Buch 2023, deceptive.design). Gemeint sind Gestaltungen, die Menschen zu etwas bringen, das sie eigentlich nicht wollen: falsche Dringlichkeit, versteckte Kosten, erschwertes Kündigen.

  Inzwischen ist das auch Recht: Der Digital Services Act der EU (2022, Art. 25) verbietet Online-Plattformen Gestaltungen, die Nutzende täuschen oder manipulieren. In Deutschland verlangt § 312k BGB seit Juli 2022 einen Kündigungsbutton für online abgeschlossene Verträge.

  Quellen: Brignull, Deceptive Patterns (2023); Yablonski, Laws of UX (Kapitel zur Ethik).

  **Einstieg Fliege (ca. 3 Minuten):** Erst nur das Foto zeigen. Was sehen Sie? Warum ist die da? Die aufgedruckte Fliege im Urinal wurde in den 1990er-Jahren am Flughafen Amsterdam Schiphol eingeführt (Idee von Jos van Bedaf und Aad Kieboom). Wer zielt, trifft besser, die Toiletten bleiben sauberer. Die oft genannte Zahl »80 Prozent weniger Spritzer« ist nicht sauber belegt, gern als »deutlich weniger« formulieren. Richard Thaler und Cass Sunstein machten das Beispiel mit »Nudge« (2008) berühmt.

  **Bestellen gegen Kündigen:** Dasselbe Wissen, gegen die Nutzenden eingesetzt. Bestellen geht mit einem großen Button, Kündigen über fünf Schritte und am Ende einen kleinen grauen Link. Brignull nennt das »Roach Motel«: leicht hinein, schwer heraus.

  Foto: Stefan Bellini, CC0, Wikimedia Commons.
---

{% screenshot "./images/nudge-fliege.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto"}' %}

{% statement "Eine Fliege, die niemand übersieht.", "Wer zielt, trifft besser. Gestaltung lenkt, ohne zu verbieten." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Bestellen: ein Schritt, ein großer Button"}' %}
<rect data-id="s0" x="60" y="140" width="120" height="220" rx="10" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="s0a" x="76" y="164" width="70" height="10" fill="#888888" />
<rect data-id="s0t0" x="76" y="190" width="88" height="8" fill="#d9d9d9" />
<rect data-id="s0t1" x="76" y="210" width="76" height="8" fill="#d9d9d9" />
<rect data-id="s0t2" x="76" y="230" width="64" height="8" fill="#d9d9d9" />
<rect data-id="s0b" x="76" y="300" width="88" height="34" rx="17" fill="#9313ce" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Kündigen: fünf Schritte, am Ende ein kleiner grauer Link"}' %}
<rect data-id="s0" x="60" y="140" width="120" height="220" rx="10" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="s0a" x="76" y="164" width="70" height="10" fill="#888888" />
<rect data-id="s0t0" x="76" y="190" width="88" height="8" fill="#d9d9d9" />
<rect data-id="s0t1" x="76" y="210" width="76" height="8" fill="#d9d9d9" />
<rect data-id="s0t2" x="76" y="230" width="64" height="8" fill="#d9d9d9" />
<rect data-id="s0b" x="76" y="300" width="88" height="34" rx="17" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="s1" x="225" y="140" width="120" height="220" rx="10" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="s1a" x="241" y="164" width="70" height="10" fill="#888888" />
<rect data-id="s1t0" x="241" y="190" width="88" height="8" fill="#d9d9d9" />
<rect data-id="s1t1" x="241" y="210" width="76" height="8" fill="#d9d9d9" />
<rect data-id="s1t2" x="241" y="230" width="64" height="8" fill="#d9d9d9" />
<rect data-id="s1b" x="241" y="300" width="88" height="34" rx="17" fill="#ffffff" stroke="#888888" stroke-width="2" />
<polyline data-id="p1" points="188,250 217,250" fill="none" stroke="#888888" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
<rect data-id="s2" x="390" y="140" width="120" height="220" rx="10" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="s2a" x="406" y="164" width="70" height="10" fill="#888888" />
<rect data-id="s2t0" x="406" y="190" width="88" height="8" fill="#d9d9d9" />
<rect data-id="s2t1" x="406" y="210" width="76" height="8" fill="#d9d9d9" />
<rect data-id="s2t2" x="406" y="230" width="64" height="8" fill="#d9d9d9" />
<rect data-id="s2b" x="406" y="300" width="88" height="34" rx="17" fill="#ffffff" stroke="#888888" stroke-width="2" />
<polyline data-id="p2" points="353,250 382,250" fill="none" stroke="#888888" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
<rect data-id="s3" x="555" y="140" width="120" height="220" rx="10" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="s3a" x="571" y="164" width="70" height="10" fill="#888888" />
<rect data-id="s3t0" x="571" y="190" width="88" height="8" fill="#d9d9d9" />
<rect data-id="s3t1" x="571" y="210" width="76" height="8" fill="#d9d9d9" />
<rect data-id="s3t2" x="571" y="230" width="64" height="8" fill="#d9d9d9" />
<rect data-id="s3b" x="571" y="300" width="88" height="34" rx="17" fill="#ffffff" stroke="#888888" stroke-width="2" />
<polyline data-id="p3" points="518,250 547,250" fill="none" stroke="#888888" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
<rect data-id="s4" x="720" y="140" width="120" height="220" rx="10" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="s4a" x="736" y="164" width="70" height="10" fill="#888888" />
<rect data-id="s4t0" x="736" y="190" width="88" height="8" fill="#d9d9d9" />
<rect data-id="s4t1" x="736" y="210" width="76" height="8" fill="#d9d9d9" />
<rect data-id="s4t2" x="736" y="230" width="64" height="8" fill="#d9d9d9" />
<rect data-id="s4b" x="760" y="336" width="40" height="5" fill="#d9d9d9" />
<polyline data-id="p4" points="683,250 712,250" fill="none" stroke="#888888" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
{% endframe %}

{% interlude "Gestaltung lenkt.", "Also tragen wir Verantwortung." %}

{% statement "Wissen über Wahrnehmung wirkt in beide Richtungen.", "Wer weiß, wohin Menschen schauen, kann ihnen helfen. Oder etwas vor ihnen verstecken." %}

{% question "Wem nützt das?", "Die Frage, die Sie ab heute an jeden Entwurf stellen. Auch an Ihren eigenen." %}

{% statement "Woran merken Sie, dass Sie Verantwortung übernehmen?", "Sie können für jede Hervorhebung sagen, wem sie nützt. Und Sie gestalten den Weg, den Nutzende nicht gehen sollen, genauso sorgfältig wie den, den sie gehen sollen." %}
