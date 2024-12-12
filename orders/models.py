from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
