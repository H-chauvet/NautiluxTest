from django.db import models


# Category model
# Here, we need to define all the fields we'll need for the Category model
class Category(models.Model):
    """
    Category model with required fields
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


# Product model
# Here, we need to define all the fields we'll need for the Product model
class Product(models.Model):
    """
    Product model with required fields
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    product_url = models.URLField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
