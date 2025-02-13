  const darkModeToggle = document.getElementById('darkModeToggle');
  const html = document.documentElement;

  // On page load, check local storage for theme preference
  document.addEventListener('DOMContentLoaded', () => {
      const theme = localStorage.getItem('theme');
      if (theme === 'dark') {
          html.classList.add('dark');
          darkModeToggle.innerHTML = '<i class="fas fa-sun text-2xl"></i>';
      } else {
          html.classList.remove('dark');
          darkModeToggle.innerHTML = '<i class="fas fa-moon text-2xl"></i>';
      }
  });

  // Toggle dark mode and store preference in local storage
  darkModeToggle.addEventListener('click', () => {
      html.classList.toggle('dark');
      const isDark = html.classList.contains('dark');
      if (isDark) {
          localStorage.setItem('theme', 'dark');
          darkModeToggle.innerHTML = '<i class="fas fa-sun text-2xl"></i>';
      } else {
          localStorage.setItem('theme', 'light');
          darkModeToggle.innerHTML = '<i class="fas fa-moon text-2xl"></i>';
      }
  });