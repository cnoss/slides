export default class ScrollSpy {
  constructor(menu, sections) {
    this.menu = menu;
    this.sections = sections;
    this.lastActiveItem = false;
  }

  init() {
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          this.refreshNavigation(entry);
        }
      });
    });

    this.sections.forEach((section) => {
      imageObserver.observe(section);
    });
  }

  refreshNavigation(targetNavElement) {
    const { id } = targetNavElement.target;
    const pattern = `[href$=${id}]`;
    const anchor = this.menu.querySelector(pattern);
    const menuItem = anchor.closest('.subnavbar__item');

    if (this.lastActiveItem) { this.lastActiveItem.removeAttribute('data-state'); }
    menuItem.setAttribute('data-state', 'active');
    this.lastActiveItem = menuItem;
  }
}
