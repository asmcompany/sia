from django import forms

# my imports
from .models import Cart, CartOrderDetail
from VEGAN_API.VEGAN_API_PRODUCT.models import Product
from django.core.validators import MinValueValidator

class CartModelForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model  = Cart


class CartOrderDetailModelForm(forms.ModelForm):

    class Meta:
        exclude = ['relative_cart']
        model   = CartOrderDetail
        widgets = {
            'orderd_item_count' : forms.NumberInput(attrs={'class':"txt-m-102 cl6 txt-center num-product"}),
            'orderd_item_price' : forms.HiddenInput(),
            'orderd_item'       : forms.HiddenInput(),
        }

    def clean_orderd_item_count(self):
        orderd_item_count = self.cleaned_data.get('orderd_item_count')
        if orderd_item_count <= 0 :
            self.add_error('orderd_item_count', 'not enough')
        return orderd_item_count
        
