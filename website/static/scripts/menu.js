const buttons = document.querySelectorAll('.menu-btn');
const contents = document.querySelectorAll('.menu-content');
const container = document.querySelector('.container');

let currentActive = "register"; // default panel (same as startup)

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    const target = btn.getAttribute('data-target');

    // 🚫 Prevent animation if same button is clicked again
    if (target === currentActive) {
      return;
    }
    currentActive = target;

    // Hide all panels first
    contents.forEach(c => c.classList.remove('active'));

    if (target === 'search') {
      // morph to "search" view
      container.classList.add('morphed');

      // wait for morph animation, then show panel
      setTimeout(() => {
        document.getElementById('search').classList.add('active');
      }, 1500);
    } 
    else if (target === 'register') {
      // morph back to original view
      container.classList.remove('morphed');

      // wait for morph reset, then show panel
      setTimeout(() => {
        document.getElementById('register').classList.add('active');
      }, 1500);
    }
    else if (target === 'logout') {
      // morph reset for logout (like register)
      container.classList.remove('morphed');
      setTimeout(() => {
        document.getElementById('logout').classList.add('active');
      }, 1500);
    }
  });
});
