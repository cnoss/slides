---
title: Popover API
layout: presentation.11ty.js
slideClasses: wrap
status: ok
footer: |
  - [Popover API, MDN](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
  - [Introducing the popover API, Chrome for Developers](https://developer.chrome.com/blog/introducing-popover-api)
text1: |
  The Popover API provides developers with a standard, consistent, flexible mechanism for displaying popover content on top of other page content. Popover content can be controlled either declaratively using HTML attributes, or via JavaScript.

text2: |
  Outline of a popover via Popover API using [popover-](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/popover) and popovertarget attribute. [🛝](https://codepen.io/cnoss/pen/PorqvmY?editors=1100)

text3: |
  Adding close-button using the [popovertarget attribute](https://www.w3schools.com/tags/att_popovertarget.asp). [🛝](https://codepen.io/cnoss/pen/PorqvmY?editors=1100)

text4: |
  Adding some CSS via [::backdrop](https://developer.mozilla.org/en-US/docs/Web/CSS/::backdrop), [:popover-open](https://developer.mozilla.org/en-US/docs/Web/CSS/:popover-open) and [@starting-style](https://developer.mozilla.org/en-US/docs/Web/CSS/@starting-style). [🛝](https://codepen.io/cnoss/pen/PorqvmY?editors=1100)

codeExample1: |
  <div id="my-popover" class="settings-popover" popover>
    <p>Ich bin ein Popover</p>
  </div>

  <header>
    <button popovertarget="my-popover">
      <span class="material-symbols-outlined">settings</span>
    </button>
  </header>

codeExample2: |
  <div id="my-popover" class="settings-popover" popover>
    <button class="close-btn" popovertarget="my-popover" popovertargetaction="hide">
      <span class="material-symbols-outlined">close</span>
    </button>
    <p>Ich bin ein Popover</p>
  </div>

  <header>
    <button popovertarget="my-popover">
      <span class="material-symbols-outlined">settings</span>
    </button>
  </header>

codeExample3: |
  &::backdrop {
    background: rgb(0 0 0 / 70%);
  }

  &:popover-open {
    @starting-style {
      opacity: 0;
    }

    opacity: 1;
  }

codeExampleStep4: |
  ::view-transition-old(root) {
    animation-name: move-out;
    animation-duration: 0.4s;
    animation-timing-function: ease-in;
    animation-direction: both;
  }
  /**/
  ::view-transition-new(root) {
    animation: 0.4s ease-in both move-in;
  }
---

{% interlude "Popover API", "[Baseline since 2024](https://caniuse.com/?search=View%20Transitions%20API)" %}
{% simpleText "Popover API", text1 %}
{% codeSmall "Popover API", text2, codeExample1, "html", "fade" %}
{% codeSmall "Popover API", text3, codeExample2, "html", "fade" %}
{% codeSmall "Popover API", text4, codeExample3, "css", "fade" %}
{% simpleText "🍻", "" %}


