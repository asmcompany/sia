# django imports
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# from within the app
from .forms import MyUserChangeForm


@admin.register(get_user_model())
class MyUserAdmin(UserAdmin):

    list_display = ['__str__', 'first_name', 'last_name', 'is_active']

    # grouped items <this will change in future>
    fieldsets = (
        (None,
            {'fields': ('username', 'password')}),

        ('Personal info', 
            {'fields': ('first_name', 'last_name', 'postal_code', 'adress')}),

        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

        ('Important dates', 
            {'fields': ('last_login', 'date_joined')}),
    )

    form = MyUserChangeForm
    




