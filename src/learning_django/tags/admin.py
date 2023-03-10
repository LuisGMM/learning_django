from django.contrib import admin

from store.models import Collection, Product, Customer

# Register your models here.

admin.site.register(Collection)

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10

    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):

        if product.inventory < 10:
            return 'Low'
        return 'Ok'


# admin.site.register(Product)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'placed_at', 'customer']