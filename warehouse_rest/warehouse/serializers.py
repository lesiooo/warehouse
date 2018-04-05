from rest_framework import serializers
from warehouse.models import SemiFinishedItem, FinishedProduct


class SemiFinishedItemSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SemiFinishedItem
        fields = [
            'url',
            'id',
            'name',
            'producer',
            'quantity',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_absolute_url(request=request)


class FinishedProductSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FinishedProduct
        fields = [
            'url',
            'name',
            'price',
            'quantity',
            'ean_code',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_absolute_url(request=request)