import django_filters
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import generic
from .models import Product
from .forms import OrderForm
from rest_framework.views import APIView
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
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

class CreateOrder(APIView):
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,HTTP_201_CREATED)
        return Response(serializer.errors,HTTP_400_BAD_REQUEST)

