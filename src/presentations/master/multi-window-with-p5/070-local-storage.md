---
title: Store shared data via LocalStorage
subtitle: Storage Event Triggering Paradigm
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
footer: |
  - [Local Storage MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
  - [Demo Implementation](https://cnoss.github.io/multi-window-experiences/00-core-concepts/local-storage-demo/index.html)
store: |
  // Write changes to local storage
  const trackMyWindowPosition = () => {
    /**/
    if (myWindowPosition.x === window.screenX 
      && myWindowPosition.y === window.screenY) return;
    /**/
    myWindowPosition.x = window.screenX;
    myWindowPosition.y = window.screenY;
    /**/
    // Store Window Data in Local Storage
    localStorage.setItem('windowPosition', JSON.stringify(myWindowPosition));
  }
listen: |
  // Listen to changes in local storage
  window.addEventListener('storage', (event) => {
    /**/
    if(!event.key === 'windowPosition') return;
    const otherWindowPosition = JSON.parse(event.newValue);
    /**/
    // Do something meaningful with the data 🕺🏼
    console.log(otherWindowPosition.x, otherWindowPosition.y);
  });

vorteile: |
  - simple key–value storage, persistent across reloads
  - built-in storage event allows reactive cross-tab communication
  - no direct window references needed
  - easy to implement and debug

nachteile: |
  - string-only storage (no complex data types without serialization)
  - storage events don’t fire in the same window 🧐
  - not designed for high-frequency updates or large data volumes
---

{% interlude "Store shared data via LocalStorage","Storage Event Triggering Paradigm" %}

{% screenshotFs "./images/local-storage.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Store shared data via [Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)"}' %}


{% codeSmall "Store shared data via LocalStorage", "LocalStorage allows browser windows of the same origin to persistently store and share string-based key–value pairs. The storage event lets other open windows react to changes in real time, making it useful for simple cross-window communication.", [{code: store, lang: "javascript"}, {code: listen, lang: "javascript"}], "css", "fade" %}

{% simpleText "Advantages 🥳", vorteile, '{"transition":"slide"}'  %}

{% simpleText "Disadvantages 😢", nachteile, '{"transition":"slide"}'  %}

{% screenshotFs "./images/local-storage.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Store shared data via [Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)"}' %}
