from django.contrib import admin
from .models import Profile, Post  # Remove Comment from here

admin.site.register(Post)
admin.site.register(Profile)
