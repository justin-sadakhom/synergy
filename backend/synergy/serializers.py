from rest_framework import serializers
from .models import Business, Product


class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ('name', 'country', 'industry', 'postal_code', 'website')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'quantity', 'cost')
