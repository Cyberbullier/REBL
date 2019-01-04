from django.urls import path
from . import views
from .views import HomeView

app_name = 'shop'
urlpatterns = [
    path('', views.entire_product_listing, name='index'),
    path('<slug:c_slug>/', views.entire_product_listing, name='productsbycategory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_description, name='productdetail'),
]
