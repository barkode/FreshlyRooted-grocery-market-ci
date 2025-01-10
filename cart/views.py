from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    HttpResponse,
    redirect,
    render,
    reverse,
)
from products.models import Product


def view_cart(request):
    """A view that renders the cart contents page."""
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the shopping cart."""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity", "1"))
    redirect_url = request.POST.get("redirect_url")
    size = request.POST.get("product_size")
    cart = request.session.get("cart", {})

    def add_or_update_cart_with_size(product, item_id, size, quantity):
        """Helper function to add or update cart items with size."""
        if size in cart[item_id]["items_by_size"]:
            cart[item_id]["items_by_size"][size] += quantity
            messages.success(
                request,
                f"Updated size {size.upper()} {product.name} quantity to "
                f"{cart[item_id]['items_by_size'][size]}",
            )
        else:
            cart[item_id]["items_by_size"][size] = quantity
            messages.success(
                request, f"Added size {size.upper()} {product.name} to your cart"
            )

    def add_or_update_cart_without_size(product, item_id, quantity):
        """Helper function to add or update cart items without size."""
        if item_id in cart:
            cart[item_id] += quantity
            messages.success(
                request, f"Updated {product.name} quantity to {cart[item_id]}"
            )
        else:
            cart[item_id] = quantity
            messages.success(request, f"Added {product.name} to your cart")

    if size:
        if item_id in cart:
            add_or_update_cart_with_size(product, item_id, size, quantity)
        else:
            cart[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request, f"Added size {size.upper()} {product.name} to your cart"
            )
    else:
        add_or_update_cart_without_size(product, item_id, quantity)

    request.session["cart"] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount."""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = request.POST.get("product_size")
    cart = request.session.get("cart", {})

    def update_cart_size(product, item_id, size, quantity):
        """Helper function to update cart items with size."""
        cart[item_id]["items_by_size"][size] = quantity
        messages.success(
            request,
            f"Updated size {size.upper()} {product.name} quantity to "
            f"{cart[item_id]['items_by_size'][size]}",
        )

    def remove_size_from_cart(product, item_id, size):
        """Helper function to remove sized items from cart."""
        del cart[item_id]["items_by_size"][size]
        if not cart[item_id]["items_by_size"]:
            cart.pop(item_id)
        messages.success(
            request, f"Removed size {size.upper()} {product.name} from your cart"
        )

    def update_cart_without_size(product, item_id, quantity):
        """Helper function to update cart items without size."""
        cart[item_id] = quantity
        messages.success(request, f"Updated {product.name} quantity to {cart[item_id]}")

    def remove_item_from_cart(product, item_id):
        """Helper function to remove items from cart."""
        cart.pop(item_id)
        messages.success(request, f"Removed {product.name} from your cart")

    if size:
        if quantity > 0:
            update_cart_size(product, item_id, size, quantity)
        else:
            remove_size_from_cart(product, item_id, size)
    else:
        if quantity > 0:
            update_cart_without_size(product, item_id, quantity)
        else:
            remove_item_from_cart(product, item_id)

    request.session["cart"] = cart
    return redirect(reverse("cart:view_cart"))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart."""
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get("product_size")
        cart = request.session.get("cart", {})

        def remove_item_size(cart, item_id, size):
            """Helper function to remove sized items."""
            del cart[item_id]["items_by_size"][size]
            if not cart[item_id]["items_by_size"]:
                cart.pop(item_id)
            messages.success(
                request, f"Removed size {size.upper()} {product.name} from your cart"
            )

        if size:
            remove_item_size(cart, item_id, size)
        else:
            cart.pop(item_id)
            messages.success(request, f"Removed {product.name} from your cart")

        request.session["cart"] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)


def clear_cart(request):
    """Remove all items from the shopping cart."""
    try:
        cart = request.session.get("cart", {})
        cart.clear()
        request.session["cart"] = cart
        messages.success(request, "Your cart has been cleared")
        return redirect(reverse("cart:view_cart"))

    except Exception as e:
        messages.error(request, f"Error clearing cart: {e}")
        return HttpResponse(status=500)
