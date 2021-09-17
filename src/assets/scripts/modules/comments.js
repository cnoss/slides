/* eslint-disable import/extensions */
import fetchData from './fetchData.js';

export default class Comments {
  constructor(url) {
    this.url = url;
    this.target = document.querySelector('[data-js-comment-list]');
  }

  async fetchData() {
    try {
      const response = await fetch(this.url);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (e) {
      // eslint-disable-next-line no-console
      console.error(e);
    }

    return true;
  }

  async init() {
    if (this.target) {
      const data = await fetchData(this.url);
      if (data) {
        this.renderData(data);
      } else {
        // eslint-disable-next-line no-console
        console.error('Fehler beim Erzeugen der Kommentare.');
      }
    }
    return true;
  }

  renderError(error) {
    this.target.innerHTML = `<li>Die Kommentare konnten leider nicht geladen werden.  Fehler: ${error}</li>`;
  }

  renderData(data) {
    const html = [];
    data.forEach((entry) => {
      html.push(`
        <li class="comment-list__item">
          <figure class="comment">
            <img src="https://mi-classroom.github.io/fd-2021-content/js-session-2/avatars/${entry.avatar}">
            <figcaption>
              <h3 class="comment-title">${entry.firstname} ${entry.lastname}, ${entry.date}</h3>
              <p class="comment-body">${entry.comment} </p>
            </figcaption>
          </figure>
        </li>
      `);
    });

    this.target.innerHTML = html.join('\n');
  }
}
