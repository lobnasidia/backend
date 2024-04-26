from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS = ((0, "Draft"), (1, "Publish"))


class Tag(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(_("email address"), unique=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions " "granted to each of their groups."
        ),
        related_name="blog_users",  # custom related name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="blog_users",  # custom related name
    )


class Blog(models.Model):
    title = models.CharField(_("title"), max_length=200, unique=True)
    slug = models.SlugField(_("slug"), max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(_("image"), upload_to="blogs")
    publish = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
