from django.contrib import admin
from .models import Product,Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','user','category')
    list_filter = ('category',)

admin.site.register(Category)