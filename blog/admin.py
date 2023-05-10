from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Registering models.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

