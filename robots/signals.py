from django.db.models.signals import post_save
from django.dispatch import receiver

from robots.models import Robot
from orders.tasks import check_is_customer_order


@receiver(post_save, sender=Robot)
def customer_order_check(sender, instance, created, **kwargs):
    if not created:
        return
    check_is_customer_order.delay(instance.id)
