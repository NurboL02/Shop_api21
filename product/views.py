from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from product.serializers import *
from product.models import *


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def get_products_list(request):
#    products = get_object_or_404(Product, id=id)
#    if request.method == 'GET':
#        serializer = ProductSerializer(products)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        serializer = ProductSerializer(products, data=request.data)
#      if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#   elif request.method == 'DELETE':
#       products.delete()
#      return Response(status=status.HTTP_204_NO_CONNECT

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# @api_view(['GET', 'POST'])
# def get_category_list(request):
#   if request.method == 'GET':
#       category = Category.objects.all()
#      serializer = CategorySerializer(category, many=True).data
#     return Response(data=serializer, status=status.HTTP_200_OK)
# elif request.method == "POST":
#   serializers = CategorySerializer(data=request.data)
#  if serializers.is_valid():
#     serializers.save()
#    return Response(serializers.data)
# return Response(serializers.errors)
class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
# @api_view(['GET','POST'])
# def get_reviews_list(request):
#   if request.method == 'GET':
#      review = Review.objects.all()
#     serializer = ReviewSerializer(review, many=True)
#    return Response(serializer.data)
# elif request.method == 'POST':
#     serializer = ReviewSerializer(data=request.data)
#    if serializer.is_valid():
#        serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def get_product(request, id):
#   if request.method == "GET":
#      product = Product.objects.all()
#     serializer = ProductSerializer(product, many=True)
#    return Response(serializer.data)
# elif request.method == "POST":
#   serializer = ProductSerializer(data=request.data)
#  if serializer.is_valid():
#     serializer.save()
#    return Response(serializer.data, status=status.HTTP_201_CREATED)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def get_review(request, id):
#   review = get_object_or_404(Review, id=id)
#  if request.method == 'GET':
#      serializer = ReviewSerializer(review)
#      return Response(serializer.data)
# elif request.method == 'PUT':
#    serializer = ReviewSerializer(review, data=request.data)
#   if serializer.is_valid():
#      serializer.save()
#     return Response(serializer.data)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# elif request.method == 'DELETE':
#   review.delete()
#  return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def get_category(request, id):
#   category = get_object_or_404(Product, id=id)
#  if request.method == 'GET':
#     serializer = CategorySerializer(category, many=False)
#    return Response(serializer.data)
# elif request.method == 'PUT':
# serializer = CategorySerializer(category, data=request.data)
#   if serializer.is_valid():
#      serializer.save()
#     return Response(serializer.data)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# elif request.method == 'DELETE':
#   category.delete()
#  return Response(status=status.HTTP_204_NO_CONTENT)
