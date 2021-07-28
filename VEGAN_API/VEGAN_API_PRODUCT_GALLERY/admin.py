from django.contrib import admin

# relative imports
from .models import ProductGallery



class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1