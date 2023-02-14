from django.db import models

# Category model
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


# Product model
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    product_url = models.URLField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)