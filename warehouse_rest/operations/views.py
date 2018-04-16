from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import OperationSerializer, CartSerializer, UserSerializer
from .models import Operation, Cart
from warehouse.models import SemiFinishedItem
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .permissions import IsOwnerOrReadOnly
from rest_framework.request import Request


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
        return '{}/{}/{}'.format(operation, operation_count+1, now().year)

    def perform_create(self, serializer):
        print('ok')
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


class CartDetail(generics.RetrieveUpdateAPIView):

    lookup_field = 'worker__username'
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(worker=user)
        return queryset

    def patch(self, request, *args, **kwargs):
        operation_list = OperationList()
        products = request.data['products']
        quantities = request.data['quantities']
        operation = request.data['operation']
        operation_number = operation_list.find_operation_number(operation=operation)

        test = Operation(operation=operation, products=products, quantities=quantities, worker=request.user, operation_number=operation_number)
        test.save()
        test_actualization = operation_list.actualize_items_quantity(request.data['products'], request.data['quantities'], 'ER')
        cart = Cart.objects.get(worker=request.user)
        cart.quantities = []
        cart.products = []
        cart.save()
        return Response(status=200)

class UserView(generics.ListCreateAPIView):

    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        # permissions.IsAuthenticated
        permissions.AllowAny
    ]

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)
        username = serializer.validated_data['username']
        print(username)
        user = User.objects.get(username=username)
        user_cart = Cart.objects.create(worker=user)

        return Response()

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.all()
        return queryset





