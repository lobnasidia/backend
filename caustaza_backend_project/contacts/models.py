from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=150)
    recieved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "contacts"

    def __str__(self):
        return self.fullname
