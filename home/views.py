from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Renders the home page.

    This view handles requests to the home page URL and
    renders the corresponding HTML template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """

    return render(
        request,
        "home/index.html",
    )
