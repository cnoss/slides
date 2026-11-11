---
title: "Stresstest"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **Live (ca. 2 Minuten).** Ein Card-Grid, wie es in jedem Entwurf steht: drei Karten, Platzhaltertext, schöne Bilder, feste Höhe. Sieht fertig aus.

  Dann kommen nacheinander echte Inhalte. Bei jeder Folie fragen: Hält die Karte das aus?

  1. **Echte Titel:** Einer ist sehr lang. Er läuft über die Karte hinaus, die Karten werden ungleich.
  2. **Ein Bild fehlt, die Kategorie ist zweizeilig:** Die Karte sieht plötzlich kaputt aus, obwohl inhaltlich alles stimmt.
  3. **Übersetzung:** Deutsche Texte sind oft deutlich länger als englische. »Events« wird zu »Veranstaltungen«, »Read more« zu »Weiterlesen«.

  Pointe: Kaputt ist nicht der Inhalt. Kaputt ist ein Entwurf, der nur für Lorem ipsum gemacht wurde.

  Die Inhalte sind ausgedacht, angelehnt an Meldungen einer Hochschul-Website.
---

{% interlude "Hält Ihre Card das aus?", "Ein Stresstest mit echten Inhalten" %}

<section class="simple" data-transition="none">
  <div>
    <h1>Mit Platzhaltertext</h1>
    <div style="display:flex;gap:2vw;align-items:flex-start;justify-content:flex-start;width:100%;"><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Lorem</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Lorem ipsum dolor sit amet</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Lorem</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Lorem ipsum dolor sit amet</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Lorem</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Lorem ipsum dolor sit amet</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div></div><p style="margin-top:3vh;font-size:2.2vh;">Sieht fertig aus.</p>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Mit echten Titeln</h1>
    <div style="display:flex;gap:2vw;align-items:flex-start;justify-content:flex-start;width:100%;"><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Studium</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Projektwoche startet</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Vom 18. bis 22. November ruhen die Vorlesungen.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Forschung</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Studierende entwickeln mit der Stadt eine barrierefreie Navigations-App für den Campus Gummersbach und alle angrenzenden Haltestellen</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Das Projekt läuft zwei Semester.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Studium</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Neue Leitlinien für KI im Studium</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Was erlaubt ist und was nicht.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Ein Bild fehlt, die Kategorie ist länger</h1>
    <div style="display:flex;gap:2vw;align-items:flex-start;justify-content:flex-start;width:100%;"><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Studium</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Projektwoche startet</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Vom 18. bis 22. November ruhen die Vorlesungen.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Forschung und Transfer, Institut für Informatik</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Medieninformatik gewinnt Förderpreis</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Ausgezeichnet wurde ein Projekt zu Gestensteuerung.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Studium</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Neue Leitlinien für KI im Studium</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Was erlaubt ist und was nicht.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Mehr lesen ›</p></div></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Dieselbe Karte, zwei Sprachen</h1>
    <div style="display:flex;gap:2vw;align-items:flex-start;justify-content:flex-start;width:100%;"><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Events</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Game Jam winners</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Three teams, 48 hours, one theme.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Read more ›</p></div><div style="width:22vw;height:44vh;background:#e4e4e4;padding:1.6vh 1.6vh 4vh;box-sizing:border-box;text-align:left;hyphens:none;"><div style="background:#c4c4c4;aspect-ratio:16/9;width:100%;margin:0 0 1.4vh;"></div><p style="font-size:1.6vh;letter-spacing:.08em;text-transform:uppercase;color:#5a5a5a;margin:0 0 .8vh;line-height:1.3;">Veranstaltungen</p><p style="font-size:2.6vh;font-weight:700;line-height:1.2;margin:0 0 1vh;color:#231f20;">Gewinnerinnen und Gewinner des Game Jams stehen fest</p><p style="font-size:1.9vh;line-height:1.4;margin:0 0 1.2vh;color:#4a4a4a;">Drei Teams, 48 Stunden, ein Thema.</p><p style="font-size:1.9vh;font-weight:700;margin:0;color:#9313ce;">Weiterlesen ›</p></div></div>
  </div>
</section>
