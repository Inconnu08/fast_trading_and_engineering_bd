from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import *


admin.site.site_header = "FAST TRADING & ENGINEERING BD Control Admin"
admin.site.site_title = "FAST TRADING & ENGINEERING BD Admin Portal"
admin.site.index_title = "Welcome to FAST TRADING & ENGINEERING BD Portal 😀"


class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'model', 'created', 'updated']
    # list_editable = ['available']
    search_fields = ['name', 'created']
    # prepopulated_fields = {'slug': ('name',)}
    list_per_page = 30


admin.site.register(Product, ProductAdmin)
