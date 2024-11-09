from django.contrib import messages
from django.shortcuts import render

from .forms import CollaborateForm
from .models import About


# Create your views here.


def about_contact(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
            The most recent instance of :model:`about.About`.
            ``collaborate_form``
                    An instance of :form:`about.CollaborateForm`.

    **Template**
    :template:`about/about.html`
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days.",
            )
    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/contact.html",
        {"about": about, "collaborate_form": collaborate_form},
    )


def about_privacy_policy(request):
    return render(request, "about/privacy_policy.html")


def about_return_policy(request):
    return render(request, "about/return_policy.html")


def about_us(request):
    return render(request, "about/about.html")
