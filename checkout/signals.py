from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Signal receiver to update order total on saving an OrderLineItem instance.
    """

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Signal receiver to update order
    total on deleting an OrderLineItem instance.
    """

    instance.order.update_total()
