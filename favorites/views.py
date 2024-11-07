from django.contrib import messages
from django.http import Http404
from django.shortcuts import (get_object_or_404, HttpResponseRedirect, redirect, render, reverse)

from products.models import Product
from profiles.models import UserProfile
from .models import Favorites


# View to display the user's favorites list
def view_favorites(request):
	if not request.user.is_authenticated:
		messages.error(
			request, "Sorry, you need to be logged in to add to your Wishlist."
			)
		return redirect(reverse("account_login"))

	user = get_object_or_404(UserProfile, user=request.user)
	favorites, created = Favorites.objects.get_or_create(user=user.user)

	template_name = "favorites/favorites.html"
	import favorites
	context = {"favorites": favorites}


	return render(request, template_name, context)


# View to add a product to the user's favorites list
def add_favorites(request, product_id):
	if not request.user.is_authenticated:
		messages.error(
			request, "Sorry, you need to be logged in to add to your Favorites."
			)
		return redirect(reverse("account_login"))

	product = get_object_or_404(Product, pk=product_id)
	try:
		fav_lst = get_object_or_404(Favorites, user=request.user.id)
	except Http404:
		fav_lst = Favorites.objects.create(user=request.user)

	if product in fav_lst.products.all():
		messages.info(request, f"{product.name} is already on your Favorites!")
	else:
		fav_lst.products.add(product)
		messages.info(request, f"{product.name} has been added to your Favorites!")  # noqa

	redirect_url = request.META.get("HTTP_REFERER", reverse("products"))

	return HttpResponseRedirect(redirect_url)


# View to remove a product from the user's wishlist
def remove_wishlist(request, product_id):
	if not request.user.is_authenticated:
		messages.error(
			request, "Sorry, you need to be logged in to edit your Favorites."
			)
		return redirect(reverse("account_login"))

	product = get_object_or_404(Product, pk=product_id)
	fav_lst= Favorites.objects.get(user=request.user)

	fav_lst.products.remove(product)
	messages.info(request, f"{product.name} has been removed from your Favorites!")  # noqa

	redirect_url = request.META.get("HTTP_REFERER", reverse("products"))

	return HttpResponseRedirect(redirect_url)


# View to clear all products from the user's wishlist
def clear_favorites(request):
	if not request.user.is_authenticated:
		messages.error(
			request, "Sorry, you need to be logged in to edit your Wishlist."
			)
		return redirect(reverse("account_login"))

	fav_lst = Favorites.objects.get(user=request.user)

	products = fav_lst.products.all()

	for product in products:
		fav_lst.products.remove(product)

	fav_lst.products.remove(product)
	messages.info(request, "Wishlist cleared!")

	return redirect(reverse("favorites:view_favorites"))