---
title: Objektivierung
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: slide

ziele1: |
  
  Aus der **Aufgaben- oder Problemstellung**. Was war der ursprüngliche Auftrag, welches Problem sollte gelöst werden. Das ist die naheliegendste Quelle und wird trotzdem oft übergangen.

  Aus den **Nutzern und ihren Bedürfnissen**. Wer benutzt das System, in welcher Situation, mit welchem Vorwissen, unter welchen Bedingungen. Hieraus lassen sich die meisten funktionalen und gestalterischen Ziele ableiten.

  Aus dem **Auftraggeber oder den Stakeholdern**. Geschäftsziele, Vorgaben, Rahmenbedingungen, auch das, was nicht offen ausgesprochen, aber erwartet wird.


ziele2: |

  Aus **Konventionen und Standards**. Plattform-Richtlinien, etablierte Muster, Barrierefreiheitsnormen. Hier kommt das Ziel aus einer geteilten Erwartung, die der Nutzer mitbringt.

  Aus **fachlichen oder technischen Anforderungen**. Datenschutz, Sicherheit, Performance, Wartbarkeit, rechtliche Vorgaben. Gerade die nichtfunktionalen Anforderungen liefern handfeste, gut verteidigbare Ziele.

  Aus **Recherche und Wettbewerb**. Wie lösen andere ein vergleichbares Problem, was hat sich bewährt, wo gibt es eine Lücke. Wichtig ist dabei, nicht "die machen das auch so" als Ziel zu nehmen, sondern zu verstehen, welches Ziel die anderen damit verfolgen.

ich0: |  
  Wer nur aus der ersten Person und ohne übergeordnetes Ziel argumentiert, stellt lediglich eine Verbindung zwischen sich und dem Ergebnis her. Daraus folgt:

ich1: |
  **Meinung steht gegen Meinung.** "Mir gefällt es" lädt direkt zur Gegenmeinung ein. Der Nächste findet etwas anderes gut, und es gibt keine Instanz, die entscheidet.
  
ich2: |  
  **Die Entscheidung wird angreifbar.** Ohne Ziel als Maßstab lässt sich nicht zeigen, dass die Lösung richtig ist, sondern nur, dass sie gefällt. Das hält keiner kritischen Nachfrage stand.
  
ich3: |  
  **Niemand außer dir ist eingebunden.** Die Begründung verbindet nur dich mit deinem Ergebnis. Publikum, Nutzer und Auftraggeber kommen darin nicht vor, also fühlt sich auch niemand abgeholt.

ich4: |
  **Die Arbeit wirkt beliebig.** Was aus einer Laune entstanden sein könnte, wirkt auch so. Ohne erkennbares Ziel sieht selbst eine durchdachte Lösung nach Zufall aus.

ich5: |
  **Du verlierst die Autorität.** Wer über Geschmack oder Gefühl argumentiert, gibt die eigene Entscheidung dem Geschmack oder Gefühl der anderen preis. Wer über Ziele argumentiert, behält die Deutungshoheit.

ich6: |
  **Kein Lerneffekt, keine Übertragbarkeit.** Eine ziellose Entscheidung lässt sich nicht auf das nächste Projekt übertragen, weil niemand sagen kann, warum sie funktioniert hat.
---


{% interlude "Objektivierung", "Vom Gefühl zum Argument", '{"transition":"slide"}'  %}

{% cite "Den Button haben wir nach oben rechts gepackt, das fühlte sich für uns am natürlichsten an." %}
{% cite "Wir haben uns für React entschieden, weil Melissa das auch auf der Arbeit benutzt." %}
{% cite "Die Daten speichern wir im Local Storage, das ist am einfachsten." %}
{% cite "Wir wollten es modern haben … " %}

{% screenshot "images/subjekt-objekt.jpeg", '{"transition":"fade", "classes":"no-shadow", "bu":"«Mir gefällt es» verbindet nur dich mit deiner Lösung, sonst niemanden.", "badge":""}' %}

{% simpleText "Die Gefahr der reinen Ich-Perspektive ", ich, '{"transition":"slide"}' %}

<section class="mi-slide fact-list">

  <h1 class="title">Die Gefahr der reinen Ich-Perspektive</h1>
    {% fragment ich0 %}
  {% fragment ich1 %}
  {% fragment ich2 %}
  {% fragment ich3 %}
  {% fragment ich4 %}
  {% fragment ich5 %}
  {% fragment ich6 %}
  {% fragment ich7 %}

  
</section>

{% screenshot "images/subjekt-ziel-objekt.jpeg", '{"transition":"fade", "classes":"no-shadow", "bu":"Über Ziele argumentieren: nachvollziehbar statt angreifbar.", "badge":""}' %}

{% simpleText "Entwicklen und fomulieren sie Ziele", "", '{"transition":"slide"}'  %}
{% question "Wo können Ziele herkommen? ", "", '{"classes":""}' %}
{% simpleText "Mögliche Quellen der Ableitung", ziele1, '{"transition":"slide"}' %}
{% simpleText "Mögliche Quellen der Ableitung", ziele2, '{"transition":"slide"}' %}

{% qa "Uns gefiel die zweite Variante besser.", "Die zweite Variante erreicht das Ziel der schnellen Orientierung besser, weil die wichtigste Aktion sofort ins Auge fällt.", '{"transition":"slide"}' %}

{% qa "Wir fand die Farben schöner", "Der Kontrast wurde erhöht, weil das Ziel war, die Lesbarkeit auch bei schlechten Lichtverhältnissen zu sichern.", '{"transition":"slide"}' %}

{% qa "Die Daten speichern wir im Local Storage. Das ist am einfachsten.", "Das Ziel war ein lauffähiger Prototyp ohne Server-Abhängigkeit, deshalb fiel die Wahl auf Local Storage als clientseitige Persistenz." %}

{% simpleText "Wie zahlt der Entwurf/ die Lösung auf das Gestaltungsziel ein?", "Gestaltgesetze, Farbigkeit, Räumlichkeit, Anordnung, Interaktion statt *gefällt/ gefiel mir* oder *ich finde/ fand*", '{"transition":"slide"}'  %}

{% simpleText "Argumentieren Sie jenseits der ersten Person, sondern anhand von objektiven/ objektivierbaren Argumenten bezogen auf das Ziel.", "Geben Sie Dritten die Chance, Ihre Argumente zu nutzen.", '{"transition":"slide"}'  %}



