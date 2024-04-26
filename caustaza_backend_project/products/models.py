from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    name_project = models.CharField(_("form"), max_length=100)
    description = models.CharField(_("subtitle"), max_length=255, blank=True)
    released_date = models.DateField()
    image = models.ImageField(_("image"), upload_to="feedbacks")

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedback")

    def __str__(self):
        return self.form
