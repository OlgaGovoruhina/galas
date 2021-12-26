from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from shop.models import Category, Product, ProductImage
from shop.serializers import CategorySerializer, ProductSerializer


def index(request):
    return render(request, 'index.html')


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def products_list(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {'category': category, 'products': products})


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product=product)
    return render(request, 'product_details.html', {'product': product, 'images': images})


# API

class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
