from rest_framework import serializers
from .models import Category, Product

# Serializer for Category data
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  ['id', 'name']


# Serializer for Category data
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_url', 'category', 'price']