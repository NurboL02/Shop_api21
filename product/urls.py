from django.contrib import admin
from django.urls import path
from product.views import *
from product.views import CategoryView, ProductView, ReviewView

urlpatterns = [
    path('api/v1/category', CategoryView.as_view({"get":"list", "post":"create"})),
    path('api/v1/category/<int:pk>', CategoryView.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})),

    path('api/v1/products',ProductView.as_view({"get":"list", "post":"create"})),
    path('api/v1/products/<int:pk>', ProductView.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})),

    path('api/v1/reviews', ReviewView.as_view({"get":"list","post":"create"})),
    path('api/v1/reviews/<int:pk>',ReviewView.as_view({"get":"retrieve", "put":"update", "delete":"destroy"}) )

]
