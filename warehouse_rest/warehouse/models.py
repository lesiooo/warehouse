from django.db import models
from rest_framework.reverse import reverse as api_reverse


class SemiFinishedItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    producer = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self, request=None):
        return api_reverse('semi-finished-item-rud', kwargs={'id': self.id}, request=request)


class FinishedProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.FloatField()
    ean_code = models.CharField(max_length=13, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self, request=None):
        return api_reverse('finished-product-rud', kwargs={'id': self.id}, request=request)

