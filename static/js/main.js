// ===== Highlight Selected Label =====
const options = document.querySelectorAll('input[name="option"]');
const labels = {
    'connect-db': document.getElementById('label-db'),
    'template': document.getElementById('label-template')
};

options.forEach(input => {
    input.addEventListener('change', () => {
        // Reset all borders
        Object.values(labels).forEach(label => label.classList.remove('border-indigo-600', 'shadow-lg'));
        // Add border + shadow to selected
        labels[input.value].classList.add('border-indigo-600', 'shadow-lg');
    });
});

// Trigger default selection on page load
const checkedInput = document.querySelector('input[name="option"]:checked');
if (checkedInput) {
    labels[checkedInput.value].classList.add('border-indigo-600', 'shadow-lg');
}

// ===== Loading Screen Animation =====
const progress = document.getElementById('progress');
const loadingScreen = document.getElementById('loading-screen');
const contentForm = document.getElementById('optionForm');
let width = 0;

const interval = setInterval(() => {
    width += 1;
    progress.style.width = width + '%';
    if (width >= 100) {
        clearInterval(interval);
        loadingScreen.classList.add('hidden');
        contentForm.classList.remove('hidden');
    }
}, 30);

// ===== Mobile Menu Toggle (if used) =====
const menuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
}
