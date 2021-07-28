from VEGAN_API.VEGAN_API_BRAND.models import Brand
from django.contrib import admin

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass