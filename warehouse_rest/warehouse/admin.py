from django.contrib import admin
from .models import FinishedProduct, SemiFinishedItem


class FinishedProductAdmin(admin.ModelAdmin):
    fields = ('name', 'ean_code', 'quantity', 'price')
admin.site.register(FinishedProduct,FinishedProductAdmin)


class SemiFinishedItemAdmin(admin.ModelAdmin):
    fields = ('name', 'quantity','producer',)
admin.site.register(SemiFinishedItem,SemiFinishedItemAdmin)


# Register your models here.
