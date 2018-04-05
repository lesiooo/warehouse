from django.contrib import admin
from .models import Operation

class OperationAdmin(admin.ModelAdmin):
    fields = ('worker', 'operation', 'operation_number')

admin.site.register(Operation, OperationAdmin)

# Register your models here.
