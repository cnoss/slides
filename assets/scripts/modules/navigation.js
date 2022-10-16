export default class Navigation {
  constructor() {
    this.slug = window.location.pathname;
    this.navItems = document.querySelectorAll('[data-js-navitem]');
    this.submenu = false;
    this.currentNavElement = false;
  }

  createSubmenu() {
    const elements = document.querySelectorAll('[data-js-scrollspy]');
    const submenuItems = [];
    elements.forEach((element) => {
      const link = `#${element.id}`;
      const linktext = element.querySelector('[data-js-linktext]').innerText;
      const item = `
        <li class="subnavbar__item">
          <a href="${link}">${linktext}</a>
        </li>
      `;

      submenuItems.push(item);
    });

    const submenu = `
      <ul class="subnavbar" data-js-dropdown-target="theory">
        ${submenuItems.join('\n')}
      </ul>
    `;

    this.submenu = submenu;
  }

  getCurrentPage() {
    this.navItems.forEach((item) => {
      const anchor = item.querySelector('[href]');

      if (!anchor.href.match(this.slug)) return;
      item.setAttribute('data-state', 'active');

      const wrapper = document.createElement('div');
      wrapper.innerHTML = this.submenu;
      item.appendChild(wrapper);

      if (!item.querySelector('.subnavbar')) return;
      item.querySelector('.subnavbar').setAttribute('data-state', 'active');
    });
  }

  init() {
    this.createSubmenu();
    this.getCurrentPage();
  }
}
