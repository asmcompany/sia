
from VEGAN_API.VEGAN_API_COMMENT.models import Comment
from django.contrib import admin

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering      = ['-timestamp']
    list_editable = ['is_offensive']
    list_display  = ['body', 'product', 'is_offensive']
    list_filter   = ['timestamp']
    list_per_page = 20