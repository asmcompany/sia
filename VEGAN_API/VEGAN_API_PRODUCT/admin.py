from VEGAN_API.VEGAN_API_PRODUCT_GALLERY.admin import ProductGalleryInline
from django.contrib import admin
# relative imports
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # brand title shoud be added to this list
    list_display = ['__str__', 'price','inventory', 'views', 'is_active']

    fieldsets = (

        (None, {'fields': ('title', 'price', 'caption')}), 

        ('SEO', {'fields': ('slug',)}), 

        ('عکس', {'fields': ('image',)}), 

        ('توضیحات و اطلاعات تکمیلی', {'fields': ('description', 'specifications')}), 

        ('تعداد موجود در انبار', {'fields': ('inventory',)}), 

        ('بیشتر', {'fields': ('is_active', 'views')}), 

        ('طبقه بندی', {'fields': ('brand', 'tag', 'category')}), 

    )

    inlines = [ProductGalleryInline]