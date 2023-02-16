from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myApp.views import CategoryViewSet, ProductViewSet


# Here, it's the 2 differents defaults routes (Category and Product)
router = DefaultRouter()
router.register(r"Category", CategoryViewSet)
router.register(r"Product", ProductViewSet)

# Here, it's the URL for endpoints, list, create, retrieve, update, delete with the correct http request (GET, POST, PUT, DELETE)

# There is one thing i can't fix -> the route /category/list | /product/list to see the see the list of categories or products
# Actually, we can see the list with the default route : /Category/ or /Product/

urlpatterns = [
    path(
        "Category/<int:pk>/retrieve/",
        CategoryViewSet.as_view({"get": "retrieve"}),
        name="category-detail",
    ),
    path(
        "Product/<int:pk>/retrieve/",
        ProductViewSet.as_view({"get": "retrieve"}),
        name="product-detail",
    ),
    path(
        "Category/<int:pk>/update/",
        CategoryViewSet.as_view({"put": "update"}),
        name="category-detail",
    ),
    path(
        "Product/<int:pk>/update/",
        ProductViewSet.as_view({"put": "update"}),
        name="product-detail",
    ),
    path(
        "Category/<int:pk>/delete/",
        CategoryViewSet.as_view({"delete": "destroy"}),
        name="category-delete",
    ),
    path(
        "Product/<int:pk>/delete/",
        ProductViewSet.as_view({"delete": "destroy"}),
        name="product-delete",
    ),
    path(
        "Category/create/",
        CategoryViewSet.as_view({"post": "create"}),
        name="category_create",
    ),
    path(
        "Product/create/",
        ProductViewSet.as_view({"post": "create"}),
        name="product_create",
    ),
    path(
        "Category/",
        CategoryViewSet.as_view({"get": "list"}),
        name="category-list",
    ),
    path(
        "Product/",
        ProductViewSet.as_view({"get": "list"}),
        name="product-list",
    ),
    path(
        "",
        include(router.urls)
    ),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework")
    ),
]
