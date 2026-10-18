/**
 * Dark / Light Mode mavzusi boshqaruv skripti
 * LocalStorage va tizim afzalliklari (prefers-color-scheme) bilan integratsiya qilingan
 */

function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        document.documentElement.classList.add('dark');
        updateThemeIcons(true);
    } else {
        document.documentElement.classList.remove('dark');
        updateThemeIcons(false);
    }
}

function toggleTheme() {
    const isDark = document.documentElement.classList.contains('dark');
    if (isDark) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
        updateThemeIcons(false);
    } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        updateThemeIcons(true);
    }
}

function updateThemeIcons(isDark) {
    const sunIcons = document.querySelectorAll('.theme-icon-sun');
    const moonIcons = document.querySelectorAll('.theme-icon-moon');

    sunIcons.forEach(icon => {
        if (isDark) {
            icon.classList.remove('hidden');
        } else {
            icon.classList.add('hidden');
        }
    });

    moonIcons.forEach(icon => {
        if (isDark) {
            icon.classList.add('hidden');
        } else {
            icon.classList.remove('hidden');
        }
    });
}

// Sahifa yuklanganda ishga tushirish
document.addEventListener('DOMContentLoaded', () => {
    initTheme();

    const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
    themeToggleBtns.forEach(btn => {
        btn.addEventListener('click', toggleTheme);
    });

    // Mobil menyuni ochish / yopish
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }
});
