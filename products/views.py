from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Category, Product


# Create your views here.

def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None

    sort_options = {
        'default': 'name',
        'price_asc': 'price',
        'price_desc': '-price',
        'rating': '-rating',
        'date': '-created_at',
        }

    if request.GET:
        if 'sort' in request.GET and sort_options.get(request.GET['sort']):
            sortkey = request.GET.get('sort', 'default')
            products = products.order_by(sort_options[sortkey])
        else:
            products = products.order_by(sort_options['default'])

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__slug__in=categories)
            categories = Category.objects.filter(slug__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You have not entered any search criteria!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = sort

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        }

    template = 'products/products.html'

    return render(request, template, context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        }

    return render(request, 'products/product_detail.html', context)
