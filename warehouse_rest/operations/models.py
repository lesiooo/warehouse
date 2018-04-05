from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.reverse import reverse
from django.contrib.postgres.fields import ArrayField

from warehouse.models import SemiFinishedItem, FinishedProduct

# Create your models here.

OPERATION_CHOICES =(
    ('ER', 'External Goods Receipt'),
    ('IR', 'Internal Receipt Product Movement'),
    ('IS', 'Internal Send Product Movement'),
    ('OD', 'Outbound Delivery')

)


class Operation(models.Model):
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='warehouse_worker')
    created = models.DateField(auto_now=True)
    operation = models.CharField(max_length=50, choices=OPERATION_CHOICES)
    operation_number = models.CharField(max_length=15)
    products = ArrayField(models.CharField(max_length=50), default=[])
    quantities = ArrayField(models.PositiveIntegerField(), default=[])


    def __str__(self):
        return self.operation_number

    def get_api_url(self, request=None):
        return reverse('operation-detail', kwargs={'id': self.id}, request=request)
