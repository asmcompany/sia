from django.contrib import admin #django
from .models import TAG          #local


@admin.register(TAG)
class TagModelAdmin(admin.ModelAdmin):
    pass