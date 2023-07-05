from rest_framework import serializers
from product.models import *


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    name =serializers.CharField(max_length=9)
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=400)
    class Meta:
        model = Review
        fields = '__all__'
