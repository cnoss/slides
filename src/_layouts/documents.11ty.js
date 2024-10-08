exports.render = function (data) {

  return `<!doctype html>
  <html lang="de">
    <head>
      <title>${data.title}</title>
      ${this.meta()}
      <link rel="stylesheet" href="${this.url('/assets/main.css')}">
      <link rel="icon" type="image/svg" href="${this.url('/assets/images/preview_black_24dp.svg')}">
      <link rel="manifest" href="${this.url('/manifest.json')}">
    </head>
    <body class="document">
      <main>
      <h1>${data.title}</h1>
      ${data.content}
      </main>
    </body>
  </html>`;
};
