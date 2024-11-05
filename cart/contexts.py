from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = Decimal("0.00")
    product_count = 0
    cart = request.session.get("cart", {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            currency_symbol = product.currency.symbol
            total += Decimal(item_data) * product.sell_price()
            product_count += item_data
            cart_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                    "currency_symbol": currency_symbol,
                }
            )
        else:
            product = get_object_or_404(Product, pk=item_id)
            currency_symbol = product.currency.symbol
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.sell_price()
                product_count += quantity
                cart_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "size": size,
                        "currency_symbol": currency_symbol,
                    }
                )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        progress_percentage = (total / settings.FREE_DELIVERY_THRESHOLD) * 100
    else:
        delivery = 0
        free_delivery_delta = 0
        progress_percentage = 100

    grand_total = delivery + total

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
        "progress_percentage": progress_percentage,
    }

    return context
