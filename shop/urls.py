from django.urls import path, include
from . import views


# Routers provide an easy way of automatically determining the URL conf.

app_name = 'shop'
urlpatterns = [
    # Uri that conntects to api
    # search urlconfig MUST appear before 'productsbycategory'
    path('shoppingcart/', include('shoppingcart.urls')),
    path('search/', include('search.urls')),
    path('order/', include('order.urls')),
    path('', views.entire_product_listing, name='index'),
    path('<slug:c_slug>/', views.entire_product_listing, name='productsbycategory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_description, name='productdetail'),

]
