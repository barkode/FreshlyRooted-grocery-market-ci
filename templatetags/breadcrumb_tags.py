from django import template

register = template.Library()


@register.simple_tag
def breadcrumb(url_name, obj=None):
    breadcrumbs = [("Home", "/")]
    if url_name == "cart":
        breadcrumbs.append(("Cart", "/cart/"))
    elif url_name == "products":
        breadcrumbs.append(("Products", "/products/"))
        if obj:
            breadcrumbs.append((obj.name, f"/products/{obj.id}/"))

    return breadcrumbs
