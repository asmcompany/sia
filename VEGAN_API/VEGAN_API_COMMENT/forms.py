from django.forms import ModelForm
from .models import Comment


class CommentModelForm(ModelForm):
    
    class Meta:
        fields = ['user', 'user_email', 'body', 'rating']
        model  = Comment

        