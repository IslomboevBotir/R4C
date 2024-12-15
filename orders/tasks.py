from R4C.celery import app
from django.core.mail import send_mass_mail

from orders.models import Order
from robots.models import Robot
from orders.constants import EMAIL_SUBJECT_ROBOT_IN_STOCK, EMAIL_MESSAGE_ROBOT_IN_STOCK
from R4C.settings import EMAIL_HOST_USER


@app.task
def check_is_customer_order(robot_id: int):
    robot = Robot.objects.filter(pk=robot_id).first()
    if not robot:
        return
    customer_emails = Order.objects.filter(robot_serial=robot.serial).values_list("customer__email", flat=True)
    if not customer_emails:
        return
    send_mass_mail(
        (
            (
                EMAIL_SUBJECT_ROBOT_IN_STOCK.format(robot_model=robot.model),
                EMAIL_MESSAGE_ROBOT_IN_STOCK.format(robot_model=robot.model, robot_serial=robot.serial),
                EMAIL_HOST_USER,
                customer_emails
            ),
        )
    )
