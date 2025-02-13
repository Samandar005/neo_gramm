 const darkModeToggle = document.getElementById('darkModeToggle');
const html = document.documentElement;

darkModeToggle.addEventListener('click', () => {
    html.classList.toggle('dark');
    const isDark = html.classList.contains('dark');
    darkModeToggle.innerHTML = isDark ? '<i class="fas fa-sun text-2xl"></i>' : '<i class="fas fa-moon text-2xl"></i>';
});