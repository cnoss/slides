---
title: p5.js Basics
layout: presentation.11ty.js
slideClasses: wrap
status: ok
footer: |
  - [P5.js](https://p5js.org)
  - [Reference](https://p5js.org/reference/)
  - [Web Editor](https://editor.p5js.org/)

theLoop: |
  function setup() {
    createCanvas(400, 400);
  }
  /**/
  function draw() {
    background(220);
    ellipse(mouseX, mouseY, 50, 50);
  }

theLoopText: |
  The tools uses a simple sketch structure based on two main functions: setup(), which runs once at the beginning, and draw(), which runs continuously like a loop. To get started, you can write your code in the <a href="https://editor.p5js.org">p5.js Web Editor</a>.

colorMode: |
  function setup() {
    createCanvas(400, 400);
    colorMode(HSB, 360, 100, 100, 100);
    fill(90, 100, 70, 100);
    stroke(270, 100, 70, 100);
    strokeWeight(10);
  }

  function draw() {
    background(0, 0, 0, 100);
    ellipse(mouseX, mouseY, 50, 50);
  }
colorModeText: |
  colorMode() in p5.js sets how colors are interpreted. Using <a href="https://color.adobe.com/de/create/color-wheel">HSB</a> (Hue, Saturation, Brightness) is often better because it separates color, intensity, and lightness, making color control more intuitive. 

randomCode: |
  function setup() {
    createCanvas(400, 400);
    colorMode(HSB, 360, 100, 100, 100);
    fill(90, 100, 70, 100);
    stroke(270, 100, 70, 100);
    strokeWeight(10);
  }

  function draw() {
    background(0, 0, 0, 100);

    const dotSize = random(-20, 100);
    ellipse(mouseX, mouseY, dotSize);
  }
randomText: | 
  random() in p5.js returns a random number, useful for adding unpredictability. randomSeed() sets the starting point for random values, making results repeatable — helpful for debugging or creating consistent outcomes.

mapText: |
  map() in p5.js converts a number from one range to another. It's useful for scaling values, like turning mouse position into color or speed.

mapCode: |
  function setup() {
    createCanvas(400, 400);
    colorMode(HSB, 360, 100, 100, 100);
    fill(90, 100, 70, 100);
  }

  function draw() {
    background(0, 0, 0, 100);
    const hue = map(mouseX, 0, 400, 0, 360);
    const dotSize = map(mouseY, 0, 400, 0, 50);
    fill(hue, 100, 100, 100);
    ellipse(mouseX, mouseY, dotSize);
  }

distText: |
  dist() in p5.js calculates the distance between two points. It's useful for measuring how far apart objects are, often used in movement or collision detection.
distCode: |
  function setup() {
    createCanvas(400, 400);
    colorMode(HSB, 360, 100, 100, 100);
    fill(90, 100, 70, 100);
  }

  function draw() {
    background(0, 0, 0, 100);
    const dotSize = dist(0, 0, mouseX, mouseY);
    ellipse(width/2, height/2, dotSize);
  }

translateText: |
  translate() in p5.js moves the origin of the drawing space, letting you draw shapes in a new position. rotate() turns the drawing space, useful for rotating shapes around a point.
translateCode: |
  function setup() {
    createCanvas(400, 400);
    colorMode(HSB, 360, 100, 100, 100);
    fill(335, 92, 87, 100);
  }

  function draw() {
    background(0, 0, 0, 100);
    translate(width/2, height/2);
    rotate(45);
    rect(-30, -30, 60, 60);
  }

animationText: |
  This code creates a rotating rectangle in the center of the canvas. The translate() function moves the origin to the center, and rotate(angle) spins the rectangle around that point. angle increases over time, causing continuous rotation, while the semi-transparent background creates a fading trail effect.
animationCode: |
  let angle = 0;

  function setup() {
    createCanvas(400, 400);
    colorMode(HSB, 360, 100, 100, 100);
    fill(335, 92, 87, 100);
  }

  function draw() {
    background(0, 0, 0, 10);

    translate(width/2, height/2);
    rotate(angle);
    rect(0, 0, 60, 60);

    angle += 0.08;
  }


---

{% codeSmall "Core Structure of a Sketch", theLoopText, theLoop , "javascript", "slide" %}

{% codeSmall "Useful Snippets: ColorMode", colorModeText, colorMode , "javascript", "slide" %}

{% codeSmall "Useful Snippets: random() & randomSeed()", randomText, randomCode , "javascript", "slide" %}

{% codeSmall "Useful Snippets: map()", mapText, mapCode , "javascript", "slide" %}

{% codeSmall "Useful Snippets: dist()", distText, distCode , "javascript", "slide" %}

{% codeSmall "Brain-Freeze: translate() & rotate()", translateText, translateCode , "javascript", "slide" %}

{% codeSmall "Useful Snippets: Simple Animation", animationText, animationCode , "javascript", "slide" %}



