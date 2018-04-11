from rest_framework import serializers
from .models import Operation, Cart
from django.contrib.auth.models import User


class OperationSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Operation

        fields = [
            'id',
            'url',
            'worker',
            'created',
            'operation',
            'operation_number',
            'products',
            'quantities',
        ]
        read_only_fields = ['url', 'worker', 'created', 'operation_number']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)


class CartSerializer(serializers.ModelSerializer):
    worker = serializers.ReadOnlyField(source='worker.username')
    class Meta:
        model = Cart

        fields = [
            'id',
            'worker',
            'products',
            'quantities',
        ]

    def get_operation(self):
        return True



class UserSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'cart'
        ]
        read_only_field = ['cart']

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def get_cart(self, obj):
        print(Cart.objects.filter(worker__id=obj.id).values('worker'))
        return Cart.objects.filter(worker__id=obj.id).values_list('products', 'quantities')