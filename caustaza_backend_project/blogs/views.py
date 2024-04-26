from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(publish=1)
    lookup_field = "slug"
