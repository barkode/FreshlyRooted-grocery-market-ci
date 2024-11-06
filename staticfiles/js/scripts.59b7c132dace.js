// Scroll to top
const btnScrollTop = document.querySelector('.btn-scroll-top');
const windowElement = window;
const preLoader = document.querySelector('.loading');

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
    console.log('Preloader loaded');
    if (preLoader) {
        console.log('Preloader found');
        preLoader.style.transition = 'opacity 0.8s';
        preLoader.style.opacity = '0';

        setTimeout(() => {
            preLoader.remove();
        }, 3000);
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const clearCartBtn = document.getElementById('clearCartBtn');
    if (clearCartBtn) {
        clearCartBtn.addEventListener('click', function (e) {
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
                setTimeout(() => {
                    window.location.href = "{% url 'cart:clear_cart' %}";
                }, cartItems.length * 100 + 500);
            }
        });
    }
    const updateItemsList = document.querySelectorAll('.update-item');
    if (updateItemsList.length > 0) {
        updateItemsList.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const form = document.querySelector('.cart-form');
                if (form) {
                    form.submit();
                }
            });
        });
    }

    const deleteItemsList = document.querySelectorAll('.delete-item');
    if (deleteItemsList.length > 0) {
        deleteItemsList.forEach(link => {
            link.addEventListener('click', async (e) => {
                e.preventDefault();
                const csrfToken = "{{ csrf_token }}";
                const itemId = link.dataset.item_id.split('remove_')[1];
                // Validate itemId
                if (!itemId) {
                    console.error('Invalid item ID');
                    return;
                }
                const url = `/cart/remove/${itemId}/`;
                // Create form data
                const formData = new FormData();
                formData.append('csrfmiddlewaretoken', csrfToken);
                try {
                    // Send POST request
                    const response = await fetch(url, {
                        method: 'POST',
                        body: formData
                    });
                    // Handle response
                    if (response.ok) {
                        location.reload();
                    } else {
                        console.error('Failed to remove item:', response.statusText);
                    }
                } catch (error) {
                    console.error('Error removing item:', error);
                }
            });
        });
    }
});

