from django.contrib import admin
from django.urls import path
from product.views import *

urlpatterns = [
    path('api/v1/category', get_category_list),
    path('api/v1/category/<int:id>', get_category),

    path('api/v1/products', get_products_list),
    path('api/v1/products/<int:id>', get_product),

    path('api/v1/reviews', get_reviews_list),
    path('api/v1/reviews/<int:id>', get_review)

]
