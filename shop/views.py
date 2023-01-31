import django_filters
from django.shortcuts import render
from django.urls import reverse
from .models import Product
# Create your views here.

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name','price','category']

def get_product_list(request):
    f = ProductFilter(request.GET,queryset=Product.objects.all())
    queryset = Product.objects.all()
    return render(request,'shop/product_list.html',{'product_list':queryset,'filter':f})


def get_filtered_product_list(request):
    f = ProductFilter(request.GET,queryset=Product.objects.all())
    return render(request,'shop/filtered_products.html',{'filter':f})