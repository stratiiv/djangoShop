import django_filters
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import generic
from .models import Product
from .forms import OrderForm
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

class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('create-order')
    else:
        form = OrderForm()
        return render(request,'shop/create_order.html',{'form':form})

