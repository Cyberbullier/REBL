from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    # fieldsets change the layout of admin add and change pages
    fieldsets = [
    ('Product',{'fields':['product'],}),
    ('Quantity',{'fields':['quantity'],}),
    ('Price',{'fields':['price'],}),
    ]
    readonly_fields = ['product','quantity','price']
    # disables ability to delete order items in backend, eg. in Admin
    can_delete= False
    # disables ability to add items to orders and removes all empty row/columns
    # in admin view for the specific page
    max_num = 0
    # edited default template in order to delete duplicate name that appeared
    template = 'admin/order/tabular.html'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','billing_name','email','creation_date']
    list_display_links = ('id','billing_name')
    search_fields = ['id','billing_name','email']
    readonly_fields = ['id','token','total','email','creation_date','billing_name','billing_address1','billing_city',
                    'billing_postalcode','billing_country','shipping_name','shipping_address1','shipping_city','shipping_postalcode','shipping_country']
    fieldsets = [
    ('ORDER INFORMATION',{'fields': ['id','token','total','creation_date']}),
    ('BILLING INFORMATION', {'fields': ['billing_name','billing_address1','billing_city','billing_postalcode','billing_country','email']}),
    ('SHIPPING INFORMATION', {'fields': ['shipping_name','shipping_address1','shipping_city','shipping_postalcode','shipping_country']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

# can't delete orders in backend
def has_delete_permission(self, request, obj=None):
    return False

# can't add to orders/add new orders in backend
def has_add_permission(self, request):
    return False
