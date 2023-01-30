from django.contrib import admin
from .models import Product,Category,Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','user','category')
    list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','product','get_price')

    @admin.display
    def get_price(self,obj):
        return obj.product.price

admin.site.register(Category)