from django.contrib import messages
from django.shortcuts import render

from .forms import CollaborateForm
from .models import About


def about_contact(request):
    """
    Args:
    request: The HTTP request object that contains metadata about the request.
    Handles 'GET' and 'POST' requests to the 'about/contact' page. On 'POST',
    it processes and validates the 'CollaborateForm', saving it if valid
    and displaying a success message.
    Renders the 'about/contact.html' template with the latest 'About' object
    and a new 'CollaborateForm' instance.
    Returns:
        HttpResponse: Rendered 'about/contact.html' template with context data.
    """
    if request.method == "POST":
        if process_collaborate_form(request):
            message = (
                "Collaboration request received! "
                "I endeavour to respond within 2 working days."
            )
            messages.success(request, message)

    about_info = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    context = {"about": about_info, "collaborate_form": collaborate_form}

    return render(request, "about/contact.html", context)


def process_collaborate_form(request):
    form = CollaborateForm(data=request.POST)
    if form.is_valid():
        form.save()
        return True
    return False


def about_privacy_policy(request):
    """
    Args:
    request: An HttpRequest object that contains metadata about the request
    being processed.
    Returns:
    HttpResponse: A response object that renders the "privacy_policy.html"
    template.
    """
    return render(request, "about/privacy_policy.html")


def about_return_policy(request):
    """
    Args:
        request: HttpRequest object that contains metadata about the request.
    """
    return render(request, "about/return_policy.html")


def about_us(request):
    """
    Args:
        request: An HttpRequest object containing metadata about the request.
    Returns:
    HttpResponse: A response object that renders the "about/about.html" page.
    """
    return render(request, "about/about.html")
