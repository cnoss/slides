---
title: Share Data via Broadcast Channel API
subtitle: Publish–Subscribe Messaging
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
footer: |
  - [Broadcast Channel API MDN](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API)
  - [window.postMessage MDN](https://developer.mozilla.org/en-us/docs/Web/API/Window/postMessage)
  - [Demo Implementation](https://cnoss.github.io/multi-window-experiences/00-core-concepts/post-message-demo/index.html)
code: |
  // In (first) window
  /**/
  // Open Broadcast Channel
  const windowPositionChannel = new BroadcastChannel('window-position');
  /**/
  /* some lines of funky code */
  /**/
  // Send my window position to the channel
  windowPositionChannel.postMessage(myWindowPosition);
  /**/
  // Receive messages from the channel
  windowPositionChannel.onmessage = (event) => {
    const otherWindowPosition = event.data;
    /**/
    // Do something meaningful with the data 🕺🏼
    console.log(otherWindowPosition.x, otherWindowPosition.y);
  }
code2: |
  // In (second) window
  /**/
  // Open Broadcast Channel
  const windowPositionChannel = new BroadcastChannel('window-position');
  /**/
  /* some lines of funky code */
  /**/
  // Send my window position to the channel
  windowPositionChannel.postMessage(myWindowPosition);
  /**/
  // Receive messages from the channel
  windowPositionChannel.onmessage = (event) => {
    const otherWindowPosition = event.data;
    /**/
    // Do something meaningful with the data 🕺🏼
    console.log(otherWindowPosition.x, otherWindowPosition.y);
  }
description: |
  The window.postMessage() method safely enables cross-origin communication between Window objects; e.g., between a page and a pop-up that it spawned, or between a page and an iframe embedded within it. The Broadcast Channel API is restricted on same origin communication.

  If a participant (tab, window, worker) sends a message via BroadcastChannel.postMessage(), it is sent to all other participants in the channel - but not to the sender itself. 

  ⚠️ Note that window.postMessage() also works without the Broadcast Channel API.

vorteile: |
  - combines broadcasting and direct messaging
  - works well for decoupled, event-based communication
  - no shared memory needed — everything flows through messages
  - no direct window references needed
  - scalable to multiple tabs and controlled windows

nachteile: |
  - requires same-origin (for BroadcastChannel)
  - no built-in state — messages must be actively passed around
  - no message history — late listeners miss earlier messages
---

{% interlude "Share Data via Broadcast Channel API & window.postMessage","Publish–Subscribe Messaging" %}

{% screenshotFs "./images/broadcast-channel.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share Data via [Broadcast Channel API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API) & [window.postMessage](https://developer.mozilla.org/en-us/docs/Web/API/Window/postMessage)"}' %}

{% codeSmall "Using Broadcast Channel API", "The window.postMessage() method safely enables cross-origin communication between Window objects; e.g., between a page and a pop-up that it spawned, or between a page and an iframe embedded within it.", [{code: code, lang: "javascript"}, {code: code2, lang: "javascript"}], "css", "fade" %}

{% simpleText "Broadcast Channel API & window.postMessage()", description, '{"transition":"slide"}'  %}

{% simpleText "Advantages 🥳", vorteile, '{"transition":"slide"}'  %}

{% simpleText "Disadvantages 😢", nachteile, '{"transition":"slide"}'  %}

{% screenshotFs "./images/broadcast-channel.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share Data via [Broadcast Channel API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API) & [window.postMessage](https://developer.mozilla.org/en-us/docs/Web/API/Window/postMessage)"}' %}
