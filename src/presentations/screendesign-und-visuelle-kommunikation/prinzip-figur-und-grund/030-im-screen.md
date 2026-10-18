---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Im Interface ist Figur und Grund ein Werkzeug für Fokus. Ein Dialog wird zur Figur, indem alles andere zum Grund gemacht wird: eine dunkle, halbtransparente Fläche (englisch Scrim) legt sich über die Seite. Ohne Scrim konkurrieren Dialog und Seite.

  Das Beispiel von BEGA (2026) macht genau das: Die Seite tritt dunkel zurück, der weiße Dialog ist eindeutig Figur. Nebenbei ein faires Cookie-Banner: Beide Wege sind Buttons.

  Weitere Formen: Bottom Sheets, Karten mit Schatten auf grauem Grund (Elevation), Fokus-Rahmen, ausgewählte Listeneinträge. Frage ans Publikum danach.
---

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Eine Seite"}' %}
<rect data-id="pg" x="90" y="40" width="420" height="520" rx="0" fill="#ffffff" />
<rect data-id="n" x="110" y="60" width="380" height="30" rx="0" fill="#d9d9d9" />
<rect data-id="h" x="110" y="120" width="260" height="24" rx="0" fill="#888888" />
<rect data-id="i" x="110" y="165" width="380" height="150" rx="0" fill="#d9d9d9" />
<rect data-id="t0" x="110" y="340" width="360" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t1" x="110" y="364" width="330" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t2" x="110" y="388" width="300" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t3" x="110" y="412" width="270" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="btn" x="110" y="460" width="140" height="40" rx="20" fill="#888888" />
<rect data-id="scrim" x="90" y="40" width="420" height="0" rx="0" fill="#231f20" />
<rect data-id="m" x="300" y="300" width="0" height="0" rx="8" fill="#ffffff" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Ein Dialog ohne Abdunklung: Figur und Grund konkurrieren"}' %}
<rect data-id="pg" x="90" y="40" width="420" height="520" rx="0" fill="#ffffff" />
<rect data-id="n" x="110" y="60" width="380" height="30" rx="0" fill="#d9d9d9" />
<rect data-id="h" x="110" y="120" width="260" height="24" rx="0" fill="#888888" />
<rect data-id="i" x="110" y="165" width="380" height="150" rx="0" fill="#d9d9d9" />
<rect data-id="t0" x="110" y="340" width="360" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t1" x="110" y="364" width="330" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t2" x="110" y="388" width="300" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t3" x="110" y="412" width="270" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="btn" x="110" y="460" width="140" height="40" rx="20" fill="#888888" />
<rect data-id="scrim" x="90" y="40" width="420" height="0" rx="0" fill="#231f20" />
<rect data-id="m" x="140" y="200" width="320" height="200" rx="8" fill="#ffffff" />
<rect data-id="mh" x="165" y="225" width="200" height="18" rx="0" fill="#231f20" />
<rect data-id="mt" x="165" y="260" width="260" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="mt2" x="165" y="282" width="220" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="mb" x="165" y="330" width="130" height="40" rx="20" fill="#9313ce" />
<rect data-id="mb2" x="310" y="330" width="120" height="40" rx="20" fill="#ffffff" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Mit Abdunklung: Der Dialog ist Figur, die Seite wird Grund"}' %}
<rect data-id="pg" x="90" y="40" width="420" height="520" rx="0" fill="#ffffff" />
<rect data-id="n" x="110" y="60" width="380" height="30" rx="0" fill="#d9d9d9" />
<rect data-id="h" x="110" y="120" width="260" height="24" rx="0" fill="#888888" />
<rect data-id="i" x="110" y="165" width="380" height="150" rx="0" fill="#d9d9d9" />
<rect data-id="t0" x="110" y="340" width="360" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t1" x="110" y="364" width="330" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t2" x="110" y="388" width="300" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t3" x="110" y="412" width="270" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="btn" x="110" y="460" width="140" height="40" rx="20" fill="#888888" />
<rect data-id="scrim" x="90" y="40" width="420" height="520" rx="0" fill="#231f20" opacity="0.55" />
<rect data-id="m" x="140" y="200" width="320" height="200" rx="8" fill="#ffffff" />
<rect data-id="mh" x="165" y="225" width="200" height="18" rx="0" fill="#231f20" />
<rect data-id="mt" x="165" y="260" width="260" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="mt2" x="165" y="282" width="220" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="mb" x="165" y="330" width="130" height="40" rx="20" fill="#9313ce" />
<rect data-id="mb2" x="310" y="330" width="120" height="40" rx="20" fill="#ffffff" />
{% endframe %}
{% screenshot "./images/screen-dialog.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Abgedunkelte Seite, weißer Dialog: eindeutig, was Figur ist<br><small>bega.com, Screenshot 2026</small>"}' %}

{% question "Wo macht Ihr Handy etwas zur Figur?", "Dialoge, Bottom Sheets, Benachrichtigungen, ausgewählte Einträge. Zu zweit, zwei Minuten." %}
