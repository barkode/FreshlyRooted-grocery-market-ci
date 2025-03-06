from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponseRedirect,
)
from django.contrib import messages
from django.http import Http404

from .models import Wishlist
from profiles.models import UserProfile
from products.models import Product


# View to display the user's wishlist
def view_wishlist(request):
    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to add to your Wishlist."
        )
        return redirect(reverse("account_login"))

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user=user.user)

    template_name = "wishlist/wishlist.html"
    context = {"wishlist": wishlist}
    return render(request, template_name, context)


# View to add a product to the user's wishlist
def add_wishlist(request, product_id):
    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to add to your Wishlist."
        )
        return redirect(reverse("account_login"))

    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlist = get_object_or_404(Wishlist, user=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, f"{product.name} is already on your Wishlist!")
    else:
        wishlist.products.add(product)
        messages.info(request, f"{product.name} has been added to your Wishlist!")  # noqa

    redirect_url = request.META.get("HTTP_REFERER", reverse("products"))

    return HttpResponseRedirect(redirect_url)


# View to remove a product from the user's wishlist
def remove_wishlist(request, product_id):
    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to edit your Wishlist."
        )
        return redirect(reverse("account_login"))

    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get(user=request.user)

    wishlist.products.remove(product)
    messages.info(request, f"{product.name} has been removed from your Wishlist!")  # noqa

    redirect_url = request.META.get("HTTP_REFERER", reverse("products"))

    return HttpResponseRedirect(redirect_url)


# View to clear all products from the user's wishlist
def clear_wishlist(request):
    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to edit your Wishlist."
        )
        return redirect(reverse("account_login"))

    wishlist = Wishlist.objects.get(user=request.user)

    products = wishlist.products.all()

    for product in products:
        wishlist.products.remove(product)

    wishlist.products.remove(product)
    messages.info(request, "Wishlist cleared!")

    return redirect(reverse("wishlist"))
