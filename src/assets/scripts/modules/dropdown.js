export default class Dropdown {
  constructor() {
    this.trigger = document.querySelectorAll('[data-js-dropdown]');
  }

  init() {
    this.trigger.forEach(
      (ele) => {
        const element = ele;
        element.addEventListener('click', (event) => {
          const dropDownTargetName = event.currentTarget.dataset.jsDropdown;
          const dropDownTarget = document.querySelector(`[data-js-dropdown-target=${dropDownTargetName}]`);

          if (dropDownTarget.dataset.state === 'active') {
            dropDownTarget.dataset.state = 'closed';
            element.dataset.state = 'closed';
          } else {
            dropDownTarget.dataset.state = 'active';
            element.dataset.state = 'active';
          }
        });
      },
    );
  }
}
