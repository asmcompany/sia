from VEGAN_API.VEGAN_API_CART.models import Cart, CartOrderDetail
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from VEGAN_API.VEGAN_API_ACCOUNT.forms import UserLoginForm, UserModelForm, UserRegisterForm
from utils import querry_debuger


# =======  LOG-IN or REGISTER users ============
class LoginRegister(View):

    def get(self, *args, **kwargs):

        # restrict authenticated users from accsessing this page
        if self.request.user.is_authenticated : 
            try   : return redirect(self.request.GET['next'])
            except: return redirect(self.request.META.get('HTTP_REFERER'))


        signup_form = UserRegisterForm()
        login_form  = UserLoginForm()

        context = {
            'signup_form' : signup_form,
            'login_form'  : login_form,
        }
        return render(self.request, 'login_or_register.html', context)
    



    # "login" or "signup"
    # check against the only field that differs between login and signup form -> password_2.
    def post(self, *args, **kwargs):
        
        # restrict authenticated users from accsessing this page
        if self.request.user.is_authenticated : 
            try   : return redirect(self.request.GET['next'])
            except: return redirect('/')



        # initial form instances
        login_form   = UserLoginForm    () 
        signup_form  = UserRegisterForm ()


        # ==== SIGN-IN ====
        if 'username' in self.request.POST:
            login_form   = UserLoginForm(data=self.request.POST) 

            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['user_password']
                user = authenticate(self.request, username=username, password=password)

                if user:
                    login(self.request, user=user)
                    try    : return redirect(self.request.GET['next']) # @login_required decorator querry parameter
                    except : return redirect('/')
                else :login_form.add_error('username', 'کاربری با مشخصات وارد شده یافت نشد')
            else :login_form.add_error('username', 'اطلاعات وارد شده صحیح نیست')


        # ==== SIGN-UP ====
        if 'user_email' in self.request.POST:
            signup_form  = UserRegisterForm(data=self.request.POST)
            if signup_form.is_valid():
                
                username = signup_form.cleaned_data['user_email']
                password = signup_form.cleaned_data['user_password']
                try:
                    user = get_user_model().objects.create_user(username=username , password=password)
                    user.save()
                    login(self.request, user)
                    try    : return redirect(self.request.GET['next']) # @login_required decorator querry parameter
                    except : return redirect('/')
                except: signup_form.add_error('user_email', 'این کاربر قبلا ثبت نام کرده')
            else: signup_form.add_error('user_email', 'اطلاعات وارد شده صحیح نیست لطفا دوباره تلاش کنید')
                
        
        context = {
            'signup_form' : signup_form,
            'login_form'  : login_form,
        }

        return render(self.request, 'login_or_register.html', context)

# ===== LOG-OUT View ======
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        try    : return redirect(request.META.get('HTTP_REFERER'))
        except : return redirect('/')
    else: return redirect('/')



# ======== USER DASHBORD =========
@querry_debuger
@login_required
def user_dashbord(request:HttpRequest):

    # instances
    user  = request.user
    cart  = Cart.get_cart_or_create_cart(user)
    cart_objects = cart.cartorderdetail_set.select_related('orderd_item')
    
    # form instances
    account_form = UserModelForm(instance=request.user)

    # User personal info change
    if set(account_form.Meta.fields).issubset(set(request.POST.keys())):
        account_form = UserModelForm(data=request.POST, instance=user)
        if account_form.is_valid():
            account_form.save()
        else: print('*'*300)
    
    

    context = {
        'info_form'   : account_form,
        'user_orders' : cart_objects,
        'cart_subtotal'  : cart.get_cart_subtotal(),
        'cart_total'  : cart.get_cart_total(),
    }
    return render(request, 'dashbord.html', context)

