from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Category, Product


class CategoryTests(APITestCase):
    def test_create_category(self):
        """
        Test that we can create a category
        """
        url = reverse("category-create")
        data = {"id": 1, "name": "test_category"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "test_category")

    def test_retrieve_category(self):
        """
        Test that we can retrieve a category
        """
        category = Category.objects.create(id=1, name="Category1")
        url = reverse("category-detail", args=[category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# New class to prevent problems with product/category objects creation
class CategoryTest2(APITestCase):
    def setUp(self):
        """
        Setup a new category
        """
        self.category = Category.objects.create(id=1, name="Test Category")

    def test_update_category(self):
        """
        Test that we can update a category
        """
        url = reverse("category-detail", args=[self.category.id])
        data = {"id": 1, "name": "New Category Name"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "New Category Name")

    def test_delete_category(self):
        """
        Test that we can delete a category
        """
        response = self.client.delete(f"/Category/{self.category.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())


class ProductTests(APITestCase):
    def setUp(self):
        """
        Setup a new product
        """
        self.category = Category.objects.create(name="TestCategory", id=1)
        self.valid_payload = {
            "id": 1,
            "name": "TestProduct",
            "product_url": "http://example.com",
            "price": 10.0,
            "category": self.category.id,
        }
        self.invalid_payload = {
            "name": "",
            "product_url": "http://example.com",
            "price": 10.0,
            "category": self.category.id,
        }

    def test_create_valid_product(self):
        """
        Test that we can create a valid product
        """
        url = reverse("product-create")
        response = self.client.post(url, data=self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "TestProduct")

    def test_create_invalid_product(self):
        """
        Test that we can't create an invalid product
        """
        url = reverse("product-create")
        response = self.client.post(url, data=self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_retrieve_product(self):
        """
        Test that we can retrieve a product
        """
        product = Product.objects.create(
            id=1,
            name="Product1",
            product_url="http://example.com/product1",
            price=10.99,
            category=self.category,
        )
        url = reverse("product-detail", args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """
        Test that we can update a product
        """
        category = Category.objects.create(id=2, name="Test Category")
        product = Product.objects.create(
            id=1,
            name="Test Product",
            product_url="https://example.com",
            price=10,
            category=category,
        )
        url = reverse("product-detail", kwargs={"pk": product.pk})
        data = {
            "id": 1,
            "name": "Updated Product",
            "product_url": "https://example.com/updated",
            "price": 20,
            "category": category.pk,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, "Updated Product")
        self.assertEqual(product.product_url, "https://example.com/updated")
        self.assertEqual(product.price, 20)
        self.assertEqual(product.category, category)


# New class to prevent problems with product/category objects creation
class ProductTest2(APITestCase):
    def setUp(self):
        """
        Setup a new category
        """
        self.category = Category.objects.create(name="Test Category", id=1)
        self.product = Product.objects.create(
            id=1,
            name="Test Product",
            product_url="http://test-product.com",
            price=10,
            category=self.category,
        )
        self.url = reverse("product-detail", kwargs={"pk": self.product.pk})

    def test_delete_product(self):
        """
        Test that we can delete a product
        """
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())
