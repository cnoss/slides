---
title: Auf dem Screen
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Ein Dialog, wie er in echten Anwendungen vorkommt: Die gefährliche Aktion ist grün, das harmlose Abbrechen rot. Frage: Welchen Button klicken Sie, um die Datei zu löschen? Viele zögern oder greifen zum grünen. Grün heißt bei uns »weiter, alles gut«, Rot heißt »Achtung, stopp«. Farbe und Beschriftung widersprechen sich, genau wie beim Farbenlesen.

  Im Alltag: Fehlermeldungen in Grün, Erfolgsmeldungen in Rot, Statusfarben, die zwischen zwei Ansichten wechseln. Und Flimmern: roter Text auf blauem Button, Links in kräftigem Blau auf Rot.

  Hinweis: Rot und Grün sind kulturell geprägt. In chinesischen Börsenkursen steht Rot für steigende Kurse.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Datei endgültig löschen?</h1>
    <p>Diese Aktion kann nicht rückgängig gemacht werden.</p>
    <p style="margin-top:4vh;">
      <span style="display:inline-block; padding:2vh 4vw; border-radius:5vh; font-size:3.4vh; background:#d81e2c; color:#fff; margin-right:2vw;">Abbrechen</span>
      <span style="display:inline-block; padding:2vh 4vw; border-radius:5vh; font-size:3.4vh; background:#14a33c; color:#fff;">Löschen</span>
    </p>
  </div>
</section>

{% question "Welchen Button klicken Sie, um zu löschen?", "Und wie lange haben Sie gezögert?" %}
