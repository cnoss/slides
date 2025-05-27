---
title: Final Thoughts
layout: presentation.11ty.js
slideClasses: images
transition: slide
status: ok

finalThoughts1: |
  There are *many technical ways* to exchange data between browser windows — from direct messaging with postMessage to reactive broadcasting with BroadcastChannel, or even shared background logic via SharedWorker. 
  
  Most approaches ultimately rely on sending messages back and forth, but *the real challenge* lies in crafting a *meaningful design concept* around that connection.

finalThoughts3: |
  In the end, your architecture is just the foundation.
  *What you build on top is what matters most.*

finalThoughts4: |
  By the way, designer and coder *Björn Staal* works with the *localStorage-based approach* — showing that even the simplest mechanisms can lead to compelling, interactive experiences if paired with a strong idea.
---


{% simpleText "Final Thoughts", finalThoughts1, '{"transition":"slide"}'  %}
{% simpleText "", finalThoughts3, '{"transition":"slide"}'  %}
{% simpleText "", finalThoughts4, '{"transition":"slide"}'  %}
{% simpleText "Physics??? 🧐", "", '{"transition":"slide"}'  %}




