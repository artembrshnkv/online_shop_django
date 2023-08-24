from rest_framework import serializers

from .models import Goods


class GoodsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        # fields = '__all__'
        fields = ('title', 'description', 'price')
