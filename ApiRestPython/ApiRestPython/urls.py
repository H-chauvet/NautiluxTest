"""ApiRestPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myApp.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'Category', CategoryViewSet)
router.register(r'Product', ProductViewSet)

# Here, its the URL for endpoints, list, create, retrieve, update, delete with the correct http request (GET, POST, PUT, DELETE)
urlpatterns = [
    path('Category/<int:pk>/retrieve/', CategoryViewSet.as_view({'get': 'retrieve'}), name='category-detail'),
    path('Product/<int:pk>/retrieve/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
    path('Category/<int:pk>/update/', CategoryViewSet.as_view({'put': 'update'}), name='category-detail'),
    path('Product/<int:pk>/update/', ProductViewSet.as_view({'put': 'update'}), name='product-detail'),
    path('Category/<int:pk>/delete/', CategoryViewSet.as_view({'delete': 'destroy'}), name='category-delete'),
    path('Product/<int:pk>/delete/', ProductViewSet.as_view({'delete': 'destroy'}), name='product-delete'),
    path('Category/create/', CategoryViewSet.as_view({'post': 'create'}), name='category_create'),
    path('Product/create/', ProductViewSet.as_view({'post': 'create'}), name='product_create'),
    path('Category/', CategoryViewSet.as_view({'get': 'list'}), name='category-list'),
    path('Product/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
