---
title: Share Data via Window Opener
subtitle: Leader-Follower Paradigm 
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
footer: |
  - [Window: opener property MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
  - [Demo Implementation](https://cnoss.github.io/multi-window-experiences/00-core-concepts/window-opener-demo/parent.html)
code: |
  // In opener/parent window
  /**/
  const childWindowPosition = {
    x: false,
    y: false
  }
  /**/
  // Open child window
  childWindow = window.open(url, 'child-window');
  /**/
  // Read window position from child
  if (childWindowPosition.x === childWindow.screenX 
    && childWindowPosition.y === childWindow.screenY) return;
    /**/
  childWindowPosition.x = childWindow.screenX;
  childWindowPosition.y = childWindow.screenY;
code2: |
  // In opened/child window
  /**/
  const parentWindowPosition = {
    x: false,
    y: false
  }
  /**/
  // Read window position from parent
  if (parentWindowPosition.x === window.opener.screenX 
    && parentWindowPosition.y === window.opener.screenY) return;
    /**/
  parentWindowPosition.x = window.opener.screenX;
  parentWindowPosition.y = window.opener.screenY;

vorteile: |
  - direct reference to the parent window
  - easy to call functions or access variables
  - minimal setup, no external messaging needed

nachteile: |
  - only works if the window was opened via window.open()
  - breaks on reloads or navigation
  - no support for cross-tab communication
  - tight coupling between windows
---

{% interlude "Share Data via window.opener","Baseline Widely available" %}

{% screenshotFs "./images/opener.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share Data via [window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)"}' %}

{% codeSmall "Using window.opener", "Baseline Widely available", [{code: code, lang: "javascript"}, {code: code2, lang: "javascript"}], "css", "fade" %}

{% simpleText "Advantages of window.opener 🥳", vorteile, '{"transition":"slide"}'  %}

{% simpleText "Disadvantages 😢", nachteile, '{"transition":"slide"}'  %}

{% screenshotFs "./images/opener.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share Data via [window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)"}' %}