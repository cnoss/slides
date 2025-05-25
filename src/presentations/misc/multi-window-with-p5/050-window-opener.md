---
title: Share Data via Window Opener
subtitle: Leader-Follower Paradigm 
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
footer: |
  - [Window: opener property MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
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
---

{% interlude "Share Data via window.opener","Baseline Widely available" %}
{% screenshotFs "./images/opener.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share Data via [window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)"}' %}
{% codeSmall "Using window.opener", "Baseline Widely available", [{code: code, lang: "javascript"}, {code: code2, lang: "javascript"}], "css", "fade" %}
{% screenshotFs "./images/opener.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Share Data via [window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)"}' %}
