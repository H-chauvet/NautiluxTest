from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# View for Category
# Here, there are all the views for the Category model, it's also called the 'endpoints'
# There is : list, destroy(delete), retrieve and create
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        """
        Function to perform the 'delete' endpoint
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        """
        Function to perform the 'list' endpoint
        """
        queryset = self.filter_queryset(self.get_queryset())
        if "name" in request.GET:
            name = request.GET.get("name")
            queryset = queryset.filter(name__icontains=name)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Function to perform the 'retrieve' endpoint
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Function to perform the 'create' endpoint
        """
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        category = Category(name=data.get("name"))
        category.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


# View for Product
# # Here, there are all the views for the Product model, it's also called the 'endpoints'
# There is : list, destroy(delete), retrieve and create
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Function to perform the 'delete' endpoint
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        """
        Function to perform the 'list' endpoint
        """
        queryset = self.filter_queryset(self.get_queryset())
        if "name" in request.GET:
            name = request.GET.get("name")
            queryset = queryset.filter(name__icontains=name)
        if "category" in request.GET:
            category_id = request.GET.get("category")
            queryset = queryset.filter(category__id=category_id)
        if "price" in request.GET:
            price = request.GET.get("price")
            queryset = queryset.filter(price=price)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Function to perform the 'retrieve' endpoint
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Function to perform the 'create' endpoint
        """
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        price = data.get("price")
        category_id = data.get("category")
        category = Category.objects.get(id=category_id)
        product = Product(
            name=data.get("name"),
            product_url=data.get("product_url"),
            price=price,
            category=category,
        )
        product.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
