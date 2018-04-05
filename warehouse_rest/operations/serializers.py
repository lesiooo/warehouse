from rest_framework import serializers
from .models import Operation


class OperationSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    #items = serializers.DictField(child=serializers.DecimalField(max_digits=8, decimal_places=2))

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
           # 'items'
        ]
        read_only_fields = ['url', 'worker', 'created', 'operation_number']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
