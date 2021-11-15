"""fast_trading_and_engineering_bd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from core.models import Product
from fast_trading_and_engineering_bd import settings

info_dict = {
    'queryset': Product.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'sitemaps': GenericSitemap(info_dict, priority=0.9)}},
         name='django.contrib.sitemaps.views.sitemap'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
