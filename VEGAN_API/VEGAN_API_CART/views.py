# django imports
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http.request import HttpRequest
from django.http.response import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect

# my models
from VEGAN_API.VEGAN_API_CART.models import Cart, CartOrderDetail
from VEGAN_API.VEGAN_API_PRODUCT.models import Product
from VEGAN_API.VEGAN_API_CART.forms import CartOrderDetailModelForm


from utils import querry_debuger

# !!! dont user querry_debuger !!!
@querry_debuger
@login_required(redirect_field_name='HTTP_REFERER') # users cant access this view normally, this is just a percaution
def add_to_cart(request:HttpRequest):

    # recieves encrypted ID and return the <Product> instance with that ID, or `ObjectDoesNotExist`
    def decrypt_product_id_and_return_instance(encrypted_id:str or int):
        dec = int( (int(encrypted_id)) // (100) ) ** (1/5)
        try    : return Product.objects.get(pk=dec)
        except : raise ObjectDoesNotExist('does not exist')


    if request.method == 'POST':

        # get current active CART of user
        # TODO: check if the user is active and return the JSON response or redirect to login
        cart = Cart.get_cart_or_create_cart(request.user)

        # manipulation of request.POST data
        # request.POST is immutable and 'orderd_item' is an encrypted number
        requestData = request.POST.copy().dict()
        requestData['orderd_item'] = decrypt_product_id_and_return_instance(int(requestData.get('orderd_item')))

        # form & instance
        order_instance = CartOrderDetail(relative_cart=cart)
        form = CartOrderDetailModelForm(requestData, instance=order_instance)

        # validate and save
        # this view is accessed though AJAX, and returns JSONResponse
        if form.is_valid():
            form.save()
            response_data = {
                'messege' : 'به سبد خرید اضافه شد'
            }
            return JsonResponse(data=response_data, status=200)
        
        else:
            return JsonResponse(data={'messege' : 'تراکنش معتبر نمیباشد لطفا دوباره امتحان کنید'}, status=400)
        

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

from django.http.response import HttpResponseNotModified
@querry_debuger
def proceed_to_checkout(request):
    
    user = request.user
    cart  = Cart.get_cart_or_create_cart(user)
    cart_objects = cart.cartorderdetail_set.select_related('orderd_item')
    
    if request.method == 'POST':
        POST = request.POST.dict()
        try:
            for order in cart_objects:
                
                order.orderd_item_count = POST.get(str(order.pk))
                order.save(update_fields=['orderd_item_count'])
        except:
            return HttpResponseNotModified()
        
    return redirect(request.META['HTTP_REFERER'])

@querry_debuger
@login_required
def remove_from_cart(request):

    if request.method  == 'POST':

        order_id_encrypted  = request.POST['order_id']
        order_id_decrypted  = CartOrderDetail.decrypt_order_detail_id(order_id_encrypted)
        order_to_be_deleted = CartOrderDetail.objects.get(id=order_id_decrypted)

        if order_to_be_deleted.relative_cart.owner.pk == request.user.pk:
            order_to_be_deleted.delete()
        else : return HttpResponseForbidden()
        return redirect(request.META['HTTP_REFERER'])

    else : return HttpResponseForbidden()