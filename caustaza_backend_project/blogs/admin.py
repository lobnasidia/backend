from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Blog, Tag, User


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.title


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
