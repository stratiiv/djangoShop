from django.shortcuts import render
from .models import Product
# Create your views here.

def get_product_list(request):
    queryset = Product.objects.all()
    return render(request,'shop/product_list.html',{'product_list':queryset})