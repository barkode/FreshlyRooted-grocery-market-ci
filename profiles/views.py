from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    # Retrieve the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Handle form submission for updating the user profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    # Retrieve the user's order history 
    orders = profile.orders.all()

    # Render the profile page with the user's profile, form, and order history
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    # Retrieve the specific order using the order number
    order = get_object_or_404(Order, order_number=order_number)

    # Display a message about the past order confirmation
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # Render the order history page with the specific order details
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
