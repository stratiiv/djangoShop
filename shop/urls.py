from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('products/',views.get_product_list,name='products'),
    path('products/filter/',views.get_filtered_product_list,name='filter-products'),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name = 'product-detail'),
    path('create-order/',views.create_order,name = 'create-order')
]
