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

document.getElementById('clearCartBtn').addEventListener('click', function (e) {
    e.preventDefault();

    if (confirm('Are you sure you want to clear your cart?')) {
        const cartItems = document.querySelectorAll('.cart-item');

        cartItems.forEach((item, index) => {
            setTimeout(() => {
                item.style.transition = 'all 0.5s ease';
                item.style.opacity = '0';
                item.style.transform = 'translateX(100px)';
            }, index * 100);
        });

        // Переходимо на URL очищення після завершення анімації
        setTimeout(() => {
            window.location.href = "{% url 'cart:clear_cart' %}";
        }, cartItems.length * 100 + 500);
    }
});

// Update quantity on click
document.querySelectorAll('.update-link').forEach(link => {
    link.addEventListener('click', (e) => {
        const form = link.previousElementSibling.querySelector('.update-form');
        if (form) {
            form.submit();
        }
    });
});

// Update quantity on click
document.querySelectorAll('.update-link').forEach(link => {
    link.addEventListener('click', (e) => {
        const form = link.previousElementSibling;
        form.submit();
    });
});

// Remove item and reload on click
document.querySelectorAll('.remove-item').forEach(button => {
    button.addEventListener('click', async (e) => {
        const csrfToken = "{{ csrf_token }}";
        const itemId = button.id.split('remove_')[1];
        const productSize = button.dataset.product_size;
        const url = `/cart/remove/${itemId}/`;

        const formData = new FormData();
        formData.append('csrfmiddlewaretoken', csrfToken);
        formData.append('product_size', productSize);

        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                location.reload();
            } else {
                console.error('Error removing item:', response.statusText);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});