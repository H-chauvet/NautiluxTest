from rest_framework import serializers
from .models import Category, Product


# Serializer for Category data
# For the category we need an id (Also for the link with product) and a name
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


# Serializer for Category data
# For the product we need an id, a name, a product_url, the category assigned to the product and the price
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ["id", "name", "product_url", "category", "price"]
