from django.contrib import admin
from .models import Product, Comment, Cart


admin.site.register(Cart)
admin.site.register(Product)

admin.site.register(Comment)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    search_fields = ('name', 'price', 'image')
    list_filter = ('name', 'price', 'image')
    def has_add_permission(self, request):
        return False
