from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from product.serializers import *
from product.models import *


@api_view(['GET'])
def get_products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_reviews_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)
@api_view(['GET'])
def get_product(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(data=serializer.data)

@api_view(['GET'])
def get_review(request, id):
    review = get_object_or_404(Product, id=id)
    serializer = ReviewSerializer(review, many=False)
    return Response(data=serializer.data)

@api_view(['GET'])
def get_category(request, id):
    category = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(category, many=False)
    return Response(data=serializer.data)

