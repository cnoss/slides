---
title: Shared Data
layout: presentation.11ty.js
slideClasses: images
transition: slide
status: ok
---

{% question "Woher kommen die *Daten*<br>und wie können wir sie *austauschen*?" %}

{% screenshotFs "./images/get-position.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Position on screen via [window.screenX](https://developer.mozilla.org/de/docs/Web/API/Window/screenX) & [window.screenY](https://developer.mozilla.org/de/docs/Web/API/Window/screenY)"}' %}

{% screenshotFs "./images/opener.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share Data via [window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)"}' %}

{% screenshotFs "./images/broadcast-channel.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share via [Broadcast Channel API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API)"}' %}

{% screenshotFs "./images/local-storage.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Store shared data via [Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)"}' %}

{% screenshotFs "./images/shared-worker.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Use of a higher-level [Shared Worker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker)"}' %}

{% screenshotFs "./images/web-socket.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Using an external component: [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)"}' %}


