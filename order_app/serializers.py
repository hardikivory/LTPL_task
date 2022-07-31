
from .models import Order, Product
from rest_framework import serializers
from django.db import models


# Product
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['order', 'category', 'brand', 'name', 'price', 'qty']

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['order']



# Order
class ListOrderSerializer(serializers.ModelSerializer):
    products = ListProductSerializer(many = True)
    class Meta:
        model = Order
        fields = ['id','timestamp','placed','total_price','total_qty', 'products']

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['placed','total_price','total_qty']

    def update(self, instance, validated_data):
        instance.placed = validated_data.get('placed')
        instance.total_price = validated_data.get('total_price')
        instance.total_qty = validated_data.get('total_qty')
        instance.save()

        return instance




