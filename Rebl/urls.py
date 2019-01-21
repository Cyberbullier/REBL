"""Rebl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from shop import views
from django.conf import settings
from django.conf.urls.static import static


# Routers provide an easy way of automatically determining the URL conf.


app_name = 'Rebl'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('shopapi.urls')),
    path('shop/', include('shop.urls')),
    path('imagefit/', include('imagefit.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
