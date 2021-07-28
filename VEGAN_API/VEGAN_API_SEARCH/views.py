# django imports
from django.http.request import HttpRequest
from django.shortcuts import render

# my imports
from VEGAN_API.VEGAN_API_PRODUCT.models import Product
from utils import sort_maker


def search(request:HttpRequest):

    
    # search products
    get = request.GET.dict()
    products = Product.search(get['q'], sort_maker(get))
    
    # search in blog

    
    
    context = {
        'products' : products
    }
    return render(request, 'search.html', context)