 tailwind.config = {
        darkMode: 'class',
        theme: {
            extend: {
                colors: {
                    neoblue: '#3b82f6',
                    neopink: '#ec4899',
                    neodark: '#1f2937',
                }
            }
        }
    }
    const darkModeToggle = document.getElementById('darkModeToggle');
        const html = document.documentElement;

        darkModeToggle.addEventListener('click', () => {
            html.classList.toggle('dark');
            const isDark = html.classList.contains('dark');
            darkModeToggle.innerHTML = isDark ? '<i class="fas fa-sun text-2xl"></i>' : '<i class="fas fa-moon text-2xl"></i>';
        });