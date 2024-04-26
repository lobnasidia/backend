from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email", "phone", "subject", "recieved_at")
    search_fields = ("fullname", "email", "phone", "subject", "recieved_at")
