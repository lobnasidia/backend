from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    tabs = [
        (
            _("General"),
            {
                "fields": ("form", "designation", "name", "quote"),
            },
        ),
    ]
