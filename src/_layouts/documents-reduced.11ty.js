exports.render = function (data) {


  return `<!doctype html>
  <html lang="de">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  
      <title>${data.title}</title>
  
      <link rel="stylesheet" href="/assets/main.css">
      <link rel="icon" type="image/svg" href="/assets/images/preview_black_24dp.svg">
    </head>
    <body>
      ${data.content}
    </body>
    <script src="/assets/scripts/gdw.js"></script>
  </html>`;
};
