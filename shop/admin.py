from django.contrib import admin
from .models import Product,Category,Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','user','category')
    list_filter = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','email','product','price','category')
    @admin.display
    def price(self,obj):
        return obj.product.price
    @admin.display
    def category(self,obj):
        return obj.product.category 

admin.site.register(Category)