---
title: Use of a higher-level Shared Worker
subtitle: Shared Process with Message-Based Communication
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
footer: |
  - [Shared Worker MDN](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker)
worker: |
  // Shared Worker Code in shared.js
  /**/
  const connections = [];
  /**/
  onconnect = function (e) {
    const port = e.ports[0];
    connections.push(port);
    /**/
    port.onmessage = function (event) {
      const data = event.data;
      /**/
      // Echo to all other windows
      connections.forEach(p => {
        if (p !== port) {
          p.postMessage(data);
        }
      });
    };
    /**/
    port.start(); // Required for older browsers
  };

workerDescription: |
  This creates a new connection to an existing or newly started SharedWorker whose code is located in the shared.js file. In contrast to workers, which start a separate thread per window or tab, a SharedWorker is only started once per Origin - all tabs share the same worker process.

client: |
  // Client Code
  // Start or connect to worker
  const worker = new SharedWorker('shared.js');
  worker.port.start();
  /**/
  const trackMyWindowPosition = () => {
    /* ... */
    // Store Window Data in Shared Worker
    worker.port.postMessage(myWindowPosition);
  }
  /**/
  // Observe my window position
  const observeMyWindowPosition = setInterval(trackMyWindowPosition, 500);
  /**/
  // Receive messages from the worker
  worker.port.onmessage = (event) => {
    /**/
    const otherWindowPosition = event.data;
    /**/
    // Do something meaningful with the data 🕺🏼
    console.log(otherWindowPosition.x, otherWindowPosition.y);
  };

---

{% interlude "Use of a higher-level Shared Worker","Shared Process with Message-Based Communication" %}

{% screenshotFs "./images/shared-worker.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Use of a higher-level [Shared Worker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker)"}' %}

{% codeSmall "Shared Worker with postMessage()", workerDescription, [{code: worker, lang: "javascript"}, {code: client, lang: "javascript"}], "css", "fade" %}

{% screenshotFs "./images/shared-worker.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Use of a higher-level [Shared Worker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker)"}' %}

