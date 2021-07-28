# django authentication
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UsernameField

# raw django form widgets & fields
from django.forms import Form
from django.forms.fields import CharField, EmailField
from django.forms.models import ModelForm
from django.forms.widgets import EmailInput, PasswordInput, TextInput


# made this custom form so i can run custom validations
# ===== User Change Form For Admin ======
class MyUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
        field_classes = {'username': UsernameField}



class UserModelForm(ModelForm):
    class Meta:
        model   = get_user_model()
        fields  = ['first_name', 'last_name', 'email', 'adress', 'phone_number', 'postal_code']
        labels  = {
            'first_name'   : ' نام '           ,
            'last_name'    : ' نام خانوادگی ' ,
            'email'        : ' ایمیل '         ,
            'adress'       : ' آدرس '          ,
            'phone_number' : ' تلفن همراه '    ,
            'postal_code'  : ' کد پستی '       ,
        }
        widgets = {
            'first_name'   :  TextInput (attrs={'class':'txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-20 focus1', 'placeholder':''}),
            'last_name'    :  TextInput (attrs={'class':'txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-20 focus1', 'placeholder':''}),
            'email'        :  EmailInput(attrs={'class':'txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-20 focus1 non-editable-field', 'placeholder':'example@gmail.com', 'readonly':''}),
            'adress'       :  TextInput (attrs={'class':'txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-20 focus1', 'placeholder':'ایران - طهران - مدان امام خمینی - خیابان گلزار - کوچه شهیدی - پلاک 2'}),
            'phone_number' :  TextInput (attrs={'class':'txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-20 focus1', 'placeholder':'+98 912 345 8675 مثال :'}),
            'postal_code'  :  TextInput (attrs={'class':'txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-20 focus1', 'placeholder':'کد پستی ده رقمی'}),
        }

    def clean_phone_number(self):
        data = self.cleaned_data["phone_number"]

        # if blank
        if len(data) == 0:
            return data
        elif not data.startswith('+98'):
            self.add_error('phone_number', 'باید با +98 شروع بشه')
        
        # if default (+98)
        elif (len(data) == 3):
            return data
        
        # length validation
        elif len(data) < 13:
            self.add_error('phone_number', 'تلفن درست نیست')
            self.add_error('phone_number', 'مثال درست : +98 939 005 2349')
        
        return data


# ====== LOG-IN FORM =========
class UserLoginForm(Form):

    username = EmailField(label='ایمیل', label_suffix=None, widget=EmailInput(attrs={
        "class" : "txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-15 focus1",
        "placeholder" : "ایمیل خود را وارد کنید (مثال : example@gmail.com)",
    }))
    # TODO: set  the min length to 8
    user_password = CharField(label='رمز عبور', label_suffix=None, widget=PasswordInput(attrs={
        "class" : "txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-15 focus1",
    }))



# ====== REGISTER FORM =========
class UserRegisterForm(Form):


    user_email = EmailField(label='ایمیل', label_suffix=None, widget=EmailInput(attrs={
        "class"       : "txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-15 focus1",
        "placeholder" : "ایمیل خود را وارد کنید (مثال : example@gmail.com)",
    }))


    user_password = CharField(label='رمز عبور', label_suffix=None, min_length=8,
        widget=PasswordInput(attrs={
        "class" : "txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-15 focus1",
        "placeholder" : "حداقل 8 کاراکتر",
        })
    )


    user_password_2 = CharField(label='تایید رمز عبور', label_suffix=None, min_length=8,
        widget=PasswordInput(attrs={
        "class" : "txt-s-120 cl3 size-a-21 bo-all-1 bocl15 p-rl-15 focus1",
        })
    )



    def clean_user_password_2(self):
        data = self.cleaned_data["user_password_2"]
        if data == self.cleaned_data.get('user_password'):
            return data
        else: 
            self.add_error('user_password', 'رمز های وارد شده یکسان نیستند')
            self.add_error('user_password_2', 'رمز های وارد شده یکسان نیستند')
    