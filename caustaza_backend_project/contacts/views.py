from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Contact
from .serializers import ContactSerializer


class ContactCreateView(CreateModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = (AllowAny,)
