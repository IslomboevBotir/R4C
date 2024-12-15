import os

from celery import Celery

from R4C.settings import RABBITMQ_PORT, RABBITMQ_HOST

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R4C.settings')

app = Celery(broker=f'amqp://guest:guest@{RABBITMQ_HOST}:{RABBITMQ_PORT}//')

app.conf.task_routes = {
    "orders.tasks.check_is_customer_order": {"queue": "high-load"}
}
