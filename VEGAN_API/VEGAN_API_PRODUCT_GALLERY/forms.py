from VEGAN_API.VEGAN_API_PRODUCT.models import Product
from django import forms
from .models import ProductGallery


class ProductGalleryModelForm(forms.ModelForm):
    
    
    class Meta:
        model = ProductGallery
        fields = '__all__'
