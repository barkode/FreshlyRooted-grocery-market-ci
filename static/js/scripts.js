// Scroll to top
const btnScrollTop = document.querySelector('.btn-scroll-top');
const windowElement = window;
const preLoader = document.getElementById('biof-loading');

if (btnScrollTop) {
    windowElement.addEventListener('scroll', () => {
        if (windowElement.scrollY >= 800) {
            btnScrollTop.classList.add('showUp');
        } else {
            btnScrollTop.classList.remove('showUp');
        }
    });

    btnScrollTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Preload handle
windowElement.addEventListener('load', () => {
    if (preLoader) {
        preLoader.style.transition = 'opacity 0.8s';
        preLoader.style.opacity = '0';

        setTimeout(() => {
            preLoader.remove();
        }, 3000);
    }
});

document.addEventListener('click', (e) => {
    // Проверяем, что клик был по кнопке qty-btn внутри qty-input
    if (!e.target.closest('.qty-input .qty-btn')) return;

    e.preventDefault();

    const btn = e.target.closest('.qty-btn');
    const input = btn.parentElement.querySelector("input[name^='quantity']");

    if (!input) return;

    const currentVal = parseInt(input.value, 10);
    const maxVal = parseInt(input.dataset.max_value, 10);
    const step = parseInt(input.dataset.step, 10);

    if (btn.classList.contains('btn-up')) {
        const newVal = currentVal + step;
        if (newVal <= maxVal) {
            input.value = newVal;
        }
    } else {
        const newVal = currentVal - step;
        if (newVal > 0) {
            input.value = newVal;
        }
    }
});