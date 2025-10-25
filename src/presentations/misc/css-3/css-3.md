---
title: CSS Grids, Custom Properties und ein bisschen Kleinkram
revealOptions:
  transition: 'slide'
  backgroundTransition: 'fade'
  center: false
---

slide-is:welcome
# CSS Grids, Custom Properties
und ein bisschen Kleinkram

___

slide-is:interlude
## What CSS can do for you?
SPOT for Style & Layout 

---

slide-is:conclusion
## Weaknesses of CSS
- schwer zu lesen und zu verstehen
- bei großen Projekten sehr unübersichtlich
- kennt keine Variabeln
- kennt keine Funktionen

___

slide-is:interlude
## Dealing with Preprocessors
[Sass](https://sass-lang.com/guide), [Less](http://lesscss.org/#), [Stylus](http://stylus-lang.com/), …

---

slide-is:simple
## With preprocessors you can
* use variables
* nest your css
* extend classes
* use functions

[Sass](https://sass-lang.com/guide), [Less](http://lesscss.org/#), [Stylus](http://stylus-lang.com/)


---

slide-is:simple
## Disadvantages of Preprocessors
* Debugging is harder
* Compilation slows down development
* Performance
* Maintainance & Overengineering
* 3rd Party Tool
* …

___

slide-is:interlude
## Dive into CSS Custom Properties
CSS Custom Properties for Cascading Variables Module Level 1
W3C Candidate Recommendation, 03 December 2015

---

slide-is:simple
## Simple Usage of Custom Properties

Define Properties

```
:root{
	--primary: #dd1166;
}
```

Use Properties

```
h1{
	color: var(--primary);
}
```

---

slide-is:simple
## Structured Usage of Custom Properties

```
:root {

    --ff: Roboto, Arial, sans-serif;
    --ff-hdlns: "Roboto Slab", Courier, monospace;

    --fs-bs: 18px;
    --fs-lg: calc(var(--fs-bs) * 2);
    --fs-mdm: calc(var(--fs-bs) * 1.6);

    --fw-bld: 700;
    --fw-rglr: 400;

    --bs-clr: #333;
    --prmry-clr: #dd1166;
    --scndry-clr: rgb(73, 82, 225);

    --cntnt-mx-wdth: 800px;
    --brkpnt-tblt: var(--cntnt-mx-wdth);
}

```

---

slide-is:simple
## Redefining Variables

```

:root {
	--fs-bs: 18px;
}

body {
	font-size: var(--fs-bs);
}

@media screen and (max-width: 800px) {
  :root {
    --fs-bs: 14px;
  }
}


```
---

slide-is:simple
## Custom Properties & Javascript

```
<script>

  // Read Properties
  const ele = document.querySelector("body");
  const customProperties = getComputedStyle(ele);
  const primaryColor = customProperties.getPropertyValue('--prmry-clr');

  // Print Property
  console.log(primaryColor);
  
  //  Write Properties
  ele.style.setProperty('--prmry', "#00ff00");

</script>

```

---

slide-is:simple
## Custom Properties in Production Environment
* Why not? (88%)
* Fallback via [cssnext](http://cssnext.io/)
* http 1.* vs http 2.*

```

h1{
  color: #dd1166;
  color: var(--prmry);
}

```


---

slide-is:image images/can-i-use-custom-properties.png

___

slide-is: interlude
## Grid Layouts in CSS

---

slide-is:image images/grid.jpeg

---

slide-is:image images/flexbox.jpeg

---

slide-is:image images/grid-flexbox.jpeg

---

slide-is:simple
## Simple Usage of CSS Grids

```
.grid{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-column-gap: 20px;
  grid-row-gap: 20px;
}

```
fr = fraction of the free space


---

slide-is:simple
## Advanced Usage

```
.grid{
  display: grid;
  grid-template-columns: 2fr repeat(2, 1fr);
  grid-auto-rows: minmax(200px, 300px);
  grid-template-rows: repeat(4,1fr);
}
```

---

slide-is:simple
## Using Lines

```
.site-header{
    grid-column: 1/5;
    grid-row: 1/2;
}

.content.right{
    grid-column: 1/3;
    grid-row: 2/3;
}

```
Container können an Rasterlinien ausgerichtet werden.

---

slide-is:simple
## Using Named Lines

```
.grid{
    display: grid;
    grid-template-columns: [left] 1fr [half-left] 1fr [middle] 1fr [half-right] 1fr [right];
    grid-template-rows: [top] 1fr [half-top] 1fr [middle] 1fr [half-bottom] 1fr [bottom];
}

.site-header{
    grid-column: left/right;
    grid-row: top/half-top;
}

```
Rasterlinien können benannt werden.

---

slide-is:simple
## Using Areas

```
.grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(4, 1fr);
    grid-template-areas: 
        "header header header header" 
        "teaser-left teaser-left teaser-right teaser-right" 
        "content content content content" 
        "footer footer footer footer";
}
.site-header {
    grid-area: header;
    border-bottom: solid 1px var(--bs-clr);
}

```
Bereiche können benannt werden.

---

slide-is:simple
## CSS Grids in in Production Environment
* Why not? (85%) Browser Support
* Fallback via @supports

```

 @supports not (display: grid) {
    .grid{
        max-width: 960px;
        margin: auto 0;
    }
}

```


---

slide-is:image images/can-i-use-css-grid.png


---

slide-is: assignment
## icon:edit Jetzt aber ran
[Dive.is](https://dive.is) in 2018er Code, sprich: mit Custom Properties und CSS Grid. 
* Material unter [assignment.zip](http://www.christiannoss.de/talks/2018-css3/assignments.zip)
* Codebeispiele unter [examples.zip](http://www.christiannoss.de/talks/2018-css3/examples.zip)
* Links unter [links.zip](http://www.christiannoss.de/talks/2018-css3/links.zip)

___

slide-is: interlude
## Expressive CSS
by John Polacek

---

slide-is:interlude
## CSS Challenges in Real Life
The Loop

---

slide-is:simple
## Mit der Zeit werden Stylesheets:
- größer
- stärker segmentiert
- spezifischer
- redundante Lösungen für das selbe Problem

---

slide-is:simple
## Performance & Maintanance

![](https://www.igvita.com/posts/12/doc-render.png)



---

slide-is:interlude
## Multiple Approaches for Sustainable CSS
OOCSS, SMACSS, Atomic CSS, MCSS, AMCSS, […](https://css-tricks.com/methods-organize-css/)


---

slide-is:simple
## The Expressive CSS Approach in a Nutshell
* Classes Are For Visual Styling
* Build on a Good Foundation
* Stay DRY With Utility Classes
* mehr bei [http://johnpolacek.github.io/expressive-css/](http://johnpolacek.github.io/expressive-css/)

___

slide-is:outro
## Danke für's Mitmachen

icon:twitter [twitter.com/cnoss](http://twitter.com/cnoss)  
icon:facebook [www.facebook.com/cnoss](https://www.facebook.com/cnoss)