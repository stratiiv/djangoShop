from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('products/',views.get_product_list,name='products'),
    path('products/filter/',views.get_filtered_product_list,name='filter-products'),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name = 'product-detail'),
    path('create-order/',views.create_order,name = 'create-order'),
    path('api/v1/create-order/',views.CreateOrderJQ.as_view(),name='create-order-api')
]

urlpatterns = format_suffix_patterns(urlpatterns)
