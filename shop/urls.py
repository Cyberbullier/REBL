from django.urls import path, include
from . import views
from .views import HomeView

app_name = 'shop'
urlpatterns = [
    # search urlconfig MUST appear before 'productsbycategory'
    path('shoppingcart/', include('shoppingcart.urls')),
    path('search/', include('search.urls')),
    path('', views.entire_product_listing, name='index'),
    path('<slug:c_slug>/', views.entire_product_listing, name='productsbycategory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_description, name='productdetail'),

]
