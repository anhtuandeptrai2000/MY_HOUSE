from django.shortcuts import render
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product


# Create your views here.
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results,status = status.HTTP_200_OK)


@api_view(['GET'])
def get_products_with_cached(request):
    if 'product_all' in cache:
        products = cache.get('product_all', {})
        return Response(products, status=status.HTTP_200_OK)
    else:
        products = Product.objects.all()
        result = [product.to_json() for product in products]
        cache.set('product_all', result, timeout =900)
        return Response(result, status=status.HTTP_200_OK)