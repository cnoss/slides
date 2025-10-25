---
title: View Transitions
layout: presentation.11ty.js
slideClasses: wrap
status: ok
footer: |
  - [View Transitions API, MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API)
  - [Explainer Document, WICG](https://github.com/WICG/view-transitions/blob/main/explainer.md)
text1: |
  The View Transitions API provides a mechanism for easily creating animated transitions between different website views. This includes animating between DOM states in a single-page app (SPA), and <span class="fragment">**animating the navigation between documents in a multi-page app (MPA)**.</span><span class="fragment">🕺🏼🙌🏽</span>

  <span class="fragment">View transitions are a popular design choice for reducing users' cognitive load, helping them stay in context, and reducing perceived loading latency as they move between states or views of an application.</span>

codeExample1: |
  <meta name="view-transition" content="same-origin" />

codeExampleStep2: |
  @view-transition {
    navigation: auto; // [auto | none]
  }

codeExampleStep3: |
  @keyframes move-out {
    from {
      transform: translateY(0%);
    }
    to {
      transform: translateY(-100%);
    }
  }
  /**/
  @keyframes move-in {
    from {
      transform: translateY(100%);
    }
    to {
      transform: translateY(0%);
    }
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

{% interlude "View Transitions API", "[Experimental Feature](https://caniuse.com/?search=View%20Transitions%20API)" %}
{% simpleText "View Transitions", text1 %}
{% codeSmall "View Transitions", "<del>Step 1: Policy in allen HTML Dokumenten hinzufügen.</del> Deprecated 😱", codeExample1, "html", "fade" %}
{% codeSmall "View Transitions", "Adding css-at-Rule. For a cross-document view transition to work, the current and destination documents of the navigation also need to be on the same origin [⎘](https://developer.mozilla.org/en-US/docs/Web/CSS/@view-transition)", codeExampleStep2, "css", "fade" %}
{% codeSmall "View Transitions", "Adding custom animation [⎘](https://developer.mozilla.org/en-US/docs/Web/CSS/@view-transition)", codeExampleStep3, "css", "fade" %}
{% codeSmall "View Transitions", "Apply the custom animation to the old and new page states [⎘](https://developer.mozilla.org/en-US/docs/Web/CSS/::view-transition-old)", codeExampleStep4, "css", "fade" %}
{% simpleText "🥳", "" %}


