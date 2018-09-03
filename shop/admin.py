from django.contrib import admin
from .models import Season, Category, Product

# Register your models here.


class Season_admin(admin.ModelAdmin):
    """
    admin authorization for model
    """
    list_display = ['name', 'slug', 'image', 'season_available', 'description']
    prepopulated_fields = {'slug':('name', )}
    list_editable = ['description']


admin.site.register(Season, Season_admin)

class Category_admin(admin.ModelAdmin):
    """
    admin authorization to model
    """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name', )}


admin.site.register(Category, Category_admin)

class Product_admin(admin.ModelAdmin):
    """
    admin authorization to model
    """
    list_display = ['name', 'slug', 'description', 'price', 'date_created', 'date_latest_update', 'product_available']
    # can't edit fields that you put in the other classes list_editable, maybe change field name?

    prepopulated_fields = {'slug':('name', )}


admin.site.register(Product, Product_admin)
