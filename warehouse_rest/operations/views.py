from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import OperationSerializer
from .models import Operation
from warehouse.models import SemiFinishedItem
from django.utils.timezone import now


class OperationDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = Operation
    serializer_class = OperationSerializer
    queryset = Operation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class OperationList(generics.ListCreateAPIView):

    serializer_class = OperationSerializer

    def get_queryset(self):
        return Operation.objects.all()

    def find_operation_number(self, operation):

        operation_count =  Operation.objects.filter(operation=operation).filter(created__year=now().year).count()
        return '{}/{}/{}'.format(operation, operation_count, now().year)

    def perform_create(self, serializer):
        serializer.save(worker=self.request.user)
        operation = serializer.validated_data['operation']
        operation_number = self.find_operation_number(operation)
        serializer.save(operation_number=operation_number)

        items_list = serializer.validated_data['products']
        quanities_list = serializer.validated_data['quantities']

        self.actualize_items_quantity(items_list, quanities_list, operation)


    def actualize_items_quantity(self, items_list, quantities_list, operation):
        for (item_id, quantity) in zip(items_list, quantities_list):
            edit_item = SemiFinishedItem.objects.get(id=int(item_id))
            if operation == 'ER' or operation == 'IR':
                edit_item.quantity -= quantity
            else:
                edit_item.quantity += quantity
            edit_item.save()

    permission_classes = [permissions.AllowAny]
