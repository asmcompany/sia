# Django
from VEGAN_API.VEGAN_API_CART.forms import CartOrderDetailModelForm
from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView

# Me
from .models import Product
from utils import querry_debuger
from VEGAN_API.VEGAN_API_COMMENT.forms import CommentModelForm




# === Product List View ===



class ProductListView(ListView):
    model = Product
    template_name = 'product_list_view.html'
    context_object_name = 'products'
    ordering = ['-pk',]
    paginate_by = 2





# === Product Detail View ===
# this page only responds to GET request
# there are total of 2 senarios of POST request -> (order, comment)
# and they are taken care of in their own app
@querry_debuger
def product_detail_view(request, slug, *args, **kwargs):

    if request.method =='POST' : print(request.POST);

    # database querries
    try:   product:Product = Product.objects.get(slug=slug, is_active=True)
    except ObjectDoesNotExist: raise Http404('item does not exist')
    
    
    # forms
    # if user isnt logged in, the form with initial values will break
    # so we except it with no initials, we could do this with (if-else) and check against request.user
    try    :comment_form = CommentModelForm (data=(request.POST or None), initial={'user':request.user.get_full_name(), 'user_email':request.user.username})
    except :comment_form = CommentModelForm (request.POST or None)
    order_form   = CartOrderDetailModelForm (data=(request.POST or None), initial={'orderd_item_price': product.price, 'orderd_item':product.encrypt_post_id()})

    context = {
        'product'        : product,
        'gallery'        : product.get_product_gallery_set(),
        'comments'       : product.get_product_comment_set(),
        'tags'           : product.get_product_tag_set(),
        'comment_form'   : comment_form,
        'order_form'     : order_form,

    }
    return render(request, 'product_detail_view.html', context)
    

