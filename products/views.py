from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.http import urlencode

from favorites.models import Favorites
from .forms import ProductForm
from .models import Category, Product


# renders all products from database
def all_products(request):
    products = Product.objects.all()
    user = request.user
    query = None
    categories = None
    sort = None
    direction = None

    if user.is_authenticated:
        favorites, created = Favorites.objects.get_or_create(user=user)
    else:
        favorites = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            elif sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"]
            if categories:
                categories = categories.split(",")
                products = products.filter(category__slug__in=categories)
                categories = Category.objects.filter(slug__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(category__name__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    items_per_page = 12
    paginator = Paginator(products, items_per_page)
    page = request.GET.get("page")

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    get_copy = request.GET.copy()
    if "page" in get_copy:
        del get_copy["page"]
    params = urlencode(get_copy, doseq=True)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
        "favorites": favorites,
        "params": params,
    }

    return render(request, "products/products.html", context)


# view for product detail page
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_authenticated:
        template = "products/product_detail.html"
        context = {
            "product": product,
        }
        return render(request, template, context)
    else:
        user = request.user
        favorites = Favorites.objects.filter(user=user, products=product_id).exists()

        template = "products/product_detail.html"
        context = {
            "product": product,
            "favorites": favorites,
        }
        return render(request, template, context)


# view fom admin adding a product
@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product:product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


# view to edit a product
@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home:home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("products:product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


# view to delete a product
@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home:home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products:products"))
