from django.urls import path
from .views import LoginRegister, log_out, user_dashbord

urlpatterns = [
    path('', LoginRegister.as_view(), name='login_register_page'),
    path('logout', log_out, name='logout_page'),
    path('dashbord', user_dashbord, name='dashbord_page'),
]
