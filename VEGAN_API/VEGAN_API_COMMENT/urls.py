
from .views import post_comment
from django.urls import path

urlpatterns = [
    path('post/<str:slug>', post_comment, name='post_comment_page')
]
