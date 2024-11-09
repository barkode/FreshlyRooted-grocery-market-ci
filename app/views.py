from django.shortcuts import render


def custom_400(request, exception):
    """
    Handles 400 Bad Request error.

    Parameters:
    request -- The HTTP request object.
    exception -- The exception that was raised causing the 400 error.

    Returns:
    Renders and returns the 400 error page (errors/400.html) with a 400 HTTP status.
    """
    return render(request, "errors/400.html", status=400)


def custom_403(request, exception):
    """
    custom_403 handles HTTP 403 Forbidden errors and returns a custom 403 error page.

    Parameters:
    request - The HTTP request object.
    exception - The exception that triggered the 403 error.

    Returns:
    HttpResponse - A response object containing the rendered 403 error page and a 403 status code.
    """
    return render(request, "errors/403.html", status=403)


def custom_404(request, exception):
    """
    custom_404 is a Django view function that handles 404 errors.

    Parameters:
    request: HttpRequest object representing the client's request.
    exception: Exception object representing the 404 error raised.

    Returns:
    HttpResponse object rendering the 'errors/404.html' template with a 404 status code.
    """
    return render(request, "errors/404.html", status=404)


def custom_500(request):
    """

    Handles custom 500 internal server error.

    Args:
        request: HTTP request object.
        exception: Exception that caused the 500 error.

    Returns:
        HttpResponse object rendering the "500.html" template with a 500 status code.
    """
    return render(request, "errors/500.html", status=500)
