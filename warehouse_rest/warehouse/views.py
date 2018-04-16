from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, permissions, mixins
from rest_framework import status
from rest_framework.response import Response

from .serializers import SemiFinishedItemSerializer, FinishedProductSerializer
from .models import FinishedProduct, SemiFinishedItem


class SemiFinishedItemList(generics.ListCreateAPIView):
    model = SemiFinishedItem
    serializer_class = SemiFinishedItemSerializer
    queryset = SemiFinishedItem.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]




class SemiFinishedItemDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = SemiFinishedItem
    serializer_class = SemiFinishedItemSerializer
    queryset = SemiFinishedItem.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly

    ]


class FinishedProductList(generics.ListCreateAPIView):
    model = FinishedProduct
    serializer_class = FinishedProductSerializer
    queryset = FinishedProduct.objects.all()
    permission_classes = [
        # permissions.IsAuthenticated
        permissions.AllowAny
    ]


class FinishedProductDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = FinishedProduct
    serializer_class = FinishedProductSerializer
    queryset = FinishedProduct.objects.all()
    permission_classes = [
        # permissions.IsAuthenticated
        permissions.AllowAny
    ]